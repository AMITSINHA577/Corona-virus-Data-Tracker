import requests
import  bs4
# import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image ### support to resize img in tkinter
import plyer
import datetime
import threading
import time


def get_html_data():
    url="https://www.mygov.in/covid-19/"
    html_data = requests.get(url)
    bs = bs4.BeautifulSoup(html_data.text,"html.parser")
    covid_data=bs.findAll("span",class_="icount")

    headings = ["Active","Total Cases","Discharged","Deaths"]
    i = 0
    coivd_details = " "
    for data in covid_data:
        # print(headings[i]+data.get_text())
        # print(headings[i] + ":" + data.get_text())
        coivd_details = coivd_details + headings[i] + " : " + data.get_text() + "\n\n"
        i = i+1
    return coivd_details

def refresh():
    new_data = get_html_data()
    datalabel.config(text=new_data)

## notifying function
def notify_me():
    while True:
        plyer.notification.notify(
            title = "Covid 19 cases of india",
            message = get_html_data(),
            timeout = 10,
            app_icon = "icon.ico"
        )
        time.sleep(30)


### GUI
root = Tk()
root.title("covid 19 india details")
root.iconbitmap("icon.ico") 
root.geometry("600x600+225+50")
root.config(bg="LightGray")
# root.config(bg="Navy")
img_resize = Image.open("corona3png.png")
resized = img_resize.resize((300,300),Image.ANTIALIAS)

# corona_img = PhotoImage(file="corona_img.png")
corona_img = ImageTk.PhotoImage(resized)
img_label = Label(root,image=corona_img,bg="LightGray")
img_label.pack()


datalabel = Label(root,text=get_html_data(),font=("poppins",18,"bold"),bg="LightGray")
datalabel.pack()

Refresh_butten = Button(root,text="REFRESH",font=("poppins",18,"bold"),command = refresh,bg="Brown")
Refresh_butten.pack()

### threading 

th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()

