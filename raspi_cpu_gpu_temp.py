# coding:utf-8
import os
import Tkinter


root = Tkinter.Tk()
root.title(u"Software Title")
root.geometry("350x50")


def DeleteEntryValue(event):
    cpu_temp,gpu_temp=Temp_get()
    EditBox.delete(0, Tkinter.END)
    EditBox.insert(Tkinter.END,"    CPU_temp="+str(cpu_temp)+"℃  "+"GPU_temp="+gpu_temp+"℃")

def Temp_get():
    
    cpu_file="/opt/vc/bin/vcgencmd measure_temp"
    gpu_file="cat /sys/class/thermal/thermal_zone0/temp"

    cpu_line = os.popen(cpu_file).readline().strip()
    gpu_line = os.popen(gpu_file).readline().strip()
    cpu_temp = cpu_line.split('=')[1].split("'")[0]
    gpu_temp = float(gpu_line)/1000

    

    return cpu_temp,str(gpu_temp)


EditBox = Tkinter.Entry(width=35)
EditBox.insert(Tkinter.END,"")
EditBox.pack()


Button = Tkinter.Button(text=u'raspi_temp', width=25)
Button.bind("<Button-1>",DeleteEntryValue) 

Button.pack()

root.mainloop()