"""
queries.py contain functionalities
"""

#NACC PLAYER LOOKUP
query="SELECT * From ncaa_players,nba_players WHERE ncaa_players.name LIKE concat('%', nba.player.name, '%')"
query="SELECT * FROM ncaa_players WHERE ncaa_players.name=%s"


#NBA PLAYER LOOKUP
query="SELECT * From ncaa_players,nba_players WHERE ncaa_players.name LIKE concat('%', nba.player.name, '%')"
query="SELECT * FROM nba_players WHERE nba_players.name=%s"


#ANNUAL NCAA REVIEW
#Average height and height range
query=" SELECT AVG(height),MAX(height),MIN(height) from ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s GROUP BY ncaa_stats.year" % year
#top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
query="SELECT player_name FROM ncaa_stats ORDER BY fg_attempts DESC LIMIT 10"
query="SELECTplayer_name FROM ncaa_stats ORDER BY tp_attempts DESC LIMIT 10"
query="SELECT player_name FROM ncaa_stats ORDER BY points DESC LIMIT 10"
query="SELECT player_name FROM ncaa_stats ORDER BY games_played DESC LIMIT 10"

#Top 10 players with highest % of attribute
query="SELECT player_name FROM ncaa_stats ORDER BY fg_percentage DESC LIMIT 10"
query="SELECTplayer_name FROM ncaa_stats ORDER BY tp_percentage DESC LIMIT 10"
query="SELECT player_name FROM ncaa_stats ORDER BY rb_percentage DESC LIMIT 10"
query="SELECT player_name FROM ncaa_stats ORDER BY ass_percentage DESC LIMIT 10"
query="SELECTplayer_name FROM ncaa_stats ORDER BY st_percentage DESC LIMIT 10"
query="SELECT player_name FROM ncaa_stats ORDER BY bl_percentage DESC LIMIT 10"
query="SELECT player_name FROM ncaa_stats ORDER BY turnover_percentage DESC LIMIT 10"



#ANNUAL NBA REVIEW
#Average height and height range
query=" SELECT AVG(height),MAX(height),MIN(height)from nba_stats,nba_players WHERE nba_stats.player_name=nba_players.name AND nba_stats.year=%s GROUP BY ncaa_stats.year" % year

#top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
query="SELECT player_name FROM nba_stats ORDER BY fg_attempts DESC LIMIT 10"
query="SELECTplayer_name FROM nba_stats ORDER BY tp_attempts DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY points DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY games_played DESC LIMIT 10"

#Top 10 players with highest % of attribute
query="SELECT player_name FROM nba_stats ORDER BY fg_percentage DESC LIMIT 10"
query="SELECTplayer_name FROM nba_stats ORDER BY tp_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY rb_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY ass_percentage DESC LIMIT 10"
query="SELECTplayer_name FROM nba_stats ORDER BY st_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY bl_percentage DESC LIMIT 10"
query="SELECT player_name FROM nba_stats ORDER BY turnover_percentage DESC LIMIT 10"