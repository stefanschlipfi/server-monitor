from utils import *
import psutil

init_logger(filename='sensor.log',logger_name='sensor')
import logging
logger = logging.getLogger('sensor')


def get_cpu_temperature():

    json_conf = load_conf()
    cpu_label = json_conf['cpu_label']
    shw = psutil.sensors_temperatures()[cpu_label][0]
    temp = format(shw.current, '.2f')

    logger.info("Using cpu_label: {0}, temp: {1}".format(cpu_label,temp))
    return temp