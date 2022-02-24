# Computer Architectures

> Date: 27.09.2021
## Introduction
Professors:
* P. Montuschi
* R. Ferrero
* B. Montrucchio
* A. Marceddu
* M. Sonza

Languages:
* 8086 -> Paolo Montuschi(Don't ask recommendation letters)
* ARM -> Renato Ferrero
* MIPS -> M. Sonza
* Paralell Architectures -> M. Sonza, Paolo Montuschi
* Labs -> A. Marceddu, B. Montrucchio.

## Arm Introduction
### The five W's of ARM Assembly
* Who? -> Renato Ferrero. Forum or telegram
* What?
	* RISC architecture
	* Exception handling
	* NXP ARM Cortex-M3 **LPC1768** Board
* When? Nov 10th to Dec 10th
* Where?
	* 9 lectures in classroom 
	* 1 virtual classroom
	* 4 laboratories (Labinf and/or virtual)
* Why?: [Assembly in Ranking 8th](https://www.tiobe.com/tiobe-index/) 
## 8086 Introduction
Process of developing a programm
* Source (Text file, hll, .c)
* Compiler (Translate into .obj)
* .obj (does not depend to language, it depends on the machine)
* Linker (.obj into .exe)
* Exec (.exe, machine language)

Process of running a programm
* Run p.exe
* OS
* Loader (moves .exe to the ram)

### Question: Without taking into account EULA (Licenced, C.C. License) that does not allow you to do Reverse Engineering. How far could do go from .exe to the source? -> impossible?

Variable at different levels:
* Source -> Name, Type
* Exec -> Cell of memory identified by an address

First Reason to say you cannnot go from .exe to source:
* The goal of the compiler is to match variables in source level to exec. Name -> Address 
* If you want to go from Address to a variable in the source level, you would lose information like the type of the variable.

Second reason: 
Let say we have a variable `a <- a + b + c + d + e` in source level.In exec level, this would have to be executed by parts like:
```
a <- a + b
a <- a + c
a <- a + d
a <- a + e
```
This means: one instruction at high level can generate many intructions at the exec level. Therefore, going from low level instructions it's not feasible, given that intructions at low level could be rearrange because of optimization. 

### Until which point can we go? From bottom to top
* Exe 100011000 (Machine level instructions). We can understand what is done when finding this instruction (e.g. add content of reg #1 with reg #2 and store result in #1)
* This understanding is **Assembly Language** e.g `ADD AX, BX` and this does not cost that much. The compiler is able to do this corresponding. **This is what we will learn**

### What is an instruction set?
* All the set of instructions that can be used to develop a program. Each machine has different sets. 

> Date: 29-09-2021
