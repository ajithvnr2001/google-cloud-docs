---
url: https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas/
title: Manage read replicas \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:28.016025+00:00
---

# Manage read replicas  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Manage read replicas Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to manage read replicas. These operations include disabling and enabling replication, promoting a replica, configuring parallel replication, and checking the replication status.

For more information about how replication works, see [Replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/replication).

This page applies to replicas of a Cloud SQL instance. To set up a Cloud SQL instance to act as a publisher to an external subscriber, see [Configure external replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica).

**Important:** Before using this feature, **review the[limitations](https://docs.cloud.google.com/sql/docs/sqlserver/replication#sql-server-limitations)**. Additionally, note that this feature only applies to the following versions of Cloud SQL for SQL Server: SQL Server 2017 Enterprise, SQL Server 2019 Enterprise, and SQL Server 2022 Enterprise.

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

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

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

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

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

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

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

To execute this cURL command at a command line prompt, you acquire an access token by using the [ gcloud auth print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command. You can also use the [ APIs Explorer on the Instances:patch page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch) to send the REST API request. 

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

When promoted, read replicas are automatically configured with backups, but they aren't automatically configured as high availability (HA) instances. You can enable high availability after promoting the replica just as you would for any non-replica instance. Configuring a read replica for high availability is done the same way as for a primary instance. Learn more about [configuring the instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-existing).

See [Promoting replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/sqlserver/replication/cross-region-replicas) to learn more about use cases for cross-region replicas. 

Before promoting a read replica, if the primary is still available and serving clients, you should do the following:

  1. Stop all writes to the primary instance. 
  2. Check the replication status of the replica. One option for doing so is the [ Always On Availability Group dashboard](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/use-the-always-on-dashboard-sql-server-management-studio?view=sql-server-ver15) in SQL Server Management Studio (SSMS). 
  3. Verify that the replica is replicating, and then check the replication lag, for example as reported by the `seconds_behind_master` metric. 
  4. Use the [`sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) stored procedure to export any logins created on the primary instance after the replica was created, and re-create them on the replica. 

**Note:** Because Cloud SQL doesn't automatically replicate logins created after replica creation, we recommend that you routinely use [`sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) to transfer new logins to your read replicas. Routine synchronization helps to ensure that applications can reconnect immediately after you promote a replica, even if the primary instance is unavailable at the time of promotion.

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

You can also use the [ APIs Explorer on the Instances:promoteReplica page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/promoteReplica) to send the REST API request. 

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

You can also use the [ APIs Explorer on the Instances:promoteReplica page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/promoteReplica) to send the REST API request. 

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

Currently, you should use T-SQL queries or SSMS to monitor replication status. For more information, see the following: 

  * [Tools to monitor Always On availability groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/monitoring-of-availability-groups-sql-server?view=sql-server-ver15)
  * [Use the Always On Availability Group dashboard](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/use-the-always-on-dashboard-sql-server-management-studio?view=sql-server-ver15)



## Troubleshoot

Issue | Troubleshooting | Read replica didn't start replicating on creation. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.   
---|---  
Unable to create read replica - invalidFlagValue error. | One of the flags in the request is invalid. It could be a flag you provided explicitly or one that was set to a default value. First, check that the value of the `max_connections` flag is greater than or equal to the value on the primary. If the `max_connections` flag is set appropriately, [inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error.  
Unable to create read replica - unknown error. | There's probably a more specific error in the log files. [Inspect the logs](https://docs.cloud.google.com/sql/docs/mysql/logging#viewing_logs) in Cloud Logging to find the actual error. If the error is: `set Service Networking service account as servicenetworking.serviceAgent role on consumer project`, you can manually create the service account necessary by following the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).  
Disk is full. | The primary instance disk size can become full during replica creation. [ Edit the primary instance](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance#editing_an_instance) to upgrade it to a larger disk size.   
The replica instance is using too much memory. | The replica uses temporary memory to cache often-requested read operations, which can lead it to use more memory than the primary instance. Restart the replica instance to reclaim the temporary memory space.  
Replication stopped. | The maximum storage limit was reached and automatic storage increase isn't enabled. [ Edit the instance](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance#editing_an_instance) to enable `automatic storage increase`.  
Replication lag is consistently high. | The write load is too high for the replica to handle. Replication lag takes place when the SQL thread on a replica is unable to keep up with the IO thread. Some kinds of queries or workloads can cause temporary or permanent high replication lag for a given schema. Some of the typical causes of replication lag are: 

  * Slow queries on the replica. Find and fix them.
  * Queries like `DELETE ... WHERE field < 50000000` cause replication lag with row-based replication since a huge number of updates are piled up on the replica.

Some possible solutions include:

  * [ Edit the instance](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance#editing_an_instance) to increase the size of the replica.
  * Reduce the load on the database.
  * Send read traffic to the read replica.
  * Index the tables.
  * Identify and fix slow write queries.
  * Recreate the replica.

  
Replica creation fails with timeout. | Long-running uncommitted transactions on the primary instance can cause read replica creation to fail. Recreate the replica after stopping all running queries.  
  
## What's next

  * Learn how to [create a read replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica). 
  * Learn more about [requirements and best practices for replication](https://docs.cloud.google.com/sql/docs/sqlserver/replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
