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
    player_query = "INSERT INTO ncaa_players(player_id, year, player_name, school_name, class_year, height, position)"\
    		"VALUES (%(player_id)s, %(year)s, %(player_name)s, %(school_name)s, %(class_year)s, %(height)s, %(position)s) ON CONFLICT DO NOTHING"

    stats_query = "INSERT INTO ncaa_stats(player_id, player_name, year, position, field_goals, field_goals_attempts, field_goals_percentage,\
    							three_points, three_points_attempts, three_points_percentage, rebounds, rebounds_per_game, assists,\
    							assists_per_game, blocks, blocks_per_game, steals, steals_per_game, points, points_per_game, turnovers)"\
    			  "VALUES( %(player_id)s, %(player_name)s, %(year)s, %(position)s, %(fg)s, %(fg_a)s, %(fg_p)s, %(threept)s, %(threept_a)s,\
    			  			%(threept_p)s, %(rb)s, %(rb_pg)s, %(ass)s, %(ass_pg)s, %(bl)s, %(bl_pg)s, %(st)s, %(st_pg)s, %(pts)s, %(pts_pg)s,\
    			  			%(turnovers)s ) ON CONFLICT DO NOTHING"

    # Insert 2008 data into ncaa_players table
    with open('datasets/ncaa_players_2008') as ncaa_2008:
    	reader = csv.reader(ncaa_2008, delimeter=',')
    	for row in reader:
    		cursor.execute(
    			player_query,
    			dict( player_id=row[4], year=2008, player_name=row[3], school_name=row[0], class_year=row[5], height=row[8], position=row[7] )
    		)

    		cursor.execute(
    			stats_query,
    			dict( player_id=row[4], player_name=row[3], year=2008, position=row[7], fg=row[10], fg_a=row[11], fg_p=row[12], threept=row[13],\
    				 threept_a=row[14], threept_p=row[15], rb=row[19], rb_pg=row[20], ass=row[21], ass_pg=row[22], bl=row[23], bl_pg=row[24], st=row[25],\
    				 st_pg=row[26], pts=row[27], pts_pg=row[28], turnovers=row[29])
    		)
    	conn.commit()
    print("Added data for 2008...")

    # Insert 2009 data into ncaa_players table
    with open('datasets/ncaa_players_2009') as ncaa_2009:
    	reader = csv.reader(ncaa_2009, delimeter=',')
    	for row in reader:
    		cursor.execute(
    			player_query,
    			dict( player_id=row[4], year=2009, player_name=row[3], school_name=row[0], class_year=row[5], height=row[8], position=row[7] )
    		)

    		cursor.execute(
    			stats_query,
    			dict( player_id=row[4], player_name=row[3], year=2009, position=row[7], fg=row[10], fg_a=row[11], fg_p=row[12], threept=row[13],\
    				 threept_a=row[14], threept_p=row[15], rb=row[19], rb_pg=row[20], ass=row[21], ass_pg=row[22], bl=row[23], bl_pg=row[24], st=row[25],\
    				 st_pg=row[26], pts=row[27], pts_pg=row[28], turnovers=row[29])
    		)
    	conn.commit()
    print("Added data for 2009...")

    # Insert 2010 data into ncaa_players table
    with open('datasets/ncaa_players_2010') as ncaa_2010:
    	reader = csv.reader(ncaa_2010, delimeter=',')
    	for row in reader:
    		cursor.execute(
    			player_query,
    			dict( player_id=row[4], year=2010, player_name=row[3], school_name=row[0], class_year=row[5], height=row[8], position=row[7] )
    		)

    		cursor.execute(
    			stats_query,
    			dict( player_id=row[4], player_name=row[3], year=2010, position=row[7], fg=row[10], fg_a=row[11], fg_p=row[12], threept=row[13],\
    				 threept_a=row[14], threept_p=row[15], rb=row[19], rb_pg=row[20], ass=row[21], ass_pg=row[22], bl=row[23], bl_pg=row[24], st=row[25],\
    				 st_pg=row[26], pts=row[27], pts_pg=row[28], turnovers=row[29])
    		)
    	conn.commit()
    print("Added data for 2010...")


if __name__ == "__main__":
    main()