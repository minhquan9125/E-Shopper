import pymysql 
def get_connection(): 
    conn = pymysql.connect(
    host='localhost', 
    user='root',           
    database='sql_python',   
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
    return conn