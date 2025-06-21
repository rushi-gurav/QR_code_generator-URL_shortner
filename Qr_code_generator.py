from tkinter import*
from tkinter.messagebox import*
from qrcode import*
from requests import*
from PIL import Image,ImageTk

root = Tk()
root.title("Qrcode generator")
root.geometry("700x600+300+20")
f = ("Cambria",30,"bold")

def gen():
	url = ent_url.get()
	if url=="":
		showerror("issue","please enter url")
		msg.configure(image="")
		msg.image =None
		ent_url.focus()
		return

		img =make(url)
		img.save("qrcode.png")
		img =Image.open("qrcode.png")
		rimg = img.resize((400,400))
		imgtk = ImageTk.PhotoImage(image = rimg)
		msg.configure(image = imgtk)
		msg.photo = imgtk
		

lab_url = Label(root, text ="Enter Url",font=f)
ent_url = Entry(root,font = f)
btn_gen = Button(root,text="Generated QRCode",font = f,command = gen)
msg = Label(root,font =f, width =400,height =400)



lab_url.pack(pady =5)
ent_url.pack(pady = 5)
btn_gen.pack(pady =5)
msg.pack(pady = 5)

root.mainloop()