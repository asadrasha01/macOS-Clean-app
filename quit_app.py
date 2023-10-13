import subprocess

def quit_all_app():
    script = '''
        tell application "System Events"
            set quitapps to name of every application process whose background only is false and name is not "Finder" and name is not "Terminal"
        end tell
        repeat with closeapp in quitapps
            tell application closeapp to quit
        end repeat
    '''
    subprocess.run(['osascript', '-e', script])
print("Applications which you chose has been succesfully quit")