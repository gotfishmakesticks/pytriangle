import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.resizable = False

f = tk.Frame()

def get_res():
    if ent_1.get() == '' or ent_2.get() == '' or ent_3.get() == '':
        messagebox.showinfo('Ошибка', 'Вы не заполнили все поля ввода')
        lbl_res['text'] = resc + 'Не все поля были заполнены'
        return
    try:

        n1 = float(ent_1.get())
        n2 = float(ent_2.get())
        n3 = float(ent_3.get())

        if n1 < 0 or n2 < 0 or n3 < 0:
            messagebox.showinfo('Ошибка', 'Вы ввели отрицательные значения в поля ввода')
            lbl_res['text'] = resc + 'Стороны треугольника не могут быть отрицательными'
            return

        if n1 == 0 or n2 == 0 or n3 == 0:
            messagebox.showinfo('Ошибка', 'Вы ввели одно или несколько нулевых значений')
            lbl_res['text'] = resc + 'Стороны треугольника не могут быть нулевыми'
            return

        if n1 > n2 + n3 or n2 > n1 + n3 or n3 > n1 + n2:
            messagebox.showinfo('Ошибка', 'У одной из сторон длина больше, чем у суммы двух других')
            lbl_res['text'] = resc + 'Треугольник не существует'
            return

        if n1 == n2 == n3:
            lbl_res['text'] = resc + 'Треугольник равносторонний'
            return
        elif n1 == n2 or n2 == n3 or n1 == n3:
            lbl_res['text'] = resc + 'Треугольник равнобедренный'
            return
        else:
            lbl_res['text'] = resc + 'Треугольник разносторонний'
            return
    except:
        messagebox.showinfo('Ошибка', 'Вы ввели недопустимые символы в поля ввода')
        lbl_res['text'] = resc + 'Ошибка в обработке введённых значений'
        return

btn = tk.Button(master=f, text='Вычислить', command=get_res)

resc = 'Результат: '

lbl_1 = tk.Label(master=f, text='Сторона 1')
lbl_2 = tk.Label(master=f, text='Сторона 2')
lbl_3 = tk.Label(master=f, text='Сторона 3')
lbl_res = tk.Label(master=f, text=resc)

ent_1 = tk.Entry(master=f)
ent_2 = tk.Entry(master=f)
ent_3 = tk.Entry(master=f)

f.pack()

btn.grid(row=2, column=0, columnspan=3)

lbl_1.grid(row=0, column=0)
lbl_2.grid(row=0, column=1)
lbl_3.grid(row=0, column=2)

ent_1.grid(row=1, column=0)
ent_2.grid(row=1, column=1)
ent_3.grid(row=1, column=2)

lbl_res.grid(row=3, column=0, columnspan=3)

root.mainloop()