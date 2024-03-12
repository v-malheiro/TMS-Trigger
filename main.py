import serial
import tkinter as tk
import platform
import time

def Interface():

    app = tk.Tk()
    app.title("Send Message")
    app.geometry("200x200")

    connect_button = tk.Button(app, text="Conectar", command=TryConnection)
    connect_button.pack()

    msg_label = tk.Label(app, text="Digite o comando (a): ")
    msg_label.pack()

    global msg_entry
    msg_entry = tk.Entry(app)
    msg_entry.insert(tk.END, "a")
    msg_entry.pack()

    port_label = tk.Label(app, text="Serial Port:")
    port_label.pack()

    global serial_port
    serial_port = tk.Entry(app)
    serial_port.insert(tk.END, "COM5" if platform.system() == "Windows" else "/dev/ttyUSB0")
    serial_port.pack()

    baud_label = tk.Label(app, text="Baud Rate:")
    baud_label.pack()

    global baud_rate
    baud_rate = tk.Entry(app)
    baud_rate.insert(tk.END, "9600")
    baud_rate.pack()

    send_button = tk.Button(app, text="Enviar Mensagem", command=SendoToArduino)
    send_button.pack()

    app.mainloop()

# Receive the message and try connection
def SendoToArduino():
    msg = msg_entry.get()
    ser.write(msg.encode())

# Try connection and send message
def TryConnection():
    try:
        global ser
        ser = serial.Serial(serial_port.get(), baud_rate.get(), timeout=1)
        print("Connection Established")
        #time.sleep(1.0)
        #ser.write(message.encode())
        #ser.close()
    except serial.SerialException:
        print("Connection Error. Check the Port")

Interface()    