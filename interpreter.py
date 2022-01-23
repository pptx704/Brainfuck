import os
class _Getch: # Python implementation of C's getchar function
    def __call__(self):
        if os.name == "nt": # if system is windows
            import msvcrt
            return msvcrt.getch().decode()

        else: # if system is posix
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

SIZE = 8 # 8 bit as default
LIMIT = 2**SIZE - 1 # 0 - 255 as default

getch = _Getch() # _Getch's __call__ method would be used as a function later

class I:
    def __init__(self, code = ""):
        """
        Initialization
        """
        self._code = code
        self.commands = {
            # Did this as a replacement of switch statements
            '.': self.period,
            ',': self.comma,
            '+': self.plus,
            '-': self.minus,
            '>': self.gt,
            '<': self.lt,
        }

    def change_code(self, code):
        self._code = code
    
    def interprete(self, code = None):

        if not code: # if whole code in memory has to be interpreted from first
            self.memarray = [0]
            self.memlength = 1
            self.ptr = 0
            code = self._code
            
        lim = len(code)
        i = 0
        while i < lim:
            var = code[i]
            # Since '[' starts a loop, the code will look for the end of the loop
            # and recursively decode all the code snippet inside the outermost []
            if var == '[':
                temp = i
                count = 1
                i += 1
                while count:
                    var = code[i]
                    if var == ']':
                        count -= 1
                    elif var == "[":
                        count += 1
                    i += 1
                i -= 1
                while self.memarray[self.ptr]:
                    self.interprete(code[temp+1:i])

            # for all other cases do the intended task
            self.commands.get(var, self.skip)()
            i += 1

    # ord and chr function is used to convert the characters to ascii
    # number and vice versa so that mathematical operations can be done
    # with ease.
    def period(self):
        val = self.memarray[self.ptr]
        print(chr(val), end="")

    def comma(self):
        self.memarray[self.ptr] = ord(getch())
    
    # extremum values like 0 and LIMIT will turn LIMIT and 0
    # in case of negation or addition in order
    def plus(self):
        if self.memarray[self.ptr] == LIMIT:
            self.memarray[self.ptr] = 0
        else:
            self.memarray[self.ptr] += 1
    
    def minus(self):
        if self.memarray[self.ptr] == 0:
            self.memarray[self.ptr] = LIMIT
        else:
            self.memarray[self.ptr] -= 1

    # This interpreter uses extendible memory on both side unlike
    # brainfuck's usual right extendible memory. Initially there is
    # only one cell when the program starts. But when user is on the
    # leftmost cell and wants to go further left (or same for the right)
    # one cell is added with initial value 0 on the direction user wants 
    # to go.
    def lt(self):
        if self.ptr == 0:
            self.memarray.insert(0,0)
            self.memlength += 1
        else:
            self.ptr -= 1
    
    def gt(self):
        if self.ptr == self.memlength - 1:
            self.memarray.append(0)
            self.memlength += 1
        self.ptr += 1

    # placeholder function for invalid characters
    def skip(self):
        pass