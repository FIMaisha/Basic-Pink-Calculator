from tkinter import *

root= Tk()
root.title("Simple Calculator")
root.resizable(False,False)
root.configure(bg="#EEE8AA")


e=Entry(root,fg="white",bg="black",width=25,borderwidth=5,justify="right",relief="groove",font=("Helvetica",10,"bold"))
e.grid(row=0,column=0,columnspan=4,ipadx=15,ipady=20)

def buttonadd(number):
	
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def buttonclear():
	e.delete(0,END)

def operatorclick(op):
	global first
	global operator

	first=float(e.get())
	operator=op
	e.delete(0,END)



def buttonequal():
    second = float(e.get())
    e.delete(0, END)

    if operator == "+":
        e.insert(0, first + second)
    elif operator == "-":
        e.insert(0, first - second)
    elif operator == "*":
        e.insert(0, first * second)
    elif operator == "/":
        e.insert(0, first / second)



def buttondot():
	current=e.get()
	if "." not in current:
		e.insert(END,".")
	
def buttonpercentage():
	current=e.get()
	if current=="":
		return
	value=float(current)/100
	e.delete(0,END)
	e.insert(0,value)

#define buttons
button1=Button(root,text="1",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(1),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button2=Button(root,text="2",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(2),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button3=Button(root,text="3",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(3),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button4=Button(root,text="4",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(4),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button5=Button(root,text="5",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(5),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button6=Button(root,text="6",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(6),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button7=Button(root,text="7",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(7),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button8=Button(root,text="8",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(8),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button9=Button(root,text="9",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(9),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")
button0=Button(root,text="0",font=("Elephant",12),padx=5,pady=5,command=lambda:buttonadd(0),bg="#BC8F8F",activebackground="gray",activeforeground="white",bd=5,relief="ridge")


add=Button(root,text="+",font=("Elephant",12),padx=5,pady=5,command=lambda:operatorclick("+"),bg="#BDB76B",bd=5,relief="ridge")
minus=Button(root,text="-",font=("Elephant",12),padx=5,pady=5,command=lambda:operatorclick("-"),bg="#BDB76B",bd=5,relief="ridge")
multiply=Button(root,text="x",font=("Elephant",12),padx=5,pady=5,command=lambda:operatorclick("*"),bg="#BDB76B",bd=5,relief="ridge")
division=Button(root,text="/",font=("Elephant",12),padx=5,pady=5,command=lambda:operatorclick("/"),bg="#BDB76B",bd=5,relief="ridge")	

equal=Button(root,text="=",font=("Elephant",12),padx=5,pady=5,command=buttonequal,bg="#2F4F4F",bd=5,relief="ridge")
clear=Button(root,text="CLEAR",font=("Elephant",12),padx=5,pady=5,command=buttonclear,bd=5,bg="#8B0000",fg="white",activebackground="#8B0000",activeforeground="black")
dot=Button(root,text=".",font=("Elephant",12),padx=5,pady=5,command=buttondot,bg="#BDB76B",bd=5,relief="ridge")
percentage=Button(root,text="%",font=("Elephant",12),padx=5,pady=5,command=buttonpercentage,bg="#A52A2A",bd=5,relief="ridge")
#put the buttons on screen
button1.grid(row=3,column=0,sticky="nsew")
button2.grid(row=3,column=1,sticky="nsew")
button3.grid(row=3,column=2,sticky="nsew")
multiply.grid(row=3,column=3,sticky="nsew")

button4.grid(row=2,column=0,sticky="nsew")
button5.grid(row=2,column=1,sticky="nsew")
button6.grid(row=2,column=2,sticky="nsew")
minus.grid(row=2,column=3,sticky="nsew")

button7.grid(row=1,column=0,sticky="nsew")
button8.grid(row=1,column=1,sticky="nsew")
button9.grid(row=1,column=2,sticky="nsew")
add.grid(row=1,column=3,sticky="nsew")

button0.grid(row=4,column=0,sticky="nsew")
dot.grid(row=5,column=1,sticky="nsew")
clear.grid(row=4,column=2,columnspan=2,sticky="nsew")
equal.grid(row=5,column=2,columnspan=2,sticky="nsew")
division.grid(row=5,column=0,sticky="nsew")
percentage.grid(row=4,column=1,sticky="nsew")


root.mainloop()
