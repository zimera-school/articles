# Tentang Bab Ini

Untuk menggunakan Rust, tentu saja anda harus melakukan instalasi terhadap Rust dan ekosistem yang bisa digunakan untuk mendukung proses membangun software menggunakan Rust. Bagian ini membahas tentang berbagai cara yang bisa digunakan untuk mulai menggunakan Rust. Selain itu, di bab ini juga akan dibahas tentang berbagai peranti pengembangan yang lazim digunakan sebagai hasil dari instalasi serta pengenalan penggunaannya.

## Rilis Rust

Rust mempunyai 3 kategori rilis:

1. **Stable**: rilis stabil, dengan *test* yang dilakukan secara menyeluruh.
2. **Beta**: rilis versi ini merupakan rilis yang disiapkan untuk menjadi versi stabil berikutnya.
3. **Nightly**: rilis versi ini merupakan rilis yang berisi berbagai eksperimen yang mungkin bisa masuk ke versi stabil berikutnya (setelah melalui versi **Beta**). Meskipun demikian, bisa juga eksperimen-eksperimen tersebut tidak akan pernah dimasukkan ke rilis resmi Rust.

Saat membangun aplikasi, pemrogram bebas untuk menggunakan kategori rilis manapun. Meskipun demikian, dianjurkan untuk menggunakan versi **Stable** karena fitur yang ada di dalamnya adalah fitur-fitur yang sudah stabil sehingga memudahkan pemrogram untuk me-*maintain* aplikasi yang dikembangkan.

Untuk semua rilis tersebut, Rust menggunakan pedoman yang disebut dengan [Semantic Versioning](https://semver.org/). Dengan menggunakan pedoman ini, setiap penomoran rilis Rust terdiri atas 3 bagian:

1. **MAJOR**: rilis dengan perubahan API (*Application Programming Intergace*) yang tidak kompatibel dengan versi MAJOR sebelumnya.
2. **MINOR**: rilis dengan penambahan fungsionalitas yang kompatibel dengan versi sebelumnya.
3. **PATCH**: rilis dengan perbaikan terhadap *bugs* yang kompatibel dengan versi *MAJOR* dan *MINOR*.

Sebagai contoh, versi `1.54.0` dari versi Rust berisi Rust dengan semua API yang kompatibel dengan versi 1.x.x sebelumnya. Angka `54` berarti penambahan fungsionalitas yang bersifat kompatibel dengan versi penambahan fungsionalitas sebelumnya. Angka `0` berarti sama sekali belum ada perubahan perbaikan *bug* (jika ada) untuk versi 1.54 tersebut.

## Siklus Rilis Rust

Versi dari Rust (*stable, beta, nightly*) dirilis setiap 6 minggu sekali (1.5 bulan sekali). Jadi, setiap 6 minggu akan muncul versi *stable, beta*, serta *nightly*). Kepastian siklus rilis ini menarik dan memberi kepastian kepada para pemrogram dalam mengantisipasi versi yang akan digunakan.

## Edisi Rust

Selain versi Rust berdasarkan *semantic versioning* seperti yang telah dijelaskan di atas, Rust juga mengenal istilah *Rust Edition* / Edisi Rust. Edisi Rust menggunakan tahun dan digunakan untuk memecahkan masalah *backward compatibility* antara berbagai versi semantik.

Saat versi stabil pertama Rust dirilis (1.x.x), Rust mempunyai janji *backward compatibility*, artinya kode sumber yang dibuat untuk versi 1.x.x awal dulu, sampai versi 1.x.x terakhir tetap bisa dikompilasi dan dijalankan menggunakan Rust versi 1.x.x terakhir. Jadi, selama masih berada di versi *MAJOR* yang sama, maka hal tersebut kompatibel. Problem dari hal ini adalah jika ingin merilis versi semantik Rust 1.x.x yang memungkinkan terjadinya *breaking changes* (perubahan yang "merusak" - membuat tidak bisa dikompilasi). Sebagai contoh, Rust versi 1.x.x terakhir memperkenalkan kata kunci yang belum ada di versi awal-awal dulu. Jika dikompilasi dengan versi semantik Rust terakhir, maka akan terjadi error. Untuk itu, maka dibuat versi edisi Rust. Setiap edisi Rust akan menjamin *backward compatibility* **terkecuali** jika pemrogram dengan sadar telah melakukan berbagai perubahan yang diperlukan dan memilih edisi Rust versi berikutnya. Jika tidak mau dan ingin tetap bisa dikompilasi, maka pemrogram tetap bisa memilih untuk berada pada edisi Rust yang sebelumnya.

Sampai saat ini, ada beberapa edisi Rust:

1. [Rust 2015](https://doc.rust-lang.org/edition-guide/rust-2015/index.html): fokus pada kestabilan.
2. [Rust 2018](https://doc.rust-lang.org/edition-guide/rust-2018/index.html): fokus pada produktivitas.
3. [Rust 2021](https://doc.rust-lang.org/edition-guide/rust-2021/index.html): belum dirilis sampai saat ini. 

Saat membuat suatu proyek kode sumber baru, secara default akan digunakan versi edisi Rust yang aktif saat ini.

## Rust Playground

Jika kebutuhan kita hanya untuk mencoba beberapa bagian kode sumber, maka kita cukup hanya menggunakan [Rust Playground](https://play.rust-lang.org/) saja. Setelah mengakses URL tersebut, kita bisa menuliskan kode sumber dan menjalankan kode sumber tersebut tanpa perlu melakukan instalasi peranti pengembangan Rust.

![Rust Playground](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3q6gbfywftba020mrtey.png)

## Instalasi Rust

Instalasi Rust bisa dilakukan dengan berbagai macam cara, tetapi cara yang paling mudah dan dianjurkan adalah dengan menggunakan [rustup](https://rustup.rs/). Prasyarat software yang diperlukan adalah [curl](https://curl.se/) yang biasanya sudah terinstall di sistem Linux.

```bash
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
info: downloading installer

Welcome to Rust!

This will download and install the official compiler for the Rust
programming language, and its package manager, Cargo.

Rustup metadata and toolchains will be installed into the Rustup
home directory, located at:

  /home/zaky/.rustup

This can be modified with the RUSTUP_HOME environment variable.

The Cargo home directory located at:

  /home/zaky/.cargo

This can be modified with the CARGO_HOME environment variable.

The cargo, rustc, rustup and other commands will be added to
Cargo's bin directory, located at:

  /home/zaky/.cargo/bin

This path will then be added to your PATH environment variable by
modifying the profile files located at:

  /home/zaky/.profile
  /home/zaky/.bashrc

You can uninstall at any time with rustup self uninstall and
these changes will be reverted.

Current installation options:


   default host triple: x86_64-unknown-linux-gnu
     default toolchain: stable (default)
               profile: default
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
>1

info: profile set to 'default'
info: default host triple is x86_64-unknown-linux-gnu
info: syncing channel updates for 'stable-x86_64-unknown-linux-gnu'
info: latest update on 2021-07-29, rust version 1.54.0 (a178d0322 2021-07-26)
info: downloading component 'cargo'
  6.0 MiB /   6.0 MiB (100 %)   1.2 MiB/s in  5s ETA:  0s
info: downloading component 'clippy'
  2.4 MiB /   2.4 MiB (100 %)   1.2 MiB/s in  2s ETA:  0s
info: downloading component 'rust-docs'
 16.7 MiB /  16.7 MiB (100 %)   1.2 MiB/s in 14s ETA:  0s
info: downloading component 'rust-std'
 21.9 MiB /  21.9 MiB (100 %)   1.2 MiB/s in 19s ETA:  0s
info: downloading component 'rustc'
 50.1 MiB /  50.1 MiB (100 %)   1.2 MiB/s in 44s ETA:  0s 
info: downloading component 'rustfmt'
  3.7 MiB /   3.7 MiB (100 %)   1.2 MiB/s in  3s ETA:  0s
info: installing component 'cargo'
info: installing component 'clippy'
info: installing component 'rust-docs'
 16.7 MiB /  16.7 MiB (100 %)   9.1 MiB/s in  1s ETA:  0s
info: installing component 'rust-std'
 21.9 MiB /  21.9 MiB (100 %)  12.5 MiB/s in  2s ETA:  0s
info: installing component 'rustc'
 50.1 MiB /  50.1 MiB (100 %)  13.7 MiB/s in  4s ETA:  0s
info: installing component 'rustfmt'
info: default toolchain set to 'stable-x86_64-unknown-linux-gnu'

  stable-x86_64-unknown-linux-gnu installed - rustc 1.54.0 (a178d0322 2021-07-26)


Rust is installed now. Great!

To get started you may need to restart your current shell.
This would reload your PATH environment variable to include
Cargo's bin directory ($HOME/.cargo/bin).

To configure your current shell, run:
source $HOME/.cargo/env
$
```

Setelah proses instalasi tersebut, ada file berisi variabel lingkungan (*environment variables*) yang harus diaktifkan, yaitu *$HOME/.cargo/env*. Berikut adalah kondisi sebelum diaktifkan dan setelah diaktifkan menggunakan perintah *source*:

```bash
$ rustc
-bash: rustc: perintah tidak ditemukan
$ cargo
-bash: cargo: perintah tidak ditemukan
$ source .cargo/env
$ rustc --version
rustc 1.54.0 (a178d0322 2021-07-26)
$ cargo --version
cargo 1.54.0 (5ae8d74b3 2021-06-22)
$
```

Secara default, isi dari file *.cargo/env* sudah diletakkan pada file *.profile* sehingga akan aktif setiap login. Setelah instalasi, silahkan logout dari shell dan kemudian mengaktifkan shell kembali supaya *.profile* dieksekusi oleh shell. Periksa hasil instalasi berikut ini:

```bash
$ rustc --version
rustc 1.54.0 (a178d0322 2021-07-26)
$ cargo --version
cargo 1.54.0 (5ae8d74b3 2021-06-22)
$ rustfmt --version
rustfmt 1.4.37-stable (a178d03 2021-07-26)
$
```

Untuk mencoba kompilator / *compiler* Rust, buat file `hello.rs` di lokasi direktori bebas:

```rust
fn main() {

    println!("Hello World!");

}
```

Untuk mengkompilasi dan menjalankan hasil:

```bash
$ rustc hello.rs 
$ ls -la
total 3216
drwxr-xr-x 2 zaky zaky    4096 Sep  4 11:58 ./
drwxr-xr-x 6 zaky zaky    4096 Sep  4 11:57 ../
-rwxr-xr-x 1 zaky zaky 3280808 Sep  4 11:58 hello*
-rw-r--r-- 1 zaky zaky      46 Sep  4 11:58 hello.rs
$ ./hello 
Hello World!
$
```

> **Catatan**: `rustc` adalah kompilator Rust, sedangkan `hello.rs` adalah file kode sumber yang akan dikompilasi menjadi *native machine code* (lihat hasil file `hello`) di atas.

Proses kompilasi tersebut merupakan proses kompilasi yang digunakan secara sederhana, cukup untuk 1 file kode sumber saja. Jika software mulai kompleks dan memerlukan banyak kode sumber serta mempunyai ketergantungan / *dependecy* ke berbagai pustaka, maka diperlukan `cargo`.

## *Uninstall* Rust

Untuk menghapus instalasi Rust, gunakan `rustup` yang sudah terinstall saat melakukan instalasi Rust. Berikut ini adalah cara menghapus instalasi Rust:

```bash
$ rustup self uninstall


Thanks for hacking in Rust!

This will uninstall all Rust toolchains and data, and remove
$HOME/.cargo/bin from your PATH environment variable.

Continue? (y/N) y

info: removing rustup home
info: removing cargo home
info: removing rustup binaries
info: rustup is uninstalled
$
```

## Memperbarui Rust

Jika muncul versi terbaru dari Rust, maka kita bisa memperbarui Rust hanya dengan menggunakan `rust update` berikut ini:

```bash
$ rustup update
info: syncing channel updates for 'stable-x86_64-unknown-linux-gnu'
679.5 KiB / 679.5 KiB (100 %) 623.0 KiB/s in  1s ETA:  0s
info: latest update on 2021-09-09, rust version 1.55.0 (c8dfcfe04 2021-09-06)
info: downloading component 'cargo'
  6.1 MiB /   6.1 MiB (100 %) 981.4 KiB/s in  6s ETA:  0s
info: downloading component 'clippy'
  2.4 MiB /   2.4 MiB (100 %)   1.1 MiB/s in  2s ETA:  0s
info: downloading component 'rust-docs'
 17.0 MiB /  17.0 MiB (100 %)   1.2 MiB/s in 15s ETA:  0s
info: downloading component 'rust-std'
 22.3 MiB /  22.3 MiB (100 %) 780.8 KiB/s in 23s ETA:  0s 
info: downloading component 'rustc'
 51.0 MiB /  51.0 MiB (100 %)   1.1 MiB/s in 52s ETA:  0s 
info: downloading component 'rustfmt'
  3.7 MiB /   3.7 MiB (100 %) 943.6 KiB/s in  4s ETA:  0s
info: removing previous version of component 'cargo'
info: removing previous version of component 'clippy'
info: removing previous version of component 'rust-docs'
info: removing previous version of component 'rust-std'
info: removing previous version of component 'rustc'
info: removing previous version of component 'rustfmt'
info: installing component 'cargo'
info: installing component 'clippy'
info: installing component 'rust-docs'
 17.0 MiB /  17.0 MiB (100 %)   7.7 MiB/s in  2s ETA:  0s
info: installing component 'rust-std'
 22.3 MiB /  22.3 MiB (100 %)  12.3 MiB/s in  2s ETA:  0s
info: installing component 'rustc'
 51.0 MiB /  51.0 MiB (100 %)  10.2 MiB/s in  6s ETA:  0s
info: installing component 'rustfmt'
info: checking for self-updates

  stable-x86_64-unknown-linux-gnu updated - rustc 1.55.0 (c8dfcfe04 2021-09-06) (from rustc 1.54.0 (a178d0322 2021-07-26))

info: cleaning up downloads & tmp directories
$
``` 

## Plugin untuk *subcommand* `Cargo`

`Cargo` memungkinkan untuk diperluas fungsionalitasnya dengan menggunakan *plugin*. Dengan menggunakan *plugin*, Cargo akan mendapatkan *subcommand*. Sebagai contoh, pada bagian ini akan dijelaskan tentang salah satu *plugin* yang bermanfaat untuk mendeteksi paket yang perlu diperbarui di skala user (bukan per proyek). *Plugin* tersebut adalah *plugin* [cargo-update](https://github.com/nabijaczleweli/cargo-update). 

### Instalasi *Plugin*

Instalasi dilakukan dengan menggunakan `cargo install`:

```bash
$ cargo install cargo-update
    Updating crates.io index
  Downloaded cargo-update v7.0.1
  Downloaded 1 crate (44.4 KB) in 1.45s
  Installing cargo-update v7.0.1
  Downloaded dirs-sys v0.3.6
...
...
...
   Compiling semver v0.9.0
   Compiling cargo-update v7.0.1
   Compiling url v2.2.2
   Compiling git2 v0.11.0
    Finished release [optimized] target(s) in 1m 24s
  Installing /home/zaky/.cargo/bin/cargo-install-update
  Installing /home/zaky/.cargo/bin/cargo-install-update-config
   Installed package `cargo-update v7.0.1` (executables `cargo-install-update`, `cargo-install-update-config`)
$
```

Untuk memeriksa pembaruan:

```bash
$ cargo install-update -a
    Updating registry 'https://github.com/rust-lang/crates.io-index'

Package       Installed  Latest  Needs update
cargo-update  v7.0.1     v7.0.1  No

No packages need updating.
Overall updated 0 packages.
```
 
## Memahami Ekosistem Rust

Mempelajari suatu bahasa pemrograman tidak hanya cukup dengan mempelajari sintaksis saja. Setiap bahasa pemrograman biasa mempunyai spesifikasi, *kompilator/interpreter*, pengelola paket pustaka, IDE, komunitas, dan lain-lain. Pemahaman mengenai ekosistem saat mempelajari suatu bahasa pemrograman menjadi hal yang sangat penting. Biasanya pemrogram mudah mempelajari sintaksis tetapi cukup perlu waktu lama untuk memahami ekosistem. Ekosistem ini juga menentukan bagaimana seorang pemrogram bisa produktif serta menggunakan idiom-idiom yang sesuai dengan bahasa pemrograman yang ditekuni. Pada bagian ini, kita akan mempelajari ekosistem dari bahasa pemrograman Rust.

### Pustaka Rust

Pustaka / *library* Rust sering disebut dengan istilah *crate*. *Crate* dari komunitas dipusatkan di https://crates.io/. Pengelolaan pustaka dalam suatu proyek software yang dikembangkan menggunakan Rust dilakukan oleh [cargo](https://doc.rust-lang.org/cargo/).
 
### Pengenalan Cargo

`cargo` adalah bagian dari peranti pengembangan Rust yang digunakan untuk mengelola paket-paket pustaka yang digunakan dalam suatu proyek. Selain itu, `cargo` juga bisa digunakan untuk keperluan menangani berbagai proses yang diperlukan oleh proyek, misalnya membangun (*build*), *test*, menjalankan *run*, dan masih banyak lagi. Selain fasilitas resmi, `cargo` juga menyediakan *plugins* untuk menambahkan kemampuan dari `cargo`. Daftar *plugins* bisa diperoleh dengan mengakses https://crates.io/search?q=cargo.

#### Inisialisasi Proyek

Untuk menginisialisasi proyek ada dua cara:

1. menggunakan `cargo init`: untuk membuat proyek pada direktori aktif.
2. menggunakan `cargo new`: untuk membuat proyek sekaligus membuat, menyiapkan, dan mengisi direktori proyek.

_Menggunakan `cargo init`_

```bash
$ mkdir hello-cargo
$ cd hello-cargo/
$ cargo init
     Created binary (application) package
$ ls -la 
total 24
drwxr-xr-x 4 zaky zaky 4096 Sep  4 12:12 .
drwxr-xr-x 3 zaky zaky 4096 Sep  4 12:12 ..
-rw-r--r-- 1 zaky zaky  180 Sep  4 12:12 Cargo.toml
drwxr-xr-x 6 zaky zaky 4096 Sep  4 12:12 .git
-rw-r--r-- 1 zaky zaky    8 Sep  4 12:12 .gitignore
drwxr-xr-x 2 zaky zaky 4096 Sep  4 12:12 src
$ tree .
.
├── Cargo.toml
└── src
    └── main.rs

1 directory, 2 files
$
```

_Menggunakan `cargo new`_

```bash
$ cargo new hello-cargo-2 --bin
     Created binary (application) `hello-cargo-2` package
$ cd hello-cargo-2/
$ ls -la
total 24
drwxr-xr-x 4 zaky zaky 4096 Sep  4 12:15 .
drwxr-xr-x 4 zaky zaky 4096 Sep  4 12:15 ..
-rw-r--r-- 1 zaky zaky  182 Sep  4 12:15 Cargo.toml
drwxr-xr-x 6 zaky zaky 4096 Sep  4 12:15 .git
-rw-r--r-- 1 zaky zaky    8 Sep  4 12:15 .gitignore
drwxr-xr-x 2 zaky zaky 4096 Sep  4 12:15 src
$ tree .
.
├── Cargo.toml
└── src
    └── main.rs

1 directory, 2 files
$
```

> **Catatan**: secara default, jika tidak menggunakan parameter, maka rerangka proyek yang dihasilkan adalah rerangka proyek untuk hasil file *binary executable* atau aplikasi yang bisa dijalankan secara langsung oleh sistem operasi. Jika ingin membuat proyek pustaka / *library*, gunakan argument `--lib` sebagai berikut: `cargo init --lib` atau `cargo new project_name --lib`.


Secara umum, hasil dari kedua perintah tersebut sama saja.

### Struktur Direktori dan Aplikasi Proyek Rust

Suatu proyek Rust yang dihasilkan oleh `cargo init` maupun `cargo new` untuk tipe aplikasi maupun pustaka mempunyai struktur yang sama, hanya berbeda di kode sumber `src`:

_Tipe Aplikasi_

```bash
tree .
.
├── Cargo.toml
└── src
    └── main.rs

1 directory, 2 files
$
```

_Tipe Pustaka_

```bash
tree .
.
├── Cargo.toml
└── src
    └── lib.rs

1 directory, 2 files
$
```

Setiap proyek juga mempunyai dua direktori dan file yang tersembunyi (*hidden*) yang diperlukan oleh [Git](https://git-scm.com) yaitu direktori `.git` dan file `.gitigore`. Direktori `.git` merupakan direktori internal dari setiap repo **Git** dan file `.gitignore` merupakan file yang digunakan untuk memberitahu direktori serta file apa di repo tersebut yang tidak perlu dimasukkan ke repo Git di [GitHub](https://github.com) atau [GitLab](https://gitlab.com). Kedua direktori dan file tersebut muncul karena asumsi bahwa proyek tersebut akan dimasukkan ke suatu repo Git tertentu. 

Berikut adalah penjelasan dari struktur direktori serta berbagai file yang ada pada suatu proyek Rust.

1. `Cargo.toml`: file ini disebut file **manifest** dan digunakan untuk mendeskripsikan metadata tentang proyek serta berbagai pustaka yang digunakan di proyek tersebut. File ini dikelola oleh pemrogram.
2. `Cargo.lock`: file yang digunakan secara internal oleh `cargo` untuk mengelola seluruh pustaka yang digunakan di proyek tersebut. File ini tidak dimaksudkan untuk dikelola oleh pemrogram. File ini akan muncul jika pemrogram sudah melakukan proses membangun aplikasi (*build*).
3. `src`: tempat pemrogram menempatkan kode sumber. Jika aplikasi, maka akan bernama `main.rs` yang akan menjadi titik awal eksekusi program.
3. `target`: direktori hasil proses kompilasi, akan muncul jika sudah dilakukan proses kompilasi / membangun / *build*. 

> **Catatan**: jika proyek merupakan proyek untuk pustaka selain pustaka sistem (yang menggunakan tipe *crate* `staticlib` atau `cdylib`), masukkan *Cargo.lock* ke baris di `.gitignore`. Selain itu, jangan masukkan. 

Suatu file Cargo.toml biasanya berisi minimal:

```bash
[package]
name = "hello-cargo-2"
version = "0.1.0"
edition = "2018"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

File `Cargo.toml` mempunyai format [TOML](https://github.com/toml-lang/toml) dan secara minimal berisi deskripsi:

1. `package`: menjelaskan tentang paket proyek tersebut, minimal berisi `name` (nama proyek), `version` (versi proyek), dan `edition` (edisi Rust yang digunakaan).
2. `dependencies`: berbagai pustaka yang digunakan di aplikasi serta versinya.

#### Membangun Proyek

Untuk membangun proyek, `cargo` harus dikerjakan pada direktori tempat proyek tersebut berada. Ada 2 kategori proyek yang dibangun:

1. Versi **debug** / **dev**
2. Versi **release**

Versi **debug** menyertakan data untuk proses *debugging* sehingga ukurannya lebih besar. Saat pengembangan, biasanya proses membangun proyek dilakukan secara default menggunakan versi *debug*. Jika proyek sudah selesai, maka dibangun menggunakan versi *release*. Berikut adalah proses serta hasil dari masing-masing versi.

_Versi *Debug*_

```bash
$ cargo build
   Compiling hello-cargo-2 v0.1.0 (/home/zaky/kerjaan/src/rust/hello-cargo-2)
    Finished dev [unoptimized + debuginfo] target(s) in 8.53s
$ tree 
Cargo.lock  Cargo.toml  .git/       .gitignore  src/        target/     
$ tree target/
target/
├── CACHEDIR.TAG
└── debug
    ├── build
    ├── deps
    │   ├── hello_cargo_2-61ab1226333d611e
    │   └── hello_cargo_2-61ab1226333d611e.d
    ├── examples
    ├── hello-cargo-2
    ├── hello-cargo-2.d
    └── incremental
        └── hello_cargo_2-1tf9vp8hw5tph
            ├── s-g21ocip69e-1gz7gsu-2d3iv3pzmnper
            │   ├── 14ljyy7cs4njs43i.o
            │   ├── 1jvulq62qig4vscu.o
            │   ├── 28iowghk4bcm6y1h.o
            │   ├── 3okkrcxho0rd7dc2.o
            │   ├── 46r7u1vfzs5zeczg.o
            │   ├── 50jgk6qv50atsv1.o
            │   ├── dep-graph.bin
            │   ├── dhg43ne52kxn1e6.o
            │   ├── query-cache.bin
            │   ├── sn76ibo0w8dil4z.o
            │   └── work-products.bin
            └── s-g21ocip69e-1gz7gsu.lock

7 directories, 17 files
$ $ du -h target/debug/
3,2M	target/debug/deps
4,0K	target/debug/examples
564K	target/debug/incremental/hello_cargo_2-1tf9vp8hw5tph/s-g21ocip69e-1gz7gsu-2d3iv3pzmnper
568K	target/debug/incremental/hello_cargo_2-1tf9vp8hw5tph
572K	target/debug/incremental
20K	target/debug/.fingerprint/hello-cargo-2-61ab1226333d611e
24K	target/debug/.fingerprint
4,0K	target/debug/build
3,8M	target/debug/
$
```

Hasil dari membangun aplikasi menggunakan versi *debug* adalah:

1. Direktori `target/debug` sebesar 3,8 MB
2. Hasil kompilasi utama: 

```bash
$ ls -la target/debug/hello-cargo-2
-rwxr-xr-x 2 zaky zaky 3290088 Sep  4 12:21 target/debug/hello-cargo-2`
$
```

_Versi *Release*_

```bash
$ cargo build --release
   Compiling hello-cargo-2 v0.1.0 (/home/zaky/kerjaan/src/rust/hello-cargo-2)
    Finished release [optimized] target(s) in 0.54s
$ tree target/release/
target/release/
├── build
├── deps
│   ├── hello_cargo_2-0904ddb38520974e
│   └── hello_cargo_2-0904ddb38520974e.d
├── examples
├── hello-cargo-2
├── hello-cargo-2.d
└── incremental

4 directories, 4 files
$ du -h target/release/
3,2M	target/release/deps
4,0K	target/release/examples
4,0K	target/release/incremental
20K	target/release/.fingerprint/hello-cargo-2-0904ddb38520974e
24K	target/release/.fingerprint
4,0K	target/release/build
3,2M	target/release/
$
```

Hasil dari membangun aplikasi menggunakan versi *release* adalah:

1. Direktori `target/release` sebesar 3,2 MB
2. Hasil kompilasi utama: 

```bash
$ ls -la target/release/hello-cargo-2
-rwxr-xr-x 2 zaky zaky 3280008 Sep  4 16:00 target/release/hello-cargo-2
$
```

Dari apa yang telah dihasilkan tersebut, kita bisa mengetahui bahwa versi *release* mempunyai ukuran lebih kecil serta waktu kompilasi yang lebih cepat daripada versi *debug*.

#### Menjalankan Hasil

Untuk menjalankan hasil, hasil utama kompilasi bisa dieksekusi secara langsung, atau bisa juga menggunakan `cargo run`.

```bash
$ target/debug/hello-cargo-2 
Hello, world!
$ target/release/hello-cargo-2 
Hello, world!
$ cargo run 
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/hello-cargo-2`
Hello, world!
$ cargo run --release
    Finished release [optimized] target(s) in 0.00s
     Running `target/release/hello-cargo-2`
Hello, world!
$
```

#### Menggunakan `cargo` untuk Mengelola *Dependencies*

Seperti yang telah dijelaskan di awal, `cargo` bisa digunakan untuk mengelola berbagai pustaka yang diperlukan. Pengelolaan ini dilakukan menggunakan file `Cargo.toml`. Berikut ini kita akan membuat aplikasi yang memanfaatkan suatu pustaka dari https://crates.io. 

Aplikasi yang kita buat merupakan aplikasi untuk mengkonversi warna 4-bit sRGB dan warna palet 8-bit yang digunakan oleh terminal ANSI (xterm, rxvt-unicode) ke dalam mode warna 256.

> **Catatan**: penggunakan *crate* pada bagian ini hanya merupakan contoh saja. Hal yang perlu diperhatikan adalah cara menggunakan *crate* / pustaka. Mengenai pemanfaatan pustakan dan kode sumber, tidak perlu dipahami.

*Crate* yang digunakan bisa diperoleh di https://crates.io/crates/ansi_colours. Masukkan dependensi ini ke `Cargo.toml`:

```bash
[package]
name = "hello-time"
version = "0.1.0"
edition = "2018"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
ansi_colours = "1.0.4"
```

Kompilasi bisa dilakukan seperti biasa. Saat proses membangun aplikasi, `cargo` akan mengambil dan mengelola pustaka / *crate* yang sudah kita spesifikasikan.

```bash
$ cargo build --release
    Updating crates.io index
  Downloaded ansi_colours v1.0.4
  Downloaded cc v1.0.70
  Downloaded 2 crates (67.7 KB) in 0.87s
   Compiling cc v1.0.70
   Compiling ansi_colours v1.0.4
   Compiling hello-time v0.1.0 (/home/zaky/kerjaan/src/rust/hello-time)
    Finished release [optimized] target(s) in 4.69s
$ cargo run --release
    Finished release [optimized] target(s) in 0.00s
     Running `target/release/hello-time`
 50: (0, 255, 215)
(100, 200, 150) ~  78 (95, 215, 135)
$
```

#### Membersihkan Hasil Kompilasi

Jika kita ingin membersihkan direktori proyek dari hasil kompilasi, gunakan perintah `cargo clean` di direktori proyek tersebut.

### Clippy

[Clippy](https://github.com/rust-lang/rust-clippy) digunakan sebagai *linter* dan digunakan untuk menangkap berbagai kemungkinan error yang umum maupun berbagai perbaikan yang bisa digunakan untuk memperbaiki kode sumber kita (meski tidak terdapat error). Untuk menggunakan *clippy*, maka *clippy* harus terinstall - biasanya sudah diinstall saat menginstall Rust menggunakan `rustup`. Jika belum terinstall, gunakan:

```bash
$ rustup component add clippy
```

Contoh penggunaaan *clippy* pada proyek `hello-cargo-2` di atas:

```bash
$ cargo clippy --release
    Checking hello-cargo-2 v0.1.0 (/home/zaky/kerjaan/src/rust/hello-cargo-2)
    Finished release [optimized] target(s) in 0.03s
$
```

Misal, kita buat error dengan sengaja di `src/main.rs` dengan menghapus penutup string:

```rust
fn main() {
    println!("Hello, world!);
}
```

Kita bisa menggunakan *clippy* berikut ini:

```bash
$ cargo clippy --release
    Checking hello-cargo-2 v0.1.0 (/home/zaky/kerjaan/src/rust/hello-cargo-2)
error[E0765]: unterminated double quote string
 --> src/main.rs:2:14
  |
2 |       println!("Hello, world!);
  |  ______________^
3 | | }
  | |__^

error: aborting due to previous error

For more information about this error, try `rustc --explain E0765`.
error: could not compile `hello-cargo-2`

To learn more, run the command again with --verbose.
$
```

Pada bagian awal seperti ini, error serta saran yang muncul sama dengan saat menggunakan `cargo build`, tetapi semakin kompleks kesalahan serta kode sumber, maka *clippy* akan memberikan masukan yang lebih baik. Pada posisi ini, pahami penggunaan *clippy*.

## Mengikuti Perkembangan Rust

Perkembangan Rust sangat menarik dan dinamis. Berikut ini adalah beberapa tempat yang bisa menjadi panduan untuk mengikuti perkembangan dari Rust.

1. [This Week in Rust](https://this-week-in-rust.org/): *newsletter* mingguan tentang perkembangan Rust
2. [Awesome Rust](https://github.com/rust-unofficial/awesome-rust).
3. [Not-Yet-Awesome Rust](https://github.com/not-yet-awesome-rust/not-yet-awesome-rust): software, kode sumber, maupun berbagai sumber daya yang belum ada di Rust meski sangat diperlukan.
4. [Komunitas Rust](https://www.rust-lang.org/community)
5. [Cari tags `Rust` di StackOverflow](https://stackoverflow.com/tags).

