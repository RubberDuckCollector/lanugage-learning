# Coprocessors and instruction sets

**2024-04-02**

- [ ] **If this box is unchecked, these code examples have not been fact checked by a teacher. If you're a teacher familiar with OCR H446, submit a pull request or email me! <eggsim49@gmail.com>**

<!-- vim-markdown-toc GFM -->

* [Coprocessor](#coprocessor)
* [Instruction sets](#instruction-sets)
    * [RISC and CISC table of differences](#risc-and-cisc-table-of-differences)
    * [RISC advantages](#risc-advantages)
    * [CISC advantages](#cisc-advantages)

<!-- vim-markdown-toc -->

## Coprocessor

A coprocessor is an additional microprocessor that aids a bigger processor in its functions and capabilities.
it's used for a special task:
- e.g: 
    - graphics processing, or:
        - **coprocessors use bespoke sets of electronics, so:**
        - some processors may have an **extra circuit** in them which is **specifically designed** to calculate division operations or square root operations

## Instruction sets

**An instruction set is a collection of commands that a processor can understand and act on.**
    - LMC example: (MAKE LMC NOTES)
    `STA` would be in the instruction set of an LMC CPU. the CPU recognises `STA`.

### RISC and CISC table of differences

| CISC                                                                                                                                    | RISC                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| USAGE: used in general purpose processors where the devices would likely be connected to mains, therefore power concerns wouldn't exist | used in mobile processors where conserving battery power is imperative |
| INSTRUCTION NUM: has a large number of instructions                                                                                     | has a low number of instructions                                       |
| COMPLEXITY: the instructions are relatively complex                                                                                     | the instructions are relatively simple                                 |
| INSTRUCTION LENGTH: the instructions **vary in length**                                                                                 | the instructions are **fixed in length**                               |
| one instruction can correspond to **more than one** processor clock cycle                                                               | one instruction **always** corresponds to **one** clock cycle          |
| there are **many** addressing modes, and **there are compound addressing modes** (direct, indirect, indexed, immediate)                 | there are limited addressing modes                                     |
| makes efficient use of RAM: the instructions take up less space in memory due to being shorter in length (?)                            | makes less efficient use of RAM: the instructions take up more space   |

### RISC advantages

| advantages                                                                           |
|--------------------------------------------------------------------------------------|
| more efficient than CISC because the instructions are stored in less space in memory |

### CISC advantages

| advantages                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| easier to code in due to being more abstracted than RISC bc one CISC instruction can mean multiple RISC instructions (the programmer wouldn't have to write all of the underlying operations out by hand) |
