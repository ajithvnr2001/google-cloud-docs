---
url: https://docs.cloud.google.com/memorystore/docs/valkey/supported-commands/
title: Supported and blocked commands \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:17.023460+00:00
---

# Supported and blocked commands  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/supported-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Supported and blocked commands Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the commands from the [official Valkey command library](https://valkey.io/commands/) that Memorystore for Valkey supports and the commands that it blocks.

## Supported commands

### Commands supported for Cluster Mode Enabled and Cluster Mode Disabled instances

Memorystore for Valkey supports the following commands for [Cluster Mode Enabled and Cluster Mode Disabled](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled) instances:

  * APPEND
  * AUTH
  * BITCOUNT
  * BITFIELD
  * BITFIELD_RO
  * BITOP
  * BITPOS
  * BLMOVE
  * BLMPOP
  * BLPOP
  * BRPOP
  * BRPOPLPUSH
  * BZMPOP
  * BZPOPMAX
  * BZPOPMIN
  * CLIENT | CACHING
  * CLIENT | GETNAME
  * CLIENT | GETREDIR
  * CLIENT | HELP
  * CLIENT | ID
  * CLIENT | INFO
  * CLIENT | KILL
  * CLIENT | LIST
  * CLIENT | REPLY
  * CLIENT | SETNAME
  * CLIENT | TRACKING
  * CLIENT | TRACKINGINFO
  * COMMAND | COUNT
  * COMMAND | DOCS
  * COMMAND | GETKEYS
  * COMMAND | GETKEYSANDFLAGS
  * COMMAND | HELP
  * COMMAND | INFO
  * COMMAND | LIST
  * CONFIG | HELP
  * COPY
  * DBSIZE
  * DECR
  * DECRBY
  * DEL
  * DISCARD
  * DUMP
  * ECHO
  * EVAL
  * EVAL_RO
  * EVALSHA
  * EVALSHA_RO
  * EXEC
  * EXISTS
  * EXPIRE
  * EXPIREAT
  * EXPIRETIME
  * FCALL
  * FCALL_RO
  * FLUSHALL
  * FLUSHDB
  * FUNCTION | DELETE
  * FUNCTION | DUMP
  * FUNCTION | FLUSH
  * FUNCTION | HELP
  * FUNCTION | KILL
  * FUNCTION | LIST
  * FUNCTION | LOAD
  * FUNCTION | RESTORE
  * FUNCTION | STATS
  * GEOADD
  * GEODIST
  * GEOHASH
  * GEOPOS
  * GEORADIUS
  * GEORADIUS_RO
  * GEORADIUSBYMEMBER
  * GEORADIUSBYMEMBER_RO
  * GEOSEARCH
  * GEOSEARCHSTORE
  * GET
  * GETBIT
  * GETDEL
  * GETEX
  * GETRANGE
  * GETSET
  * HDEL
  * HELLO
  * HEXISTS
  * HGET
  * HGETALL
  * HINCRBY
  * HINCRBYFLOAT
  * HKEYS
  * HLEN
  * HMGET
  * HMSET
  * HRANDFIELD
  * HSCAN
  * HSET
  * HSETNX
  * HSTRLEN
  * HVALS
  * INCR
  * INCRBY
  * INCRBYFLOAT
  * INFO
  * KEYS
  * LATENCY | DOCTOR
  * LATENCY | GRAPH
  * LATENCY | HELP
  * LATENCY | HISTOGRAM
  * LATENCY | HISTORY
  * LATENCY | LATEST
  * LATENCY | RESET
  * LCS
  * LINDEX
  * LINSERT
  * LLEN
  * LMOVE
  * LMPOP
  * LOLWUT
  * LPOP
  * LPOS
  * LPUSH
  * LPUSHX
  * LRANGE
  * LREM
  * LSET
  * LTRIM
  * MEMORY | DOCTOR
  * MEMORY | HELP
  * MEMORY | MALLOC-STATS
  * MEMORY | PURGE
  * MEMORY | STATS
  * MEMORY | USAGE
  * MGET
  * MODULE | HELP
  * MONITOR
  * MSET
  * MSETNX
  * MULTI
  * OBJECT | ENCODING
  * OBJECT | FREQ
  * OBJECT | HELP
  * OBJECT | IDLETIME
  * OBJECT | REFCOUNT
  * PERSIST
  * PEXPIRE
  * PEXPIREAT
  * PEXPIRETIME
  * PFADD
  * PFCOUNT
  * PFMERGE
  * PING
  * PSETEX
  * PSUBSCRIBE
  * PTTL
  * PUBLISH
  * PUBSUB|CHANNELS
  * PUBSUB | HELP
  * PUBSUB|NUMPAT
  * PUBSUB|NUMSUB
  * PUBSUB | SHARDCHANNELS
  * PUBSUB | SHARDNUMSUB
  * PUNSUBSCRIBE
  * QUIT
  * RANDOMKEY
  * RENAME
  * RENAMENX
  * RESET
  * RESTORE
  * ROLE
  * RPOP
  * RPOPLPUSH
  * RPUSH
  * RPUSHX
  * SADD
  * SCAN
  * SCARD
  * SCRIPT | DEBUG
  * SCRIPT | EXISTS
  * SCRIPT | FLUSH
  * SCRIPT | HELP
  * SCRIPT | KILL
  * SCRIPT | LOAD
  * SDIFF
  * SDIFFSTORE
  * SELECT
  * SET
  * SETBIT
  * SETEX
  * SETNX
  * SETRANGE
  * SINTER
  * SINTERCARD
  * SINTERSTORE
  * SISMEMBER
  * SLOWLOG|HELP
  * SMEMBERS
  * SMISMEMBER
  * SMOVE
  * SORT
  * SORT_RO
  * SPOP
  * SPUBLISH
  * SRANDMEMBER
  * SREM
  * SSCAN
  * SSUBSCRIBE
  * STRLEN
  * SUBSCRIBE
  * SUBSTR
  * SUNION
  * SUNIONSTORE
  * SUNSUBSCRIBE
  * TIME
  * TOUCH
  * TTL
  * TYPE
  * UNLINK
  * UNSUBSCRIBE
  * UNWATCH
  * WAIT
  * WATCH
  * XACK
  * XADD
  * XAUTOCLAIM
  * XCLAIM
  * XDEL
  * XGROUP | CREATE
  * XGROUP | CREATECONSUMER
  * XGROUP | DELCONSUMER
  * XGROUP | DESTROY
  * XGROUP | HELP
  * XGROUP | SETID
  * XINFO | CONSUMERS
  * XINFO | GROUPS
  * XINFO | HELP
  * XINFO | STREAM
  * XLEN
  * XPENDING
  * XRANGE
  * XREAD
  * XREADGROUP
  * XREVRANGE
  * XTRIM
  * ZADD
  * ZCARD
  * ZCOUNT
  * ZDIFF
  * ZDIFFSTORE
  * ZINCRBY
  * ZINTER
  * ZINTERCARD
  * ZINTERSTORE
  * ZLEXCOUNT
  * ZMPOP
  * ZMSCORE
  * ZPOPMAX
  * ZPOPMIN
  * ZRANDMEMBER
  * ZRANGE
  * ZRANGEBYLEX
  * ZRANGEBYSCORE
  * ZRANGESTORE
  * ZRANK
  * ZREM
  * ZREMRANGEBYLEX
  * ZREMRANGEBYRANK
  * ZREMRANGEBYSCORE
  * ZREVRANGE
  * ZREVRANGEBYLEX
  * ZREVRANGEBYSCORE
  * ZREVRANK
  * ZSCAN
  * ZSCORE
  * ZUNION
  * ZUNIONSTORE



### Additional commands supported for Cluster Mode Enabled instances

Memorystore for Valkey also supports the following commands for [Cluster Mode Enabled](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled) instances:

  * ASKING
  * CLUSTER | COUNT-FAILURE-REPORTS
  * CLUSTER | COUNTKEYSINSLOT
  * CLUSTER | GETKEYSINSLOT
  * CLUSTER | HELP
  * CLUSTER | INFO
  * CLUSTER | KEYSLOT
  * CLUSTER | LINKS
  * CLUSTER | MYID
  * CLUSTER | NODES
  * CLUSTER | REPLICAS
  * CLUSTER | SHARDS
  * CLUSTER | SLOTS
  * READONLY
  * READWRITE



## Blocked commands

Memorystore for Valkey supports all Valkey 7.2 commands, except for the commands that are listed in this section. For these blocked commands, Memorystore for Valkey returns a `NOPERM` error.

  * ACL | DELUSER
  * ACL | DRYRUN
  * ACL | GETUSER
  * ACL | LIST
  * ACL | LOAD
  * ACL | LOG
  * ACL | SAVE
  * ACL | SETUSER
  * ACL | USERS
  * ACL | CAT
  * ACL | GENPASS
  * ACL | HELP
  * ACL | WHOAMI
  * BGREWRITEAOF
  * BGSAVE
  * CLIENT | NO-EVICT
  * CLIENT | PAUSE
  * CLIENT | UNBLOCK
  * CLIENT | UNPAUSE
  * CLUSTER | ADDSLOTS
  * CLUSTER | ADDSLOTSRANGE
  * CLUSTER | BUMPEPOCH
  * CLUSTER | DELSLOTS
  * CLUSTER | DELSLOTSRANGE
  * CLUSTER | FAILOVER
  * CLUSTER | FLUSHSLOTS
  * CLUSTER | FORGET
  * CLUSTER | MEET
  * CLUSTER | REPLICATE
  * CLUSTER | RESET
  * CLUSTER | SAVECONFIG
  * CLUSTER | SET-CONFIG-EPOCH
  * CLUSTER | SETSLOT
  * CONFIG | GET
  * CONFIG | RESETSTAT
  * CONFIG | REWRITE
  * CONFIG | SET
  * DEBUG
  * FAILOVER
  * LASTSAVE
  * MIGRATE
  * MODULE | LIST
  * MODULE | LOAD
  * MODULE | LOADEX
  * MODULE | UNLOAD
  * MOVE
  * PFDEBUG
  * PFSELFTEST
  * PSYNC
  * REPLCONF
  * REPLICAOF
  * RESTORE-ASKING
  * SAVE
  * SHUTDOWN
  * SLAVEOF
  * SLOWLOG | GET
  * SLOWLOG | LEN
  * SLOWLOG | RESET
  * SWAPDB
  * SYNC
  * XSETID



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
