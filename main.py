#####################################################
# Packages                                          #
#####################################################

import pytz
import time
import pyautogui
from datetime import datetime
from typing import Optional, Union


#####################################################
# Constants                                         #
#####################################################

COORDINATES: dict = {
        "teams_icon": {"x": 151, "y": 1047},
        "first_pin_icon": {"x": 218, "y": 350},
        "first_pin_message_area": {"x": 658, "y": 309}
    }


#####################################################
# Helper Functions                                  #
#####################################################

def get_current_datetime_ist() -> str:

    """
        Gets the current date and time in IST (Indian Standard Time) format.
    """

    # Define IST timezone
    ist_timezone = pytz.timezone("Asia/Kolkata")

    # Get current datetime in UTC and convert to IST
    current_time_ist = datetime.now(ist_timezone)

    return current_time_ist.strftime("%Y-%m-%d %I:%M%p")


def track_mouse(interval_seconds: Optional[Union[int, float]] = 1) -> None:

    """
        Tracks and logs the current mouse position at regular intervals.
    """

    while True:

        # Get current mouse position
        x, y = pyautogui.position()
        
        # Log the position
        print(f"x: {x}, y: {y}")
        
        # Wait for the specified interval before the next reading
        time.sleep(interval_seconds)


#####################################################
# Functions                                         #
#####################################################

def ziggle() -> None:

    """
        Automates mouse navigation and simulates zigzag-like motion every 1 minute.
    """

    # Travle to Destination

    for position_tag, position_values in COORDINATES.items():
        
        x_coordinate: int = position_values["x"]
        y_coordinate: int = position_values["y"]

        print(f"(Travel) Move To '{position_tag}'")
        pyautogui.moveTo(x = x_coordinate, y = y_coordinate, duration = 0.5)
        
        time.sleep(1)

        pyautogui.click()


    # Walk Around

    counter : int = 1
    swapper : int = 1

    while True:

        time.sleep(60)

        # Get current mouse position
        x, y = pyautogui.position()
        
        pyautogui.moveTo(x, y + (20 * swapper))
        pyautogui.click()

        print(f"(Ziggle {counter}) at {get_current_datetime_ist()}")
        
        counter +=  1
        swapper *= -1


if __name__ == "__main__":

    ziggle()
