import serial
import tkinter as tk
import platform

def Interface():
    app = tk.Tk()
    app.title("Send Message")
    app.geometry("200x200")

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
    TryConnection(msg)

# Try connection and send message
def TryConnection(message):
    try:
        ser = serial.Serial(serial_port.get(), baud_rate.get(), timeout=1)
        print("Connection Established")
        ser.write(message.encode())
        ser.close()
    except serial.SerialException:
        print("Connection Error. Check the Port")

if __name__ == "__main__":
    Interface()    