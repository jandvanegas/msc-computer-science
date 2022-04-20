#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void matmul(int **A, int **B, int r, int x, int c, int **C);
int getPosition(int **A, int **B, int i, int j, int x);
int** initMatrix(int x, int y);
int main() {
  int AI[2][3] = {{1, 2, 3},
            {4, 5, 6}};
  int r=2, x=3;
  int **A = initMatrix(r, x);
  for (int i=0; i<r; i++) {
    for (int j=0;j<x; j++) {
      A[i][j] = AI[i][j];
    }
  }
  int BI[3][2] = {{10, 11},
    {20, 21},
    {30, 31}};
  int c=2;
  int **B = initMatrix(x, c);
  for (int i=0; i<x; i++) {
    for (int j=0;j<c; j++) {
      B[i][j] = BI[i][j];
    }
  }

  int **C = initMatrix(r, c);

  matmul(A, B, r, x, c, C);

  for (int i=0; i<r; i++) {
    for (int j=0;j<c; j++) {
      printf("%d ", C[i][j]);
    }
    printf("\n");
  }

}

int** initMatrix(int x, int y) {
  int **R;
  
  R = (int **) malloc(x * sizeof(int *));
  for (int i=0; i < x; i++) {
    R[i] = (int *) malloc( y * sizeof(int *));
  }
  return R;
}

void matmul(int **A, int **B, int r, int x, int c, int **C) {
  for (int i=0; i<r; i++) {
    for (int j=0; j<c; j++) {
      C[i][j] = getPosition(A, B, i, j, x);
    }
  }

}

int getPosition(int **A, int **B, int i, int j, int x) {
  int value = 0;
  for (int k=0; k<x; k++) {
    value = value + A[i][k] * B[k][j];
  }
  return value;
} 

