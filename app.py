import time
import cv2
import numpy as np
import pygetwindow as gw
from PIL import Image
from tkinter import Tk, Label
from PIL import ImageTk
import pyautogui
import win32gui
import win32ui
import win32con
import threading

SCREENSHOT_FREQUENCY = 100 # milliseconds

def get_mgba_window():
    windows = gw.getWindowsWithTitle('mGBA')
    if windows:
        return windows[0]
    return None

def capture_screenshot(window):
    hwnd = window._hWnd  # Get the window handle
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    # Adjust for border and title bar (fine-tune these values if necessary)
    border_size = 8  # Typical padding size
    title_bar_height = 30 + 25  # Approximate title bar height + menu bar height
    left += border_size
    top += title_bar_height
    right -= border_size
    bottom -= border_size

    width = right - left
    height = bottom - top

    # Get the window's device context
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)

    # Attempt to capture only the visible area
    try:
        saveDC.BitBlt((0, 0), (width, height), mfcDC, (border_size, title_bar_height), win32con.SRCCOPY)
    except Exception as e:
        print(f"BitBlt error: {e}")
        return None

    # Convert the bitmap to an image
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    img = np.frombuffer(bmpstr, dtype=np.uint8).reshape(bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)  # Convert to grayscale

    # Cleanup resources
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return img


def update_image(label, window):
    screenshot = capture_screenshot(window)
    img = Image.fromarray(screenshot)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(SCREENSHOT_FREQUENCY, update_image, label, window)

def main():
    window = get_mgba_window()
    if not window:
        print("mGBA window not found")
        return

    root = Tk()
    root.title("mGBA Screenshot Viewer")
    label = Label(root)
    label.pack()

    update_image(label, window)
    root.mainloop()

def controls():
    import controllerControl
    control_thread = threading.Thread(target=controllerControl.main, daemon=True)
    control_thread.start()

controls()

if __name__ == "__main__":
    main()
