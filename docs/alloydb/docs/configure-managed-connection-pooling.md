---
url: https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling/
title: Configure managed connection pooling \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:53.065160+00:00
---

# Configure managed connection pooling  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure managed connection pooling Stay organized with collections  Save and categorize content based on your preferences. 

To scale your AlloyDB for PostgreSQL workloads, absorb sudden connection spikes, and reduce connection latency, you can enable _managed connection pooling_. Managed connection pooling maintains a pool of pre-established server connections and dynamically multiplexes incoming client requests across those connections instead of opening and closing a backend connection for every database operation.

Instead of connecting directly to the database backend, your application connects to a pooler, which provides shorter connection times and improved scalability for your read and write workloads. While you can use managed connection pooling for any transactional workload, it is best suited for applications that use short-lived connections or experience connection surges.

**Note:** Managed connection pooling is disabled by default.

## Before you begin

Managed connection pooling also supports connections with the AlloyDB Auth Proxy or AlloyDB Language Connectors.

### Required roles

To get the permission that you need to enable and use managed connection pooling, ask your administrator to grant you the [AlloyDB Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`) IAM role on the AlloyDB instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `alloydb.instances.update` permission, which is required to enable and use managed connection pooling. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Advanced configuration options

AlloyDB managed connection pooling supports the following advanced pooling configuration options. You can customize managed connection pooling to meet the needs of your instance by setting these configurations on an instance-level basis using the Google Cloud console, gcloud CLI, or the AlloyDB API.

**Configuration name** | **Description** |  Connection mode   
(`connection-pooling-pool-mode`)  |  For the connection mode, you can select either transaction (default) or session.   
  
Transaction (`transaction`):   
Pools connections at a transaction level. A server connection is assigned to a client during a transaction. After the transaction completes, the server connection is put back into the pool.   
  
Session (`session`):   
Pools connections at a session level. A server connection is assigned to the client during the whole time that it stays connected. After the client disconnects, the server connection is put back into the pool.   
---|---  
Maximum pool size   
(`connection-pooling-max-pool-size`)  |  The maximum size of the connection pool per user and database pair. This value can range from `1` to `262,042` connections, and the default value is `50` connections.   
Minimum pool size   
(`connection-pooling-min-pool-size`)  |  The minimum size of the connection pool. This value can range from `0` to `262,042` connections, and the default value is `0` connections.   
Maximum client connections   
(`connection-pooling-max-client-connections`)  |  The maximum number of simultaneous client connections allowed. This value can range from `1` to `262,042` connections, and the default value is `5000` connections.   
Idle client connection timeout(s)   
(`connection-pooling-client-connection-idle-timeout`)  |  The time that a client connection remains idle before it times out. This value can range from `0` to `2,147,483` seconds, and the default value is `0` seconds.   
Idle server connection timeout(s)   
(`connection-pooling-server-idle-timeout`)  |  The time that a server connection remains idle before it times out. This value can range from `0` to `2,147,483` seconds, and the default value is `600` seconds.   
Query wait timeout(s)   
(`connection-pooling-query-wait-timeout`)  |  The time that a query waits until it times out. This value can range from `0` to `2,147,483` seconds, and the default value is `120` seconds.   
Maximum prepared statements   
(`connection-pooling-max-prepared-statements`)  |  The maximum number of prepared statement commands sent in transaction pooling mode. This value can range from `0` to `262,042`, and the default value is `0`.   
Ignore startup parameters   
(`connection-pooling-ignore-startup-parameters`)  |  A comma-separated list of startup parameters that the pooler ignores when they aren't tracked in startup packets by default. The default value is `extra_float_digits`.   
Server lifetime(s)   
(`connection-pooling-server-lifetime`)  |  The maximum time a server connection is unused before managed connection pooling closes it. This value can range from `0` to `2,147,483` seconds, and the default value is `3600` seconds.   
Stats users   
(`connection-pooling-stats-users`)  |  A comma-separated list of database users authorized to connect to the statistics console. This parameter can be configured using the Google Cloud CLI or the AlloyDB API. Authorized users can access advanced metrics, which are maintained in the `alloydb_mcp_stats_{pooler_id}` database for each pooler.   
  
By default, managed connection pooling initiates connections to the AlloyDB server. When a client connection is established and authenticated, managed connection pooling might create one or more server connections so that the size of the pool matches the chosen configuration. The client connection is then assigned an available server connection. Server connections are maintained until they are explicitly closed or they are idle for longer than the idle server connection timeout period.

When you enable managed connection pooling, the AlloyDB Auth Proxy server's connections are also pooled using a separate pool that includes only pooled connections with AlloyDB Auth Proxy enabled.

## Enable managed connection pooling

**Note:** Enabling managed connection pooling on AlloyDB instances created before November 2024 requires a one-time update to network settings. This update results in a brief disruption to VPC network connectivity, typically lasting less than 15 seconds. Public IP is not affected. Your database won't restart during this process.

You can enable managed connection pooling for any existing or new instances.

### Enable for a new primary instance

To create a new primary instance with managed connection pooling enabled, see [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create#create-primary-instance). You can enable managed connection pooling for an instance using the Google Cloud console, Google Cloud CLI, or the AlloyDB API.

### Enable for a new read pool instance

To create a new read pool instance with managed connection pooling enabled, see [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create#create-read-pool). You can enable managed connection pooling for an instance using the Google Cloud console, Google Cloud CLI, or the AlloyDB API.

### Enable for an existing instance

You can enable managed connection pooling for an existing instance using the Google Cloud console, Google Cloud CLI, or the AlloyDB API.

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource name** column.

  3. In the **Overview** page, navigate to **Instances in your cluster**.

  4. Click **Edit primary** or **Edit read pool**.

  5. Under **Managed connection pool** , select the **Enable managed connection pool** checkbox.

  6. Optional: To configure managed connection pooling options, click **Advanced pooling options**.

You can customize managed connection pooling options to meet the needs of your instance. For more information, see Advanced configuration options.

  7. Click **Save changes**.




###  gcloud 

To enable managed connection pooling for an existing primary or read pool instance, use the following [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command:
    
    
    gcloud alloydb instances update INSTANCE_ID \
      --project=PROJECT_ID \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --enable-connection-pooling
    

Replace the following:

  * `INSTANCE_ID`: the ID of the AlloyDB instance that you want to enable managed connection pooling for.
  * `PROJECT_ID`: the ID of the project.
  * `REGION_ID`: the ID of the region.
  * `CLUSTER_ID`: the ID of the cluster.



After you enable managed connection pooling, you can customize managed connection pooling options to meet the needs of your instance by setting the advanced configuration options. For more information on how to set the configuration options, see Modify managed connection pooling for an instance.

###  REST 

To enable managed connection pooling for an existing primary or read pool instance, use the following command and set `connectionPoolConfig`:

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of the project.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the ID of the cluster. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `INSTANCE_ID`: the ID of the instance.



HTTP method and URL:
    
    
    PATCH https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID
    

Request JSON body:
    
    
    {
      "connectionPoolConfig": {
        "enabled": true
      }
    }
    

## Connect to managed connection pooling

Connecting to managed connection pooling is identical to direct database connections, except on a different port. Managed connection pooling listens on port `6432`. Any user added to the AlloyDB instance is able to connect using managed connection pooling.

### Connect using built-in authentication

The command example connects your AlloyDB instance to managed connection pooling using built-in authentication.
    
    
    psql postgresql://USERNAME:PASSWORD@IP_ADDRESS:6432/postgres
    

Replace the following:

  * `USERNAME`: the database username to connect with the AlloyDB instance.
  * `PASSWORD`: the password for the user.
  * `IP_ADDRESS`: the IP address of the AlloyDB instance.

**Note:** Connections from users with the `REPLICATION` role aren't supported.

### Connect using SSL connections

Instance SSL mode also applies to any connections to the managed connection pool. By default, only SSL connections are accepted. To allow unencrypted connections, use the following [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to set instance SSL mode to `ALLOW_UNENCRYPTED_AND_ENCRYPTED`.
    
    
    gcloud alloydb instances update INSTANCE_ID \
      --project=PROJECT_ID \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --ssl-mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED
    

### Connect using IAM authentication

You can connect to managed connection pooling using IAM authentication in one of two ways:

  * Authenticate with an OAuth 2.0 token: use gcloud CLI to get an OAuth 2.0 token and use it as the password when connecting to port `6432`. For more information, see [Authenticate with an OAuth 2.0 token](https://docs.cloud.google.com/alloydb/docs/connect-iam#procedure).

  * Authenticate automatically: use the [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect) with the `--auto-iam-authn` flag, or enable IAM authentication programmatically with [AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors#configure-connectors).




## View statistics about managed connection pools

When you enable managed connection pooling on your AlloyDB instance, you can connect to the built-in stats console to see real-time, detailed information about your connection pools. You can access the stats console on port `6432` through a private IP address using private services access or Private Service Connect. The stats console is useful for monitoring active or idle connections, troubleshooting wait times, and optimizing pool sizes.

To use the stats console, follow these steps:

  1. By default, no database users are authorized to access the stats console. You must use the Google Cloud CLI to specify which database users can connect, which allowlists them for stats console access.

To add a stats console user, use the `gcloud alloydb instances update` command:
         
         gcloud alloydb instances update INSTANCE_ID \
         --project=PROJECT_ID \
         --region=REGION_ID \
         --cluster=CLUSTER_ID \
         --connection-pooling-stats-users=STATS_USERS
         

Replace the following:

     * `INSTANCE_ID`: the name of the AlloyDB instance that you want to authorize statistics console users for.
     * `STATS_USERS`: a comma-separated list of database usernames.
     * `PROJECT_ID`: the ID of the project.
     * `REGION_ID`: the ID of the region.
     * `CLUSTER_ID`: the ID of the cluster.
  2. Connect to the instance on port `6432`. Each individual connection pooler instance maintains its own metrics in a uniquely numbered database. Specify the relevant statistics database for the pooler you want to monitor:

     * For standard poolers, use `alloydb_mcp_stats_POOLER_ID`. The ID is `1`, up to the number of poolers running on the instance.
     * For the Auth Proxy pooler, use `alloydb_mcp_stats_authproxy_pooler1`.
**Note:** The Auth Proxy pooler stats console database is reachable only by connecting using the Auth Proxy client.
    
    psql postgresql://USERNAME:PASSWORD@IP_ADDRESS:6432/alloydb_mcp_stats_1
    

Replace the following:

     * `POOLER_ID`: the ID of the connection pooler. The ID is `1`, up to the number of poolers running on the instance.
     * `USERNAME`: the database username to connect with the AlloyDB instance.
     * `PASSWORD`: the password for the user.
     * `IP_ADDRESS`: the IP address of the AlloyDB instance. This must be a Private Service Connect (PSC) or private services access (PSA) address.
  3. After you connect, run PgBouncer-compatible `SHOW` commands to view metrics, for example:

     * `SHOW STATS;`: displays general statistics for each database.
     * `SHOW POOLS;`: lists the status of all current connection pools.
     * `SHOW CLIENTS;`: shows information about current client connections.



For a full list of available commands, see the official [PgBouncer documentation](https://www.pgbouncer.org/usage.html#admin-console).

## Modify managed connection pooling for an instance

After you enable managed connection pooling, you can customize managed connection pooling options to meet the needs of your instance using the advanced configuration options. These configuration options are called _managed connection pooling flags_. For more information, see Advanced configuration options. These options also apply to the AlloyDB Auth Proxy pooler.

You can modify managed connection pooling configuration options for an existing instance using the Google Cloud console, Google Cloud CLI, or the AlloyDB API.

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, navigate to **Instances in your cluster**.

  4. Click **Edit instance** or **Edit read pool** for the instance that you want to modify.

  5. Under **Managed connection pool** , expand **Advanced pooling options**.

  6. Modify the advanced pooling options that you want to update. You can modify the following options:

     * Connection mode
     * Maximum pool size
     * Minimum pool size
     * Maximum client connections
     * Idle client connection timeout(s)
     * Idle server connection timeout(s)
     * Query wait timeout(s)
     * Maximum prepared statements
     * Ignore startup parameters
     * Server lifetime(s)
  7. Click **Update instance**.




###  gcloud 

To modify managed connection pooling configuration options for an existing instance, use the following [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command:
    
    
      gcloud alloydb instances update INSTANCE_ID \
        --project=PROJECT_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        { \
          --connection-pooling-pool-mode=CONNECTION_MODE \
          | --connection-pooling-max-pool-size=MAX_POOL_SIZE \
          | --connection-pooling-min-pool-size=MIN_POOL_SIZE \
          | --connection-pooling-max-client-connections=MAX_CLIENT_CONNECTIONS \
          | --connection-pooling-server-idle-timeout=SERVER_IDLE_TIMEOUT_PERIOD \
          | --connection-pooling-query-wait-timeout=QUERY_WAIT_TIMEOUT_PERIOD \
          | --connection-pooling-ignore-startup-parameters=IGNORE_STARTUP_PARAMETERS \
          | --connection-pooling-max-prepared-statements=MAX_PREPARED_STATEMENTS \
          | --connection-pooling-server-lifetime=SERVER_LIFETIME \
          | --connection-pooling-client-connection-idle-timeout=CLIENT_CONNECTION_IDLE_TIMEOUT \
        }
    

Replace the following:

  * `INSTANCE_ID`: the name of the AlloyDB instance that you want to modify managed connection pooling options for.
  * `PROJECT_ID`: the ID of the project.
  * `REGION_ID`: the ID of the region.
  * `CLUSTER_ID`: the ID of the cluster.
  * You can configure the following options:

    * `--connection-pooling-pool-mode`. This must be one of `session` or `transaction`.
    * `--connection-pooling-max-pool-size`
    * `--connection-pooling-min-pool-size`
    * `--connection-pooling-max-client-connections`
    * `--connection-pooling-server-idle-timeout`
    * `--connection-pooling-query-wait-timeout`
    * `--connection-pooling-ignore-startup-parameters`
    * `--connection-pooling-max-prepared-statements`
    * `--connection-pooling-server-lifetime`
    * `--connection-pooling-client-connection-idle-timeout`



###  REST 

To modify managed connection pooling configuration options for an existing instance, use the following command and set `connectionPoolConfig`:

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of the project.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the ID of the cluster. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `INSTANCE_ID`: the ID of the instance.
  * You can configure the following options:

    * `POOL_MODE`. This must be one of `session` or `transaction`.
    * `MAX_POOL_SIZE`
    * `MIN_POOL_SIZE`
    * `MAX_CLIENT_CONNECTIONS`
    * `SERVER_IDLE_TIMEOUT`
    * `QUERY_WAIT_TIMEOUT`
    * `IGNORE_STARTUP_PARAMETERS`
    * `MAX_PREPARED_STATEMENTS`
    * `SERVER_LIFETIME`
    * `CLIENT_CONNECTION_IDLE_TIMEOUT`
    * `STATS_USERS`



HTTP method and URL:
    
    
    PATCH https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID
    

Request JSON body:
    
    
    {
      "connectionPoolConfig": {
        "enabled": true,
        "flags": {
          "pool_mode": "POOL_MODE",
          "max_pool_size": "MAX_POOL_SIZE",
          "min_pool_size": "MIN_POOL_SIZE",
          "max_client_connections": "MAX_CLIENT_CONNECTIONS",
          "server_connection_idle_timeout": "SERVER_IDLE_TIMEOUT",
          "query_wait_timeout": "QUERY_WAIT_TIMEOUT",
          "ignore_startup_parameters": "IGNORE_STARTUP_PARAMETERS",
          "max_prepared_statements": "MAX_PREPARED_STATEMENTS",
          "server_lifetime": "SERVER_LIFETIME",
          "client_connection_idle_timeout": "CLIENT_CONNECTION_IDLE_TIMEOUT",
          "stats_users": "STATS_USERS"
        }
      }
    }
    

## View managed connection pooling status for an instance

You can view the status of managed connection pooling for an instance using the Google Cloud console, Google Cloud CLI, or the AlloyDB API.

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, find the instance you want to view the status of managed connection pooling for. The **Managed connection pooling** field shows whether it is enabled or disabled.




###  gcloud 

To view the status of managed connection pooling for an existing instance, use the following [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command:
    
    
    gcloud alloydb instances describe INSTANCE_ID \
      --project=PROJECT_ID \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --format="value(connectionPoolConfig.enabled)"
    

Replace the following:

  * `INSTANCE_ID`: the name of the AlloyDB instance that you want to view managed connection pooling status for.
  * `PROJECT_ID`: the ID of the project.
  * `REGION_ID`: the ID of the region.
  * `CLUSTER_ID`: the ID of the cluster.



If managed connection pooling is enabled, the following response is returned:

`True`

###  REST 

To view the status of managed connection pooling for your AlloyDB instance, use the following command and look for `connectionPoolConfig`:

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of the project.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the ID of the cluster. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `INSTANCE_ID`: the ID of the instance.



HTTP method and URL:
    
    
    GET https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID
    

## Disable managed connection pooling for an existing instance

You can disable managed connection pooling for an existing instance using the Google Cloud console, Google Cloud CLI, or the AlloyDB API.

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, navigate to **Instances in your cluster**.

  4. Click **Edit instance** or **Edit read pool** for the instance that you want to disable managed connection pooling for.

  5. Under **Managed connection pool** , clear the **Enable managed connection pool** checkbox.

  6. Click **Update instance**.

**Note:** After you disable managed connection pooling, all connections that were made to managed connection pooling are dropped.



###  gcloud 

To disable managed connection pooling for an existing instance, use the following [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command:
    
    
    gcloud alloydb instances update INSTANCE_ID \
      --project=PROJECT_ID \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --no-enable-connection-pooling
    

Replace the following:

  * `INSTANCE_ID`: the name of the AlloyDB instance that you want to disable managed connection pooling for.
  * `PROJECT_ID`: the ID of the project.
  * `REGION_ID`: the ID of the region.
  * `CLUSTER_ID`: the ID of the cluster.



###  REST 

To disable managed connection pooling for an existing instance, use the following command and set `connectionPoolConfig.enabled` to `false`:

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of the project.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the ID of the cluster. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `INSTANCE_ID`: the ID of the instance.



HTTP method and URL:
    
    
    PATCH https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID
    

Request JSON body:
    
    
    {
      "connectionPoolConfig": {
        "enabled": false
      }
    }
    

## Monitor managed connection pooling

AlloyDB provides the following metrics to help you monitor how managed connection pooling is running on your instance. Each metric is labeled with the pooler ID. You can view these metrics using the Metrics Explorer.

Metric name | Description  
---|---  
**Number of connection pools**  
  
`/database/conn_pool/num_pools` | The total number of connection pools per database.  
**Client connections**  
  
`/database/conn_pool/client_connections` | Tracks the number of client connections grouped by the status of the client connection per database. The statuses included in this metric are:  


  * `active`: the number active connections per database including the idle clients that don't have any pending query requests.
  * `waiting`: the number of clients waiting for a server connection per database.

  
**Server connections**  
  
`/database/conn_pool/server_connections` | Tracks the number of server connections grouped by the status of the server connection per database. The statuses included in this metric are:  


  * `active`: the number of active connections per database.
  * `idle`: the number of idle server connections per database.

  
**Average wait time**  
  
`/database/conn_pool/client_connections_avg_wait_time` | The average time spent by all clients in waiting state for a server in microseconds per database.  
  
For more information, see [AlloyDB metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-alloydb).

## Limitations

The following limitations apply:

  * If you use managed connection pooling in the transaction pooling mode, then the following SQL features aren't supported: 
    * `SET/RESET`
    * `LISTEN`
    * `WITH HOLD CURSOR`
    * `PREPARE/DEALLOCATE`
    * `PRESERVE/DELETE ROW` temp tables
    * `LOAD`
    * Session-level advisory locks
    * Protocol-level prepared plans
  * Managed connection pooling isn't supported for public IP connections.
  * Connections from users with the [PostgreSQL `REPLICATION`](https://www.postgresql.org/docs/current/sql-createrole.html) role aren't supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
