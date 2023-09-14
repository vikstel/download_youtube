from pytube import YouTube


YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
yt = YouTube('https://youtu.be/FyTL1bnUx5I?si=LGBuhTgOcQi8OkuF')
print(yt.title)
ys = yt.streams.get_highest_resolution()
ys.download()
print("Downloaded")


# download  pytube https://youtube.com/watch?v=2lAe1cqCOXo
# download playlist  pytube https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n
# https://youtube.com/playlist?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&si=6NfDpcXF-AMqBdu8 - salfedu Jango