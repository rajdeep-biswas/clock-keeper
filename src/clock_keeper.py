"""
Author: r4jdeepbiswas@gmail.com
"""


import datetime
import logging


class Timer:
    
    def __init__(self):
        """
        Constructor that initializes timestamps to empty strings.
        """
        startts = ""
        endts = ""
    

    def markStart(self):
        """
        Marks start of event and logging.infos out timestamp.
        """
        self.startts = datetime.datetime.now()
        logging.info("started processing:", self.startts)
    

    def markEnd(self):
        """
        Marks end of event and logging.infos out timestamp and the total duration that was taken.
        """
        self.endts = datetime.datetime.now()
        logging.info("done processing:", self.endts)
        logging.info("this operation took:", self.endts - self.startts)
