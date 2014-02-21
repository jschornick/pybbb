""" Access GPIO pins via SysFS interface """

import os
class GPIO(object):

    def __init__(self, num):
        if not (2 <= num <= 117):
            raise ValueError('GPIO num must be in 2-117')
        self.sysfs = '/sys/class/gpio/gpio' + str(num)
        self.value_path = self.sysfs + "/value"
        self.direction_path = self.sysfs + "/direction"
        self.num = num
        self.direction = None

    def get_value(self):
        """ Approx 10kHz (0.10 ms per read), 70% faster than File.open() """
        fd = os.open(self.value_path, os.O_RDONLY)
        val = os.read(fd,1)
        os.close(fd)
        return ord(val[0]) - ord('0')

    def set_value(self, val):
        fd = os.open(self.value_path, os.O_WRONLY)
        os.write(fd, str(val) + '\n')
        os.close(fd)

    value = property(get_value, set_value)

    def input(self):
        with open(self.direction_path, 'w') as f:
            f.write('in\n')
        self.direction = 'in'

    def output(self):
        with open(self.direction_path, 'w') as f:
            f.write('out\n')
        self.direction = 'in'

    def __str__(self):
        return "GPIO %d (%s) " % (self.num, self.direction)


