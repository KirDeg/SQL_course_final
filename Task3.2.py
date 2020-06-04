# Использовались пакеты psycopg2(2.7.61), numpy(1.15.4), pandas(0.23.4). При решении задания предпологал, что в те дни,
# когда не указаны объемы продаж по определенному товару, то значит торговля по нему не велась вовсе

def my_func32(date_start, date_end):
    import psycopg2
    from collections import defaultdict
    import numpy as np
    import pandas as pd
    import datetime

    #Подключаемся к БД:
    conn = psycopg2.connect(dbname='AdHacks', user='postgres',
                            password='111222', host='localhost', port="5433")
    cursor = conn.cursor()

    # Составляем запрос:
    SQL1 = "SELECT DISTINCT product, SUM(revenue) AS revenue, date FROM revenue WHERE date BETWEEN '"
    SQL2 = "' AND '"
    SQL3 = "' GROUP BY date, product ORDER BY date;"
    SQL = SQL1 + date_start + SQL2 + date_end + SQL3
    cursor.execute(SQL)
    records = cursor.fetchall()
    cursor.close()
    conn.close()

    #Формируем упорядоченный набор попавших дат за указанный период:
    date_set = sorted(list({records[n][2] for n in range(len(records))}))
    # Формируем набор товаров:
    keys_set = (list({records[n][0] for n in range(len(records))}))

    # Составляем словарь, где отражено, в какие даты была получена выручка, включая и нулевую:
    dict1 = defaultdict(list)
    for m, n, k in records:
        dict1[k].append([m, n])

    for item in date_set:
        if len(dict1[item]) != len(keys_set):
            for item2 in list(set(keys_set) - set(dict1[item][n][0] for n in range(len(dict1[item])))):
                dict1[item].append([item2, 0])

    # Делаем список значений словаря одномерным:
    data_list = ([list(dict1.values())[n][j] for n in range(len(dict1.values())) for j in range(len(keys_set))])


    # Строим финальный словарь с правильной последовательностью продаж:
    dict_final = defaultdict(list)
    for a, b in data_list:
        dict_final[a].append(b)
    # Рассчитываем корреляционную матрицу:
    array_results = (np.corrcoef(list(dict_final.values())))

    # Составляем таблицу из корреляционной матрицы:
    null_values = np.zeros((len(array_results), 1))
    corr_matrix = pd.DataFrame(np.hstack((null_values, array_results)), columns=["Товар"] + sorted([n for n in keys_set]))
    corr_matrix.loc[:,"Товар"] = sorted([n for n in keys_set])
    corr_matrix.set_index("Товар", inplace=True)

    return corr_matrix


print(my_func32('2000/01/01', '2015-06-01'))
