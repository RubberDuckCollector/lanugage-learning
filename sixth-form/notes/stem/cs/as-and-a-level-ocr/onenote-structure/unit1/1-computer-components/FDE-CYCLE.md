# FDE cycle

**2024-03-25**

- [ ] **If this box is unchecked, this file has not been fact checked by a teacher. If you're a teacher familiar with OCR H446, submit a pull request or email me! <eggsim49@gmail.com>**

## FDE cycle

<details><summary><strong>Top level GCSE explanation (will rewrite for A Level with opcodes and operands and CIR at some point)</strong></summary>
    <ol>
        <li>
            The program counter (PC) stores the address in memory of the next instruction to be processed
        </li>
        <li>
            The address from the PC is copied in the memory address register (MAR)
        </li>
        <li>
            The PC will now increment to the next instruction in memory, to prepare for the next clock cycle
        </li>
        <li>
            The control unit (CU) will fetch the instruction from the address listed in the MAR and store the actual instruction in the memory data register (MDR)
        </li>
        <li>
            Once the CU has the instruction, it can decode it, which means work out what needs doing and what components need contacting next. Then the Cu can execute the instruction, which means passing requests to different computer components as necessary
        </li>
        <li>
            If the instruction requires arithmetic or logical decisions to be made, the CU will pass the instruction to the arithmetic logic unit (ALU) to calculate the result. The result is stored in the accumulator (ACC)
        </li>
        <li>
            The CU, now that it has processed that instruction, will work on the next instruction. The program counter is holding the memory address of the next instruction. The CU will copy this to the MAR. The cycle repeats
        </li>
    </ol>
</details>
