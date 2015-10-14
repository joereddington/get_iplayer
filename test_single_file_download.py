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

gauth =  enguage_auth()
drive = GoogleDrive(gauth)
myfile = drive.CreateFile({'id': '1EthTy-SWjJjFMqlPkC0bNb-6cvE-xpTVKFX2-HzLxXg'})
print myfile['title']  # world.png
print myfile['mimeType']  # world.png
myfile.GetContentFile("hope.csv",mimetype='text/csv')  # Save Drive file as a local file


