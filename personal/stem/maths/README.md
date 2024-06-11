<!-- vim-markdown-toc GFM -->

* [Maths...](#maths)
* [Goals](#goals)
* [Plan, structure, and more](#plan-structure-and-more)
* [IGCSE-EDEXCEL](#igcse-edexcel)

<!-- vim-markdown-toc -->

# Maths...

- I've never been *good* at maths, whether it's between terrible teachers or not being willing to understand it, but I want to learn it now.
- Last year I had to go back to the sine rule for challenge 36 on OCR programming challenges [here](https://www.ocr.org.uk/Images/260930-coding-challenges-booklet.pdf) on HegartyMaths (RIP), and I felt really comfortable.
- I felt confident in my understanding of equations when I had to flip all fractions to get $\frac{\sin(a, b, c)}{a, b, c}$ vs $\frac{a, b, c}{\sin(a, b, c)}$, etc..
- I want to revisit maths now because I'm still shit at it, not being confident or strong with mental maths at all, but I know i've spent so much time practicing my pattern recognition, problem solving, and logical thinking through learning to code. I think I'll have a much easier time coming back to mathematical thinking by myself
    - Python is my most used language because I was taught it in school, but I also have plans to explore Haskell, Lua, and Rust.

- For context:
    - I got a 7 in Edexcel IGCSE maths in the 2022 exam cycle in the summer.
    - I'm not a stranger to maths, but I am unqauianted with its patterns and when and how to apply them.
    - Here's my programmer POV:
        - There will be a recursive **and** an iterative solution to a problem with repeating programming statements (e.g n<sup>th</sup> term of fibonacci sequence).
        - Coded example:
            - You can reverse a string like this: `msg = msg[::-1]`, where `msg` is any given string,
            - You can also reverse a string like this, it's verbose and unnecessary but it shows my point:
            ```python
            msg = "hello world"  # just an example string
            msg = list(msg)
            msg.reverse()
            msg = "".join(msg)
            ```
            - There's going to be a concise solution to any given problem, and a longer solution. Disregarding space and time complexity, those two solutions would have the same output, thus in a way making them both useful. They've both outputted the desired effects/answer

- My thoughts
    - You can see how I automatically know that there are multiple ways of laying out the same thing in program code,
    - And that is exactly what I want to be able to do with maths and with mathematical notation.
    - I'm not particularly amazing at programming, I've just attempted and completed enough things (free and available on my GitHub) by myself to be comfortable in my chosen programming language.
    - I want to be at the same level with maths, where I can instinctively know different ways to describe concepts and solve problems. This means that my understanding on the patterns widens, as I essentially have more fluent access to the grammar of maths and I can manipulate it with ease.
        - (This is how learning languages works! Learn lots of synonyms and antonyms to increase your dominance over the target language!)

# Goals

1. I'm going to start from the beginning of GCSE/IGCSE, which (I think) teaches up from the introduction of basic concepts like ratios, to the *canonically* hardest topics on there, which are compound inverse functions with algebraic fractions and some absolute bs with some geometry and vectors on IGCSE Higher.

# Plan, structure, and more

TL;DR: Starting from IGCSE again because that's a good starting point that goes up to some more involved topics like algebraic fractions.
- I will naturally be covering the foundation tier as part of the higher tier because the higher tier incorporates all of the foundation tier in its spec.
- I'll be doing lots of linking too. I'll link from one `.md` file to another. So I really need well-defined preconditions in terms of the structure of my files before I begin writing them. This is why I've chosen to replicate the spec's structure.
- I'll be making loads of connections to computer science. That's kinda the point. Realising how interconnected cs and maths are and using cs to strengthen my mathematical skills

# IGCSE-EDEXCEL

- If a dir has `-f` on the end, it's in foundation but I'm lumping all my work into the higher tier because foundation maths is too slow for me
- As you can see in the file tree, I've replicated the spec by AO1, 2, and 3 components.
    - Then, I've made dirs for each unit.
        - The unit numbers are contiguous, which is something I didn't know. The units are just assigned an AO number ig.
    - My README structure:
        - Let's use AO1, unit 1 numbers and the number system as an example.
        - In `1.1-integers-f`, I'll put a README file there.
        - It's named `IGCSE-EDEXCEL-AO1-1-1.1-README.md`. I think that's a good naming system. Course, board, AO, topic, unit
            - At the top of that file, I'll write down everything I still remember about that skill/topic, then below that I'll write what I think I need to learn, and what I think I need to practice. Then there'll be my work, then anything I've found out from that work at the bottom.
            - From computer science I've learnt that systems for everything from naming files and variables to the structure of files is essential for maintainable systems.
