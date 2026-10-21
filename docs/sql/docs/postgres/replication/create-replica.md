---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica/
title: Create read replicas \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:45.284891+00:00
---

# Create read replicas  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Create read replicas Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica "View this page for the SQL Server database engine")

This page describes how to create a read replica for a Cloud SQL instance.

A read replica is a copy of the primary instance that reflects changes to the primary in almost real time, in normal circumstances. You can use a read replica to offload read requests or analytics traffic from the primary instance.

Additionally, for disaster recovery, you can perform a regional migration. If a replica is a [ cross-region replica](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas), you can perform a failover to another region; specifically, you can promote a replica to a standalone instance (in which case, existing replicas would not consider that instance as primary).

**Note:** Don't use a replica as the source for systems like Datastream or Kafka. If a replica is recreated (because of replication breakage, for example), then the replica inherits the primary disk and can lose binary logs, which will break downstream replication. In such a scenario, systems like Datastream or Kafka must be re-initialized to stream from this replica.

For more information about how replication works, see [Replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/replication).

## Before you begin

If you are creating the first replica for this instance, ensure that the instance meets the requirements for primary instances. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/replication#requirements).

## Create a read replica

The steps for creating a read replica are below.

**Note:** If you specify PostgreSQL 16 and later as the database version for your replica, then the default Cloud SQL edition is Enterprise Plus. If you either don't specify a database version or you specify a version other than PostgreSQL 16 and later, then the default Cloud SQL edition is Enterprise.

If the primary instance has a [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip) connection and the instance accepts database connections from [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/postgres/language-connectors) only, then you can't create read replicas for the instance.

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance for which you want to create a replica, and then open the `more actions` menu next to the listing.
  3. Select **Create read replica**. 

If you don't see that choice, then the instance is a replica; you can't create a replica of a replica.

  4. In the **Customize your instance** section of the page, update settings for your replica. Begin by clicking **Show configuration options** to display the groups of settings. Then, expand the desired groups to review and customize the settings. A **Summary** of all the options you select appears on the right. Customizing these settings is optional. Defaults are assigned in every case where no customizations are made.

For more details about each setting, see the [About instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings) page.

For example, to allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over an internal connection, expand the **Connections** group, and then deselect the **Public IP** check box.

  5. Click **Create replica**. 

Cloud SQL creates a backup, if needed, and creates the replica. You are returned to the instance page for the primary.




### gcloud

Create the replica:
    
    
    gcloud sql instances create REPLICA_NAME \
    --master-instance-name=MASTER_INSTANCE_NAME

You can specify a different tier size using the `--tier` parameter, if needed. Also, if you're creating a replica from a primary instance, and the Cloud SQL edition for the instance is either Enterprise or is Enterprise Plus, version 16 and later, then you don't have to specify a value for this parameter. The replica inherits the machine type from the primary instance. 

You can specify a different region using the `--region` parameter. 

If the primary instance has an internal IP address only, and you want to allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over an internal connection, then add the `--enable-google-private-path` parameter to the command. 

You must create the replica in the same VPC network as the primary instance. You can also specify an `allocated-ip-range-name` in that VPC network. If no range is specified, the replica is created in a random range. 

### Terraform

To create a read replica, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "read_replica" {
      name                 = "postgres-replica-instance-name"
      master_instance_name = google_sql_database_instance.primary.name
      region               = "europe-west4"
      database_version     = "POSTGRES_14"
    
      settings {
        tier              = "db-custom-2-7680"
        availability_type = "ZONAL"
        disk_size         = "100"
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }

### REST v1

Use the [`insert`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/insert) method of the instances resource to create the read replica. The region and databaseVersion properties must be the same as the master. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * database-version: Enum version string (for example, POSTGRES_12)
  * primary-instance-name: The name of the primary instance
  * primary-instance-region: The region of the primary instance
  * replica-region: The region of the replica instance
  * replica-name: The name of the replica instance
  * machine-type: Enum string of the machine type. For example: "db-custom-1-3840"
  * private-network: The authorized network that you're adding or selecting to create a private connection.

You set the value of the `ipv4Enabled` parameter to `false` because you want the Cloud SQL instance to be associated with a private IP address, not a public IP one.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/postgres/private-ip#allocated-ip).

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

Use the [`insert`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/insert) method of the instances resource to create the read replica. The region and databaseVersion properties must be the same as the master. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * database-version: Enum version string (for example, POSTGRES_12)
  * primary-instance-name: The name of the primary instance
  * primary-instance-region: The region of the primary instance
  * replica-region: The region of the replica instance
  * replica-name: The name of the replica instance
  * machine-type: Enum string of the machine type. For example: "db-custom-1-3840"
  * private-network: The authorized network that you're adding or selecting to create a private connection.

You set the value of the `ipv4Enabled` parameter to `false` because you want the Cloud SQL instance to be associated with a private IP address, not a public IP one.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/postgres/private-ip#allocated-ip).

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

To create a read replica of an instance with [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) enabled, use [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API. You can create this replica in either the same region or in a different region from the primary instance ([cross-region read replica](https://docs.cloud.google.com/sql/docs/postgres/replication#cross-region-read-replicas)).

The read replica can't replicate from an instance with a different connectivity type. For example, an instance with Private Service Connect enabled can replicate only from another Private Service Connect instance. It also can't replicate from an instance that supports external IP connections or from an instance that's configured with [private services access](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access).

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

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint). If you're using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#connect-cloud-sql-auth-proxy) or [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#connect-using-language-connectors), then create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.

  * AVAILABILITY_TYPE: enable high availability for the instance. For this parameter, specify one of the following values: 
    * `REGIONAL`: enable high availability and is recommended for production instances. The instance fails over to another zone within your selected region.
    * `ZONAL`: provide no failover capability. This is the default value.

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#deactivate-ha-instance).




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

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#deactivate-ha-instance).

  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint). If you're using the Cloud SQL Auth proxy or Cloud SQL Language Connectors, then you must create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.




HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "POSTGRES_13",
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

For more information about setting and removing high availability for instances, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#ha-instance) and [Deactivate high availability for an instance](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#deactivate-ha-instance).

  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.

Cloud SQL doesn't copy the allowed projects for the primary instance over to the replica. For each replica, you must create a [Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint). If you're using the Cloud SQL Auth proxy or Cloud SQL Language Connectors, then you must create a [DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#zones) and [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) for the replicas.




HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "masterInstanceName": "PRIMARY_INSTANCE_NAME",
      "project": "PROJECT_ID",
      "databaseVersion": "POSTGRES_13",
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

If you enable the [`cloudsql.iam_authentication`](https://docs.cloud.google.com/sql/docs/postgres/flags) flag on the primary instance, Cloud SQL for PostgreSQL enables it on the read replicas automatically. However, if you don't enable this flag on the primary instance, Cloud SQL for PostgreSQL doesn't enable it on the read replicas. You can't use the replicas for IAM database authentication. 

To configure a read replica for IAM database authentication:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the Configuration tile, look for the `cloudsql.iam_authentication` flag. If the flag isn't on the list, enabling the flag in the read replica is unnecessary. If the flag is on the list, you must enable the flag on the read replica. If you need to enable the flag on the read replica, continue with the next step.
  4. Select **Replicas** from the SQL navigation menu.
  5. Click the name of the replica you want to edit.
  6. Click **Edit**.
  7. In the **Configuration options** section, expand **Flags**. 
  8. Select **\+ Add** item.
  9. Enter `cloudsql.iam_authentication` for the flag name. Make sure that **On** is selected for this flag.
  10. Click **Save**.



## Create cascading replicas

This section describes how to create and manage cascading replicas.

For information about how cascading replicas work, see [Cascading replicas](https://docs.cloud.google.com/sql/docs/postgres/replication#cascading-replicas).

### Steps to create a cascading replica

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

  1. Create the new replica by specifying your primary replica as the primary instance using the [`--master-instance-name`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) flag:
    
    gcloud sql instances create REPLICA_NAME \
          --master-instance-name=PARENT_REPLICA_NAME \

Replace the following:  

     * REPLICA_NAME: the unique ID for the replica that you are creating
     * PARENT_REPLICA_NAME: the name of the parent replica
  2. After you create the cascading replica, you can see that the changes made to the primary instance are replicated through all the replicas in the cascading replicas chain.



### curl

  1. To create a replica under the parent replica, edit the following JSON code sample, and save it to a file called `request.json`: 
         
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

  * Learn how to [manage replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas).
  * Learn about [cross-region replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas).
  * Learn about [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
