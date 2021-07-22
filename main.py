from tkinter import *
from tkinter import messagebox
import time
from random import choice

FONT = ('San Serif', 24)

tests = []
def current_milli_time():
    return round(time.time() * 1000)


try:
    with open('paragraphs','r') as f:
        m = f.readline()
        while m:
            tests.append(m)
            m = f.readline()
except FileNotFoundError:
    messagebox(title="ERROR", message="Missing the paragraphs file")
else:
    tests.append("The quick brown fox jumps over the lazy dog")


def where(location):
    test.configure(state='normal')
    character = '1.' + str(location)
    end = '1.' + str(location+1)
    test.tag_add('where', character, end)
    test.configure(state='disabled')


def opps(location):
    test.configure(state='normal')
    character = '1.' + str(location)
    end = '1.' + str(location+1)
    test.tag_add('error', character, end)
    test.configure(state='disabled')


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
        where(len(list1)-1)
        list2 = list(test.get(1.0, 'end'))
        for i in range(len(list1) - 1):
            if list1[i] != list2[i]:
                opps(i)
                mistake += 1

        if len(list1) == len(list2):
            end = current_milli_time()
            wpm = (len(list1)/5 - mistake) / ((end - start)/1000)*60
            response = messagebox.askquestion(title="Complete", message=f"You finished with a net WPM of {wpm:.2f}\n\n"
                                                                        f"Would you like to try agian?")
            if response == 'yes':
                test.delete(1.0,'end')
                test.insert('end', get_message(tests))
                text.delete(1.0,'end')
            else:
                window.quit()


def get_message(messages):
    return choice(messages)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Test")
window.geometry('1000x800')

test = Text(window, width=60, background='White', foreground='cyan', font=FONT, wrap=WORD)
test.place(x=10, y=10)
test.insert('end', get_message(tests))
test.configure(state='disabled')

text = Text(window, width=60, background='white', foreground='green', font=FONT, wrap=WORD)
text.place(x=10, y=250)
test.tag_configure('error', background='red', font=FONT)
test.tag_configure('where', underline=True, foreground='black')
where(0)
window.bind('<KeyPress>', onKeyPress)

window.mainloop()