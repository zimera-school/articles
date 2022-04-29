# Tentang Bab Ini

IDE (*Integrated Development Environment*) adalah software yang digunakan sebagai peranti pengembangan terintegrasi. IDE sangat penting dalam membangun aplikasi. Produktivitas pemrogram biasanya sangat tergantung dari kepiawaiannya menggunakan IDE. Bab ini membahas tentang IDE yang bisa digunakan untk membangun aplikasi menggunakan Rust. Ada beberapa software dasar yang akan dijelaskan dan digunakan dalam pembahasan ini, yaitu:

1. [Vim](https://www.vim.org/) / [NeoVim](https://neovim.io/)
2. [Visual Studio Code](https://code.visualstudio.com/) / [VSCodium](https://vscodium.com/)
3. [Eclipse](https://www.eclipse.org/)

Pada umumnya, terkait dengan IDE, ada 2 kategori:

1. IDE yang memang sejak awal khusus dirancang untuk suatu bahasa pemrograman tertentu. Contoh dari IDE ini antara lain adalah IDE Borland Delphi, IntelliJ IDEA, Apache NetBeans, dan lain-lain. Software jenis ini biasanya juga memberikan fasilitas pembuatan plugins untuk bahasa pemrograman lain dengan mekanisme plugins yang khusus untuk IDE tersebut, contohnya adalah Apache NetBeans yang bisa digunakan untuk C/C++, PHP, dan lain-lain. Mekanisme ini tidak cross software, artinya mekanisme plugin untuk Apache NetBeans tidak akan bisa digunakan oleh IntelliJ IDEA.
2. Editor teks yang bersifat umum / generik dan memerlukan konfigurasi maupun plugin / add-on / tambahan untuk keperluan penggunaan editor teks tersebut untuk keperluan suatu bahasa pemrograman.

Kecenderungan saat ini menuju ke nomor 2, bahkan beberapa IDE (kategori nomor 1) juga menggunakan mekanisme nomor 2. Mekanisme pertama memang cenderung ditinggalkan karena setiap IDE / editor teks harus secara spesifik mendefinisikan dan mengelola plugins sendiri-sendiri. Selain mendatangkan kerepotan pengelole IDE / editor teks, hal ini juga mendatangkan kerepotan komunikas serta pengembangan kompilator / interpreter bahasa pemrograman. Karena berbagai kerepotan itu, makan muncul [Language Server Protocol / LSP](https://microsoft.github.io/language-server-protocol/).

Dengan menggunakan mekanisme LSP, maka setiap IDE / editor teks hanya perlu membuat dan mengelola klien LSP  saja sesuai dengan protokol LSP. Setelah itu, komunitas bahasa pemrograman tertentu akan membuat dan mengelola server LSP sesuai spesifikasi protokol LSP. Dengan demikian, selama IDE / editor teks mengikuti protokol klien LSP dan tersedia server LSP dari komunitas pengembangan bahasa pemrograman, maka sudah cukup untuk menjadikan IDE / editor teks tersebut sebagai IDE bahasa pemrograman sesuai dengan server LSP yang dikembangkan komunitas pengembang bahasa pemrograman tersebut. Protokol LSP menyediakan:

1. *Completion*
2. *Hover/tooltips*
3. *Go to definition*
4. *Show/go to references*
5. *Show method signatures*
6. *Rename*
7. *Code actions*, misalnya untuk *automatic formatting*, *organize imports*,dan lain-lain.

Mekanisme LSP kurang lebih sebagai berikut:

___
Menjalankan IDE / Editor teks => menjalankan plugin / add-on klien LSP => mengaktifkan server LSP sesuai konfigurasi => IDE bahasa pemrograman.
___

Untuk kompilator Rust, server LSP dikembangkan di [repo **rls**](https://github.com/rust-lang/rls). Untuk menggunakan LSP, install terlebih dahulu `rls`:

```bash
$ rustup component add rls rust-analysis rust-src
info: downloading component 'rls'
info: installing component 'rls'
info: downloading component 'rust-analysis'
  2.8 MiB /   2.8 MiB (100 %) 868.9 KiB/s in  4s ETA:  0s
info: installing component 'rust-analysis'
info: downloading component 'rust-src'
  2.3 MiB /   2.3 MiB (100 %)   1.2 MiB/s in  2s ETA:  0s
info: installing component 'rust-src'
$
```

Hasilnya adalah sebagai berikut:

```bash
$ rls --version
rls 1.41.0 (a82a052 2021-07-21)
$ rls --help

    --version or -V to print the version and commit info
    --help or -h for this message
    --cli starts the RLS in command line mode
    No input starts the RLS as a language server
$
```

Setelah itu, IDE / editor teks dikonfigurasi untuk mengaktifkan LSP.

## Vim / Neovim

Mengkonfigurasi Vim / Neovim dari awal cukup menyita waktu dan cenderung ribet. Untuk menyingkat, akan digunakan [SpaceVim](https://spacevim.org/). Dengan menggunakan SpaceVim, kerumitan-kerumitan instalasi klien LSP akan diabstraksi oleh Spacevim, sehingga menggunakan fasilitas LSP akan lebih mudah.

### Instalasi Vim

Distribusi Linux biasanya secara default sudah menginstall Vim. Jika belum, maka bisa menggunakan *package manager* (apt, urpmi, dnf, pacman, dan lain-lain) ataupun install dari kode sumber Vim secara langsung. Untuk OS lain, bisa mengikuti petunjuk di [halaman download Vim](https://www.vim.org/download.php).

### Instalasi Neovim

Neovim biasanya juga tersedia di berbagai distribusi Linux dan bisa diinstall menggunakan *package manager*. Untuk OS lain, bisa mengikuti petunjuk di [GitHub Releases page untuk Neovim](https://github.com/neovim/neovim/releases).

### Instalasi SpaceVim

Instalasi Spacevim dijelaskan di [URL instalasi SpaceVim]. Jika menggunakan Windows, tersedia file `install.cmd` yang bisa dijalankan secara langsung. Jika menggunakan Linux:

_Instalasi SpaceVim untuk Vim dan Neovim_

```bash
$ curl -sLf https://spacevim.org/install.sh | bash
```

_Instalasi SpaceVim untuk Vim_

```bash
$ curl -sLf https://spacevim.org/install.sh | bash -s -- --install vim
```

_Instalasi SpaceVim untuk Neovim_

```bash
$ curl -sLf https://spacevim.org/install.sh | bash -s -- --install neovim
$
```

> **Catatan**: saat menginstall SpaceVim di Linux, kompilasi harus dilakukan untuk `vimproc.vim`. Masuk ke direktori `$HOME/.SpaceVim/bundle/vimproc.vim`, setelah itu berikan perintah `make`. Hasilnya adalah file `$HOME/.SpaceVim/bundle/vimproc.vim/lib/vimproc_linux64.so*`

### Konfigurasi SpaceVim

Konfigurasi SpaceVim diletakkan pada file `$HOME/Spacevim.d/init.toml`. Berikut ini tambahan yang diperlukan untuk konfigurasi SpaceVim - Rust:

```bash
...
...
...
[[layers]]
  name = "lang#toml"

[[layers]]
  name = "lang#rust"

[[layers]]
  name = "lsp"
  filetypes = [
    "rust"
  ]
  [layers.override_cmd]
    rust = ["rls"]
...
...
...
```

> **Catatan**: plugin untuk TOML juga harus diaktifkan karena konfigurasi `cargo` menggunakan format serialisasi [TOML](https://toml.io/en/).


Saat menjalankan Rust, akan diinstall paket-paket yang diperlukan secara otomatis. Setelah selesai instalasi, Vim / Neovim bisa digunakan untuk IDE Rust.

![Neovim + SpaceVim untuk Rust](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zkqgbbf7cfzzwrltydav.png)

## Visual Studio Code / VSCodium

Visual Studio Code (selanjutnya disebut *VS Code* adalah IDE generik yang dibuat oleh Microsoft. VS Code dirancang untuk memungkinkan adanya penambahan fasilitas melalui [Extension](https://code.visualstudio.com/docs/editor/extension-marketplace). Daftar lengkap *extensions* bisa dilihat pada [Extensions Marketplace](https://marketplace.visualstudio.com/VSCode).

VSCodium adalah versi VS Code tanpa *telemetry*. [Telemetry](https://code.visualstudio.com/docs/getstarted/telemetry) adalah fasilitas dari VS Code yang mengumpulkan data dari pengguna untuk keperluan layanan yang lebih baik (setidaknya, definisinya mengatakan demikian). VS Code secara default mengaktifkan fasilitas telemetry. Bagian lainnya sama dengan VS Code sehingga pembahasan tetang VS Code juga berlaku untuk VSCodium. Selanjutnya, keduanya akan disebut dengan *VS Code* saja.

### Instalasi VS Code / VSCodium

Untuk instalasi VS Code, cukup download dari [download VS Code](https://code.visualstudio.com/Download) / ([download VSCodium](https://github.com/VSCodium/vscodium/releases)) dan kemudian ekstraksi hasil download tersebut. Untuk menjalankan VS Code, cukup jalankan `code` yang terdapat pada direktori hasil ekstraksi. Jika menggunakan VSCodium, jalankan `codium` yang terdapat pada direktori hasil ekstraksi.

### Extension untuk Rust

Extension untuk Rust di VS Code tersedia di [marketplace - Rust](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust). Untuk melakukan instalasi, tekan `Ctl-P` (*Quick Open*) dan masukkan perintah untuk instalasi berikut ini: `ext install rust-lang.rust`. Setelah itu, extension akan di-install:

![Instalasi extension Rust di VS Code](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3ulligpvnwkb9jz8va55.png)

Setelah itu, kita bisa menggunakan VS Code sebagai IDE  Rust. Gunakan **File - Open Folder** untuk membuka proyek Rust.

![VS Code - Rust in Action](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8c4zj5o1hebnke6f7053.png)




## Eclipse

[Eclipse Foundation](https://eclipse.org) juga mempunyai proyek yang didedikasikan untuk membuat IDE Rust dengan basis IDE Eclipse untuk membangun aplikasi menggunakan Rust. Untuk memperoleh software ini, silahkan akses ke Web dari proyek [Eclipse Corrosion](https://projects.eclipse.org/projects/tools.corrosion). Sebagai informasi, sampai saat artikel ini ditulis, Eclipse Corrosion masih berstatus *Eclipse Incubation*, artinya belum menjadi proyek utama, masih masa inkubasi. Hal ini perlu diperjelas supaya memahami dukungan dari *Eclipse Foundation* terhadap IDE berbasis Eclipse ini.

Untuk menggunakan Eclipse Corrosion, lihat terlebih dahulu versi terbaru dari Eclipse Corrosion di https://projects.eclipse.org/projects/tools.corrosion. Setelah itu, download Eclipse Corrosion dari https://download.eclipse.org/corrosion/releases/latest/products/. Kelak, jika sudah tidak berada di posisi inkubasi, Eclipse Corrosion akan bisa diambil dari download utama Eclipse.

> **Catatan**: untuk menggunakan Eclipse, setidaknya harus memiliki JRE (Java Runtime Environment) versi 8.

Setelah itu, ekstrak hasil download:

```bash
$ tar -xvf eclipseide-rust-1.2.1-linux.gtk.x86_64.tar.gz
eclipse/
eclipse/p2/
eclipse/p2/org.eclipse.equinox.p2.engine/
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/1623857155371.profile.gz
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/.lock
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/.data/
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/.data/org.eclipse.equinox.internal.p2.touchpoint.eclipse.actions/
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/.data/org.eclipse.equinox.internal.p2.touchpoint.eclipse.actions/jvmargs
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/.data/.settings/
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/.data/.settings/org.eclipse.equinox.p2.artifact.repository.prefs
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/.data/.settings/org.eclipse.equinox.p2.metadata.repository.prefs
eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/CorrosionIDE.profile/1623857155392.profile.gz
...
...
...
eclipse/plugins/org.eclipse.corrosion_1.2.1.202106081156.jar
eclipse/icon.xpm
eclipse/eclipse
eclipse/.eclipseproduct
eclipse/readme/
eclipse/readme/readme_eclipse.html
eclipse/dropins/
eclipse/eclipse.ini
eclipse/configuration/
eclipse/configuration/org.eclipse.equinox.simpleconfigurator/
eclipse/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
eclipse/configuration/config.ini
eclipse/configuration/org.eclipse.update/
eclipse/configuration/org.eclipse.update/platform.xml
$
```

Hasil ekstrak adalah direktori *eclipse* dengan isi sebagai berikut:

```bash
$ cd eclipse/
$ ls -la
total 376
drwxr-xr-x  8 zaky zaky   4096 Jun 16 22:25 ./
drwxr-xr-x  4 zaky zaky   4096 Sep 11 11:40 ../
-rw-r--r--  1 zaky zaky  84784 Jun 16 22:25 artifacts.xml
drwxr-xr-x  4 zaky zaky   4096 Jun 16 22:25 configuration/
drwxr-xr-x  2 zaky zaky   4096 Jun 16 22:25 dropins/
-rwxr-xr-x  1 zaky zaky  80072 Jun 12 04:14 eclipse*
-rw-r--r--  1 zaky zaky    821 Jun 16 22:25 eclipse.ini
-rw-r--r--  1 zaky zaky     61 Jun 12 03:06 .eclipseproduct
drwxr-xr-x 37 zaky zaky   4096 Jun 16 22:25 features/
-rwxr-xr-x  1 zaky zaky 140566 Jun 12 04:14 icon.xpm*
drwxr-xr-x  4 zaky zaky   4096 Jun 16 22:25 p2/
drwxr-xr-x 11 zaky zaky  32768 Jun 16 22:25 plugins/
drwxr-xr-x  2 zaky zaky   4096 Jun 16 22:25 readme/
$
```

Untuk menjalankan *Eclipse for Rust Developers*, masuk ke direktori hasil ekstrak kemudian eksekusi
file *eclipse* sebagai berikut:

```bash
$ cd eclipse
$ ./eclipse
```

Setelah *splash screen*, Eclipse akan menanyakan *workspace* tempat menyimpan berbagai proyek Rust. Isikan seperti yang anda kehendaki (bebas), setelah itu,
klik pada *Launch*, maka akan dimunculkan window utama dari Eclipse. Sebelum mulai menggunakan Eclipse for Rust, isikan **Rust Preferences** dengan memilih  **Window - Rust Preferences**:

![Rust Preferences](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8w09t7wijrcvz6t65ue7.png)

Setelah isian sesuai, kita bisa menggunakan Eclipse for Rust:

![Window utama Eclipse for Rust](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s3kzox3l0gduadfmkdyv.png)

