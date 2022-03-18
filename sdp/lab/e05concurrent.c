#include <stdio.h>
#include <stdlib.h>

void binary_function(int *, int);
void print_int_location(int *ptr, size_t length);

int main ( int argc, char *argv[]) {
  int n;
  int *vet;

  n = atoi (argv[1]);

  vet = (int *) malloc(n * sizeof(int));
  if (vet == NULL) { printf("Allocatin Error.\n"); exit(1); }

  printf("Binary Numbers:\n");

  binary_function(vet, n);

  free(vet);

  return 0;
}

void binary_function ( int *vet, int n) {
  int j;
  for (j=0; j<n; j++) {
    int child_id = 0;
    for (int k=0; k<2; k++){
      child_id = (int) fork();
      if (!child_id) {
        if (k==0) vet[j] = 0;
        if (k==1) vet[j] = 1;
        break;
      }
    }
    if (child_id) exit(0);
  }
  print_int_location(vet, n);
}

void print_int_location(int *ptr, size_t length){
  size_t i = 0;
  for ( ; i< length; i++) printf("%d", ptr[i]);
  printf("\n");
}
