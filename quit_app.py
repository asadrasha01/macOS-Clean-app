import subprocess

def quit_all_app():
    script = '''
    with timeout of 600 seconds
        tell application "System Events"
            set quitapps to name of every application process whose background only is false and name is not "Finder" and name is not "Terminal"
        end tell
        repeat with closeapp in quitapps
            tell application closeapp to quit
        end repeat
    end timeout
    '''
    subprocess.run(['osascript', '-e', script])