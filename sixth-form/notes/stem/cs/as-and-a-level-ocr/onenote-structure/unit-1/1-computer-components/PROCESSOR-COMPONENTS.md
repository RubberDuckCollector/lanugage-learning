# CPU Components

**2024-03-23**

- [ ] **If this box is unchecked, this file has not been fact checked by a teacher. If you're a teacher familiar with OCR H446, submit a pull request or email me! <eggsim49@gmail.com>**

<!-- vim-markdown-toc GFM -->

* [Registers](#registers)
    * [PC (program counter)](#pc-program-counter)
    * [ALU (arithmetic logic unit)](#alu-arithmetic-logic-unit)
    * [ACC (accumulator)](#acc-accumulator)
    * [system clock](#system-clock)
    * [CIR (current instruction register)](#cir-current-instruction-register)
* [Buses](#buses)
    * [data bus](#data-bus)
    * [address bus](#address-bus)
    * [control bus](#control-bus)

<!-- vim-markdown-toc -->

## Registers

A register is a piece of memory in a processor that has extremely fast access speed by the processor components
- registers can hold ***one*** piece of data or instruction ***at a time***
- not the same as main memory, that would be RAM
- which has a larger capacity and is slower

### PC (program counter)

- increments by one ready for the next instruction to be processed after the current FDE cycle
- also increments when a branch or jump instruction is found by the CPU

### ALU (arithmetic logic unit)

- carries out mathematical operations such as arithmetic (+ - * /) and logical comparisons (AND, OR, NOT)

### ACC (accumulator)

- stores the results of the calculations/operations in the ALU

### system clock

- a continuously oscillating signal that sends out a pulse (either 0 or 1) that all CPU components sync themselves with
- therefore the CPU components cannot operate at conflicting times
- one clock cycle corresponds to an FDE cycle
- the rate at which the clock sends out pulses is the clock frequency
    - this is measured in Hertz (Hz)
    - calculated by $num\ of\ clock\ cycles\div{time}$
        - if you have a CPU that completes 5 clock cycles in 2 seconds, you'll have a shitty CPU but it'll be $\frac{5}{2}$ Hz.

### CIR (current instruction register)

- stores and deciphers the current instruction being processed on the current FDE cycle
- this is divided up into its opcode and operand
    - the opcode tells the CPU what to do
    - the operand is the data being acted on
    - LMC example:
        - on [Wikipedia](https://en.wikipedia.org/wiki/Little_man_computer#Examples)
        - here: ↓
    ```
    STA FIRST
    ```
    - `STA` is the operand, the process going on
    - `FIRST` is the data that `STA` is working on
    - (that line of code is storing the data in FIRST into the accumulator)

## Buses

- buses are sets of wires in the processor that two or more components together
- all of the types of buses together in the processor is called the system bus
- the width of the bus is the number of parallel wires the bus has

### data bus

- bi-directional
    - meaning data can flow both ways through it
- transports data and instructions between components

### address bus

- carries the memory address in which data is being sent to or retrieved from
- for each extra wire that is added to this bus, the bus will be able to address double the locations in memory
    - in other words, an address bus with $n$ wires can carry $2^n$ signals
    - so, if an address bus had $3$ wires, it would have $2^3 = 8$ addressable locations

### control bus

- bi-directional
    - meaning data can flow both ways through it

- possible control signals that are handled:
    - **bus request**
        - shows that a device is requesting use of the **data** bus
    - **bus grant**
        - shows that the CPU has granted access to use the **data** bus
    - **memory write**
        - used to write data into an addressed location
    - **memory read**
        - data is read from a specific location to be placed on the data bus
    - **interrupt request**
        - used to show the CPU there is an unexpected event ocurring that needs expedited access to the CPU 
    - **clock**
        - used to synchronise operations of CPU components
