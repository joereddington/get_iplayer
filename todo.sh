#Here's what I want, I want to download subtitle files, convert them into CVS ones and make them ready to go up to Google Drive. 

#Let's work this out. 

#Download: done. 
perl get_iplayer http://www.bbc.co.uk/iplayer/episode/b064449w/the-worlds-worst-place-to-be-disabled --modes=subtitles

#Convert to SRT
python convertSubtitles.py nameoffile

#Convert into CSV
python convert_srt_to_sup.py #needs to take in arguments (and have a test suite)
#Upload to google drive


def test_cases_to_write(): 
"""
We need, 

Several checks that we are downloading the correct file
	find out if there is a file comparison bit of the unit testing
Check the empty file. 
Check extremely long file (in terms of content, and of time passing) 
Several checks that the file we convert matches our other examples. 
Several checks that converting to *.sup format works 

Several checks that the *.sup format, once downloaded, works with the rest of the framework. 
A long form check, with an srt file going up, coming down and converting to english. 


"""
	pass

