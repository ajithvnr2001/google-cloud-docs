---
url: https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey/
title: Migrate from Memorystore for Memcached to Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:52.046110+00:00
---

# Migrate from Memorystore for Memcached to Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/memcached/resources)



Send feedback 

#  Migrate from Memorystore for Memcached to Memorystore for Valkey Stay organized with collections  Save and categorize content based on your preferences. 

We recommend that you migrate your Memorystore for Memcached workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey). Memorystore for Memcached is a key-value datastore, but Memorystore for Valkey is a more feature-rich data structure server.

Memorystore for Valkey provides you with similar functionality to Memorystore for Memcached. In addition, Memorystore for Valkey has the following benefits:

  * It offers a fully managed, high-performance, in-memory datastore for Valkey, a Redis-compatible, open-source project.
  * It's a fully managed Valkey service for Google Cloud, which supports both Cluster Mode Enabled and Cluster Mode Disabled instances.
  * Your applications that run on Google Cloud can achieve extreme performance by leveraging the highly scalable, available, secure Valkey service without the burden of managing complex Valkey deployments.



## Memorystore for Valkey features

Migrating to Memorystore for Valkey provides you with access to features that aren't available in Memorystore for Memcached. These features provide you with better application development, reliability, and performance.

The following table lists and describes features that are available in Memorystore for Valkey, and explains the advantages of using these features.

Feature | Description | Advantages  
---|---|---  
Multiple databases | Memorystore for Memcached is a single, flat keyspace. However, by default, the [Cluster Mode Disabled](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled) mode of Memorystore for Valkey supports up to 16 databases for an instance. You can configure your environment so that you can have up to 100 databases for an instance. | Having multiple databases for an instance prevents a single point of failure for the instance, lets you backup or restore a single database without impacting the availability or consistency of other databases, and lets you scale or migrate your databases more efficiently.  
Rich data structures | In addition to strings, Memorystore for Valkey supports lists, sets, sorted sets, hashes, and bitmaps. Memorystore for Valkey also supports [Bloom filters](https://docs.cloud.google.com/memorystore/docs/valkey/about-bloom-filters), [vector search](https://docs.cloud.google.com/memorystore/docs/valkey/about-vector-search), and [JSON](https://docs.cloud.google.com/memorystore/docs/valkey/about-json). | You can use Memorystore for Valkey for complex use cases such as leaderboards, task queues, and object caching, without application serialization. You can also use vector search to perform semantic queries at sub-millisecond latencies.  
Transactions | You can use the [`MULTI`](https://valkey.io/commands/multi/) and [`EXEC`](https://valkey.io/commands/exec/) commands to run a group of commands as a single, indivisible unit atomically. | Although you can use the compare-and-swap (CAS) capabilities of Memorystore for Memcached for optimistic locking on a key level, Memorystore for Valkey lets you run a group of commands atomically.   
Pub/Sub messaging | By using [Pub/Sub](https://docs.cloud.google.com/pubsub) with Memorystore for Valkey, your client applications can subscribe to channels and receive real-time messages. | Memorystore for Valkey lets you transform your cache into a lightweight message broker for real-time updates and inter-service communication.  
Lua scripts | You can use [Lua](https://valkey.io/topics/eval-intro/) to run complex application logic atomically on your server by using the [`EVAL`](https://valkey.io/commands/eval/) command.  | Using server-side scripts reduces your network round trips and ensures that Memorystore for Valkey can perform complex operations without interruptions. This boosts your application's performance.  
High-availability, replication, and shard support | Memorystore for Valkey's architecture supports and provides [high availability (HA)](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas). Your client applications can access Memorystore for Valkey nodes directly by connecting to individual endpoints (or shards). | HA and replication enhance your system's reliability and minimize interruptions during critical updates. Using shards helps you distribute the high load of traffic associated with your client applications effectively.  
Persistence | Memorystore for Valkey supports the following types of [persistence](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview):

  * **Append-only file (AOF)** : used for data durability. It stores data durably by recording every write command to a log file called the AOF file. If a system failure or restart occurs, then the server replays AOF file commands sequentially to restore your data.
  * **Redis database (RDB)** : used for data protection. It protects your data by saving snapshots of your data on durable storage. If node failures occur, then you can recover your data.

| By using AOF and RDB persistence, you can store your critical data in Memorystore for Valkey durably. You can recover your data at any time. Memorystore for Valkey handles the underlying persistence mechanism so there's little ramp-up to using persistence.  
  
## Migrate your workloads

To migrate your Memorystore for Memcached workloads to Memorystore for Valkey, you must complete the following actions:

  1. **Modify your client libraries**: change the client libraries for your applications from Memcached libraries to Valkey libraries.
  2. **Modify your commands**: replace all commands for the Memcached API for your client applications with the corresponding commands for the Valkey API.
  3. **Deploy and verify the migration**: set up the migration and confirm that you can use it to migrate your workloads to Memorystore for Valkey.



### Modify your client libraries

In this section, you change the client libraries for your applications from Memcached libraries to Valkey libraries.

The following table lists examples of Memcached client libraries for Python, Java, Go, and Node.js, and the corresponding libraries for Valkey.

Language | Memcached client library | Valkey client library  
---|---|---  
Python | [python-memcached](https://pypi.org/project/python-memcached/), [pymemcache](https://pypi.org/project/pymemcache/) | [valkey-py](https://valkey-py.readthedocs.io/en/latest/)  
Java | [spymemcached](https://github.com/couchbase/spymemcached) | [Valkey GLIDE](https://glide.valkey.io/), [valkey-java](https://github.com/valkey-io/valkey-java)  
Go | [gomemcache](https://github.com/bradfitz/gomemcache) | [Valkey GLIDE](https://glide.valkey.io/), [valkey-go](https://github.com/valkey-io/valkey-go)  
Node.js | [memjs](https://www.npmjs.com/package/memjs) | [Valkey GLIDE](https://glide.valkey.io/), [ioredis](https://www.npmjs.com/package/ioredis)  
  
**Note** : We don't endorse any specific client libraries for Memcached or Valkey. We recommend that you evaluate and select your libraries based on your specific requirements.

To access code samples that use client libraries for Valkey, see [Client library code samples](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples).

### Modify your commands

In this section, you replace all commands for the Memcached API for your client applications with the corresponding commands for the Valkey API.

To modify your commands, you must complete the following actions:

  1. **Modify your connection setup**: change the connection of your client applications from the Memcached server to the Valkey server.
  2. **Modify the commands**: replace all Memcached API commands with the corresponding commands for the Valkey API.

**Note:** For the Valkey commands in this section, we use the [valkey-py](https://valkey-py.readthedocs.io/en/latest/) client library. However, we don't endorse this library. Also, for more information about these commands, see [Valkey commands](https://valkey-py.readthedocs.io/en/stable/commands.html).

#### Modify your connection setup

In this section, you change the connection of your client applications from the Memcached server to the Valkey server.

  1. Find the code that you use to connect your client applications to the Memcached server. This might be similar to the following code:
         
         import memcache;
         mc = memcache.Client(['MEMCACHED_IP_ADDRESS:11211'])
         

Replace MEMCACHED_IP_ADDRESS with the IP address of your Memorystore for Memcached instance.

  2. Modify this code so that your client applications can connect to the Valkey server. This might be similar to the following code:
         
         import valkey;
         v = valkey.Valkey(host=VALKEY_IP_ADDRESS, port=6379, db=0)
         

Replace VALKEY_IP_ADDRESS with the IP address of the Memorystore for Valkey instance that you create when you deploy and verify the migration.




#### Modify the commands

In this section, you replace all Memcached API commands for your client applications with the corresponding commands for the Valkey API.

##### DECR

The `DECR` command lets you decrement the value that's stored at a key by an amount.

  1. Find the code that you use in Memcached for the `DECR` command. This might be similar to the following code:
         
         mc.DECR('KEY_NAME', AMOUNT)
         

Make the following replacements:

     * KEY_NAME: the name of the key.
     * AMOUNT: the value by which you want to decrement the number that's stored at the key. This value must be an integer.
  2. Modify this code so that you can use it with Valkey. Your modifications might be similar to the following code:
         
         v.DECR('KEY_NAME', AMOUNT)
         




##### DELETE

The `DELETE` command lets you remove a key. For example, you can delete a user.

  1. Find the code that you use in Memcached for the `DELETE` command. This might be similar to the following code:
         
         mc.DELETE('USERNAME')
         

Replace USERNAME with the name of the user that you want to delete.

  2. Modify this code so that you can use it with Valkey. Your modifications might be similar to the following code:
         
         v.DELETE('USERNAME')
         




##### GET

The `GET` command lets you retrieve a value that's associated with a key. For example, you can get information about a user.

  1. Find the code that you use in Memcached for the `GET` command. This might be similar to the following code:
         
         data = mc.GET('USERNAME')
         

Replace USERNAME with the name of the user about which you want to get information.

  2. Modify this code so that you can use it with Valkey. Your modifications might be similar to the following code:
         
         data = v.GET('USERNAME')
         




##### INCR

The `INCR` command lets you increment the value that's stored at a key by an amount.

  1. Find the code that you use in Memcached for the `INCR` command. This might be similar to the following code:
         
         mc.INCR('KEY_NAME', AMOUNT)
         

Make the following replacements:

     * KEY_NAME: the name of the key.
     * AMOUNT: the value by which you want to increment the number that's stored at the key. This value must be an integer.
  2. Modify this code so that you can use it with Valkey. Your modifications might be similar to the following code:
         
         v.INCR('KEY_NAME', AMOUNT)
         




##### MGET

The `MGET` command lets you retrieve values for multiple keys in a single command. Using `MGET` improves the performance of your environment.

  1. Find the code that you use in Memcached for the `MGET` command. This might be similar to the following code:
         
         data_map = mc.get_multi(['KEY_NAME_1', 'KEY_NAME_2'])
         

Replace KEY_NAME_1 and KEY_NAME_2 with the names of the keys about which you want to retrieve information.

  2. Modify this code so that you can use it with Valkey. Your modifications might be similar to the following code:
         
         data_list = v.MGET(['KEY_NAME_1', 'KEY_NAME_2'])
         




##### SET

The `SET` command lets you specify a value for a key. For example, you can set an expiration time for a user that accesses a system (in seconds).

  1. Find the code that you use in Memcached for the `SET` command. This might be similar to the following code:
         
         mc.SET('USERNAME', 'data', time=EXPIRATION_TIME)
         

Make the following replacements:

     * USERNAME: the name of the user that's accessing the system
     * EXPIRATION_TIME: the number of seconds that the user has until the user can no longer access the system
  2. Modify this code so that you can use it with Valkey. Your modifications might be similar to the following code:
         
         v.SET('USERNAME', 'data', ex=EXPIRATION_TIME)
         




### Deploy and verify the migration

In this section, you set up the migration and confirm that you can use it to migrate your workloads to Memorystore for Valkey.

To deploy and verify the migration, complete the following steps:

  1. **Create a Memorystore for Valkey instance** : make sure that the instance that you [create](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances) has a similar size to your Memorystore for Memcached instance. Also, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to [monitor the usage](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics) of the Memorystore for Valkey instance.
  2. **Write to both instances** : for a zero-downtime migration, modify your applications to write to both instances. This populates the Valkey cache and lets you benchmark key monitoring metrics.
  3. **Stop traffic to the Memorystore for Memcached instance** : change the configuration of your applications so that read operations point to the IP address and port number (6379) of the Memorystore for Valkey instance.
  4. **Monitor your applications** : [monitor](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances) the error rates and latencies of your applications.
  5. **Delete the Memorystore for Memcached instance** : stop writing to the Memorystore for Memcached instance, and then [delete](https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances) the instance.



## FAQ

This section contains frequently asked questions (FAQs) about migrating your Memorystore for Memcached workloads to Memorystore for Valkey.

### Why are you migrating to Memorystore for Valkey?

Valkey is a high-performance, open-source project fork of the Redis codebase. Memorystore for Valkey provides a managed service that's compatible with the Redis protocol. This ensures that all existing Redis client libraries and commands work seamlessly. Migrating to Memorystore for Valkey is functionally equivalent to migrating to a standard, Redis-compatible server.

### Do you have to reconfigure your network firewall rules?

Memorystore for Memcached instances typically use port **11211** whereas Memorystore for Valkey instances use port **6379**. You must ensure that your Virtual Private Cloud (VPC) firewall rules allow egress traffic from your applications to the Memorystore for Valkey instances on the correct port.

**Note:** If you created a Cluster Mode Enabled instance when you deployed and verified the migration, then your instance requires additional ports. For more information, see [Which ports do you need to set up networking in Memorystore for Valkey?](https://docs.cloud.google.com/memorystore/docs/valkey/networking#ports).

### How does Valkey handle the serialization of complex objects?

Because Memcached doesn't know the structure of complex objects, such as Python objects or Java objects, it treats all objects as opaque blobs.

As a result, before any data hits the network, serialization happens entirely on the side of the client applications. The server sees only byte arrays. For example, to read a single property such as a user's email address, you must retrieve the entire serialized object, deserialize it in your applications, and then read the field associated with the property.

Valkey can store blobs and understand the structure of the complex objects. You can also use Valkey to expand an object's fields into a Valkey hash table. You can use this table to retrieve deep-nested values directly.

The following example uses a Valkey hash table to retrieve a user's email address:
    
    
    # valkey-py
    client.hset("user:101", mapping={
        "name": "username",
        "email": "username@example.com",
        "login_count": 10
    })
    client.hget("user:101", "email") # -> b"username@example.com"
    

### How do communication protocols differ between Memcached and Valkey?

Memcached uses an ASCII protocol and an optional binary protocol. Valkey uses the Redis Serialization Protocol (RESP).

Although these are different protocols, modern Valkey client application libraries handle the RESP protocol automatically. This makes the difference between the protocols transparent to the application code.

### After you migrate to Memorystore for Valkey, how do you map the `flags` field?

Memorystore for Memcached supports the `flags` field. This field contains a 32-bit unsigned integer that client application libraries use to store metadata about stored values.

Memorystore for Valkey doesn't support this field. To map the `flags` field to Memorystore for Valkey, complete the following steps:

  1. Serialize the flags into the key name of a string object.
  2. Serialize the flags into the value of a string object.
  3. Use a hash object with a designated field for flags.



### Does Memorystore for Valkey offer better performance?

In most scenarios, performance is better in Memorystore for Valkey. This is due to Valkey's advanced data structures, persistent connections, pipelining support, and improved efficiency for multi-key operations. However, you must modify your client libraries and commands correctly.

**Note:** For more information about configuring Memorystore for Valkey for optimal performance, see [Best practices for Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices).

### If your Memorystore for Memcached instances use multiple nodes, then what do you do in Memorystore for Valkey?

When you deploy and verify your migration, create Cluster Mode Enabled instances in Memorystore for Valkey. These instances handle sharding and high availability internally, and appear as single endpoints to your applications. This simplifies the client-side logic of your applications.

### If your Memorystore for Memcached instances use multiple nodes, then which node type do we recommend for your Memorystore for Valkey instances?

For each of your Memorystore for Memcached instances, to determine its node size, check the value that's associated with the [**Memory per node**](https://docs.cloud.google.com/memorystore/docs/memcached/instance-node-properties) property. Then, to determine the node type for your corresponding Memorystore for Valkey instances, use the following table:

Memorystore for Memcached node size | Memorystore for Valkey node type | Total node capacity | vCPU count  
---|---|---|---  
< 1 GB | shared-core-nano | 1.4 GB | 0.5 (Shared)  
1 GB – 5 GB | standard-small | 6.5 GB | 2  
6 GB – 12 GB | highmem-medium | 13.0 GB | 2  
13 GB – 50 GB | highmem-xlarge | 58.0 GB | 8  
  
The `shared-core-nano` node type is for small workloads. This node type provides variable [performance](https://docs.cloud.google.com/compute/docs/general-purpose-machines#sharedcore) and doesn't have an SLA, making it unsuitable for production workloads.

The more virtual CPUs (vCPUs) that you select for your Memorystore for Valkey instance, the better the performance. If your instance runs resource-intensive workloads, then select a node type with a higher vCPU (for example, `highmem-xlarge`). If your instance performs less-demanding tasks, then select a node type with a lower vCPU (for example, `highmem-medium`).

**Note:** For more information about the Memorystore for Valkey node types, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
