# import pafy В ИТОГЕ НЕ РАБОТАЕТ
from pytube import YouTube

# url = input("URL, pleas -> ")

# def download(url):
#     try:
#         d = pafy.new(url)
#         streams = d.streams

#         avaliable_streams = {}
#         count = 1

#         for stream in streams:
#             avaliable_streams[count] = stream
#             print(f'{count} -> {stream}' )
#             count += 1
        
#         stream_count = int(input('Number stream - >'))
#         s = streams[stream_count-1].download()
#         print('finish download')

#     except:
#         print('oh, error')

# download(url)   

yt = YouTube('https://www.youtube.com/watch?v=o5wC0QqqN1c') #ссылка на видео.
# yt.stream показывает какое видео ты можешь скачать 
# (mp4(720) + audio или только mp4(1080) без звука). 
# Сейчас стоит фильтр по mp4.
print(yt.streams.filter(file_extension='mp4')) 
stream = yt.streams.get_by_itag(22) #выбираем по тегу, в каком формате будем скачивать.
stream.download() #загружаем видео.