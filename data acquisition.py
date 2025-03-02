
import time
from cursor import Cursor
from webcam import Webcam
from pynput.mouse import Listener
import os
import pandas as pd

subfolder = input("Directory to save images and target to: ")
os.makedirs(subfolder, exist_ok=True)

cursor = Cursor()
cam = Webcam()
cam.directory = subfolder

def on_click(x, y, button, pressed):
    if button == button.left:
        cursor.pressed = pressed

listener = Listener(on_click=on_click)
listener.start()

target = pd.DataFrame(columns=['id', 'x_coordinate', 'y_coordinate'])

nb_pictures = int(input("How many pictures do you wish to take?: "))
id = 0
while True:
    if (cursor.get_pressed()):
        if (id %100 == 0):
            print(f"Pressed: {id}")
        cam.capture(id)

        x, y = cursor.get_position()
        new_row = pd.DataFrame([{'id': id, 'x_coordinate': x, 'y_coordinate': y}])
        target = pd.concat([target, new_row], ignore_index=True)

        id += 1
        time.sleep(0.2)

        if (id >= nb_pictures):
            print("Enough pictures for today...")
            target.to_csv(os.path.join(subfolder, 'target.csv'), index=False)
            break

        # print("Ready for next picture...")

table = pd.read_csv(os.path.join(subfolder, 'target.csv'))
print(table.head())



# if __name__ == "__main__":
    
#     # cursor.set_position(10, 20)

#     while True:
#         # x, y = cursor.get_position()
#         # print(f'x: {x} and y: {y}')
#         # print(cursor.get_pressed())
#         # cursor.set_position(100, 100)
#         print(cursor.get_pressed())