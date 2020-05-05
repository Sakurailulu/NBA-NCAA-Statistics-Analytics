-- Project Schema

DROP SCHEMA IF EXISTS basketball;
CREATE SCHEMA basketball;

DROP TABLE IF EXISTS ncaa_players;
DROP TABLE IF EXISTS ncaa_stats;
DROP TABLE IF EXISTS nba_players;
DROP TABLE IF EXISTS nba_stats;

CREATE TABLE ncaa_players(
	player_id 		INTEGER,
	year 			INTEGER,
	player_name 	VARCHAR(255),
	school_name 	VARCHAR(255),
	class_year 		VARCHAR(40),
	height 			VARCHAR(40),
	position 		VARCHAR(40),
	PRIMARY KEY(player_id, year)
);

CREATE TABLE ncaa_stats(
	player_id 					INTEGER,
	player_name					VARCHAR(255),
	year 						INTEGER,
	position					VARCHAR(40),
	field_goals					INTEGER DEFAULT 0,
	field_goals_attempts		INTEGER DEFAULT 0,
	field_goals_percentage		FLOAT DEFAULT 0,
	three_points 				INTEGER DEFAULT 0,
	three_points_attempts		INTEGER DEFAULT 0,
	three_points_percentage		FLOAT DEFAULT 0,
	rebounds 					INTEGER DEFAULT 0,
	rebounds_per_game			FLOAT DEFAULT 0,
	assists 					INTEGER DEFAULT 0,
	assists_per_game			FLOAT DEFAULT 0,
	blocks 						INTEGER DEFAULT 0,
	blocks_per_game				FLOAT DEFAULT 0,
	steals 						INTEGER DEFAULT 0,
	steals_per_game				FLOAT DEFAULT 0,
	points 						INTEGER DEFAULT 0,
	points_per_game				FLOAT DEFAULT 0,
	turnovers					INTEGER DEFAULT 0,
	PRIMARY KEY(player_id, year)
);

CREATE TABLE nba_players(
	player_name 	VARCHAR(255),
	position		VARCHAR(40),
	height			VARCHAR(40),
	birthdate		VARCHAR(255),
	college			VARCHAR(255),
	PRIMARY KEY(player_name, birthdate)
);

CREATE TABLE nba_stats(
	player_name						VARCHAR(255),
	year 							INTEGER,
	position						VARCHAR(40),
	age 							INTEGER,
	team 							VARCHAR(40),
	games_played					INTEGER,
	minutes_player					INTEGER,
	true_shoot						FLOAT,
	offensive_rebound_percentage	FLOAT,
	defensive_rebound_percentage	FLOAT,
	total_rebound_percentage		FLOAT,
	assist_pecentage				FLOAT,
	steal_percentage				FLOAT,
	blocks_percentage				FLOAT,
	turnover_percentage				FLOAT,
	field_goals 					INTEGER,
	field_goals_attempts 			INTEGER,
	field_goals_percentage			FLOAT,
	three_points 					INTEGER,
	three_points_attempts			INTEGER,
	three_points_percentage			FLOAT,
	points 							INTEGER,
	PRIMARY KEY(player_name, team)
);