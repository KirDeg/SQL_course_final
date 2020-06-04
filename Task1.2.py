# Задание выполнялось на Python 3.6.7. Использовались пакеты psycopg2(2.7.61) для подключения к БД PostgreSQL из Python
# и datetime для правильного отображения формата дат


def my_func(product):

    import psycopg2
    import datetime

    conn = psycopg2.connect(dbname='AdHacks', user='postgres',
                            password='111222', host='localhost', port="5433")
    cursor = conn.cursor()

    SQL1 = "SELECT date_start, price FROM prices WHERE product = '"
    SQL2 = "' ORDER BY date_start ASC;"
    SQL = SQL1 + str(product) + SQL2
    cursor.execute(SQL)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return([str(records[n][0]) for n in range(len(records))], [records[n][1] for n in range(len(records))])


print(my_func('B'))
