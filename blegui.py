from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from jnius import autoclass

# https://gist.github.com/tito/7432757#file-bluetooth_kivy-py
# BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
# BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
# BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
# UUID = autoclass('java.util.UUID')
#
# def get_socket_stream(name):
#     paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
#     socket = None
#     for device in paired_devices:
#         if device.getName() == name:
#             socket = device.createRfcommSocketToServiceRecord(
#                 UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
#             recv_stream = socket.getInputStream()
#             send_stream = socket.getOutputStream()
#             break
#     socket.connect()
#     return recv_stream, send_stream



class blegui(BoxLayout):
    def readBle(self,dt):

        #to be suppressed on communication with arduino is setup
        if self.ids['pb1'].value == 100:
            self.ids['pb1'].value = 0
        if self.ids['pb2'].value == 100:
            self.ids['pb2'].value = 0
        if self.ids['pb3'].value == 100:
            self.ids['pb3'].value = 0
        val1 = self.ids['pb1'].value + 1
        val2 = self.ids['pb2'].value + 1
        val3 = self.ids['pb3'].value + 1

        self.updatePB((val1, val2, val3))


    def connectBle(self):
        self.ids['pb1'].value = 0
        self.ids['pb2'].value = 50
        self.ids['pb3'].value = 75
        try:
            assert(self.timer)
        except AttributeError:
            self.timer = Clock.schedule_interval(self.readBle, .0005)


    def updatePB(self, vals):
        self.ids['pb1'].value = vals[0]
        self.ids['pb2'].value = vals[1]
        self.ids['pb3'].value = vals[2]
        # print(self.ids['pb1'].value, self.ids['pb2'].value, self.ids['pb3'].value)


class bleguiApp(App):
    def build(self):
        self.recv_stream, self.send_stream = get_socket_stream('linvor')
        self.title = "Rehab"
        return blegui()


if __name__ == '__main__':
    bleguiApp().run()
