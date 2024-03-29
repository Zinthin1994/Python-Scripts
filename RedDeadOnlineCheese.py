'''
NOTES:
1.)You may need to set up the connection manually in Chiaki and there may be issues with firewall (needs to be turned off)
2.)Sometimes it may not work. Delete and reregister and it will work again


Key to Button Mapping:
Circle = Backspace
Triangle = C
X = Enter/Return
Square = \
D-Pad Right = Right Arrow
D-Pad Left = Left Arrow
D-Pad Up = up Arrow
D-Pad Down = Down Arrow
R1 = 3
L1 = 2 
R3 = 6
L3 = 5
Share = f
Options = o
PS = ESC
Touchpad = t
R2 = 4
L2 = 1
Left Stick Left = [
Left Stick Right = ]
Left Stick Down = Del
Left Stick Up = Ins
Right Stick Left = -
Right Stick Right = =
Right Stick Down = PgDown
Right Stick Up = PgUp


'''
import time
import pydirectinput
import pygetwindow as gw

def find_chiaki_stream_window():
    try:
        return gw.getWindowsWithTitle("Chiaki | Stream")[0]
    except IndexError:
        print("Window not found.")
        return None

def main():
    # Wait for 3 seconds before starting the loop
    time.sleep(3)

    chiaki_window = find_chiaki_stream_window()

    if chiaki_window is not None:
        print("Script started. Press 'Ctrl+C' to stop.")
        try:
            while True:
                # Focus on Chiaki|Stream window
                chiaki_window.activate()

                # Press the '4' key using pydirectinput
                pydirectinput.press('4')

                # Wait for 5 seconds before the next iteration
                time.sleep(5)
                
                pydirectinput.keyDown(']')
                
                time.sleep(5)
                
                pydirectinput.keyUp(']')
                
                pydirectinput.keyDown('[')
                
                time.sleep(5)
                
                pydirectinput.keyUp('[')
                
                pydirectinput.press('enter')
                
                time.sleep(5)
                

        except KeyboardInterrupt:
            print("Script stopped.")
    else:
        print("Chiaki | Stream window not found.")

if __name__ == "__main__":
    main()
        