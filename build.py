import PyInstaller.__main__

if __name__ == '__main__':
    PyInstaller.__main__.run([
        "keygen.py", "-F", "-c", "-i", "static/key.ico", "--version-file", "static/version.txt"
    ])
