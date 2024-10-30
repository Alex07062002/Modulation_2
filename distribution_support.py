# FIXME Выполняя данную работу, можно руководствоваться возможностью
# FIXME предельного перехода из дискретного распределения Пуассона
# FIXME в непрерывное нормальное распределение
from math import log10, sqrt
import numpy as np
from scipy.stats import poisson
from scipy.stats import norm
import matplotlib.pyplot as plot

def generate_time_values(count_of_time)-> list[int]:
    return [i for i in range(count_of_time)]

#count_splitter = интенствность потока
def generate_random_application(length_time_array, count_splitter) -> list[int]:

    array_application = []

    while length_time_array - count_splitter > 0:
        x = np.random.randint(low=0,high=count_splitter)
        for i in range(count_splitter):
            if i != x:
                array_application.append(0)
            else:
                array_application.append(1)
        length_time_array -= count_splitter
    x = np.random.randint(low=0, high=length_time_array)
    for i in range(length_time_array):
        if i != x:
            array_application.append(0)
        else:
            array_application.append(1)
    return array_application

# For normal distribution:
# мю = Мат. ожидание = 371;
# сигма = sqrt(мат. ожидание) = sqrt(371).

def random_values_distribution(array_application, mu, type_dist) -> list[int]:

    x = np.arange(0, 2*mu,int(log10(mu)))

    if type_dist == "Poisson":
        y = poisson.pmf(x, mu=mu)#FIXME FIXED!!! poisson work with only Integer values x-axis
        generate_diagram_of_distribution(x,y,"Poisson")
    else:
        normal_dist = norm(mu, sqrt(mu))
        y = normal_dist.pdf(x)
        generate_diagram_of_distribution(x,y,"Normal")

    array_values_distribution = []
    counter = 0

    while counter < len(array_application):
        if array_application[counter] == 0:
            counter += 1
            array_values_distribution.append(0)
        elif array_application[counter] == 1:
            if type_dist == "Poisson":
                rnd_value = int(poisson.rvs(mu))
            else:
                normal_dist = norm(mu, sqrt(mu))
                rnd_value = int(normal_dist.rvs())
            counter += 1
            array_values_distribution.append(rnd_value)
            while rnd_value != 0 and counter<len(array_application):
                rnd_value -= 1
                counter += 1
                array_values_distribution.append(rnd_value)

    return array_values_distribution

def status_application(array_values_distribution, array_application):

    array_status_application = []
    counter_success = 0
    counter_failed = 0

    for i in range (len(array_values_distribution)):
        if array_application[i] == 0:
            array_status_application.append("-")
        elif array_values_distribution[i-1] <= 1 and array_application[i] == 1:
            array_status_application.append("Work")
            counter_success += 1
        elif array_values_distribution[i-1] > 1 and array_application[i] == 1:
            array_status_application.append("Fail")
            counter_failed += 1
    return array_status_application,counter_success,counter_failed

def status_of_chanel(array_values_distribution)-> list[str]:

    array_status_chanel = []

    for i in range(len(array_values_distribution)):
        if array_values_distribution[i] != 0:
            array_status_chanel.append("Work")
        else:
            array_status_chanel.append("Free")
    return array_status_chanel

#depricated
def count_failed_application() -> int:
    return 0
#depricated
def count_success_application() -> int:
    return 0

def generate_diagram_of_distribution(x_array, y_array, name) -> None:
    plot.plot(x_array, y_array)
    plot.title(name + " distribution")
    plot.xlabel("Random variable")
    plot.ylabel("Probability")
    plot.show()

def important_values(mu, intensity):
    relative_throughput = intensity/(intensity+mu)
    absolute_bandwidth = intensity*relative_throughput
    probability_failure = 1 - relative_throughput
    return relative_throughput,absolute_bandwidth,probability_failure
