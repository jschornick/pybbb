""" Access ADCs vias SysFS interface """

import glob

class adc(object):

  def __init__(self, num):
    self.num = num
    # need to read a glob here, since numbering is not consistent
    # TODO: verify num is reasonable (0-6)
    self.sysfs = glob.glob('/sys/devices/ocp.*/helper.*/AIN' + str(num))[0]

  def __str__(self):
    out = "ADC#%d (%s)" % (self.num, self.sysfs)
    return out

  def read(self):
    with open(self.sysfs, 'r') as f:
      f.read()
    val = None
    # Read a second time to ensure we get the current value (bug in ADC driver)
    while not val:
      try:
        with open(self.sysfs, 'r') as f:
          val = f.read()
      except:
        pass
    return int(val)

