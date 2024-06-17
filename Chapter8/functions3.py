#8.6
def city_country(city,country):
    result = city+", "+ country
    return result.title()

message = city_country('kathmandu','nepal')
print(message)
message = city_country('new delhi','india')
print(message)
message = city_country('boston','united states of america')
print(message)

#8.7
def make_album1(artist,title,songs=None):
    if songs:
        music_album={'Artist Name':artist,'Album Title':title,'Number of Songs':songs}
    else:
        music_album={'Artist Name':artist,'Album Title':title}
    return music_album

album = make_album1('Atif Aslam','wowo')
print(album)
album = make_album1('Narayan Gopal','Real',97)
print(album)
album = make_album1('Udit Narayan','Old')
print(album)

#8.8
def make_album2(artist,title,songs=None):
    if songs:
        music_album={'Artist Name':artist,'Album Title':title,'Number of Songs':songs}
    else:
        music_album={'Artist Name':artist,'Album Title':title}
    print(music_album)

while True:
    print("Enter the details...")
    artist_name = input("Artist Name:")
    album_title = input("Album Title:")

    if artist_name == 'q':
        break
    else:
        make_album2(artist_name,album_title)





