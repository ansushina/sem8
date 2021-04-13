import tkinter as tk
class Table(tk.Frame): 
    def __init__(self, master, rows, columns): 
        super().__init__(master)
        self.array = []
        self.rows = rows
        self.columns = columns
        for i in range(rows):
            self.array.append([])
            for j in range(columns):
                self.array[i].append(tk.Entry(self, width=10))
                self.array[i][j].grid(row=i, column=j)

    def set(i, j, value): 
        if (i >= self.rows) or (j >= self.columns):
            return
        self.array[i][j].insert(str(value))
