#include <stdio.h>
#include <math.h>
#include <stdlib.h>


int main(){
    
int n=1000;
float *x;
float *u;
FILE *in;

in = fopen("Datos.dat","w"); 

x=malloc(n*sizeof(float));
u=malloc(n*sizeof(float));

if(!x || !u){
    printf("Error");
    exit(1);
	 }
int i;
for(i=0; i<n; i++){
x[i]=(i*1.0)/n;
}


for(i=0; i<n; i++){
u[i]=exp(-((x[i]-0.3)*(x[i]-0.3))/0.01);
}

u[0]=0;
u[n-1]=0;

for(i=0;i<n;i++){
    fprintf(in, "%f %f\n", x[i],u[i]);
  }


}

