#include <math.h>
#include <stdio.h>
#include <stdlib.h>
void integrar (float a, float b, float h);

int main(int argc, char **argv){
  
  
  float value_a;
  float value_b;
  float value_h;
  

value_a=atof(argv[1]);
value_b=atof(argv[2]);
value_h=atof(argv[3]);

integrar(value_a, value_b, value_h);

} 

void integrar (float a, float b, float h){

float resultado;
float num;
int i;

num=(b-a)/h;
float ValorFuncion(float a);
for(i=0;i<num;i++){

    resultado+=(ValorFuncion(a+i*h))*h;
  }
  printf("%f", resultado);

} 

float ValorFuncion(float a){

float funcion;
funcion=1/(sqrt(1+cos(a)*sin(a)));

return funcion;
} 

