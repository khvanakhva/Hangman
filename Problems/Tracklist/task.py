def tracklist(**tracks):
    for key, value in tracks.items():
        print(key)
        for k, j in value.items():
            print('ALBUM:', k, 'TRACK:', j)
