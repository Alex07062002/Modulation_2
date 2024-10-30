import math
import openpyxl

import ExcelHelper
import distribution_support

#Вариант-18
UNIT_OF_TIME = 100
COUNT_OF_TIME = 100*UNIT_OF_TIME #(100 minutes)

INTENSITY = 2.19
COUNTER_SPLITTER = int(UNIT_OF_TIME//INTENSITY) #service_intensity
MU = 3.71*UNIT_OF_TIME

NAME_OF_FILE = "C:\\Users\\Alexey\\Desktop\\Modulation\\Output.xlsx"


if __name__ == "__main__":
    relative_throughput, absolute_bandwidth, probability_failure = distribution_support.important_values(MU,INTENSITY)
    time_array = distribution_support.generate_time_values(COUNT_OF_TIME)
    application_array = distribution_support.generate_random_application(len(time_array),COUNTER_SPLITTER)
    array_distribution = distribution_support.random_values_distribution(application_array, MU, "Poisson")
    array_status_application, count_success, count_failed = distribution_support.status_application(array_distribution, application_array)
    array_status_chanel = distribution_support.status_of_chanel(array_distribution)

    ExcelHelper.open_and_write_to_excel(time_array,"A",NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel(application_array,"B",NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel(array_distribution,"C",NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel(array_status_application,"D",NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel(array_status_chanel,"E",NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel([count_success],"F",NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel([count_failed],"G",NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel([relative_throughput], "H", NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel([absolute_bandwidth], "I", NAME_OF_FILE)
    ExcelHelper.open_and_write_to_excel([probability_failure], "J", NAME_OF_FILE)

    list_with_values = ["Момент времени","Событие согласно интенсивности","Оставшаяся продолжительность работы канала",
                        "Статус обработки заявки","Статус канала","Заявок обработано","Заявок пропущено",
                        "относительная пропускная способность","абсолютная пропускная способность","Вероятность отказа"]

    workbook = openpyxl.load_workbook(NAME_OF_FILE)
    worksheet = workbook.active
    for i in range(len(list_with_values)):
        worksheet.cell(row=1,column=i+1).value = list_with_values[i]
    workbook.save(NAME_OF_FILE)