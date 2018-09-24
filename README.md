# myTOWN Desktop Application

![alt text](https://i.imgur.com/pPoTIVa.png "myTOWN")

myTOWN is an desktop application I developed at the Elevate Hackathon. This applications serve to manage the storage of passwords and also launches instances of chrome which automatically log you into the respepctive portals. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to install a few pre-requestive libraries along with Python 3.6.4+

```
pip3 install selenium
pip3 install pycryptodome
```

### Installing

A step by step series of examples that tell you how to get a development env running

The first step is create a clone of the repository

```
git clone https://github.com/krishchow/ElevateDesktop.git
```

Next you should change directory into the working directory and then run the GUI file

```
python3 GUI.py
```

If everything is properly you should be greeted by a GUI window!

## Deployment

In order to compile and deploy the application you need to compile the application using pyinstaller

```
pip3 install pyinstaller
pyinstaller --onefile --noconsole GUI.py
```

## Built With

* [Selenium](https://selenium-python.readthedocs.io/) - The web interface we used to automate form filling
* [tkinter](https://docs.python.org/3/library/tk.html) - The library used for creating the Graphical User Interface
* [sqlite3](https://docs.python.org/3.4/library/sqlite3.html) - The library used to create and interface with the primary SQL database
* [Pycrypto](https://pypi.org/project/pycrypto/) - The library used to AES encrypt the passwords for the various platforms
* [threading](https://docs.python.org/3/library/threading.html) - The library used to multithread the GUI to keep it responsive
* [hashlib](https://docs.python.org/3/library/hashlib.html) - The library used to SHA256 hash the passwords 

## Authors

* **Krish Chowdhary** - *Application Development* - [krishchow](https://github.com/krishchow)
* **Robert Nash** - *GUI Styling* - [RobertNash1](https://github.com/RobertNash1)
* **Mary Ma** - *PowerPoint Presentation Development* - [maxiaoyum](https://github.com/maxiaoyum)

See also the list of [contributors](https://github.com/krishchow/ElevateDesktop/contributors) who participated in this project.

## Acknowledgments

* Thank you to the Hackworks team and all of the mentors at the Elevate Hackathon!
