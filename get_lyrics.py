import lyricsgenius as lg
import os

file = open("./fleetwoodmac.txt", "w")

genius = lg.Genius(os.environ.get("GENIUS_ACCESS_TOKEN"), skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def get_lyrics(arr, k):
    c = 0
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("".join(s))
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:
            print(f"some exception at {name}: {c}")

if __name__=="__main__": 
    get_lyrics(['Fleetwood Mac'], 50)
