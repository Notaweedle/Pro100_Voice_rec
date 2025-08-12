import screen_brightness_control as sbc

def decrease_brightness():
     sbc.set_brightness('-20')

def increase_brightness():
     sbc.set_brightness('+20')

def max_brightness():
     sbc.set_brightness('100')

def min_brightness():
     sbc.set_brightness('0')

max_brightness()



   
    