import os, sys
import pathlib

# installation de pyinstaller
os.system(sys.executable + " -m pip install pyinstaller --upgrade")

# Path: 
path = pathlib.Path(__file__).parent.absolute()

command = "pyinstaller"

target = "application.py"

# Options
options = [
    "--onefile",
    "--noconsole",
    "--icon=assets/graphics/SuperCandy.ico",
    "--name=CandyCrush",
    "--add-data=assets;assets",
    "--add-data=lib;lib",
    "--hidden-import=PIL",
    "--collect-submodules=PIL",
    # disable hooks
    "--exclude-module=PyQt5",
    "--exclude-module=PyQt5.QtCore",
    "--exclude-module=PyQt5.QtGui",
    "--exclude-module=PyQt5.QtWidgets",
    "--exclude-module=PyQt5.QtNetwork",
    "--exclude-module=PyQt5.QtPrintSupport",
    "--exclude-module=PyQt5.QtSvg",
    "--exclude-module=PyQt5.QtTest",
    "--exclude-module=PyQt5.QtWebChannel",
    "--exclude-module=PyQt5.QtWebEngineCore",
    "--exclude-module=PyQt5.QtWebEngineWidgets",
    "--exclude-module=PyQt5.QtWebSockets",
    "--exclude-module=PyQt5.QtXml",
    "--exclude-module=PyQt5.QtXmlPatterns",
    "--exclude-module=PyQt5.sip",
    "--exclude-module=PyQt5.uic",
    "--exclude-module=PyQt5.uic.port_v2",
    "--exclude-module=PyQt5.uic.port_v3",
    "--exclude-module=PyQt5.uic.properties",
    "--exclude-module=PyQt5.uic.Compiler",
    "--exclude-module=PyQt5.uic.Compiler.qtproxies",
    "--exclude-module=PyQt5.uic.Compiler.indenter",
    "--exclude-module=PyQt5.uic.Compiler.qtproxies",
    "--exclude-module=PyQt5.uic.Compiler.indenter",
    "--exclude-module=PyQt5.uic.Compiler.qobjcreator",
    ]


command += " " + " ".join(options) + " " + target

# se mettre dans le dossier du projet
os.chdir(path)

# lancer la commande
os.system(command)
