
a = '<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="7fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">'
b = a[9:-1].replace('"','').split(' ')

for element in b:
    if element.startswith('mime_type='):
        print(element[10:])

print(b)