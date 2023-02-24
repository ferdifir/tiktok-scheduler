import tiktokapi
import datetime
import time

# Masukkan informasi login akun TikTok Anda
username = "username_tiktok"
password = "password_tiktok"

# Login ke akun TikTok menggunakan TikTok API
api = tiktokapi.TikTokAPI(username, password)

# Masukkan informasi video dan jadwal
video_path = "path_to_video_file"
caption = "Ini adalah caption video saya"
music_id = "id_musik_yang_akan_digunakan"
publish_time = datetime.datetime(2023, 2, 25, 10, 30) # Jadwal posting video

# Hitung durasi waktu yang tersisa hingga jadwal posting video
time_diff = (publish_time - datetime.datetime.now()).total_seconds()
if time_diff > 0:
    time.sleep(time_diff)

# Unggah video ke TikTok
response = api.upload_video(video_path, caption=caption, music_id=music_id)

# Ambil ID video yang telah diunggah
video_id = response["item_id"]

# Set status video menjadi "publish"
api.set_video_upload_status(video_id, "publish")
