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
1:09:17
### Memory
```
|-----| 1230
|-----| 1231
|-----| 1232
|-----|  |
|-----|  Our convention increasing in this direction
|-----|
| 1 byte |
```

Let's say we want to move the content of AX (|AL|AH|) to the address 
1234 `MOV @ 1232, AX`, but we have then a mismatch
because 1232 address is just 8 byte long. However the compiler will
consider 1232 as the first cell to be involved. Therefore, two cell
actually would be involved. 
There are two ways to store the register 
Littler Endian (Lower at the lower address)
```
|AL| 1232
|AH| 1233
```
or 
Big Endian (Higher at the lower address)
|AH| 1232
|AL| 1233
### Stack -> LIFO
Last input, first output
```
_____
|   |<Stack Segment> <-SP = 0
|   |
|   |
|   |
|   |
|   |
| x | 
| x | 
| x |
| x | 
| x | <-SP The stack has two values
| x | 
| x | 
| x | 
-----
|   | <- SP when stack is empty
```
* Increase of the stack is opposite to the increase of address of memory
* SP(Stack pointer) -> points to the top of the stack
* Each element in an stack is 16 bits -> two cells
* No allowed pushing constants
* At the beginning when the stack is empty, SP is outside the Stack 
  segment and has value the size of the SS plus one
* When an item is added to the Stack, SP is reduced by two cells addres
  in the stack.
* When pushing to the stack `PUSH AX`, two things happen. `SUB SP, 2`
  and `MOV [SP] AX`.
* It is stored as little endian.
```
|    |
| AL | 
| AH | 
-----
```
* SP should not be negative because that would mean the stack was 
  overflowed.
* Choose mindfully the size of the SS(Stack segment). You have limited 
  area in 8086.

> Date 01/10/2021
### Instructions 8086
<Label> : <Operator> <Operand(s)> ; <comment>
```
Addressing Modes
Register | Direct
Constant | Indirect
------------------
CPU      | Memory
```
```
MOV dest, source ; copy from source to destination
```
* Operations needing two operands:
  I cannot have two operands both in memory.
CPU
* Register -> Mov AX, BX
* Constant -> MOV AX, 7
(MOV 7, AX) -> Not valid

Memory
Direct
* MOV AX,  @7 ; at address 7 

Commands to compiler
JOHN DW 101 ; Reserve 16 bits in the data segment
              and store 101 in that address. JOHN will have the address
              of this space. Therefore, the developer can use this 
              variable to reference the reserved address.
Symbol Table
Used by the compiler, just on compilation. After that it is deleted.
Meaning it is not used at runtime.
NAME What?     Equivalence
JOHN Word Data  <address>

MOV AX, JOHN + 2 ; This will be replaced at compile time with
MOV AX, <address> + 2

Array definition
N EQU 35 ; Constant definition
JIM DB N DUP(?); DUP dupplication, N number of cells, ? random value.

* Indirect
```
MOV JIM[ ], 0; in the space, you can use BX, BP, SI, DI
MOV JIM[BX], 0 ; BX is a contribution to compute the final address of memory. 
```
1:35:19
In a loop it would be
```
MOV JIM[BX], 0

INC BX
```
* At compiler -> JIM is replaced with the real address
* At runtime the real address is sum up with BX, and that is the 
  destination where 0 is placed.

* Be careful using the next way of addressing:
```
MOV JIM[BX][SI], 0; BX or BP, SI or DI
;JIM[BX][SI] -> <JIM address> BX + SI -> this is the offset of 
; the data segment
; BP in the first square  accesses the stack segment
```
* The next operations are translated to different actions 
  because the operands are different. In the first case for 
  example the first is Register content to Register content,
  in the second constant to Register content.
```
BOB DW ?
MOV AX, BX ; Register to Register
MOV AX, 2 ; Constant to Register
MOV AX, BOB ; Content of the address to Register. BOB becomes hardcoded
MOV AX, [BX] ; Content of the Address BX has to Register
```
* Data transfer
```
MOV dest, source
MOV JOHN, JIM ; WRONG to have two memory cells
MOV JOHN, 0 ; OK 0 is not in memory. It is part of the instruction
```
* Challenge
```
XCHG AX, BX; Let say we want this to swap values.

;Not a good solution
MOV CX, AX
MOV AX, BX
MOV BX, CX

;A good solution
PUSH CX
MOV CX, AX
MOV AX, BX
MOV BX, CX
POP CX

;Another good solution, but slowest
PUSH AX
PUSH BX
POP AX
POP BX

;Another good solution
PUSH AX
MOV BX, AX
POP AX

;The fastest
XOR AX, BX
XOR BX, AX
XOR AX, BX
```

