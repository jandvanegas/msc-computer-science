# Unix Standard and Implementations
## UNIX System Overview
The focus of this text is to describe the services provided by versions
of UNIX operating system.
### UNIX Architecture
* An OS can be defined as the software that controls the hardware 
  resources and provides an environment under which programs can run.
* We call this software *kernel*.
* The interface to the kernel is a layer of sofware call the *system 
  call*.
* Libraries of common functions are build on top of the system call
  interface, but applications are free to use both.
### Logging in
* When we log in to a UNIX system
	* We insert user and password
	* The system looks up our login name in its password file (
	  usually /etc/passwd)
* Once we log in, we can type commands to the shell program. The system
  knows which sheel to execute based on the password file.
* There are many shells (e.g. Bourne Shell /bin/sh, Bourne-again Shell
  /bin/bash, C shell /bin/csh, Korn shell /bin/ksh, TENEX C shell 
  /bin/tcsh)
* The Bourne-again shell is the GNU shell provided with all Linux 
  systems. It was designed to be POSIX conformant, while still 
  remaining compatible with the Bourne shell.
### Files and Directorys
* The file system is hierarchical arragement of directories and files.
  Everything starts in the directory called root (/).
* A directory is a file that contains directory entries.
* *stat* and *fstat* functions return a structure of information
  containing all the attributes of a file
* The names in a directory are call filenames. */* and *null character*
  cannot appear in a filename. POSIX.1 recommend (a-z,A-z,0-9,.,-,_)
* .(current dir) and \.\.(parent dir) are created when a new directory is created
* Pathname is a sequence of filenames separated by slashes. 

