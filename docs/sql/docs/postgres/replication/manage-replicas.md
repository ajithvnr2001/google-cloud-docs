---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas/
title: Manage read replicas \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:53.294094+00:00
---

# Manage read replicas  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Manage read replicas Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas "View this page for the SQL Server database engine")

This page describes how to manage read replicas. These operations include disabling and enabling replication, promoting a replica, configuring parallel replication, and checking the replication status.

For more information about how replication works, see [Replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/replication).

## Disable replication

By default, a replica starts with replication enabled. However, you can disable replication, for example, to debug or analyze the state of an instance. When you are ready, you explicitly re-enable replication. Disabling or re-enabling replication doesn't restart the replica instance.

Disabling replication does not stop the replica instance; it becomes a read-only instance that is no longer replicating from its primary instance. You continue to be charged for the instance. On the disabled replica, you can re-enable replication, delete the replica, or promote the replica to a stand-alone instance.

When you disable the replication for an extended period of time, your disk storage requirements might increase. For example, your instance might accumulate transactional logs to let you resume replication when you re-enable replication. To avoid increasing disk storage requirements, instead of disabling replication for an extended period of time, consider promoting the replica or creating a clone of the primary instance.

To disable replication:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select a replica instance by clicking its name.
  3. Click **Disable replication** in the button bar.
  4. Click **OK**.



### gcloud
    
    
    gcloud sql instances patch REPLICA_NAME \
    --no-enable-database-replication

### REST v1

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * replica-name: The name of the replica instance



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseReplicationEnabled": "False"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "replica-name",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * replica-name: The name of the replica instance



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseReplicationEnabled": "False"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "replica-name",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Enable replication

If a replica has not been replicating for a long time, it will take longer for it to catch up to the primary instance. In this case, delete the replica and create a new one.

To enable replication:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select a replica instance by clicking its name.
  3. Click **Enable replication**.
  4. Click **Ok**.



### gcloud
    
    
    gcloud sql instances patch REPLICA_NAME \
    --enable-database-replication

### REST v1

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * replica-name: The name of the replica instance



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseReplicationEnabled": "True"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "replica-name",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * replica-name: The name of the replica instance



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseReplicationEnabled": "True"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "replica-name",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Promote a replica

Promoting a read replica stops replication and converts the instance to a standalone Cloud SQL primary instance with read and write capabilities.

When promoted, read replicas are automatically configured with backups, but they aren't automatically configured as high availability (HA) instances. You can enable high availability after promoting the replica just as you would for any non-replica instance. Configuring a read replica for high availability is done the same way as for a primary instance. Learn more about [configuring the instance for high availability](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#ha-existing).

See [Promoting replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas) to learn more about use cases for cross-region replicas. 

Before promoting a read replica, if the primary is still available and serving clients, you should do the following:

  1. Stop all writes to the primary instance. 
  2. Check the replication status of the replica (follow the instructions in the **psql Client** tab). 
  3. Verify that the replica is replicating, and then wait until the replication lag reported by the `replay_lag` metric is 0. 



Otherwise, a newly promoted instance may be missing some transactions that were committed to the primary instance.

To promote a replica to a standalone instance:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select a replica instance by clicking its name.
  3. Click **Promote replica**.
  4. Click **Ok**.



### gcloud
    
    
    gcloud sql instances promote-replica REPLICA_NAME
      

### REST v1

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command.

You can also use the [ APIs Explorer on the Instances:promoteReplica page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/promoteReplica) to send the REST API request. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * replica-name: The name of the replica instance



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name/promoteReplica

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name/promoteReplica"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name/promoteReplica" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/replica-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "PROMOTE_REPLICA",
      "name": "operation-id",
      "targetId": "replica-name",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command.

You can also use the [ APIs Explorer on the Instances:promoteReplica page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/promoteReplica) to send the REST API request. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * replica-name: The name of the replica instance



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name/promoteReplica

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name/promoteReplica"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name/promoteReplica" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/replica-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "PROMOTE_REPLICA",
      "name": "operation-id",
      "targetId": "replica-name",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

Confirm that the promoted instance is configured correctly. In particular, consider [configuring the instance for high availability](https://docs.cloud.google.com/sql/docs/configure-ha#ha-existing) if needed.

## Check replication status

When you view a replica instance using the Google Cloud console or log into the instance using an administration client, you get details about replication, including status and metrics. When you use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), you get a brief summary of the replication configuration.

Before checking the replication status for a Cloud SQL replica instance, use the   
[`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command to display the status of the instance. As a result, you can see whether replication is enabled for the replica instance.

The following metrics are available for replica instances. ([Learn more](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance#available-metrics) about additional metrics available for all instances, including non-replica instances.)

Metric| Description  
---|---  
Replication State  
(`cloudsql.googleapis.com/database/replication/state`) |  Indicates whether replication is actively streaming logs from the primary to the replica. Possible values are:

  * `Running`
  * `Stopped`
  * `Error`

This metric reports `Running` if:

  1. `pg_catalog.pg_stat_wal_receiver` reports a `status` of "streaming", **and**
  2. `pg_catalog.pg_is_wal_replay_paused()` reports "f" (false).

For more information, see [The Statistics Collector](https://www.postgresql.org/docs/12/static/monitoring-stats.html) and [System Administration Functions](https://www.postgresql.org/docs/12/static/functions-admin.html) in the PostgreSQL Reference Manual.  
Replication Lag  
(`cloudsql.googleapis.com/database/replication/replica_lag`) |  The amount of time that the replica's state is lagging behind the state of the primary instance. This is the difference between (1) the current time and (2) the original timestamp at which the primary committed the transaction that is currently being applied on the replica. In particular, writes may be counted as lagging even if they have been received by the replica, if the replica has not yet applied the write to the database. For cascading replicas, each primary-replica pair is monitored separately and there's no single metric that yields the end-to-end (primary to replica) lag.  For more information, see [Replication lag](https://docs.cloud.google.com/sql/docs/postgres/replication/replication-lag).  
Lag Bytes  
(`cloudsql.googleapis.com/database/postgresql/replication/replica_byte_lag`) |  Reports the number of bytes by which the read replica lags the primary. Four time series are produced for each replica, showing the number of bytes in the primary's write-ahead log that have not yet been…

  * `sent_location`: …sent to the replica
  * `write_location`: …written to disk by the replica
  * `flush_location`: …flushed to disk by the replica
  * `replay_location`: …replayed by the replica

These metrics serve different purposes; for example, `replay_location` gives an indication of the replication lag (the number of transactions committed to the primary that have not yet been applied to the replica), while `flush_location` gives an indication of the number of transactions that have not been recorded durably on the replica instance. These metrics are computed by comparing `pg_catalog.pg_current_wal_lsn()` to one of the following fields from `pg_stat_replication`: `sent_lsn`, `write_lsn`, `flush_lsn`, or `replay_lsn`. For more information, see [The Statistics Collector](https://www.postgresql.org/docs/current/static/monitoring-stats.html) in the PostgreSQL Reference Manual.  
Max Lag Bytes  
(`cloudsql.googleapis.com/database/postgresql/external_sync/max_replica_byte_lag`) |  For **a replica of an external primary** , reports the maximum replication lag (in bytes) over all databases that are being replicated to this instance. For each database, this is defined as the number of bytes in the primary's write-ahead log that have not been confirmed to be received by the replica. This metric is computed by sending a query to the primary to compare `pg_catalog.pg_current_wal_lsn()` to the value of `confirmed_flush_lsn` for each database being replicated to this replica instance. For more information, see [The Statistics Collector](https://www.postgresql.org/docs/current/static/monitoring-stats.html) in the PostgreSQL Reference Manual.  
  
To check replication status:

### Console

Cloud SQL reports the `Replication State` metric on the [default Cloud SQL monitoring dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/cloudsql_database).

To view other metrics for in-region and cross-region replicas, and replicas of external servers, create a custom dashboard and add the metrics you wish to monitor to it:

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select the **Dashboards** tab.
  3. Click **Create dashboard**.
  4. Give the dashboard a name and click OK.
  5. Click **Add chart**.
  6. For **Resource Type** select **Cloud SQL Database**.
  7. Do any of the following:
     1. **To monitor the replication state metric** : in the **Select a metric** field, type `Replication state`. Then add a filter for `state = "Running"`. The chart shows 1 if replication is running and 0 otherwise.
     2. **To monitor the replication lag, in bytes, for a read replica** : in the **Select a metric** field, type `Lag Bytes`. Then add a filter on `replica_lag_type = "replay_location"`. The chart shows the number of bytes associated with transactions that have been committed on the primary but have not yet been replayed on the replica.
     3. **To monitor the replication lag, in bytes, for a replica of an external primary** : in the **Select a metric** field, type `Max Lag Bytes`. The chart shows the number of bytes associated with transactions that have been committed on the primary but have not yet been confirmed received by the replica.



### gcloud

For a replica instance, check the replication status with:
    
    
    gcloud sql instances describe REPLICA_NAME

In the output, look for the properties `databaseReplicationEnabled` and `masterInstanceName`.

For a primary instance, check if there are replicas with:
    
    
    gcloud sql instances describe PRIMARY_INSTANCE_NAME

In the output, look for the property `replicaNames`.

### psql Client

Some replication status metrics are produced by the primary and some are produced by the replica. For the following steps, connect to the replica or primary instance (as directed below) with a PostgreSQL client.

For information, see [Connection options for external applications](https://docs.cloud.google.com/sql/docs/postgres/external-connection-methods). 

  1. To check the replica's status **from the primary instance** : 
         
         select * from pg_stat_replication;

Look for the following metrics in the output of the command: 
     * `client_addr`: The IP address of the replica instance.
     * `state`: Indicates whether the SQL thread for executing events in the relay log is running. The value is `streaming` when replication is started.
     * `replay_lag`: The number of bytes that the replica SQL thread is behind the primary instance. The value is `O` or a small number of bytes.
  2. To check the replica's status **from the replica instance** : 
         
         select * from pg_stat_wal_receiver;

Look for the following metrics in the output of the command:

     * `sender_host`: The IP address of the primary instance.
     * `status`: Indicates whether the SQL thread for executing events in the relay log is running. The value is `streaming` when replication is started.
     * `last_msg_send_time` and `last_msg_receipt_time`: The difference between these two timestamps is the lag time.

To check whether replication has been paused:
    
    select pg_is_wal_replay_paused();

The value is `t` if replication is paused and `f` otherwise.

To check whether there are transactions that have been received from the primary but not yet applied:
    
    # for PostgreSQL 9.6
    select pg_catalog.pg_last_xlog_receive_location(), pg_catalog.pg_last_xlog_replay_location();
    # for PostgreSQL 10 and above
    select pg_catalog.pg_last_wal_receive_lsn(), pg_catalog.pg_last_wal_replay_lsn();

If the two values are equal, then the replica has processed all of the transactions it has received from the primary.



* For more details about the output from these commands, see the PostgreSQL documentation on [The Statistics Collector](https://www.postgresql.org/docs/current/static/monitoring-stats.html). 

## Troubleshoot

Issue | Troubleshooting | Read replica didn't start replicating on creation. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.   
---|---  
Unable to create read replica - invalidFlagValue error. | One of the flags in the request is invalid. It could be a flag you provided explicitly or one that was set to a default value. First, check that the value of the `max_connections` flag is greater than or equal to the value on the primary. If the `max_connections` flag is set appropriately, [inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.  
Unable to create read replica - unknown error. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error. If the error is: `set Service Networking service account as servicenetworking.serviceAgent role on consumer project`, you can manually create the service account necessary by following the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).  
Disk is full. | The primary instance disk size can become full during replica creation. [ Edit the primary instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to upgrade it to a larger disk size.   
Disk space increases significantly. | A slot that's not actively used to track data causes PostgreSQL to hold onto WAL segments indefinitely, causing the disk space to grow indefinitely. If you use the [logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) features in Cloud SQL, replication slots are created and dropped automatically. Unused replication slots can be detected by querying the [`pg_replication_slots`](https://www.postgresql.org/docs/current/static/view-pg-replication-slots.html) system view and filtering on the `active` column. Unused slots can be dropped to remove WAL segments using the [`pg_drop_replication_slot`](https://www.postgresql.org/docs/current/static/functions-admin.html#FUNCTIONS-REPLICATION) command.   
The replica instance is using too much memory. | The replica uses temporary memory to cache often-requested read operations, which can lead it to use more memory than the primary instance. Restart the replica instance to reclaim the temporary memory space.  
Replication stopped. | The maximum storage limit was reached and automatic storage increase isn't enabled. [ Edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to enable `automatic storage increase`.  
Replication lag is consistently high. | The write load is too high for the replica to handle. Replication lag takes place when the SQL thread on a replica is unable to keep up with the IO thread. Some kinds of queries or workloads can cause temporary or permanent high replication lag for a given schema. Some of the typical causes of replication lag are: 

  * Slow queries on the replica. Find and fix them.
  * All tables must have a unique/primary key. Every update on such a table without a unique/primary key causes full table scans on th replica.
  * Queries like `DELETE ... WHERE field < 50000000` cause replication lag with row-based replication since a huge number of updates are piled up on the replica.

Some possible solutions include:

  * [ Edit the instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#editing_an_instance) to increase the size of the replica.
  * Reduce the load on the database.
  * Send read traffic to the read replica.
  * Index the tables.
  * Identify and fix slow write queries.
  * Recreate the replica.

  
Errors when rebuilding indexes in PostgreSQL 9.6. | You get an error from PostgreSQL informing you that you need to rebuild a particular index. This can be done only on the primary instance. If you create a new replica instance, you soon get the same error again. [Hash indexes are not propagated to replicas](https://www.postgresql.org/docs/9.6/indexes-types.html) in PostgreSQL versions below 10. If you must use hash indexes, upgrade to PostgreSQL 10+. Otherwise, if you also want to use replicas, don't use hash indexes in PostgreSQL 9.6.  
Query on the primary instance is always running. | After creating a replica, the query `SELECT * from pg_stat_activity where state = 'active' and pid = XXXX and username = 'cloudsqlreplica'` is expected to run continuously on your primary instance.   
Replica creation fails with timeout. | Long-running uncommitted transactions on the primary instance can cause read replica creation to fail. Recreate the replica after stopping all running queries.  
If the primary instance and the replica have [different vCPU sizes](https://docs.cloud.google.com/sql/docs/postgres/instance-settings), then there might be query performance issues because the query optimizer takes vCPU sizes into account. |  To resolve this issue, complete the following steps:

  1. Turn on the [log_duration](https://docs.cloud.google.com/sql/docs/postgres/flags#postgres-l) flag and set the `log_statement` parameter to `ddl`. This provides you with both the queries and the run time on the database. However, depending on your workload, this might cause performance issues.
  2. On both the primary instance and the read replica, run `explain analyze` for the queries.
  3. Compare the query plan and check for differences.

If this is a specific query, then modify the query. For example, you can change the order of the joins to see if you get better performance.  
  
## What's next

  * Learn how to [create a read replica](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica). 
  * Learn more about [requirements and best practices for replication](https://docs.cloud.google.com/sql/docs/postgres/replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
