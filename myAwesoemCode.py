import time
import os


class PrettyDecent():
    """
    A Pretty decent class
    """

    def __init__(self):
        self.text = 'This is decent!'
        self.do_something()

    def do_something(self):
        print(self.text)


def main():
    decent = PrettyDecent()

if __name__ == '__main__':
    main()
