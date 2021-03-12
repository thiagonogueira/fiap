# Schema: accountid, dateofpurchase, transactionid, purchaseprice, storename, storecategory, cityname, provincename, purchasemethod
#AccId, Date, TransactionId, Price, MerchantName, MerchantCategory, City, Province, Purchase Method
#0714,2015-07-01,4000645,506.94,Rage Shoes,Shoes,Kroonstad,Free State,credit

from datetime import datetime
import random
import time
import uuid

import cx_Oracle

YEAR = 2020
MONTH = 3
DAY = 11


N_REGISTERS = random.randint(259200 * .85, 259200 * 1.15)
# N_REGISTERS = 10
SLEEP_TIME = 0.3

MINTIME = datetime(YEAR, MONTH, DAY, 0, 0, 0)
MAXTIME = datetime(YEAR, MONTH, DAY, 23, 59, 59)

OUTPUT_TYPES = ['db']

method = ["credit", "debit", "credit", "credit", "debit", "credit", "credit", "cash", "credit"]

shop_dict = {
    'Edgars': 'Clothing',
    'CNA': 'Stationary',
    'Sportmans Warehouse': 'Sports Equipment',
    'Pick n Pay': 'Groceries',
    'Rage Shoes': 'Shoes',
    'BT Games': 'Games',
    'Dions Wired': 'Electronics',
    'Makro': (
        'Shoes',
        'Clothing',
        'Electronics',
        'Groceries',
        'Stationary',
        'Sports Equipment',
        'Games'
        )
    }

city_dict = {
    'Kroonstad': 'Free State',
    'Cape Town': 'Western Cape',
    'Pretoria': 'Gauteng',
    'PE': 'Eastern Cape',
    'Johannesburg': 'Gauteng',
    'Potchefstroom': 'North West',
    'Bloemfontein': 'Free State',
    'Stellenbosch': 'Western Cape',
    'Krugersdorp': 'Gauteng',
    'Somerset West': 'Western Cape',
    'Kimberley': 'Northern Cape',
    'Upington': 'Northern Cape',
    'Klerksdorp': 'North West',
    'Potchefstroom': 'North West',
    'Parys': 'Free State',
    'Gauteng': 'Boksburg'
    }

min_ts = int(time.mktime(MINTIME.timetuple()))
max_ts = int(time.mktime(MAXTIME.timetuple()))


if 'file' in OUTPUT_TYPES:
    out_dir = '/data/marketplace/sales'
    filename =  str(YEAR) + str(MONTH).zfill(2) + str(DAY).zfill(2) + '.csv'
    outFileName = out_dir + '/' + filename
    f = open(outFileName,'a')

if 'db' in OUTPUT_TYPES:
    connection = cx_Oracle.connect(
    'hdpadmin',
    'hadoop',
    'localhost/xe')

    cursor = connection.cursor()
    cursor.execute(
        "ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS'"
        " NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF'"
        )

i = 1
while True:
    time.sleep(SLEEP_TIME)

    account_id = str(random.randint(1, 1000)).zfill(4)
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction_id = str(uuid.uuid1())
    value = '{:.2f}'.format(random.randint(2900, 80000) / 100)
    x_stores = random.choice(list(shop_dict.keys()))
    x_category = shop_dict[x_stores] if x_stores != 'Makro' else shop_dict[x_stores][random.randint(0,6)]
    x_cities = random.choice(list(city_dict.keys()))
    x_province = city_dict[x_cities]
    x_choice = random.choice(method)

    out_line = (
        account_id,
        date_time,
        transaction_id,
        value,
        x_stores,
        x_category,
        x_cities,
        x_province,
        x_choice
    )

    if 'file' in OUTPUT_TYPES:
            f.write('|'.join(out_line) + '\n')
            f.flush()

    if 'db' in OUTPUT_TYPES:
        cursor.execute("insert into mp_sales values (:1, :2, :3, :4, :5, :6, :7, :8, :9)", out_line)
        connection.commit()

    if not i / 1000:
        print(i)

f.close()
connection.close()
