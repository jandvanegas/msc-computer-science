#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void matmul(int **A, int **B, int r, int x, int c, int **C);
void *getPosition(void *);
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

struct thread_mul {
  int **A;
  int **B;
  int **C;
  int i;
  int x;
  int j;
};

void matmul(int **A, int **B, int r, int x, int c, int **C) {
  struct thread_mul *t;
  pthread_t *threads;
  t = (struct thread_mul *) malloc(r * c * sizeof(struct thread_mul));
  threads = (pthread_t *) malloc(r * c * sizeof(pthread_t));
  
  for (int i=0; i<r; i++) {
    for (int j=0; j<c; j++) {
      int value;
      t[i+r*j].A = A;
      t[i+r*j].B = B;
      t[i+r*j].i = i;
      t[i+r*j].j = j;
      t[i+r*j].x = x;
      t[i+r*j].C = C;
      pthread_create(&threads[i*r+j], NULL, getPosition, (void *) &t[i*r+j]);
    }
  }
  for (int i=0; i<r; i++) {
    for (int j=0; j<c; j++) {
      pthread_join(threads[i*r + j], NULL);
    }
  }

}

void  *getPosition(void *args) {
  int value = 0;
  struct thread_mul *t;
  t = (struct thread_mul *) args;
  for (int k=0; k<t->x; k++) {
    value = value + t->A[t->i][k] * t->B[k][t->j];
  }
  t->C[t->i][t->j] = value;
} 

