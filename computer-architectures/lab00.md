# Lab 00

```
.model small
.stack ; default size 1kb
.data  ; data segment

opa dw 3
opb dw 2
res dw ?

.code ; code segment
     
.startup
mov al, opa
mov ax, opb
mov rex, ax

.exit   

end
```
Mov to a register
```
.model small
.stack ; default 1kb
.data ; data segment
.code ;
.startup
MOV AX, 0
.exit
end
```
Mov to a memory cell
```
.model small
.stack
.data
var dw ?   
.code
.startup
mov var, 0
.exit
end
```
Sum up two values
```
.model small
.stack
.data
OPD1 dw 10
OPD2 dw 24
result dw ?   
   
.code
.startup   

mov AX, OPD1
add AX, OPD2
mov result, AX


.exit
end
```
Sum elements of a matrix
```
.model small
.stack
.data

vett dw 2, 5, 16, 12, 34
result dw ?

.code
.startup

mov ax, vett
add ax, vett + 2
add ax, vett + 4
add ax, vett + 6
add ax, vett + 8


.exit
end
```
Sum of elements with loop using jumps
```
dim equ 15
.model small
.stack
.data             
vett DW 2, 5, 16, 12, 34, 7, 20, 11, 31, 44, 70, 69, 2, 4, 23
result DW ?                                             

.code
.startup
mov ax, 0
mov cx, dim ; array size now stored in cx
mov di, 0 
lab:    add ax, vett[di] ; add i-th element to AX
        add di, 2 ; go to next element
        dec cx
        cmp cx, 0 ; compare array index with 0
        jnz lab   ; jump if not equal to zero
        mov result, ax
.exit
end
```
Read 20 characters and print them out
```
dim equ 20   
.model small
.stack
.data

vett db dim dup(?)

.code
.startup
     
        mov cx, dim
        mov di, 0
        mov ah, 1   ; set ah for reading     
lab1:   int 21h     ; read the character      
        mov vett[di], al    ; store the character
        inc di              ; go to next element
        dec cx
        cmp cx, 0
        jnz lab1
        mov cx, dim
        mov ah, 2           ; set ah for writing
lab2:   dec di     
        mov dl, vett[di]
        int 21h             ; display character
        dec cx
        cmp cx, 0
        jnz lab2
         
.exit    
end
```
Get minimun value
```
        .model small
        .stack
dim     equ 20
        .data
table   db  dim dup(?)
        .code
        .startup
        
        mov cx, dim
        mov di, table
        mov ah, 1
lab1:   int 21h
        mov [di], al
        inc di
        dec cx
        cmp cx, 0
        jne lab1
        mov cl, 0FFH   
        mov di, 0
ciclo:  cmp cl, table [di]; compare with current minimun
        jb dopo                                         
        mov cl, table[di] ; store new minimun
dopo:   inc di
        cmp di, dim
        jb ciclo
output: mov dl, cl
        mov ah, 2
        int 21h
        .exit
        end
```
