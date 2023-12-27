import datetime 

class Alarm:
  _sound_types = ['Bird', "Chicken"]
  def __init__(self, time, sound=0, status=False):
    self.time = time
    self.sound = Alarm._sound_types[sound] 
    self.status = status

    def set_time(self, time):
      self.time = time
    
    def set_sound(self, sound):
      self.sound = _sound_types[sound]
    
    def toggle_status(self, status):
      if not self.status:
        self.status = True
      else:
        self.status = False

    def _str__(self):
      #Return object props
      pass
class Clock:

  def __init__(self):
    self.current_time = datetime.datetime.now()
    self.alarms = {} # Alarm.time: Alarm

    def set_time(self, time):
      self.current_time = time
      return "Alarm Updated"

    def add_alarm(self, alarm):
      self.alarms[alarm.time] = alarm
      return "Alarm Created"
    
    def remove_alarm(self, time):
      if time in self.alarms:
        del self.alarms[time]
        return "Alarm deleted"
      else:
        return "Alarm doesnt exist"
    
    def check_alarms(self):
      if self.current_time in self.alarms:
        return f"{self.alarms[self.current_time]} is ringing"
    

      

      





