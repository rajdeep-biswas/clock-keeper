"""
Author: r4jdeepbiswas@gmail.com
"""


import datetime


class Timer:
    
    def __init__(self):
        """
        Constructor that initializes timestamps to empty strings.
        """
        startts = ""
        endts = ""
    

    def markStart(self):
        """
        Marks start of event and prints out timestamp.
        """
        self.startts = datetime.datetime.now()
        print("started processing:", self.startts)
    

    def markEnd(self):
        """
        Marks end of event and prints out timestamp and the total duration that was taken.
        """
        self.endts = datetime.datetime.now()
        print("done processing:", self.endts)
        print("this operation took:", self.endts - self.startts)
