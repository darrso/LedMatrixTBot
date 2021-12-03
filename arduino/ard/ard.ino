#define ROW_1 2  
#define ROW_2 3  
#define ROW_3 4   
#define ROW_4 5  
#define ROW_5 6  
#define ROW_6 7  
#define ROW_7 8   
#define ROW_8 9   

#define COL_1 10  
#define COL_2 11   
#define COL_3 12   
#define COL_4 13  
#define COL_5 A0   
#define COL_6 A1   
#define COL_7 A2  
#define COL_8 A3 

int inc;
int i = 0;
byte tu[]={0,0,0,0,0,0,0,0};

const byte rows[] = {
    ROW_1, ROW_2, ROW_3, ROW_4, ROW_5, ROW_6, ROW_7, ROW_8
};

void setColumns(byte b) {
    digitalWrite(COL_1, (~b >> 0) & 0x01);
    digitalWrite(COL_2, (~b >> 1) & 0x01);
    digitalWrite(COL_3, (~b >> 2) & 0x01);
    digitalWrite(COL_4, (~b >> 3) & 0x01);
    digitalWrite(COL_5, (~b >> 4) & 0x01);
    digitalWrite(COL_6, (~b >> 5) & 0x01);
    digitalWrite(COL_7, (~b >> 6) & 0x01);
    digitalWrite(COL_8, (~b >> 7) & 0x01);
}

void  drawScreen(byte buffer2[]){
    for (byte i = 0; i < 8; i++) {
    setColumns(buffer2[i]);
          
    digitalWrite(rows[i], HIGH);
    delay(2);
    digitalWrite(rows[i], LOW);
    }
}

void setup() {

  for (byte i = 2; i <= 13; i++)
  pinMode(i, OUTPUT);
 
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop()
{
while (Serial.available() > 0 && i < 8) 
{ inc = Serial.parseInt(); 
tu[i] = inc; ++i; 
Serial.println(i);
Serial.println(tu[i]);
 }
 if (i == 8){ i = 0;}

drawScreen(tu);
  }
  
