---
url: https://docs.cloud.google.com/sql/docs/mysql/create-read-pool/
title: Create and manage read pools \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:17:55.916125+00:00
---

# Create and manage read pools  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/create-read-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create and manage read pools Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/create-read-pool "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/create-read-pool "View this page for the SQL Server database engine")

This page describes how to create and manage [read pools](https://docs.cloud.google.com/sql/docs/mysql/about-read-pools) for your large read workloads.

## Before you begin

  1. Read pools contain copies of a primary instance. If you haven't done so already, create a [Cloud SQL Enterprise Plus edition primary instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance). While read pools support [public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) connectivity, for the purpose of this guide, create a primary instance with private IP connectivity that uses [private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access). 

For more information about primary instances and replication, see [About replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas).

  2. After the primary instance is created, choose a password for the root user and run the following command to set the password on the primary instance. Save this password to use later when connecting to the read pool. 
         
         gcloud --project=PROJECT \
             sql users set-password root --host=% \
             --instance=PRIMARY_INSTANCE_NAME --prompt-for-password
           

Make sure you're using `gcloud` v532.0.0 or later.

Make the following replacements:

     * PROJECT: the name of the project where you want the primary instance and read pool to reside.
     * PRIMARY_INSTANCE_NAME: the name of the primary instance.



## Create a read pool

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

Use the following `gcloud sql instances create` command to create a read pool with multiple read pool nodes:
    
    
          gcloud sql instances create READ_POOL_NAME \
          --tier=TIER --edition=ENTERPRISE_PLUS \
          --instance-type=READ_POOL_INSTANCE --node-count=NODE_COUNT \
          --master-instance-name=PRIMARY_INSTANCE_NAME --no-assign-ip
        

Make the following replacements:

  * READ_POOL_NAME: the name you want to use for the read pool.
  * TIER: the machine type you want to use for each read pool node in the read pool, such as `db-perf-optimized-N-4`.
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`. 
  * PRIMARY_INSTANCE_NAME: the name of the primary instance associated with the read pool, such as `my-primary-instance`.



### Terraform

To create a read pool, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). Then, set the `instance_type` attribute to `"READ_POOL_INSTANCE"` and the `node_count` attribute to the number of nodes you want to use.

The following example includes resources for the primary instance and the read pool. 
    
    
    resource "google_sql_database_instance" "primary" {
      name             = "mysql-primary"
      database_version = "MYSQL_8_4"
      region           = "europe-west4"
    
      instance_type = "CLOUD_SQL_INSTANCE"
    
      settings {
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
    
        backup_configuration {
          enabled            = true
          binary_log_enabled = true
        }
    
        ip_configuration {
          ipv4_enabled = true
        }
      }
    }
    
    resource "google_sql_database_instance" "replica" {
      name             = "mysql-replica"
      database_version = "MYSQL_8_4"
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

Use the [ `insert`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert) method of the instances resource to create a read pool with multiple read pool nodes. The `databaseVersion` property must be the same as the primary.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where you want the primary instance and read pool to reside.
  * REGION: the region for the read pool, such as `us-east1`. The region must be the same as the primary instance.
  * TIER: the machine type you want to use for each read pool node in the read pool, such as `db-perf-optimized-N-4`.
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * READ_POOL_NAME: the name you want to use for the read pool, such as `my-read-pool`.
  * DATABASE_VERSION: the database version you want to use. For example, `MYSQL_8_0_37`. 
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`.
  * FULL_NETWORK_NAME: the full network path where you want the read pool to reside, such as `projects/vpc-host-project/global/networks/my-network-name`.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT/instances

Request JSON body: 
    
    
    {
      "name": "READ_POOL_NAME",
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT",
      "databaseVersion": "DATABASE_VERSION",
      "region": "REGION",
      "instanceType": "READ_POOL_INSTANCE",
      "nodeCount": NODE_COUNT,
      "settings": {
        "tier": "TIER",
        "edition": "ENTERPRISE_PLUS",
        "ipConfiguration": {
          "ipv4Enabled": false,
          "privateNetwork": "FULL_NETWORK_NAME"
        }
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE_READ_POOL",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

### REST v1beta4

Use the [ `insert`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert) method of the instances resource to create a read pool with multiple read pool nodes. The `databaseVersion` property must be the same as the primary.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where you want the primary instance and read pool to reside.
  * REGION: the region for the read pool, such as `us-east1`. The region must be the same as the primary instance.
  * TIER: the machine type you want to use for each read pool node in the read pool, such as `db-perf-optimized-N-4`.
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * READ_POOL_NAME: the name you want to use for the read pool, such as `my-read-pool`.
  * DATABASE_VERSION: the database version you want to use. For example, `MYSQL_8_0_37`. 
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`.
  * FULL_NETWORK_NAME: the full network path where you want the read pool to reside, such as `projects/vpc-host-project/global/networks/my-network-name`.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances

Request JSON body: 
    
    
    {
      "name": "READ_POOL_NAME",
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT",
      "databaseVersion": "DATABASE_VERSION",
      "region": "REGION",
      "instanceType": "READ_POOL_INSTANCE",
      "nodeCount": NODE_COUNT,
      "settings": {
        "tier": "TIER",
        "edition": "ENTERPRISE_PLUS",
        "ipConfiguration": {
          "ipv4Enabled": false,
          "privateNetwork": "FULL_NETWORK_NAME"
        }
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE_READ_POOL",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

## Convert a read replica to a read pool

You can convert an existing Cloud SQL Enterprise Plus edition read replica into a read pool by specifying the number of nodes in the pool. During this conversion process, the replica IP will become the read pool IP (the read endpoint), so existing clients can connect to the pool without reconfiguration.

The newly created read pool nodes will have the same machine type and configuration as the original read replica. Changing this machine type or configuration requires a separate operation. This operation is only supported for zonal read replicas. To [convert a highly available (HA) read replica](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#deactivate-ha-instance) to a read pool, you must first convert it to a zonal read replica.

For more information, see Edit read pool configuration.

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

Use the following `gcloud sql instances patch` command to convert a read replica for use with a read pool:
    
    
          gcloud sql instances patch READ_REPLICA_NAME \
          --instance-type=READ_POOL_INSTANCE --node-count=NODE_COUNT
        

Make the following replacements:

  * READ_REPLICA_NAME: the name of the read replica you want to convert.
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`. 



### Terraform

To convert a read replica to a read pool, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). The manifest looks similar to the one you used in [Create a read replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica#create-2nd-gen). Then, complete the following steps:

  * Change the `instance_type` attribute from `"READ_REPLICA_INSTANCE"` to `"READ_POOL_INSTANCE"` and the `node_count` attribute to the number of nodes you want to use.
  * If you previously set it, clear the `settings.availability_type` attribute.



### REST v1

Use the [ `patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method of the instances resource to convert a read replica to a read pool.

Before using any of the request data, make the following replacements: 

  * READ_REPLICA_NAME: the name of the read replica you wish to convert, such as `my-read-replica`.
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_REPLICA_NAME

Request JSON body: 
    
    
    {
      "instanceType": "READ_POOL_INSTANCE",
      "nodeCount": NODE_COUNT
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_REPLICA_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_REPLICA_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_REPLICA_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "READ_REPLICA_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

### REST v1beta4

Use the [ `patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) method of the instances resource to convert a read replica to a read pool.

Before using any of the request data, make the following replacements: 

  * READ_REPLICA_NAME: the name of the read replica you wish to convert, such as `my-read-replica`.
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_REPLICA_NAME

Request JSON body: 
    
    
    {
      "instanceType": "READ_POOL_INSTANCE",
      "nodeCount": NODE_COUNT
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_REPLICA_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_REPLICA_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_REPLICA_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "READ_REPLICA_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

## Convert a read pool to a read replica

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

Use the following `gcloud sql instances patch` command to convert a read replica for use with a read pool:
    
    
          gcloud sql instances patch READ_POOL_NAME \
          --instance-type=READ_REPLICA_INSTANCE --availability-type=ZONAL
        

Make the following replacements:

  * READ_POOL_NAME: the name of the read pool you want to convert.



### Terraform

To convert a read pool to a read replica, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). The manifest looks similar to the one you used in [Create a read pool](https://docs.cloud.google.com/sql/docs/mysql/create-read-pool). Then, change the `instance_type` attribute from `"READ_POOL_INSTANCE"` to `"READ_REPLICA_INSTANCE"`, clear the `node_count` attribute, and set the `settings.availability_type` attribute to `ZONAL`. 

### REST v1

Use the [ `patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method of the instances resource to convert a read pool to a read replica.

Before using any of the request data, make the following replacements: 

  * READ_POOL_NAME: the name of the read pool, such as `my-read-pool`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME

Request JSON body: 
    
    
    {
      "instanceType": "READ_REPLICA_INSTANCE",
      "settings": {
        "availabilityType": "ZONAL"
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "READ_POOL_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

### REST v1beta4

Use the [ `patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) method of the instances resource to convert a read pool to a read replica.

Before using any of the request data, make the following replacements: 

  * READ_POOL_NAME: the name of the read pool, such as `my-read-pool`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME

Request JSON body: 
    
    
    {
      "instanceType": "READ_REPLICA_INSTANCE",
      "settings": {
        "availabilityType": "ZONAL"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "READ_POOL_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

## View read pool information

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

Use the following `gcloud sql instances describe` command to describe the read pool:
    
    
          gcloud sql instances describe READ_POOL_NAME
        

Make the following replacements:

  * READ_POOL_NAME: the name of the read pool you want to describe.



An example response with IP address and node information, might look similar to the following:
    
    
          ...
          connectionName: my-project:us-central1:read-pool
          ipAddresses:
          - ipAddress: 10.3.0.108
            type: PRIVATE
          nodeCount: 2
          nodes:
          - dnsName: c5bdacb09ffc.j10o8yqc7pve.us-central1.sql.goog.
            gceZone: us-central1-f
            ipAddresses:
            - ipAddress: 10.3.0.112
              type: PRIVATE
            name: read-pool-node-01
            state: RUNNABLE
          - dnsName: 8f77c454d6b2.j10o8yqc7pve.us-central1.sql.goog.
            gceZone: us-central1-c
            ipAddresses:
            - ipAddress: 10.3.0.113
              type: PRIVATE
            name: read-pool-node-02
            state: RUNNABLE
        

### REST v1

Use the [ `get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get) method to view read pool details.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where the read pool resides.
  * READ_POOL_NAME: the name of the read pool, such as `my-read-pool`.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      [...],
      "connectionName": "my-project:us-central1:read-pool",
      "ipAddresses": [
        {
          "type": "PRIVATE",
          "ipAddress": "10.3.0.108"
        }
      ],
      "nodeCount": 2,
      "nodes": [
        {
          "ipAddresses": [
            {
              "type": "PRIVATE",
              "ipAddress": "10.3.0.112"
            }
          ],                                                                                                                 
          "name": "read-pool-node-01",
          "gceZone": "us-central1-f",
          "dnsName": "c5bdacb09ffc.j10o8yqc7pve.us-central1.sql.goog.",
          "state": "RUNNABLE"
        },
        {
          "ipAddresses": [
            {
              "type": "PRIVATE",
              "ipAddress": "10.3.0.113"
            }
          ],
          "name": "read-pool-node-02",
          "gceZone": "us-central1-c",
          "dnsName": "8f77c454d6b2.j10o8yqc7pve.us-central1.sql.goog.",
          "state": "RUNNABLE"
        }
      ]
    }
    

### REST v1beta4

Use the [ `get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/get) method to view read pool details.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where the read pool resides.
  * READ_POOL_NAME: the name of the read pool, such as `my-read-pool`.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      [...],
      "connectionName": "my-project:us-central1:read-pool",
      "ipAddresses": [
        {
          "type": "PRIVATE",
          "ipAddress": "10.3.0.108"
        }
      ],
      "nodeCount": 2,
      "nodes": [
        {
          "ipAddresses": [
            {
              "type": "PRIVATE",
              "ipAddress": "10.3.0.112"
            }
          ],                                                                                                                 
          "name": "read-pool-node-01",
          "gceZone": "us-central1-f",
          "dnsName": "c5bdacb09ffc.j10o8yqc7pve.us-central1.sql.goog.",
          "state": "RUNNABLE"
        },
        {
          "ipAddresses": [
            {
              "type": "PRIVATE",
              "ipAddress": "10.3.0.113"
            }
          ],
          "name": "read-pool-node-02",
          "gceZone": "us-central1-c",
          "dnsName": "8f77c454d6b2.j10o8yqc7pve.us-central1.sql.goog.",
          "state": "RUNNABLE"
        }
      ]
    }
    

## Add or remove read pool nodes

The following steps scale a read pool in or out by modifying the number of read pool nodes in the read pool. Some operation limitations apply. For more information, see [Read pool limitations](https://docs.cloud.google.com/sql/docs/mysql/about-read-pools#limitations).

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

Use the following `gcloud sql instances patch` command to scale the read pool:
    
    
          gcloud sql instances patch READ_POOL_NAME \
          --node-count=NODE_COUNT
        

Make the following replacements:

  * READ_POOL_NAME: the name of the read pool.
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`. 



### Terraform

To change the number of read pool nodes, update an existing [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). The manifest looks similar to the one you used in [Create a read pool](https://docs.cloud.google.com/sql/docs/mysql/create-read-pool). Then, change the `node_count` attribute to the number of nodes you want to use. 

### REST v1

Use the [ `patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method to scale a read pool in or out by modifying the number of read pool nodes in the read pool.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where the read pool resides.
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME

Request JSON body: 
    
    
    {
      "nodeCount": NODE_COUNT
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "READ_POOL_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

### REST v1beta4

Use the [ `patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) method to scale a read pool in or out by modifying the number of read pool nodes in the read pool.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where the read pool resides.
  * NODE_COUNT: the number of read pool nodes you want in the read pool. Choose any number from `1` to `20`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME

Request JSON body: 
    
    
    {
      "nodeCount": NODE_COUNT
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAMEINSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "READ_POOL_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

## Edit read pool configuration

The following steps show you how to edit read pool configuration. For more detailed information, see [About instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings) and [Edit instances](https://docs.cloud.google.com/sql/docs/mysql/edit-instance). 

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

Use the following `gcloud sql instances patch` command to vertically scale the read pool, for example, by modifying the machine type:
    
    
          gcloud sql instances patch READ_POOL_NAME \
          --tier=TIER
        

Make the following replacements:

  * READ_POOL_NAME: the name of the read pool.
  * TIER: the machine type you want to apply to each read pool node in the read pool, such as `db-perf-optimized-N-8`.



### Terraform

To edit the read pool configuration, update an existing [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). The manifest looks similar to the one you used in [Create a read pool](https://docs.cloud.google.com/sql/docs/mysql/create-read-pool). Then, update the attributes you want to change in the `settings` field. For example, change the `settings.tier` attribute to a different machine type. 

### REST v1

Use the [ `patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method to modify read pool node configuration. Settings are uniformly applied across all read pool nodes in the read pool.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where the read pool resides.
  * TIER: the machine type you want to use for each read pool node in the read pool, such as `db-perf-optimized-N-4`.
  * READ_POOL_NAME: the name of the read pool, such as `my-read-pool`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME

Request JSON body: 
    
    
    {
      "settings": {
        "tier": "TIER"
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "READ_POOL_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

### REST v1beta4

Use the [ `patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) method to modify read pool node configuration. Settings are uniformly applied across all read pool nodes in the read pool.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where the read pool resides.
  * TIER: the machine type you want to use for each read pool node in the read pool, such as `db-perf-optimized-N-4`.
  * READ_POOL_NAME: the name of the read pool, such as `my-read-pool`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME

Request JSON body: 
    
    
    {
      "settings": {
        "tier": "TIER"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "READ_POOL_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

## Connect to a read pool

There are many ways to connect to a read pool. The following steps show one way, namely, connecting to a read pool with a private IP address by creating a VM in the same VPC network to serve as the connection source.

For more information about other ways you can configure connectivity to a Cloud SQL instance, see [About Cloud SQL connections](https://docs.cloud.google.com/sql/docs/mysql/connect-overview). The connection methods usually require you to first obtain the IP address or connection name of the instance, as described in View read pool information. Read pools support most of the connection methods available for other Cloud SQL instances, with some [limitations](https://docs.cloud.google.com/sql/docs/mysql/about-read-pools#limitations).

If connecting using the Cloud SQL Auth Proxy or the Cloud SQL Connectors, make sure to update to the latest version. For read pool support, the minimum required versions include the following:

  * Cloud SQL Auth Proxy: v2.15.2
  * Cloud SQL Python Connector: v1.18.0
  * Cloud SQL Go Connector: v1.16.0
  * Cloud SQL Node Connector: v1.7.0
  * Cloud SQL Java Connector: v1.24.0



### Console

To connect to a read pool, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

You're taken to the instance Overview page. Click into the new read pool to view the details including its private IP address. In the **Connect to this instance** section, copy and save the instance's **Connection name**. The `connection name` is in the format `projectID:region:instanceID`. You'll use this `connection name` later when starting the Cloud SQL Auth Proxy.
  2. [Create a Compute Engine VM](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-private-ip#create-vm).
  3. [Open two SSH connections to the Compute Engine VM](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-private-ip#open-ssh). These are used in subsequent steps to run the Cloud SQL Auth Proxy and run the database client.
  4. [Install the client](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-private-ip#install-client).
  5. [Install the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-private-ip#install-proxy).
  6. [Start the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-private-ip#start-proxy).
  7. [Connect to your Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-private-ip#connect).



For more information, see [Connect to a Cloud SQL instance with private IP](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-private-ip).

## Delete a read pool

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

Use the following `gcloud sql instances delete` command to delete a read pool:
    
    
          gcloud sql instances delete READ_POOL_NAME
        

Make the following replacements:

  * READ_POOL_NAME: the name of the read pool you want to delete.



### REST v1

Use the [ `delete`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/delete) method to delete a read pool.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where the read pool resides.
  * READ_POOL_NAME: the name of the read pool, such as `my-read-pool`.



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE",
      "name": "OPERATION_ID",
      "targetId": "READ_POOL_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

### REST v1beta4

Use the [ `delete`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/delete) method to delete a read pool.

Before using any of the request data, make the following replacements: 

  * PROJECT: the name of the project where the read pool resides.
  * READ_POOL_NAME: the name of the read pool, such as `my-read-pool`.



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/instances/READ_POOL_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE",
      "name": "OPERATION_ID",
      "targetId": "READ_POOL_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT/operations/OPERATION_ID",
      "targetProject": "PROJECT"
    }
    

## What's next

  * [About read pools](https://docs.cloud.google.com/sql/docs/mysql/about-read-pools)
  * [Read pool autoscaling](https://docs.cloud.google.com/sql/docs/mysql/read-pool-autoscaling)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
