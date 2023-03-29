from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import datetime
import os
from upload_file_to_goggle_drive_config import folder_id

# upload file to this folder https://drive.google.com/drive/u/4/folders/1MM1ioDbpxYGNjsYLACnd_u64yAHETQDL path_to_dir_where_json_file_is
path_to_dir_where_json_file_is = \
                        os.path.join ( os.getcwd () ,
                                       'datasets' ,
                                       'json_key_for_google' )
json_file_name="stocks-formed-right-entry-7d1e2c6ba582.json"

# Set up the authentication parameters
creds = service_account.Credentials.from_service_account_file(
    os.path.join(path_to_dir_where_json_file_is,json_file_name))
service = build('drive', 'v3', credentials=creds)

# Set up the file path and name
path_to_dir_where_txt_file_with_data_is = \
                        os.path.join ( os.getcwd () ,
                                       'current_rebound_breakout_and_false_breakout' )

# Get the current date
today = datetime.datetime.now().strftime('%Y-%m-%d')



file_name = "stocks_" + today + '.txt'
file_path = os.path.join(path_to_dir_where_txt_file_with_data_is,file_name)



mime_type = 'text/plain'
media = MediaFileUpload(file_path, mimetype=mime_type)
# media = {'mimeType': 'text/plain', 'body': open(file_path, "rb")}
file_metadata = {'name': f'{file_name}', 'parents': [f'{folder_id}']}
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
print('File ID:', file.get('id'))
print(type(media))
print("media")
print(media)
# try:
#     file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
#     print('File ID: %s' % file.get('id'))
# except HttpError as error:
#     print('An error occurred: %s' % error)
