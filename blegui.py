from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.clock import Clock


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
        self.title = "Rehab"
        return blegui()


if __name__ == '__main__':
    bleguiApp().run()
