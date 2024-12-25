import time
import vgamepad as vg

def main():
    print("Control mGBA using the following commands:")
    print("left: Move left (left on the D-Pad)")
    print("right: Move right (right on the D-Pad)")
    print("up: Move up (up on the D-Pad)")
    print("down: Move down (down on the D-Pad)")

    gamepad = vg.VX360Gamepad()  # Create a virtual Xbox 360 gamepad

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "left":
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # Press left on the D-Pad
            gamepad.update()
            time.sleep(0.1)  # Hold the button briefly
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # Release the D-Pad
            gamepad.update()
            print("Sent 'Left' input")
        elif command == "right":
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            print("Sent 'Right' input")
        elif command == "up":
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            print("Sent 'Up' input")
        elif command == "down":
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            print("Sent 'Down' input")
        else:
            print("Invalid command. Please enter left, right, up or down")

if __name__ == "__main__":
    main()
