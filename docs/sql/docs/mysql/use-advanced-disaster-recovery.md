---
url: https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery/
title: Use advanced disaster recovery (DR) \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:42.534340+00:00
---

# Use advanced disaster recovery (DR)  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use advanced disaster recovery (DR) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery "View this page for the SQL Server database engine")

This page describes how to use [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery#advanced_disaster_recovery). Advanced DR provides two main capabilities:

  * **Replica failover** lets you fail over your primary instance to the DR replica immediately in the event of a region failure.
  * **Switchover** lets you reverse the roles of the primary instance and a DR replica with zero data loss. You can use switchover to restore a deployment to its original deployment state after replica failover, or you can use switchover to test DR.



Advanced DR is supported only on Cloud SQL Enterprise Plus edition instances.

**Note:** This page contains features related to Cloud SQL editions. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).

## Before you begin

If you plan to use the Google Cloud SDK, then you must use version 502.0.0 or later. To check the version of the Google Cloud SDK, run `gcloud --version`. To update the Google Cloud SDK, run `gcloud components update`.

To install the Google Cloud SDK, see [Install the ](https://docs.cloud.google.com/sdk/docs/install)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Designate a DR replica

To perform advanced DR, you must first designate a cross-region DR replica.

### Primary instance requirements

The primary instance must be a Cloud SQL Enterprise Plus edition instance and have a designated DR replica.

If you're creating your Cloud SQL instance with a [DNS write endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint), then your primary instance must have the same SSL configuration as the designated DR replica before you invoke the switchover or replica failover operation. For example, if you configure your DR replica to [enforce SSL encryption](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#enforcing-ssl), but the primary instance allows unencrypted connections, then clients won't be able to connect to the new primary instance after the switchover or failover operation completes.

### DR replica requirements

The designated DR read replica must meet the following requirements:

  * Must be a Cloud SQL Enterprise Plus edition instance


  * Must be the same database major and minor version as the primary instance, running MySQL 8.0.31 or later

  * Must have binary logging enabled. You can't turn off binary logging while the instance is a designated DR replica.

To enable binary logging for a replica, run the following command:



    
    
         gcloud sql instances patch --enable-bin-log REPLICA_NAME

  * Must be in a separate [region](https://docs.cloud.google.com/docs/geography-and-regions) from the primary instance

  * Must be a direct read replica; can't be a cascading replica



  * Besides using the default values, the DR replica can't have any of the following flags configured:

    * `replicate_do_db`
    * `replicate_ignore_db`
    * `replicate_do_table`
    * `replicate_wild_do_table`
    * `replicate_ignore_table`
    * `replicate_wild_ignore_table`


  * Must store the transaction logs used for PITR in Cloud Storage

  * Can't be an external replica




### DR replica recommendations

This section provides recommendations for your DR replica. The following recommendations can help you avoid performance issues in your deployment:

  * Use the same disk size as the primary instance or enable auto-growth.
  * Use a consistent HA configuration. If you enable HA on the primary instance, then also enable HA on the DR replica.
  * Use a consistent data cache configuration. If you enable data cache on the primary instance, then also enable data cache on the DR replica.
  * Configure any appropriate database flags for your DR replica before and after any switchover or replica failover operations.
  * Use the same machine type (tier) and size for both the primary instance and DR replica.



### Create a replica to satisfy DR replica requirements

If the primary instance doesn't already have a cross-region read replica that satisfies the DR replica requirements, then create one.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the primary instance.
  3. In the **Actions** column, click the **More Actions** menu.
  4. Select **Create read replica**.
  5. In the **Instance ID** field, enter a name for the **DR replica**.
  6. In the **Database version** field, the same major version of the primary instance is selected for you.
  7. If you are using MySQL 8.0, then in the **Minor version** field, keep the pre-selected minor version. The DR replica and the primary instance must share the same database minor version.
  8. In the **Choose a region and zonal availability** section of the page, do the following: 
     * Select a _different_ region than the region of your primary instance.
     * Optional. Select **Multiple zones** for the DR replica.
     * Optional. Select the **Primary** and **Secondary zones** for the DR replica.
  9. In the **Customize your instance** section of the page, you can update the settings for your DR replica. For more details about each setting, see the [About instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings) page.
  10. For **Machine shapes** , select the same machine type as your primary instance.
  11. For **Flags** , configure any flags that are required for your database.
  12. Click **Create replica**.



Cloud SQL creates a backup of the primary instance and creates the replica. You are returned to the instance page for the primary.

### gcloud

To create a replica that meets the requirements of a DR replica, run the following command:
    
    
    gcloud sql instances create REPLICA_NAME \
       --master-instance-name=PRIMARY_INSTANCE_NAME \
       --region=REPLICA_REGION_NAME \
       --database-version=DATABASE_VERSION \
       --tier=MACHINE_TYPE \
       --availability-type=AVAILABILITY_TYPE
       --edition="ENTERPRISE_PLUS"

Replace the following variables:

  * REPLICA_NAME: the name of the DR replica.
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * REPLICA_REGION_NAME: specify a region that is different than the region of the primary instance.
  * DATABASE_VERSION: specify the version string that matches the database major and minor version of the primary instance, for example `MYSQL_8_0_31` . 

The database major and minor versions must be the same for both the primary and DR replica.

  * MACHINE_TYPE: specify the same machine type as the primary instance. We recommend that the machine type matches the machine type of the primary instance.
  * AVAILABILITY_TYPE: if the primary instance is configured for high availability, then we recommend that you specify `REGIONAL` to enable high availability.
  * EDITION: specify `ENTERPRISE_PLUS`.



### Terraform

To create a DR replica, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "original-primary" {
      name   = "mysql-original-primary-instance"
      region = "us-east1"
      # Specify a database version that supports Cloud SQL Enterprise Plus edition.
      database_version = "MYSQL_8_0"
      instance_type    = "CLOUD_SQL_INSTANCE"
    
      settings {
        # Specify a tier that supports Cloud SQL Enterprise Plus edition.
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
        backup_configuration {
          # You must enable automated backups and binary logging.
          enabled            = true
          binary_log_enabled = true
        }
      }
      # Set `deletion_protection` to true to ensure that one can't accidentally
      # delete this instance by use of Terraform whereas
      # `deletion_protection_enabled` flag protects this instance at the Google Cloud level.
      deletion_protection = false
    }
    
    resource "google_sql_database_instance" "dr-replica" {
      name = "mysql-dr-replica-instance"
      # DR replica must be in a different region than the region of the primary instance.
      region = "us-west2"
      # DR replica must be the same database version as the primary instance.
      database_version = "MYSQL_8_0"
      instance_type    = "READ_REPLICA_INSTANCE"
      # Specify the primary instance as the master instance.
      master_instance_name = google_sql_database_instance.original-primary.name
    
      settings {
        # DR replica must be in the same tier as your primary instance and support Enterprise Plus edition.
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
      }
    
      # Set `deletion_protection` to true to ensure that one can't accidentally
      # delete this instance by use of Terraform whereas
      # `deletion_protection_enabled` flag protects this instance at the Google Cloud level.
      deletion_protection = false
    }

### REST v1

Before using any of the request data, make the following replacements: 

  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * PROJECT_ID: the ID or project number of the Google Cloud project of the primary instance and DR replica.
  * DATABASE_VERSION: version string that matches the database major and minor version of the primary instance, for example `MYSQL_8_0_31`. The database version must be the same for both the primary and DR replica.
  * REPLICA_NAME: the name of the DR replica instance that you're creating. 
  * REPLICA_REGION: the region of DR replica instance. The replica region must be different from the region of the primary instance.
  * MACHINE_TYPE: specify the same machine type as the primary instance. We recommend that you select the same machine type as the primary instance.
  * AVAILABILITY_TYPE: if the primary instance is configured for high availability, then we recommend that you specify `REGIONAL` to enable high availability.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "DATABASE_VERSION",
      "name": "REPLICA_NAME",
      "region": "REPLICA_REGION",
      "settings":
      {
        "tier": "MACHINE_TYPE",
        "availabilityType": "AVAILABILITY_TYPE",
        "settingsVersion": 0,
        "replicationType": "ASYNCHRONOUS",
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T22:43:37.981Z",
      "operationType": "CREATE_REPLICA",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * PROJECT_ID: the ID or project number of the Google Cloud project of the primary instance and DR replica.
  * DATABASE_VERSION: version string that matches the database major and minor version of the primary instance, for example `MYSQL_8_0_31`. The database version must be the same for both the primary and DR replica.
  * REPLICA_NAME: the name of the DR replica instance that you're creating.
  * REPLICA_REGION: the region of DR replica instance. The replica region must be different from the region of the primary instance.
  * MACHINE_TYPE: specify the same machine type as the primary instance. We recommend that the disk size matches the disk size of the primary instance.
  * AVAILABILITY_TYPE: if the primary instance is configured for high availability, then we recommend that you specify `REGIONAL` to enable high availability.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "DATABASE_VERSION",
      "name": "REPLICA_NAME",
      "region": "REPLICA_REGION",
      "settings":
      {
        "tier": "MACHINE_TYPE",
        "availabilityType": "AVAILABILITY_TYPE",
        "settingsVersion": 0,
        "replicationType": "ASYNCHRONOUS",
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T22:43:37.981Z",
      "operationType": "CREATE_REPLICA",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_UD/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Designate the DR replica for the primary instance

The following procedures describe how to designate one of the cross-region replicas of a primary instance as a DR replica for switchover or replica failover.

### Console

To designate a DR replica for a primary instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find and select the primary instance. The **Overview** page for the primary instance appears.
  3. In the navigation menu, click **Replicas**.
  4. In the list of read replicas, find the cross-region read replica that you want to designate as the DR replica.
  5. For the replica, click the more_vert **Actions** button, and select **Designate as DR replica**.
  6. Click **Confirm**.



### gcloud

To designate a DR replica for a primary instance, use the following command:
    
    
    gcloud sql instances patch PRIMARY_INSTANCE_NAME \
       --failover-dr-replica-name=REPLICA_NAME

Replace the following variables:

  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * REPLICA_NAME: the name of the DR replica.



### Terraform

To designate a DR replica for a primary instance, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    data "google_project" "default" {
    }
    
    resource "google_sql_database_instance" "original-primary" {
      name   = "mysql-original-primary-instance"
      region = "us-east1"
      # Specify a database version that supports Cloud SQL Enterprise Plus edition.
      database_version = "MYSQL_8_0"
      instance_type    = "CLOUD_SQL_INSTANCE"
    
      replication_cluster {
        # Designate the DR replica.
        # The format for setting the DR replica is `project-id:dr-replica-name`.
        failover_dr_replica_name = "${data.google_project.default.project_id}:mysql-dr-replica-instance"
      }
    
      settings {
        # Specify a tier that supports Cloud SQL Enterprise Plus edition.
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
        backup_configuration {
          # You must enable automated backups and binary logging.
          enabled            = true
          binary_log_enabled = true
        }
      }
      # Set `deletion_protection` to true to ensure that one can't accidentally
      # delete this instance by use of Terraform whereas
      # `deletion_protection_enabled` flag protects this instance at the Google Cloud level.
      deletion_protection = false
      # Optional. Add more settings.
    }
    
    resource "google_sql_database_instance" "dr-replica" {
      name = "mysql-dr-replica-instance"
      # DR replica must be in a different region than the region of the primary instance.
      region = "us-west2"
      # DR replica must be the same database version as the primary instance.
      database_version = "MYSQL_8_0"
      instance_type    = "READ_REPLICA_INSTANCE"
      # Specify the primary instance as the master instance.
      master_instance_name = google_sql_database_instance.original-primary.name
    
      settings {
        # DR replica must be in the same tier as your primary instance and support Enterprise Plus edition.
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
      }
    
      # Set `deletion_protection` to true to ensure that one can't accidentally
      # delete this instance by use of Terraform whereas
      # `deletion_protection_enabled` flag protects this instance at the Google Cloud level.
      deletion_protection = false
      # Optional. Add more settings.
    }
    

### REST v1

Before using any of the request data, make the following replacements: 

  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * REPLICA_NAME: the name of the DR replica.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME

Request JSON body: 
    
    
    {
      "replicationCluster": {
         "failoverDrReplicaName": "REPLICA_NAME"
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * REPLICA_NAME: the name of the DR replica.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME

Request JSON body: 
    
    
    {
      "replicationCluster": {
         "failoverDrReplicaName": "REPLICA_NAME"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Change the DR replica designation

If the replica meets the requirements, then you can designate a different replica as the DR replica. The old DR replica loses the DR replica designation.

### Console

To change the DR replica for a primary instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find and select the primary instance. The **Overview** page for the primary instance appears.
  3. In the navigation menu, click **Replicas**.
  4. In the list of read replicas, find the cross-region read replica that you want to designate as the new DR replica.
  5. For the replica, click the more_vert **Actions** button, and select **Designate as DR replica**.



### gcloud

To change the DR replica, run the designate command again, and specify a different DR replica.

### REST

To change the DR replica, make the designate API request again, and specify a different DR replica.

### View the DR replica designation

You can check which DR replica is assigned to the primary instance by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API. You can also check whether a replica is a designated DR replica.

To find out which DR replica is designated for a primary instance, use the following procedure.

### Console

To find out which read replica is the designated DR replica for a primary instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find and select the primary instance. The **Overview** page for the primary instance appears.
  3. In the navigation menu, click **Replicas**.
  4. In the list of read replicas, verify that `MySQL disaster recovery replica` appears in the **Type** column for the designated DR replica.



### gcloud

To find out which instance is the designated DR replica of a primary instance, use the following command:
    
    
    gcloud sql instances describe PRIMARY_INSTANCE_NAME

Replace the following variable:

  * PRIMARY_INSTANCE_NAME: the name of the primary instance



The output of this command contains the field named `failoverDrReplica` which identifies the designated DR replica.

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project that contains the instance.
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0_31",
      "settings": {
      . . .
      "replicaNames": [
        "my-instance-replica"
      ],
      "ipAddresses": [
        {
          "type": "PRIMARY",
          "ipAddress": "192.5.4.1"
        }
      ],
      "instanceType": "CLOUD_SQL_INSTANCE",
       . . .
      "connectionName": "my-project:us-east1:my-instance",
      "name": "my-instance",
      "region": "us-east1",
      "gceZone": "us-east1-c",
      "secondaryGceZone": "us-east1-b",
      "databaseInstalledVersion": "MYSQL_8_0_31",
      "maintenanceVersion": "MYSQL_8_0_31.R20240207.00_07",
      **"replicationCluster" {
           "failoverDrReplicaName": "my-project:my-instance-replica"
       },**
      "createTime": "2024-03-15T18:11:03.596Z",
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
    }
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project that contains the instance.
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0_31",
      "settings": {
      . . .
      "replicaNames": [
        "my-instance-replica"
      ],
      "ipAddresses": [
        {
          "type": "PRIMARY",
          "ipAddress": "192.5.4.1"
        }
      ],
      "instanceType": "CLOUD_SQL_INSTANCE",
       . . .
      "connectionName": "my-project:us-east1:my-instance",
      "name": "my-instance",
      "region": "us-east1",
      "gceZone": "us-east1-c",
      "secondaryGceZone": "us-east1-b",
      "databaseInstalledVersion": "MYSQL_8_0_31",
      "maintenanceVersion": "MYSQL_8_0_31.R20240207.00_07",
      **"replicationCluster" {
           "failoverDrReplicaName": "my-project:my-instance-replica"
       },**
      "createTime": "2024-03-15T18:11:03.596Z",
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
    }
    }
    

To check whether a replica is a DR replica, use one of the following procedures.

### Console

To check whether a replica instance is a DR replica, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the replica instance.
  3. Verify that `MySQL disaster recovery replica` appears in the **Type** column for the designated DR replica.



### gcloud

To check whether a replica instance is a DR replica, run the following command:
    
    
    gcloud sql instances describe REPLICA_NAME

Replace the following variable:

  * REPLICA_NAME: the name of the read replica that you want to check



If the replica is a DR replica, then the output of the command contains the field `drReplica=true`.

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project that contains the instance.
  * REPLICA_NAME: the name of the replica.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project that contains the instance.
  * REPLICA_NAME: the name of the replica.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Remove the DR replica

You can clear the DR replica designation from a primary instance. However, if no DR replica is assigned to a primary instance, then you can't perform switchover or replica failover.

### Console

To remove a designated DR replica from a primary instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find and select the primary instance. The **Overview** page for the primary instance appears.
  3. In the navigation menu, click **Replicas**.
  4. In the list of read replicas, find the cross-region read replica that you want to remove.
  5. For the replica, click the more_vert **Actions** button, and select **Remove as DR replica**.
  6. Click **Confirm**.



### gcloud

To remove the DR replica designation, run the following command on the primary instance:
    
    
    gcloud sql instances patch PRIMARY_INSTANCE_NAME \
      --clear-failover-dr-replica-name

Replace the following variable:

  * PRIMARY_INSTANCE_NAME: the name of the primary instance from which you want to remove the designated DR replica



### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project of the primary instance and DR replica. 
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * Set the `failoverDrReplicaName` field to an empty string.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME

Request JSON body: 
    
    
    {
      "replicationCluster": {
         "failoverDrReplicaName": ""
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project of the primary instance and DR replica. 
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * Set the `failoverDrReplicaName` field to an empty string.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME

Request JSON body: 
    
    
    {
      "replicationCluster": {
         "failoverDrReplicaName": ""
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Perform a switchover

After you've designated a DR replica, you can perform the switchover operation. However, as a best practice, avoid performing the switchover operation under the following circumstances:

  * The primary instance is being actively used.
  * Admin operations are in progress, such as automated backup or the enablement or disablement of high availability (HA).



To avoid a timeout, consider performing switchover when the transaction volume is low.

When switchover completes, the operation takes a backup of the new primary instance (the former DR replica) as soon as the new primary instance is promoted. After this backup is complete, then point-in-time-recovery (PITR) is fully enabled on the new primary instance. This backup can take between 5 and 15 minutes to complete depending on the disk size. PITR coverage starts only after this backup has completed.

To reduce total switchover time, Cloud SQL configures and enables PITR in a separate, asynchronous operation after the switchover completes. For more information about the considerations of using PITR with advanced DR, see Use PITR with advanced DR.

After the switchover operation is complete, you'll notice that the direction of replication is reversed.

After your old primary instance is reconfigured as a read replica, the [DNS write endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint), which previously resolved to the old primary instance, resolves to the new primary instance.

**Important** : If you're not using a DNS write endpoint, then you must point your applications to use the IP address of the new primary instance.

If you [configure Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#configure-psc-outbound) on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery), then after a switchover operation, when the DR replica is promoted to the primary instance, outbound connectivity continues to work on the new primary that's created. If you don't configure outbound connectivity on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery), then in order for the service to continue to work after switchover operations, you need to enable Private Service Connect outbound connectivity on the new primary instance.

### Before you begin

Before you perform the switchover operation, do the following:

  * Designate a DR replica. You can only perform a switchover between the primary instance and the designated DR replica.
  * Verify that the primary instance and the DR replica are online.
  * If you're using a [DNS write endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint), then verify that the SSL configuration for the primary instance and the DR replica are the same. For example, if the DR replica is configured to [enforce SSL encryption](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#enforcing-ssl), but the primary instance allows unencrypted connections, then clients won't be able to connect to the new primary instance after the switchover operation completes.
  * Take an on-demand backup of the primary instance. This backup is a precaution in case you need to recover from any unexpected failures.

**Note:** For Cloud SQL to update a [write endpoint](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#connect-write-endpoint) and point it to the correct instance, make sure that your replica is on the new network architecture before the switchover operation occurs. If the instance isn't created with this architecture, then you can [upgrade the instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture).

### Perform the switchover operation

### Console

To perform the switchover operation, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the designated DR replica of the primary instance.
  3. Click the DR replica instance. The **Overview** page for the DR replica appears.
  4. Click the **Switchover** button.
  5. On the **Perform switchover between the primary and DR replica** page, enter the name of the primary instance in the **Instance ID** field.
  6. Click **Switchover**.



### gcloud

To perform the switchover operation, run the following command:
    
    
    gcloud sql instances switchover REPLICA_NAME
       [--db-timeout=TIMEOUT_DURATION ]

Replace the following variables:

  * REPLICA_NAME: the name of the designated DR replica that you want the primary instance to switch roles with.
  * TIMEOUT_DURATION: optional. the timeout period to allow for the completion of database operations on the instance.

If you don't specify this parameter, the switchover operation includes a timeout of 10 minutes.

You can increase the value of this timeout by specifying the `--db-timeout` parameter. Replace TIMEOUT_DURATION with a time period duration of up to 24 hours, including an initial notation for the format. For example, for 30 seconds, specify `30s`. For 24 hours, specify `24h`. You can also specify fractional units of time period by using decimals up to 9 places. For example, for 30.5 minutes, specify `30.5m`. 

If you don't have any pending operations, then you can decrease the value of this timeout.




### Terraform

To begin the switchover operation, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). To make the DR replica the new primary instance, use the first sample. The sample contains comments for the Terraform configuration changes you need to make to switch the primary instance and the DR replica.
    
    
    #
    # This sample provides the first part of the switchover operation and turns the DR replica
    # into the new primary instance.
    data "google_project" "default" {
    }
    
    resource "google_sql_database_instance" "original-primary" {
      name             = "mysql-original-primary-instance"
      region           = "us-east1"
      database_version = "MYSQL_8_0"
      instance_type    = "CLOUD_SQL_INSTANCE"
    
      replication_cluster {
        failover_dr_replica_name = "${data.google_project.default.project_id}:mysql-dr-replica-instance"
      }
    
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
        backup_configuration {
          enabled            = true
          binary_log_enabled = true
        }
      }
      # Set `deletion_protection` to true to ensure that one can't accidentally
      # delete this instance by use of Terraform whereas
      # `deletion_protection_enabled` flag protects this instance at the Google Cloud level.
      deletion_protection = false
      # Optional. Add more settings.
    }
    
    resource "google_sql_database_instance" "dr-replica" {
      name             = "mysql-dr-replica-instance"
      region           = "us-west2"
      database_version = "MYSQL_8_0"
      # Change the instance type from "READ_REPLICA_INSTANCE" to "CLOUD_SQL_INSTANCE".
      instance_type = "CLOUD_SQL_INSTANCE"
      # Remove or comment out the master_instance_name from the DR replica.
      # master_instance_name = google_sql_database_instance.original-primary.name
      # Add the original primary instance to a list of replicas for the new primary.
      replica_names = [google_sql_database_instance.original-primary.name]
    
      # Designate the original primary instance as the DR replica of the new primary instance.
      # The format for setting the DR replica is `project-id:dr-replica-name`.
      replication_cluster {
        failover_dr_replica_name = "${data.google_project.default.project_id}:${google_sql_database_instance.original-primary.name}"
      }
    
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
        backup_configuration {
          # Add a backup configuration section to enable automated backups and binary logging for the new primary instance.
          enabled            = true
          binary_log_enabled = true
        }
      }
      # Set `deletion_protection` to true to ensure that one can't accidentally
      # delete this instance by use of Terraform whereas
      # `deletion_protection_enabled` flag protects this instance at the Google Cloud level.
      deletion_protection = false
      # Optional. Add more settings.
    }
    

After you make your changes, update the primary and DR replica by running `terraform plan`. Verify that the output includes `Plan: 0 to add, 1 to change, 0 to destroy.` To perform the switchover, run `terraform apply`.

At this point, the original primary is a replica of the new primary instance. However, that change isn't reflected in your Terraform state automatically. To make the original primary instance a replica of the new primary instance in your Terraform state, use the second sample. The second sample provides comments that describe the changes you need to make after running the first sample.
    
    
    #
    # This sample provides the second part of the switchover operation and makes the original primary instance
    # a replica of the new primary instance. After you run `terraform apply` for this sample, you'll see
    # the following message:
    #
    # "No changes. Your infrastructure matches the configuration.
    #
    # Terraform has compared your real infrastructure against your configuration and found no differences,
    # so no changes are needed.
    #
    # Apply complete! Resources: 0 added, 0 changed, 0 destroyed."
    data "google_project" "default" {
    }
    
    resource "google_sql_database_instance" "original-primary" {
      name             = "mysql-original-primary-instance"
      region           = "us-east1"
      database_version = "MYSQL_8_0"
      # Change instance type for the original primary from "CLOUD_SQL_INSTANCE" to "READ_REPLICA_INSTANCE".
      instance_type = "READ_REPLICA_INSTANCE"
      # Set master_instance_name to the the new primary instance, the old DR replica.
      master_instance_name = "mysql-dr-replica-instance"
      # replica_names = [] # If you previously defined a replica_names field in your template, then delete the DR replica
      # (new primary) from the list of replicas.  Don't delete the entire replica_names field.
      # Instead set the field to an empty string. For example, replica_names = [""].
    
      replication_cluster {
        # This instance no longer requires a designated DR replica since it's a replica.
        # Remove the DR replica designation by setting the field to an empty string.
        failover_dr_replica_name = ""
      }
    
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
        backup_configuration {
          # Disable automated backups because this instance is now a replica.
          enabled            = false
          binary_log_enabled = true
        }
      }
      deletion_protection = false
    }
    
    resource "google_sql_database_instance" "dr-replica" {
      name             = "mysql-dr-replica-instance"
      region           = "us-west2"
      database_version = "MYSQL_8_0"
      instance_type    = "CLOUD_SQL_INSTANCE"
      replica_names    = [google_sql_database_instance.original-primary.name]
    
    
      replication_cluster {
        failover_dr_replica_name = "${data.google_project.default.project_id}:${google_sql_database_instance.original-primary.name}"
      }
    
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
        backup_configuration {
          enabled            = true
          binary_log_enabled = true
        }
      }
      deletion_protection = false
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

In the event of region failure or a disaster, you can perform DR by invoking a replica failover operation to your designated DR replica. To perform a replica failover, you promote the designated DR replica. In contrast with switchover, the promotion of the DR replica is immediate.

Since the DR replica assumes the role of the primary instance immediately, it's possible that the replica doesn't have all of the data from the old primary instance due to replication lag. For this reason, a replica failover can incur data loss.

As part of the promotion process, replica failover takes a backup of the new primary instance (the former DR replica) right after the DR replica becomes the new primary instance. After this backup is complete, point-in-time-recovery (PITR) is fully enabled on the new primary instance. This backup can take between 5 and 15 minutes to complete depending on the disk size of the new (and old) primary instance. During this backup period, PITR isn't available. 

To reduce total replica failover operation time, Cloud SQL configures and enables PITR in a separate, asynchronous operation after the failover operation completes. 

When the old primary instance comes back online, the replica failover process takes a backup. After this backup is taken, the old primary instance is recreated as a read replica of the new primary instance.

For more information about the considerations of using PITR with advanced DR, see Use PITR with advanced DR.

After you invoke the replica failover operation, the [DNS write endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint), which previously resolved to the old primary instance, resolves to the new primary instance.

**Important** : If you're not using a DNS write endpoint, then you must point your applications to use the IP address of the new primary instance.

If you [configure Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#configure-psc-outbound) on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery), then after replica failover operations, when the DR replica is promoted to the primary instance, outbound connectivity continues to work on the new primary that's created. If you don't configure outbound connectivity on the [disaster recovery (DR) replica](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery), then in order for the service to continue to work after replica failover operations, you need to enable Private Service Connect outbound connectivity on the new primary instance.

### Before you begin

Before you can perform a replica failover, do the following:

  * If you haven't done so already, then designate a DR replica. You can only perform a replica failover between the primary instance and the designated DR replica.
  * Make sure the DR replica is online and healthy.

**Note:** For Cloud SQL to update a [write endpoint](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#connect-write-endpoint) and point it to the correct instance, make sure that your replica is on the new network architecture before the replica failover operation occurs. If the instance isn't created with this architecture, then you can [upgrade the instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture).

### Perform the replica failover operation

### Console

To perform the replica failover operation, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the designated DR replica of the primary instance.
  3. Click the DR replica instance. The **Overview** page for the DR replica appears.
  4. Click the **Replica Failover** button.
  5. On the **Perform replica failover between the primary and DR replica** page, enter the name of the primary instance in the **Instance ID** field to confirm that you want to proceed with the operation.
  6. To start the replica failover, click **Replica Failover**.



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
     3. Verify that MySQL VERSION appears in the **Type** column for the new primary instance.

### gcloud

You can check the status by running the following command:
    
    gcloud sql instances describe DR_REPLICA_NAME

Replace the following variable:

     * DR_REPLICA_NAME: the name of the promoted DR replica

In the output, check that the following field appears and the replica has become a standalone Cloud SQL primary instance:
    
    **instanceType** : CLOUD_SQL_INSTANCE
    

  2. To verify the completion of the second phase, check the operations log on the instance for the message `RECONFIGURE_OLD_PRIMARY`.

The appearance of this message depends on when the old primary instance returns online, which can take minutes or days in the event of a disaster.

For more information on how to check the operations logs on an instance, see [View instance logs](https://docs.cloud.google.com/sql/docs/mysql/logging).




## Use PITR with advanced DR

With both switchover and replica failover, as soon as the DR replica is promoted to a primary instance, the following changes occur to support backup and PITR:

  * Backup configuration, including any automated backup scheduling, is copied from the old primary instance to the new primary instance.


  * If disabled, then the binlog configuration flag is turned on to enable PITR.


  * A new backup is taken to support PITR on the new primary instance.

  * The transaction log retention policy is copied from the old primary instance to the new primary instance.




For both the backup configuration and transaction log retention policies, we recommend that you verify that the settings inherited from the old primary instance are correct for the new primary instance.

### Start of PITR coverage

At the end of the switchover operation, Cloud SQL schedules automated backups and takes the first backup of the new primary instance. If you want PITR coverage to begin sooner than later, then we recommend that you verify that the first backup is successful. The newly promoted primary instance has PITR coverage _only_ after the first automated backup has completed successfully.

For more information about how to view the backups that are available for an instance, see [View a list of backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#viewbackups).

### PITR coverage for instances during switchover and replica failover

When an instance participates in a switchover or a replica failover operation, the instance spends time as a read replica. PITR and restoring a backup are supported during the time period that the instance spends as a read replica and as a primary instance.

You can perform PITR to a time before the switchover when the instance was a primary instance. For both switchover and replica failover operations, Cloud SQL initiates a best-effort backup for the new primary instance as soon as the new primary instance is promoted. PITR is enabled on the promoted instance only after this backup is completed. This backup can take 5 to 15 minutes to complete depending on the disk size.

Cloud SQL performs this PITR enablement asynchronously, after the switchover or replica failover operation completes, so it doesn't add to the time that the operation takes.

### Split-brain during replica failover

It's possible that split-brain occurs when the primary instance continues to accept writes while a replica is promoted using replica failover. After the replica is promoted, when the old primary instance is available again, it is rebuilt as a replica of the promoted instance and a final backup is made. This backup can be used to recover any split-brain data that was not written to the promoted replica.

**Note:** Split-brain can't happen for switchover operations.

### Deletion of backups and transaction logs on replicas

If a primary instance that was enabled with PITR and backups becomes a read replica, then the last backup and PITR retention policy from its time as a primary instance is preserved and applied during its time as a replica. Even though the new primary instance is not taking backups, the old backups and transaction logs used for PITR are deleted on the read replica according to the last configured policy.

For example, if the instance is configured to have daily automated backups and keep 7 backups with 7 days of PITR logs, then when this instance becomes a read replica, anything older than 7 days is deleted once a day.

If you need to delete backups sooner, then you can remove backups manually. For more information, see [Delete a backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#delete-backup).

**Note:** You can't modify backup configuration settings while the instance is a replica.

### Recommendations for VPC Service Controls and advanced DR

If you use VPC Service Controls, then make sure that your service perimeters allow necessary communications for all recovery operations such as point-in-time recovery (PITR) operations, especially when you use CMEK with keys in a different project.

Advanced DR operations, like switchover and replica failover, can enable or reconfigure features like PITR, which can be blocked by VPC Service Controls if the service perimeters aren't configured correctly for CMEK and cross-project key access.

  * **Keep KMS key project in same perimeter as instance** : as a best practice, include the project containing the KMS key in the same VPC Service Controls perimeter as your Cloud SQL instances.
  * **Use a perimeter bridge** : as a secondary (less recommended) option, you can use a [perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters) to connect projects in different perimeters.
  * **Test** : use VPC Service Controls dry run mode to test your DR procedures (like switchover) and identify potential VPC Service Controls violations without enforcement.



For more information, see [Configure VPC Service Controls](https://docs.cloud.google.com/sql/docs/mysql/admin-api/configure-service-controls).

## Limitations

  * You can't designate a Cloud SQL Enterprise Plus edition read replica instance as DR replica if the primary instance stores its transaction logs for point-in-time recovery (PITR) on disk. To check where an instance stores its logs for PITR, see [Check the storage location of transaction logs used for PITR](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/configure-pitr#check-log-storage-location).

  * You can't designate an external replica as a DR replica.

  * Terraform isn't supported for replica failover operations.




## Troubleshoot

Issue | Troubleshooting  
---|---  
Switchover operation has failed. | 

  * Make sure that the instance meets all the stated DR replica requirements. 
  * Check the volume of transactions on the database. Switchover secures binary logs of the primary instance in Cloud Storage before it performs switchover. If the transaction volume is high, then the operation might timeout. Consider retrying the operation when the transaction load is lower.

  
Switchover operation has failed and the primary instance is stuck in read-only mode. |  Perform a database restart to bring the primary instance back to write mode.  
Switchover operation has completed, but the Google Cloud console doesn't show the new reversed roles for the instances. | Refresh your browser to show the updated topology.  
Replica failover operation has failed. | 

  * Make sure that a DR replica is designated for the primary instance and is online.
  * If failover to the DR replica has failed, then promote to a regular (non-DR) read replica instead.

  
After a switchover operation, the new replica fails to replicate with error "Cannot replicate to server ... because the present server has purged required binary logs". |  One root cause is if you run certain administrative commands on a read replica that has binary logging enabled (such as a disaster recovery replica), MySQL increments the replica's GTID (`gtid_executed`) with the replica's own server UUID. After a switchover operation, when the former primary instance becomes a read replica of the promoted DR replica, replication fails because the binary logs containing these local GTID transactions have already been purged. To prevent such replication failures after a switchover, avoid running the following commands on a read replica:

  * `FLUSH TABLES`
  * `FLUSH PRIVILEGES`
  * `REPAIR TABLE TABLE_NAME`
  * `FLUSH SLOW LOGS`
  * `FLUSH GENERAL LOGS`

If you must run any of these commands on a read replica, then disable binary logging for your client session before you run the command:
    
    
    SET SESSION sql_log_bin = 0;
      
  
Can't tell if replication isn't happening | [Connect to the replica](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip) and type: 
    
    
    show slave status;
    

  * If replication is happening, then the first column "`Slave_IO_State`" shows "`Waiting for master to send event`" and the "`Last_IO_Error`" field is empty.
  * If replication is **not** happening, then the first column `"Slave_IO_State"` shows `"Connecting to master"`. and the `"Last_IO_Error"` field shows an error similar to `"error connecting to master 'cloudsqlreplica@x.x.x.x:3306"`.

You can also view the replication status for the replicas in the Cloud SQL monitoring dashboard. For more information, see [Monitor Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance#cloud-monitoring).  
You received the following error message: `"Instance was converted into a replica between the target PITR time and the last available base backup. PITR logs are not available for the period instance was a replica. Please clone from the instance that was primary at time %s"` | You can't perform PITR for a time period when an instance underwent switchover to a replica. The PITR logs are not available for the time period when the instance was a replica.

  * Review the list of operations for the instance to determine whether the instance was a replica at that point in time
  * Use the list of operations to determine which instance was the primary instance at that point in time.
  * Clone that instance to perform PITR.

  
You received the following error message: ` "You can only designate a disaster recovery (DR) replica for primary instances that are storing their PITR logs in Cloud Storage. PITR logs of the instance %s are not stored in Cloud Storage"` | Your primary instance has not switched the storage location of its transaction logs to Cloud Storage yet. You can try again again after the storage location for the transaction logs has been switched, or you can try designating a DR replica for a different primary instance. For more information about moving the storage location of the transaction logs used for PITR, see [Using point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr).  
You received the following error message: `"The specified failover dr replica name REPLICA_NAME must be one of the replicas of the primary instance INSTANCE_NAME`." |  For more information about how to designate a DR replica and the correct command syntax, see  Designate the DR replica for the primary instance.  
  
## What's next

  * View all the [Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations).
  * Read about [database observability](https://docs.cloud.google.com/sql/docs/mysql/observability)
  * [Monitor Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
