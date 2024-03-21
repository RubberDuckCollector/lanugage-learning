# Started 2024-03-20

# Checked ?

- [ ] checked and corrected by a maths student/maths teacher?

## Spec info

- spec can be found [here](https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Mathematics%20A/2016/Specification%20and%20sample%20assessments/International-GCSE-in-Mathematics-Spec-A.pdf)
- we should:
    1. understand and use all integers (int, plural *ints*) positive, negative and zero
    2. understand place value
    3. use directed numbers in practical situations e.g temperature
    4. order integers i.e place them in order
    5. use the four rules of +, -, \*, and /
    6. use brackets and the hierarchy of operations (BIDMAS, BODMAS)
    7. use the terms "odd", "even", "prime numbers", "factors", and "multiples"
    8. identify prime factors, common factors, and common multiples

## What I think I already know

i'll go ahead and answer as many as i can.

1. an integer is a whole number. it does not have any meaningful decimal place values.
    - zero is in between negative and positive ints on a number line full of ints

2. we use base 10. that means there are 10 digits that each individually represent a value.
    - they are 0 to 9
    - you can think of a base 10 number as having columns. the rightmost column before the decimal place is the units
        - this represents values of $x\times{10}^0$, where $x$ is any digit from 0-9. anything to the power of 0 is 1, so it's $x\times{1}$
    - then the next column to the left represents values of $x\times{10}^1$, meaning that the digit there in the tens column is multiplied by $10^1$
        - so the number $42$ contains:
            - $4\times{10}^1$, equaling 40
            - $2\times{10}^0$, equaling 2, as $10^0$ is 1, $2\cdot1 = 2$.
    - there is a decimal place to the right of the units column
    - the column to the right of this decimal place represents a value $\frac{x}{10}$, $0.x$ where $x$ is a digit from 0 to 9
    - the denominator multiplies by 10 with each time you move right
        - so the 2nd column to the right of the decimal would represent values of $\frac{x}{100}$, $0.0x$
        - and the 3rd column to the right of the decimal would represent values of $\frac{x}{1000}$, $0.00x$ and so on
    - there's a trick, where if it's the 2nd decimal place to the right, there are $2-1$ zeros, if it's the 3rd, there are $3-1$ zeros then the digit and so on

## What I had to look up

3. directed numbers
    - i didn't know they were numbers with a sign as well as a magnitude
    - i know in computer science an antiquated way of representing negatives is with sign and magnitude
        - the leftmost bit is the sign, 1 means the number is negative
        - however this means you lose the upper range of the numbers you can handle and you gain the burden of a negative zero value and a positive zero value, which don't make sense
    - ig vector values such as velocity are directed numbers too. velocity has a 1 dimensional direction, and it has a magnitude. either going at a certain speed away from the start, or going *the other way* but what's precise is the rate of movement/distance covered.

# Ended ?
