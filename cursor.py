import pyautogui
from pynput.mouse import Listener

class Cursor():
    def __init__(self):
        self.pressed = False

    def get_position(self):
        """Cursor informations

        Returns:
            int, int: x and y coordinates
        """
        x, y = pyautogui.position()
        return x, y
    
    def set_position(self, x, y):
        """Move cursor

        Args:
            x (int): x coordinate to move the cursor to
            y (int): y coordinate to move the cursor to
        """
        pyautogui.moveTo(x, y)

    def get_pressed(self, button="left"):
        """Check if the mouse button is pressed

        Args:
            button (str): The button to check (default is "left")

        Returns:
            bool: True if the button is pressed, False otherwise
        """
        return self.pressed