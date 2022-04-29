# SpaceVim and Language Server Protocol

Some of you may already know about [LSP/LSIF](https://microsoft.github.io/language-server-protocol/) and possibly have been used them intensively, but for some, maybe it's a little bit confusing. In this post, I will explain about how to setup Language Server Protocol in SpaceVim. This can be separated into two conditions:

1. [Supported programming language](https://spacevim.org/layers/language-server-protocol/).
2. Not supported yet

For both condition, the *lsp* layer should be installed and activated. Use this in ``$HOME/.Spacevim.d/init.toml``:

```
[[layers]]
  name = "lsp"
```

For first condition, it is easier to setup since you just activate Language Server Protocol client in SpaceVim and install the server (depends on your programming language(s) of choice). For example, if I want to use Rust with LSP inside SpaceVim, what I did just put some configuration at ``$HOME/.SpaceVim.d/init.toml``:

```
[[layers]]
  name = "lsp"
  filetypes = [
    "rust"
  ]
```

SpaceVim will take care of everything, provided that Rust compiler toolchain has been installed succesfully (means you have *rls* in your $PATH).

What if my favorit programming language has no official support from SpaceVim? Now, see, this is the beauty of LSP. Once you have executable server for a programming language of your choice available, then things are easy. I'll give an example of *OCaml* here.

Since we need to find the server for OCaml's LSP, let's find one. We have [ocamllsp](https://github.com/ocaml/ocaml-lsp) here. Let's install it so that we can have server implementation for Ocaml:

```
$ opam pin add ocaml-lsp-server https://github.com/ocaml/ocaml-lsp.git
Package ocaml-lsp-server does not exist, create as a NEW package? [Y/n] Y
Processing: [ocaml-lsp-server.~dev: git]
[ocaml-lsp-server.~dev] synchronised from git+https://github.com/ocaml/ocaml-lsp.git
ocaml-lsp-server is now pinned to git+https://github.com/ocaml/ocaml-lsp.git (version ~dev)

The following actions will be performed:
  ∗ install menhirLib           20200624 [required by menhir]
  ∗ install stdlib-shims        0.1.0    [required by ocaml-lsp-server]
  ∗ install menhirSdk           20200624 [required by menhir]
  ∗ install easy-format         1.3.2    [required by yojson]
  ∗ install dune-build-info     2.6.2    [required by ocaml-lsp-server]
  ∗ install menhir              20200624 [required by ocaml-lsp-server]
  ∗ install biniou              1.2.1    [required by yojson]
  ∗ install yojson              1.7.0    [required by ocaml-lsp-server]
  ∗ install ppx_yojson_conv_lib v0.14.0  [required by ocaml-lsp-server]
  ∗ install ocaml-lsp-server    ~dev*
===== ∗ 10 =====
Do you want to continue? [Y/n] Y

<><> Gathering sources ><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
[easy-format.1.3.2] downloaded from cache at https://opam.ocaml.org/cache
[biniou.1.2.1] downloaded from cache at https://opam.ocaml.org/cache
[dune-build-info.2.6.2] downloaded from cache at https://opam.ocaml.org/cache
[menhir.20200624] downloaded from cache at https://opam.ocaml.org/cache
[menhirLib.20200624] downloaded from cache at https://opam.ocaml.org/cache
[ppx_yojson_conv_lib.v0.14.0] downloaded from cache at https://opam.ocaml.org/cache
[stdlib-shims.0.1.0] downloaded from cache at https://opam.ocaml.org/cache
[yojson.1.7.0] found in cache
[menhirSdk.20200624] downloaded from cache at https://opam.ocaml.org/cache
[ocaml-lsp-server.~dev] synchronised from git+https://github.com/ocaml/ocaml-lsp.git

<><> Processing actions <><><><><><><><><><><><><><><><><><><><><><><><><><><><>
∗ installed stdlib-shims.0.1.0
∗ installed dune-build-info.2.6.2
∗ installed easy-format.1.3.2
∗ installed menhirLib.20200624
∗ installed menhirSdk.20200624
∗ installed biniou.1.2.1
∗ installed yojson.1.7.0
∗ installed ppx_yojson_conv_lib.v0.14.0
∗ installed menhir.20200624
∗ installed ocaml-lsp-server.~dev
Done.
$ which ocamllsp
/home/bpdp/.opam/4.10.0/bin/ocamllsp
$
```

*note*: the result of the last command (``which ocamllsp``) should be different than yours.

Now, put this configuration:

```
[[layers]]
  name = "lsp"
  filetypes = [
    "rust",
    "ocaml"
  ]
  [layers.override_cmd]
    ocaml = ["ocamllsp"]  
```

You are all set. Fire up *nvim* or *vim* and enjoy!

