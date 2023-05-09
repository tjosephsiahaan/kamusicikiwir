meme_dict = {
            "CRINGE": "Sesuatu yang memalukan, menjijikan, dan kurang lucu",
            "LOL": "tanggapan singkat soal sesuatu yang kocak",
            "STROLLED": "rickroll dalam versi lain",
            "NEGRO": "bahasa spanyol dari kata hitam",
            "KUNIMA": "nama lain dari manusia merah",
            "COEG": "Bahasa yang sedikit lebih kasar dari kata cuy",
            "ICIKIWIR" : "Ucapan ketika seseorang sedang berdendang",
            "YANTO" : "kalian pasti ketik ini karena penasaran ini nama bapak siapa kan?",
            "TETAP BERSAMA" : "Salah satu voice command dari game Free Fire",
            
            }
            

word = input("Ketik kata yang ingin kamu ketahui(WARNING: harus menggunakan huruf kapital):")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("sorry, the word that you're trying to find isn't available")
