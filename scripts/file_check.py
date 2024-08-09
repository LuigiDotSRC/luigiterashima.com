import os
from datetime import datetime, timezone

def get_file_modification_time(file_path):
    """Retrieve the time a file was last modified on the local machine
    :param file_path: file path of the target file 
    :return: datetime object of the last modification 
    """
    try:
        mod_time = os.path.getmtime(file_path)
        mod_time_datetime = datetime.fromtimestamp(mod_time)
        mod_time_utc = mod_time_datetime.astimezone(timezone.utc)
        # formatted_mod_time = mod_time_utc.strftime('%Y-%m-%d %H:%M:%S')

        return mod_time_utc
    except FileNotFoundError:
        return f"File {file_path} not found."
    except Exception as e:
        return str(e)
    
def get_files_in_dir(dir):
    """Retrieve the filepaths of all the files in a directory 
    :param file_path: target directory 
    :return: list of all the files inside the directory in strings  
    """
    try:
        entries = os.listdir(dir)
        files = [os.path.join(dir, entry) for entry in entries if os.path.isfile(os.path.join(dir, entry))]
        return files
    except FileNotFoundError:
        return f"Directory {dir} not found."
    except Exception as e:
        return str(e)
        