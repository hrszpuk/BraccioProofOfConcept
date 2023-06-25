# Communication Protocol
In order to control the robot in real time we must have a way to communicate with it.
The Arduino already has a serial port/cable for uploading scripts, so we may as well use that.

For this proof of concept I've decided to use 5 bytes to represent each instruction.
The first byte is the instruction byte. This will be a letter such as `R` or `S`
The second byte is the motor byte. This will be a digit representing a motor.
The final 3 bytes are used to represent the degrees the motor is moving.

| Command        | Description                                               | Letter |
|----------------|-----------------------------------------------------------|:------:|
| SETUP          | Moves the Arduino into the default position.              |   S    |
| ROTATE         | Tell the robot arm to rotate (`ROTATE [MOTOR] [DEGREES]`) |   R    |

In the frontend the user may type `rotate M2 90` (rotate Motor 2 90 degrees) and it will be sent to the backend as `R1090`.

| Constants | Description                                                                    | Number |
|-----------|--------------------------------------------------------------------------------|:------:|
| M1        | Reference the M1 motor when rotating.                                          |   1    |
| M2        | Reference the M2 motor when rotating.                                          |   2    |
| M3        | Reference the M3 motor when rotating.                                          |   3    |
| M4        | Reference the M4 motor when rotating.                                          |   4    |
| M5        | Reference the M5 motor when rotating.                                          |   5    |
| M6        | Reference the M6 motor when rotating.                                          |   6    |
| DEFAULT   | Reference the default motor position (returns motor to its original position). |  999   |

The major flaw for this design is that the motors can only be moved consecutively despite the fact the braccio library allows for motors to be controlled concurrently.
In this case, the design could be scaled up to use a variable length 25-byte capacity instruction set (example: `R109021563045417751006099`).