'''
    Module ptop.statistics

    Generate stats by using the plugins in the ../plugins directory and gather the common info in one section so as 
    to render the info in the GUI
'''

import os, threading
from ptop.utils import ThreadJob
from ptop.plugins import SENSORS_LIST


class Statistics:
    def __init__(self):
        '''
            Record keeping for primitive system parameters
        '''
        self.plugin_dir = os.path.join(os.path.dirname(__file__),'plugins') #plugins directory
        self.plugins = SENSORS_LIST # plugins list
        self.statistics = {} # statistics object to be passed to the GUI
        for sensor in self.plugins:
            self.statistics[sensor.name] = sensor.currentValue
        self.stop_event = threading.Event()

    def generate(self):
        '''
            Generate the stats using the plugins list periodically
        '''
        for sensor in self.plugins:
            # update the sensors value periodically
            job = ThreadJob(sensor.update,self.stop_event,sensor.interval)
            job.start()



        

