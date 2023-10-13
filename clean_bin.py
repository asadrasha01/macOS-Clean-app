import subprocess

def cleaning_bin():
    script = 'tell app "Finder" to empty'
    subprocess.run(['osascript', '-e', script])
    print()