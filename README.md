# CiaServer
This is a small helper script which allows you to install CIA files via FBI over your local network.

### Note to windows users
To use this tool you need Python3 to be installed. Make sure you check `Add to path` setting. If you do not want to add python to PATH
you need to change `PYTHON_PATH` variable in `install_windows_context_menu.cmd` to correct location.

## Installation
To run this script couple of additional python modules need to be installed:

```
pip install qrcode --user
pip install pillow --user
```

## Usage 

### KDE

```
$ bash install_kde_service_menu.sh
```

then it will be available right in the context menu `Actions/Install from QR Code`.

### Linux / macos

```
$ ./CiaServer.py path/to/game.cia
```
### Windows

Double click on `install_windows_context_menu.cmd` to setup file associations. After that you can just double click .CIA file in Windows Explorer.

Also you can run it as usual from command line:

```
C:\> python CiaServer.py path\to\game.cia
```
