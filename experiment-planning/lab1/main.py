from Modeller import Modeller
from EventGenerator import Generator
from Distributions import  RayleighDistribution, WeibullDistribution
from Processor import Processor
import math
from matplotlib import pyplot


def view():
    Xdata = list()
    Ydata = list()
    Ydata_t = list()

    lambda_obr = 100
    k = 2

    for lambda_coming in range(1, lambda_obr+1, 5):
            sigma = (1/lambda_coming) * (math.pi / 2) ** (-1/2)
            lam = (1/lambda_obr) * math.log(2, math.e) ** (-1 / k)

            generators = [
                Generator(
                    RayleighDistribution(sigma),
                    20000,
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
            result = model.event_mode(12000)
            Xdata.append(lambda_coming/lambda_obr)
            Ydata.append(result['wait_time_middle'])
            # print(lambda_coming/lambda_obr) 
            # print(result['wait_time_middle']) 
            ro = lambda_coming/lambda_obr
            if ro != 1:
                Ydata_t.append(ro/(1 - ro)/lambda_coming)

    pyplot.title('Среднее время ожидания')
    pyplot.grid(True)
    # pyplot.plot(Xdata, Ydata_t)
    pyplot.plot(Xdata, Ydata)
    pyplot.xlabel("Коэффикиент загрузки")
    pyplot.ylabel("Среднее время пребывания в очереди")
    pyplot.show()



if __name__ == '__main__':
    clients_number = 10000 #Количество клиентов
    proccessed = 1000

    lambda_coming = float(input("Введите интенсивность прихода послетителей: "))
    lambda_obr = float(input("Введите интенсивность обработки: "))

    sigma = (1/lambda_coming) * (math.pi / 2) ** (-1/2)

    k = 2
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
    result = model.event_mode(proccessed)
    # print(result)
    print("Загрузка системы(расчетная): ", lambda_coming/lambda_obr, 
    "\nВремя работы:", result['time'], 
    "\nСреднее время ожидания: ", result['wait_time_middle'], 
    "\nКоличество обработанных заявок", proccessed)
    # view()