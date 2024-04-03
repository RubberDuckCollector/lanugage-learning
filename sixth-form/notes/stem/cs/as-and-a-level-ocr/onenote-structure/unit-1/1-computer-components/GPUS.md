# GPUS

**2024-04-03**

- [ ] **If this box is unchecked, this file has not been fact checked by a teacher. If you're a teacher familiar with OCR H446, submit a pull request or email me! <eggsim49@gmail.com>**

<!-- vim-markdown-toc GFM -->

* [GPUs and graphics processing](#gpus-and-graphics-processing)
* [Uses](#uses)
* [Table of differences](#table-of-differences)

<!-- vim-markdown-toc -->

A GPU (Graphical Processing Unit) is a [coprocessor](./COPROCESSORS-AND-INSTRUCTION-SETS.md) that differs from CPUs in its architecture and usage.
- GPUs are not used as general purpose processors but serve special purposes instead

- GPUs are well suited fro graphics processing because they can do lots of maths in parallel...
- which allows them to make the calculations necessary for drawing pixels on a screen.

GPUS used to only be used for graphics processing...
- but now their parallel processing capabilies have been applied to different situations.

## GPUs and graphics processing

GPUs are great at graphics processing because:
1. it's possible to render graphics using parallel processing, which they're good at due to their high numbers of cores
1. coordinate positions in environments rendered by GPUs are stored as floating point numbers, meaning that lots of floating point arithmetic is required to render the scene
    - and GPUs are great at floating point arithmetic
1. the 3D scene lends itself well to 3 dimensional matrices, meaning the GPU can implement SIMD to act on each element in a multi-dimensional matrix, where a CPU would find this very **inefficient**
    - e.g:
        - a GPU will loop `for every vertex in map_geometry` or loop `for every pixel in screen`.
        - we can see how this would be efficient with parallel processing - the screen can be split up into segments handled by groups of cores and be processed in parallel
        - which is enabled by the thousands of cores, making GPUs unique

## Uses

- graphics processing
- predicting the weather - **weather modelling**
- password cracking (a hash of a password is obtained, then the attacker brute forces the password by hashing different passwords with the same hashing algorithm and sees if the hashes are identical)
- machine learning
- data mining
    - this includes:
        - mining for cryptocurrency,
        - distributed OSs like [folding at home](https://foldingathome.org/)
        - analysis of statistics and probability - economics

## Table of differences

| GPUs                                                                      | CPUs                                                                                                       |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| has a **large** number of cores                                           | has a **lower** number of cores                                                                            |
| a GPU core typically runs slower than a CPU core                          | a CPU core runs faster than a GPU core                                                                     |
| a GPU core is typically **physically smaller** than a CPU core            | a CPU core is typically **bigger** than a GPU core                                                         |
| can perform parallel processing at a larger scale                         | cannot perform parallel processing at large scales                                                         |
| makes good use of [SIMD](./PROCESSOR-ARCHITECTURES.md#simd)               | does not typically do SIMD                                                                                 |
| GPUs are faster and more efficient for certain tasks                      | CPUs are faster, taking into account all of the computing needs of someone due to their generalised nature |
| GPUs are great at performing **simple operations** on **large** data sets | CPUs are great at performing **complex operations** on **smaller** data sets                               |
