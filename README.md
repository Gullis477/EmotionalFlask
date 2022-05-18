# Emotionally-aware IDE

Modern IDE:s (Integrated development environment) are technically smart from the computer's perspective but not from an emotional perspective. The main goal of the project is to develop an IDE that can interpret the developer’s emotions and behaviour to enhance their programming performance. The intent of the project is to create a VScode extension prototype, that does not have to be a finished product. The extension should be compatible with three specific devices, not a general solution. The devices which shall be used are Empatica E4 wristband, Epoc+ helmet and GazePoint. A method for processing and analyzing data from these devices should be created and integrated with the extension. This method will contain different metrics from each device along with an algorithm to interpret the data to produce an emotional metric outcome. With the collected data some feedback will be given to the user about their programming performance and possible improvements. 

This extension includes:
- Live graphs from collected data
- Live detection to prevent the user from getting stuck
- Classified emotions based on simulated data
- Notifications based on the emotion
- A user-friendly web page

## How to use:
- Install the files for the flask server from github
- Open the terminal and navigate to the folder
- Type "flask run" in the terminal
- Opten the extension
- If the webview did not open, run the command


## This extension was made for the following devices:
Empatica E4 wristband
Epoc+ helmet
GazePoint


