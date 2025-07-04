import os
from dotenv import load_dotenv

from supabase import create_client
load_dotenv()

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
supabase = create_client(url, key)


def create_user(email, password):
    response = supabase.auth.sign_up(
    {
        "email": email,
        "password": password,
    }
)
    return response


def login_user(email, password):
    response = supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password,
        }
    )
    return response

email = input("Enter your email: ")
password = input("Enter your password: ")
login_user(email, password)