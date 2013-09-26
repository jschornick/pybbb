""" Access ADCs vias SysFS interface """

import glob

class adc(object):

  def __init__(self, num, repeat=8):
    self.num = num
    # need to read a glob here, since numbering is not consistent
    # TODO: verify num is reasonable (0-6)
    self.sysfs = glob.glob('/sys/devices/ocp.*/helper.*/AIN' + str(num))[0]
    self.repeat = repeat

  def __str__(self):
    out = "ADC#%d (%s)" % (self.num, self.sysfs)
    return out

  def read(self, repeat=None):

    if not repeat:
        repeat = self.repeat

    for i in range(repeat):
        val = None
        while not val:
          try:
            with open(self.sysfs, 'r') as f:
              val = f.read()
          except:
            pass

    return int(val)

