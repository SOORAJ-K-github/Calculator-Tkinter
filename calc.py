from tkinter import *

def result(sign,f,s):
    display.delete(0,END)
    if sign=="+":display.insert(0,f+s)
    elif sign=="-":display.insert(0,f-s)
    elif sign=="/":display.insert(0,f/s)
    elif sign=="*":display.insert(0,f*s)


def check():
    num=display.get()
    if "x" in num:return result(sign="*",f=float(num[:num.index("x")]),s=float(num[num.index("x")+1:]))
    elif "+" in num:return result(sign="+",f=float(num[:num.index("+")]),s=float(num[num.index("+")+1:]))
    elif "÷" in num:return result(sign="/",f=float(num[:num.index("÷")]),s=float(num[num.index("÷")+1:]))
    elif num.count("-")>1:return result(sign="-",f=float(num[:num.index("-",1)]),s=float(num[num.index("-",1)+1:]))
    elif "-" in num and num[0]!="-":return result(sign="-",f=float(num[:num.index("-")]),s=float(num[num.index("-")+1:]))
    else:
        display.delete(0,END)
        display.insert(0,"ERROR")


window=Tk()
window.title("Calculator")
calc=Frame(window,bg="#202020")
calc.pack()


display=Entry(calc,font=("Arial",25,"bold"),relief=SUNKEN,bd=20,justify=RIGHT,bg="#2d2d2d",width=15,fg="dark grey")
display.grid(columnspan=5)




Button(calc,text="1",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"1")).grid(row=1,column=0)
Button(calc,text="2",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"2")).grid(row=1,column=1)
Button(calc,text="3",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"3")).grid(row=1,column=2)
Button(calc,text="+",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"+")).grid(row=1,column=3)
Button(calc,text="c",font=("Arial",25,"bold"),bg="#ef443b",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.delete(0,END)).grid(row=1,column=4)

Button(calc,text="4",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"4")).grid(row=2,column=0)
Button(calc,text="5",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"5")).grid(row=2,column=1)
Button(calc,text="6",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"6")).grid(row=2,column=2)
Button(calc,text="-",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"-")).grid(row=2,column=3)
Button(calc,text="B",font=("Arial",25,"bold"),bg="#5d658d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.delete(len(display.get())-1,END)).grid(row=2,column=4)

Button(calc,text="7",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"7")).grid(row=3,column=0)
Button(calc,text="8",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"8")).grid(row=3,column=1)
Button(calc,text="9",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"9")).grid(row=3,column=2)
Button(calc,text="x",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"x")).grid(row=3,column=3)


Button(calc,text=".",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),".")).grid(row=4,column=0)
Button(calc,text="0",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"0")).grid(row=4,column=1)
Button(calc,text="%",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"%")).grid(row=4,column=2)
Button(calc,text="÷",font=("Arial",25,"bold"),bg="#2d2d2d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=lambda :display.insert(len(display.get()),"÷")).grid(row=4,column=3)
Button(calc,text="=",font=("Arial",25,"bold"),bg="#5d658d",height=1,width=3,relief=FLAT,bd=2,padx=5,pady=5,fg="white",command=check).grid(row=4,column=4)


window.mainloop()

