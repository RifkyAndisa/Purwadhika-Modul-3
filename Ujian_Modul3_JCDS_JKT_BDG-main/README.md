![purwadhika logo](https://static.wixstatic.com/media/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png/v1/fill/w_246,h_39,al_c,usm_0.66_1.00_0.01/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png)

Selamat datang di Ujian Modul 3, JCDS Bandung dan Jakarta.
Pada ujian kali ini, Anda akan mengerjakan soal untuk kasus:
- __Classification__: Hunting Basketball Player

Selamat mengerjakan!

### Case: Hunting Basketball Player (POIN: 100)
![nba](https://images.unsplash.com/photo-1499754162586-08f451261482?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max)
Anda adalah seorang Data Scientist di tim basket International yang berencana untuk merekrut beberapa pemain basket berbakat untuk meningkatkan performa tim. Tim Anda sering sekali menjadi tim juru kunci  dalam klasemen yang mengakibatkan sponsor dari perusahaan swasta dan profit penjualan merchandise pun semakin berkurang. Di sisi lain, tim Anda sudah terlalu lama menghamburkan uang untuk menggaji pemain-pemain yang kurang memiliki bakat. Sehingga para _stake holders_ merasa perlu adanya perombakan pemain, dengan harapan tim Anda lebih sering menang dan profit dari segala sektor pun meningkat.

Baru-baru ini manager tim mengatakan ingin mengganti 10 pemain. Dan berharap Anda, sebagai Data Scientist, untuk dapat menemukan pemain baru yang berbakat dengan cepat.

Data pilihan pemain bisa Anda download di repository ini dengan nama file: [__new_players.csv__](https://github.com/ridhoaryo/Ujian_Modul3_JCDS_JKT_BDG/blob/master/new_players.csv). Dalam dataset ini tidak terdapat nama pemain. Maka Anda akan memilih mereka berdasarkan data-data historical mereka.

Untuk memudahkan proses recruitment, Anda akan menggunakan dataset [__nba_players.csv__](https://github.com/ridhoaryo/Ujian_Modul3_JCDS_JKT_BDG/blob/master/nba_players.csv) sebagai dasar untuk membangun model machine learning untuk menentukan pemain-pemain baru yang pantas Anda rekrut. Kolom `potential_player` pada dataset NBA adalah acuan Anda. 0 berarti pemain tersebut tidak memiliki potensi dan cenderung untuk tidak direkrut. Dan sebaliknya.

__Requirements:__

Buatlah sebuah file __Jupyter Notebook (.ipynb)__, bernama "[Nama_Anda]_basketball_team_recruitment.ipynb". Download & gunakan dataset NBA di repository ini dengan nama file: [__nba_players.csv__](https://github.com/ridhoaryo/Ujian_Modul3_JCDS_JKT_BDG/blob/master/nba_players.csv). Dan penjelasan tiap kolom dapat dilihat [di sini](https://www.kaggle.com/justinas/nba-players-data)

1. __(POIN: 15)__ Lakukan _data preprocessing_, seperti menghapus kolom yang sekiranya tidak dibutuhkan, strategi apa yang akan digunakan untuk mengisi _missing value_, metode apa yang akan digunakan untuk melakukan encoding, feature apa yang bisa ditambahkan, dan lain-lain. Serta berikan penjelasan di setiap langkah yang Anda jalankan. 

2. __(POIN: 20)__ Buatlah minimal __5 (lima)__ macam data visualisasi yang dapat menampilkan insight dari para pemain NBA baik yang di-cap sebagai potential player maupun yang bukan. Ceritakan juga insight yang Anda temukan.

3. __(POIN: 10)__ Buatlah training_validation dataset dan testing dataset. Silahkan Anda atur test_size / train_size maupun random_state sesuai dengan keinginan Anda.

4. __(POIN: 20)__ Buatlah __2 (dua) benchmark machine learning model__ untuk klasifikasi (pilihan model bebas). Lakukan `cross_val_score` untuk mengetahui model benchmark mana yang berpotensi. Pada poin ini, tentukan juga scoring yang menjadi fokus Anda (pilih salah satu):
    
    - Recall, atau
    - Precision

    Kata kuncinya adalah, tim Anda sedang dilanda krisis ekonomi. Sehingga, dengan kata lain, Anda harus benar-benar selektif siapa yang akan Anda rekrut.

5. __(POIN: 25)__ Pada step ini tingkatkan performa pada tiap model, sehingga dapat memenuhi fokus evaluasi yang sudah Anda tentukan pada step sebelumnnya. Sebagai pengingat, beberapa cara untuk meningkatkan performa seperti **dan tidak terbatas pada**: 
    - feature selection (SelectPercentile, SelectKBest, RFE)
    - preprocessing (Polynomial, Scaling)
    - feature extraction (PCA)
    - hyperparameter tuning (Grid / Random)
    - resampling (ROS, RUS, Smote)
    - dll

6. __(POIN: 10)__ Gunakan model terbaik yang diperoleh, untuk mengklasifikasi pemain pada dataset __new_players__ , manakah pemain yang patut direkrut atau tidak. Tampilkan hasilnya dalam sebuah __dataframe__.

__Catatan:__ Kirim source code jawaban Anda dalam 1 (satu) file .ipynb. Kemudian kirimkan via email ke ridhoaryo1991@gmail.com dan email operational masing-masing.

