"""
Author: r4jdeepbiswas@gmail.com
"""


import datetime
import logging


logging.basicConfig(level=logging.DEBUG)


class Timer:
    
    def __init__(self):
        """
        Constructor that initializes timestamps to empty strings.
        """
        startts = ""
        endts = ""
    

    def markStart(self):
        """
        Marks start of event and logs out timestamp.
        """
        self.startts = datetime.datetime.now()
        logging.debug("started processing: " + str(self.startts))
    

    def markEnd(self):
        """
        Marks end of event and logs out timestamp and the total duration that was taken.
        """
        self.endts = datetime.datetime.now()
        logging.debug("done processing:" + str(self.endts))
        logging.debug("this operation took:" + str(self.endts - self.startts))
