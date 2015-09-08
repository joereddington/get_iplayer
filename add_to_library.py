import os
import convertSubtitles
import pysrt
import csv

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import argparse

def setup_argument_list():
     "creates and parses the argument list for naCount"
     parser = argparse.ArgumentParser(
         description=__doc__)
     parser.add_argument('-u', nargs="?",dest='url',
                         help="Allows use of a folder url from the commandline")
     return parser.parse_args()

def get_url():
     args=setup_argument_list()
     url=DEFAULT_URL
     if args.url:
             url=args.url
     return url

def enguage_auth():
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile("mycreds.txt")
        if gauth.credentials is None:
                # Authenticate if they're not there
                gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
                # Refresh them if expired
                gauth.Refresh()
        else:
                # Initialize the saved creds
                gauth.Authorize()
        # Save the current credentials to a file
        gauth.SaveCredentialsFile("mycreds.txt")
        # from http://stackoverflow.com/a/24542604/170243
        gauth.LocalWebserverAuth()
        return gauth


def upload_csv(name_here,name_there):
        drive = GoogleDrive(enguage_auth())
        file5 = drive.CreateFile({"parents": [{"kind": "drive#fileLink","id":"0BxcNVxCOXNUvfkIyMWxIcGU2WkdfX0FiOTljYzVlZ1V5eW5NXzY0bHpQUGpPV3hfTkI1VHM" }]})
        # Read file and set it as a content of this instance.
        file5.SetContentFile(name_here)
        file5['title']=name_there
        file5.Upload({'convert': True})  # Upload it


def convert_srt_to_sup(input_file, out_file):
        subs = pysrt.open(input_file)
        with open(out_file, "wb") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ("Start",
                     "End",
                     "Character",
                     "Original Text",
                     "Translation",
                     "Machine Translations"))
                for caption in subs:
                        print caption.text
                        writer.writerow(
                            (caption.start, caption.end, "", caption.text.encode('latin-1'), "", ""))



DEFAULT_URL = "http://www.bbc.co.uk/iplayer/episode/b068232r/secrets-of-china-1-fit-in-or-fail"
URL=get_url()
name_there = URL.rpartition('/')[2]
name_here = name_there+".csv"

os.system("perl get_iplayer --force "+URL+" --modes=subtitles")
# Download: done.

# Convert to SRT
convertSubtitles.ttml2srt(["lastdownloaded.srt"], False, False)

# Convert into CSV (which I'm choosing to call *.Sup)
convert_srt_to_sup('lastdownloaded_converted.srt', name_here)
# Upload to google drive
upload_csv(name_here,name_there)


def test_cases_to_write():
        """
        We need,

        Several checks that we are downloading the correct file
                find out if there is a file comparison bit of the unit testing
        Check the empty file.
        Check extremely long file (in terms of content, and of time passing)
        Several checks that the file we convert matches our other examples.
        Several checks that converting to *.sup format works

        Several checks that the *.sup format, once downloaded, works with
        the rest of the framework.
        A long form check, with an srt file going up, coming down and
        converting to english.


        """
        pass
