---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica/
title: Create read replicas \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:28.102495+00:00
---

# Create read replicas  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create read replicas Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica "View this page for the SQL Server database engine")

This page describes how to create a read replica for a Cloud SQL instance.

A read replica is a copy of the primary instance that reflects changes to the primary in almost real time, in normal circumstances. You can use a read replica to offload read requests or analytics traffic from the primary instance.

Additionally, for disaster recovery, you can perform a regional migration. If a replica is a [ cross-region replica](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas), you can perform a failover to another region; specifically, you can promote a replica to a standalone instance (in which case, existing replicas would not consider that instance as primary).

**Note:** Don't use a replica as the source for systems like Datastream or Kafka. If a replica is recreated (because of replication breakage, for example), then the replica inherits the primary disk and can lose binary logs, which will break downstream replication. In such a scenario, systems like Datastream or Kafka must be re-initialized to stream from this replica.

For more information about how replication works, see [Replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/replication).

## Before you begin

If you are creating the first replica for this instance, ensure that the instance meets the requirements for primary instances. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/replication#requirements).

**Note:** For information about using parallel replication for performance improvements, see [ Configuring parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication).

## Create a read replica

The steps for creating a read replica are below.

**Note** : If you specify MySQL 8.4 as the database version for your replica, then the default Cloud SQL edition is Enterprise Plus. If you don't specify a database version or you specify a version other than MySQL 8.4, then the default Cloud SQL edition is Enterprise.

If the primary instance has a [private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip) connection and the instance accepts database connections from [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/mysql/language-connectors) only, then you can't create read replicas for the instance.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance for which you want to create a replica, and then open the `more actions` menu next to the listing.
  3. Select **Create read replica**. 

If you don't see that choice, then the instance is a replica; you can't create a replica of a replica.

  4. If the instance had backups and binary logging enabled, continue with the next step. Otherwise, select **Automate backups** and **Enable binary logging** , click **Continue** , and then click **Save and restart** to restart the instance. 

Enabling binary logging causes the instance to be restarted.

  5. In the **Customize your instance** section of the page, update settings for your replica. Begin by clicking **Show configuration options** to display the groups of settings. Then, expand the desired groups to review and customize the settings. A **Summary** of all the options you select appears on the right. Customizing these settings is optional. Defaults are assigned in every case where no customizations are made.

For more details about each setting, see the [About instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings) page.

For example, to allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over an internal connection, expand the **Connections** group, and then deselect the **Public IP** check box.

  6. Click **Create replica**. 

Cloud SQL creates a backup, if needed, and creates the replica. You are returned to the instance page for the primary.




### gcloud

  1. Check the status of the primary instance: 
         
         gcloud sql instances describe PRIMARY_INSTANCE_NAME
               

If the `databaseReplicationEnabled` property is `true`, the instance is a replica; you cannot create a replica of a replica.

  2. If the `enabled` property under `backupConfiguration` is `false`, enable backups for the primary instance now: 
         
         gcloud sql instances patch PRIMARY_INSTANCE_NAME \
         --backup-start-time=>HH:MM
               

The `backup-start-time` parameter is specified in 24-hour time, in the UTC±00 time zone, and specifies the start of a 4-hour backup window. Backups can start any time during the backup window. 
  3. If the `binaryLogEnabled` property is `false`, enable binary logs on the primary instance: 
         
         gcloud sql instances patch PRIMARY_INSTANCE_NAME \
         --enable-bin-log

Enabling binary logs causes the instance to be restarted. 
  4. Create the replica: 
         
         gcloud sql instances create REPLICA_NAME \
         --master-instance-name=PRIMARY_INSTANCE_NAME

You can specify a different tier size using the `--tier` parameter, if needed. If you're creating a replica from a primary instance for MySQL 8.4 and later, and the Cloud SQL edition for the instance is either Enterprise or is Enterprise Plus, then you don't have to specify a value for this parameter. The replica inherits the machine type from the primary instance.

You can specify a different region using the `--region` parameter.

You can add more parameters for other instance settings. To learn more, see [gcloud sql instances create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create).

If the primary instance has an internal IP address only, and you want to allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over an internal connection, then add the `--enable-google-private-path` parameter to the command.

You must create the replica in the same VPC network as the primary instance. You can also specify an `allocated-ip-range-name` in that VPC network. If no range is specified, the replica is created in a random range.



  * Binary logging is supported on read replica instances (MySQL 5.7 and later only. Not supported on legacy HA failover replicas). Enable binary logging on a replica with the same `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)` command, using the replica's instance name instead of the primary's instance name. 
        
        gcloud sql instances patch REPLICA_INSTANCE_NAME \
        --enable-bin-log \
        --enforce-new-sql-network-architecture
            

Binary logging durability on the replica (but not on the primary) instance can be set with the [`sync_binlog`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-s) flag, which controls how often the MySQL server synchronizes the binary log to disk.

Backups cannot be enabled on replica instances, but binary logging can be enabled on a replica even when backups are disabled, unlike the primary.

The binlog retention period on replica instances is automatically set to one day, unlike seven days on primary instances.

  * Use the `enforce-new-network-architecture` flag to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip). 



### Terraform

To create a read replica, use [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "read_replica" {
      name                 = "mysql-replica-instance-name"
      master_instance_name = google_sql_database_instance.primary.name
      region               = "europe-west4"
      database_version     = "MYSQL_8_0"
    
      replica_configuration {
        failover_target = false
      }
    
      settings {
        tier              = "db-n1-standard-2"
        availability_type = "ZONAL"
        disk_size         = "100"
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }

#### Apply the changes

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

#### Delete the changes

To delete your changes, do the following:

  1. To disable deletion protection, in your Terraform configuration file set the `deletion_protection` argument to `false`. 
         
         deletion_protection =  "false"

  2. Apply the updated Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply



  3. Remove resources previously applied with your Terraform configuration by running the following command and entering `yes` at the prompt:
         
         terraform destroy




### REST v1

  1. **Get the current backup configuration**

Use the [`get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get) method of the instances resource to return the database version and current backup configuration for the primary. 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * primary-instance-name: The name of the primary instance

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/primary-instance-name

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/primary-instance-name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/primary-instance-name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    "backupConfiguration": {
        "kind": "sql#backupConfiguration",
        "startTime": "12:00",
        "enabled": false,
        "binaryLogEnabled": false
    }
    

  2. **Verify that the replication fields are set**

If either `enabled` or `pointInTimeEnabled` are `false`, use the [`patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method of the instances resource to enable them both. In the request, specify any properties of the backup configuration that you wish to change. 

To enable backups, set `enabled` to `true` and the `startTime` to a time of day in `HH:MM` format. The `startTime` parameter is specified in 24-hour time, in the UTC±00 time zone, and specifies the start of a 4-hour backup window. Backups can start any time during the backup window.

To enable point-in-time recovery, set `pointInTimeEnabled` to `true`.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the primary or read replica instance that you're configuring for high availability
     * START_TIME: the time (in hours and minutes)

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "startTime": "START_TIME",
          "enabled": true,
          "binaryLogEnabled": true
        }
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. **Create the read replica**

Use the [ `insert`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert) method of the instances resource to create the read replica. The `databaseVersion` property must be the same as the primary. If the primary instance uses an internal IP address, you can specify an `allocatedIpRange` the same way as when you [create a primary instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen). If no range is specified, the replica is created in a random range. For a cross-region read replica, specify a region other than the primary instance's region.

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * database-version: Enum version string (for example, MYSQL_8_0)
     * primary-instance-name: The name of the primary instance
     * primary-instance-region: The region of the primary instance
     * replica-region: The region of the replica instance
     * replica-name: The name of the replica instance
     * machine-type: Enum string of the machine type. For example: "db-custom-1-3840"
     * private-network: The authorized network that you're adding or selecting to create a private connection.
You set the value of the `ipv4Enabled` parameter to `false` because you want the Cloud SQL instance to be associated with a private IP address, not a public IP one.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances

Request JSON body: 
    
    {
      "masterInstanceName": "primary-instance-name",
      "project": "project-id",
      "databaseVersion": "database-version",
      "name": "replica-name",
      "region": "replica-region",
      "settings":
      {
        "tier": "machine-type",
        "settingsVersion": 0,
        "ipConfiguration": {
        object (IpConfiguration)
      },
      {
      "ipv4Enabled": false,
      "privateNetwork": private-network,
      "requireSsl": boolean,
      "authorizedNetworks": [
        {
          object (AclEntry)
        }
      ],
      "allocatedIpRange": string
        }
      },
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE_REPLICA",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




### REST v1beta4

  1. **Get the current backup configuration**

Use the [`get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/get) method of the instances resource to return the database version and current backup configuration for the master. 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * primary-instance-name: The name of the primary instance

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/primary-instance-name

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/primary-instance-name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/primary-instance-name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    "backupConfiguration": {
        "kind": "sql#backupConfiguration",
        "startTime": "12:00",
        "enabled": false,
        "binaryLogEnabled": false
    }
    

  2. **Verify that the replication fields are set**

If either `enabled` or `binaryLogEnabled` are `false` on the primary instance, use the [`patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) method of the instances resource to enable them both. In the request, specify any properties of the backup configuration that you want to change. 

To enable backups, set `enabled` to `true` and the `startTime` to a time of day in `HH:MM` format. The `startTime` parameter is specified in 24-hour time, in the UTC±00 time zone, and specifies the start of a 4-hour backup window. Backups can start any time during the backup window.

To enable point-in-time recovery, set `binaryLogEnabled` to `true` on the primary instance.

Binary logging is supported on read replica instances (MySQL 5.7 and later only). Enable binary logging on a replica with the same API, using the replica's instance ID instead of the primary's instance ID. 

Binary logging durability on the replica (but not on the primary) instance can be set with the [`sync_binlog`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-s) flag, which controls how often the MySQL server synchronizes the binary log to disk. 

Backups cannot be enabled on replica instances, but binary logging can be enabled on a replica even when backups are disabled, unlike the primary. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the primary or read replica instance that you're configuring for high availability
     * START_TIME: the time (in hours and minutes)

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "startTime": "START_TIME",
          "enabled": true,
          "binaryLogEnabled": true
        }
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
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. **Create the read replica**

Use the [ `insert`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert) method of the instances resource to create the read replica. The `databaseVersion` property must be the same as the primary. If the primary instance uses an internal IP address, you can specify an `allocatedIpRange` the same way as when you [create a primary instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen). For a cross-region read replica, specify a region other than the primary instance's region.

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * database-version: Enum version string (for example, MYSQL_8_0)
     * primary-instance-name: The name of the primary instance
     * primary-instance-region: The region of the primary instance
     * replica-region: The region of the replica instance
     * replica-name: The name of the replica instance
     * machine-type: Enum string of the machine type. For example: "db-custom-1-3840"
     * private-network: The authorized network that you're adding or selecting to create a private connection.
You set the value of the `ipv4Enabled` parameter to `false` because you want the Cloud SQL instance to be associated with a private IP address, not a public IP one.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances

Request JSON body: 
    
    {
      "masterInstanceName": "primary-instance-name",
      "project": "project-id",
      "databaseVersion": "database-version",
      "name": "replica-name",
      "region": "replica-region",
      "settings":
      {
        "tier": "machine-type",
        "settingsVersion": 0,
        
        "ipConfiguration": {
        object (IpConfiguration)
      },
      {
      "ipv4Enabled": false,
      "privateNetwork": private-network,
      "requireSsl": boolean,
      "authorizedNetworks": [
        {
          object (AclEntry)
        }
      ],
      "allocatedIpRange": string
        }
        
      },
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE_REPLICA",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




## Create a read replica of an instance with Private Service Connect enabled

To create a read replica of an instance with [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect) enabled, use [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API. You can create this replica in either the same region or in a different region from the primary instance ([cross-region read replica](https://docs.cloud.google.com/sql/docs/mysql/replication#cross-region-read-replicas)).

The read replica can't replicate from an instance with a different connectivity type. For example, an instance with Private Service Connect enabled can replicate only from another Private Service Connect instance. It also can't replicate from an instance that supports external IP connections or from an instance that's configured with [private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access).

### gcloud

To create a read replica of an instance, use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command:
    
    
    gcloud sql instances create REPLICA_INSTANCE_NAME \
    --master-instance-name=PRIMARY_INSTANCE_NAME \
    --project=PROJECT_ID \
    --region=REGION_NAME \
    --enable-private-service-connect \
    --allowed-psc-projects=ALLOWED_PROJECTS \
    --availability-type=AVAILABILITY_TYPE \
    --no-assign-ip

Make the following replacements:

  * REPLICA_INSTANCE_NAME: the name of the replica instance.
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * REGION_NAME: the region name for the replica instance.
  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-endpoint). If you're using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#connect-cloud-sql-auth-proxy) or [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#connect-using-language-connectors), then create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.

  * AVAILABILITY_TYPE: enable high availability for the instance. For this parameter, specify one of the following values: 
    * `REGIONAL`: enable high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provide no failover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#deactivate-ha-instance).




### REST v1

Before using any of the request data, make the following replacements: 

  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * REPLICA_INSTANCE_NAME: the name of the replica instance.
  * REGION_NAME: the region name for the replica instance.
  * MACHINE_TYPE: the machine type for the instance.
  * AVAILABILITY_TYPE: enable high availability for the instance. For this parameter, specify one of the following values: 
    * `REGIONAL`: enable high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provide no failover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#deactivate-ha-instance).

  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-endpoint). If you're using the Cloud SQL Auth proxy or Cloud SQL Language Connectors, then you must create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.




HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "MYSQL_8_0",
      "name": "REPLICA_INSTANCE_NAME",
      "region": "REGION_NAME",
      "kind": "sql#instance",
      "settings":
      {
        "tier": "MACHINE_TYPE",
        "availabilityType": "AVAILABILITY_TYPE",
        "settingsVersion": 0,
        "ipConfiguration": {
          "ipv4Enabled": false,
          "pscConfig": {
            "allowedConsumerProjects": [ALLOWED_PROJECTS],
            "pscEnabled": true
          }
        },
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "ASYNCHRONOUS",
        "tier": "MACHINE_TYPE"
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
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "CREATE_REPLICA",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * REPLICA_INSTANCE_NAME: the name of the replica instance.
  * REGION_NAME: the region name for the replica instance.
  * MACHINE_TYPE: the machine type for the instance.
  * AVAILABILITY_TYPE: enable high availability for the instance. For this parameter, specify one of the following values: 
    * `REGIONAL`: enable high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provide no failover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#deactivate-ha-instance).

  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-endpoint). If you're using the Cloud SQL Auth proxy or Cloud SQL Language Connectors, then you must create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.




HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "MYSQL_8_0",
      "name": "REPLICA_INSTANCE_NAME",
      "region": "REGION_NAME",
      "kind": "sql#instance",
      "settings":
      {
        "tier": "MACHINE_TYPE",
        "availabilityType": "AVAILABILITY_TYPE",
        "settingsVersion": 0,
        "ipConfiguration": {
          "ipv4Enabled": false,
          "pscConfig": {
            "allowedConsumerProjects": [ALLOWED_PROJECTS],  
            "pscEnabled": true
          }
        },
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "ASYNCHRONOUS",
        "tier": "MACHINE_TYPE"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "CREATE_REPLICA",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Configure read replicas for IAM database authentication

Read replicas do not have the `cloudsql_iam_authentication` flag enabled automatically when it is enabled on the primary instance. 

To configure a read replica for IAM database authentication:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the Configuration tile, look for the `cloudsql_iam_authentication` flag. If the flag isn't on the list, enabling the flag in the read replica is unnecessary. If the flag is on the list, you must enable the flag on the read replica. If you need to enable the flag on the read replica, continue with the next step..
  4. Select **Replicas** from the SQL navigation menu.
  5. Click the name of the replica you want to edit.
  6. Click **Edit**.
  7. In the **Configuration options** section, expand **Flags**. 
  8. Select **\+ Add** item.
  9. Enter `cloudsql_iam_authentication` for the flag name. Make sure that **On** is selected for this flag.
  10. Click **Save**.



## Create cascading replicas

This section describes how to create and manage cascading replicas.

For information about how cascading replicas work, see [Cascading replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#cascading-replicas).

### Steps to create a cascading replica

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. For MySQL 5.7 or later, [enable replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#enable_replication).
  3. Click the **Replicas** tab for the replica that will act as a parent for the replica that you want to create.
  4. Click **Create replica**.
  5. On the **Create read replica** page, update the instance ID, and any other configuration options, including the name, region, and zone.
  6. Click **Create**. 

Cloud SQL creates a replica. You're returned to the instance page for the parent replica.

  7. Follow steps 4-6 for each new cascading replica that you want to create.



### gcloud

  1. If you're using MySQL version 5.7 or later, then enable binlogs for the primary of the new replica:  

         
         gcloud sql instances patch --enable-bin-log PARENT_REPLICA_NAME

Replace PARENT_REPLICA_NAME with the name of the parent replica. 
  2. Create the new replica by specifying your primary replica as the primary instance using the [`--master-instance-name`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) flag:
    
    gcloud sql instances create REPLICA_NAME \
          --master-instance-name=PARENT_REPLICA_NAME \

Replace the following:  

     * REPLICA_NAME: the unique ID for the replica that you are creating
     * PARENT_REPLICA_NAME: the name of the parent replica
  3. After you create the cascading replica, you can see that the changes made to the primary instance are replicated through all the replicas in the cascading replicas chain.



### curl

  1. If you are using MySQL version 5.7 or later, enable binary logging:   
  
To enable binary logging, save the following JSON in a file named request.JSON, then invoke the curl command to enable binary logging.   

         
         {
           "settings":
           {
             "backupConfiguration":
             {
               "enabled": false,
               "binaryLogEnabled": true
             }
           }
         }

  2. To create a replica under the parent replica, edit the following JSON code sample, and save it to a file called `request.json`: 
         
         {
           "masterInstanceName": "PARENT_REPLICA_NAME",
           "project": "PROJECT_ID",
           "name": "REPLICA_NAME",
           "region": "REPLICA_REGION",
           "settings":
             {
               "tier": "MACHINE_TYPE",
             }
         }

  3. Run the following command: 
         
         curl -X POST
         -H "Authorization: Bearer "$(gcloud auth print-access-token)
         -H "Content-Type: application/json; charset=utf-8"
         -d @request.json
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"




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

  * Learn how to [manage replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas).
  * Learn about [cross-region replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas).
  * Learn about [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
