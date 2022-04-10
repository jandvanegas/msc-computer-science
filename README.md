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
* .obj (does not depend on the language, it depends on the machine)
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

First Reason to say you cannot go from .exe to the source:

* The goal of the compiler is to match variables in source level to exec. Name -> Address
* If you want to go from Address to a variable in the source level, you would lose information like the type of the variable.

Second reason: Let's say we have a variable `a <- a + b + c + d + e` in source level. At exec level, this would have to be executed by parts like:

```asm6502
a <- a + b
a <- a + c
a <- a + d
a <- a + e
```

This means: one instruction at a high level can generate many instructions at the exec level. Therefore, going from low-level instructions it's not feasible, given that instructions at low-level could be rearranged because of optimization.

### Until which point can we go? From bottom to top

* Exe 100011000 (Machine level instructions). We can understand what is done when finding this instruction (e.g. add the content of reg #1 with reg #2 and store the result in #1)
* This understanding is **Assembly Language** e.g `ADD AX, BX` and this does not cost that much. The compiler can do this corresponding. **This is what we will learn**

### What is an instruction set?

* All the set of instructions that can be used to develop a program.
Each machine has different sets.

> Date: 29-09-2021
### 8086 Arch
* It is important to know the hw architecture of the hardware you use.
* Full control means full responsability.
* 16 bits architecture -> size of the registers.
* General purpose Registers A, B, C, D
    * AX -> 16 bits
    * AH, AL -> AH|AL
* Registers
  * Be used as pointers 
    * SI, DI, BP, (BX) -> 16 bits
  * Can be used as general and pointers, but do not used them 
directly.
    * SP -> Stack pointer
    * IP -> Instruction pointer. Program Counter (PC)
      * Notes 
      * Next (In time domain)
      * Following (in space domain)
  * Segment 16 bits
    * CS -> Code Segment
    * SS -> Stack Segment
    * DS -> Data Segment
    * ES -> Extra Segment
  * How to address 1M of instructions
    * How many cells can be addres with the IP? 
    * IP is 16 bits = 2^16 = 64K cells
    * But we need 20 bits 2^20 = 1M
    * However, we just need the Address bus to be 20 bits 
    * We need 4 bits more.
    * | 4 bits | IP |
    * This was solved overlapping with CS registers like:
    * | 0000 | 16 bits IP     | +  
      | 16 bits CS     | 0000 |
```
| - - - - - - - - - - - - - - - - | 
| Code                            | CS 2^16
| - - - - - - - - - - - - - - - - | 
|                                 | 
| - - - - - - - - - - - - - - - - | 
| Data                            | DS 2^16
| - - - - - - - - - - - - - - - - | 
|                                 | 
| - - - - - - - - - - - - - - - - | 
| Stack                           | CS 2^16
| - - - - - - - - - - - - - - - - | 
|                                 | 
| - - - - - - - - - - - - - - - - | 
|                                 | 
| - - - - - - - - - - - - - - - - | 
| Code 2                          | After The first part is full
|                                 | Update CS and clear IP
| - - - - - - - - - - - - - - - - | 
```

    * Bad indexing example: Assembler does not check if you bad index.
    If you want a carrot but you index 3. Assembler does not tell you
    that you're accessing a tomato. However if yo declare correctly
    the compiler would check. An even worst case is if you index 5 and
    you end up accessing code.
```
|                                 | 
| - - - - - - - - - - - - - - - - | 
| Data                            | 0 |_| Carrots 
|                                 | 1 |_| Carrots 
|                                 | 2 |_| Carrots 
|                                 | 3 |_| Tomato 
| - - - - - - - - - - - - - - - - | 
| Code                            | 
| - - - - - - - - - - - - - - - - | 
|                                 | DS 2^16
| - - - - - - - - - - - - - - - - | 
```
> Date: 30/09/2021

