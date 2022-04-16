
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

int main (int argc, char *argv[]) {
  int i, j, a, n, pid;

  setbuf (stdout, 0);
  a = atoi (argv[1]);
  n = atoi (argv[2]);

  for (i=0; i<a; i++) {
    for (j=0; j<n; j++) {
      pid = fork ();
      if (pid==0) {
        sleep (1);
        break;
      } else {
        sleep (1);
        printf ("Level %d: pid=%d generated pid=%d\n", i, getpid(), pid);
        if (j==n-1) {
	        printf ("EXIT pid=%d\n", getpid());
          exit (0);
        }
      }
    }
  }

  printf ("RETURN pid=%d\n", getpid());

  return (0);
}
