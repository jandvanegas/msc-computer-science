# Lab 01
Write a program in 8086 assemgly to:
* Read in input a short text of 4 lines, each of
  these lines long from 20 to 50 characters
* Count number of occurences of letters
* Apply a crypthographic algorithm

## Reading
* Reading stops when one of these conditions is 
satisfied
  * After at least 20 characters, an Enter has been
  read
  * 50 characters have been read withoug any ENTER
* Enter character corresponds to 13 in ASCII table
```
line_min equ 5
line_max equ 10
.model small
.stack
.data 

first_line db line_max dup (?)
second_line db line_max dup (?)
third_line db line_max dup (?)
fourth_line db line_max dup (?)

.code
.startup
                     
        mov di, 0
        mov ah, 1 ; set to reading
first:  
        int 21h   ; read      
        mov first_line[di], al
        inc di  
        cmp di, line_min
        jnge first
        cmp al, 13
        je  second_setup   
        cmp di, line_max
        jne first       
second_setup:
        mov di, 0
        
second: 
        int 21h
        mov second_line[di, al
        inc di    
        cmp di, line_min
        jnge second
        cmp al, 13
        je  third_setup
        cmp di, line_max
        jne second   
third_setup:
        mov di, 0
        
third:  
        int 21h
        mov third_line[di], al
        inc di
        cmp di, line_min
        jnge third
        cmp al, 13
        je  fourth_setup
        cmp di, line_max
        jne third       
fourth_setup:
        mov di, 0
          
fourth:
        int 21h
        mov fourth_line[di], al
        inc di
        cmp di, line_min
        jnge fourth
        cmp al, 13
        je next
        cmp di, line_max
        jne fourth
next:
   
.exit
end]
```
