#include <WiFi.h>
#include <PubSubClient.h>


const char* ssid = "S Bera";
const char* pass = "12345678";

const char* mqtt_server = "91.121.93.94";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;
const int ledPin1 = 26;

void setup(){
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  Serial.println("Server is Setted");
  pinMode(ledPin1, OUTPUT);

  client.setCallback(callback);

}

void setup_wifi() {
  
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to : ");
  Serial.print(ssid);
  Serial.println();
  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}




void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();
  if (String(topic) == "opencv") {
    Serial.print("Changing output to ");
    if(messageTemp == "1"){
      Serial.println("Device-1 on");
      digitalWrite(ledPin1, HIGH);
    }
    else if(messageTemp== "0"){
      Serial.println("Device-1 off");
      digitalWrite(ledPin1, LOW);
    }
    

  }
}


void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect(mqtt_server)) {
      Serial.println("connected");
      // Subscribe
      client.subscribe("opencv");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


void loop(){
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}





