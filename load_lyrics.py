import pandas as pd
from lyricsgenius import Genius


def load_lyrics(save_folder):
    TOKEN = input('Enter Genius access token: ')
    genius = Genius(TOKEN)
    data = []
    top2000 = pd.read_excel('NPORadio2-Top-2000-2024.xlsx')
    for _, info in top2000.iterrows():
        song = genius.search_song(title=info['Titel'], artist=info['Artiest'])
        print(song.lyrics)
        data.append({'title': info['Titel'], 'artist': info['Artiest'], 'rank': info['Numering'], 'year': info['Jaar'],
                     'lyrics': song.lyrics})
    return data


