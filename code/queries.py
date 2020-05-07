"""
queries.py contain functionalities
"""
import psycopg2
import psycopg2.extras

conn_str = "host='localhost' dbname='dbms_final_project' user='dbms_project_user'\
             password='dbms_password'"
conn = psycopg2.connect(conn_str,cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()

#NCAA PLAYER LOOKUP
def ncaa_player_lookup(name):
    ret=[]
    query="SELECT * FROM ncaa_stats,ncaa_players WHERE ncaa_players.id=ncaa_stats.player_id AND ncaa_players.name ILIKE concat('%', %s, '%')"
    cursor.execute(query,(name))
    records=cursor.fetchall()
    resultofSearching=[]
    if(len(records))==0:
        resultofSearching.append("Can not find this player in the datasets")
    else:
        resultofSearching.append(records)
    ret.append(resultofSearching)
    query="SELECT * From ncaa_players,ncaa_stats,nba_stats WHERE ncaa_players.id=ncaa_stats.player_id AND ncaa_players.name LIKE concat('%', nba_players.name, '%') AND ncaa_players.name ILIKE concat('%', %s, '%')"
    cursor.execute(query,(name))
    records = cursor.fetchall()
    resultofEnteringNBA=[]
    if len(records)==0: 
        resultofEnteringNBA.append("This player was not on the nba team any time between 2000 and 2017") 
    else:
        resultofEnteringNBA.append(records)
    ret.append(resultofEnteringNBA)
    return ret
        


#NBA PLAYER LOOKUP
def nba_player_lookup(name):
    ret=[]
    query="SELECT * FROM nba_stats WHERE nba_stats.player_name ILIKE concat('%', %s, '%')"
    cursor.execute(query,(name))
    records=cursor.fetchall()
    resultofSearching=[]
    if(len(records))==0:
        resultofSearching.append("Can not find this player in the datasets")
    else:
        resultofSearching.append(records)
    ret.append(resultofSearching)
    query="SELECT * From nba_players,ncaa_players,ncaa_stats WHERE ncaa_players.id=ncaa_stats.player_id AND ncaa_players.name LIKE concat('%', nba_players.name, '%') AND nba_players.name ILIKE concat('%', %s, '%')"
    cursor.execute(query,(name))
    records = cursor.fetchall()
    resultofWasInNCAA=[]
    if len(records)==0: 
        resultofWasInNCAA.append("This player was not on the nba team any time between 2000 and 2017" )
    else:
        resultofWasInNCAA.append(records)
    ret.append(resultofWasInNCAA)
    return ret



#ANNUAL NCAA REVIEW
#Average height and height range
def annual_ncaa_review(year):
    ret=[]
    query=" SELECT AVG(height),MAX(height),MIN(height) from ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s GROUP BY ncaa_stats.year"
    cursor.execut(query,(year))
    records=cursor.fetchall()
    resultofHeight=[]
    if len(records)==0:
        resultofHeight.append("The year asked is not in database usage[2000-2017]")
    else:
        resultofHeight.append(records)
    ret.append(resultofHeight)
    return ret
    
#top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY fg_attempts DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY tp_attempts DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY games_played DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY three_pointers DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY rebounds DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY assists DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY  blocks DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY  steals DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY pts DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY turnovers DESC LIMIT 10"

#Top 10 players with highest % of attribute
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY fg_percentage DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY tp_percentage DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY rb_percentage DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY ass_percentage DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY st_percentage DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY bl_percentage DESC LIMIT 10"
query="SELECT name FROM ncaa_stats,ncaa_players WHERE  ncaa_stats.player_id=ncaa_players.id ORDER BY pts_pergame DESC LIMIT 10"



#ANNUAL NBA REVIEW
#Average height and height range
query=" SELECT AVG(height),MAX(height),MIN(height)from nba_stats,nba_players WHERE nba_stats.player_name=nba_players.name AND nba_stats.year=%s GROUP BY ncaa_stats.year" % year

#top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
query="SELECT player_name FROM nba_stats ORDER BY fg_attempts DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY tp_attempts DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY points DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY games_played DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY three_pointers DESC LIMIT 10"
#Top 10 players with highest % of attribute
query="SELECT player_name FROM nba_stats ORDER BY fg_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY tp_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY rb_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY ass_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY st_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY bl_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY turnover_percentage DESC LIMIT 10"


query="SELECT college,COUNT(college) AS frequency FROM nba_players GROUP BY college ORDER BY COUNT(college)  DESC LIMIT 10"
