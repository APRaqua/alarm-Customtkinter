import sys
import customtkinter
import datetime
import time
from pygame import mixer
from threading import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("500X350")

#Use Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()

##playing alarm tone
def playmusic():
       mixer.init()
       selected_ringtone=ring.get()
       mixer.music.load(selected_ringtone)
       mixer.music.play()
       while mixer.music.get_busy():
          time.sleep(30)
          mixer.music.stop()
          sys.exit()


def alarm():
    # Infinite Loop
    while True:
       # Set Alarm
       set_alarm_time = f"{hrs.get()}:{mins.get()}:{sec.get()}"

       # Wait for one seconds
       time.sleep(1)

       # Get current time
       current_time = datetime.datetime.now().strftime("%H:%M:%S")
       print(current_time,set_alarm_time)

       # Check whether set alarm is equal to current time or not
       if current_time == set_alarm_time:
          print("Time to Wake up")
          # Playing sound
          playmusic()

def stop_alarm():
    # Stop the currently playing music
    mixer.music.stop()




label=customtkinter.CTkLabel(root,text="Set Alarm",font=("Roboto",24))
label.grid(row=0,column=2,pady=12,padx=10,sticky='ew')




hours= ('00', '01', '02', '03', '04', '05', '06', '07',
       '08', '09', '10', '11', '12', '13', '14', '15',
       '16', '17', '18', '19', '20', '21', '22', '23', '24'
       )
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
       '08', '09', '10', '11', '12', '13', '14', '15',
       '16', '17', '18', '19', '20', '21', '22', '23',
       '24', '25', '26', '27', '28', '29', '30', '31',
       '32', '33', '34', '35', '36', '37', '38', '39',
       '40', '41', '42', '43', '44', '45', '46', '47',
       '48', '49', '50', '51', '52', '53', '54', '55',
       '56', '57', '58', '59', '60')
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
       '08', '09', '10', '11', '12', '13', '14', '15',
       '16', '17', '18', '19', '20', '21', '22', '23',
       '24', '25', '26', '27', '28', '29', '30', '31',
       '32', '33', '34', '35', '36', '37', '38', '39',
       '40', '41', '42', '43', '44', '45', '46', '47',
       '48', '49', '50', '51', '52', '53', '54', '55',
       '56', '57', '58', '59', '60')

hour=customtkinter.StringVar(root)
hour.set(hours[0])

hlabel=customtkinter.CTkLabel(root,text="Hours:",font=("Arial",16))
hlabel.grid(row=1,column=1,padx=10,pady=10)
hrs=customtkinter.CTkComboBox(master=root,values=hours)
hrs.grid(row=2,column=1,pady=12,padx=10)

mlabel=customtkinter.CTkLabel(root,text="Minutes:",font=("Arial",16))
mlabel.grid(row=1,column=2,padx=10,pady=10)
minute=customtkinter.StringVar(root)
minute.set(minutes[0])
mins=customtkinter.CTkOptionMenu(master=root,values=minutes)
mins.grid(row=2,column=2,pady=12,padx=10)

slabel=customtkinter.CTkLabel(root,text="Seconds:",font=("Arial",16))
slabel.grid(row=1,column=3,padx=10,pady=10)
second=customtkinter.StringVar(root)
second.set(seconds[0])
sec=customtkinter.CTkOptionMenu(master=root,values=seconds)
sec.grid(row=2,column=3,pady=12,padx=10)

rings=("ring1.mp3","ring2.mp3","ring3.mp3","ring4.mp3")
ringtone=customtkinter.StringVar(root)
ringtone.set(rings[0])
rlabel=customtkinter.CTkLabel(root,text="Ringtone:",font=("Arial",18))
rlabel.grid(row=3,column=1,padx=9,pady=12)
ring=customtkinter.CTkComboBox(master=root,values=rings)
ring.grid(row=3,column=2,pady=12,padx=10)

button=customtkinter.CTkButton(master=root,text="Set Alarm",command=Threading,hover_color="light blue",corner_radius=50)
button.grid(row=4,column=2,pady=12,padx=30)

stop_button = customtkinter.CTkButton(master=root, text="Stop Alarm",corner_radius=50)
stop_button.grid(row=5,column=2,padx=10,pady=12)
stop_button.configure(command=stop_alarm)

root.mainloop()