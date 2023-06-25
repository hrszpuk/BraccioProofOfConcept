import time
import serial

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
    commands = input(">> ")

send = arduino.write(bytes("S0000", "utf-8"))
print(f"Sent {send} bytes")
time.sleep(0.1)
print(f"Read: {arduino.read_all()}")
arduino.close()
