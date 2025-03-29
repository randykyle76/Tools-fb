import facebook

# Ganti dengan token akses Anda
ACCESS_TOKEN = 'your_access_token_here'

def get_user_profile():
    graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version="3.1")
    profile = graph.get_object("me")
    return profile

def post_status(message):
    graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version="3.1")
    post = graph.put_object(parent_object='me', connection_name='feed', message=message)
    return post

if __name__ == "__main__":
    # Contoh mendapatkan profil pengguna
    profile = get_user_profile()
    print("User Profile:", profile)

    # Contoh memposting status
    status_message = "Hello, this is a test post from my Python script!"
    post = post_status(status_message)
    print("Post ID:", post['id'])
