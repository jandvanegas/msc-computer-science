#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <stdbool.h>

int sigusr1Count = 0;
int sigusr2Count = 0;
bool lastSignal1 = false;
bool lastSignal2 = false;

static void signalHandler(int signal);

int main (int argc, char *argv[]) {
  int n;
  n = atoi(argv[1]);
  signal(SIGUSR1, signalHandler);
  signal(SIGUSR2, signalHandler);
  while (1){
    sleep(2);
    n++;
    fprintf(stdout, "Increasing n to %d\n", n);
  }
}

static void signalHandler(int signal) {
  bool success = (lastSignal1 && signal == SIGUSR2) ||
    (lastSignal2 && signal == SIGUSR1);
  if (success) fprintf(stdout, "success\n");

  if (signal == SIGUSR1) { 
    lastSignal1 = true;
    lastSignal2 = false;
    sigusr1Count++;
    sigusr2Count = 0;
  }
  if (signal == SIGUSR2) {
    lastSignal1 = false;
    lastSignal2 = true;
    sigusr2Count++;
    sigusr1Count = 0;
  }

  if (sigusr1Count == 2 || sigusr2Count == 2) fprintf(stdout, "error\n");
  if (sigusr1Count == 3 || sigusr2Count == 3) exit(0);

}
