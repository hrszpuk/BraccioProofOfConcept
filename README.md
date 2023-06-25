# Braccio Controller Proof Of Concept
A proof of concept for a robotic arm controller. Written in Python and C++.

The main motivation behind this project is an issue I have with my robot arm.
Since it uses Arduino, I cannot control the arm in real-time.
I must upload a C++ script to the controller *then* run it.
This is really annoying and I think it would be much easier if I could control the robot arm in real time.



https://github.com/hrszpuk/BraccioProofOfConcept/assets/107559570/00ae4d60-5464-45d1-b545-c815d44e7a2e



This prototype will have a console-based interface and will be a predecessor to a fully graphical application (probably written in Java).
For more information about how this works internally, checkout [COMMUNICATION.md](COMMUNICATION.md).

## Project Structure

### Frontend
The frontend of the project is a Python script designed to be used in the terminal.
You'll use this interface to communicate with the Arduino.

Typing "help" with come up with a list of commands and a brief explanation of how the program works.

### Backend
The backend of the project is a C++ Arduino script that listens for commands over the serial port.
