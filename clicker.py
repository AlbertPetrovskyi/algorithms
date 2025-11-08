import pyautogui
import time
import random

screen_width, screen_height = pyautogui.size()
waiting = 5
sleep = [0, 0.1]
step = [-40, 40]
step_time = [0, 0.1]

for i in range(waiting):
    if i == 0:
        print("Aim at your target. ", end="")
        time.sleep(1)
        print(f"Clicking starts in {waiting-i} ", end="")
        time.sleep(1)
    if i > 0:
        if i == waiting-1:
            print(f"{waiting - i}. ", end="")
            time.sleep(1)
            print("Started clicking.")
        else:
            print(f"{waiting - i} ", end="")
            time.sleep(1)

x, y = pyautogui.position()

for i in range(10):
    sleep_time = random.uniform(sleep[0], sleep[1])
    x_offset = random.randint(step[0], step[1])
    y_offset = random.randint(step[0], step[1])
    center_duration = random.uniform(step_time[0], step_time[1])
    move_duration = random.uniform(step_time[0], step_time[1])

    pyautogui.moveTo(x, y, duration=center_duration)
    pyautogui.moveRel(x_offset, y_offset, duration=move_duration)
    pyautogui.click()

    time.sleep(sleep_time)

print("Done clicking!")
