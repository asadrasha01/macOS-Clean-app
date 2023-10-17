# Build app

``` Bash
pyinstaller --name 'macClean' \
            --onefile \
            --icon 'icon48.icns' \
            --windowed \
            --osx-bundle-identifier 'MacClean' \
            main.py
```