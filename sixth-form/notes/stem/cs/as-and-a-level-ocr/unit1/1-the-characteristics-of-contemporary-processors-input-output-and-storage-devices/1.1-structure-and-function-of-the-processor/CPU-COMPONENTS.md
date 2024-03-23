# CPU Components

**Started 2024-03-23**

- [ ] **if this box is unchecked, this file has not been fact checked by a teacher. if you're a teacher familiar with OCR H446, submit a pull request!**

## CPU components

### PC (program counter)
    - increments by one ready for the next instruction to be processed after the current FDE cycle
    - also increments when a branch or jump instruction is found by the CPU

### ALU (arithmetic logic unit)
    - carries out mathematical operations such as arithmetic (+ - * /) and logical comparisons (AND, OR, NOT)

### ACC (accumulator)
    - stores the results of the calculations in the ALU

### system clock
    - a continuously oscillating signal that sends out a pulse (either 0 or 1) that all CPU components sync themselves with
    - therefore the CPU components cannot operate at conflicting times
    - one clock cycle corresponds to an FDE cycle
    - the rate at which the clock sends out pulses is the clock frequency
        - this is measured in Hertz (Hz)
        - calculated by $num\ of\ clock\ cycles\div{time}$
            - if you have a CPU that completes 5 clock cycles in 2 seconds, you'll have a shitty CPU but it'll also be $\frac{5}{2}$ Hz.

### CIR (current instruction register)
    - stores the current instruction being processed
    - this is divided up into its opcode and operand
        - the opcode tells the CPU what to do
        - the operand is the data being acted on
        - [LMC](../../2-software-and-software-development/2.4-types-of-programming-languages/TYPES-OF-PROGRAMMING-LANGUAGES.md#lmc) example:
        ```
        STA FIRST
        ```
        - `STA` is the operand, the process going on
        - `FIRST` is the data that `STA` is working on
        - (that line of code is storing the data in FIRST into the accumulator)


**Finished ?**
