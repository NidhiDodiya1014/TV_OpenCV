import pyautogui
import speech_recognition as sr
import time
import re


recognizer = sr.Recognizer()
mic = sr.Microphone()

print("🎙️ Voice-controlled YouTube & Mouse Automation is running...")
print("Say commands like: play, pause, forward, back, speed up, move cursor left/right/up/down, click")


def handle_command(command):
    command = command.lower()

    
    if "play" in command or "pause" in command:
        print("▶️ Toggling Play/Pause")
        pyautogui.press("space")
    elif "forward" in command or "skip" in command:
        print("⏩ Skipping forward 5 seconds")
        pyautogui.press("right")
    elif "back" in command or "rewind" in command:
        print("⏪ Rewinding 5 seconds")
        pyautogui.press("left")
    elif "speed up" in command:
        print("⚡ Speeding up (2x)")
        pyautogui.press(">")
    elif "slow down" in command:
        print("🐢 Slowing down")
        pyautogui.press("<")

    
    elif "button" in command:
        handle_click(command)

    
    elif "" in command and any(d in command for d in ["nidhi", "daya", "upar", "niche"]):
        move_cursor_by_voice(command)

    else:
        print(f"✖ Unrecognized command: {command}")


def move_cursor_by_voice(command):
    direction = None
    pixels = 100  

    if "daya" in command:
        direction = "right"
    elif "nidhi" in command:
        direction = "left"
    elif "upar" in command:
        direction = "up"
    elif "niche" in command:
        direction = "down"

    
    
        pixels = 1000

    x, y = pyautogui.position()
    if direction == "right":
        x += pixels
    elif direction == "left":
        x -= pixels
    elif direction == "up":
        y -= pixels
    elif direction == "down":
        y += pixels

    print(f"🖱️ Moving cursor {direction} by {pixels}px")
    pyautogui.moveTo(x, y, duration=0.3)


def handle_click(command):
    if "double" in command:
        print("🖱️ Double Clicking")
        pyautogui.doubleClick()
    elif "right" in command:
        print("🖱️ Right Clicking")
        pyautogui.rightClick()
    else:
        print("🖱️ Single Clicking")
        pyautogui.click()


with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    while True:
        print("\n🎧 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {command}")
            handle_command(command)

        except sr.WaitTimeoutError:
            print("⌛ Listening timed out.")
            continue
        except sr.UnknownValueError:
            print("❓ Could not understand audio.")
            continue
        except sr.RequestError:
            print("⚠️ Could not connect to speech recognition service.")
            break
