import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    # conn = sqlite3.connect(':memory:')
    print(sqlite3.version)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_entry(conn, table_name, fields, entry):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    column_names = ", ".join(fields)
    values = ", ".join(["?"]*len(fields))
    sql = """ INSERT INTO {}({})
              VALUES({}) """.format(table_name, column_names, values)
    cur = conn.cursor()
    cur.execute(sql, entry)
    return cur.lastrowid

def select_all(conn, table_name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(table_name))

    rows = cur.fetchall()

    for row in rows:
        print(row)
