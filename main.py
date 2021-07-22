from tkinter import *
from tkinter import messagebox
import time

def current_milli_time():
    return round(time.time() * 1000)

message ="This is a test"

def onKeyPress(event):
    global start
    mistake = 0
    try:
        ascii = ord(event.char)
    except TypeError:   # Non displayable key hit such as CMD, CTRL, Option ..
        print('Non displayable key hit')
        ascii=0

    if ascii >= 32:
        text.insert('end', (event.char) )
        list1 = list(text.get(1.0, 'end'))
        if len(list1) - 1 == 1:
            start = current_milli_time()
        list2 = list(test.get(1.0, 'end'))
        for i in range(len(list1)-1):
            if list1[i] != list2[i]:
                character = '1.'+str(i)
                end = '1.'+str(i+1)
                test.tag_add('error', character, end)
                mistake += 1
        if len(list1) == len(list2):
            end = current_milli_time()
            wpm =(len(list1)/5 - mistake) /((end - start)/1000)*60
            messagebox.showinfo(title="Complete", message=f"You made {mistake} mistakes with a net WPM of {wpm:.2f}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Test")
window.geometry('800x400')

test = Text(window, background='White', foreground='black', font=('Comic Sans MS', 24))
test.place(x=10, y=10)
test.insert('end', message)

text = Text(window, background='white', foreground='green', font=('Comic Sans MS', 24))
text.place(x=10, y=40)
test.tag_configure('error', background='red', font=('Comic Sans MS', 24))
window.bind('<KeyPress>', onKeyPress)

window.mainloop()