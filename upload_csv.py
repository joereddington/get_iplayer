#!/usr/bin/env python
"""Uploads csv files from local directory to Google Drive
TODO:
put in particular directory,
make sure that you back off if file exists
have a library file that contains commonly used functions

"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


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


drive = GoogleDrive(enguage_auth())
file5 = drive.CreateFile()
# Read file and set it as a content of this instance.
file5.SetContentFile('out.csv')
file5.Upload({'convert':True})  # Upload it
