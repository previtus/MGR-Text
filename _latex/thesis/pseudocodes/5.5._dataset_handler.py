def load_dataset(path_to_segments_file):
# part of DatasetHandler which creates the Dataset object
	dataset = Dataset()
	dataset.init_from_segments(path_to_segments_file):
		# loads 4 important lists:
		Segments = LoadDataFile(path_to_segments_file)
		list_of_images, labels, osm, segment_ids = self.load_data_from_segments(Segments)
		self.init_from_lists(list_of_images, labels, osm, segment_ids)
	
	dataset.shuffle_by_segments()
	# shuffles data while respecting that the data from one segment should be next to each other

	return dataset

def load_data_from_segments(Segments):
	for Segment in Segments:
		for i_th_image in Segment.number_of_images:
			index = Segment.location_index[i_th_image]

			list_of_images <- Segment.get_image_filename(i_th_image)
			labels         <- Segment.get_score()
			osm            <- Segment.distinct_nearby_vector[index]
			segment_ids    <- Segment.get_id()
	return list_of_images, labels, osm, segment_ids