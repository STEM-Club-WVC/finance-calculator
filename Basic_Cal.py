from tkinter import *


class Box:

    def __init__(self,column,row,text,color):
        self.text_lable = Label(root, text =  text, bg = color,padx = 20,width = 20).grid(row = row,column = column)
        self.row = row 
        self.column = column
        
        self.value = Entry(root,width = 30).grid(row = row+1,column = column)

root = Tk()
root.geometry('900x200')
         

beg_val = Box(0,0,'Beginning Value','pink')
int_rat = Box(1,0,'Intrest Rate','green')
sav_rat = Box(2,0,'Savings Rate(Monthly','lightblue') 
dur_yer = Box(3,0,'Duration (Years)','purple') 
por_val = Box(4,0,'Portfollio Value','yellow') 
por_inc = Box(0,3,'Portfolio Income Production','lightblue') 
cop_rat = Box(1,3,'Coupon Rate','yellow') 
tax_rat = Box(2,3,'Tax Rate','green') 
inf_rat = Box(3,3,'Inflation','orange')     

#print(beg_val.value.get())

root.mainloop()

