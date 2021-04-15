from Modeller import Modeller
from EventGenerator import Generator
from Distributions import  RayleighDistribution, WeibullDistribution
from Processor import Processor
import math
from matplotlib import pyplot

def modelling(clients_number, clients_proccessed, lambda_coming, lambda_obr, disp=1): 
    sigma = (1/lambda_coming) * (math.pi / 2) ** (-1/2)

    k = (math.sqrt(disp)/lambda_obr)**(-1.086)
    lam = (1/lambda_obr) * math.log(2, math.e) ** (-1 / k)

    generators = [
        Generator(
            RayleighDistribution(sigma),
            clients_number,
        ), 
    ]

    operators = [
            Processor(
                WeibullDistribution(k, lam)
            ),
        ]
    for generator in generators: 
        generator.receivers = operators.copy()

    model = Modeller(generators, operators)
    result = model.event_mode(clients_proccessed)
    print("Загрузка системы(расчетная): ", lambda_coming/lambda_obr, 
    "\nВремя работы:", result['time'], 
    "\nСреднее время ожидания: ", result['wait_time_middle'], 
    "\nКоличество обработанных заявок", clients_proccessed)
    return result


def view(start, end, N):
    print(start, end, N)
    Xdata = list()
    Ydata = list()

    lambda_obr = 100
    k = 2

    for lambda_coming in range(int(start * 100), int(end * 100), 5):
            result = modelling(
                clients_number=N+1000,
                clients_proccessed=N, 
                lambda_coming=lambda_coming,
                lambda_obr=lambda_obr
            )
            Xdata.append(lambda_coming/lambda_obr)
            Ydata.append(result['wait_time_middle'])

    pyplot.title('Среднее время ожидания')
    pyplot.grid(True)
    pyplot.plot(Xdata, Ydata)
    pyplot.xlabel("Коэффикиент загрузки")
    pyplot.ylabel("Среднее время пребывания в очереди")
    pyplot.show()