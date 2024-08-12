from supabase import create_client, Client 
from dotenv import load_dotenv
import os 
import random 
import string 

load_dotenv() 
URL = os.getenv('SUPABASE_URL')
KEY = os.getenv('SUPABASE_KEY')
TABLE_NAME = 'blogs'

supabase = create_client(URL, KEY)

def generate_random_id():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(10)) 
    
def upload_blog(file_name, title, tags):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.abspath(os.path.join(script_dir, f'../blogs/{file_name}'))

    with open(file_path, 'r') as file:
        content = file.read() 
        response = (
            supabase.table(TABLE_NAME)
            .insert({
                'id': generate_random_id(),
                'title': title,
                'content': content, 
                'tags': tags
            })
            .execute()
        )

if __name__ == '__main__':
    file = input('Enter blog filename: ')
    title = input('Enter blog title: ')
    tags_list = []

    try: 
        while True:
            user_input = input("Enter a tag (CTRL-D to finish): ")
            tags_list.append(user_input)    
    except EOFError:
        pass

    upload_blog(file, title, tags_list)
    print('Uploading blog to database')