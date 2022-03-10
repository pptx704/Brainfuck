# My Brainfu*k Repo

Basically wanted to create something with Brainfu*k but realized that with the smol brain I have, I need to see the cell values real-time so that I can debug. So instead of writing BF programs, I started writing an IDE for myself. Currently I wrote the interpreter only on Python and trying to figure out and working on the IDE with realtime memory array update while someone is coding.

Whatever, since this repo is not only about the IDE but also whatever I do related to brainfu*k will be uploaded in this repo. 

### How to use the interpreter-
1. Download the `interpreter.py` file.
2. Use/Modify the following code snippet-
```python
from interpreter import I
code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
i = I(code)
i.interprete()
# Hello world!
i.change_code("-[------->+<]>--.[--->+<]>++..-----------.--.[--->+<]>+++.--[->+++<]>.--[--->+<]>-.--[->++++<]>-.--------.+++.------.--------.-[--->+<]>.")
i.interprete()
# Goodbye world!
```

### Plans-
- [x] Creating an interpreter
- [ ] Optimize it further
- [ ] Create the IDE (Not possible because of [Halting Problem](https://brilliant.org/wiki/halting-problem/))
- [ ] Write some actual BF program
- [x] Optional: Anything else (Supports both NT and Posix system)