import pyautogui
import keyboard  # using module keyboard
import time
import array


class spray_pattern:
    def __init__(name, points):
        self.name = name
        self.points = points


def record_spray(name):
    points = []
    print("Creating new spray " + "'" + name + "'")
    print("Press Enter to continue...")
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('enter'):  # if key 'q' is pressed
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break
    print("Press Enter again to stop...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    while True:  # making a loop
        points.append(pyautogui.position())
        print(pyautogui.position())
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('enter'):  # if key 'q' is pressed
                print('Spray added!')
                print(points)
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break


def main():
    print("Welcome to Spray Controller!")
    print("What would you like to do...\nCreate a Spray: 1\nRun: 2")
    record_spray(raw_input("Name of the spray... \n"))


main()
