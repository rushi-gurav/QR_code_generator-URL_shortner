from tkinter import*
from tkinter.messagebox import*
from pyshorteners import*
from webbrowser

root = Tk()
root.title("URL Shortener by Rushi Gurav")
root.geometery("1200x400+100+20")
f = ("Callibri",30,"bold")

def short():
	url = ent_url.get()
	if url ==""
		showerror("issue","please enter url")
		ent_url.focus()
		return

	sh = Shortener()
	res = sh.tinyurl.short(url)
	ent_res.insert(0,res)
	btn_open.pack()
	btn_open.configure(state = NORMAL)

def show():
	url = ent_res.get()
	if url == "":
		showerror("issue","u did not short it")
		ent_url.focus()
		btn_open.configure(state = DISABLED)
		return
	webbrowser.open(url)

lab_url = Label(root,text="Enter Url",font = f)
ent_url = Entry(root,font=f,width =50)
btn_short = Button(rooot,text="Short the URL",font =f,command = short)
ent_res = Entry(root,font=f,width =50)
btn_open = Button(rooot,text="Open in browser",font =f,command = show)
btn_open.config(state =DISABLED)

lab_url.pack(pady = 5)
ent_url.pack(pady =5)
btn_short.pack(pady=5)
ent_res.pack(pady=5)
btn_open.pack_forget()

root.mainloop()
