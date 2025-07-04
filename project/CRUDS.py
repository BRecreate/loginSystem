import os
from dotenv import load_dotenv
import json

from supabase import create_client
load_dotenv()

# carregar as variáveis de ambiente do arquivo .env
# para ter acesso ao banco do supabase

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
supabase = create_client(url, key)

# CRUDS para criar, ler, atualizar e deletar usuários

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

def get_user():
    user = supabase.auth.get_user()
    return user

def update_user(email, password):
    response = supabase.auth.update_user(
        {
            "email": email,
            "password": password,
        }
    )
    return response
def delete_user():
    response = supabase.auth.sign_out()
    return response

# Função para carregar e restaurar a sessão
def load_and_set_session():
    try:
        if os.path.exists("session.json"):
            with open("session.json", "r") as f:
                session_data = json.load(f)

            access_token = session_data.get("access_token")
            refresh_token = session_data.get("refresh_token")

            if access_token and refresh_token:
                # Restaura a sessão no cliente supabase
                supabase.auth.set_session(access_token, refresh_token)
                print("Sessão restaurada com sucesso!")
                user_id = supabase.auth.get_user().user.id
                print(user_id)
            else:
                print("Dados da sessão incompletos no arquivo.")
    except Exception as e:
        print(f"Falha ao carregar a sessão: {e}")

# Agora você pode verificar se o usuário está autenticado
try:
    user_response = supabase.auth.get_user()
    if user_response.user:
        print(f"Usuário autenticado: {user_response.user.email}")
        # Agora você pode fazer chamadas autenticadas para o banco de dados
        data, count = supabase.table('sua_tabela').select('*').execute()
        print(data)
    else:
        print("Nenhum usuário autenticado. Peça para o usuário fazer login.")
except Exception as e:
    print(f"Erro ao obter o usuário: {e}")

load_and_set_session()

try:
    user = supabase.auth.sign_in_with_password({
        "email": input(),
        "password": input(),
    })

    # Obter a sessão completa
    session = supabase.auth.get_session()

    # Salvar os dados da sessão em um arquivo JSON para persistência
    # Em uma aplicação real, considere um método de armazenamento mais seguro.
    if session:
        with open("session.json", "w") as f:
            f.write(session.json())
        print("Sessão salva com sucesso!")
    # O token de acesso do usuário agora está armazenado na sessão do cliente supabase
except Exception as e:
    print(f"Erro no login: {e}")

user_id = supabase.auth.get_user().user.id
print(user_id)

#supabase.auth.sign_out()supabase.auth.sign_out()
# Limpar a sessão
# if os.path.exists("session.json"):
#     os.remove("session.json")
#     print("Sessão limpa com sucesso!")