
from tkinter import * 
import Input as i
from Table import Table
from functions import *
root = Tk()

varList = {
    "lambda": StringVar(),
    "mu": StringVar(),
    "k": StringVar(), 
    "N": StringVar(), 
    "start": StringVar(), 
    "end": StringVar(),
    "N_exp": StringVar(), 

}

def work_proc(Event):
    modelling(
        clients_number=float(varList["N"].get())+1000,
        clients_proccessed=float(varList["N"].get()),
        lambda_coming=float(varList["lambda"].get()),
        lambda_obr=float(varList["mu"].get())
    )

def work_view(Event):
    view(
        start=float(varList["start"].get()), 
        end=float(varList["end"].get()), 
        N=float(varList["N_exp"].get())
    )


def one_model_list(root):
    items = [
        i.Item(text="Интенсивность поступления заявок:", var=varList["lambda"], value=10),
        i.Item(text="Интенсивность обслуживания заявок:", var=varList["mu"], value=15),
        i.Item(text="Число заявок:", var=varList["N"], value=1000),
    ]
    i_list = i.InputList(master=root, items=items)
    i_list.grid(column=1)

    btn = Button(root, text="Запуск")
    btn.bind("<Button-1>", work_proc)       
    btn.grid(column=1, padx=10, pady=10)                          


def expirement_list(root): 
    items = [
        i.Item(text="От:", var=varList["start"], value=0.01), 
        i.Item(text="До:", var=varList["end"], value=1.1), 
        i.Item(text="Число заявок:", var=varList["N_exp"], value=1000)
    ]

    i_list = i.InputList(master=root, items=items)
    i_list.grid(column=1)

    btn2 = Button(root, text="Запуск")
    btn2.bind("<Button-1>", work_view)       
    btn2.grid(column=1, padx=10, pady=10)  


if __name__ == '__main__':
    f_proc = Frame(root)
    f_view = Frame(root)

    one_model_list(f_proc)
    expirement_list(f_view)

    f_proc.pack()
    f_view.pack()

    # table = Table(master=root, rows=10, columns=13)
    # table.pack()

    root.mainloop()
    

    