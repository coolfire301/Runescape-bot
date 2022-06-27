import pyautogui
import os
import time
import numpy as np
import cv2
from PIL import Image
import imagehash


def search_for_image(large_image, small_image):
    method = cv2.TM_SQDIFF_NORMED
    large_image = cv2.imread(large_image)
    small_image = cv2.imread(small_image)
    result = cv2.matchTemplate(small_image, large_image, method)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc
    ja = "nee"
    if ja == "ja":

            # Step 2: Get the size of the template. This is the same size as the match.
        trows,tcols = small_image.shape[:2]

        # Step 3: Draw the rectangle on large_image
        cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

        # Display the original image with the rectangle around the match.
        cv2.imshow('output',large_image)

        # The image is only displayed if we call this
        cv2.waitKey(0)
    return mnLoc

def take_screenshot(name):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    cv2.imwrite(name, image)

def open_runescape():
    os.startfile(r"C:\Users\timod\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\OldSchool RuneScape")
    time.sleep(5)
    take_screenshot(r"Screenshots\login\runescape_start_up.png")
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    click_loc = search_for_image(r"Screenshots\login\runescape_start_up.png",r"Screenshots\login\existing_user_login.png") 
    pyautogui.moveTo(click_loc)
    pyautogui.click(click_loc)
    pyautogui.write('USER_EMAIL', interval = 0.1)
    pyautogui.press("tab")
    pyautogui.write('User_PASSWORD', interval = 0.1)

    click_loc = search_for_image(r"Screenshots\login\runescape_start_up.png",r"Screenshots\login\world_change_small.PNG")
    pyautogui.moveTo(click_loc)
    pyautogui.click(click_loc)
    take_screenshot(r"Screenshots\login\world_choose.png")
    click_loc = search_for_image(r"Screenshots\login\world_choose.png",r"Screenshots\login\world_316_change.PNG") 
    pyautogui.moveTo(click_loc)
    pyautogui.click(click_loc)
    click_loc = search_for_image(r"Screenshots\login\runescape_start_up.png",r"Screenshots\login\login_login.PNG")
    pyautogui.moveTo(click_loc)
    pyautogui.click(click_loc)

    time.sleep(10)
    take_screenshot(r"Screenshots\login\ready_to_play.png")
    click_loc = search_for_image(r"Screenshots\login\ready_to_play.png",r"Screenshots\login\click_to_play.PNG")
    pyautogui.moveTo(click_loc)
    pyautogui.click(click_loc)
    
def fishing_task():
    take_screenshot(r"Screenshots\fishing\fishing_locations.png")
    click_loc = search_for_image(r"Screenshots\fishing\fishing_locations.png",r"Screenshots\fishing\fishing_spot.PNG")
    pyautogui.click(click_loc)

def check_if_tree_is_down():
    take_screenshot(r"Screenshots\Wood_cutting\wood_locations.png")
    hash0 = imagehash.average_hash(Image.open('Screenshots\Wood_cutting\wood_locations.png')) 
    hash1 = imagehash.average_hash(Image.open('Screenshots\Wood_cutting\cut_down_tree.PNG')) 
    cutoff = 5 # maximum bits that could be different between the hashes. 

    if hash0 - hash1 < cutoff:
      print('images are similar')
    else:
      print('images are not similar')
    
def wood_cutting_task():

    check_if_tree_is_down()
    
    take_screenshot(r"Screenshots\Wood_cutting\wood_locations.png")
    check_if_tree_is_down()
    click_loc = search_for_image(r"Screenshots\Wood_cutting\wood_locations.png",r"Screenshots\Wood_cutting\start_tree.PNG")
    pyautogui.moveRel(click_loc, duration=1)
    pyautogui.click(click_loc)
    pyautogui.click(click_loc)
    pyautogui.click(click_loc)

def fire_making():
    take_screenshot(r"Screenshots\fire_making\fire_making_locations.png")
    click_loc = search_for_image(r"Screenshots\fire_making\fire_making_locations.png",r"Screenshots\fire_making\fire_box.PNG")
    click_loc2 = search_for_image(r"Screenshots\fire_making\fire_making_locations.png",r"Screenshots\fire_making\fire_wood.PNG")
    pyautogui.click(click_loc)
    pyautogui.click(click_loc2)

def move_mouse():
    pyautogui.moveTo(100, 150)
    pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
    pyautogui.dragTo(100, 150)
    pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down


def main():
    #open_runescape()
    #fishing_task()
    for x in range(24):
        #wood_cutting_task()
        #check_if_tree_is_down()
        time.sleep(10)
        fire_making()

main()
