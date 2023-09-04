import tkinter as tk
import math

calculation = ''

def add_to_calculation(symbol):
    global calculation
    
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
        
def evaluate_calculation():
    global calculation

    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0,'end')


root = tk.Tk()
root.geometry("650x360")

text_result = tk.Text(root, height=1, width=30,font=("Arial",24))
text_result.grid(columnspan=6)

btn_1 = tk.Button(root,text='√',command=lambda: add_to_calculation('math.sqrt('),width=5,font=("Arial",24), bg="green")
btn_1.grid(row=2,column=1)

btn_2 = tk.Button(root,text='Log',command=lambda: add_to_calculation('math.log('),width=5,font=("Arial",24), bg="green")
btn_2.grid(row=2,column=2)

btn_3 = tk.Button(root,text='(',command=lambda: add_to_calculation('('),width=5,font=("Arial",24), bg="green")
btn_3.grid(row=2,column=3)

btn_4 = tk.Button(root,text=')',command=lambda: add_to_calculation(')'),width=5,font=("Arial",24), bg="green")
btn_4.grid(row=2,column=4)

btn_5 = tk.Button(root,text='^',command=lambda: add_to_calculation('**'),width=5,font=("Arial",24), bg="green")
btn_5.grid(row=2,column=5)

btn_6 = tk.Button(root,text='*',command=lambda: add_to_calculation('*'),width=5,font=("Arial",24), bg="green")
btn_6.grid(row=2,column=6)

btn_7 = tk.Button(root,text='π',command=lambda: add_to_calculation('math.pi'),width=5,font=("Arial",24), bg="green")
btn_7.grid(row=3,column=1)

btn_8 = tk.Button(root,text='e',command=lambda: add_to_calculation('math.e'),width=5,font=("Arial",24), bg="green")
btn_8.grid(row=3,column=2)

btn_9 = tk.Button(root,text='7',command=lambda: add_to_calculation(7),width=5,font=("Arial",24), bg="green")
btn_9.grid(row=3,column=3)

btn_10 = tk.Button(root,text='8',command=lambda: add_to_calculation(8),width=5,font=("Arial",24), bg="green")
btn_10.grid(row=3,column=4)

btn_11 = tk.Button(root,text='9',command=lambda: add_to_calculation(9),width=5,font=("Arial",24), bg="green")
btn_11.grid(row=3,column=5)

btn_12 = tk.Button(root,text='/',command=lambda: add_to_calculation('/'),width=5,font=("Arial",24), bg="green")
btn_12.grid(row=3,column=6)

btn_13 = tk.Button(root,text='Sin',command=lambda: add_to_calculation('math.sin('),width=5,font=("Arial",24), bg="green")
btn_13.grid(row=4,column=1)

btn_14 = tk.Button(root,text='Cos',command=lambda: add_to_calculation('math.cos('),width=5,font=("Arial",24), bg="green")
btn_14.grid(row=4,column=2)

btn_15 = tk.Button(root,text='4',command=lambda: add_to_calculation(4),width=5,font=("Arial",24), bg="green")
btn_15.grid(row=4,column=3)

btn_16 = tk.Button(root,text='5',command=lambda: add_to_calculation(5),width=5,font=("Arial",24), bg="green")
btn_16.grid(row=4,column=4)

btn_17 = tk.Button(root,text='6',command=lambda: add_to_calculation(6),width=5,font=("Arial",24), bg="green")
btn_17.grid(row=4,column=5)

btn_18 = tk.Button(root,text='-',command=lambda: add_to_calculation('-'),width=5,font=("Arial",24), bg="green")
btn_18.grid(row=4,column=6)

btn_19 = tk.Button(root,text='Tan',command=lambda: add_to_calculation('math.tan('),width=5,font=("Arial",24), bg="green")
btn_19.grid(row=5,column=1)

btn_20 = tk.Button(root,text='Hyp',command=lambda: add_to_calculation('math.hypot('),width=5,font=("Arial",24), bg="green")
btn_20.grid(row=5,column=2)

btn_21 = tk.Button(root,text='1',command=lambda: add_to_calculation(1),width=5,font=("Arial",24), bg="green")
btn_21.grid(row=5,column=3)

btn_22 = tk.Button(root,text='2',command=lambda: add_to_calculation(2),width=5,font=("Arial",24), bg="green")
btn_22.grid(row=5,column=4)

btn_23 = tk.Button(root,text='3',command=lambda: add_to_calculation(3),width=5,font=("Arial",24), bg="green")
btn_23.grid(row=5,column=5)

btn_24 = tk.Button(root,text='+',command=lambda: add_to_calculation('+'),width=5,font=("Arial",24), bg="green")
btn_24.grid(row=5,column=6)

btn_25 = tk.Button(root,text='Clear',command=lambda: clear_field(),width=11,font=("Arial",24), bg="green")
btn_25.grid(row=6,column=1,columnspan=2)

btn_26 = tk.Button(root,text='0',command=lambda: add_to_calculation(0),width=5,font=("Arial",24), bg="green")
btn_26.grid(row=6,column=3)

btn_27 = tk.Button(root,text='.',command=lambda: add_to_calculation('.'),width=5,font=("Arial",24), bg="green")
btn_27.grid(row=6,column=4)

btn_28 = tk.Button(root,text=',',command=lambda: add_to_calculation(','),width=5,font=("Arial",24), bg="green")
btn_28.grid(row=6,column=5)

btn_29 = tk.Button(root,text='=',command= evaluate_calculation,width=5,font=("Arial",24), bg="green")
btn_29.grid(row=6,column=6)

root.mainloop()