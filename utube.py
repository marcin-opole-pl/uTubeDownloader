from pytube import YouTube
import sys
from set_lang import lang


def main():
    
    # Get url
    print('______________________________', end='\n\n')
    video = input(lang()[0])
    print('______________________________')

    # Check for http
    if not video.startswith('http'):
        video = 'http://' + video
    print(f'Pobieram informacje z: {video}', end='\n\n')
    
    # Search for video and setup callback
    try:
        yt = YouTube(video, on_progress_callback=progress_info)
    except:
        sys.exit("ERROR. Sprawdź połączenie z internetem. Sprawdź czy adres url jest poprawny")
        print('')

    # Get streams info
    i = yt.streams.filter(only_audio=True)
    print(yt.title)
    print('Dostępne streamy audio:', end='\n\n')
    for j in i:
        print('SIZE: ', j.filesize_mb, 'mb', ' -- ', j, end='\n\n')

    # Choose itag
    itag = input("Wybierz odpowiedni itag (jeżeli się da wybierz - 249): ")
    print('') 

    # Get stream 
    i = yt.streams.get_by_itag(itag)

    #Gets the title of the video
    title = input("Tytuł poprosze: ")
 
    #Just message
    print (f'Pobieram: {title}', end='\n\n')
    
    #Starts the download process
    try:
        i.download(output_path = 'D:/Audiobook',filename=title, max_retries=10)
    except:
        print('')
        sys.exit('Chwilowy błąd YouTube. Sprobuj za chwilę lub wybierz inny film do pobrania')
        print('')

# Checks and displays progress
def progress_info(stream, chunk, bytes_remaining):
    #Gets the percentage of the file that has been downloaded.
    downloaded = stream.filesize - bytes_remaining
    percent = (100*downloaded)/stream.filesize
    print(f'Pobrano {round(percent)}% z {round(stream.filesize_mb)} MB')
       

if __name__ == '__main__':
    main()