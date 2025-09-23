url pws : https://abelyvia-tori-streetkicks.pbp.cs.ui.ac.id/

Tugas 2
Cara saya mengimplementasikan checklist adalah pada umumnya saya mengikuti tutorial yang diberikan dengan 
mencoba memahami per stepnya, membaca ppt untuk lebih memahami MVT pada jango itu seperti apa , bertanya kepada 
GPT untuk meminta penjelasan lebih lanjut tentang langkah demi langkah yang diberikan. 

![alt text](bagan.png)

peran settings.py pada proyek ini adalah mengatur production untuk keamanan
dan debugging, mengatur nama aplikasi django yang aktif dan akan digunakan 
dalam installed_apps dan mengatur allowed host untuk meluncurkan website, 
mengatur middleware yang diproses, mengatur koneksi database yang digunakan, melakukan autentikai dan validasi terhadap password. settings.py dijadikan pusat 
konfigurasi proyek django yang mengatur seluruh fitur perilaku dalam aplikasi django


cara kerja migrasi database di django adalah 
1. membuat model aplikasi django di models.py
2. membuat file migrasi dengan menjalankan python manage.py makemigrations
3. menerapkan perubahan pada migrasi yang dibuat dengan menjalankan python manage.py migrate
dengan ini django menyimpan informasi migrasi yang sudah dijalankan dan memungkinkan django untuk selalu cek apakah migrasi sudah berhasil dijalankan
migrasi ini membantu mengelola setiap perubahan database secara struktur dan otomatis 

alasan kenapa django dijadikan permulaan pembelajaran ini adalah 
1. struktur pemrograman web yang diberikan django terstruktur dan mudah untuk dipahami
2. banyak fitur bawaan dari framework ini seperti templates, autentikasi, admin, sehingga mengurangi kebutuhan ekstra library
3. berbasis bahasa python yang paling dasar dan mudah dipahami
4. django sesuai untuk kebutuhan pemrograman web berskala besar maupun kecil

feedback kepada asisten dosen untuk tutorial 1 :
mungkin karena tutorial 1 masih bisa dibilang tidak terlalu kompleks jadi mudah dipahami dan tidak terlalu banyak kendala. namun, kemarin saya sempat mengalami 
sedikit kendala dan langsung bertanya dan dibantu oleh kakak asdos untuk menyelesaikan masalah tersebut, terima kasih banyak kak, maaf kalau selama pengerjaan tugas2 ini agak banyak nanya huhuhu. 

Tugas 4
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
= authentication form adalah kelas login yang dibuat untuk menangani proses login pengguna yang dimana dia secara otomatis memvalidasi username dan passwordnya. Kelebihannya adalah keamanan yang terjamin, mudah digunakan tinggal panggil functionnya aja, terintegrasi langsung dengan sistem autenikasi django. Kekurangannya adalah kustomisasi terbatas hanya bisa memvalidasi username dan password


2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
autentikasi adalah proses memverifikasi identitas dan data pengguna kayak usernamenuya atau passwordnya. kalau otorisasi lebih ke apa yang boleh dilakukan pengguna setelah melakukan verifikasi login. Django menyediakan autentikasi bawaan dari app yaitu django.contrib.auth yang dimana meliputi : 
a. user model - menyimpan identitas, username, password
b. password management - menyimpan password dari user dalam bentuk hash
c. django menggunakan backend untuk memverifikasi identitas user
d. session management dimana jika login, instance user dan jika belum login anonymous 
untuk otorisasi, django mengatur hak permissions dan groups yang meliputi permissions yang otomatis punya 3 model seperti add chage delete view, groups untuk mengelompokkan user tertentu, flags khusus untuk setiap role para user contoh is_admin yang akan menjadi admin 


3.  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Kelebihan session yaitu keamanan yang tinggi ,data yang sensitif disimpan di server sehingga user tidak dapat melihat atu memanipulasinya, 
kapasitas yang besar, dan pengembangan memiliki kontrol penuh atas data dan dapat menghapusnya kapan saja. Kekurangan dari session adalah beban server yang jika ada ribuan pengguna yang aktif akan memengaruhi performa server dan kompleksitas dalam mengatur session jika session habis user harus login lagi. 
Kelebihan cookies adalah tidak membebani server karena setiap data disimpan di client, persistensi untuk client, mudah dan mendukung fitur interaktif 
untuk client. Kekurangan cookies adalah ukuran yang terbatas, keamanan yang rendah, pengguna dapat menonaktifkan cookies yang dapat menganggu fungsionalitas aplikasi. 

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
terdapat beberapa risiko potensial yang harus diwaspadai yaitu 
a.  penyerang dapat memasukkan kode berbahaya kedalam laman web yang dapat mencuri cookie pengguna termasuk session ID untuk autentikasi
b. penyerang dapat memaksa peramban pengguna untuk mengirim request ke situs web tanpa sepengetahuan user dan menggunakan cookie yang ada 
c. cookie dapat dicuri saat koneksi tidak aman atau jika cookie tidak memiliki flag keamanan yang tepat
cara django menangani hal ini adalah : 
a. django menyertakan token unik disetiap formulir POST. saat formulir dikirim, django akan membandingkan token yang diterima dengan token di formulir dan jika berbeda, django otomatis akan menolak
b. cookie sesi menerima flag secara default. ini menyebabkan cookie tidak dapat diakses oleh javascript, sehingga mencegah serangan XSS yang ingin mencuri cookie
c. django dapat diatur untuk menambahkan flag secure pada cookie yang memastikan cookie hanya dikirim melalui koneksi https yang terenkripsi
d. bisa menggunakan signed cookies dimana django akan memastikan setiap data dalam cookie tidak dimanipulasi 

5. yang pertama saya lakukan adalah mengimplementasikan fungsi register logout dan login di views.py kemudian membuat file html untuk tiap fungsi, menambahkannya ke urls.py dan menambahkan sesi login sebelum main berjalan, dilanjut menghubungkan product dan user dengan menambahkan variabel user di models.py, lalu saya menambahkan detail info pengguna yang login dengan menggunakan fungsi last login di file main.html saya, setelah selesai menambahkan beberapa function saya membuat akun user dan juga menambahkan product di setiap akunnya. kurang lebihnya saya hampir keseluruhan mengikuti step di tutorial

