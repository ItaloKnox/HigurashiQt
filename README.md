# HigurashiQt

This is part of an ongoing project to port the 
[Higurashi_Installer_WPF](https://github.com/07th-mod/Higurashi_Installer_WPF) to Qt for multiplataform 
support in Python. Currently this repo only holds a functional version of the installer in Python with 
command line support.

## Dependencies:

* Python 3.7
* aria2c
* 7-zip (commandline)

**This installer currently works on Windows and Linux**. Remember that Windows needs to have the 
dependencies fully accessible from the cmd to make this installer work. Install with 
[Chocolatey](https://chocolatey.org/) if you are unsure how to proceed.

**Mac is currently unsuported because of the lack of compatible path structure.** This is going to be 
fixed before the first stable release.

## How to use the command line tool

1. Put the file ``instaler.py`` inside the game folder. [Check 
here](http://07th-mod.com/wiki/Higurashi/Higurashi-Getting-started/) for a list of compatible games.
2. Run ``py install.py <chapter>`` to start the installation. Here are some examples:
	* ``py install.py Himatsubushi``
	* ``py install.py ConsoleArcs``
	* ``py install.py Tsumihoroboshi``
3. Wait until the installation is finished.
