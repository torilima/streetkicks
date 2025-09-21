url pws : https://abelyvia-tori-streetkicks.pbp.cs.ui.ac.id/

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