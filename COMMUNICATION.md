# Communication Protocol
In order to control the robot in real time we must have a way to communicate with it.
The Arduino already has a serial port/cable for uploading scripts, so we may as well use that.

| Command        | Description                                               |
|----------------|-----------------------------------------------------------|
| SETUP          | Moves the Arduino into the default position.              |
| START          | Start sending rotation instructions to the arduino.       |
| END            | Stop sending rotation instructions to the arduino.        |
| ROTATE         | Tell the robot arm to rotate (`ROTATE [MOTOR] [DEGREES]`) |
| SET_DEFAULT    | Sets the default position for the Arduino to move to.     |

In the frontend the user may type `rotate M2 90` (rotate Motor 2 90 degrees) and it will be sent to the backend.

| Constants | Description                                                                   |
|-----------|-------------------------------------------------------------------------------|
| M1        | Reference the M1 motor when rotating.                                         |
| M2        | Reference the M2 motor when rotating.                                         |
| M3        | Reference the M3 motor when rotating.                                         |
| M4        | Reference the M4 motor when rotating.                                         |
| M5        | Reference the M5 motor when rotating.                                         |
| M6        | Reference the M6 motor when rotating.                                         |
| DEFAULT   | Reference the default motor position (returns motor to its original position. |

The frontend will keep track of the current motor value, calculate the new motor value, then send that value to the Arduino.
