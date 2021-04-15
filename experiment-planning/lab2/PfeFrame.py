import tkinter as tk
from Table import Table
from functions import *

class PfeFrame(tk.Frame): 
    def __init__(self, master): 
        super().__init__(master)

        self.MainTable = Table(master=self, rows=10, columns=14)
        self.MainTable.pack(padx=10, pady=10)
        self.BTable = Table(master=self, rows=2, columns=8)
        self.BTable.pack(padx=10, pady=10)

        self.MainTable.set( 0, 0, "№")
        self.MainTable.set( 0, 1, "x0")
        self.MainTable.set( 0, 2, "x1")
        self.MainTable.set( 0, 3, "x2")
        self.MainTable.set( 0, 4, "x3")
        self.MainTable.set( 0, 5, "x12")
        self.MainTable.set( 0, 6, "x13")
        self.MainTable.set( 0, 7, "x23")
        self.MainTable.set( 0, 8, "x123")
        self.MainTable.set( 0, 9, "y")
        self.MainTable.set( 0, 10, "y^ л")
        self.MainTable.set( 0, 11, "y^ чн")
        self.MainTable.set( 0, 12, "|y - y^л|")
        self.MainTable.set( 0, 13, "|y - y^чн|")

        self.BTable.set( 0, 0, "b0")
        self.BTable.set( 0, 1, "b1")
        self.BTable.set( 0, 2, "b2")
        self.BTable.set( 0, 3, "b3")
        self.BTable.set( 0, 4, "b12")
        self.BTable.set( 0, 5, "b13")
        self.BTable.set( 0, 6, "b23")
        self.BTable.set( 0, 7, "b123")

    def set_x_values(self): 
        for i in range(len(self.x_table)):
            self.MainTable.set_column(i+1, self.x_table[i])

    def modelling(self): 
        y = []
        for i in range(len(self.x_table[0])):
            result = modelling(
                clients_number=self.count+1000,
                clients_proccessed=self.count,
                lambda_coming=self.lambda_min if self.x_table[1][i] == -1 else self.lambda_max,
                lambda_obr=self.mu_min if self.x_table[2][i] == -1 else self.mu_max, 
                disp=self.mu_disp_min if self.x_table[3][i] == -1 else self.mu_disp_max, 
            )

            y.append(result['wait_time_middle'])
        return y

    def count_one(self, lam, mu, disp):
        if lam < self.lambda_min or lam > self.lambda_max or mu < self.mu_min or mu > self.mu_max: 
            tk.messagebox.showinfo(title="error", message="Точка не входит в промежуток варьирования!")
            return 


        result = modelling(
                clients_number=self.count+1000,
                clients_proccessed=self.count,
                lambda_coming=lam,
                lambda_obr=mu, 
                disp=disp
            )

        x0 = 1 
        i_lam = (self.lambda_max -self.lambda_min)/2
        lam0 = (self.lambda_max + self.lambda_min)/2
        x1 = (lam - lam0)/i_lam
        i_mu = (self.mu_max -self.mu_min)/2
        mu0 = (self.mu_max + self.mu_min)/2
        x2 = (mu - mu0)/i_mu
        i_disp = (self.mu_disp_max -self.mu_disp_min)/2
        disp0 = (self.mu_disp_max + self.mu_disp_min)/2
        x3 = (disp - disp0) / i_disp
        x12 = x1 * x2
        x13 = x1 * x3
        x23 = x2 * x3
        x123 = x1*x2*x3

        line = [x0] + [x1] + [x2] + [x3] + [x12] + [x13] + [x23] + [x123]
        y = result['wait_time_middle']

        s = 0
        l = 3
        for j in range(l): 
            s += line[j] * self.b[j]
        y_lin = s

        s = 0
        l = len(line)
        for j in range(l): 
            s += line[j] * self.b[j]
        y_nl = s

        y_lin_per = abs(y - y_lin)
        y_nl_per = abs(y - y_nl)

        line += [y] + [y_lin] + [y_nl] + [y_lin_per] + [y_nl_per]

        self.MainTable.set_row(9, line, 1)

    def run(self, lambda_min, lambda_max, mu_min, mu_max, mu_disp_min, mu_disp_max, count):
        self.lambda_max = lambda_max
        self.lambda_min = lambda_min
        self.mu_max = mu_max
        self.mu_min = mu_min
        self.mu_disp_min = mu_disp_min
        self.mu_disp_max = mu_disp_max
        self.count = count
        exp_count = 8 
        # считаем иксы
        x0 = [1 for i in range(exp_count)]
        x1 = [1 if i%2==1 else -1 for i in range(exp_count)]
        x2 = [-1 if i%4 < 2 else 1 for i in range(exp_count)]
        x3 = [-1 if i%8 < 4 else 1 for i in range(exp_count)]
        x12 = [x1[i]*x2[i] for i in range(len(x1))]
        x13 = [x1[i]*x3[i] for i in range(len(x1))]
        x23 = [x2[i]*x3[i] for i in range(len(x2))]
        x123 = [x1[i]*x2[i]*x3[i] for i in range(len(x1))]

        # отображаем иксы
        self.x_table = [x0] + [x1] + [x2] + [x3] + [x12] + [x13] + [x23] + [x123] 
        self.set_x_values()

        print(self.x_table)

        # Считаем игреки
        y = self.modelling()
        for i in range(9):
            self.MainTable.set(i+1, 0, i+1)

        # Считаем b
        b0 = self.count_b(x0, y)
        b1 = self.count_b(x1, y)
        b2 = self.count_b(x2, y)
        b3 = self.count_b(x3, y)
        b12 = self.count_b(x12, y)
        b13 = self.count_b(x13, y)
        b23 = self.count_b(x23, y)
        b123 = self.count_b(x123, y)

        b = [b0] + [b1] + [b2] + [b3] + [b12] + [b13] + [b23] + [b123]
        print(b)
        

        # Отображаем игреки и b
        self.MainTable.set_column(9, y)
        self.BTable.set_row(1, b)
        self.b = b

        # Считаем линейную и частично не линейную модели
        y_lin = self.count_lin(self.x_table, b, 4)
        y_nl = self.count_lin(self.x_table, b, len(b))
        
        y_lin_per = [abs(y[i] - y_lin[i]) for i in range(len(y))]
        y_nl_per = [abs(y[i] - y_nl[i]) for i in range(len(y))]

        # Отрисовываем
        self.MainTable.set_column(10, y_lin)
        self.MainTable.set_column(11, y_nl)
        self.MainTable.set_column(12, y_lin_per)
        self.MainTable.set_column(13, y_nl_per)
        self.MainTable.set_row(9, ['','','','','','',
                                    '','','','','','',''], 1)

    def count_b(self, x, y): 
        sum = 0
        for i in range(len(x)):
            sum += x[i]*y[i]
        return sum/len(x)

    def count_lin(self, x_table, b, l):
        y_lin = []
        for i in range(len(x_table)):
            x = x_table[i] 
            y = 0
            for j in range(l): 
                y += x_table[j][i]*b[j]
            y_lin.append(y)
        return y_lin 


            