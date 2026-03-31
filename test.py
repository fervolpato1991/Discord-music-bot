import yt_dlp

ytdl = yt_dlp.YoutubeDL()

info = ytdl.extract_info("https://www.youtube.com/watch?v=dQw4w9WgXcQ", download=True)

print("OK", info["title"])