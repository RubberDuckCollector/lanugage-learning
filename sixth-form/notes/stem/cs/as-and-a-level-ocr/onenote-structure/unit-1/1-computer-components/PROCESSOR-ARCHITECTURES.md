# Proccesor architectures

**2024-04-01**

- [ ] **If this box is unchecked, this file has not been fact checked by a teacher. If you're a teacher familiar with OCR H446, submit a pull request or email me! <eggsim49@gmail.com>**

<!-- vim-markdown-toc GFM -->

* [Types of architectures](#types-of-architectures)
* [SIMD and MIMD](#simd-and-mimd)
    * [SIMD](#simd)
    * [MIMD](#mimd)

<!-- vim-markdown-toc -->

- a processor can ***only*** **fetch** instructions, **decode** instructions, and **execute** instructions.

## Types of architectures

1. **Von Neumann architecture**
    - there are 3 buses:
        1. data bus
        2. [control bus](./PROCESSOR-COMPONENTS.md#control-bus)
        3. address bus
    - the instructions and data of the CPU are stored in the same space in memory
    - they're also stored in the same format
    - **the single control unit** is responsible for managing the **fetching**, **decoding** and the **executing** of the processor.
    - makes use of registers to store instructions and data
    - used in processors for general purpose computing (e.g desktop computers and laptops)
    - pros:
        - its simplistic design makes it well-suited for general purpose computing
    - cons:
        - data and instructions cannot be transported in parallel, meaning that the CPU loses time waiting for one thing at a time to be transported into a register

1. **Harvard architecture**
    - instructions and data are stored in **separate** memory locations
    - used in mobile processors
    - pros:
        - instructions and data can be fetched **in parallel** (time is not lost waiting for one instruction/piece of data to arrive at the CPU at a time)
        - the cache memory that stores the instructions and data can each be made more efficient than in Von Neumann architecture
        - because in the Von Neumann architecture, the cache memory has to be somewhat standardised and general due to its general use cases
        - the cache in Harvard architecture can be specialised for instructions and specialised for data
    - cons:
        - it's more complex than the Von Neumann architecture, meaning that the processor would be bigger in size
            - which may not be suitable for all applications

1. **contemporary architecture**
    - this is a combination of Harvard and Von Neumann
    - it combines elements from the two architectures

## SIMD and MIMD

### SIMD

- one instruction is carried out on multiple data sets **through the use of parallel processing on more than one core at a time**

### MIMD

- more than one instruction is carried out on more than one data set **also through the use of parallel processing on more than one core simultaneously**
