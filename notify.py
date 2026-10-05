import os
import subprocess

# ==============================================================================
# CONFIGURATION DEFAULTS (Modify these to match your application defaults)
# ==============================================================================
DEFAULT_APP_NAME = "Productivity Monitor"
DEFAULT_ICON_PATH = "/home/raja/Personal-Productivity-Tracker/icon64.png"
DEFAULT_PIPE_PATH = "/data/data/com.termux/files/usr/tmp/notify_pipe"


def send(
    title: str, 
    message: str, 
    app_name: str = DEFAULT_APP_NAME, 
    icon_path: str = DEFAULT_ICON_PATH,
    pipe_path: str = DEFAULT_PIPE_PATH
) -> bool:
    """
    Sends a notification from Python using configured default variables or custom overrides.
    
    :param title: Notification headline
    :param message: Body text of the notification
    :param app_name: Application label (defaults to DEFAULT_APP_NAME)
    :param icon_path: Absolute path to custom PNG/SVG or icon theme name (defaults to DEFAULT_ICON_PATH)
    :param pipe_path: Path to PRoot-to-Termux named pipe (defaults to DEFAULT_PIPE_PATH)
    """
    # 1. Direct Named Pipe Method (PRoot -> Termux Host)
    if os.path.exists(pipe_path):
        try:
            with open(pipe_path, "w") as pipe:
                pipe.write(f"{app_name}|{title}|{message}|{icon_path}\n")
            return True
        except Exception:
            pass

    # 2. Desktop Linux Execution (notify-send fallback)
    try:
        display_title = f"[{app_name}] {title}" if app_name else title
        cmd = ["notify-send", display_title, message]
        
        if icon_path:
            cmd.extend(["-i", icon_path])
            
        subprocess.run(cmd, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False



if __name__=="__main__":
    send(
        title="Test Notification",
        message="This is a test notification",
        app_name="Productivity Monitor"
    )
