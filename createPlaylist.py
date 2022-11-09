import requests

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/21gy23orrht2pmsir7hxxssli/playlists'
ACCESS_TOKEN = 'BQCKMvF1ahwUaX-VnQgbobi_pq39yuoUVN9g9KY0Pa-d5XyxrKdqZqPU8C7C_95txn2uAy-Q7iv9pRHoj-w7jzCYBr0fCOlreO523y9C93oN4cld6UxfBXIYQwAfe1KBzAUnK4b-lPPL36I-206KZKD5A-WLj9ckM3P4ddETlzxnxT_jieS4llmy3Rc6emo8fU9_gJZsjp5N6TambfpWJ3EXWZGPv1d5po1ZdOmEA5PgLX224SH6uqbze6-moNCu'

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name = "my private playlist",
        public = False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()