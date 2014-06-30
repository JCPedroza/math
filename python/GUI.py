import Math
from Tkinter import Tk, Frame, Button, Label, Entry

class TheFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calcutron5000")

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)

        self.entry = Entry(self)
        self.entry.grid(row=0, column=0)

        gcdButton = Button(self, text="gcd", command=self.gcd)
        gcdButton.grid(row=1, column=0)
        lcmButton = Button(self, text="lcm", command=self.lcm)
        lcmButton.grid(row=1, column=1)
        factorsButton = Button(self, text="factors", command=self.factors_of)
        factorsButton.grid(row=1, column=2)
        isprimeButton = Button(self, text="is prime?", command=self.is_prime)
        isprimeButton.grid(row=2, column=0)
        issquareButton = Button(self, text="is square?", command=self.is_square)
        issquareButton.grid(row=2, column=1)
        squarefactorsButton = Button(self, text="square factors", command=self.square_factors_of)
        squarefactorsButton.grid(row=2, column=2)

        self.result = Label(self, text="Results here")
        self.result.grid(row=3, column=0)

        self.pack()
        self.centerWindow()

    def centerWindow(self):
        w = 400
        h = 400
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))

    # ==================
    #  Input Handling
    # ==================

    def get_entry(self):
        """ Parses the entry input, from string to float. Ignores non-digit strings. """
        return map(float, filter(lambda x: x.isdigit(), self.entry.get().split()))

    def input_is_valid(self, input, min_size, max_size=10):
        """ Checks that the input has the desired specifications. """
        length = len(input)
        if length < min_size:
            self.result.config(text="Requires at least {0} numbers".format(min_size))
            return False
        if length > max_size:
            self.result.config(text="Max {0} numbers".format(max_size))
            return False
        return True

    # ==================
    #    Operations
    # ==================

    def gcd(self):
        """ Return greatest common divisor using Euclid's Algorithm. """
        entry = self.get_entry()
        if self.input_is_valid(entry, 2):
            result = Math.gcdm(entry[0], entry[1])
            self.result.config(text=result)

    def lcm(self):
        """ Return lowest common multiple. """
        entry = self.get_entry()
        if self.input_is_valid(entry, 2):
            result = Math.lcmm(*entry)
            self.result.config(text=result)

    def factors_of(self):
        """ Return a set of the factors of entry. """
        entry = self.get_entry()
        if self.input_is_valid(entry, 1):
            result = sorted(Math.factors_of(entry[0]))
            self.result.config(text=result)

    def is_prime(self):
        """ Check if entry is a prime number. """
        entry = self.get_entry()
        if self.input_is_valid(entry, 1):
            result = Math.is_prime(entry[0])
            self.result.config(text=str(result))

    def is_square(self):
        """ Check if entry is a perfect square, based on the Babylonian algorithm. """
        entry = self.get_entry()
        if self.input_is_valid(entry, 1):
            result = Math.is_square(entry[0])
            self.result.config(text=str(result))

    def square_factors_of(self):
        """ Return a set of the factors of entry that are perfect squares. """
        entry = self.get_entry()
        if self.input_is_valid(entry, 1):
            result = sorted(Math.square_factors_of(entry[0]))
            self.result.config(text=result)

def main():
    root = Tk()
    app = TheFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()