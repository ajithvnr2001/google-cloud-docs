---
url: https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices/
title: Best practices for Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:56.283388+00:00
---

# Best practices for Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Best practices for Memorystore for Redis Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on optimally using Memorystore for Redis. This page also points out potential issues to avoid.

For a list of troubleshooting scenarios, see [Troubleshooting](https://docs.cloud.google.com/memorystore/docs/redis/troubleshooting).

## High availability and data durability best practices

We recommend using the Standard Tier as the primary mechanism for high availability (HA). The Standard Tier provides a highly available instance with multiple replicas, and enables fast recovery using automatic failover if the primary fails. Additionally, enabling RDB snapshots on Standard Tier instances provides extra protection from node failures.

In some scenarios, you might also want to ensure that you can recover data from snapshot backups. In these scenarios, backups and the ability to restore data from RDB snapshots can provide additional protection from data loss.

If you enable RDB snapshots and need to recover your data, then Memorystore for Redis can do this from the latest snapshot. These snapshots are for internal system recovery only and you can't access them.

### Durability limitations and best practices

Although the Standard Tier provides HA through replication and automatic failover, HA doesn't guarantee full data durability. Memorystore for Redis can't provide full data durability even with HA enabled during certain catastrophic events, such as temporary regional failures.

To help protect your data and provide a baseline level of persistence, RDB snapshots are enabled by default when you create a Memorystore for Redis instance using the Google Cloud console.

For production workloads, consider the following best practices to further improve your data resilience:

  * **Disaster recovery** : Memorystore for Redis doesn't support cross-region replication. If your disaster recovery strategy requires cross-region replication for true regional resilience, then we recommend using a Memorystore for Valkey instance. For more information about configuring and managing secondary instances across regions, see [Work with cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication) in the _Memorystore for Valkey_ documentation.
  * **Maximum durability** : if your application requires the highest possible level of data durability, then we recommend using a Memorystore for Valkey instance configured with cross-region replication, automated daily backups, and Append-Only File (AOF) persistence. This combination provides the most robust protection against data loss. For more information, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview) in the _Memorystore for Valkey_ documentation.



## Capacity planning best practices

To ensure that you can successfully provision resources and build resilient architectures, we recommend the following capacity planning best practices:

  * **Deploy across multiple locations** : if you can't create an instance in your preferred zone because of temporary resource constraints, then try creating the instance either in a different zone within the same region or in a different region.
  * **Use cross-region access** : configure your clients to access your instances that are located in different regions. If you need to provision an instance that's in a different region because of local resource constraints, then your clients can connect to the instance.
  * **Choose a different capacity tier** : if you encounter resource constraints because of the size of an instance, then either select a different capacity tier or resize the instance. For more information, see [Capacity tier performance](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview#capacity_tier_performance).



## RDB exporting

When exporting a RDB backup use the following guidance:

  * [Export during a period of low write-rate](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview#exporting_under_high_write_load).
  * If exporting during a period of high write-rate, [temporarily lower `maxmemory` config to 50%](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#export_operation) of the instance capacity to provide sufficient overhead for a successful operation.



## Resource-intensive operations

For Standard Tier Redis instances, the following operations use extra memory for the duration of the operation:

  * [Version upgrade](https://docs.cloud.google.com/memorystore/docs/redis/version-upgrade-behavior)
  * [Scaling up/down](https://docs.cloud.google.com/memorystore/docs/redis/scaling-instances)
  * [Manual failover](https://docs.cloud.google.com/memorystore/docs/redis/manual-failover-overview)
  * [Import / export](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview)



Version upgrade, scaling, and manual failover use extra memory (for Standard Tier instances) due to replication. These operations follow the replication process described in [Standard Tier instance upgrade behavior](https://docs.cloud.google.com/memorystore/docs/redis/version-upgrade-behavior#standard_tier_instance_upgrade_behavior).

Import and export operations require extra memory because of the forked Redis process and copy-on-write data management associated with these operations.

In order to mitigate the drawbacks of resource-intensive operations, you should:

  * Lower the [maxmemory](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#maxmemory_configuration) config to 80% of the instance capacity for the duration of the operation. This provides sufficient overhead for a successful operation.
  * [Monitor the system memory usage ratio metric](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio), and ensure that this metric is under 80% before running one of these operations.
  * Run these operations during periods of low instance traffic (such as overnight or over the weekend).
  * [Have retry logic with exponential backoff](https://docs.cloud.google.com/memorystore/docs/redis/high-availability#retrying_the_instance_connection_after_failover) in place before running these operations.



## Operations and scenarios that require a connection retry

The following operations and scenarios break the network connection between your network and the Redis instance:

  * [Version upgrade](https://docs.cloud.google.com/memorystore/docs/redis/version-upgrade-behavior)
  * [Scaling up/down](https://docs.cloud.google.com/memorystore/docs/redis/scaling-instances)
  * [Importing](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview)
  * [Manual failover](https://docs.cloud.google.com/memorystore/docs/redis/manual-failover-overview)
  * [System maintenance](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy)
  * [Certificate Authority rotation](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption#certificate_authority_rotation) for Redis instances that have [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption) enabled
  * Emergency failover



These operations modify your instance, requiring a temporary connection break. You need to [have retry logic with exponential backoff](https://docs.cloud.google.com/memorystore/docs/redis/high-availability#retrying_the_instance_connection_after_failover) in place before running these operations so that your application automatically reconnects and continues to function normally.

## Routine maintenance

Memorystore for Redis instances undergo maintenance periodically. For more details, see the Memorystore for Redis [maintenance policy](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy).

Implement the following best practices so you are prepared for routine maintenance:

  * [Set a maintenance window](https://docs.cloud.google.com/memorystore/docs/redis/managing-maintenance-updates#setting_a_maintenance_window) for when maintenance updates can occur. 
    * Schedule maintenance windows for times of low instance traffic and sufficient memory overhead. For more information, see [Impacts of maintenance updates](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy#impacts_of_maintenance_updates).
  * [Turn on maintenance windows notifications](https://docs.cloud.google.com/memorystore/docs/redis/managing-maintenance-updates#turning_on_maintenance_notifications) to alert you of upcoming maintenance.
  * [Have retry logic with exponential backoff](https://docs.cloud.google.com/memorystore/docs/redis/high-availability#retrying_the_instance_connection_after_failover) in place.
  * For Standard Tier instances you can simulate a maintenance event by using [manual failover](https://docs.cloud.google.com/memorystore/docs/redis/manual-failover-overview) to see how the failover caused by maintenance affects your application.
  * For Basic Tier instances you can simulate the impact of a maintenance update by temporarily [scaling](https://docs.cloud.google.com/memorystore/docs/redis/scaling-instances) the instance to a larger size. After you observe the impact you can scale back to the original size.



## Memory management

Memory management can be a challenge because of the well known [memory fragmentation](https://redis.io/topics/memory-optimization#memory-allocation) that occurs with open source Redis. We recommend that you lower the `maxmemory` configuration for your instance to give yourself overhead in the case of high memory pressure.

The best way to monitor the memory pressure on your Memorystore instance is by [using the System Memory Usage Ratio metric](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio). For more a detailed guide on how to manage memory for Memorystore for Redis, see [Memory management best practices](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices).

## Managing idle connections

Over time, you may see the number of connections to your Memorystore instance increase if connections are not being properly terminated. This can have negative performance implications, especially if you are using in-transit encryption, which [imposes maximum connections limits](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption#connection_limits_for_in-transit_encryption) based on your capacity tier. To mitigate this, we recommend utilizing the `timeout` [Redis configuration parameter](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs) which allows you to set the number of seconds before idle client connections are automatically terminated.

## Access Transparency resource names

Sensitive data shouldn't be stored in Memorystore for Redis resource names. By resource names, we mean Memorystore for Redis instance names, and instance metadata, such as tags. Data stored in resource names is not guaranteed to be protected by Google Cloud [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview), and may conflict with your organization's Access Transparency compliance requirements.

## Serverless VPC Access Connector required for some serverless environments

[Some serverless environments](https://docs.cloud.google.com/memorystore/docs/redis/supported-environments#serverless-environments-that-need-a-serverless-vpc-access-connector) require a [Serverless VPC Access Connector](https://docs.cloud.google.com/memorystore/docs/redis/supported-environments#serverless-vpc-access-connector-requirement) in order to connect to Memorystore for Redis. Set up the Serverless VPC Access connector for your project if you want to connect using one of these environments.

## Networking

We recommend that you use the **private services access** [connection mode](https://docs.cloud.google.com/memorystore/docs/redis/networking#connection_modes). Memorystore for Redis uses two connection modes: private services access and direct peering. The private services access connection mode makes IP range management more simple and allows you to use Shared VPC if you want.

Once you have created an instance, the connection mode cannot be changed.

For more details, see [Networking](https://docs.cloud.google.com/memorystore/docs/redis/networking).

## Monitoring and alerts

We recommend using [monitoring](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances) and [alerts](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#create-stackdriver-alert) because they give you key signals on the memory usage of your Redis instance. They also give you insight into how efficiently your Redis instance responds to incoming cache requests.

You should set up the following default alerts:

  * [Setting a Cloud Monitoring alert for memory usage](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#create-stackdriver-alert)
  * [Setting a Cloud Monitoring alert for System Memory Usage Ratio](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#system-memory-stackdriver-alert)



## CPU usage best practices

The [improper use of expensive redis commands](https://docs.cloud.google.com/memorystore/docs/redis/troubleshoot-issues#high_cpu_usage_error_scenarios) leads to high latency, unresponsiveness, or connectivity issues. Standard Tier instances provide HA during disaster recovery and rely on asynchronous replication between primary and replica nodes. If one of the nodes has an expensive command processing that blocks the Redis main thread, replication could be impacted. If the issue persists and a location outage happens, the most recent data written in the location of the outage might not be available in the other location.

We recommend [using Cloud Monitoring](https://docs.cloud.google.com/memorystore/docs/redis/monitor-instances) to set alerts for the [Main Thread CPU Seconds](https://docs.cloud.google.com/memorystore/docs/redis/supported-monitoring-metrics) (`redis.googleapis.com/stats/cpu_utilization_main_thread`) metric to make sure CPU utilization doesn't exceed 0.8 seconds for the primary node or 0.5 seconds for each replica node, when the replica is designated as a [read replica](https://docs.cloud.google.com/memorystore/docs/redis/about-read-replicas).

If your Redis instance exceeds the recommended values, we recommend you [scale](https://docs.cloud.google.com/memorystore/docs/redis/scale-instances) the instance to a higher [capacity tier](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview#capacity_tier_performance) or follow the [troubleshooting instructions](https://docs.cloud.google.com/memorystore/docs/redis/troubleshoot-issues#high_cpu_usage_error_scenarios) to avoid CPU intensive operations.

If your instance either experiences high CPU utilization or the instance's resources become exhausted (for example, by having too many connections), then the instance might misbehave and external metrics might be missing.

### Resource-intensive commands

We strongly recommend that you avoid using Redis commands that are resource-intensive. Using these commands might result in the following performance issues:

  * High latency and client timeouts
  * Memory pressure caused by commands that increase memory usage
  * Data loss during node replication and synchronization because the Redis main thread is blocked
  * Starved health checks, observability, and replication



The following table lists examples of Redis commands that are resource-intensive and provides you with alternatives that are resource-efficient.

**Tip** : In addition to being resource-intensive, as your total data size increases, so does the cost of using these commands.

To find which long-running commands you use, use [`SLOWLOG`](https://redis.io/docs/latest/commands/slowlog/). This tool provides you with a list of commands that take the longest to run. As a result, you know the commands that cause latency issues. To determine resource-efficient alternatives for these commands, refer to the following table.

**Category** | **Resource-intensive command** | **Resource-efficient alternative**  
---|---|---  
Run for the entire keyspace | `KEYS` | `SCAN`  
Run for a variable-length keyset | `LRANGE` | Limit the size of the range that you use for a query.  
`ZRANGE` | Limit the size of the range that you use for a query.  
`HGETALL` | `HSCAN`  
`SMEMBERS` | `SSCAN`  
Block the running of a script | `EVAL` | Ensure that your script doesn't run indefinitely.  
`EVALSHA` | Ensure that your script doesn't run indefinitely.  
Remove files and links | `DEL` | `UNLINK`  
Publish and subscribe | `PUBLISH` | `SPUBLISH`  
`SUBSCRIBE` | `SSUBSCRIBE`  
  
## Redis client best practices

This section provides guidance on optimally using your Redis client.

### Detect and handle unresponsive connections

We strongly recommend configuring your client application to detect unresponsive connections to Memorystore for Redis. When an unresponsive connection is detected, the client must reset it. To build a resilient application, we recommend the following client configurations:

  * **Configure TCP keep-alive parameters** : set the `TCP keepalive time`, `TCP keepalive interval`, and `TCP keepalive probes` parameters so that clients detect and drop unresponsive connections proactively, even when connections are idle. For example, if you set the `TCP keepalive time` parameter to 30 seconds, `TCP keepalive interval` to 10 seconds, and `TCP keepalive probes` to 3, then clients reset unresponsive idle connections within a minute.
  * **Configure TCP user timeouts** : set this timeout in your clients to reset connections that have outstanding requests and stop responding. For example, if you set the timeout to 15 seconds, then clients reset unresponsive connections that have outstanding requests after 15 seconds.



## Client-specific best practices

If you scale out your applications, then you might experience `READONLY` errors on write commands. Memorystore for Redis uses a non-Sentinel deployment with static endpoints, and clients don't receive dynamic role information up front. If you use a single client connection for both your primary and replica endpoints, then your client might accidentally send write commands to the read-only replica. The replica returns a `READONLY` error because it can't process write commands.

To prevent write misrouting, don't use a single connection for both reads and writes. Instead, split your operations by creating the following separate client instances:

  * **Primary client** : connect only to the primary endpoint
  * **Replica client** : connect only to the replica endpoint



The following tabs show you how to configure the separate templates in Go, Java, Node.js, and Python.

### Go
    
    
    package main
    
    import (
      "context"
      "fmt"
    
      "github.com/redis/go-redis/v9"
    )
    
    func main() {
    ctx := context.Background()
    
      // Initialize the primary client connecting only to the primary endpoint
      primaryClient := redis.NewClient(&redis.Options{
          Addr:     "PRIMARY_HOST:6379",
          Password: "YOUR_PASSWORD",
          DB:       0,
      })
      defer primaryClient.Close()
    
      // Initialize the replica client connecting only to the replica endpoint
      replicaClient := redis.NewClient(&redis.Options{
          Addr:     "REPLICA_HOST:6379",
          Password: "YOUR_PASSWORD",
          DB:       0,
      })
      defer replicaClient.Close()
    
      // Use the primary client for all mutating commands
      err := primaryClient.Set(ctx, "example_key", "example_value", 0).Err()
      if err != nil {
          fmt.Printf("Failed to write to primary: %v\n", err)
      }
    
      // Use the replica client for all read-only commands
      val, err := replicaClient.Get(ctx, "example_key").Result()
      if err != nil {
          fmt.Printf("Failed to read from replica: %v\n", err)
      } else {
          fmt.Printf("Successfully read value: %s\n", val)
      }
    }

### Java
    
    
    @Bean
    public RedisConnectionFactory primaryConnectionFactory() {
      RedisStandaloneConfiguration config = new RedisStandaloneConfiguration("PRIMARY_HOST", 6379);
      config.setPassword(RedisPassword.of("YOUR_PASSWORD"));
      return new LettuceConnectionFactory(config);
    }
    
    @Bean
    public RedisConnectionFactory replicaConnectionFactory() {
      RedisStaticMasterReplicaConfiguration config =
          new RedisStaticMasterReplicaConfiguration("PRIMARY_HOST", 6379);
      config.addNode("REPLICA_HOST", 6379);
      config.setPassword(RedisPassword.of("YOUR_PASSWORD"));
    
      LettuceClientConfiguration clientConfig = LettuceClientConfiguration.builder()
          .readFrom(ReadFrom.REPLICA_PREFERRED)
          .build();
    
      return new LettuceConnectionFactory(config, clientConfig);
    }
    
    @Bean
    public RedisTemplate<String, Object> primaryRedisTemplate(
      @Qualifier("primaryConnectionFactory") RedisConnectionFactory factory) {
    
      RedisTemplate<String, Object> template = new RedisTemplate<>();
      template.setConnectionFactory(factory);
      return template;
    }
    
    @Bean
    public RedisTemplate<String, Object> replicaRedisTemplate(
      @Qualifier("replicaConnectionFactory") RedisConnectionFactory factory) {
    
      RedisTemplate<String, Object> template = new RedisTemplate<>();
      template.setConnectionFactory(factory);
      return template;
    }

### Node.js
    
    
    import { createClient } from 'redis';
    
    async function main() {
    // Initialize the primary client connecting only to the primary endpoint
    const primaryClient = createClient({
      url: 'redis://PRIMARY_HOST:6379',
      password: 'YOUR_PASSWORD'
    });
    
    // Initialize the replica client connecting only to the replica endpoint
    const replicaClient = createClient({
      url: 'redis://REPLICA_HOST:6379',
      password: 'YOUR_PASSWORD'
    });
    
    primaryClient.on('error', (err) => console.error('Primary Client Error', err));
    replicaClient.on('error', (err) => console.error('Replica Client Error', err));
    
    await primaryClient.connect();
    await replicaClient.connect();
    
    // Use the primary client for all mutating commands
    try {
      await primaryClient.set('example_key', 'example_value');
      console.log('Successfully wrote to primary');
    } catch (err) {
      console.error('Failed to write to primary:', err);
    }
    
    // Use the replica client for all read-only commands
    try {
      const val = await replicaClient.get('example_key');
      console.log(`Successfully read value: ${val}`);
    } catch (err) {
      console.error('Failed to read from replica:', err);
    }
    
    await primaryClient.disconnect();
    await replicaClient.disconnect();
    }
    
    main();

### Python
    
    
    import redis
    
    def main():
      # Initialize the primary client connecting only to the primary endpoint
      primary_client = redis.Redis(
          host='PRIMARY_HOST',
          port=6379,
          password='YOUR_PASSWORD',
          decode_responses=True
      )
    
      # Initialize the replica client connecting only to the replica endpoint
      replica_client = redis.Redis(
          host='REPLICA_HOST',
          port=6379,
          password='YOUR_PASSWORD',
          decode_responses=True
      )
    
      # Use the primary client for all mutating commands
      try:
          primary_client.set('example_key', 'example_value')
          print('Successfully wrote to primary')
      except redis.RedisError as e:
          print(f'Failed to write to primary: {e}')
    
      # Use the replica client for all read-only commands
      try:
          val = replica_client.get('example_key')
          print(f'Successfully read value: {val}')
      except redis.RedisError as e:
          print(f'Failed to read from replica: {e}')
    
    if __name__ == '__main__':
      main()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
