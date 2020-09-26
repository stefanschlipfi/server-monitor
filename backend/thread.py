from threading import Thread
from sensor import get_cpu_temperature,get_ssd_temperature
from time import sleep

from utils import *
init_logger(filename='thread.log',logger_name='thread')
import logging
logger = logging.getLogger('thread')

class CpuTempThread(Thread):
    def __init__(self,socketio,namespace):
        self.delay = 1
        self.socketio = socketio
        self.namespace = namespace
        super().__init__()

    def get_cpu_temperature(self):
        """
        Get Cpu temperature from sensor.py
        """
        logging.info("Entered infinity loop, delay: {}".format(self.delay))
        while True:
            cpu_temp = get_cpu_temperature()
            ssd_temp = get_ssd_temperature()
            self.socketio.emit('cpu temperature',{'data':cpu_temp},namespace = self.namespace)
            self.socketio.emit('ssd temperature',{'data':ssd_temp},namespace = self.namespace)
            sleep(self.delay)

    def run(self):
        self.get_cpu_temperature()