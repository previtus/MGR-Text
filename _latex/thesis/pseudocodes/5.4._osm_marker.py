def Marker(Segments, radius = 100):
# OSM Marker
	global connection
	connection = ConnectionHandler() # handles Python <> PostgreSQL DB

	for Segment in Segments:
		MarkSegment(Segment, radius)
	return Segments

def MarkSegment(Segment, radius):
	for (i, distinct_location) in Segment.DistinctLocations:
		nearby_vector = connection.query_location(distinct_location, radius)
		Segment.mark_with_vector(nearby_vector, i)

class ConnectionHandler:
def query_location(self, location, radius):
	sql_command = self.sql_cmd_radius(location, radius)
	# builds the query 
	# SELECT <interesting_columns> FROM table WHERE distance < radius

	rows, column_names = self.run_command( sql_command )
	
	pairs = extract_all_pairs(rows, column_names)
	# returns pairs of column names and their values
	# for example "highway=primary", ...

	nearby_vector = [0] * number_of_observed_pairs
	
	for pair in pairs
		if pair in observed_pairs:
			index = indice_dictionary(pair)
			nearby_vector[ index ] += 1
	return nearby_vector