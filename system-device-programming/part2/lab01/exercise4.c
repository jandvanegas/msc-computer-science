#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char **argv) {
	int h = atoi(argv[1]);
	int n = atoi(argv[2]);
	int total = 1;
	printf("Starting with h=%d and n=%d\n", h, n);
	for (int level=0; level<=h; level++) {
		int child_id=0;
		for (int child=0; child<n; child++) {
			child_id = (int) fork();
			if (!child_id) {
				break;
			} 
			printf("Level %d: %d generated %d\n", level, getpid(), child_id);
		}
		if (child_id) exit(0);
	}
	int pid = getpid();
	printf("Finishing leaf %d \n", pid);
}

