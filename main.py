from tkinter import * #installed pytube- python youtube package, imported tkinter
import tkinter.font
from pytube import YouTube
import urllib.request
import json
import urllib
import pprint
from tkinter import messagebox as mb
import os.path
from os import path

root = Tk()
Desired_font = tkinter.font.Font( family = "Comic Sans MS",size = 15,  weight = "bold") #standardizing format
#root.geometry('700x500') #size of window
root.resizable(0,0)
root.title("Sachin - Youtube Video Downloader") 

lbl = Label(root,text = 'Youtube Video Downloader')
lbl.pack()
 
link = StringVar()

lbl2 = Label(root, text = 'Paste Link Here:')
lbl2.pack()

link_enter = Entry(root, width = 70,textvariable = link) #entry widget
link_enter.pack()
lbl8 = Label(root, text = 'Enter path to download video:')
lbl8.pack()
lbl8.configure(font = Desired_font)
route = Entry(root, width = 70) #entry widget
route.pack()

def Downloader():     #function that downloads the file in mp4 format
    url =YouTube(str(link.get()))
    if not url:
        mb.showinfo(title= "invalid URL", message="Invalid URL entered! Try Again")#url entered by user from entry widget
    video = url.streams.first()
    url2 = link_enter.get()
    if not len(url2) == 43:
        mb.showinfo(title= "invalid URL", message="Invalid URL entered! Try Again")
    APIKEY = "AIzaSyDS8_NYOwJF9FwiIwRPArFZMyj-uQ8QYmU"
    url3 = link_enter.get()
    VideoID = url3[32:]
    params = {'id': VideoID, 'key': APIKEY,'fields': 'items(id,snippet(channelId,title,categoryId),statistics)','part': 'snippet,statistics'}

    URL = 'https://www.googleapis.com/youtube/v3/videos'

    query_string = urllib.parse.urlencode(params)
    URL = URL + "?" + query_string
    with urllib.request.urlopen(URL) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())    
    if data['items'] == []:
            mb.showinfo(title= "empty URL", message="No URL entered! Try Again")    
    if route.get == '':
        mb.showinfo(title= "empty path", message="No path entered! Try Again")
    if path.exists(route.get()): 
        video.download(output_path = route.get())
    else:
        mb.showinfo(title= "wrong path", message="wrong path entered! Try Again")  

    

def info():
    APIKEY = "AIzaSyDS8_NYOwJF9FwiIwRPArFZMyj-uQ8QYmU"    
    url = link_enter.get()
    VideoID = url[32:]
    if not len(url) == 43:
        mb.showinfo(title= "invalid URL", message="Invalid URL entered! Try Again")
    #    mb.showinfo(title= "invalid URL", message="Invalid URL entered! Try Again")
    params = {'id': VideoID, 'key': APIKEY,'fields': 'items(id,snippet(channelId,title,categoryId),statistics)','part': 'snippet,statistics'}

    URL = 'https://www.googleapis.com/youtube/v3/videos'

    query_string = urllib.parse.urlencode(params)
    URL = URL + "?" + query_string

    with urllib.request.urlopen(URL) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        if data['items'] == []:
            mb.showinfo(title= "invalid URL", message="Invalid URL entered! Try Again")
        #pprint.pprint(data)
        #print("TITLE: %s " % data['items'][0]['snippet']['title'])
        lbl4 = Label(root, text = "TITLE --> " + data['items'][0]['snippet']['title'])
        lbl4.pack()      
        lbl4.configure(font = Desired_font) 
        lbl5 = Label(root, text = "LIKES -->" + data['items'][0]['statistics']['likeCount'])
        lbl5.pack()      
        lbl5.configure(font = Desired_font) 
        lbl8 = Label(root, text = "COMMENTS -->" + data['items'][0]['statistics']['commentCount'])
        lbl8.pack()      
        lbl8.configure(font = Desired_font)
        lbl7 = Label(root, text = "VIEWS -->" + data['items'][0]['statistics']['viewCount'])
        lbl7.pack()      
        lbl7.configure(font = Desired_font)
        lbl6 = Label(root, text = "DISLIKES -->" + data['items'][0]['statistics']['dislikeCount'])
        lbl6.pack()      
        lbl6.configure(font = Desired_font)


btn =Button(root,text = 'DOWNLOAD',bg = 'bisque2', padx = 2, command = Downloader)
btn.pack()
btn.configure(font = Desired_font) #configuring/assigning widgets with desired format

btn2 =Button(root,text = 'INFO',bg = 'bisque2', padx = 2, command = info)
btn2.pack()
btn2.configure(font = Desired_font)


lbl.configure(font = Desired_font)
lbl2.configure(font = Desired_font) 
link_enter.configure(font = Desired_font)

root.mainloop()



'''
{'items': [{'id': 'hRK5xA3rM98',
            'snippet': {'categoryId': '15',
                        'channelId': 'UC38r7_x7oMPAZweB2fvGDXQ',
                        'title': 'Excuse me sir, do you hav time for a quick '
                                 'pet?'},
            'statistics': {'commentCount': '12170',
                           'dislikeCount': '2334',
                           'favoriteCount': '0',
                           'likeCount': '259655',
                           'viewCount': '4260899'}}]}

'''