---
url: https://docs.cloud.google.com/sql/docs/postgres/read-pool-autoscaling/
title: Read pool autoscaling \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:05.171807+00:00
---

# Read pool autoscaling  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/read-pool-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Read pool autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/read-pool-autoscaling "View this page for the MySQL database engine") | PostgreSQL | SQL Server

Read pool autoscaling automatically adds or removes [read pool nodes](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools#what-are-read-pools) in the [read pool](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools#what-are-read-pools) based on your application's workload needs.

You can control read pool autoscaling by either limiting the average CPU utilization across the read pool or by limiting the number of client connections allowed access to the read pool, using one of two target metrics:

  * **Average CPU utilization** : lets you set the average CPU usage you want the read pool to operate within. The read pool automatically [scales in or out](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools#what_are_read_pools) based on your application's workload CPU usage.
  * **Average database connections** : lets you specify the average number of client database connections that should be served by each node. The read pool automatically [scales in or out](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools#what_are_read_pools) based on the number of client connections.



To apply these target metrics, you must also set a minimum and maximum read pool node count.

To enable read pool autoscaling, you can configure one or both of these target metrics on the instance. If both metrics are active, Cloud SQL applies the maximum read pool node count indicated by both metrics.

The following table lists the limits for each target metric:

Target metric name | Limits | Related public metric | Average CPU utilization | Between 0.1 and 0.9. | The [average CPU utilization](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics) (`cloudsql.googleapis.com/database/cpu/utilization`) across the read pool nodes in the read pool.  
---|---|---  
Average database connections |  Between 10 and 262,142. Note: The maximum acceptable value correlates to the maximum value set by the `max_connections` database flag.  |  Represents an [average of database client connections](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics) (`cloudsql.googleapis.com/database/postgresql/num_backends`) across the read pool nodes in the read pool. Note: When [Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling) is enabled on the instance, the individual connections that make up a connection pool aren't separately counted and included in the `AVERAGE_DB_CONNECTIONS` metric. If Managed Connection Pooling is enabled, then we recommend using only the `AVERAGE_CPU_UTILIZATION` metric to control read pool autoscaling.   
  
When the conditions are met to resize the read pool, read pool autoscaling operations can be viewed from the Google Cloud console. All other operations on the read pool and the primary instance are blocked until read pool autoscaling completes.

## Read pool autoscaling characteristics

The following characteristics apply:

  * Scale in operations remove only one node at a time.
  * Scale out operations add, in parallel, as many nodes as needed.
  * By default, both scale-in and scale-out operations are applied. You can optionally block scale-in operations by manually disabling them (`disableScaleIn`).
  * By default, a cooldown period of 600 seconds is applied between successive read pool autoscaling operations. A minimum cooldown period of 60 seconds is required whether scaling in or out.
  * When setting a target metric, you must also define the minimum (`minNodeCount`) and maximum (`maxNodeCount`) read pool node count you want to use. If you enable autoscaling on an existing read pool, then the current read pool size must fall within the range you set.



### Limitations

The following limitations apply:

  * If you want to create a new read pool or scale an existing read pool, then you must wait for previous create and scaling operations to complete. This applies to operations associated with the read pool as well as other read pools associated with the same primary instance. If you try to run concurrent operations, you might receive the following error message: 
        
        Operation failed because another operation was already in progress.
        




## Before you begin

  * Make sure you complete all required [prerequisite steps](https://docs.cloud.google.com/sql/docs/postgres/create-read-pool#before_you_begin) to create a read pool.

  * Make sure to use [`gcloud` version 544.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#54400_2025-10-21) or later.

  * Make sure to use [Terraform provider version](https://github.com/hashicorp/terraform-provider-google/releases/tag/v7.8.0) 7.8.0 or later.



  * Make sure to also set appropriate values for `max_wal_senders` and `max_replication_slots`. For more information, see [Read pool characteristics](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools#read-pool-characteristics).



## Create a read pool with autoscaling enabled

If you specify a target value of 0.50 for `AVERAGE_CPU_UTILIZATION`, read pool nodes will be added or removed from the read pool to keep the average CPU utilization across the read pool at 0.50 or less.

### gcloud

To create a read pool with autoscaling enabled, run the following:
    
    
      gcloud sql instances create READ_POOL_NAME \
      --tier=MACHINE_TIER --edition=ENTERPRISE_PLUS \
      --instance-type=READ_POOL_INSTANCE --node-count=NODE_COUNT \
      --database-version=DATABASE_VERSION \
      --master-instance-name=PRIMARY_INSTANCE_NAME \
      --region=REGION --network=NETWORK_NAME \
      --no-assign-ip \
      --auto-scale-enabled \
      --auto-scale-max-node-count=MAX_NODE_COUNT \
      --auto-scale-min-node-count=MIN_NODE_COUNT \
      --auto-scale-target-metrics=TARGET_METRIC_1=VALUE_1
      

Replace the following:

  * READ_POOL_NAME: the name you want to assign the read pool.
  * MACHINE_TIER: the machine tier you want to use, such as `db-perf-optimized-N-2`.
  * NODE_COUNT: the read pool node count you want to start with.
  * DATABASE_VERSION: the database version you want to use, such as `POSTGRES_16`.
  * PRIMARY_INSTANCE_NAME: the name of the primary instance you want to use.
  * REGION: the region you want to use, such as `us-east1`.
  * NETWORK_NAME: the name of the network you want to use.
  * MAX_NODE_COUNT: the maximum number of read pool nodes you want the read pool to use, such as `5`.
  * MIN_NODE_COUNT: the minimum number of read pool nodes you want the read pool to use, such as `1`.
  * TARGET_METRIC_1: the target metric you want to use, such as the following: 
    * `AVERAGE_CPU_UTILIZATION`
    * `AVERAGE_DB_CONNECTIONS`
You must define at least one of the two available metrics.
  * VALUE_1: the value you want to assign for the target metric you previously indicated. For example, for the `AVERAGE_CPU_UTILIZATION` target metric, you might assign the value `0.50`.



### Terraform

To create a read pool with autoscaling enabled, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).

The following example includes resources for the primary instance and the read pool.
    
    
    resource "google_sql_database_instance" "primary" {
      name             = "postgres-primary"
      database_version = "POSTGRES_17"
      region           = "europe-west4"
    
      instance_type = "CLOUD_SQL_INSTANCE"
    
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
    
        backup_configuration {
          enabled = true
        }
    
        ip_configuration {
          ipv4_enabled = true
        }
      }
    }
    
    resource "google_sql_database_instance" "replica" {
      name             = "postgres-replica"
      database_version = "POSTGRES_17"
      region           = "europe-west4"
    
      master_instance_name = google_sql_database_instance.primary.name
      instance_type        = "READ_POOL_INSTANCE"
      node_count           = 2
    
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
    
        ip_configuration {
          ipv4_enabled = true
        }
        read_pool_auto_scale_config {
          enabled                    = true
          disable_scale_in           = false
          max_node_count             = 20
          min_node_count             = 2
          scale_in_cooldown_seconds  = 600
          scale_out_cooldown_seconds = 600
          target_metrics {
            metric       = "AVERAGE_CPU_UTILIZATION"
            target_value = 0.5
          }
        }
      }
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

To create a read pool with autoscaling enabled, use a POST request with the [instances:insert](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/insert) method.

Before using any of the request data, make the following replacements: 

  * READ_POOL_NAME: the name you want to assign the read pool.
  * REGION: the region where you want the instance to reside, such as `us-central1`.
  * PRIMARY_INSTANCE_ID: the ID of the primary instance you want to use.
  * PROJECT_ID: the ID of the project where you want the read pool to be located, such as `my-project-name`.
  * DATABASE_VERSION: the database version you want to use, such as `POSTGRES_16`.
  * MACHINE_TIER: the machine tier you want to use, such as `db-perf-optimized-N-2`.
  * FULL_NETWORK_NAME: the name of the network you want to use.
  * MAX_NODE_COUNT: the maximum number of read pool nodes you want the read pool to use, such as `10`.
  * MIN_NODE_COUNT: the minimum number of read pool nodes you want the read pool to use, such as `2`.
  * TARGET_METRIC_1: the target metric you want to use, such as `AVERAGE_CPU_UTILIZATION` or `AVERAGE_DB_CONNECTIONS`. You must define at least one of the two available metrics.
  * VALUE_1: the value you want to assign for the target metric you previously indicated. For example, for the `AVERAGE_CPU_UTILIZATION` target metric, you might assign the value `0.50`.
  * NODE_COUNT: the read pool node count you want to start with, such as `3`.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name":"READ_POOL_NAME",
      "region":"REGION",
      "masterInstanceName":"PRIMARY_INSTANCE_ID",
      "project":"PROJECT_ID",
      "databaseVersion":"DATABASE_VERSION",
      "settings":{
        "tier":"MACHINE_TIER",
        "edition":"ENTERPRISE_PLUS",
        "ipConfiguration":{
          "privateNetwork":"FULL_NETWORK_NAME",
          "ipv4Enabled": false
        },
        "readPoolAutoScaleConfig":{
          "enabled": true,
          "minNodeCount": MIN_NODE_COUNT,
          "maxNodeCount": MAX_NODE_COUNT,
          "targetMetrics": [
            {
              "metric":"TARGET_METRIC_1",
              "targetValue": VALUE_1
            }
          ]
        }
      },
      "instanceType":"READ_POOL_INSTANCE",
      "nodeCount": NODE_COUNT
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
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/PRIMARY_INSTANCE_ID",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "PRIMARY_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

To create a read pool with autoscaling enabled, use a POST request with the [instances:insert](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/insert) method.

Before using any of the request data, make the following replacements: 

  * READ_POOL_NAME: the name you want to assign the read pool.
  * REGION: the region where you want the instance to reside, such as `us-central1`.
  * PRIMARY_INSTANCE_ID: the ID of the primary instance you want to use.
  * PROJECT_ID: the ID of the project where you want the read pool to be located, such as `my-project-name`.
  * DATABASE_VERSION: the database version you want to use, such as `POSTGRES_16`.
  * MACHINE_TIER: the machine tier you want to use, such as `db-perf-optimized-N-2`.
  * FULL_NETWORK_NAME: the name of the network you want to use.
  * MAX_NODE_COUNT: the maximum number of read pool nodes you want the read pool to use, such as `10`.
  * MIN_NODE_COUNT: the minimum number of read pool nodes you want the read pool to use, such as `2`.
  * TARGET_METRIC_1: the target metric you want to use, such as the following: 
    * `AVERAGE_CPU_UTILIZATION`
    * `AVERAGE_DB_CONNECTIONS`
You must define at least one of the two available metrics.
  * VALUE_1: the value you want to assign for the target metric you previously indicated. In this example, for the `AVERAGE_CPU_UTILIZATION` target metric, assign the value `0.50`.
  * NODE_COUNT: the read pool node count you want to start with, such as `3`.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name":"READ_POOL_NAME",
      "region":"REGION",
      "masterInstanceName":"PRIMARY_INSTANCE_ID",
      "project":"PROJECT_ID",
      "databaseVersion":"DATABASE_VERSION",
      "settings":{
        "tier":"MACHINE_TIER",
        "edition":"ENTERPRISE_PLUS",
        "ipConfiguration":{
          "privateNetwork":"FULL_NETWORK_NAME",
          "ipv4Enabled": false
        },
        "readPoolAutoScaleConfig":{
          "enabled": true,
          "minNodeCount": MIN_NODE_COUNT,
          "maxNodeCount": MAX_NODE_COUNT,
          "targetMetrics": [
            {
              "metric":"TARGET_METRIC_1",
              "targetValue": VALUE_1
            }
          ]
        }
      },
      "instanceType":"READ_POOL_INSTANCE",
      "nodeCount": NODE_COUNT
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
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
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/PRIMARTY_INSTANCE_ID",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "PRIMARTY_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Enable read pool autoscaling on an existing read pool

If you already have a read pool created, then you can enable autoscaling by indicating the autoscaling configuration you want to use.

For example, if you specify a target value of `50` for `AVERAGE_DB_CONNECTIONS`, nodes will be added or removed from the read pool to keep the average database connections across the pool at 50 or less.

### gcloud

To enable read pool with autoscaling on an existing read pool, run the following command.
    
    
      gcloud sql instances patch INSTANCE
      --auto-scale-enabled
      --auto-scale-max-node-count=MAX_NODE_COUNT
      --auto-scale-min-node-count=MIN_NODE_COUNT
      --auto-scale-out-cooldown-seconds=COOLDOWN_SECONDS_SCALE_OUT
      --auto-scale-in-cooldown-seconds=COOLDOWN_SECONDS_SCALE_IN
      --auto-scale-target-metrics=TARGET_METRIC_1=VALUE_1
      

Replace the following:

  * INSTANCE_NAME: the instance name associated with the read pool you want to modify.
  * MAX_NODE_COUNT: the maximum number of read pool nodes you want the read pool to use, such as `10`.
  * MIN_NODE_COUNT: the minimum number of read pool nodes you want the read pool to use, such as `2`.
  * COOLDOWN_SECONDS_SCALE_OUT: Optional: the cooldown or wait time in seconds between read pool node creation or deletion, such as `180`. A minimum cooldown period of 60 seconds is required. The default value is 600 seconds.
  * COOLDOWN_SECONDS_SCALE_IN: Optional: the cooldown or wait time in seconds between read pool node creation or deletion, such as `180`. A minimum cooldown period of 60 seconds is required. The default value is 600 seconds.
  * TARGET_METRIC_1: the target metric you want to use, such as the following: 
    * `AVERAGE_CPU_UTILIZATION`
    * `AVERAGE_DB_CONNECTIONS`
You must define at least one of the two available metrics. 
  * VALUE_1: the value you want to assign for the target metric you previously indicated. In this example, for the `AVERAGE_DB_CONNECTIONS` target metric, assign the value `50`.



### REST v1

To enable an existing read pool with autoscaling, use the [PATCH](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/patch) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_ID: the ID of the instance associated with the read pool.
  * MAX_NODE_COUNT: the maximum number of read pool nodes you want the read pool to use, such as `10`.
  * MIN_NODE_COUNT: the minimum number of read pool nodes you want the read pool to use, such as `2`.
  * COOLDOWN_SECONDS: Optional: the cooldown or wait time in seconds between read pool node creation or deletion, such as `180`.
  * SCALE_IN_DISABLED: Optional: lets you disable [read pool scale in](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools#what_are_read_pools) behavior. To disable read pool scale-in, set the value to `true`.
  * TARGET_METRIC_1: the target metric you want to use, such as the following: 
    * `AVERAGE_CPU_UTILIZATION`
    * `AVERAGE_DB_CONNECTIONS`
You must define at least one of the two available metrics.
  * VALUE_1: the value you want to assign for the target metric you previously indicated. In this example, for the `AVERAGE_DB_CONNECTIONS` target metric, assign the value `50`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "readPoolAutoScaleConfig": {
          "enabled": true,
          "minNodeCount": MIN_NODE_COUNT,
          "maxNodeCount": MAX_NODE_COUNT,
          "scaleOutCooldownSeconds": COOLDOWN_SECONDS,
          "disableScaleIn": SCALE_IN_DISABLED,
          "targetMetrics": [
            {
              "metric": "TARGET_METRIC_1",
              "targetValue": VALUE_1
            }
          ]
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

To enable an existing read pool with autoscaling, use the [PATCH](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/patch) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_ID: the ID of the instance associated with the read pool.
  * MAX_NODE_COUNT: the maximum number of read pool nodes you want the read pool to use, such as `10`.
  * MIN_NODE_COUNT: the minimum number of read pool nodes you want the read pool to use, such as `2`.
  * COOLDOWN_SECONDS: Optional: the cooldown or wait time in seconds between read pool node creation or deletion, such as `180`.
  * SCALE_IN_DISABLED: Optional: lets you disable [read pool scale in](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools#what_are_read_pools) behavior. To disable read pool scale-in, set the value to `true`.
  * TARGET_METRIC_1: the target metric you want to use, such as the following: 
    * `AVERAGE_CPU_UTILIZATION`
    * `AVERAGE_DB_CONNECTIONS`
You must define at least one of the two available metrics.
  * VALUE_1: the value you want to assign for the target metric you previously indicated. In this example, for the `AVERAGE_DB_CONNECTIONS` target metric, assign the value `50`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "readPoolAutoScaleConfig": {
          "enabled": true,
          "minNodeCount": MIN_NODE_COUNT,
          "maxNodeCount": MAX_NODE_COUNT,
          "scaleOutCooldownSeconds": COOLDOWN_SECONDS,
          "disableScaleIn": SCALE_IN_DISABLED,
          "targetMetrics": [
            {
              "metric": "TARGET_METRIC_1",
              "targetValue": VALUE_1
            }
          ]
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Disable read pool autoscaling on a read pool

Complete the following steps to disable read pool autoscaling.

### gcloud

To disable read pool autoscaling, run the following command.
    
    
      gcloud sql instances patch INSTANCE_NAME
      --no-auto-scale-enabled
      

Replace the following:

  * INSTANCE_NAME: the instance name associated with the read pool you want to modify.



### REST v1

To disable read pool autoscaling, use the [PATCH](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/patch) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_ID: the ID of the instance associated with the read pool.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":{
        "readPoolAutoScaleConfig":{
          "enabled": false
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

To disable read pool autoscaling, use the [PATCH](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/patch) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_ID: the ID of the instance associated with the read pool.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":{
        "readPoolAutoScaleConfig":{
          "enabled": false
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## View metrics

Use [system insights](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights) to view relevant metrics for your read pool.

For `AVERAGE_CPU_UTILIZATION`, refer to the **CPU utilization** [key metric chart](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights#metrics).

For `AVERAGE_DB_CONNECTIONS`, refer to the **Connections per database** [key metric chart](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights#metrics).

## Monitor read pool autoscaling operations

When the conditions are met to trigger a read pool autoscaling event, an `UPDATE` operation runs on the instance. You can view this operation from the Google Cloud console.

Read pool autoscaling operations can take 10 minutes or longer to apply to the instance. Any existing connections won't be transferred to newly added read pool nodes, meaning only new connections will be impacted by read pool autoscaling.

While the autoscaling operation is running on the read pool, you must wait for it to finish before running other updates on the read pool or on the primary instance. If you try to run concurrent requests, you might receive the following error message:
    
    
      Operation failed because another operation was already in progress.
      

You can inspect your read pool instance and see the node count change:
    
    
      gcloud sql instances describe READ_POOL_NAME
      | grep nodeCount
      

Replace the following:

  * READ_POOL_NAME: the name of the read pool for which you want to get information.



### System event audit logs

You can also see the [system event](https://docs.cloud.google.com/sql/docs/postgres/audit-logging#system-events) audit log message associated with method `cloudsql.instances.readPoolAutoScale`, which contains the old and new node count.

## What's next

  * [About read pools](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools)
  * [Create a read pool](https://docs.cloud.google.com/sql/docs/postgres/create-read-pool)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
