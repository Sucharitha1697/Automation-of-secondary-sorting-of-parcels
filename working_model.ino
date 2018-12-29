char packet_number;
time_t t = now();
int c1=0,c2=0,c3=0,c4=0;
int m1f = 38;
int m1b = 39;
int m2f = 40;
int m2b = 41;
int m3f = 42;
int m3b = 43;
int m4f = 44;
int m4b = 45;
int m5f = 46;
int m5b = 47;
int m1_pwm = 1;
int m2_pwm = 2; 
int m3_pwm = 3;
int m4_pwm = 4;
int m5_pwm = 5;
int m1_state = 0;
int m2_state = 0;
int m3_state = 0;
int m4_state = 0;
int m5_state = 0;
int m1_state_prev = 0;
int m2_state_prev = 0;
int m3_state_prev = 0;
int m4_state_prev = 0;
int m5_state_prev = 0;
void open_all()
{
  digitalWrite(m1f,1); digitalWrite(m1b,0);
  digitalWrite(m2f,1); digitalWrite(m2b,0);
  digitalWrite(m3f,1); digitalWrite(m3b,0);
  digitalWrite(m4f,1); digitalWrite(m4b,0);
  digitalWrite(m5f,0); digitalWrite(m5b,1);
  analogWrite(m1_pwm, 200);
  delay(300);
  analogWrite(m1_pwm, 0);
  analogWrite(m2_pwm, 200);
  delay(300);
  analogWrite(m2_pwm, 0);
  analogWrite(m3_pwm, 200);
  delay(300);
  analogWrite(m3_pwm, 0);
  analogWrite(m4_pwm, 200);
  delay(300);
  analogWrite(m4_pwm, 0);
  analogWrite(m5_pwm, 200);
  delay(300b);
  analogWrite(m5_pwm, 0);
  }

  void codes()
  {
    
    }
  
void setup() 
{
  for(int i=21;i<=33;i++)
   {  
      pinMode(i,OUTPUT);
      digitalWrite(i,LOW); 
   }  
  
  pinMode(18,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(18),codes,RISING);
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);  
  pinMode(12,OUTPUT);
  digitalWrite(12,LOW);  
  pinMode(11,OUTPUT);
  digitalWrite(11,LOW);  
  pinMode(10,OUTPUT);
  digitalWrite(10,LOW);  
  Serial.begin(9600);
  open_all();
}
void check_Status(int state,int forward_pin, int reverse_pin, int state_prev, int pwm)
{
     if(state != state_prev)
     {
         {
           if(state == 1)
           {
            
            digitalWrite(forward_pin,LOW);
            digitalWrite(reverse_pin,HIGH);
            delay(1000);
            digitalWrite(forward_pin,LOW);
            digitalWrite(reverse_pin,LOW);
            
           }
         else
         {
            digitalWrite(forward_pin,HIGH);
            digitalWrite(reverse_pin,LOW);
            delay(1000);
            digitalWrite(forward_pin,LOW);
            digitalWrite(reverse_pin,LOW);
         }
         analogWrite(pwm,255);
    }
  }
}

void generate(int val, int pins)
{
  int i=0;
  for(int j=pins;j<=pins+2;j++)
    digitalWrite(j,LOW);
  while(1)
    {
      int pin = pins + 2 - i ;
      if( val%2 == 1 )
         digitalWrite( pin , HIGH);
       else
          digitalWrite( pin , LOW);
       if(val == 0)
          break;
       val = val /2;
       i++;
    }
    
    
}
/*
 0 ---->  close   and   1 ------>  open
 1 -----> open    and   0  ------> close  FOR MOTOR 5 (upper motor) 
  */
void loop() 
{
  if(Serial.available() > 0)
  {
    packet_number = Serial.read();
    if(packet_number == 'a')          //Left_bottom
    {  
      digitalWrite(13,1);
      c1++;
      c1 = c1%8;
      m1_state = 0; m2_state = 0; m5_state =0;
      check_Status(m1_state, m1f, m1b , m1_state_prev , m1_pwm);
      check_Status(m2_state, m2f, m2b, m2_state_prev , m2_pwm);
      check_Status(m5_state, m5f, m5b, m5_state_prev , m5_pwm);
      m1_state_prev = 0;m2_state_prev = 0;m5_state_prev =0;
      generate(c1,22);
      digitalWrite(13,0);
      
    }
    else if(packet_number == 'b')      //Left_middle
    {
      digitalWrite(12,1);
      c2++;
      c2 = c2%8;
      m1_state = 0;m2_state = 1;m5_state = 0;
      check_Status(m1_state, m1f, m1b , m1_state_prev , m1_pwm);
      check_Status(m2_state, m2f, m2b, m2_state_prev , m2_pwm);
      check_Status(m5_state, m5f, m5b, m5_state_prev , m5_pwm);
      m1_state_prev = 0;m2_state_prev = 1;m5_state_prev =0;
      generate(c2,25);
      digitalWrite(12,0);

     }
     else if(packet_number == 'c')      //Left_top
    {
      digitalWrite(11,1);
      c3++;
      c3 = c3 % 8 ;
      m1_state = 1;m2_state = 0;m5_state = 0;
      check_Status(m1_state, m1f, m1b , m1_state_prev , m1_pwm);
      check_Status(m2_state, m2f, m2b, m2_state_prev , m2_pwm);
      check_Status(m5_state, m5f, m5b, m5_state_prev , m5_pwm);
      m1_state_prev = 1;m2_state_prev = 0;m5_state_prev =0;
      generate(c3,28);
      digitalWrite(11,0);
     
    }
     else if(packet_number == 'd')       //Right_bottom 
    {
      digitalWrite(9,1);
      c4++;
      c4 = c4 % 8 ;
      m5_state = 1; m3_state = 0;m4_state=0;
      check_Status(m5_state, m5f, m5b, m5_state_prev , m5_pwm);
      check_Status(m3_state, m3f, m3b, m3_state_prev , m3_pwm);
      check_Status(m4_state, m4f, m4b, m4_state_prev, m4_pwm);
      m5_state_prev = 1; m3_state_prev = 0;m4_state_prev=0;
      generate(c4,31);
      digitalWrite(9,0);
    }
    else if(packet_number == 'e')        //Right_middle
    {
     
      m5_state = 1; m3_state = 0;m4_state=1;
      check_Status(m5_state, m5f, m5b, m5_state_prev , m5_pwm);
      check_Status(m3_state, m3f, m3b, m3_state_prev , m3_pwm);
      check_Status(m4_state, m4f, m4b, m4_state_prev, m4_pwm);
      m5_state_prev = 1; m3_state_prev = 0;m4_state_prev=1;
   
    }
    else if(packet_number == 'f')         //Right_top 
    {
      m5_state = 1; m3_state = 1;m4_state=0;
      check_Status(m5_state, m5f, m5b, m5_state_prev , m5_pwm);
      check_Status(m3_state, m3f, m3b, m3_state_prev , m3_pwm);
      check_Status(m4_state, m4f, m4b, m4_state_prev, m4_pwm);
      m5_state_prev = 1; m3_state_prev = 1;m4_state_prev=0;
                
    }

    if(c1==7)
    {
      digitalWrite(13,HIGH);
      delay(500);
      digitalWrite(13,LOW);
      delay(500);
      digitalWrite(13,HIGH);
      delay(500);
      digitalWrite(13,LOW);
      delay(500);
      digitalWrite(13,HIGH);
      delay(500);
      digitalWrite(13,LOW);
      delay(500);
      digitalWrite(13,HIGH);
      delay(500);
      digitalWrite(13,LOW);
      delay(500);
      c1=0;
      generate(c1,22);
      }
    if(c2==7)
    {
      digitalWrite(12,HIGH);
      delay(500);
      digitalWrite(12,LOW);
      delay(500);
      digitalWrite(12,HIGH);
      delay(500);
      digitalWrite(12,LOW);
      delay(500);
      digitalWrite(12,HIGH);
      delay(500);
      digitalWrite(12,LOW);
      delay(500);
      digitalWrite(12,HIGH);
      delay(500);
      digitalWrite(12,LOW);
      delay(500);
      c2=0;
      generate(c2,25);
    }
    if(c3==7)
    {
      digitalWrite(11,HIGH);
      delay(500);
      digitalWrite(11,LOW);
      delay(500);
      digitalWrite(11,HIGH);
      delay(500);
      digitalWrite(11,LOW);
      delay(500);
      digitalWrite(11,HIGH);
      delay(500);
      digitalWrite(11,LOW);
      delay(500);
      digitalWrite(11,HIGH);
      delay(500);
      digitalWrite(11,LOW);
      delay(500);
      c3=0;
      generate(c3,28);
      }
    if(c4==7)
    {
      digitalWrite(9,HIGH);
      delay(500);
      digitalWrite(9,LOW);
      delay(500);
      digitalWrite(9,HIGH);
      delay(500);
      digitalWrite(9,LOW);
      delay(500);
      digitalWrite(9,HIGH);
      delay(500);
      digitalWrite(9,LOW);
      delay(500);
      digitalWrite(9,HIGH);
      delay(500);
      digitalWrite(9,LOW);
      delay(500);
      c4=0;
      generate(c4,31);
      }
  }  
Serial.flush();
    
}
