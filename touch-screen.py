import evdev
from evdev import InputDevice, categorize, ecodes

device = evdev.InputDevice('/dev/input/event3')
print device

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        #print categorize(event)
        #print event.type, event.code, event.value
        if event.code == ecodes.BTN_TOUCH and event.value == 1:
            #print 'You touched me'
            fr = open('/tmp/marquee-mode', 'r')
            mode = fr.readline().replace('\n','')
            fr.close()
            fw = open('/tmp/marquee-mode', 'w')
            if mode == '1':
                fw.write('2')
            elif mode == '2':
                fw.write('1')
            fw.close()
            print mode

'''
import mouse
def test():
    print('cc')

mouse.on_click(test)
mouse.wait(mouse.RIGHT)
'''
