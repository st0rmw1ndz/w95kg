# win95-keygen

Windows 95 & Office 97 key generator/validator

## Usage

```commandline
usage: keygen.py [-h] [-o] [-r] [-f] [key]

win95-keygen - Windows 95 & Office 97 key generator/validator

positional arguments:
  key           key to validate

options:
  -h, --help    show this help message and exit
  -o, --oem     generate an OEM key
  -r, --retail  generate a retail key
  -f, --office  generate an Office 97 key
```

## Examples

```commandline
py keygen.py -f
Office 97 key: 2278-0499303
```

```commandline
py keygen.py 33899-OEM-0900903-88381
OEM key is valid
```

## Building

Be sure [PyInstaller](https://pyinstaller.org/en/stable/installation.html) is installed. Then, run `build.py` in your terminal. If all goes well, it should be built.

(Tested on Windows 10)