#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *create_threads();

int main(int argc, char *argv[]) {
  pthread_t tid;
  long int t = atoi(argv[1]);
  pthread_create(&tid, NULL, create_threads, (void *) t); 
  void *status;
  pthread_join(tid, &status);
  exit(0);
}

void *create_threads(void *args){
  int long t = (long int) args;
  fprintf(stdout, "Thread created with param %ld\n", t);
  pthread_exit(NULL);
}
