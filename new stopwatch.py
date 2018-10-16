from tkinter import *
import numpy as np
import time

'''
def update_timeText():
    if state:
        global timer
        # Every time this function is called,
        # we will increment 1 centisecond (1/100 of a second)
        timer[2] += 1
         
        # Every 100 centisecond is equal to 1 second
        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1
        # Every 60 seconds is equal to 1 min
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1], timer[2])
        # Update the timeText Label box with the current time
        timeText.configure(text=timeString)
    top.after(8, update_timeText)
'''


def update_timeText():
    global lap,stop,fstart,time_,re
    if state:
        elapsed_time=time.clock()-fstart
        timeText.configure(text=convert(time_+elapsed_time))
    top.after(10, update_timeText)


def convert(elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        text='%02d:%02d:%02d' % (minutes, seconds, hseconds)
        return text


def startt():
    global state
    state = True
    global lap,fstart,re,time_
    if re==0:
        
        fstart=time.clock()
        lap=fstart
        pass
    else:
        re=0
        lap=time.clock()
        fstart=time.clock()



def stopp():
    global state
    state = False
    global lap,stop,fstart,time_,re,timelap
    stop=time.clock()
    labstop.configure(text='Time: '+convert(time_+(stop-fstart)))
    time_=time_+(stop-fstart)
    timelap=timelap+(stop-lap)
    if re!=0:
        re=0
        timelap=stop-lap
        

def resett():
    global lap,stop,fstart,re,time_,i,index,labels,timelap
    re=1
    i=0
    index=0
    time_=0
    stop=0
    lap=0
    fstart=0
    timelap=0
    global timer
    timer = [0, 0, 0]
    timeText.configure(text='00:00:00')
    for label in labels:
        label.destroy()
    but4.config(text='Lap',state=DISABLED)
    
def lapp():
    global lap,stop,fstart,i,time_,re,labels,timelap
    stop=time.clock()
    i+=1
    if re==0:
        re=1
        lab1=Label(top,text='Lap '+str(i)+ ' : '+convert(timelap+stop-lap))
        lab1.grid(columnspan=2)
        lap=time.clock()
    else:
        lab1=Label(top,text='Lap '+str(i)+ ' : '+convert(stop-lap))
        lab1.grid(columnspan=2)
        lap=time.clock()
    labels.append(lab1)
re=1
i=0
lap=0
fstart=0
stop=0
index=0
time_=0
labels=[]
timelap=0

def toggle1():
    if but2.config('text')[-1] == 'Start':
        startt()
        but2.config(text='Stop')
        but4.config(text='Lap',command=lapp,state='normal')
    else:
        stopp()
        but2.config(text='Start')
        but4.config(text='Reset',command=resett)
        


state=False
top=Tk()
top.title('Stopwatch')
operator=''

txtdisplay=Label(top,text='Welcome',font=('arial',15))
txtdisplay.grid(row=0,column=0,columnspan=2)

'''
timer = [0, 0, 0]
pattern = '{0:02d}:{1:02d}:{2:02d}'
'''

timeText = Label(top, text="00:00:00", font=("arial", 20))
timeText.grid()

#top.resizable(0,0)

labstop = Label(top, text="", font=("arial", 10))
labstop.grid(row=4,columnspan=2)


but2=Button(top,padx=10,pady=2,bd=8,fg='black',font=('arial',10,'bold'),
           text='Start',command=toggle1)
but2.grid(row=2,columnspan=2)
    
but4=Button(top,padx=10,pady=2,bd=8,fg='black',font=('arial',10,'bold'),
           text='Lap',state=DISABLED)
but4.grid(row=3,columnspan=2)


update_timeText()

top.mainloop()




