# Basic Keylogger Project

This is a simple keylogger script written in Python using the `pynput` library to capture keystrokes and log them to a file.

## Features
- Logs all keystrokes made by the user.
- Stores the logged keystrokes with a timestamp in a file named `keylog.txt`.
- Stops logging when the "Esc" key is pressed.

## Prerequisites  
ChatGPT

Here is the README.md file for your keylogger project:

# Basic Keylogger Project

This is a simple keylogger script written in Python using the `pynput` library to capture keystrokes and log them to a file.

## Features
- Logs all keystrokes made by the user.
- Stores the logged keystrokes with a timestamp in a file named `keylog.txt`.
- Stops logging when the "Esc" key is pressed.

## Requirements
- Python 3.x
- `pynput` library

You can install using following command:
```bash
pip install pynput
```

## Usage  
1. Clone or download the project files.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. Keylogger will start running and capture all keystrokes in `keylog.txt` file.
4. Press `Esc` to stop keylogger

## Output

```
2024-12-28 18:06:51,302: h
2024-12-28 18:06:51,418: e
2024-12-28 18:06:51,532: l
2024-12-28 18:06:51,669: l
2024-12-28 18:06:51,834: o
2024-12-28 18:06:52,091: Key.enter
2024-12-28 18:06:52,704: Key.ctrl_l
2024-12-28 18:06:53,284: Key.esc
```

## License  
This project is open-source and available under the MIT License.

## Author:  
> Created By: Harsh Gharsandiya