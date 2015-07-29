#Here's what I want, I want to download subtitle files, convert them into CVS ones and make them ready to go up to Google Drive. 

#Let's work this out. 

#Download: done. 
perl get_iplayer http://www.bbc.co.uk/iplayer/episode/b064449w/the-worlds-worst-place-to-be-disabled --modes=subtitles

#Convert to SRT
python convertSubtitles.py nameoffile

#Convert into CSV
echo we have the SRT python library for this - Maybe, in fact, we do it directly from convertSubtitles.py

#Upload to google drive
