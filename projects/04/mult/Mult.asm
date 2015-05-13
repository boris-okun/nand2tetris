// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@temp
M=1

@R2
M=0

@sign
M=0

@R0
D=M

@END
D;JEQ

@R1
D=M

@END
D;JEQ

@32767
D=-A

@R0
D=D&M

@sign
M=D

@32767
D=A

@R0
M=D&M

@32767
D=-A

@R1
D=D&M

@sign
M=D-M

@32767
D=A

@R1
M=D&M

@LOOP
0;JMP

(POSR1)
@sign
M=M+1

(LOOP)
@temp
D=M

@R1
D=D&M

@NEXT
D;JEQ

@R0
D=M

@R2
M=M+D

(NEXT)
@R0
D=M

@R0
M=D+M

@temp
D=M

@temp
MD=D+M

@R1
D=M-D

@LOOP
D;JGE

@sign
D=M

@END
D;JEQ

@R2
M=-M

(END)
@END
0;JMP
