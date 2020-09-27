from utils import *
import psutil

init_logger(filename='sensor.log',stream=False,logger_name='sensor')
import logging
logger = logging.getLogger('sensor')


def get_temperature():
    """
    get temprature dict from json config file
    return device_dict with temp
    """
    device_dict = {}

    sensors = load_conf()['sensors']
    for device,name in sensors.items():
        shw = psutil.sensors_temperatures()[name][0]
        temp = format(shw.current, '.2f')
        d_dict = {'temperature':temp}
        logger.debug("Using {0},name: {1}, temp: {2}".format(device,name,temp))

        if device == 'cpu':
            d_dict.update({'cores':psutil.cpu_count()})

        device_dict[device] = d_dict
    return device_dict
