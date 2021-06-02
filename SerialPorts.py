import serial
import serial.tools.list_ports


class SerialPorts:

    def getports(self):
        ports = serial.tools.list_ports.comports()
        for i in range(0,len(ports)):
            ports[i] = str(ports[i])

        return ports
