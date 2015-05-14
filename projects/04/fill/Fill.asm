// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.


@8192
D=A

@screensize
M=D

@count
M=0

@state
M=0

(KEABORDLOOP)
    @KBD
    D=M
    
    @state
    D=D-M

    @KEABORDLOOP
    D;JEQ

    @state
    M=M+D
    D=M

    @BLACKSCREENLOOP
    D;JGT

    @WHITESCREENLOOP
    0;JMP

(BLACKSCREENLOOP)
    @SCREEN
    D=A

    @count
    A=D+M
    M=-1

    @count
    MD=M+1

    @screensize
    D=M-D

    @BLACKSCREENLOOP
    D;JGT

    @count
    M=0

    @KEABORDLOOP
    0;JMP

(WHITESCREENLOOP)
    @SCREEN
    D=A

    @count
    A=D+M
    M=0

    @count
    MD=M+1

    @screensize
    D=M-D

    @WHITESCREENLOOP
    D;JGT

    @count
    M=0

    @KEABORDLOOP
    0;JMP
