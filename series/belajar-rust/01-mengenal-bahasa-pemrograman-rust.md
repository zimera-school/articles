# Tentang Bab Ini

Bagian ini membahas tentang gambaran umum dari bahasa pemrograman serta peranti pengembangan Rust. Dengan mempelajari bab ini, pembaca diharapkan bisa memahami gambaran umum dari Rust sehingga bisa memberikan semacam pemahaman terhadap ruang lingkup masalah-masalah pemrograman yang bisa diselesaikan menggunakan Rust serta posisi Rust di antara berbagai bahasa pemrograman dan peranti pengembangan lainnya.

## Apakah Rust Itu?

Secara umum, biasanya para pemrograman akan menyebut *Rust* untuk segala macam peranti pengembangan yang terkait dengan Rust. Pada dasarnya, saat membicarakan tentang peranti pengembangan, ada beberapa komponen sebagai berikut:

1. Spesifikasi bahasa pemrograman
2. Implementasi bahasa pemrograman dalam bentuk _compiler_ / _interpreter_
3. _Package Manager_ yang digunakan untuk mengelola pustaka / paket yang diperlukan saat dilakukan proses kompilasi maupun untuk instalasi berbagai peranti pendukung yang dibutuhkan pemrogram saat membangun aplikasi.
4. _Build Tool_ yang digunakan untuk mengelola proses kompilasi serta hasil akhirnya.

Hal tersebut juga berlaku untuk *Rust*. Meskipun seringkali hanya disebut *Rust*, biasanya sudah mengacu ke setidaknya spesifikasi bahasa pemrograman Rust serta _compiler_ dari Rust. Pada pembahasan ini, penyebutan *Rust* akan mengacu pada spesifikasi bahasa pemrograman serta peranti standar untuk *compiler* maupun pustaka standar yang disertakan pada saat instalasi Rust. Informasi tentang Rust bisa diperoleh di [Web bahasa pemrograman Rust](https://www.rust-lang.org/)

## Sejarah Singkat Rust

1. Rust pertama kali dibuat oleh salah seorang pegawai dari Mozilla yang bernama _Graydon Hoare_ sekitar tahun 2006. Saat itu, Graydon membuat bahasa pemrograman baru dan _compiler_ dari bahasa pemrograman tersebut menggunakan [OCaml](https://ocaml.org). 
2. Mozilla mulai men-sponsori dan mendukung Rust untuk keperluan internal pada tahun 2009 (diumumkan tahun 2010).
3. Tahun 2010, pengembangan Rust menggunakan OCaml dihentikan, digantikan dengan _self-hosting compiler_ (Rust dibuat dengan menggunakan Rust). Tahun 2011, Rust berhasil digunakan untuk mengkompilasi dirinya sendiri. Saat itu, Rust menggunakan _LLVM_ sbagai _compiler backend_.
4. Versi stabil pertama (versi 1.0.0) dari Rust berhasil dirilis pada tanggal 15 Mei 2015.
5. Setelah itu, Rust menetapkan pola rilis pasti setiap 6 minggu, artinya setiap 6 minggu ada rilis baru untuk versi stabil, beta, dan _nightly_.

## Paradigma Pemrograman Rust

Paradigma pemrograman merupakan cara pandang untuk menyelesaikan permasalahan pemrograman. Rust tidak mempunyai suatu paradigma pemrograman spesifik tertentu, tetapi lebih ke arah _multi-paradigm_ atau mempunyai lebih dari satu paradigma. Secara umum, paradigma pemrograman Rust adalah:

1. Konkuren: mendukung pemrograman secara konkuren, artinya lebih dari satu unit komputasi bisa dieksekusi secara "bersamaan" (secara _overlap_, bergantian - tidak harus menunggu satu unit komputasi selesai baru kemudian satu unit komputasi berikutnya dieksekusi.
2. Fungsional: program dikonstruksi dengan menggunakan melakukan komposisi _function_.
3. Generik: tipe pada fungsi bisa dispesifikasikan belakangan, bukan pada saat pembuatan fungsi.
4. Imperatif: program terdiri atas berbagai _statement_ yang mengubah _state_ dari program (misal dengan memanipulasi variabel, dan lain-lain).
5. Terstruktur: program menekankan pada penggunakan berbagai struktur kendali serta subprogram, terutama digunakan untuk _readibility_.
6. PBO (Pemrograman Berorientasi Obyek): meski Rust tidak murni bahasa PBO, tetapi Rust mendukung berbagai fitur PBO yang memungkinkan pemrogram untuk mengkonstruksi program dengan pendekatan obyek yang mempunyai karakteristik serta perilaku tertentu dan adanya interaksi antar obyek tersebut dalam menyelesaikan masalah pemrograman.

## Lisensi Rust

Semua artifak dari Rust (_compiler_, logo, situs Web, dan lain-lain) mempunyai lisensi ganda:

1. _MIT License_
2. _Apache License_ - Versi 2.0

## Software yang Dibangun Menggunakan Rust

Rust digunakan untuk membangun berbagai software, mulai dari _low level_ sampai dengan _high level_. Istilah _low level_ dan _high level_ ini digunakan untuk menunjukkan kedekatan dengan akses mesin. _Low level_ dikenal juga dengan istilah _system programming_ (meski istilah ini bukan merupakan istilah yang kanonikal). Rust merupakan satu di antara sedikit bahasa pemrograman dan peranti pengembangan yang bisa digunakan utk semua level. Bagian ini menunjukkan beberapa software yang dibangun dengan menggunakan Rust.

1. [Servo](https://servo.org/): _engine_ penjelajah Web (_Web browser_) yang digunakan dalam browser *Mozilla Firefox* melalui proyek *Quantum*.
2. [Redox](https://www.redox-os.org/): sistem operasi baru dengan teknologi _microkernel_ dengan _userland_ mirip Unix.
3. [Nushell](https://www.nushell.sh/): shell.
4. [TiKV](https://tikv.org/): basis data _key-value_ transaksional yang terdistribusi.
5. [Deno](https://deno.land/): _runtime_ untuk JavaScript dan TypeScript.
6. [Discord](https://discord.com/): salah satu peranti pengembangan yang digunakan untuk mengembangkan sistem Discord.

## Domain Masalah dari Rust

Rust bisa digunakan untuk menyelesaikan berbagai masalah pada berbagai domain. Secara umum, Rust bisa digunakan untuk pembuatan software di aras rendah (*system programming*) maupun di berbagai masalah pemrograman aras atas. Beberapa domain masalah yang bisa diselesaikan oleh Rust antara lain:

1. System Programming
2. Akses ke peranti keras (*interfacing*)
3. CLI (*Command Line Interface*)
4. Backend
5. Aplikasi Web
6. Akses ke berbagai basis data
7. GUI (*Graphical User Interface*)
8. Cloud

