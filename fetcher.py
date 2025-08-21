import requests
import os

# URL dari playlist yang ingin diambil
url = "https://lime-ibex-566528.hostingersite.com/sc/V+/event.php"

# Header User-Agent untuk menyamar sebagai browser biasa
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Nama file untuk menyimpan hasil
output_filename = "playlist.m3u"

try:
    # Melakukan permintaan GET ke URL dengan header yang sudah ditentukan
    response = requests.get(url, headers=headers, timeout=15)
    
    # Memeriksa apakah permintaan berhasil (status code 200)
    response.raise_for_status()

    # Menyimpan konten respons ke dalam file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    print(f"Playlist berhasil diunduh dan disimpan sebagai '{output_filename}'")
    
    # Menampilkan beberapa baris pertama dari konten yang diunduh
    print("\n--- Awal Konten Playlist (10 baris pertama) ---")
    lines = response.text.splitlines()
    for i, line in enumerate(lines[:10]):
        print(f"{i+1}: {line}")
    print("--------------------------------------------")

except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat mencoba mengambil URL: {e}")
