char x;
double t;
String str1,str;
#include<stdlib.h>
#define EN 10
#define DIR 9
#define PUL 8
void setup() { 
  pinMode(13,OUTPUT);
  pinMode(EN,OUTPUT);
  pinMode(DIR,OUTPUT);
  pinMode(PUL,OUTPUT);
  digitalWrite(13,LOW);
  Serial.begin(9600); 
  Serial.println("initial");          
} 
 
void loop() { 
  while(Serial.available()<=0)
  {}
  delay(2000);
 
  while(Serial.available()>0)
  {
  x=Serial.read();
  str+=x;
  }
  str1=str[1];
  long str2=(str[3]-48)*1000+(str[4]-48)*100+(str[5]-48)*10+(str[6]-48);
  if(str1=="a"){
  rotate_degree(1, str2);
  str.remove(0);
  }
  else if(str1=="b")
    {rotate_degree(0, str2);
    str.remove(0);}
 
} 
void rotate(int ST,bool dir)
{
    if(dir==0)
      digitalWrite(DIR,HIGH);
    else
      digitalWrite(DIR,LOW);
    t=millis();
    while((millis()-t)<2)
    {}
    digitalWrite(ST,HIGH);
    t=millis();
    while((millis()-t)<2)
    {}
    digitalWrite(ST,LOW);  
}
void rotate_degree(bool dir,int n)
{
    float buoc=200.00/360.00*n;
  
    if(dir==1){
      digitalWrite(DIR,HIGH);}
    else
      {digitalWrite(DIR,LOW);}
    for(int i=0;i<buoc;i++)
    {
      t=millis();
      while((millis()-t)<0.5)
      {}
      digitalWrite(PUL,HIGH);
      t=millis();
      while((millis()-t)<0.5)
      {}
      digitalWrite(PUL,LOW);
    }
}
//void quay_mai(bool dir,int n)
//{
//  if(dir==1){
//      digitalWrite(DIR,HIGH);}
//    else
//      {digitalWrite(DIR,LOW);}
//  while(1)
//  {
//      t=millis();
//      while((millis()-t)<0.5)
//      {}
//      digitalWrite(PUL,HIGH);
//      t=millis();
//      while((millis()-t)<0.5)
//      {}
//      digitalWrite(PUL,LOW);
//      if (n==0)
//      {
//        exit(0);
//      }
//
//   
//  }

//even
