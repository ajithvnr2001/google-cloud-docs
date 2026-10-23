---
url: https://docs.cloud.google.com/memorystore/docs/cluster/client-library-code-samples/
title: Client library code samples \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:20.508248+00:00
---

# Client library code samples  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/client-library-code-samples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Client library code samples Stay organized with collections  Save and categorize content based on your preferences. 

This page provides examples of Memorystore for Redis Cluster configurations for different client libraries.

## Lettuce

We recommend using [Lettuce](https://lettuce.io/), versions 6.2.4 and later.

**Caution** : If you use Lettuce to connect to a cluster in Memorystore for Redis Cluster, then change the `validateClusterNodeMembership` parameter to `false`. Otherwise, when the topology changes, you might get `unknownPartition` errors.

### Lettuce
    
    
    
    // Create RedisURI from the MRC discovery endpoint
    RedisURI redisUri = RedisURI.Builder.redis(CLUSTER_DISC_EP_ADDR, CLUSTER_DISC_EP_PORT).build();
    
    // Configure client' resources
    // Configure reconnectDelay with exponential backoff and full jitter
    ClientResources resources = DefaultClientResources.builder()
                            .reconnectDelay(Delay.fullJitter(
        Duration.ofMillis(100),     // minimum 100 millisecond delay
        Duration.ofSeconds(5),      // maximum 5 second delay
        100, TimeUnit.MILLISECONDS) // 100 millisecond base
    ).build();
    
    // Create a cluster client with the URI and resources
    RedisClusterClient clusterClient = RedisClusterClient.create(resources, redisUri);
    
    // Configure the topology refreshment options
    // Enable periodic cluster topology updates so that the client updates the cluster topology in the intervals of
    // 60 seconds
    // Enable adaptive topology refresh that uses all triggers: MOVED_REDIRECT, ASK_REDIRECT,
    // PERSISTENT_RECONNECTS, UNCOVERED_SLOT, UNKNOWN_NODE
    // By enabling dynamicRefreshSources, the Lettuce client can query other healthy, discovered
    // nodes for topology updates if the main discovery endpoint is temporarily unavailable. This
    // prevents client-side topology desynchronization and reconnection loops during maintenance
    // events such as rolling OS upgrades where the discovery endpoint might be rotated.
    // Enable closing stale connections when refreshing the cluster topology. This reduces the need to handle
    // failed connections during command runtime.
    ClusterTopologyRefreshOptions topologyRefreshOptions = ClusterTopologyRefreshOptions.builder()
                                    .enablePeriodicRefresh(1, TimeUnit.MINUTES)
                                    .enableAllAdaptiveRefreshTriggers()
                                    .dynamicRefreshSources(true)
                                    .closeStaleConnections(true)
                                    .build();
    
    // Configure the socket options
    // Set connectTimeout based on your application requirements and workload
    // Enable TCP keepAlive to reduce the need to handle failed connections during command runtime
    SocketOptions socketOptions = SocketOptions.builder()
        .connectTimeout(CONNECT_TIMEOUT)
        .keepAlive(true)
        .build();
    
    // Configure the client options
    // Enable AutoReconnect when connection is lost
    // Set nodeFilter to filter out failed nodes from the topology
    // Disable validateClusterNodeMembership to allow redirecting commands to newly added nodes
    
    clusterClient.setOptions(ClusterClientOptions.builder()
                                    .topologyRefreshOptions(topologyRefreshOptions)
                .socketOptions(socketOptions)
                                    .autoReconnect(true)
                                    .nodeFilter(it ->
                                        ! (it.is(RedisClusterNode.NodeFlag.FAIL)
                                        || it.is(RedisClusterNode.NodeFlag.EVENTUAL_FAIL)
                                        || it.is(RedisClusterNode.NodeFlag.NOADDR)))
                                    .validateClusterNodeMembership(false)
                                    .build());
    
    // Create a connection pool
    GenericObjectPool<StatefulRedisClusterConnection<String, String> pool = ConnectionPoolSupport.createGenericObjectPool(() -> clusterClient.connect(), new GenericObjectPoolConfig());
    pool.setMaxTotal(MAX_CONNECTIONS_IN_CONNECTION_POOL);
    
    // Get a connection from the connection pool
    StatefulRedisClusterConnection<String, String> connection = pool.borrowObject();
    
    // Get a cluster sync command and call 'set'
    RedisAdvancedClusterCommands<String, String> syncCommands = connection.sync();
    syncCommands.set(key, value);
    
    

## redis-py

We recommend using [redis-py](https://github.com/redis/redis-py), versions 5.1 and later.

### redis-py
    
    
    
    // Create a cluster client. A connection pool is used internally.
    cluster_client = redis.RedisCluster(
            host=CLUSTER_DISC_EP_ADDR,
            port=CLUSTER_DISC_EP_PORT,
            retry=Retry(EqualJitterBackoff(), 3))
    
    cluster_client.set('key', 'value')
    
    

## PHPRedis

We recommend using [PHPRedis](https://github.com/phpredis/phpredis), versions 5.0.0 and later.

### PHPRedis
    
    
    
    // In redis.ini
    redis.clusters.seeds = "cluster[]=CLUSTER_DISC_EP_ADDR:CLUSTER_DISC_EP_PORT"
    redis.clusters.cache_slots = "cluster=1"
    redis.clusters.persistent = "cluster=1"
    
    $cluster = new RedisCluster('cluster');
    $cluster->set("key", "value");
    
    

## Redisson

We recommend using [Redisson](https://redisson.org/), versions 3.20.1 and later.

### Redisson
    
    
    
    Config config = new Config();
    ClusterServersConfig clusterConfig = config.useClusterServers()
              .addNodeAddress("redis://CLUSTER_DISC_EP_ADDR:CLUSTER_DISC_EP_PORT")
              .setScanInterval(60000)  // cluster topology periodic refresh
              .setMasterConnectionMinimumIdleSize(1)
              .setMasterConnectionPoolSize(10)
              .setSlaveConnectionMinimumIdleSize(1)
              .setSlaveConnectionPoolSize(10)
              .setIdleConnectionTimeout(60000)
              .setPingConnectionInterval(0)
              .setKeepAlive(true)
              .setTcpNoDelay(true)
    
    RedissonClient redisson = Redisson.create(config);
    RBucket<String> bucket = redisson.getBucket("key");
    bucket.set("value");
    
    

## go-redis

We recommend using [go-redis](https://github.com/redis/go-redis), versions 9.11.0 and later.

### go-redis
    
    
    
    import (
      "context"
      "time"
    
      "github.com/redis/go-redis/v9"
    )
    
    clusterClient = redis.NewClusterClient(&redis.ClusterOptions{
        Addrs:        []string{"CLUSTER_DISC_EP_ADDR:CLUSTER_DISC_EP_PORT"},
        // PoolSize applies per cluster node and not for the whole cluster.
        PoolSize:        10,
        ConnMaxIdleTime: 60 * time.Second,
        MinIdleConns: 1,
    })
    
    ctx := context.Background()
    
    err := clusterClient.Set(ctx, "key", "value", 0).Err()
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
