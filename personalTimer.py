from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivy.clock import Clock

import datetime


KV = '''
Screen: 
    MDLabel:
        id: mylab
        text:"02:00:00" 
        halign: "center"
        font_style: "H2"
    MDIconButton:
        id: playbut
        icon:"play-circle"
        pos_hint:{"center_x":0.4, "center_y":0.7}
        user_font_size:"64sp"
        on_release:app.play()
    MDIconButton:
        icon:"stop-circle"
        pos_hint:{"center_x":0.6, "center_y":0.7}
        user_font_size:"64sp"
        on_release: app.stop()
         

'''

class Test02App(MDApp): 
    def build(self):
        return Builder.load_string(KV)

    def update_time(self, *args): 
        label = self.root.ids.mylab.text 
        self.root.ids.mylab.text = self.removeSecond(datetime.datetime.strptime(label,'%H:%M:%S'),1)

    def removeSecond(self,tm,secs):
        fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
        fulldate = fulldate - datetime.timedelta(seconds=secs)
        return fulldate.time().strftime('%H:%M:%S')  

    def play(self):  
        if self.root.ids.playbut.icon == "play-circle":
            self.event = Clock.schedule_interval(self.update_time,1)
            self.root.ids.playbut.icon = "pause-circle"
        else: 
            self.event.cancel()
            self.root.ids.playbut.icon = "play-circle"

    def stop(self): 
        self.root.ids.mylab.text = "02:00:00"


Test02App().run()        