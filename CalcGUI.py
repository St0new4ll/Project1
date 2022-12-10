import tkinter as tk
from tkinter import ttk
import formula
import math

"""
The first compute function is used by the first tab, it checks which operation has been picked and then calls
from the formula file to perform the needed operation.

This compute handles algebraical functions
"""


def compute():
    try:
        first_num = entry_first.get()
        second_num = entry_second.get()
        operation = radio_1.get()

        if operation == 1:
            label_result.config(text=f'{first_num} + {second_num} = {formula.add(first_num, second_num)}')
        elif operation == 2:
            label_result.config(text=f'{first_num} - {second_num} = {formula.subtract(first_num, second_num)}')
        elif operation == 3:
            label_result.config(text=f'{first_num} * {second_num} = {formula.multiply(first_num, second_num)}')
        elif operation == 4:
            label_result.config(text=f'{first_num} / {second_num} = {formula.divide(first_num, second_num)}')
        elif operation == 5:
            label_result.config(text=f'{first_num} ^ {second_num} = {formula.RaiseTo(first_num, second_num)}')
        else:
            label_result.config(text='No operation selected')
    except ValueError:
        label_result.config(text='Enter numeric values')
    except ZeroDivisionError:
        label_result.config(text='Cannot divide by 0 (change second number value)')
    except:
        label_result.config(text='Error occurred! Check input values')

"""
The second compute function handles the second tab, it handles trigonometric function 
"""
def compute2():
    try:
        first_num = float(entry_first2.get())
        operation = radio_2.get()

        if operation == 1:
            label_result2.config(text=f'(Answer is in Radians) Sine of {first_num} is {math.sin(first_num)}')
        elif operation == 2:
            label_result2.config(text=f'(Answer is in Radians) Cosine of {first_num} is {math.cos(first_num)}')
        elif operation == 3:
            label_result2.config(text=f'(Answer is in Radians) Tangent of {first_num} is {math.tan(first_num)}')
        elif operation == 4:
            if first_num > 1 or first_num < -1:
                label_result2.config(text='ArcSine and ArcCosine input must be between -1 and 1')
            else:
                label_result2.config(text=f'(Answer is in Radians) ArcSine of {first_num} is {math.asin(first_num)}')
        elif operation == 5:
            if first_num > 1 or first_num < -1:
                label_result2.config(text='ArcSine and ArcCosine input must be between -1 and 1')
            else:
                label_result2.config(text=f'(Answer is in Radians) ArcCosine of {first_num} is {math.acos(first_num)}')
        elif operation == 6:
            label_result2.config(text=f'(Answer is in Radians) ArcTangent of {first_num} is {math.atan(first_num)}')
        else:
            label_result2.config(text='No operation selected')
    except ValueError:
        label_result2.config(text='Enter numeric values')
    except ZeroDivisionError:
        label_result2.config(text='Cannot divide by 0 (change second number value)')
    except:
        label_result2.config(text='Error occurred! Check input values')

"""
The third compute function handles the third tab and contains the area functions

Because some areas only require one input, it will check if it is one function that only needs one
Trying to perform a .get() on the second entry when it is disabled will result in a value error
"""
def compute3():
    try:
        operation = radio_3.get()

        if operation == 1:
            first_num = float(entry_first3.get())
            second_num = float(entry_second3.get())
            if first_num < 0:
                label_result3.config(text=f'Enter positive values only')
            elif second_num < 0:
                label_result3.config(text=f'Enter positive values only')
            elif first_num == second_num:
                label_result3.config(text=f'The area of a square with sides '
                                          f'{first_num} is {formula.sqr(first_num)}')
            else:
                label_result3.config(text=f'The area of a rectangle with sides of length {first_num} '
                                          f'and {second_num} is {formula.rect(first_num, second_num)}')
        elif operation == 2:
            first_num = float(entry_first3.get())
            second_num = float(entry_second3.get())
            if first_num < 0:
                label_result3.config(text=f'Enter positive values only')
            elif second_num < 0:
                label_result3.config(text=f'Enter positive values only')
            label_result3.config(text=f'The area of a triangle with base of {first_num} and height of '
                                      f'{second_num} is {formula.tri(first_num, second_num)}')
        elif operation == 3:
            first_num = float(entry_first3.get())
            if first_num < 0:
                label_result3.config(text=f'Enter positive values only')
            label_result3.config(text=f'The area of a circle with radius {first_num} is {formula.circ(first_num):.3f}')
        elif operation == 4:
            first_num = float(entry_first3.get())
            second_num = float(entry_second3.get())
            if first_num < 0:
                label_result3.config(text=f'Enter positive values only')
            elif second_num < 0:
                label_result3.config(text=f'Enter positive values only')
            label_result3.config(text=f'The area of an ellipse with base of {first_num} and height of '
                                      f'{second_num} is {formula.ellip(first_num, second_num)}')
        else:
            label_result3.config(text='No operation selected')
    except ValueError:
        label_result3.config(text='Enter numeric values')
    except ZeroDivisionError:
        label_result3.config(text='Cannot divide by 0 (change second number value)')
    except:
        label_result3.config(text='Error occurred! Check input values')

"""
The fourth compute handles the fourth tab and covers volume formulae. Like the third compute it handles if the 
chosen operation only requires one value
"""
def compute4():
    try:
        operation = radio_4.get()
        if operation == 1:
            first_num = float(entry_first4.get())
            if first_num < 0:
                label_result4.config(text=f'Enter positive values only')
            label_result4.config(text=f'The volume of a cube with sides {first_num} is {formula.cube(first_num)}')
        elif operation == 4:
            first_num = float(entry_first4.get())
            if first_num < 0:
                label_result4.config(text=f'Enter positive values only')
            label_result4.config(text=f'The volume of a sphere with radius {first_num} is {formula.sphere(first_num)}')
        elif operation == 2:
            first_num = float(entry_first4.get())
            second_num = float(entry_second4.get())
            if first_num < 0:
                label_result4.config(text=f'Enter positive values only')
            elif second_num < 0:
                label_result4.config(text=f'Enter positive values only')
            label_result4.config(text=f'The volume of a cylinder with radius of {first_num} and height of '
                                      f'{second_num} is {formula.cylin(first_num, second_num)}')
        elif operation == 3:
            first_num = float(entry_first4.get())
            second_num = float(entry_second4.get())
            if first_num < 0:
                label_result4.config(text=f'Enter positive values only')
            elif second_num < 0:
                label_result4.config(text=f'Enter positive values only')
            label_result4.config(text=f'The volume of a prism with base side of '
                                      f'{first_num} and height {second_num} is {formula.prism(first_num, second_num)}')
        else:
            label_result4.config(text='No operation selected')
    except ValueError:
        label_result4.config(text='Enter numeric values')
    except ZeroDivisionError:
        label_result4.config(text='Cannot divide by 0 (change second number value)')
    except:
        label_result4.config(text='Error occurred! Check input values')

"""
Creates the root window and its tabs
"""
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.geometry('500x300')

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Algebra')
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Trigonometry')
tabControl.pack(expand=1, fill="both")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Area')
tabControl.pack(expand=1, fill="both")

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='Volume')
tabControl.pack(expand=1, fill="both")

'''First Tab, Contains Algebraic Options'''

frame_first = tk.Frame(tab1)
label_first = tk.Label(frame_first, text='First number')
entry_first = tk.Entry(frame_first, width=40)
label_first.pack(padx=5, side='left')
entry_first.pack(padx=30, side='left')
frame_first.pack(anchor='w', pady=10)

frame_second = tk.Frame(tab1)
label_second = tk.Label(frame_second, text='Second number')
entry_second = tk.Entry(frame_second, width=40)
label_second.pack(padx=5, side='left')
entry_second.pack(padx=15, side='left')
frame_second.pack(anchor='w', pady=10)

frame_operation = tk.Frame(tab1)
label_operation = tk.Label(frame_operation, text='Operation\t')
radio_1 = tk.IntVar()
radio_1.set(0)
radio_add = tk.Radiobutton(frame_operation, text='Add', variable=radio_1, value=1)
radio_subtract = tk.Radiobutton(frame_operation, text='Subtract', variable=radio_1, value=2)
radio_multiply = tk.Radiobutton(frame_operation, text='Multiply', variable=radio_1, value=3)
radio_divide = tk.Radiobutton(frame_operation, text='Divide', variable=radio_1, value=4)
radio_RaiseTo = tk.Radiobutton(frame_operation, text='Raise to the Power', variable=radio_1, value=5)
label_operation.pack(side='left', padx=5)
radio_add.pack(side='left')
radio_subtract.pack(side='left')
radio_multiply.pack(side='left')
radio_divide.pack(side='left')
radio_RaiseTo.pack(side='left')
frame_operation.pack(anchor='w', pady=10)

frame_result = tk.Frame(tab1)
label_result = tk.Label(frame_result)
label_result.pack(pady=10)
frame_result.pack()

frame_button = tk.Frame(tab1)
button_compute = tk.Button(frame_button, text='COMPUTE', command=compute)
button_compute.pack(pady=10)
frame_button.pack()

'''End of First Tab'''

'''Second Tab, Contains Trigonometry Options'''
frame_first2 = tk.Frame(tab2)
label_first2 = tk.Label(frame_first2, text='Degrees')
entry_first2 = tk.Entry(frame_first2, width=40)
label_first2.pack(padx=5, side='left')
entry_first2.pack(padx=30, side='left')
frame_first2.pack(anchor='w', pady=10)

frame_operation2 = tk.Frame(tab2)
label_operation2 = tk.Label(frame_operation2, text='Operation\t')
radio_2 = tk.IntVar()
radio_2.set(0)
radio_Sin = tk.Radiobutton(frame_operation2, text='Sin', variable=radio_2, value=1)
radio_Cos = tk.Radiobutton(frame_operation2, text='Cos', variable=radio_2, value=2)
radio_Tan = tk.Radiobutton(frame_operation2, text='Tan', variable=radio_2, value=3)
radio_Asin = tk.Radiobutton(frame_operation2, text='Asin', variable=radio_2, value=4)
radio_Acos = tk.Radiobutton(frame_operation2, text='Acos', variable=radio_2, value=5)
radio_Atan = tk.Radiobutton(frame_operation2, text='Atan', variable=radio_2, value=6)
label_operation2.pack(side='left', padx=5)
radio_Sin.pack(side='left')
radio_Cos.pack(side='left')
radio_Tan.pack(side='left')
radio_Asin.pack(side='left')
radio_Acos.pack(side='left')
radio_Atan.pack(side='left')
frame_operation2.pack(anchor='w', pady=10)

frame_result2 = tk.Frame(tab2)
label_result2 = tk.Label(frame_result2)
label_result2.pack(pady=10)
frame_result2.pack()

frame_button2 = tk.Frame(tab2)
button_compute2 = tk.Button(frame_button2, text='COMPUTE', command=compute2)
button_compute2.pack(pady=51)
frame_button2.pack()
'''End of Second Tab'''

'''Third tab, Containing Area Formulas'''
frame_first3 = tk.Frame(tab3)
label_first3 = tk.Label(frame_first3, text='Length or Base')
entry_first3 = tk.Entry(frame_first3, width=40)
label_first3.pack(padx=5, side='left')
entry_first3.pack(padx=25, side='left')
frame_first3.pack(anchor='w', pady=10)

frame_second3 = tk.Frame(tab3)
label_second3 = tk.Label(frame_second3, text='Width or Height')
entry_second3 = tk.Entry(frame_second3, width=40)
label_second3.pack(padx=5, side='left')
entry_second3.pack(padx=20, side='left')
frame_second3.pack(anchor='w', pady=10)

frame_operation3 = tk.Frame(tab3)
label_operation3 = tk.Label(frame_operation3, text='Shape\t')
radio_3 = tk.IntVar()
radio_3.set(0)

radio_Sqr = tk.Radiobutton(
    frame_operation3, text='Square/Rectangle', variable=radio_3, value=1,
    command=lambda: entry_second3.config(state="normal")
)
radio_Tri = tk.Radiobutton(
    frame_operation3, text='Triangle', variable=radio_3, value=2,
    command=lambda: entry_second3.config(state="normal")
)
radio_Circ = tk.Radiobutton(
    frame_operation3, text='Circle', variable=radio_3, value=3,
    command=lambda: entry_second3.config(state="disabled")
)
radio_Ellip = tk.Radiobutton(
    frame_operation3, text='Ellipse', variable=radio_3, value=4,
    command=lambda: entry_second3.config(state="normal")
)

label_operation3.pack(side='left', padx=5)
radio_Sqr.pack(side='left')
radio_Tri.pack(side='left')
radio_Circ.pack(side='left')
radio_Ellip.pack(side='left')
frame_operation3.pack(anchor='w', pady=10)

frame_result3 = tk.Frame(tab3)
label_result3 = tk.Label(frame_result3)
label_result3.pack(pady=10)
frame_result3.pack()

frame_button3 = tk.Frame(tab3)
button_compute3 = tk.Button(frame_button3, text='COMPUTE', command=compute3)
button_compute3.pack(pady=10)
frame_button3.pack()
'''End of Tab Three'''

'''Fourth Tab, Containing Volume Formulas'''
frame_first4 = tk.Frame(tab4)
label_first4 = tk.Label(frame_first4, text='Length, Base, or Radius')
entry_first4 = tk.Entry(frame_first4, width=40)
label_first4.pack(padx=5, side='left')
entry_first4.pack(padx=9, side='left')
frame_first4.pack(anchor='w', pady=10)

frame_second4 = tk.Frame(tab4)
label_second4 = tk.Label(frame_second4, text='Width or Height')
entry_second4 = tk.Entry(frame_second4, width=40)
label_second4.pack(padx=5, side='left')
entry_second4.pack(padx=45, side='left')
frame_second4.pack(anchor='w', pady=10)

frame_operation4 = tk.Frame(tab4)
label_operation4 = tk.Label(frame_operation4, text='Shape\t')
radio_4 = tk.IntVar()
radio_4.set(0)

radio_Cube = tk.Radiobutton(
    frame_operation4, text='Cube', variable=radio_4, value=1,
    command=lambda: entry_second4.config(state="disabled")
)
radio_Cyl = tk.Radiobutton(
    frame_operation4, text='Cylinder', variable=radio_4, value=2,
    command=lambda: entry_second4.config(state="normal")
)
radio_Pris = tk.Radiobutton(
    frame_operation4, text='Prism', variable=radio_4, value=3,
    command=lambda: entry_second4.config(state="normal")
)
radio_Spher = tk.Radiobutton(
    frame_operation4, text='Sphere', variable=radio_4, value=4,
    command=lambda: entry_second4.config(state="disabled")
)

label_operation4.pack(side='left', padx=5)
radio_Cube.pack(side='left')
radio_Cyl.pack(side='left')
radio_Pris.pack(side='left')
radio_Spher.pack(side='left')
frame_operation4.pack(anchor='w', pady=10)

frame_result4 = tk.Frame(tab4)
label_result4 = tk.Label(frame_result4)
label_result4.pack(pady=10)
frame_result4.pack()

frame_button4 = tk.Frame(tab4)
button_compute4 = tk.Button(frame_button4, text='COMPUTE', command=compute4)
button_compute4.pack(pady=10)
frame_button4.pack()

'''End of Tab Four'''

root.mainloop()
