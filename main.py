import serial

# Serial port configs
#porta_serial = '/dev/ttyUSB0'
serial_port = 'COM5'
baud_rate = 9600

# Receive and send the message to arduino
def SendoToArduino():
    msg = input("Digite o comando (a): ")
    TryConnection(msg)

# Try connection and send message
def TryConnection(message):
    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print("Connection Established")
        ser.write(message.encode())
        ser.close()
    except serial.SerialException:
        print("Connection Error. Check the Port")

if __name__ == "__main__":
    SendoToArduino()    