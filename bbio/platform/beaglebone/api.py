# api.py 
# Part of PyBBIO
# github.com/alexanderhiam/PyBBIO
# Apache 2.0 license
# 
# Beaglebone platform API file.


from bbio.platform.platform import detect_platform 
PLATFORM = detect_platform()

if "3.8" in PLATFORM:
  from bone_3_8.adc improt analog_init, analog_cleanup
  from bone_3_8.pwm import pwm_init, pwm_cleanup
  from serial_port import serial_cleanup
  
elif "3.2" in PLATFORM:
  from bone_3_2.adc improt analog_init, analog_cleanup
  from bone_3_2.pwm import pwm_init, pwm_cleanup
  from serial_port import serial_cleanup
  
def platform_init():
  analog_init()
  pwm_init()

def platform_cleanup():
  analog_cleanup()
  pwm_cleanup()
  serial_cleanup()

