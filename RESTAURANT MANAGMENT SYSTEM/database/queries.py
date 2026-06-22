from database.db_connection import get_connection
#signup function
def insert_user(name,email,contact,city,password):
    conn=get_connection()
    cursor=conn.cursor()
    query=""" INSERT INTO USERS (NAME,EMAIL,CONTACT,CITY,PASSWORD)
              VALUES (%s,%s,%s,%s,%s)"""
    cursor.execute(query,(name,email,contact,city,password))
    conn.commit()
    cursor.close()
    conn.close()

#login function
def login_user(contact,password):
    conn=get_connection()
    cursor=conn.cursor()
    query="""
    SELECT * FROM USERS 
    WHERE CONTACT=%s AND PASSWORD=%s"""
    cursor.execute(query,(contact,password))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    return user

#Sign up check
def check_user(contact):
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT * FROM USERS WHERE CONTACT=%s"
    cursor.execute(query,(contact,))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    return user

#UPDATE LOGIN
def update_login_status(contact,status):
    conn=get_connection()
    cursor=conn.cursor()
    query=""" UPDATE USERS SET IS_LOGGED_IN = %s WHERE CONTACT = %s"""
    cursor.execute(query,(status,contact))
    conn.commit()
    cursor.close()
    conn.close()

#Logged_user
def get_logged_in_user():
    conn=get_connection()
    cursor=conn.cursor()
    query=""" SELECT * FROM USERS WHERE IS_LOGGED_IN = 1"""
    cursor.execute(query)
    user=cursor.fetchone()
    cursor.close()
    return user

#bill_no
def get_next_bill_no():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT MAX(BILL_NO) FROM BILLS"
    cursor.execute(query)
    result = cursor.fetchone()
    if result[0] is None:
        return 1001
    return result[0] + 1

#Save button
def save_bill(costomer_name,contact,city,bill_date,bill_time,table_no,grand_total):
    conn=get_connection()
    cursor=conn.cursor()
    query = """ INSERT INTO BILLS (CUSTOMER_NAME,CONTACT,CITY,BILL_DATE,BILL_TIME,TABLE_NO,GRAND_TOTAL) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values=(costomer_name,contact,city,bill_date,bill_time,table_no,grand_total)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()
