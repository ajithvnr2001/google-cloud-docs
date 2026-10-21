---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas/
title: Manage read replicas \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:05.314653+00:00
---

# Manage read replicas  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Manage read replicas Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas "View this page for the SQL Server database engine")

This page describes how to manage read replicas. These operations include disabling and enabling replication, promoting a replica, configuring parallel replication, and checking the replication status.

For more information about how replication works, see [Replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/replication).

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

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

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

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

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

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

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

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

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

When promoted, read replicas are automatically configured with backups, but they aren't automatically configured as high availability (HA) instances. You can enable high availability after promoting the replica just as you would for any non-replica instance. Configuring a read replica for high availability is done the same way as for a primary instance. Learn more about [configuring the instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-existing).

See [Promoting replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas) to learn more about use cases for cross-region replicas. 

Before promoting a read replica, if the primary is still available and serving clients, you should do the following:

  1. Stop all writes to the primary instance. 
  2. Check the replication status of the replica (follow the instructions in the **mysql Client** tab). 
  3. Verify that the replica is replicating, and then wait until the replication lag reported by the `Seconds_Behind_Master` metric is 0. 



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

You can also use the [ APIs Explorer on the Instances:promoteReplica page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/promoteReplica) to send the REST API request. 

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

You can also use the [ APIs Explorer on the Instances:promoteReplica page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/promoteReplica) to send the REST API request. 

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

## Configure parallel replication

Reducing replication lag is important for managing replication performance. Replication lag occurs when the updates to a read replica fall behind the updates to the primary instance. This section describes how users can enable parallel replication, which can reduce replication lag.

In MySQL replication, a replication SQL thread is used to execute the transactions that are collected in the relay log on the read replica. Parallel replication reduces replication lag by [increasing the number of SQL threads](https://dev.mysql.com/doc/refman/8.4/en/replication-threads.html) that work to execute these transactions. Read replicas with parallel replication enabled are sometimes called multithreaded replicas.

Parallel replication is available in these three scenarios in Cloud SQL for MySQL:

  * [Read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica)
  * [Replication from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external)
  * [Legacy high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha)



For simplicity, this page uses the terms "primary instance" and "read replica."

**Note:** In Cloud SQL for MySQL, replication is single-threaded by default in MySQL 8.0.26 and earlier versions. Parallel replication is enabled by default on MySQL 8.0.27 and later versions.   
Cloud SQL for MySQL supports flags for parallel replication for MySQL 5.7 and MySQL 8.0. This document contains links to documentation for the MySQL 8.0 versions of the flags. The flags are unsupported for MySQL 5.6.

### Basic steps to change parallel replication flags

**Note:** The Google Cloud console option is disabled when replication is disabled. Please use the gcloud commands instead.

The steps for enabling parallel replication are the following:

  1. On a read replica, [disable replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#disabling_replication).
  2. On the read replica, [set the flags](https://docs.cloud.google.com/sql/docs/mysql/flags#setting_a_database_flag) for parallel replication. Use the `gcloud` command to set the flags. The Google Cloud console option is disabled when replication is disabled.
  3. On the read replica, [enable replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#enabling_replication).
  4. Optionally, on the primary instance, set the flags to optimize performance for parallel replication.



### Read replicas: Flags for parallel replication

Cloud SQL for MySQL supports several flags for parallel replication on read replicas. For information about the flags, click these links to the MySQL 8.0 documentation:

  * [replica_parallel_workers](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_replica_parallel_workers)
  * [replica_parallel_type](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_replica_parallel_type)
  * [replica_preserve_commit_order](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_replica_preserve_commit_order)
  * [replica_pending_jobs_size_max](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_replica_pending_jobs_size_max)



Changing these flags does not restart the read replica.

**Note:** Before setting these flags, [disable replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#disabling_replication). After setting the flags, [enable replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#enabling_replication).

The following table contains the allowed ranges and default values for these flags:

Read replica flag | Allowed values | MySQL 5.7 default value | MySQL 8.0 and later default value  
---|---|---|---  
`replica_parallel_workers` | 0-1024 | 0 | 0 (MySQL 8.0.26 and earlier)  
4 (MySQL 8.0.27 and later)  
`replica_parallel_type` | `DATABASE, LOGICAL_CLOCK` | `DATABASE` | `DATABASE` (MySQL 8.0.26 and earlier)  
`LOGICAL_CLOCK` (MySQL 8.0.27 and later)  
`replica_preserve_commit_order` | `ON, OFF` | `OFF` | `OFF` (MySQL 8.0.26 and earlier)  
`ON` (MySQL 8.0.27 and later)  
`replica_pending_jobs_size_max` | 1024-1GB | 16MB | 128MB  
  
The `replica_preserve_commit_order` flag prevents gaps in the sequence of transactions executed from the replica's relay log.

The `[replica_preserve_commit_order=1](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_replica_preserve_commit_order)` setting requires the following:

  * [Enabling binary logs](https://docs.cloud.google.com/sql/docs/mysql/replication#bin-log-replica) on the replica (only for MySQL 5.7, MySQL 8.0.18 and earlier version)
  * Setting the `[replica_parallel_type](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_replica_parallel_type)` to `LOGICAL_CLOCK`

**Note:** The legacy high availability configuration does not support enabling binary logging on failover replicas; you cannot set the `replica_preserve_commit_order` flag to `1` on failover replicas.

The `replica_pending_jobs_size_max` flag sets the maximum memory, in bytes, available to applier queues holding events not yet applied.

**Note:** In Cloud SQL, the maximum allowed value of the `replica_pending_jobs_size_max` flag is 1GB.

### Primary instance: Flags for parallel replication

Cloud SQL for MySQL supports several flags for use on a primary instance. Depending on which version of Cloud SQL for MySQL you're using, you can use the following flags to tune replication performance for associated read replicas with parallel replication enabled.

  * [binlog_transaction_dependency_history_size](https://dev.mysql.com/doc/refman/9.7/en/replication-options-binary-log.html#sysvar_binlog_transaction_dependency_history_size)
  * [binlog_transaction_dependency_tracking](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_transaction_dependency_tracking)
  * [transaction_write_set_extraction](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_transaction_write_set_extraction)



Changing these flags doesn't require you to restart the primary instance.

The following table contains the allowed ranges and default values for these flags:

Primary instance flag | Allowed values | MySQL 5.7 default value | MySQL 8.0 default value | MySQL 8.4 default value | MySQL 9.7 default value  
---|---|---|---|---|---  
`binlog_transaction_dependency_history_size` | 1-1000000 | 25000 | 25000 | 25000 | 1000000  
`binlog_transaction_dependency_tracking` | `COMMIT_ORDER, WRITESET, WRITESET_SESSION` | `COMMIT_ORDER` | `WRITESET` | Not applicable (deprecated in MySQL 8.4) | Not applicable (deprecated in MySQL 9.7)  
`transaction_write_set_extraction` | `OFF, MURMUR32, XXHASH64` | `OFF` | `XXHASH64` | Not applicable (deprecated in MySQL 8.4) | Not applicable (deprecated in MySQL 9.7)  
  
In MySQL 5.7, if `binlog_transaction_dependency_tracking` is set to `WRITESET` or `WRITESET_SESSION`, then set `transaction_write_set_extraction` to a non-`OFF` value (`XXHASH64` or `MURMUR32`).

## Check replication status

When you view a replica instance using the Google Cloud console or log into the instance using an administration client, you get details about replication, including status and metrics. When you use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), you get a brief summary of the replication configuration.

Before checking the replication status for a Cloud SQL replica instance, use the   
[`gcloud sql instances describe`](https://cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command to display the status of the instance. As a result, you can see whether replication is enabled for the replica instance.

The following metrics are available for replica instances. ([Learn more](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance#available-metrics) about additional metrics available for all instances, including non-replica instances.)

Metric| Description  
---|---  
Replication State  
(`cloudsql.googleapis.com/database/replication/state`) |  Indicates whether replication is actively streaming logs from the primary to the replica. Possible values are:

  * `Running`
  * `Stopped`
  * `Error`

This metric reports `Running` if both the replica's I/O and SQL threads report they are running. See the **Slave I/O thread running state** and **Slave SQL thread running state** metrics below for more information, or consult [Checking Replication Status](https://dev.mysql.com/doc/refman/8.4/en/replication-administration-status.html) in the MySQL Reference Manual.  
Replication Lag  
(`cloudsql.googleapis.com/database/replication/replica_lag`) |  The amount of time that the replica's state is lagging behind the state of the primary instance. This is the difference between (1) the current time and (2) the original timestamp at which the primary committed the transaction that is currently being applied on the replica. In particular, writes may be counted as lagging even if they have been received by the replica, if the replica has not yet applied the write to the database. For cascading replicas, each primary-replica pair is monitored separately and there's no single metric that yields the end-to-end (primary to replica) lag.  This metric reports the value of `Seconds_Behind_Master` when `SHOW REPLICA STATUS` is run on the replica. For more information, see [Checking Replication Status](https://dev.mysql.com/doc/refman/8.4/en/replication-administration-status.html) in the MySQL Reference Manual.  
Network Lag  
(`cloudsql.googleapis.com/database/replication/network_lag`) |  The amount of time, in seconds that it takes from writing the binlog in the primary database to reach the IO thread in the replica. If the network_lag is zero, or negligible, but the `replica_lag` is high, it indicates that the SQL thread is not able to apply replication changes fast enough.  
Slave I/O thread running state  
(`cloudsql.googleapis.com/database/mysql/replication/slave_io_running_state`) |  Indicates whether the I/O thread for reading the primary instance's binary log is running on the replica. Possible values are:

  * `Yes`
  * `No`
  * `Connecting`

This metric reports the value of `Slave_IO_Running` when `SHOW REPLICA STATUS` is run on the replica. For more information, see [Checking Replication Status](https://dev.mysql.com/doc/refman/8.4/en/replication-administration-status.html) in the MySQL Reference Manual.  
Slave SQL thread running state  
(`cloudsql.googleapis.com/database/mysql/replication/slave_sql_running_state`) |  Indicates whether the SQL thread for executing events in the relay log is running on the replica. Possible values are:

  * `Yes`
  * `No`
  * `Connecting`

This metric reports the value of `Slave_SQL_Running` when `SHOW REPLICA STATUS` is run on the replica. For more information, see [Checking Replication Status](https://dev.mysql.com/doc/refman/8.4/en/replication-administration-status.html) in the MySQL Reference Manual.  
  
To check replication status:

### Console

Cloud SQL reports the `Replication State` and `Replication Lag` metrics on the [default Cloud SQL monitoring dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/cloudsql_database).

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
     2. **To monitor the replication lag metric** : in the **Select a metric** field, type `replica_lag`. The chart shows the amount of time that the replica's state lags behind that of its primary.
     3. **To monitor the status of the replica's I/O thread** : in the **Select a metric** field, type `Slave I/O thread running state`. Then add a filter on `state = "Yes"`. The chart shows 1 if the thread is running and 0 otherwise.
     4. **To monitor the status of the replica's SQL thread** : in the **Select a metric** field, type `Slave SQL thread running state`. Then add a filter on `state = "Yes"`. The chart shows 1 if the thread is running and 0 otherwise.



### gcloud

For a replica instance, check the replication status with:
    
    
    gcloud sql instances describe REPLICA_NAME

In the output, look for the properties `databaseReplicationEnabled` and `masterInstanceName`.

For a primary instance, check if there are replicas with:
    
    
    gcloud sql instances describe PRIMARY_INSTANCE_NAME

In the output, look for the property `replicaNames`.

### mysql Client

  1. Connect to the replica with a MySQL client. 

For information, see [Connection Options for External Applications](https://docs.cloud.google.com/sql/docs/mysql/external-connection-methods). 

  2. Check the replica's status: 
         
         SHOW REPLICA STATUS \G

Look for the following metrics in the output of the command:

     * `Master_Host`: The name of the primary instance.
     * `Slave_IO_Running`, `Slave_SQL_Running`: Whether the I/O and SQL threads, respectively, are running. These threads are responsible for transferring events from the primary to the replica's relay log and executing those events from the relay log. The value of the metric is `Yes` if the thread is running. Both threads must be running for replication to be active.
     * `Seconds_Behind_Master`: The amount of time, in seconds, by which the replica lags in processing the primary's transactions, i.e. the difference between (1) the current time and (2) the original timestamp at which the primary committed the transaction that is currently being applied on the replica. The value is `NULL` if replication is broken.
     * `Master_Log_file`, `Read_Master_Log_Pos`, `Relay_Master_Log_File`, `Exec_Master_Log_Pos`: These metrics show the coordinates (filename and offset) that the I/O thread has read events up to (`Master_Log_file` and `Read_Master_Log_Pos`) and that the SQL thread has executed events up to (`Relay_Master_Log_File` and `Exec_Master_Log_Pos`). If they are the same (i.e. `Master_Log_file` is equal to `Relay_Master_Log_File` and `Read_Master_Log_Pos` is equal to `Exec_Master_Log_Pos`) then the replica has processed all of the events it has received from the primary.



For more details about the output from this command, see the MySQL documentation on [Checking Replication Status](https://dev.mysql.com/doc/refman/8.4/en/replication-administration-status.html).

## Troubleshoot

Issue | Troubleshooting | Read replica didn't start replicating on creation. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.   
---|---  
Unable to create read replica - invalidFlagValue error. | One of the flags in the request is invalid. It could be a flag you provided explicitly or one that was set to a default value. First, check that the value of the `max_connections` flag is greater than or equal to the value on the primary. If the `max_connections` flag is set appropriately, [inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.  
Unable to create read replica - unknown error. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error. If the error is: `set Service Networking service account as servicenetworking.serviceAgent role on consumer project`, you can manually create the service account necessary by following the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).  
Disk is full. | The primary instance disk size can become full during replica creation. [ Edit the primary instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to upgrade it to a larger disk size.   
The replica instance is using too much memory. | The replica uses temporary memory to cache often-requested read operations, which can lead it to use more memory than the primary instance. Restart the replica instance to reclaim the temporary memory space.  
Replication stopped. | The maximum storage limit was reached and automatic storage increase isn't enabled. [ Edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to enable `automatic storage increase`.  
Replication lag is consistently high. | The write load is too high for the replica to handle. Replication lag takes place when the SQL thread on a replica is unable to keep up with the IO thread. Some kinds of queries or workloads can cause temporary or permanent high replication lag for a given schema. Some of the typical causes of replication lag are: 

  * Slow queries on the replica. Find and fix them.
  * All tables must have a unique/primary key. Every update on such a table without a unique/primary key causes full table scans on th replica.
  * Queries like `DELETE ... WHERE field < 50000000` cause replication lag with row-based replication since a huge number of updates are piled up on the replica.

Some possible solutions include:

  * [ Configure parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication).
  * Set the [innodb_flush_log_at_trx_commit](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i) flag on the read replica to 2. See [Tips for working with flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips) for more information about this flag.
  * [ Edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to increase the size of the replica.
  * Reduce the load on the database.
  * Send read traffic to the read replica.
  * Index the tables.
  * Identify and fix slow write queries.
  * Recreate the replica.

  
Replication lag suddenly spikes. | This is caused by long-running transaction(s). When a transaction (single statement or multi-statements) commits on the source instance, the start time of the transaction is recorded in the binary log. When the replica receives this binlog event, it compares that timestamp with the current timestamp to calculate replication lag. Hence, a long-running transaction on the source would result in an immediate large replication lag on the replica. If the amount of row changes in the transaction is large, the replica would also spend a long time to execute it. During the time, replication lag is increasing. Once the replica finishes this transaction, the catch up period would depend on the write workload on the source and the replica's processing speed. To avoid a long transaction, some possible solutions include:

  * Break the transaction into multiple small transactions 
  * Chunk a single large write query into smaller batches 
  * Try to separate long SELECT queries from a transaction mixed with DMLs 

  
Changing parallel replication flags results in an error. | An incorrect value is set for one of or more of these flags. On the primary instance that's displaying the error message, set the parallel replication flags:

  1. Modify the `binlog_transaction_dependency_tracking` and `transaction_write_set_extraction`flags: 
     * `binlog_transaction_dependency_tracking=COMMIT_ORDER`
     * `transaction_write_set_extraction=OFF`
  2. Add the `slave_pending_jobs_size_max` flag: `slave_pending_jobs_size_max=33554432`
  3. Modify the `transaction_write_set_extraction` flag: `transaction_write_set_extraction=XXHASH64`
  4. Modify the `binlog_transaction_dependency_tracking` flag: `binlog_transaction_dependency_tracking=WRITESET`

  
Replica creation fails with timeout. | Long-running uncommitted transactions on the primary instance can cause read replica creation to fail. Recreate the replica after stopping all running queries.  
  
## What's next

  * Learn how to [create a read replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica). 
  * Learn about Cloud SQL stored procedures for [read replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes).
  * Learn how to [configure an external replica configuration](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica).
  * Learn how to [configure an external primary configuration](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server). 
  * Learn more about [requirements and best practices for replication](https://docs.cloud.google.com/sql/docs/mysql/replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
