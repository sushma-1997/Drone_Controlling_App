# sprint1-team_8_sprint_1

# To Run the Plane Control Application

This guide will walk you through the steps to run the Plane Control Application. The application is composed of two parts: a Flask server, and a Flutter application.

# Step 1: Clone the Repository

https://github.com/SLUSE-Spring2022/sprint1-team_8_sprint_1.git

# Step 2: Set up the Flask Server

1. Open a terminal and navigate to the cloned repository

2. Create a Python virtual environment and activate it

``` 
 python3 -m venv venv
 source venv/bin/activate
```
3. Install the required libraries with pip

``` 
 pip install -r requirements.txt
```
4. Run the Flask server

```
 flask run
```
The server will run on http://localhost:5000 by default.


# Step 3: Set up the ArduPilot Software

1. Open another terminal and navigate to the directory where ArduPilot is installed

2. Start the simulator with the following command 

```
 sim_vehicle.py -v ArduPlane --map --console
```
# Step 4: Set up the Flutter Application

1. Open a new terminal and navigate to the Plane_Application_Mobile directory

2. Check that Flutter is installed and in your path by running
```
 flutter doctor
```
If flutter not installed,

Download the Flutter SDK for your operating system from the official Flutter website:
```
https://flutter.dev/docs/get-started/install
```
Add Flutter to PATH:
Add the following line to your shell profile (.bashrc, .zshrc, etc.):
```
 export PATH="$PATH:[path-to-flutter-sdk]/flutter/bin"
```
Replace [path-to-flutter-sdk] with the actual path to your Flutter SDK the extracted file just you downloded.


3. Run the following command to install the dependencies
```
flutter pub get
```

4. Check the list of available emulators with the following command
```
flutter emulators
```
5. Activate your emulator with the following command, replacing <emulator_id> with the ID of the emulator you want to use:
```
 flutter emulators --launch <emulator_id>
```

for ios
```
 flutter emulators --launch ios
```
It will launch the flutter emulator in a side window ( apporx waiting time: 1 min) 

6. Run the Flutter application
```
flutter run
```
The application should launch and connect to the Flask server running on your computer 

**(sometimes flutter may take some time to connect the whole setup my ideal time to suggest wait 15 seconds to make sure flutter application is ready to use)**

When it is ready you can perfom the ARM and DISARM functions from the application to plane via flask. 

We've added new widgets that allow the user to control the plane's throttle and elevator settings of the plane through the UI using arrow buttons.To increase either value, the user taps the upward arrow button. To decrease, they tap the downward arrow button. The current percentage value is displayed between the two arrow buttons.










