import mysql.connector
from contextlib import contextmanager
import logging
logger=logging.getLogger("db_helper")
logger.setLevel(logging.DEBUG)
file_handling=logging.FileHandler("server.log")
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handling.setFormatter(formatter)
logger.addHandler(file_handling)
@contextmanager
def connection():
    connector = mysql.connector.connect(host="localhost", user="root", passwd="root", database="expense_manager")
    if connector.is_connected():
        print("Connected")
    else:
        print("Not connected")
    my_cursor = connector.cursor(dictionary=True)
    yield my_cursor
    connector.commit()
    my_cursor.close()
    connector.close()

def fetch_data():
    logging.info("fetching data")
    with connection() as cursor:
        cursor.execute("SELECT * FROM expenses")
        datas = cursor.fetchall()
        for data in datas:
            print(data)
def fetch_expenses_from_date(expense_date):
    logger.info(f"fetching data for the given date:{expense_date}")
    with connection() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
        expense = cursor.fetchall()
    return expense
def insert_expenses(expense_date,amount,category,notes):
    logger.info(f"inserted expenses in the provided date :{expense_date}")
    with connection() as cursor:
        cursor.execute("INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",(expense_date,amount,category,notes),)
def delete_expenses(expense_date):
    logger.info(f"deleted all the  expenses in the given date:{expense_date}")
    with connection() as cursor:
        cursor.execute("DELETE FROM  expenses WHERE expense_date=%s",(expense_date,))
def fetch_expense_summary(start_date,end_date):
    logger.info(f"provide summary of all expenses for the days between {start_date} and {end_date}")
    with connection() as cursor:
        cursor.execute(" SELECT category,SUM(amount) as total FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category;",(start_date,end_date)  )
        data=cursor.fetchall()
        return data
def fetch_expense_monthly(start_date,end_date):
    logger.info(f"provide summary of all expenses for the days between {start_date} and {end_date}")
    with connection() as cursor:
        cursor.execute(" SELECT expense_date,SUM(amount) as total FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY expense_date;",(start_date,end_date)  )
        data=cursor.fetchall()
        return data
if __name__ == "__main__":
   insert_expenses("2024-08-02",500,"Food","Biriyani")
   fetch_expenses_from_date("2024-08-02")
   delete_expenses("2024-08-02")
   fetch_expenses_from_date("2024-08-02")

   summary=fetch_expense_summary(start_date="2024-08-01",end_date="2024-08-05")
   for spends in summary:
       print(spends)
   


