# Getting Started with ArangoDB

## Environment Variable(s)

`$ARANGODB_HOME` shoud be set to ArangoDB installation directory

## Configuration

Put all contents of [conf](conf/) at one of this location:

1.  $HOME/.arangodb/etc/relative/
2.  $ARANGODB_HOME/etc/arangodb3/
3.  $ARANGODB_HOME/.arangodb/
4.  /etc/arangodb3/

## Start ArangoDB

```bash
$ arangod --configuration ~/.arangodb/arangod.conf
2022-06-25T14:38:42Z [13805] INFO [e52b0] {general} ArangoDB 3.9.2 [linux] 64bit, using jemalloc, build tags/v3.9.2-0-g8bf70c5f5b6, VPack 0.1.35, RocksDB 6.27.0, ICU 64.2, V8 7.9.317, OpenSSL 1.1.1o  3 May 2022
2022-06-25T14:38:42Z [13805] INFO [75ddc] {general} detected operating system: Linux version 5.18.0-2-amd64 (debian-kernel@lists.debian.org) (gcc-11 (Debian 11.3.0-3) 11.3.0, GNU ld (GNU Binutils for Debian) 2.38.50.20220615) #1 SMP PREEMPT_DYNAMIC Debian 5.18.5-1 (2022-06-16)
2022-06-25T14:38:42Z [13805] INFO [25362] {memory} Available physical memory: 8087801856 bytes, available cores: 8
2022-06-25T14:38:42Z [13805] INFO [3bb7d] {cluster} Starting up with role SINGLE
2022-06-25T14:38:42Z [13805] INFO [f6e0e] {aql} memory limit per AQL query automatically set to 4852681113 bytes. to modify this value, please adjust the startup option `--query.memory-limit`
2022-06-25T14:38:42Z [13805] INFO [a1c60] {syscall} file-descriptors (nofiles) hard limit is 1048576, soft limit is 1048576
2022-06-25T14:38:44Z [13805] INFO [fe333] {engines} RocksDB recovery starting, scanning WAL starting from sequence number 1990, latest sequence number: 2070
2022-06-25T14:38:44Z [13805] INFO [a4ec8] {engines} RocksDB recovery finished, WAL entries scanned: 81, recovery start sequence number: 1990, latest WAL sequence number: 2070, max tick value found in WAL: 609, last HLC value found in WAL: 0
2022-06-25T14:38:44Z [13805] INFO [c1b63] {arangosearch} ArangoSearch maintenance: [1..1] commit thread(s), [1..1] consolidation thread(s)
2022-06-25T14:38:44Z [13805] INFO [6ea38] {general} using endpoint 'http+tcp://127.0.0.1:8529' for non-encrypted requests
2022-06-25T14:38:46Z [13805] INFO [cf3f4] {general} ArangoDB (version 3.9.2 [linux]) is ready for business. Have fun!
```

If needed, `arangosh` can be used as a client for ArangoDB:

```bash
$ arangosh
Please specify a password: 

                                       _     
  __ _ _ __ __ _ _ __   __ _  ___  ___| |__  
 / _` | '__/ _` | '_ \ / _` |/ _ \/ __| '_ \ 
| (_| | | | (_| | | | | (_| | (_) \__ \ | | |
 \__,_|_|  \__,_|_| |_|\__, |\___/|___/_| |_|
                       |___/                 

arangosh (ArangoDB 3.9.2 [linux] 64bit, using jemalloc, build tags/v3.9.2-0-g8bf70c5f5b6, VPack 0.1.35, RocksDB 6.27.0, ICU 64.2, V8 7.9.317, OpenSSL 1.1.1o  3 May 2022)
Copyright (c) ArangoDB GmbH

Command-line history will be persisted when the shell is exited. You can use `--console.history false` to turn this off
Connected to ArangoDB 'http+tcp://127.0.0.1:8529, version: 3.9.2 [SINGLE, server], database: '_system', username: 'root'

Type 'tutorial' for a tutorial or 'help' to see common examples
127.0.0.1:8529@_system> 
```

From arangosh above, we will create database (**myarangodb**) and user for our database (**bpdp**). 

```js
> const users = require('@arangodb/users');
// username: bpdp
// password: bpdpass
users.save('bpdp', 'bpdpass');
> db._createDatabase('myarangodb');
> users.grantDatabase('bpdp', 'myarangodb', 'rw');
````

Put username and pass in arangosh configuration (`$HOME/.arangodb/arangosh.conf`) and then use the configuration for arangosh:

```bash
$ arangosh --configuration ~/.arangodb/arangosh.conf

                                       _
  __ _ _ __ __ _ _ __   __ _  ___  ___| |__
 / _` | '__/ _` | '_ \ / _` |/ _ \/ __| '_ \
| (_| | | | (_| | | | | (_| | (_) \__ \ | | |
 \__,_|_|  \__,_|_| |_|\__, |\___/|___/_| |_|
                       |___/

arangosh (ArangoDB 3.9.2 [linux] 64bit, using jemalloc, build tags/v3.9.2-0-g8bf70c5f5b6, VPack 0.1.35, RocksDB 6.27.0, ICU 64.2, V8 7.9.317, OpenSSL 1.1.1o  3 May 2022)
Copyright (c) ArangoDB GmbH

Command-line history will be persisted when the shell is exited. You can use `--console.history false` to turn this off
Connected to ArangoDB 'http+tcp://127.0.0.1:8529, version: 3.9.2 [SINGLE, server], database: 'myarangodb', username: 'bpdp'

Type 'tutorial' for a tutorial or 'help' to see common examples
127.0.0.1:8529@myarangodb>
```
