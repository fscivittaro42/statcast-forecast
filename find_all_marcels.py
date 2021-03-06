import sqlite3
from marcel_projector import compute_marcel_projection

def create_file_with_headers(filename):
	'''
	Writes a new file with the given filename and populates the first row
	with column headers.

	Inputs: filename

	Returns: nothing - creates new file
	'''

	myfile = open(filename, 'w')

	HEADERS = ['player_id', 'name', 'position', 'team', 'year', 'age', 'g',
			   'ab', 'pa', 'h', 'singles', 'doubles', 'triples', 'homerun',
			   'runs', 'runs_batted_in', 'bb', 'ibb', 'so', 'hbp', 'sf', 'sh',
			   'gdp', 'sb', 'cs', 'avg', 'obp','slg', 'woba']

	myfile.write(','.join(HEADERS) + '\n')

	myfile.close()


def calculate_all_marcels(year, db, filename):
	'''
	Calculates Marcel projections for every player in the given database
	and stores the data in a csv file with the given filename.

	Inputs:
		year: the year to project for
		db: the database to retrieve names from
		filename: the file to append projections to

	Returns: nothing - updates filename
	'''

	player_list = retrieve_all_players(year - 1, db)

	for player in player_list:
		proj = compute_marcel_projection(player, year, db)

		myfile = open(filename, 'a')
		myfile.write(','.join(proj) + '\n')
		myfile.close()


def retrieve_all_players(year, db):
	'''
	Returns a list of all players from the database for a given year.

	Inputs:
		year: the year to retrieve players from - this is the year before the
			one we would like to project
		db: the database to retrieve names from

	Returns: a list of all the players found within the database for the given
		year
	'''

	conn = sqlite3.connect(db)
	c = conn.cursor()

	query="""
		  SELECT name FROM regular_data
		  WHERE year = ?
		  AND NOT shift
		  AND NOT noshift
		  AND NOT trad_shift
		  AND NOT nontrad_shift
		  """

	all_names = c.execute(query).fetchall()

	name_list = []

	for name in all_names:
		name_list.append(name[0])

	return list(set(name_list))