# TikTok Scheduler
TikTok Scheduler adalah program berbasis Python yang memungkinkan Anda untuk membuat jadwal posting video TikTok dengan caption dan musik yang telah ditentukan. Program ini menggunakan TikTok API untuk mengunggah video dan melakukan operasi pada akun TikTok Anda.

## Cara Penggunaan

1. Unduh dan pasang Python di komputer Anda.

2. Buka terminal atau command prompt dan pasang paket TikTok API dengan perintah berikut: pip install tiktokapi.

3. Salin kode program di atas ke file Python baru di editor teks.

4. Ganti nilai variabel username dan password dengan informasi login akun TikTok Anda.

5. Atur informasi video dan jadwal yang ingin Anda jadwalkan dengan mengisi nilai variabel video_path, caption, music_id, dan publish_time.

6. Jalankan program dengan perintah python nama_file.py. Pastikan Anda menjalankan program di direktori yang sama dengan file Python dan video yang akan diunggah.

7. Program akan menunggu hingga waktu yang ditetapkan dalam variabel publish_time tiba sebelum mengunggah video. Jika waktu jadwal posting telah tiba, program akan langsung mengunggah video.

## Keterangan
tiktokapi: Paket Python untuk mengakses TikTok API.

username dan password: Informasi login akun TikTok Anda. Harap perhatikan bahwa program hanya akan bekerja jika Anda memiliki akun TikTok yang valid dan terverifikasi.

video_path: Path file video yang akan diunggah ke TikTok. Pastikan file video tersedia di direktori yang sama dengan file Python.

caption: Deskripsi atau pesan yang akan ditampilkan di bawah video. Maksimal 100 karakter.

music_id: ID musik yang akan digunakan sebagai background video. Anda dapat menemukan ID musik dengan mencari di aplikasi TikTok atau melalui TikTok API Explorer.

publish_time: Waktu dan tanggal publikasi video yang dijadwalkan. Gunakan format datetime.datetime(year, month, day, hour, minute) untuk mengatur waktu publikasi.
Pastikan zona waktu pada komputer Anda sudah diatur dengan benar.

time_diff: Durasi waktu yang tersisa hingga jadwal posting video. Program akan menunggu hingga waktu jadwal posting tiba sebelum mengunggah video.

response: Respons dari TikTok API setelah video berhasil diunggah. Mengandung informasi tentang ID video yang telah diunggah.

video_id: ID video yang telah diunggah ke TikTok. Digunakan untuk melakukan operasi lebih lanjut pada video seperti penghapusan atau pengeditan.

## Catatan
- Pastikan untuk mematuhi aturan dan kebijakan TikTok saat menggunakan API mereka. Hal ini termasuk menghindari pelanggaran hak cipta atau konten yang tidak pantas dan tidak mengabaikan peringatan keamanan atau privasi.

- Program ini hanya akan berhasil jika Anda memiliki akses ke akun TikTok yang valid dan terverifikasi. Jangan membagikan informasi login akun Anda dengan orang lain atau memperbolehkan aplikasi pihak ketiga untuk mengakses akun TikTok
