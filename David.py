from tkinter import *




class Calculator:

    def __init__(self):
        self.no_dup_chars = ['.','*','/']
        self.no_show_chars = ['=','c','C']
        self.last_val = 0
        self.enter_val = 0
        self.window = Tk()
        self.window.bind_all("<Key>",self.keyboard)
        self.display = StringVar()
        entry = Entry(self.window, text=self.display, bg='lightblue')
        entry.bind('<KeyPress>', self.Key)
        entry.grid(row=0, columnspan=4, sticky=NSEW)

        # create items for buttons
        buttons = ['C',
                   '7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '0', '.', '=', '+']
        # Create a starting point to generate buttons
        r = 2
        c = 3
        close = Button(self.window, text="Close", bg='green', command=self.exit)
        close.grid(row=r, column=0, columnspan=2, sticky=NSEW)
        delete = Button(self.window, text="Delete", bg='green', command=self.Delete)
        delete.grid(row=r, column=2, sticky=NSEW)
        self.last_val = 0
        for b in buttons:

            # create buttons with a loop
            button = Button(self.window, text=b,
                            command=lambda btn = b:self.add_to_display(btn))
            button.grid(row=r, column=c, sticky=NSEW)

            if b == '=':
                button.bind('<ButtonRelease-1>', self.Calc)
            elif b == 'C':
                button.bind('<ButtonRelease-1>', self.Clear)
            elif b == '.' or b == '*' or b == '/':
                self.enter_val = b
                button.bind('<ButtonRelease-1>', self.Check)

            # Color Changer
            if c < 3 and r > 2:
                button.configure(bg='grey')
            else:
                button.configure(bg='green')

            # New Row
            c += 1
            if c > 3:
                r += 1
                c = 0

        # Edit grid
        self.GridConfig(self.window, 7, 4, 80)
        self.window.mainloop()

    def add_to_display(self,char):
        txt = self.display.get()
        # print(char)
        if char in self.no_show_chars:
            # print('no_show_chars')
            return
        elif len(txt)==0 and char not in self.no_show_chars:
            # print('0 len')
            self.display.set(txt + char)
            return
        elif (char == txt[-1] and char in self.no_dup_chars):
            return

        else:
            self.display.set(txt + char)
    def keyboard(self,ev):
        # print(ev.char)
        char = ev.char
        # print(ord(char))
        if char in ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']:
            self.add_to_display(char)
        if char == chr(8):
            self.Delete()
        if char == chr(13):
            self.Calc(ev)

    def GridConfig(self,parent, r, c, size):
        _r = 0
        _c = 0
        while _r != r:
            parent.grid_rowconfigure(_r, minsize=size)
            _r += 1
        while _c != c:
            parent.grid_columnconfigure(_c, minsize=size)
            _c += 1

    def Calc(self,ev = 0):
        try:

            self.display.set(round(eval(self.display.get().strip('0')), 4))

        except:
            self.display.set("Please enter valid equation")

    def exit(self,):
        self.window.destroy()

    def Check(self,event):
        char = event.widget.cget("text")
        # print(self.enter_val)

        if char == self.last_val:
            self.Delete()
        # else:
        #     char = self.enter_val

    def Clear(self,event):
        self.display.set('')

    def Delete(self,):
        self.display.set(self.display.get()[:-1])

    def Key(self,event):
        if event.char not in ['C', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']:
            return 'break'




calc = Calculator()
