#include <WiFi.h>
#include <driver/ledc.h> // Include this for ESP32 PWM control

// Replace with your network credentials
const char* ssid = "#";
const char* password = "#";

// Set web server port number to 80
WiFiServer server(80);

// Variables to store RGB pin numbers and PWM channels
const int redPin = 26;
const int greenPin = 27;
const int bluePin = 25;

int redValue = 0;
int greenValue = 0;
int blueValue = 0;

// Function to generate HTML content
String generateHTML(int redValue, int greenValue, int blueValue) {
  String html = "<!DOCTYPE html><html><head>"
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
                "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css\">"
                "<style>body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }"
                ".color-preview { width: 100px; height: 100px; margin: 20px auto; border: 1px solid #ccc; }"
                ".button-group { margin: 10px 0; }</style></head><body>"
                "<h1>ESP32 RGB Controller</h1>"
                "<div class=\"color-preview\" style=\"background-color: rgb(" + String(redValue) + "," + String(greenValue) + "," + String(blueValue) + ");\"></div>"
                "<h5>Adjust Colors</h5><div class=\"button-group\">"
                "<label>Red</label>"
                "<a href=\"/-r\" class=\"btn red\">-</a>"
                "<a href=\"/Red\" class=\"btn red lighten-1\">Toggle (" + String(redValue) + ")</a>"
                "<a href=\"/+r\" class=\"btn red\">+</a></div>"
                "<div class=\"button-group\">"
                "<label>Green</label>"
                "<a href=\"/-g\" class=\"btn green\">-</a>"
                "<a href=\"/Green\" class=\"btn green lighten-1\">Toggle (" + String(greenValue) + ")</a>"
                "<a href=\"/+g\" class=\"btn green\">+</a></div>"
                "<div class=\"button-group\">"
                "<label>Blue</label>"
                "<a href=\"/-b\" class=\"btn blue\">-</a>"
                "<a href=\"/Blue\" class=\"btn blue lighten-1\">Toggle (" + String(blueValue) + ")</a>"
                "<a href=\"/+b\" class=\"btn blue\">+</a></div>"
                "</body></html>";
  return html;
}

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();

  // Configure PWM channels
  ledcSetup(0, 5000, 8);  // Channel 0, 5 kHz, 8-bit resolution
  ledcSetup(1, 5000, 8);  // Channel 1, 5 kHz, 8-bit resolution
  ledcSetup(2, 5000, 8);  // Channel 2, 5 kHz, 8-bit resolution

  // Attach PWM channels to pins
  ledcAttachPin(redPin, 0);
  ledcAttachPin(greenPin, 1);
  ledcAttachPin(bluePin, 2);
}

void loop() {
  WiFiClient client = server.available();  // Listen for incoming clients

  if (client) {  // If a new client connects
    Serial.println("New Client.");
    String currentLine = "";  // Make a String to hold incoming data from the client
    String header = "";       // Variable to store the HTTP request header

    while (client.connected()) {  // Loop while the client is connected
      if (client.available()) {  // If there's bytes to read from the client
        char c = client.read();  // Read a byte
        header += c;
        if (c == '\n') {  // If the byte is a newline character
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g., HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();

            // RGB control logic
            if (header.indexOf("GET /-r") >= 0) redValue = max(0, redValue - 1);
            else if (header.indexOf("GET /+r") >= 0) redValue = min(255, redValue + 1);
            else if (header.indexOf("GET /+g") >= 0) greenValue = min(255, greenValue + 1);
            else if (header.indexOf("GET /-g") >= 0) greenValue = max(0, greenValue - 1);
            else if (header.indexOf("GET /+b") >= 0) blueValue = min(255, blueValue + 1);
            else if (header.indexOf("GET /-b") >= 0) blueValue = max(0, blueValue - 1);
            else if (header.indexOf("GET /Red") >= 0) redValue = (redValue == 0) ? 255 : 0;
            else if (header.indexOf("GET /Green") >= 0) greenValue = (greenValue == 0) ? 255 : 0;
            else if (header.indexOf("GET /Blue") >= 0) blueValue = (blueValue == 0) ? 255 : 0;

            // Update PWM values
            ledcWrite(0, redValue);
            ledcWrite(1, greenValue);
            ledcWrite(2, blueValue);

            // Send HTML response
            client.println(generateHTML(redValue, greenValue, blueValue));
            break;
          } else {
            currentLine = "";  // Clear the currentLine
          }
        } else if (c != '\r') {  // If the character is not a carriage return
          currentLine += c;      // Add it to the currentLine
        }
      }
    }

    // Clear the header and stop the connection
    header = "";
    client.stop();
    Serial.println("Client Disconnected.");
  }
}
