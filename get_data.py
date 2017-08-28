import sys
import json
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    spotify = spotipy.Spotify(auth=token)
    data = []

    # List of urban artists.
    artists = ['Daddy Yankee','Wisin','Yandel','Bad Bunny','J Balvin','Don Omar','Ozuna','Maluma','Arcangel', \
                'De La Ghetto','Farruko','Nicky Jam','Zion & Lennox','Alexis & Fido','J Alvarez','Cosculluela', \
                'Pusho','Almighty','Justin Quiles','Noriel','Jowell & Randy','Plan B','Lary Over','Brytiago', \
                'Darkiel','Jory Boy','Baby Rasta & Gringo','Alexio','Yomo', 'Tego Calderon','Tony Dize','Reykon', \
                'White Noise & D-Anel','CNCO','Juanka','DJ Luian','Dayme y El High','Kevin Roldan','Anuel AA','Sammy & Falsetto', \
                'Los De La Nazza']
    print "Artists # " + str(len(artists))
    for artist in artists:
        results = spotify.search(q='artist:' + artist, type='artist')
        items = results['artists']['items']
        info = {}
        tracks = {}
        if len(items) > 0:
            info['id'] = items[0]['uri'].split(':')[-1]
            info['popularity'] = items[0]['popularity']
            info['genres'] = items[0]['genres']
            info['followers'] = items[0]['followers']['total']
            top_tracks = spotify.artist_top_tracks(info['id'])
            json_tracks = []
            for track in top_tracks['tracks']:
                tracks['name'] = track['name']
                tracks['popularity'] = track['popularity']
                tracks['id'] = track['id']
                analysis = spotify.audio_features(str(track['id']))[0]
                tracks['acousticness'] = analysis['acousticness']
                tracks['danceability'] = analysis['danceability']
                tracks['duration_ms'] = analysis['duration_ms']
                tracks['energy'] = analysis['energy']
                tracks['instrumentalness'] = analysis['instrumentalness']
                tracks['key'] = analysis['key']
                tracks['liveness'] = analysis['liveness']
                tracks['loudness'] = analysis['loudness']
                tracks['tempo'] = analysis['tempo']
                tracks['valence'] = analysis['valence']
                json_tracks.append(tracks)
                tracks = {}
            print json_tracks
            exit()
            info["tracks"] = json_tracks
            data.append({artist:info})
    print data
else:
    print "Can't get token for", username





