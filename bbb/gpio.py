""" Access GPIO pins via SysFS interface """
class gpio(object):

  def __init__(self, num):
    self.sysfs = '/sys/class/gpio/gpio' + str(num)

  # TODO: convert to a property
  def set_value(self, val):
    with open(self.sysfs + '/value', 'w') as f:
      f.write(str(val) + '\n')

  def get_value(self):
    with open(self.sysfs + '/value', 'r') as f:
      x = int(f.read())
    return x

  def input(self):
    with open(self.sysfs + '/direction', 'w') as f:
      f.write('in\n')

  def output(self):
    with open(self.sysfs + '/direction', 'w') as f:
      f.write('out\n')

