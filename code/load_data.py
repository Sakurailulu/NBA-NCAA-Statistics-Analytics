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
    
    print("Inserting data into ncaa_players, ncaa_stats")
    query = "INSERT INTO ncaa_players VALUES()"\
    		"(%()s, %()s, ON CONFLICT DO NOTHING"

    # Insert 2008 data into ncaa_players table
    with open('datasets/ncaa_players_2008') as ncaa_2008:
    	reader = csv.reader(ncaa_2008, delimeter=',')

    	for row in reader:
    
    # Insert 2009 data into ncaa_players table
    with open('datasets/ncaa_players_2009') as ncaa_2009:
    	reader = csv.reader(ncaa_2009, delimeter=',')

    # Insert 2010 data into ncaa_players table
    with open('datasets/ncaa_players_2010') as ncaa_2010:
    	reader = csv.reader(ncaa_2010, delimeter=',')

if __name__ == "__main__":
    main()
A&M-Corpus Christi,26172,2013,"Ali, Hameed",1289295,So.,2012-13,G,6-2,29,81,220,0.368,23,78,0.295,33,43,0.767,52,1.793,56,1.931,5,0.172,42,1.448,218,7.517,35