-- Project Schema

DROP SCHEMA IF EXISTS basketball;
CREATE SCHEMA basketball;

CREATE TABLE ncaa_players(
	player_id 	INTEGER PRIMARY KEY,
	player_name VARCHAR(255),
	school_name VARCHAR(255),
	class_year 	VARCHAR(40),
	height 		VARCHAR(40),
	position 	VARCHAR(40)
);

CREATE TABLE ncaa_stats(
	player_id 					INTEGER,
	player_name					VARCHAR(255),
	year 						INTEGER,
	position					VARCHAR(40),
	field_goals					INTEGER,
	field_goals_attempts		INTEGER,
	field_goals_percentage		FLOAT,
	three_points 				INTEGER,
	three_points_attempts		INTEGER,
	three_points_percentage		FLOAT,
	rebounds 					INTEGER,
	rebounds_per_game			FLOAT,
	assists 					INTEGER,
	assists_per_game			FLOAT,
	blocks 						INTEGER,
	blocks_per_game				FLOAT,
	steals 						INTEGER,
	steals_per_game				FLOAT,
	points 						INTEGER,
	points_per_game				FLOAT,
	turnovers					INTEGER,
	PRIMARY KEY(player_id, year)
);

CREATE TABLE nba_players(
	player_name VARCHAR(255),
	position	VARCHAR(40),
	height		VARCHAR(40),
	birthdate	VARCHAR(255),
	college		VARCHAR(255),
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
	ture_shoot						FLOAT,
	three_points_percentage			FLOAT,
	free_throw_rate					FLOAT,
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