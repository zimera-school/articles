## Introduction

A graph is a representation of data structure which emerge from Discrete Mathematics (more specifically, studied in Graph Theory) to represent interconnected data and solving any problems related with those interconnected data. Currently, there are two big graph implementation in software:
1. Triple, mainly represented by [RDF](https://www.w3.org/TR/rdf11-concepts/) with [SPARQL](https://www.w3.org/TR/sparql11-overview/) as its query language. In TripleStore, data is represented as *Subject-Predicate-Object*. The database for this kind of data is usually called *TripleStore*. An example of TripleStore is [BlazeGraph](https://blazegraph.com/). 
2. Property Graph, mainly represented as node and relationship in which they can have properties. The database for this kind of data is usually called *Graph Database*. [Gremlin - by TinkerPop project](https://tinkerpop.apache.org/) and [Cypher - by Neo4J](https://opencypher.org/) are their query language (also [AQL - Arango Query Language - by ArangoDB](https://www.arangodb.com/docs/stable/aql/), but AQL does not only provides graph query language).

In this article, we will explain Property Graph only. Some Graph DBMS which support Property Graph natively, for example:
1. [JanusGraph](https://janusgraph.org/)
2. [Neo4J](https://neo4j.com/)

Some other DBMS use already available DBMS engine to handle graph data, for example:
1. [PostgreSQL](https://www.postgresql.org/) with graph extension, developed by a team at Apache Software Foundation as [Apache AGE](https://age.apache.org/). Apache AGE uses Gremlin.
2. [Redis](https://redis.io/) module for graph - [RedisGraph](https://oss.redis.com/redisgraph/). RedisGraph uses Cypher for its query language.
3. [YugabyteDB](https://www.yugabyte.com/) provides a detail on [how to represent and manipulate graph data using YugabyteDB](https://docs.yugabyte.com/latest/api/ysql/the-sql-language/with-clause/traversing-general-graphs/graph-representation/)

Let's start with RedisGraph!

## Redis Installation

If you already have Redis installed using your distro, you may use them provided that you use Redis version as required in [Redis module center](https://redis.io/modules). If not, just use your distro specific package manager. For example, in Debian-based distro, you may use:

```bash
$ sudo apt install redis-server redis-cli redis-tools
```

After that, go to RedisGraph installation. If you want to use the hard way - compile Redis, use this guide below. Redis src has beed downloaded from [Redis website](https://redis.io/download). In this article, I use version 6.2.6 with TLS.

```
$ tar -xvf redis-6.2.6.tar.gz
$ cd redis-6.2.6
$ make BUILD_TLS=yes
cd src && make all
make[1]: Entering directory '/home/bpdp/master/postdoc-ugm/redis-6.2.6/src'
    CC Makefile.dep
...
...
...
    CC mt19937-64.o
    LINK redis-server
    INSTALL redis-sentinel
    CC redis-cli.o
redis-cli.c: In function ‘_serverAssert’:
redis-cli.c:485:18: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
  485 |     *((char*)-1) = 'x';
      |     ~~~~~~~~~~~~~^~~~~
    CC cli_common.o
    LINK redis-cli
    CC redis-benchmark.o
redis-benchmark.c: In function ‘_serverAssert’:
redis-benchmark.c:269:18: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
  269 |     *((char*)-1) = 'x';
      |     ~~~~~~~~~~~~~^~~~~
    LINK redis-benchmark
    INSTALL redis-check-rdb
    INSTALL redis-check-aof

Hint: It's a good idea to run 'make test' ;)

make[1]: Leaving directory '/home/bpdp/master/postdoc-ugm/redis-6.2.6/src'
$ 
```

At this point, we've already got Redis compiled, ready to serve. The results are in `src/`:

```bash
$ ls -la src/
total 63300
drwxr-xr-x 3 bpdp bpdp   12288 Okt 21 12:15 ./
drwxr-xr-x 7 bpdp bpdp    4096 Okt  4 17:59 ../
-rw-r--r-- 1 bpdp bpdp   89642 Okt  4 17:59 acl.c
-rw-r--r-- 1 bpdp bpdp     426 Okt 21 12:15 acl.d
-rw-r--r-- 1 bpdp bpdp  287152 Okt 21 12:15 acl.o
...
...
...
-rwxr-xr-x 1 bpdp bpdp 4877400 Okt 21 12:15 redis-benchmark*
-rw-r--r-- 1 bpdp bpdp   76300 Okt  4 17:59 redis-benchmark.c
-rw-r--r-- 1 bpdp bpdp     441 Okt 21 12:15 redis-benchmark.d
-rw-r--r-- 1 bpdp bpdp  796440 Okt 21 12:15 redis-benchmark.o
-rwxr-xr-x 1 bpdp bpdp 9310280 Okt 21 12:15 redis-check-aof*
-rw-r--r-- 1 bpdp bpdp    7243 Okt  4 17:59 redis-check-aof.c
-rw-r--r-- 1 bpdp bpdp     444 Okt 21 12:15 redis-check-aof.d
-rw-r--r-- 1 bpdp bpdp   35744 Okt 21 12:15 redis-check-aof.o
-rwxr-xr-x 1 bpdp bpdp 9310280 Okt 21 12:15 redis-check-rdb*
-rw-r--r-- 1 bpdp bpdp   14772 Okt  4 17:59 redis-check-rdb.c
-rw-r--r-- 1 bpdp bpdp     444 Okt 21 12:15 redis-check-rdb.d
-rw-r--r-- 1 bpdp bpdp   89992 Okt 21 12:15 redis-check-rdb.o
-rwxr-xr-x 1 bpdp bpdp 4678976 Okt 21 12:15 redis-cli*
-rw-r--r-- 1 bpdp bpdp  318821 Okt  4 17:59 redis-cli.c
-rw-r--r-- 1 bpdp bpdp     396 Okt 21 12:15 redis-cli.d
-rw-r--r-- 1 bpdp bpdp  877064 Okt 21 12:15 redis-cli.o
-rw-r--r-- 1 bpdp bpdp   66774 Okt  4 17:59 redismodule.h
-rwxr-xr-x 1 bpdp bpdp 9310280 Okt 21 12:15 redis-sentinel*
-rwxr-xr-x 1 bpdp bpdp 9310280 Okt 21 12:15 redis-server*
...
...
...
-rw-r--r-- 1 bpdp bpdp   21090 Okt  4 17:59 zmalloc.c
-rw-r--r-- 1 bpdp bpdp     100 Okt 21 12:15 zmalloc.d
-rw-r--r-- 1 bpdp bpdp    5215 Okt  4 17:59 zmalloc.h
-rw-r--r-- 1 bpdp bpdp   50152 Okt 21 12:15 zmalloc.o
$ 
```

Just in case, if you want to check whether everything is ok, test them using `make test`:

```bash
$ make test
cd src && make test
make[1]: Entering directory '/home/bpdp/master/postdoc-ugm/redis-6.2.6/src'
Cleanup: may take some time... OK
Starting test server at port 21079
[ready]: 15259
...
...
...
Testing solo test
[ok]: Active defrag
[ok]: Active defrag big keys
[ok]: Active defrag big list
[ok]: Active defrag edge case
[64/64 done]: defrag (74 seconds)

                   The End

Execution time of different units:
  0 seconds - unit/printver
  0 seconds - unit/type/incr
  1 seconds - unit/protocol
  1 seconds - unit/info
  1 seconds - unit/keyspace
  2 seconds - unit/auth
  0 seconds - unit/quit
  3 seconds - unit/type/hash
  2 seconds - unit/acl
  6 seconds - unit/type/set
  5 seconds - unit/multi
  6 seconds - unit/sort
  7 seconds - unit/type/string
  7 seconds - unit/scan
  7 seconds - unit/type/stream-cgroups
  8 seconds - unit/type/list
  13 seconds - unit/other
  15 seconds - unit/expire
  16 seconds - unit/type/list-2
  12 seconds - unit/latency-monitor
  0 seconds - integration/convert-zipmap-hash-on-load
  3 seconds - integration/logging
  21 seconds - unit/type/zset
  14 seconds - integration/aof
  17 seconds - integration/replication-2
  13 seconds - integration/rdb
  30 seconds - unit/type/list-3
  8 seconds - integration/failover
  31 seconds - unit/dump
  32 seconds - unit/type/stream
  1 seconds - unit/pubsub
  2 seconds - unit/slowlog
  27 seconds - integration/block-repl
  3 seconds - integration/redis-benchmark
  1 seconds - unit/limits
  20 seconds - integration/corrupt-dump-fuzzer
  3 seconds - unit/introspection
  16 seconds - integration/psync2-pingoff
  11 seconds - integration/redis-cli
  22 seconds - integration/corrupt-dump
  3 seconds - unit/bitfield
  6 seconds - unit/introspection-2
  2 seconds - unit/lazyfree
  4 seconds - unit/wait
  23 seconds - integration/psync2-reg
  1 seconds - unit/tls
  1 seconds - unit/oom-score-adj
  8 seconds - unit/memefficiency
  14 seconds - unit/scripting
  1 seconds - unit/shutdown
  10 seconds - unit/bitops
  1 seconds - unit/networking
  3 seconds - unit/tracking
  8 seconds - unit/pendingquerybuf
  21 seconds - unit/obuf-limits
  52 seconds - integration/replication-4
  53 seconds - integration/replication-3
  47 seconds - integration/psync2
  46 seconds - unit/hyperloglog
  54 seconds - unit/maxmemory
  54 seconds - north
  123 seconds - unit/aofrw
  165 seconds - integration/replication-psync
  227 seconds - integration/replication
  74 seconds - defrag

\o/ All tests passed without errors!

Cleanup: may take some time... OK
make[1]: Leaving directory '/home/bpdp/master/postdoc-ugm/redis-6.2.6/src'
$
```
Check whether you have this, shows that all tests passed:

```
...
...
\o/ All tests passed without errors!
...
...
```

Now, install Redis using this command:

```bash
$ make PREFIX=/home/bpdp/software/postdoc-ugm/redis-6.2.6/ install
cd src && make install
make[1]: Entering directory '/home/bpdp/master/postdoc-ugm/redis-6.2.6/src'

Hint: It's a good idea to run 'make test' ;)

    INSTALL redis-server
    INSTALL redis-benchmark
    INSTALL redis-cli
make[1]: Leaving directory '/home/bpdp/master/postdoc-ugm/redis-6.2.6/src'
$
```

Don't forget to change `PREFIX` to a location in your own computer and then put them inside a text file so that we may source them whenever we need to use Redis (we use Fish Shell, if you use Bash or any other shell, change accordingly):

```bash
$ cat ~/env/fish/postdoc-ugm/redis-graph 
set -x PATH $HOME/software/postdoc-ugm/redis-6.2.6/bin $PATH
$
```

To make background save more robust, use this (if this is not done, Redis will display warning):

```bash
$ sudo sysctl vm.overcommit_memory=1
[sudo] password for bpdp:
vm.overcommit_memory = 1
$
```

To check:

```
$ source ~/env/fish/postdoc-ugm/redis-graph
$ redis-server
4596:C 21 Oct 2021 16:34:31.976 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
4596:C 21 Oct 2021 16:34:31.976 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=4596, just started
4596:C 21 Oct 2021 16:34:31.976 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
4596:M 21 Oct 2021 16:34:31.976 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.6 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                  
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 4596
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           https://redis.io       
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

4596:M 21 Oct 2021 16:34:31.977 # Server initialized
4596:M 21 Oct 2021 16:34:31.977 * Ready to accept connections

```

At that point, we are ready to use Redis server from our `redis-cli`:

```bash
$ redis-cli
127.0.0.1:6379> help
redis-cli 6.2.6
To get help about Redis commands type:
      "help @<group>" to get a list of commands in <group>
      "help <command>" for help on <command>
      "help <tab>" to get a list of possible help topics
      "quit" to exit

To set redis-cli preferences:
      ":set hints" enable online hints
      ":set nohints" disable online hints
Set your preferences in ~/.redisclirc
127.0.0.1:6379> 
```

Now, we are ready with Redis Server and Client. It's time to get RedisGraph ready!

## RedisGraph

RedisGraph has some deps and those dependencies are *not included* inside their source distribution. Therefore, we need to use Git with specific tag (as of today, v2.4.11 is the latest GA). Here's how to get the source:

```bash
$ git clone https://github.com/RedisGraph/RedisGraph -b v2.4.11 --recurse-submodules -j8
Cloning into 'RedisGraph'...
remote: Enumerating objects: 49063, done.
remote: Counting objects: 100% (2906/2906), done.
remote: Compressing objects: 100% (1082/1082), done.
remote: Total 49063 (delta 1998), reused 2448 (delta 1736), pack-reused 46157
Receiving objects: 100% (49063/49063), 39.33 MiB | 114.00 KiB/s, done.
Resolving deltas: 100% (38402/38402), done.
Submodule 'deps/RediSearch' (https://github.com/RediSearch/RediSearch.git) registered for path 'deps/RediSearch'
Submodule 'deps/googletest' (https://github.com/google/googletest.git) registered for path 'deps/googletest'
Submodule 'deps/libcypher-parser' (https://github.com/RedisGraph/libcypher-parser.git) registered for path 'deps/libcypher-parser'
Submodule 'deps/rax' (https://github.com/antirez/rax.git) registered for path 'deps/rax'
Submodule 'deps/readies' (https://github.com/RedisLabsModules/readies.git) registered for path 'deps/readies'
Submodule 'deps/xxHash' (https://github.com/Cyan4973/xxHash.git) registered for path 'deps/xxHash'
Cloning to '/home/bpdp/master/postdoc-ugm/RedisGraph/deps/RediSearch'...
remote: Enumerating objects: 34395, done.        
remote: Counting objects: 100% (1802/1802), done.        
remote: Compressing objects: 100% (1097/1097), done.        
remote: Total 34395 (delta 1150), reused 1182 (delta 696), pack-reused 32593        
Receiving objects: 100% (34395/34395), 23.62 MiB | 71.00 KiB/s, done.
Resolving deltas: 100% (25261/25261), done.
Cloning to '/home/bpdp/master/postdoc-ugm/RedisGraph/deps/rax'...
remote: Enumerating objects: 668, done.        
remote: Counting objects: 100% (25/25), done.        
remote: Compressing objects: 100% (14/14), done.        
remote: Total 668 (delta 12), reused 19 (delta 11), pack-reused 643        
Receiving objects: 100% (668/668), 236.14 KiB | 1.41 MiB/s, done.
Resolving deltas: 100% (414/414), done.
Cloning to '/home/bpdp/master/postdoc-ugm/RedisGraph/deps/readies'...
remote: Enumerating objects: 2354, done.        
remote: Counting objects: 100% (833/833), done.        
remote: Compressing objects: 100% (329/329), done.        
remote: Total 2354 (delta 608), reused 675 (delta 503), pack-reused 1521        
Receiving objects: 100% (2354/2354), 390.69 KiB | 17.00 KiB/s, done.
Resolving deltas: 100% (1577/1577), done.
Cloning to '/home/bpdp/master/postdoc-ugm/RedisGraph/deps/libcypher-parser'...
remote: Enumerating objects: 3250, done.        
remote: Counting objects: 100% (68/68), done.        
remote: Compressing objects: 100% (46/46), done.        
remote: Total 3250 (delta 42), reused 43 (delta 21), pack-reused 3182        
Receiving objects: 100% (3250/3250), 2.10 MiB | 28.00 KiB/s, done.
Resolving deltas: 100% (2488/2488), done.
Cloning to '/home/bpdp/master/postdoc-ugm/RedisGraph/deps/xxHash'...
remote: Enumerating objects: 4784, done.        
remote: Counting objects: 100% (345/345), done.        
remote: Compressing objects: 100% (188/188), done.        
remote: Total 4784 (delta 189), reused 255 (delta 143), pack-reused 4439        
Receiving objects: 100% (4784/4784), 2.54 MiB | 27.00 KiB/s, done.
Resolving deltas: 100% (2922/2922), done.
Cloning to '/home/bpdp/master/postdoc-ugm/RedisGraph/deps/googletest'...
remote: Enumerating objects: 23334, done.        
remote: Counting objects: 100% (234/234), done.        
remote: Compressing objects: 100% (142/142), done.        
remote: Total 23334 (delta 120), reused 146 (delta 81), pack-reused 23100        
Receiving objects: 100% (23334/23334), 9.49 MiB | 44.00 KiB/s, done.
Resolving deltas: 100% (17191/17191), done.
Submodule path 'deps/RediSearch': checked out '68430b3c838374478dd9ffe4e361534f572b16ff'
Submodule 'deps/googletest' (https://github.com/google/googletest.git) registered for path 'deps/RediSearch/deps/googletest'
Submodule 'deps/readies' (https://github.com/RedisLabsModules/readies.git) registered for path 'deps/RediSearch/deps/readies'
Cloning to '/home/bpdp/master/postdoc-ugm/RedisGraph/deps/RediSearch/deps/googletest'...
remote: Enumerating objects: 23334, done.        
remote: Counting objects: 100% (234/234), done.        
remote: Compressing objects: 100% (148/148), done.        
remote: Total 23334 (delta 120), reused 141 (delta 75), pack-reused 23100        
Receiving objects: 100% (23334/23334), 9.56 MiB | 1.05 MiB/s, done.
Resolving deltas: 100% (17185/17185), done.
Kloning ke '/home/bpdp/master/postdoc-ugm/RedisGraph/deps/RediSearch/deps/readies'...
remote: Enumerating objects: 2354, done.        
remote: Counting objects: 100% (833/833), done.        
remote: Compressing objects: 100% (329/329), done.        
remote: Total 2354 (delta 608), reused 675 (delta 503), pack-reused 1521        
Receiving objects: 100% (2354/2354), 390.69 KiB | 853.00 KiB/s, done.
Resolving deltas: 100% (1577/1577), done.
Submodule path 'deps/RediSearch/deps/googletest': checked out 'dea0216d0c6bc5e63cf5f6c8651cd268668032ec'
Submodule path 'deps/RediSearch/deps/readies': checked out '89be267427c7dfcfaab4064942ef0f595f6b1fa3'
Submodule path 'deps/googletest': checked out '565f1b848215b77c3732bca345fe76a0431d8b34'
Submodule path 'deps/libcypher-parser': checked out '38cdee1867b18644616292c77fe2ac1f2b179537'
Submodule path 'deps/rax': checked out 'ba4529f6c836c9ff1296cde12b8557329f5530b7'
Submodule path 'deps/readies': checked out 'd59f3ad4e9b3d763eb41df07567111dc94c6ecac'
Submodule path 'deps/xxHash': checked out '726c14000ca73886f6258a6998fb34dd567030e9'
$
```
Now, we have RedisGraph source code complete with its dependencies. Time to install.
 
### Installation

To install, just do `make` and put `redisgraph.so` file as the result of RedisGraph compilation to any location that we prefer.

```bash
$ cd RedisGraph
$ make
...
...
...
    CC /home/bpdp/master/postdoc-ugm/RedisGraph/src/util/thpool/pools.o
    CC /home/bpdp/master/postdoc-ugm/RedisGraph/src/util/thpool/thpool.o
    CC /home/bpdp/master/postdoc-ugm/RedisGraph/src/util/range/numeric_range.o
    CC /home/bpdp/master/postdoc-ugm/RedisGraph/src/util/range/string_range.o
    CC /home/bpdp/master/postdoc-ugm/RedisGraph/src/util/range/unsigned_range.o
    CC /home/bpdp/master/postdoc-ugm/RedisGraph/src/util/cache/cache_array.o
    CC /home/bpdp/master/postdoc-ugm/RedisGraph/src/util/cache/cache.o
    CC redisgraph.so
objcopy --only-keep-debug redisgraph.so redisgraph.so.debug
objcopy --strip-debug redisgraph.so
objcopy --add-gnu-debuglink redisgraph.so.debug redisgraph.so
make[1]: Leaving directory '/home/bpdp/master/postdoc-ugm/RedisGraph/src'
$
```

### Configuration

Now, put `redisgraph.so` file to any directory and then refer it in a configuration file:

```bash
$ pwd
/home/bpdp/software/postdoc-ugm
$ cat redis-6.2.6/redis.conf
loadmodule /home/bpdp/software/postdoc-ugm/redis/modules/redisgraph.so
$
```

### Let's Try RedisGraph!

```bash
$ redis-server /home/bpdp/software/postdoc-ugm/redis-6.2.6/redis.conf
5946:C 21 Oct 2021 16:51:57.090 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
5946:C 21 Oct 2021 16:51:57.090 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=5946, just started
5946:C 21 Oct 2021 16:51:57.090 # Configuration loaded
5946:M 21 Oct 2021 16:51:57.091 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.6 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                  
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 5946
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           https://redis.io       
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

5946:M 21 Oct 2021 16:51:57.092 # Server initialized
5946:M 21 Oct 2021 16:51:57.094 * <graph> Starting up RedisGraph version 2.4.11.
5946:M 21 Oct 2021 16:51:57.095 * <graph> Thread pool created, using 8 threads.
5946:M 21 Oct 2021 16:51:57.095 * <graph> Maximum number of OpenMP threads set to 8
5946:M 21 Oct 2021 16:51:57.095 * Module 'graph' loaded from /home/bpdp/software/postdoc-ugm/redis/modules/redisgraph.so
5946:M 21 Oct 2021 16:51:57.095 * Ready to accept connections
```

Let's try some `Cypher` query from `redis-cli` (query was taken from RedisGraph example):

```bash
$ redis-cli
127.0.0.1:6379> GRAPH.QUERY MotoGP "CREATE (:Rider {name:'Valentino Rossi'})-[:rides]->(:Team {name:'Yamaha'}), (:Rider {name:'Dani Pedrosa'})-[:rides]->(:Team {name:'Honda'}), (:Rider {name:'Andrea Dovizioso'})-[:rides]->(:Team {name:'Ducati'})"
1) 1) "Labels added: 2"
   2) "Nodes created: 6"
   3) "Properties set: 6"
   4) "Relationships created: 3"
   5) "Cached execution: 0"
   6) "Query internal execution time: 61.852344 milliseconds"
127.0.0.1:6379> GRAPH.QUERY MotoGP "MATCH (r:Rider)-[:rides]->(t:Team) WHERE t.name = 'Yamaha' RETURN r.name, t.name"
1) 1) r.name
   2) t.name
2) 1) 1) Valentino Rossi
      2) Yamaha
3) 1) "Cached execution: 0"
   2) "Query internal execution time: 55.436734 milliseconds"
```

We are all set! When we close Redis server, the graph will persist. Happy hacking!.
