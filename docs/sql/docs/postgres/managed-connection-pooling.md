---
url: https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling/
title: Managed Connection Pooling overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:11.383725+00:00
---

# Managed Connection Pooling overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Managed Connection Pooling overview Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling "View this page for the MySQL database engine") | PostgreSQL | SQL Server

Managed Connection Pooling lets you scale your workloads by optimizing resource use and connection latency for your Cloud SQL instances. PostgreSQL creates a new process for each connection, which incurs memory usage and connection setup overhead. In architectures that frequently establish many short-lived connections—such as microservices or serverless applications running on Cloud Run—this overhead can affect database performance and scalability.

With Managed Connection Pooling enabled, clients connect to an intermediary connection pool cluster instead of connecting directly to the database server. This dynamic assignment provides performance improvements, especially for scaled connections, by absorbing sudden connection spikes and reusing existing database connections.

## Connection poolers and connection pools

When client applications connect to an instance with Managed Connection Pooling enabled, they connect to an intermediary connection pool cluster rather than connecting directly to the database server. The connection pool cluster consists of one or more connection poolers. A connection pooler is a database proxy service that manages and routes database connections between client applications and the database server.

A connection pooler maintains connection pools as a group of open reusable database server connections per database and user pair.

When an authenticated client application connects to a database as a specific user, the connection pooler routes the request to the corresponding connection pool:

  * If an idle server connection is available in the pool, then the connection pooler assigns it to the client request.
  * If an idle server connection is not available and the pool limit (`max_pool_size`) has not been reached, then the connection pooler creates a new server connection in the pool.
  * If all server connections in the pool are in use and the pool limit has been reached, then the client transitions to a waiting state until a server connection becomes available.
  * When the request finishes, the server connection returns to the connection pool for reuse.



### Relationship between poolers and pools

A single connection pooler can manage multiple connection pools simultaneously, with one pool for each unique database and database user pair that connects through that pooler.

If your instance runs multiple connection poolers, then each connection pooler independently maintains its own separate set of connection pools for the database and user pairs routed to it.

Managed Connection Pooling performance and scaling capabilities operate on multiple levels:

  * **Connection pool cluster scaling:** The number of connection poolers in the cluster scales automatically based on the number of vCPU cores provisioned for the instance (dividing the vCPU count by 4, with a minimum of 1 connection pooler). This ensures that connection pooling does not become a bottleneck. Incoming client connections are distributed across the available connection poolers. For example:

    * An instance with 2 or 4 vCPUs runs 1 connection pooler.
    * An instance with 8 vCPUs runs 2 connection poolers.
    * An instance with 16 vCPUs runs 4 connection poolers.
    * An instance with 32 vCPUs runs 8 connection poolers.
    * An instance with 64 vCPUs runs 16 connection poolers.
  * **Pooler and pool scaling:** Because connection poolers operate independently, all configuration options are applied per connection pooler rather than globally across the instance. Server connections are created on demand up to a maximum limit defined by `max_pool_size` for each managed pool in each connection pooler. For example, if `max_pool_size` is set to 50 on an instance running 2 connection poolers (8 vCPUs), then each connection pooler can open up to 50 server connections for a specific database and user pair, allowing a total of up to 100 server connections across the instance for that pool. Accurate pool sizing is vital for performance: setting this value too low can lead to longer connection wait times, while setting it too high can waste database server resources.

  * **Client connection configurations:** Client connection limits and timeout behavior are also configured per connection pooler. Key parameters include:

    * `max_client_connections`: Limits the maximum number of client connections allowed per connection pooler (the default value is 5,000 connections for each connection pooler).
    * `client_connection_idle_timeout`: Controls the duration that a client connection can remain idle before it times out.
    * `query_wait_timeout`: Controls the duration that a query waits for an available server connection in the pool before timing out.



## Use cases and considerations

Keep the following in mind when you use Managed Connection Pooling:

  * While you can use Managed Connection Pooling for any transactional workloads, it provides the most throughput and latency benefit to applications that contain short-lived connections, or applications that result in a connection surge.
  * For long-lived connections, the connection performance using Managed Connection Pooling can be slightly lower than when using a direct connection. In this case, Managed Connection Pooling provides connection scaling when the number of connections is very high. However, for applications that typically establish long-lived connections, you might want to avoid using connection pooling.
  * You can use Identity and Access Management to secure connections to your instance depending on the port that Managed Connection Pooling uses. For more information about how IAM works in Cloud SQL and its limitations, see [IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication).



For more information about enabling Managed Connection Pooling, see [Configure Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/configure-mcp).

## Requirements

To use Managed Connection Pooling, your instance must meet the following requirements:

  * Your instance must be a Cloud SQL Enterprise Plus edition instance. 
  * You must be connected to your instance using only a direct connection or the Cloud SQL Auth Proxy.
  * Your instance must be set up for [private service access](https://docs.cloud.google.com/sql/docs/postgres/private-ip#set_up_private_services_access_for_your_network), use public IP, or have [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) enabled.
  * Your instance must use the new [Cloud SQL network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture).
  * Managed Connection Pooling requires a minimum maintenance version number of `POSTGRES_$version.R20250727.00_14`. For more information about performing self-service maintenance, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). 



## Pooling options

Managed Connection Pooling lets you manage how connections are pooled using the `pool_mode` parameter. You can use the following pooling options:

  * `transaction` (default): pools connections at a transaction level. Connections are returned to the pool after each transaction completes. Cloud SQL recommends using `transaction` pooling mode for short-lived connections.
  * `session`: pools connections at a session level. Each session uses a dedicated server connection that maintains a session state. This reduces pooling efficiency. When a client disconnects, the server connection returns to the connection pool.



## Advanced configuration options

You can [customize Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/configure-mcp#modify-mcp) by using the following configuration options.

**Note:** Configuration options are set per connection pooler. Because Managed Connection Pooling runs multiple connection poolers based on the instance size (1 connection pooler for every 4 vCPUs, with a minimum of 1 connection pooler), determine your configuration values based on your instance size and pool size requirements.**Configuration name** | **Description** |  `max_pool_size` |  The maximum number of server connections allowed to a database and user pair in each connection pool. This configuration is applied per connection pooler. Determine this value based on your instance size and pool size requirements.   
  
The default value is `50` connections per database and user pair for each connection pooler.   
---|---  
`min_pool_size` |  The minimum number of server connections available at any time in each connection pool. This configuration is applied per connection pooler. Determine this value based on your instance size and pool size requirements.   
  
If the number of server connections is less than the `min_pool_size`, then this setting adds more server connections to the pool. This helps manage sudden increases in database load after periods of inactivity and ensures connections are available and ready to use.   
  
The default value is `0` connections.   
`max_client_connections` |  The maximum number of client connections allowed per connection pooler when using Managed Connection Pooling. Determine this value based on your instance size and pool size requirements.   
  
The default value is `5,000` connections for each connection pooler.   
`max_prepared_statements` |  The maximum number of protocol-level named prepared statements supported per connection pooler in `transaction` pooling mode. Determine this value based on your instance size and pool size requirements.   
  
Setting this option to `0` disables prepared statement support. For optimal performance, this value should exceed the number of commonly used prepared statements in your database. A high number of prepared statements in Managed Connection Pooling may cause an increase in memory usage.   
  
The default value is `0` statements.   
`client_connection_idle_timeout` |  The time that a client connection remains idle before it times out. This value can range from `0` to `2,147,483` seconds, and the default value is `0` seconds.   
`server_connection_idle_timeout` |  The time that a server connection remains idle before it times out. This value can range from `0` to `2,147,483` seconds, and the default value is `600` seconds.   
`query_wait_timeout` |  The time that a query waits for a server connection in a pool before it times out.   
  
Setting this option to 0 disables it, which allows indefinite client queuing. Enabling this option prevents unresponsive servers from holding up connections.   
  
This value can range from `0` to `2,147,483` seconds, and the default value is `120` seconds.   
`ignore_startup_parameters` |  The parameters you want ignored, that aren't tracked in the Managed Connection Pooling startup packets by default.   
`server_lifetime` |  The maximum time a server connection is unused before Managed Connection Pooling closes it. If the value is set to `0` seconds, then the connection is immediately closed after use.   
  
The default value is `3600` seconds.   
  
## Limitations

When using Managed Connection Pooling with your Cloud SQL Enterprise Plus edition instances, consider these limitations:

  * Enabling Managed Connection Pooling on an existing instance results in a database restart. 
  * Managed Connection Pooling can only be used with Cloud SQL Auth Proxy version 2.15.2 and later.
  * If you're using the Cloud SQL Go Language Connector, then we recommend a minimum Go version of `1.24`. If you use Go version 1.23 or earlier, then you might experience limitations on performance when using Managed Connection Pooling.
  * If you're using Managed Connection Pooling in `transaction` pooling mode, then the following SQL features aren't supported:

    * `SET/RESET`
    * `LISTEN`
    * `WITH HOLD CURSOR`
    * `PREPARE/DEALLOCATE`
    * `PRESERVE/DELETE ROW` temp tables
    * `LOAD`
    * Session-level advisory locks
  * If you're using the [asyncpg database interface library](https://magicstack.github.io/asyncpg/current/) for Managed Connection Pooling pooler on port 3307 and 6432, then you must update the `max_prepared_statements` to a value larger than 0 to enable support for prepared statements in Managed Connection Pooling pooler.

  * If you're using Cloud SQL for PostgreSQL version 17, then the `sslnegotiation=direct` option isn't supported.

  * Client IP tracking isn't supported with Managed Connection Pooling. If you enable _store client IP addresses_ in [query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights), then client IP addresses are displayed as `local` instead of the IP address itself. 




## Ports used by Managed Connection Pooling

When you enable Managed Connection Pooling, the ports used by Cloud SQL instances to serve database traffic change. You can use Identity and Access Management to secure connections, depending on the port.

The ports used by Managed Connection Pooling and their available IAM options are as follows:

  * **TCP port`5432`**: used for direct connections by the Postgres database server. This is the default port number for [directly connecting using the psql client](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip#connect).

  * **TCP port`6432`**: used for direct connections by the Managed Connection Pooling server. To connect using this port, specify `psql -p 6432` when [directly connecting using the psql client](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip#connect).

You can use any [IAM authentication option](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication#compare-db-auth-options) when using this port.

  * **TCP port`3307`**: used for the Cloud SQL Auth Proxy only connections by a Managed Connection Pooling server. When you use Cloud SQL Auth Proxy to connect to Managed Connection Pooling, this port number is configured with the Cloud SQL Auth Proxy client and can't be changed.

You can use any [IAM authentication option](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication#compare-db-auth-options), or [automatic IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication#auto-iam-auth) with this port.




## Server connections used by Managed Connection Pooling

The `max_connections` database configuration limits the maximum number of server connections a pooler in Managed Connection Pooling can use. Cloud SQL recommends adjusting this value based on your instance's workload requirements and the database instance size. During peak load, the number of connections for authentication can become very high.

If you're using the default `max_pool_size` of 50 connections per pool, then we recommend reserving at least 15 server connections per CPU for Managed Connection Pooling when you set the `max_connections` flag for your database. For more information about the `max_connections` flag, see [Maximum concurrent connections](https://docs.cloud.google.com/sql/docs/quotas#maximum_concurrent_connections). To modify the `max_connections` flag for your instance, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags#config).

## What's next

  * [Create an instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance)
  * [Configure Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/configure-mcp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
