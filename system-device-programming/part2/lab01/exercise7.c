#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *create_threads();

struct thread_tree {
  int index;
  int final;
  long int* tree;
};

int main(int argc, char *argv[]) {
  int t = atoi(argv[1]);
  fprintf(stdout, "Thread created with param %d\n", t);

  pthread_t tid;
  struct thread_tree tree;
  tree.index = 0;
  tree.final = t;
  tree.tree = (long int*) malloc(tree.index + 1 * sizeof(long int));
  pthread_create(&tid, NULL, create_threads, (void *) &tree); 

  void *status;
  pthread_join(tid, &status);

  exit(0);
}

void *create_threads (void *args){
  struct thread_tree *t; 
  t = (struct thread_tree *) args;
  pthread_t current = pthread_self();
  t->tree[t->index] = current;

  if (t->index == t->final - 1) {
    for (int i=0; i<=t->index; i++) {
      fprintf(stdout, "%ld ", t->tree[i]);
    }
    fprintf(stdout, "\n");
  }
  else {

    pthread_t tid2;
    struct thread_tree tree2;
    tree2.tree = (long int*) malloc(t->index + 1  * sizeof(long int));
    tree2.index = t->index + 1;
    tree2.final = t->final;
    for (int j=0; j<=t->index; j++) {
      tree2.tree[j] = t->tree[j];
    }
    pthread_create(&tid2, NULL, create_threads, (void *) &tree2); 

    pthread_t tid1;
    struct thread_tree tree1;
    tree1.tree = (long int*) malloc(t->index + 1 * sizeof(long int));
    tree1.index = t->index + 1;
    tree1.final = t->final;
    for (int i=0; i<=t->index; i++) {
      tree1.tree[i] = t->tree[i];
    }
    pthread_create(&tid1, NULL, create_threads, (void *) &tree1); 

    void *status1;
    pthread_join(tid1, &status1);
    void *status2;
    pthread_join(tid2, &status2);
  }
  pthread_exit(NULL);
}
