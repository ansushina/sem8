
from tkinter import *
import tkinter as tk
import Input as i
from Table import Table
from functions import *
from PfeFrame import *
root = Tk()
experiment = PfeFrame(root)


varList = {
    "lambda": StringVar(),
    "mu": StringVar(),
    "mu_disp": StringVar(),
    "k": StringVar(), 
    "N": StringVar(), 
    "start": StringVar(), 
    "end": StringVar(),
    "N_exp": StringVar(), 
    "lambda_min": StringVar(), 
    "lambda_max": StringVar(),
    "mu_min": StringVar(),
    "mu_max": StringVar(),
    "mu_disp_min": StringVar(),
    "mu_disp_max": StringVar(),
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

def work_pfe(Event):
    try:
        lambda_min = float(varList["lambda_min"].get())
        lambda_max = float(varList["lambda_max"].get())
        mu_min = float(varList["mu_min"].get())
        mu_max = float(varList["mu_max"].get())
        mu_disp_min = float(varList["mu_disp_min"].get())
        mu_disp_max = float(varList["mu_disp_max"].get())
        count = float(varList["N"].get())
        experiment.run(
            lambda_min=lambda_min,
            lambda_max=lambda_max,
            mu_max=mu_max,
            mu_min=mu_min, 
            count=count, 
            mu_disp_min=mu_disp_min, 
            mu_disp_max=mu_disp_max
        )        
        add_button.config(state='normal')
    except ValueError:
        tk.messagebox.showinfo(title="error", message="Ошибка ввода параметров!")

def work_one(Event): 
    lam = float(varList["lambda"].get())
    mu = float(varList["mu"].get())
    mu_disp = float(varList["mu_disp"].get())
    experiment.count_one(lam=lam, mu=mu, disp=mu_disp)

def pfe_inputs(root):
    frame_inputs = Frame(root)
    items_1 = [
        i.Item(text="Lambda_min:", var=varList["lambda_min"], value=1), 
        i.Item(text="Labmda_max:", var=varList["lambda_max"], value=100), 
    ]
    items_2 = [
        i.Item(text="Mu_min:", var=varList["mu_min"], value=1), 
        i.Item(text="Mu_max:", var=varList["mu_max"], value=100), 
    ]
    items_3 = [
        i.Item(text="mu_disp_min:", var=varList["mu_disp_min"], value=1), 
        i.Item(text="mu_disp_max:", var=varList["mu_disp_max"], value=100), 
    ]
    i_list_1 = i.InputList(master=frame_inputs, items=items_1)
    i_list_2 = i.InputList(master=frame_inputs, items=items_2)
    i_list_3 = i.InputList(master=frame_inputs, items=items_3)

    i_list_1.pack(side=LEFT, padx=10, pady=10)
    i_list_2.pack(side=LEFT,  padx=10, pady=10)
    i_list_3.pack(side=LEFT,  padx=10, pady=10)

    frame_inputs.grid(column=1)

    items_4 = [
        i.Item(text="Число заявок:", var=varList["N"], value=1000), 
    ]

    i_list_4 = i.InputList(master=root, items=items_4)
    i_list_4.grid(column=1,  padx=10, pady=10)

    btn = Button(root, text="Запуск")
    btn.bind("<Button-1>", work_pfe)
      
    btn.grid(column=1, padx=10, pady=10) 

def draw_new_point(root):
    items = [
        i.Item(text="Интенсивность поступления заявок:", var=varList["lambda"], value=10),
        i.Item(text="Интенсивность обслуживания заявок:", var=varList["mu"], value=15),
        i.Item(text="Дисперсия....:", var=varList["mu_disp"], value=15),
    ]
    i_list = i.InputList(master=root, items=items)
    i_list.grid(column=1)

    btn = Button(root, text="Добавить", state=DISABLED)
    btn.bind("<Button-1>", work_one)       
    btn.grid(column=1, padx=10, pady=10)
    btn.config(state="disabled")
    return btn


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
    # f_proc = Frame(root)
    # f_view = Frame(root)

    # one_model_list(f_proc)
    # expirement_list(f_view)

    # f_proc.pack()
    # f_view.pack()

    f_pfe = Frame(root)
    pfe_inputs(f_pfe)
    add_button = draw_new_point(f_pfe)
    f_pfe.pack()

    experiment.pack()

    root.mainloop()
    

    