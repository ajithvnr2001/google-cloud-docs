---
url: https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica/
title: Create read replicas \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:16.037467+00:00
---

# Create read replicas  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Create read replicas Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to create a read replica for a Cloud SQL instance.

To set up a Cloud SQL instance to act as a publisher to an external subscriber, see [Configure external replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica).

**Important:** Before using this feature, review **[About replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/replication)** , including the **[Limitations](https://docs.cloud.google.com/sql/docs/sqlserver/replication#sql-server-limitations)**.

A read replica is a copy of the primary instance that reflects changes to the primary in almost real time, in normal circumstances. You can use a read replica to offload read requests or analytics traffic from the primary instance.

Additionally, for disaster recovery, you can perform a regional migration. If a replica is a [ cross-region replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/cross-region-replicas), you can perform a failover to another region; specifically, you can promote a replica to a standalone instance (in which case, existing replicas would not consider that instance as primary).

**Note:** Don't use a replica as the source for systems like Datastream or Kafka. If a replica is recreated (because of replication breakage, for example), then the replica inherits the primary disk and can lose binary logs, which will break downstream replication. In such a scenario, systems like Datastream or Kafka must be re-initialized to stream from this replica.

For more information about how replication works, see [Replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/replication).

## Before you begin

If you are creating the first replica for this instance, ensure that the instance meets the requirements for primary instances. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/replication#requirements).

## Create a read replica

When creating a read replica, keep the following considerations in mind:

  * You can create a maximum of seven read replicas per primary instance. 
    * This value can include any combined number of read replicas and [read pool node count under a read pool instance](https://docs.cloud.google.com/sql/docs/sqlserver/about-read-pools). For example, a primary instance might have two read replicas, and a separate read pool of five read replicas (read pool nodes).
  * If an edition isn't specified, then Cloud SQL Enterprise edition is the default.
  * If, when creating a read replica or cascading replica, the primary is an Cloud SQL Enterprise Plus edition instance, then you must indicate the edition and tier you want to use.



The steps for creating a read replica are below.

**Note:** If the primary instance has a [private IP](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip) connection and the instance accepts database connections from [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/language-connectors) only, then you can't create read replicas for the instance.

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance for which you want to create a replica, and then open the `more actions` menu next to the listing.
  3. Select **Create read replica**. 

If you don't see that choice, then the instance is a replica; you can't create a replica of a replica.

  4. In the **Customize your instance** section, update settings for your replica. Begin by clicking **Show configuration options** to display the groups of settings. Then, expand the desired groups to review and customize the settings. A **Summary** of all the options you select appears on the right. Customizing these settings is optional. Defaults are assigned in every case where no customizations are made.

For more details about each setting, see the [About instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings) page.

  5. Click **Create replica**. 

Cloud SQL creates a backup, if needed, and creates the replica. You are returned to the instance page for the primary.




### gcloud

Create the replica:
    
    
    gcloud sql instances create REPLICA_NAME \
    --master-instance-name=PRIMARY_INSTANCE_NAME
      

You can specify a different tier size using the `--tier` parameter, if needed. 

You can specify a different region using the `--region` parameter. 

If the primary instance has an internal IP address only, then add the `--no-assign-ip` parameter to the command. 

You can add more parameters for other instance settings. To learn more, see [gcloud sql instances create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create).

You must create the replica in the same VPC network as the primary instance. You can also specify an `allocated-ip-range-name` in that VPC network. If no range is specified, the replica is created in a random range. 

### Terraform

To create a read replica, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "read_replica" {
      name                 = "sqlserver-replica-instance-name"
      master_instance_name = google_sql_database_instance.primary.name
      region               = "europe-west4"
      database_version     = "SQLSERVER_2019_ENTERPRISE"
      root_password        = "INSERT-PASSWORD-HERE"
      replica_configuration {
        failover_target = false
      }
    
      settings {
        tier              = "db-custom-2-7680"
        availability_type = "ZONAL"
        disk_size         = "100"
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }

### REST v1beta4

Use the [`insert`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/insert) method of the instances resource to create the read replica. The region and databaseVersion properties must be the same as the master. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * database-version: Enum version string (for example, SQLSERVER_2017_ENTERPRISE)
  * primary-instance-name: The name of the primary instance
  * primary-instance-region: The region of the primary instance
  * replica-region: The region of the replica instance
  * replica-name: The name of the replica instance
  * machine-type: Enum string of the machine type. For example: "db-custom-1-3840"

You set the value of the `ipv4Enabled` parameter to `false` because you want the Cloud SQL instance to be associated with a private IP address, not a public IP one.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated-ip).

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

To create a read replica of an instance with [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) enabled, use [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API. You can create this replica in either the same region or in a different region from the primary instance ([cross-region read replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication#cross-region-read-replicas)).

The read replica can't replicate from an instance with a different connectivity type. For example, an instance with Private Service Connect enabled can replicate only from another Private Service Connect instance. It also can't replicate from an instance that supports external IP connections or from an instance that's configured with [private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access).

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

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint). If you're using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#connect-cloud-sql-auth-proxy) or [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#connect-using-language-connectors), then create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.

  * AVAILABILITY_TYPE: enable high availability for the instance. For this parameter, specify one of the following values: 
    * `REGIONAL`: enable high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provide no failover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#deactivate-ha-instance).




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

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#deactivate-ha-instance).

  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint). If you're using the Cloud SQL Auth proxy or Cloud SQL Language Connectors, then you must create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.




HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "SQLSERVER_2019_STANDARD",
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

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#deactivate-ha-instance).

  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint). If you're using the Cloud SQL Auth proxy or Cloud SQL Language Connectors, then you must create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.




HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "SQLSERVER_2019_STANDARD",
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
    

## Create cascading replicas

This section describes how to create and manage cascading replicas.

For information about how cascading replicas work, see [Cascading replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication#cascading-replicas-sqlserver).

### Before you begin

The primary instance must have a cascadable replica. The following section provides the steps to create a cascadable replica.

### Steps to create a cascadable replica

When you create a cascadable replica, you must create the replica in a different region than the primary instance. You configure a cascadable replica by setting the `cascadable-replica` flag.

### gcloud

Create the new replica by specifying the primary instance using the [`--master-instance-name`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) flag and using the `--cascadable-replica` flag:
    
    
    gcloud sql instances create REPLICA_NAME \
       --master-instance-name=PRIMARY_INSTANCE_NAME \
       --cascadable-replica \
       --region=REGION

Replace the following:

  * REPLICA_NAME: the unique ID for the replica that you are creating.
  * PRIMARY_INSTANCE_NAME: the name of the primary instance.
  * REGION: the region where you want to create the new replica. This region must be different from the region of the primary instance.



You must create the replica in the same VPC network as the primary instance. You can also [specify an allocated IP range name ](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#configure_an_instance_to_use_private_ip) in that VPC network. If no range is specified, then the replica is created in a random range. 

You can add more parameters for other instance settings. For example, 

  * You can specify a different machine tier size using the `--tier` parameter.
  * If the primary instance has a private IP address only, then add the `--no-assign-ip` parameter to the command.



For more information adding parameters for instance settings, see [gcloud sql instances create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create). 

After the cascadable replica is created, you can create a cascading replica.

### curl

  1. To create a cascadable replica under the primary instance, edit the following JSON code sample, and save it to a file called `request.json`. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID.
     * DATABASE_VERSION: enum string of the database version. For example, `SQLSERVER_2017_ENTERPRISE.`
     * PRIMARY_INSTANCE_NAME: the name of the primary instance.
     * PRIMARY_INSTANCE_REGION: the region of the primary instance.
     * REPLICA_REGION: the region of the replica instance.
     * REPLICA_NAME: the name of the replica instance.
     * MACHINE_TYPE: enum string of the machine type. For example, `db-custom-2-3840`.
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "DATABASE_VERSION"
      "name": "REPLICA_NAME",
      "region": "REPLICA_REGION",
      "settings":
        {
          "tier": "MACHINE_TYPE",
          "settingsVersion": 0,
        }
        "replicaConfiguration":
        {
         "cascadableReplica": true
        }
    }

  2. In the `replicaConfiguration` section, make sure that the `cascadadableReplica` field is set to `true`.
  3. Run the following command: 
         
         curl -X POST
         -H "Authorization: Bearer "$(gcloud auth print-access-token)
         -H "Content-Type: application/json; charset=utf-8"
         -d @request.json
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"




After the cascadable replica is created, you can create a cascading replica.

### Terraform

To create a cascadable replica, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 

The following sample creates a primary instance and a cascadable replica that you can assign as the DR replica when you perform a [switchover](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery#perform-switchover) operation as part of [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#advanced-dr).
    
    
    resource "google_sql_database_instance" "original-primary" {
      name   = "sqlserver-primary-instance-name"
      region = "us-east1"
      # Specify a database version that supports Cloud SQL Enterprise Plus edition.
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
      # Specify the original primary instance as the master instance.
      master_instance_name = google_sql_database_instance.original-primary.name
      # DR replica must be in a different region than the region of the primary instance.
      region = "us-west2"
      # DR replica must be the same database version as the primary instance.
      database_version = "SQLSERVER_2022_ENTERPRISE"
      instance_type    = "READ_REPLICA_INSTANCE"
      root_password    = "INSERT-PASSWORD-HERE"
      replica_configuration {
        # Make the replica a cascadable replica.
        cascadable_replica = true
      }
    
      settings {
        # DR replica must be in the same tier as your primary instance and support Enterprise Plus edition.
        tier    = "db-perf-optimized-N-2"
        edition = "ENTERPRISE_PLUS"
      }
    }

### Steps to create a cascading replica

When you create a cascading replica, you must create the replica in the same region as the cascadable replica. You configure a cascading replica by providing the name of the cascadable replica in the `–master-instance-name` parameter. 

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the **Replicas** tab for the replica that will act as a parent for the replica that you want to create.
  3. Click **Create replica**.
  4. On the **Create read replica** page, update the instance ID, and any other configuration options, including the name, region, and zone.
  5. Click **Create**. 

Cloud SQL creates a replica. You're returned to the instance page for the parent replica.

  6. Follow steps 4-6 for each new cascading replica that you want to create.



### gcloud

  1. Create the new replica by specifying the cascadable replica instance in the [`--master-instance-name`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) flag:
    
    gcloud sql instances create REPLICA_NAME \
          --master-instance-name=CASCADABLE_REPLICA_NAME \

Replace the following:  

     * REPLICA_NAME: the unique ID for the replica that you are creating
     * CASCADABLE_REPLICA_NAME: the name of the cascadable replica
  2. After you create the cascading replica, you can see that the changes made to the primary instance are replicated through all the replicas in the cascading replicas chain.



### curl

  1. To create a cascading replica under the cascadable replica, edit the following JSON code sample, and save it to a file called `request.json`: 
         
         {
           "masterInstanceName": "CASCADABLE_REPLICA_NAME",
           "project": "PROJECT_ID",
           "name": "REPLICA_NAME",
           "region": "REPLICA_REGION",
           "settings":
             {
               "tier": "MACHINE_TYPE",
             }
         }

  2. Run the following command: 
         
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

  * Learn how to [manage replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas).
  * Learn about [cross-region replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/cross-region-replicas).
  * Learn about [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
