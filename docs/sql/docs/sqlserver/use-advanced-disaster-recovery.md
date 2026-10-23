---
url: https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery/
title: Use advanced disaster recovery (DR) \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:46.910872+00:00
---

# Use advanced disaster recovery (DR)  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use advanced disaster recovery (DR) Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to use [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#advanced_disaster_recovery). Advanced DR provides two main capabilities:

  * **Replica failover** lets you fail over your primary instance to the DR replica immediately in the event of a region failure. For Cloud SQL for SQL Server, the DR replica is a cascadable replica.
  * **Switchover** lets you reverse the roles of the primary instance and a DR replica with zero data loss. You can use switchover to restore a deployment to its original deployment state after replica failover, or you can use switchover to test DR.



Advanced DR is supported only on Cloud SQL Enterprise Plus edition instances.

**Note:** This page contains features related to Cloud SQL editions. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro).

## Before you begin

If you plan to use the Google Cloud SDK, then you must use version 502.0.0 or later. To check the version of the Google Cloud SDK, run `gcloud --version`. To update the Google Cloud SDK, run `gcloud components update`.

To install the Google Cloud SDK, see [Install the ](https://docs.cloud.google.com/sdk/docs/install)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Create a DR replica

Before you use advanced DR, [create a cascadable replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica#cascadable-replica-steps-sqlserver) of the primary instance in a different [region](https://docs.cloud.google.com/docs/geography-and-regions) than the primary instance.

**Note:** Cloud SQL doesn't automatically replicate SQL Server logins created after replica creation. We recommend that you routinely use the [`sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) stored procedure to transfer new logins from your primary instance to your DR replica. This helps to ensure that applications can reconnect successfully after a switchover or replica failover operation, even if the primary instance becomes unreachable during a disaster.

## Perform a switchover

After you've created a DR replica, you can perform the switchover operation. However, as a best practice, avoid performing the switchover operation under the following circumstances:

  * The primary instance is being actively used.
  * Admin operations are in progress, such as automated backup or the enablement or disablement of high availability (HA).



To avoid a timeout, consider performing switchover when the transaction volume is low.

When switchover completes, the operation takes a backup of the new primary instance (the former DR replica) as soon as the new primary instance is promoted. This backup can take between 5 and 15 minutes to complete depending on the disk size. After this backup is complete, if you want to use PITR on the promoted instance, then you must manually [enable PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr#enablingpitr). For more information about the considerations of using PITR with advanced DR, see Use PITR with advanced DR.

After the switchover operation is complete, you'll notice that the direction of replication is reversed.

After your old primary instance is reconfigured as a read replica, the [DNS write endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-using-write-endpoint), which previously resolved to the old primary instance, resolves to the new primary instance.

If you [configure Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#configure-psc-outbound) on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery), then after a switchover operation, when the DR replica is promoted to the primary instance, outbound connectivity continues to work on the new primary that's created. If you don't configure outbound connectivity on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery), then in order for the service to continue to work after switchover operations, you need to enable Private Service Connect outbound connectivity on the new primary instance.

### Before you begin

Before you perform the switchover operation, do the following:

  * If you haven't done so already, create a DR replica.
  * Use the [`sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) stored procedure to transfer any SQL Server logins created on the primary instance after the DR replica was created. Synchronizing logins ensures that applications can reconnect immediately after the switchover operation completes.
  * Verify that the primary instance and the DR replica are online.
  * If you're using a [DNS write endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-using-write-endpoint), then verify that the SSL configuration for the primary instance and the DR replica are the same. For example, if the DR replica is configured to [enforce SSL encryption](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#enforcing-ssl), but the primary instance allows unencrypted connections, then clients won't be able to connect to the new primary instance after the switchover operation completes.
  * Take an on-demand backup of the primary instance. This backup is a precaution in case you need to recover from any unexpected failures.

**Note:** For Cloud SQL to update a [write endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#connect-write-endpoint) and point it to the correct instance, make sure that your replica is on the new network architecture before the switchover operation occurs. If the instance isn't created with this architecture, then you can [upgrade the instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture).

### Perform the switchover operation

### gcloud

To perform the switchover operation, run the following command:
    
    
    gcloud sql instances switchover REPLICA_NAME

Replace the following variables:

  * REPLICA_NAME: the name of the DR replica that you want the primary instance to switch roles with.



### Terraform

To begin the switchover operation, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). To make the DR replica the new primary instance, use the first sample. The sample contains comments for the Terraform configuration changes you need to make to switch the primary instance and the DR replica.
    
    
    resource "google_sql_database_instance" "original-primary" {
      name             = "sqlserver-primary-instance-name"
      region           = "us-east1"
      database_version = "SQLSERVER_2022_ENTERPRISE"
      instance_type    = "CLOUD_SQL_INSTANCE"
      root_password    = "INSERT-PASSWORD-HERE"
      replica_names    = ["sqlserver-replica-instance-name"]
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
        backup_configuration {
          enabled = "true"
        }
      }
    }
    
    resource "google_sql_database_instance" "dr_replica" {
      name = "sqlserver-replica-instance-name"
      # Remove or comment out the master_instance_name
      # master_instance_name = google_sql_database_instance.original-primary.name
      region           = "us-west2"
      database_version = "SQLSERVER_2022_ENTERPRISE"
      # Change the instance type from "READ_REPLICA_INSTANCE" to "CLOUD_SQL_INSTANCE".
      instance_type = "CLOUD_SQL_INSTANCE"
      root_password = "INSERT-PASSWORD-HERE"
      # Add the original primary to the replica_names list
      replica_names = ["sqlserver-primary-instance-name"]
      # Remove or comment out the replica_configuration section
      # replica_configuration {
      #  cascadable_replica = true
      # }
    
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
      }
    }

After you make your changes, update the primary and DR replica by running `terraform plan`. Verify that the output includes `Plan: 0 to add, 1 to change, 0 to destroy.` To perform the switchover, run `terraform apply`.

At this point, the original primary is a replica of the new primary instance. However, that change isn't reflected in your Terraform state automatically. To make the original primary instance a replica of the new primary instance in your Terraform state, use the second sample. The second sample provides comments that describe the changes you need to make after running the first sample.
    
    
    resource "google_sql_database_instance" "original-primary" {
      name = "sqlserver-primary-instance-name"
      # Set master_instance_name to the new primary instance, the original DR replica.
      master_instance_name = "sqlserver-replica-instance-name"
      region               = "us-east1"
      database_version     = "SQLSERVER_2022_ENTERPRISE"
      # Change the instance type from "CLOUD_SQL_INSTANCE" to "READ_REPLICA_INSTANCE".
      instance_type = "READ_REPLICA_INSTANCE"
      root_password = "INSERT-PASSWORD-HERE"
      # Remove  values from the replica_names field, but don't remove the field itself.
      replica_names = []
      # Add replica_configuration section and set cascadable_replica to true.
      replica_configuration {
        cascadable_replica = true
      }
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
        backup_configuration {
          enabled = "true"
        }
      }
    }
    
    resource "google_sql_database_instance" "dr_replica" {
      name             = "sqlserver-replica-instance-name"
      region           = "us-west2"
      database_version = "SQLSERVER_2022_ENTERPRISE"
      # Change the instance type from "READ_REPLICA_INSTANCE" to "CLOUD_SQL_INSTANCE".
      instance_type = "CLOUD_SQL_INSTANCE"
      root_password = "INSERT-PASSWORD-HERE"
      # Add the original primary to the replica_names list
      replica_names = ["sqlserver-primary-instance-name"]
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
      }
    }

If your Terraform state is updated successfully, then when you run `terraform plan` against the second sample, a message similar to the following appears:

`No changes. Your infrastructure matches the configuration.`

If you run `terraform apply`, then you receive a message similar to the following:

`Resources: 0 added, 0 changed, 0 destroyed.`

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project of the primary instance and the DR replica.
  * REPLICA_NAME: the name of the DR replica.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/switchover

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/switchover"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/switchover" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T22:43:37.981Z",
      "operationType": "SWITCHOVER",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project of the primary instance and the DR replica.
  * REPLICA_NAME: the name of the DR replica.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME/switchover

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME/switchover"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME/switchover" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T22:43:37.981Z",
      "operationType": "SWITCHOVER",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Perform DR by invoking a replica failover

In the event of region failure or a disaster, you can perform DR by invoking a replica failover operation to your designated DR replica. To perform a replica failover, you promote the DR replica. In contrast with switchover, the promotion of the DR replica is immediate.

Since the DR replica assumes the role of the primary instance immediately, it's possible that the replica doesn't have all of the data from the old primary instance due to replication lag. For this reason, a replica failover can incur data loss.

As part of the promotion process, replica failover takes a backup of the new primary instance (the former DR replica) right after the DR replica becomes the new primary instance. After this backup is complete, point-in-time-recovery (PITR) is fully enabled on the new primary instance. This backup can take between 5 and 15 minutes to complete depending on the disk size of the new (and old) primary instance. During this backup period, PITR isn't available. 

When the old primary instance comes back online, the replica failover process takes a backup. After this backup is taken, the old primary instance is recreated as a read replica of the new primary instance.

For more information about the considerations of using PITR with advanced DR, see Use PITR with advanced DR.

After you invoke the replica failover operation, the [DNS write endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-using-write-endpoint), which previously resolved to the old primary instance, resolves to the new primary instance.

If you [configure Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#configure-psc-outbound) on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery), then after replica failover operations, when the DR replica is promoted to the primary instance, outbound connectivity continues to work on the new primary that's created. If you don't configure outbound connectivity on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery), then in order for the service to continue to work after replica failover operations, you need to enable Private Service Connect outbound connectivity on the new primary instance.

### Before you begin

Before you can perform a replica failover, do the following:

  * If you haven't done so already, then create a DR replica.
  * If the primary instance is still accessible, use the [`sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) stored procedure to transfer any unsynchronized SQL Server logins to the DR replica. Routinely synchronizing logins ensures that applications can reconnect immediately after failover.
  * Make sure the DR replica is online and healthy.

**Note:** For Cloud SQL to update a [write endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#connect-write-endpoint) and point it to the correct instance, make sure that your replica is on the new network architecture before the replica failover operation occurs. If the instance isn't created with this architecture, then you can [upgrade the instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture).

### Perform the replica failover operation

### gcloud

To invoke a replica failover to the DR replica, use the following command:
    
    
    gcloud sql instances promote-replica \
       REPLICA_NAME --failover

Replace the following variable:

  * REPLICA_NAME: the name of the DR replica



### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project of the primary instance and DR replica.
  * REPLICA_NAME: the name of the DR replica.
  * ENABLE_REPLICA_FAILOVER: set to `true` to use replica failover. If you set to ` false`, then the API uses the regular `promoteReplica` method without replica failover. 



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/promoteReplica?failover=ENABLE_REPLICA_FAILOVER

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/promoteReplica?failover=ENABLE_REPLICA_FAILOVER"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME/promoteReplica?failover=ENABLE_REPLICA_FAILOVER" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "PROMOTE_REPLICA",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project of the primary instance and DR replica.
  * REPLICA_NAME: the name of the DR replica.
  * ENABLE_REPLICA_FAILOVER: set to `true` to use replica failover. If you set to ` false`, then the API uses the regular `promoteReplica` method without replica failover. 



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME/promoteReplica?failover=ENABLE_REPLICA_FAILOVER

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME/promoteReplica?failover=ENABLE_REPLICA_FAILOVER"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME/promoteReplica?failover=ENABLE_REPLICA_FAILOVER" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T22:43:37.981Z",
      "operationType": "PROMOTE_REPLICA",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Check the status of a replica failover

Replica failover occurs in two phases. The first phase is the promotion of the DR replica. The second phase is the recreation of the old primary instance as a read replica.

To check the status of replica failover, check the status of each phase.

  1. Check the status of the first phase.

### Console

To check if the DR replica has been promoted to a standalone instance, do the following:

     1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

     2. Find the name of the DR replica that you promoted.
     3. Verify that SQL Server VERSION appears in the **Type** column for the new primary instance.

### gcloud

You can check the status by running the following command:
    
    gcloud sql instances describe DR_REPLICA_NAME

Replace the following variable:

     * DR_REPLICA_NAME: the name of the promoted DR replica

In the output, check that the following field appears and the replica has become a standalone Cloud SQL primary instance:
    
    **instanceType** : CLOUD_SQL_INSTANCE
    

  2. To verify the completion of the second phase, check the operations log on the instance for the message `RECONFIGURE_OLD_PRIMARY`.

The appearance of this message depends on when the old primary instance returns online, which can take minutes or days in the event of a disaster.

For more information on how to check the operations logs on an instance, see [View instance logs](https://docs.cloud.google.com/sql/docs/sqlserver/logging).




## Use PITR with advanced DR

Whether a switchover or replica failover, if the DR replica is promoted to a primary instance, and you want to use PITR on the promoted instance, you must manually enable PITR.

After PITR is enabled, the backup configuration and transaction log retention policies apply. If you don't specify values for these settings, the default value of 14 days applies.

For more information, see [Use PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr#gcloud).

After PITR is enabled on the new primary instance, you can restore the instance to any point in time during which it is an active primary instance.

### Split-brain during replica failover

It's possible that split-brain occurs when the primary instance continues to accept writes while a replica is promoted using replica failover. After the replica is promoted, when the old primary instance is available again, it is rebuilt as a replica of the promoted instance and a final backup is made. This backup can be used to recover any split-brain data that was not written to the promoted replica.

**Note:** Split-brain can't happen for switchover operations.

### Deletion of backups and transaction logs on replicas

If a primary instance that was enabled with PITR and backups becomes a read replica, then the last backup and PITR retention policy from its time as a primary instance is preserved and applied during its time as a replica. Even though the new primary instance is not taking backups, the old backups and transaction logs used for PITR are deleted on the read replica according to the last configured policy.

For example, if the instance is configured to have daily automated backups and keep 7 backups with 7 days of PITR logs, then when this instance becomes a read replica, anything older than 7 days is deleted once a day.

If you need to delete backups sooner, then you can remove backups manually. For more information, see [Delete a backup](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backing-up#delete-backup).

**Note:** You can't modify backup configuration settings while the instance is a replica.

### Recommendations for VPC Service Controls and advanced DR

If you use VPC Service Controls, then make sure that your service perimeters allow necessary communications for all recovery operations such as point-in-time recovery (PITR) operations, especially when you use CMEK with keys in a different project.

Advanced DR operations, like switchover and replica failover, can enable or reconfigure features like PITR, which can be blocked by VPC Service Controls if the service perimeters aren't configured correctly for CMEK and cross-project key access.

  * **Keep KMS key project in same perimeter as instance** : as a best practice, include the project containing the KMS key in the same VPC Service Controls perimeter as your Cloud SQL instances.
  * **Use a perimeter bridge** : as a secondary (less recommended) option, you can use a [perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters) to connect projects in different perimeters.
  * **Test** : use VPC Service Controls dry run mode to test your DR procedures (like switchover) and identify potential VPC Service Controls violations without enforcement.



For more information, see [Configure VPC Service Controls](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/configure-service-controls).

## Limitations

  * You can't designate a Cloud SQL Enterprise Plus edition read replica instance as DR replica if the primary instance stores its transaction logs for point-in-time recovery (PITR) on disk. To check where an instance stores its logs for PITR, see [Check the storage location of transaction logs used for PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/configure-pitr#check-log-storage-location).

  * You can't designate an external replica as a DR replica.

  * Terraform isn't supported for replica failover operations.



  * You can't use the Google Cloud console to perform replica failover or switchover operations.



## Troubleshoot

Issue | Troubleshooting  
---|---  
Switchover operation has failed. | 

Make sure the instance meets all the stated DR replica [(cascadable replica) requirements](https://docs.cloud.google.com/sql/docs/sqlserver/replication#configure_cascading_replicas). 
  * Check the volume of transactions on the database. If the transaction volume is high, then the operation might timeout. Consider retrying the operation when the transaction load is lower.

  
Switchover operation has failed and the primary instance is stuck in read-only mode. |  Perform a database restart to bring the primary instance back to write mode.  
Switchover operation has completed, but the Google Cloud console doesn't show the new reversed roles for the instances. | Refresh your browser to show the updated topology.  
Replica failover operation has failed. | 

  * Make sure that you've created a DR replica for the primary instance and that the DR replica is online.
  * If failover to the DR replica has failed, then promote to a regular (non-DR) read replica instead.

  
  
## What's next

  * View all the [Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations).
  * Read about [database observability](https://docs.cloud.google.com/sql/docs/sqlserver/observability)
  * [Monitor Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
