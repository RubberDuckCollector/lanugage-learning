# Stacks

**2024-04-03**

- [ ] **If this box is unchecked, this file has not been fact checked by a teacher. If you're a teacher familiar with OCR H446, submit a pull request or email me! <eggsim49@gmail.com>**

<!-- vim-markdown-toc GFM -->

* [Stack operations](#stack-operations)
    * [Stack operations table](#stack-operations-table)
    * [Stack pop() function example in order](#stack-pop-function-example-in-order)
* [Stack coded example](#stack-coded-example)

<!-- vim-markdown-toc -->


- stacks are LIFO (last in first out)
    - the last element to enter the stack is the first element to leave the stack.

it's like a **stack of books** in a box:
- you put the books on top of each other,
- when you want to take the books out, you can't fit your hand down the side of the box and lift out a book from an arbitrary position in the stack,
    - so you take the books out one by one from the top of the stack in the box.

## Stack operations

There is a collection of operations that the spec requires us to know

1. `push()`
1. `pop()`
1. `peek()`
1. `isEmpty()`
1. `isFull()`

### Stack operations table

| operation   | takes a parameter? | return type                                                        | description                                                                   |
|-------------|--------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `push()`    | yes                | no return type (in python)                                         | puts a new element onto the **top** of the stack                              |
| `pop()`     | no                 | type of element that's just been removed from the top of the stack | removes and returns the last element added to the stack                       |
| `peek()`    | no                 | type of last element added to stack                                | returns the last element added to the stack without altering the stack        |
| `isEmpty()` | no                 | boolean                                                            | returns true if the stack has **0** elements in it, otherwise false           |
| `isFull()`  | no                 | boolean                                                            | returns true if the stack has **more than 0** elements in it, otherwise false |

### Stack pop() function example in order

- stacks have a pointer called **top**. this is important. it can be named differently from question to question, but what it is will be the same.

Here, `stack_pointer` is a pointer that will **always** be referring to the top item in the stack.

1. check if stack is empty
1. if stack is empty, display error and return/halt
1. else, return data item indexed by `stack_pointer`
1. decrement `stack_pointer` by one

## Stack coded example

- used <https://tohtml.com/python/>

<details><summary>expand this tab for stack coded example</summary>
    <pre class="code_syntax" style="color:#d1d1d1;background:#000000;"><span class="line_wrapper"><span style="color:#e66170; font-weight:bold; ">from</span> dataclasses <span style="color:#e66170; font-weight:bold; ">import</span> dataclass</span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper"><span style="color:#00dddd; ">@</span>dataclass</span>
    <span class="line_wrapper"><span style="color:#e66170; font-weight:bold; ">class</span> Stack<span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">    stack<span style="color:#d2cd86; ">:</span> <span style="color:#e66170; font-weight:bold; ">list</span></span>
    <span class="line_wrapper">    max_size<span style="color:#d2cd86; ">:</span> <span style="color:#e66170; font-weight:bold; ">int</span>  <span style="color:#9999a9; "># this is the user defined max length of self.stack</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">def</span> is_empty<span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">        <span style="color:#e66170; font-weight:bold; ">return</span> <span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">stack is empty</span><span style="color:#02d045; ">"</span> <span style="color:#e66170; font-weight:bold; ">if</span> <span style="color:#e66170; font-weight:bold; ">len</span><span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span> <span style="color:#00dddd; ">==</span> <span style="color:#008c00; ">0</span> <span style="color:#e66170; font-weight:bold; ">else</span> <span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">stack is not empty</span><span style="color:#02d045; ">"</span></span>
    <span class="line_wrapper">    </span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">def</span> is_full<span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">        <span style="color:#e66170; font-weight:bold; ">return</span> <span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">stack is full</span><span style="color:#02d045; ">"</span> <span style="color:#e66170; font-weight:bold; ">if</span> <span style="color:#e66170; font-weight:bold; ">len</span><span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span> <span style="color:#00dddd; ">==</span> self<span style="color:#d2cd86; ">.</span>max_size <span style="color:#e66170; font-weight:bold; ">else</span> <span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">stack is not full</span><span style="color:#02d045; ">"</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">def</span> peek<span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">        <span style="color:#e66170; font-weight:bold; ">if</span> <span style="color:#e66170; font-weight:bold; ">len</span><span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span> <span style="color:#00dddd; ">&gt;</span> <span style="color:#008c00; ">0</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">            <span style="color:#e66170; font-weight:bold; ">return</span> self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">[</span><span style="color:#00dddd; ">-</span><span style="color:#008c00; ">1</span><span style="color:#d2cd86; ">]</span></span>
    <span class="line_wrapper">        <span style="color:#e66170; font-weight:bold; ">else</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">            <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">cannot peek from an empty stack</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">def</span> push_to_stack<span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">,</span> data<span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">        <span style="color:#e66170; font-weight:bold; ">if</span> <span style="color:#e66170; font-weight:bold; ">len</span><span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span> <span style="color:#00dddd; ">&lt;</span> self<span style="color:#d2cd86; ">.</span>max_size<span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">            self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">.</span>append<span style="color:#d2cd86; ">(</span>data<span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">            <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">f"</span><span style="color:#02d045; background:#281800; ">{</span><span style="color:#ffffff; background:#281800; ">data</span><span style="color:#02d045; ">}</span><span style="color:#00c4c4; "> has been pushed to the stack!</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">        <span style="color:#e66170; font-weight:bold; ">else</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">            <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">Stack is at its maximum size. You cannot add any more elements</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">def</span> pop_from_stack<span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">        <span style="color:#e66170; font-weight:bold; ">if</span> <span style="color:#e66170; font-weight:bold; ">len</span><span style="color:#d2cd86; ">(</span>self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span> <span style="color:#00dddd; ">&gt;</span> <span style="color:#008c00; ">0</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">            last_item <span style="color:#d2cd86; ">=</span> self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">[</span><span style="color:#00dddd; ">-</span><span style="color:#008c00; ">1</span><span style="color:#d2cd86; ">]</span></span>
    <span class="line_wrapper">            self<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">.</span>pop<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span>  <span style="color:#9999a9; "># this will remove the top item in the stack and print it</span></span>
    <span class="line_wrapper">            <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">popped </span><span style="color:#02d045; ">"</span> <span style="color:#00dddd; ">+</span> last_item<span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">        <span style="color:#e66170; font-weight:bold; ">else</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">            <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">Cannot pop from an empty stack. would cause an underflow</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper"><span style="color:#e66170; font-weight:bold; ">def</span> main<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">    my_stack <span style="color:#d2cd86; ">=</span> Stack<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">[</span><span style="color:#d2cd86; ">]</span><span style="color:#d2cd86; ">,</span> <span style="color:#008c00; ">5</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#9999a9; "># can use object's class and method and pass object as parameter</span></span>
    <span class="line_wrapper">    <span style="color:#9999a9; "># print(Stack.is_empty(my_stack))</span></span>
    <span class="line_wrapper">    <span style="color:#9999a9; "># print()</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#9999a9; "># can also use object and parameter together directly</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>is_empty<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#9999a9; "># perform method on my_stack</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>push_to_stack<span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">first</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span>  <span style="color:#9999a9; "># use dot syntax to see my_stack personal stack value</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>is_full<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>push_to_stack<span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">second</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>push_to_stack<span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">third</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>push_to_stack<span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">fourth</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>push_to_stack<span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">fifth</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">trying to add 'sixth' to stack.</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>push_to_stack<span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">sixth</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">stack is full?</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>is_full<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">aobut to pop</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>pop_from_stack<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">stack now: </span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">,</span> my_stack<span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">about to peek the stack</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">top item in the stack:</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>peek<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">for</span> i <span style="color:#e66170; font-weight:bold; ">in</span> <span style="color:#e66170; font-weight:bold; ">range</span><span style="color:#d2cd86; ">(</span><span style="color:#e66170; font-weight:bold; ">len</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">        my_stack<span style="color:#d2cd86; ">.</span>pop_from_stack<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">stack now: </span><span style="color:#02d045; ">"</span> <span style="color:#00dddd; ">+</span> <span style="color:#e66170; font-weight:bold; ">str</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>stack<span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#00c4c4; ">trying to pop from stack now</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>pop_from_stack<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#008080; ">\n</span><span style="color:#00c4c4; ">trying to peek the stack</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    my_stack<span style="color:#d2cd86; ">.</span>peek<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span><span style="color:#02d045; ">"</span><span style="color:#008080; ">\n</span><span style="color:#00c4c4; ">is stack empty?</span><span style="color:#02d045; ">"</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper">    <span style="color:#e66170; font-weight:bold; ">print</span><span style="color:#d2cd86; ">(</span>my_stack<span style="color:#d2cd86; ">.</span>is_empty<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper"></span>
    <span class="line_wrapper"><span style="color:#e66170; font-weight:bold; ">if</span> __name__ <span style="color:#00dddd; ">==</span> <span style="color:#02d045; ">'</span><span style="color:#00c4c4; ">__main__</span><span style="color:#02d045; ">'</span><span style="color:#d2cd86; ">:</span></span>
    <span class="line_wrapper">    main<span style="color:#d2cd86; ">(</span><span style="color:#d2cd86; ">)</span></span>
    <span class="line_wrapper"></span></pre>
</details>
