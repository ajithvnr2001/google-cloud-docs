---
url: https://docs.cloud.google.com/memorystore/docs/redis/supported-commands/
title: Supported and blocked commands \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:59.055559+00:00
---

# Supported and blocked commands  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/supported-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Supported and blocked commands Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the commands from the [official Redis command library](https://redis.io/commands/) that Memorystore for Redis supports and the commands that it blocks.

## Supported commands

Memorystore for Redis supports the following commands:

  * APPEND
  * ASKING
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

**Note** : The `LATENCY` command group isn't blocked. However, Memorystore for Redis doesn't support setting the `latency-monitor-threshold` parameter. Therefore, the `LATENCY` commands don't return relevant information for this parameter.
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

  * READONLY

  * READWRITE

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

  * SLOWLOG | GET

  * SLOWLOG | HELP

  * SLOWLOG | LEN

  * SLOWLOG | RESET

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




## Blocked commands

Memorystore for Redis supports all Redis 7.2 commands, except for the commands that are listed in this section. For these blocked commands, Memorystore for Redis returns a `NOPERM` error.

  * ACL | CAT
  * ACL | DELUSER
  * ACL | GENPASS
  * ACL | GETUSER
  * ACL | HELP
  * ACL | LIST
  * ACL | LOAD
  * ACL | LOG
  * ACL | SAVE
  * ACL | SETUSER
  * ACL | USERS
  * ACL | WHOAMI
  * ACL | CAT
  * ACL | GENPASS
  * ACL | HELP
  * ACL | WHOAMI
  * BGREWRITEAOF
  * BGSAVE
  * CLIENT
  * CLUSTER
  * COMMAND
  * CONFIG

**Note** : Memorystore for Redis blocks the `CONFIG` command, which stops you from modifying the `redis.conf` file for your Redis server. However, you can use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to modify a defined set of [supported Redis configurations](https://docs.cloud.google.com/memorystore/docs/redis/supported-redis-configurations).
  * DEBUG

  * LASTSAVE

  * MIGRATE

  * OBJECT

  * REPLICAOF

  * SAVE

  * SHUTDOWN




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
