#!/usr/bin/python3
dev_mode  = True 
TK_SILENCE_DEPRECATION = 1 
from tkinter import *
import sys 
import threading 
from sounds import *
import time 


menu_level = 0
menu_0 = ["Open Diary", "Credits"]
menu_1 = ["Diary 1", "Diary 2","Diary 3","Diary 4","flip"] 
menus = [menu_0,menu_1]
point = 1 #starts at one for nicer experience. 

 


def up(e):
 play(page_turn)
 global point 
 point = (point +1 )% len(menus[menu_level])
 announce(None)
def down(e):
 global point 
 play(page_turn)
 point =(point -1)%len(menus[menu_level])
 announce(None)
 
def announce(e):
 return play(files.get(menus[menu_level][point]))
def leave(e=None):
 bg_set_check(False)
 kill(get_background_music())
 kill(get_currently_playing()) 
 sys.exit()
def selection():
 return menus[menu_level][point]

def seleciont_noise(selection):
    noises ={ "flip":"open7.mp3",}
    play(noises.get(selection, "open2.mp3"))
    time.sleep(0.3)
    return
def activate(e):
 seleciont_noise(selection())
# announce(None)
 global menu_level
 global point
 if selection() == "Open Diary":
  menu_level =1
  point = 0
  announce(None)
  return 
 elif selection() == "Credits":
  leave(None)
 elif selection() == "Diary 1":
  kill(get_background_music(),get_currently_playing())
  set_currently_playing( play_p("diaryentry1.mp3"))
 elif selection() == "flip":
  menu_level = 0
  point = 0
  announce(None)


def is_running(*procs):
 def test(proc):
  try:
   return proc.is_alive()
  except:
   return False
 x = list(test(p) for p in procs)
 return True in x

background_check = [True]
def bg_check():
 return background_check[0]
def bg_set_check(x):
 background_check[0] = x

def background_checker():
 print("background checker started")
 while(bg_check()):
  time.sleep(0.5)
  if not is_running(get_background_music(), get_currently_playing()): 
   set_background_music( background_loop_sound("backgroundnovoice.mp3"))
 else:
  kill(get_background_music())
  kill(get_currently_playing())

def skip(e):
 kill(get_currently_playing())
 play("open4.mp3")
 return
if dev_mode:
 def bonus(e=None):
  play("open"+e.char+".mp3")
  return 
  
root=Tk()
root.title("Sound Explorer's Diary") 
root.protocol("WM_DELETE_WINDOW", leave)
root.bind("<Up>",up)
root.bind("<Right>",up)
root.bind("<Left>",down)
root.bind("<Down>",down)
root.bind("a",announce)
root.bind("q",leave)
root.bind("<space>", activate)
root.bind("s",skip)
if dev_mode: 
 for i in range(1,10):
  root.bind(str(i),bonus)

if __name__ =='__main__':
 set_background_music( background_loop_sound("background.mp3"))
 bg = threading.Thread(target=background_checker).start() 
 root.mainloop()







