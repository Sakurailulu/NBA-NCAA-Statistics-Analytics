import psycopg2
import psycopg2.extras
import csv

connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password'"
conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()


def main():
    # Creating schema
    print("Creating schema...")
    cursor.execute(open("schema.sql", "r").read())


    print("Loading data")
    




if __name__ == "__main__":
    main()
