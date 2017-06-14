def getGoogleViewUrls(self, min_allowed_distance = 30)
        edge_length = 1000*distance_between_two_points(self.Start, self.End)
        number_of_fractions = int(max(floor(edge_length / min_allowed_distance),1.0))

        for (last_fraction, current_fraction) in fractions:
            # runs for example with 0.0 - 0.2, 0.2 - 0.4, ..., 0.8 - 1.0
            PointA = interpolation(self.Start, self.End, fraction=last_fraction)
            PointB = interpolation(self.Start, self.End, fraction=current_fraction)

            urls, filenames <- self.betweenPoints(PointA, PointB)

	return urls, filenames