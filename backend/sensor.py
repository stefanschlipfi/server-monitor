from utils import *
import psutil

init_logger(filename='sensor.log')
import logging
logger = logging.getLogger('outdoor-kitchen')


def get_cpu_temperature():

    json_conf = load_conf()
    cpu_label = json_conf['cpu_label']
    shw = psutil.sensors_temperatures()[cpu_label][0]
    logger.info("Using cpu_label: {0}, temp: {1}".format(cpu_label,shw.current))
    return shw.current