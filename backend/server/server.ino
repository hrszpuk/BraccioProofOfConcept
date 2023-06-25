#include <Braccio.h>
#include <Servo.h>

Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;

int defaultPositions[] = {90, 45, 180, 180, 90, 10};

int M1 = 90;
int M2 = 45;
int M3 = 180;
int M4 = 180;
int M5 = 90;
int M6 = 10;

char* data;
char instruction;
size_t dataLength = 5;
int motor, degrees;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  Braccio.begin();
  pinMode(LED_BUILTIN, LOW);
  data = malloc(dataLength * sizeof(char));
}

void loop() {
  if(Serial.available()) {    
     while (Serial.available()>0){
        Serial.readBytes(data, dataLength);  
        pinMode(LED_BUILTIN, HIGH);

        instruction = data[0];
        motor = data[1] - '0';

        data[0] = '0';
        data[1] = '0';
        degrees = atoi(data);
        
        switch(instruction) {
          case 'S': {
            Braccio.ServoMovement(
              20, 
              defaultPositions[0], 
              defaultPositions[1], 
              defaultPositions[2], 
              defaultPositions[3], 
              defaultPositions[4], 
              defaultPositions[5]
            );
            Serial.print("Valid: Moved to \"safety\" position");
            break;
          }
          case 'R': {
            if (degrees == 999) 
              degrees = defaultPositions[motor];
            else if (0 > degrees || degrees > 180) {
              Serial.print("Error: Invalid Degrees (0 < d < 180)");
              break;
            } 

            if (1 > motor || motor > 6) {
              Serial.print("Error: Invalid Motor Id (0 < m < 7)");
              break;
            }
            
            switch(motor) {
              case 1: M1 = degrees; break;
              case 2: M2 = degrees; break;
              case 3: M3 = degrees; break;
              case 4: M4 = degrees; break;
              case 5: M5 = degrees; break;
              case 6: M6 = degrees; break;
            }
            Braccio.ServoMovement(20, M1, M2, M3, M4, M5, M6);
            break;
          }
          default: Serial.print("Error: Invalid Instruction Byte");
        }
     }
     
    //the serial buffer is over just go to the line (or pass your favorite stop char)               
    Serial.println();
  }
  
  //slows down the visualization in the terminal
  delay(1000);
}
