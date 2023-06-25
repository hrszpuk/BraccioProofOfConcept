import time
import serial

help = """
Instructions:
    SETUP                   - All motors enter default position
    ROTATE [ID] [DEGREES]   - Rotate a motor a number of degrees

Motors:
    M1 (base)
    M2 (shoulder)
    M3 (elbow)
    M4 (wrist vertical)
    M5 (wrist rotation)
    M6 (gripper)

NOTE: Degrees must be between 0 and 180 (motor limits)

Examples:
    >> SETUP
    >> ROTATE M1 180 
    >> ROTATE M3 90
"""

print("ARDUINO BRACCIO ROBOT ARM CONTROLLER - Proof Of Concept")

port = input("Enter the port of your Arduino: ")
arduino = serial.Serial(port=port, baudrate=9600, timeout=.1)
arduino.bytesize = 8
arduino.parity = 'N'
arduino.stopbits = 1

print("Setting up serial connection with the Arduino")
time.sleep(1)

print(">> type \"help\" for a list of instructions")

while True:
    command = input(">> ").strip(" \n\r\t").upper()
    if command == "HELP":
        print(help)
    elif command == "SETUP":
        send = arduino.write(bytes("S0000", "utf-8"))
    elif command == "QUIT":
        print("Closing serial connection with the Arduino")
        arduino.close()
    else:
        command = command.split(" ")
        if command[0] != "ROTATE":
            print("Unknown command")
            continue
        elif len(command) != 3:
            print("ROTATE command takes 2 parameters: [ID] [DEGREES]")
        else:
            instruction = "R"
            motor = command[1].removeprefix("M")
            degrees = command[2]

            if len(degrees) < 2:
                degrees = "00" + degrees
            elif len(degrees) < 3:
                degrees = "0" + degrees

            instruction += motor + degrees

            send = arduino.write(bytes(instruction, "utf-8"))

