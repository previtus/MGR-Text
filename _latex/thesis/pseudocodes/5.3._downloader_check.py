def RunCheck(segments_filename):
# Check downloaded segments and fix them
	Segments = LoadDataFile(segments_filename)
	if (HasErroneousData(Segments, ERROR)):
		Segments = FixDataFile_FailedDownloads(Segments, ERROR)
	SaveDataFile(Segments, segments_filename)

def FixDataFile_FailedDownloads(Segments, ERROR):
	BrokenSegments = []
	for (i, Segment) in Segments:
		if Segment.ErrorMesages[i] == ERROR
			BrokenSegments.append(Segment)

	FilenameMapOfBroken <- GenListOfUrls(BrokenSegments)
	DownloadUrlFilenameMap(FilenameMapOfBroken, BrokenSegments)
	return Segments