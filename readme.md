## Project Overview

This script enables hands-free control of YouTube playback and desktop cursor actions via voice commands. It listens for speech, maps keywords to media controls or mouse automation, and executes actions like play/pause, seeking, speed adjustment, cursor movement, and clicking.

### What This Script Does
- Captures microphone input and performs speech recognition  
- Maps recognized phrases to YouTube media controls (play, pause, seek, speed)  
- Automates mouse movement and clicks based on voice (“move right”, “click”)  
- Runs continuously, listening for commands until terminated

### Key Benefits
- Hands-free media control for presentations or accessibility  
- Customizable command set for specialized workflows  
- Combines media playback and cursor automation in one tool  
- Leverages open-source libraries (SpeechRecognition, PyAutoGUI)

### When to Use
- Controlling YouTube videos without keyboard or mouse  
- Automating repetitive cursor tasks via voice  
- Prototyping voice interfaces for media applications  
- Building assistive tools or smart-environment demos

### Core Capabilities
- Play, pause, stop, and resume YouTube videos  
- Seek forward/backward by configurable intervals  
- Increase or decrease playback speed  
- Move cursor in cardinal directions or relative offsets  
- Perform left/right clicks and drag actions  

#### Running the Script
Install dependencies and launch the controller:
```bash
pip install SpeechRecognition PyAudio PyAutoGUI
python yt.py
```
Speak commands like “play”, “pause”, “seek forward 10 seconds”, “speed up”, “move mouse right”, or “click”.

#### Extending Voice Commands
Open yt.py and locate the command-to-handler mapping (usually a `commands` dict). Add new entries to customize behavior:
```python
import pyautogui

# Define a new handler
def mute_video():
    # Press YouTube’s mute shortcut
    pyautogui.press('m')

# Register under your chosen keyword
commands['mute'] = mute_video
```
Restart the script, then say “mute” to toggle mute on the active video.
## Installation & Quick Start

Get voice-controlled YouTube playback and cursor automation running in minutes.

### 1. Clone the Repository  
```bash
git clone https://github.com/NidhiDodiya1014/TV_OpenCV.git
cd TV_OpenCV
```

### 2. Create & Activate Virtual Environment  
Linux/macOS  
```bash
python3 -m venv venv
source venv/bin/activate
```  
Windows (PowerShell)  
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies  
A `requirements.txt` covers core packages:  
```bash
pip install -r requirements.txt
```  
If you need to install manually:  
```bash
pip install SpeechRecognition PyAudio pyautogui opencv-python pafy youtube-dl
```

#### Troubleshooting PyAudio on Windows  
Download the matching `.whl` from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install:  
```powershell
pip install PyAudio-<version>-cp37-cp37m-win_amd64.whl
```

### 4. Verify Microphone Access  
Run a quick test to list available microphones:  
```bash
python - <<EOF
import speech_recognition as sr
print(sr.Microphone.list_microphone_names())
EOF
```  
Ensure your preferred device appears.

### 5. Launch the Voice Controller  
Invoke `yt.py` with a YouTube URL:  
```bash
python yt.py --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```  
You’ll see console prompts:
```
Listening for commands…
```

### 6. Try Your First Commands  
• “play” → starts playback  
• “pause” → pauses video  
• “seek forward 10 seconds”  
• “speed 1.5” → set playback rate  
• “move cursor to top left”  
• “click” → simulates mouse click  

### 7. Next Steps  
- Customize command-handler mapping in `yt.py`  
- Extend with new voice actions (e.g., volume control)  
- Integrate OpenCV-based screen detection from other modules in this repo  

You’re all set—enjoy hands-free YouTube control!
## Voice Commands & Usage

This section lists all supported voice commands in `yt.py`, shows day-to-day usage examples and gives tips to improve speech-recognition accuracy.

### Recognized Voice Commands

- **Playback Control**
  - “play” / “pause”
  - “stop”
  - “seek forward `<n>` seconds”
  - “seek backward `<n>` seconds”
  - “set speed to `<x>`” (e.g., “set speed to 1.25”)
- **Volume Control**
  - “volume up”
  - “volume down”
  - “mute” / “unmute”
- **YouTube Navigation**
  - “open video `<video_url>`”
  - “search `<keywords>`”
- **Cursor Automation**
  - “move cursor `<direction>` `<n>` pixels” (directions: up, down, left, right)
  - “click” (left-click at current position)
  - “double click”
  - “right click”
- **Custom Commands**
  - Extend the `commands` dict in `yt.py` to map new phrases to callback functions.

### Quick Start

1. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the script  
   ```bash
   python yt.py
   ```
3. Speak one of the commands above into your microphone.

### Usage Examples

#### 1. Play & Pause
```bash
# Start playback of current YouTube tab
> “play”

# Pause video
> “pause”
```

#### 2. Seeking
```bash
# Jump ahead by 15 seconds
> “seek forward 15 seconds”

# Go back 10 seconds
> “seek backward 10 seconds”
```

#### 3. Speed Adjustment
```bash
# Speed up to 1.5×
> “set speed to 1.5”

# Restore normal speed
> “set speed to 1.0”
```

#### 4. Opening & Searching Videos
```bash
# Open a specific YouTube URL
> “open video https://www.youtube.com/watch?v=dQw4w9WgXcQ”

# Search for “open source computer vision tutorial”
> “search open source computer vision tutorial”
```

#### 5. Cursor Movements & Clicks
```bash
# Move cursor down by 100 pixels
> “move cursor down 100 pixels”

# Single left-click
> “click”

# Right-click
> “right click”
```

### Tips for Reliable Recognition

- **Quiet Environment**: Minimize background noise and echo.
- **Clear Pronunciation**: Speak commands distinctly; pause slightly before keywords.
- **Consistent Microphone Position**: Keep mic fixed at ~6–12 inches from your mouth.
- **Phrase Pacing**: Do not rush phrases; allow 1 second between words.
- **Custom Grammar**: For specialized commands, update `r.recognize_google(..., language='en-US')` and tweak the `commands` mapping in `yt.py`.
- **Error Handling**: The script retries on `UnknownValueError`; watch the console logs for misinterpreted phrases.

### Extending Commands

1. Open `yt.py`.
2. Locate the `commands` dictionary:
   ```python
   commands = {
       "play":    lambda: toggle_playback(),
       "pause":   lambda: toggle_playback(),
       # ...
   }
   ```
3. Add your phrase and bind to a handler:
   ```python
   commands["next chapter"] = lambda: seek_forward(60)  # jump 1 minute
   ```
4. Restart the script and speak your new command.

With these voice commands and best practices, you can control YouTube playback and automate cursor actions hands-free. Enjoy seamless media control!
## Customization & Development

This section shows how to extend yt.py by adding or modifying voice commands, changing hotkeys, and tuning command execution timings. All examples assume you’re working in the `NidhiDodiya1014/TV_OpenCV` repo and have installed its dependencies.

### Command Dictionary Structure

In `yt.py`, YouTubeController defines a `commands` dictionary mapping spoken phrases to actions:

```python
import time
import pyautogui

class YouTubeController:
    def __init__(self):
        # phrase -> { hotkey: str, callback: callable, delay: float }
        self.commands = {
            "play":       { "hotkey": "space", "delay": 0.1 },
            "pause":      { "hotkey": "space", "delay": 0.1 },
            "forward":    { "callback": lambda: self.seek(5), "delay": 0.2 },
            "rewind":     { "callback": lambda: self.seek(-5), "delay": 0.2 },
            "speed up":   { "hotkey": "]",     "delay": 0.1 },
            "slow down":  { "hotkey": "[",     "delay": 0.1 },
            # ...
        }

    def seek(self, seconds: int):
        """Seek video by pressing arrow keys in a loop."""
        key = "right" if seconds > 0 else "left"
        for _ in range(abs(seconds) // 5):
            pyautogui.press(key)
            time.sleep(0.05)
```

- **hotkey**: single key or key name passed to `pyautogui.press`
- **callback**: custom function to run instead of pressing a hotkey
- **delay**: pause after action (in seconds)

### Adding a New Voice Command

1. Open `yt.py`.
2. In `__init__`, append a new entry to `self.commands`.  
3. Choose between a simple hotkey or a callback.

Example: add “louder” to increase volume (Up arrow) and “screenshot” to grab a frame.

```python
class YouTubeController:
    def __init__(self):
        self.commands.update({
            "louder": {
                "hotkey": "up",
                "delay": 0.1
            },
            "screenshot": {
                "callback": self.take_screenshot,
                "delay": 0.5
            }
        })

    def take_screenshot(self):
        """Capture current screen and save to disk."""
        img = pyautogui.screenshot()
        timestamp = int(time.time())
        filename = f"screenshot_{timestamp}.png"
        img.save(filename)
        print(f"Saved {filename}")
```

### Modifying Existing Commands

- **Change hotkey**: edit the `"hotkey"` value.
- **Adjust delay**: modify the `"delay"` to speed up or slow down execution.
- **Switch to callback**: replace `"hotkey"` with `"callback"` to run custom logic.

```diff
- "speed up": { "hotkey": "]", "delay": 0.1 },
+ "speed up": {
+     "callback": lambda: self.adjust_speed(0.25),
+     "delay": 0.2
  }
```

### Custom Callback Logic

For complex actions, define new methods in `YouTubeController`:

```python
class YouTubeController:
    # ...
    def adjust_speed(self, delta: float):
        """Increase/decrease playback speed by delta."""
        # Example: open console, type command, close console
        pyautogui.keyDown('shift')
        pyautogui.press('i')  # open dev-tools
        pyautogui.keyUp('shift')
        time.sleep(0.2)
        pyautogui.typewrite(f'document.querySelector("video").playbackRate += {delta}\n')
        time.sleep(0.1)
        pyautogui.keyDown('shift')
        pyautogui.press('i')  # close dev-tools
        pyautogui.keyUp('shift')
```

Register it:

```python
self.commands["faster"] = {
    "callback": lambda: self.adjust_speed(0.1),
    "delay": 0.3
}
self.commands["slower"] = {
    "callback": lambda: self.adjust_speed(-0.1),
    "delay": 0.3
}
```

### Tweaking Recognition Timing

In `yt.py`, you can adjust how long the recognizer listens or pauses between commands:

```python
recognizer = sr.Recognizer()
with sr.Microphone() as mic:
    recognizer.pause_threshold = 0.5    # seconds of silence before processing
    recognizer.energy_threshold = 300   # ambient noise level
    audio = recognizer.listen(mic, timeout=5, phrase_time_limit=4)
```

Modify `pause_threshold`, `timeout`, or `phrase_time_limit` to suit your environment.

### Testing Your Changes

1. Run updated script:  
   ```bash
   python yt.py
   ```
2. Speak your new or modified commands clearly.
3. Observe console logs and action delays.
4. Iterate: tweak hotkeys, delays, or callback code until behavior matches expectations.

By editing the `commands` dictionary and adding custom methods, you can tailor yt.py’s voice controls to any media or UI automation task.
