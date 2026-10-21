---
url: https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture/
title: Upgrade an instance to the new network architecture \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:46.748518+00:00
---

# Upgrade an instance to the new network architecture  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Upgrade an instance to the new network architecture Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture "View this page for the SQL Server database engine")

  


This page describes how to upgrade your Cloud SQL instances from the old network architecture to the new network architecture.

This Cloud SQL network architecture upgrade page applies only to some Cloud SQL instances. If your Cloud SQL instances use a Virtual Private Cloud (VPC) network project that was created before August 2021, then you need to upgrade the Cloud SQL network architecture for your instances.

## Overview

The following table shows the benefits of new network architecture compared to the old network architecture:

Capability | Old network architecture | New network architecture  
---|---|---  
Migrating from Cloud SQL to AlloyDB for PostgreSQL using Database Migration Service  | Requires that you configure a private IP address for the migration  | No additional network configuration required.  
  
For example, [Cloud SQL to AlloyDB for PostgreSQL migration](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quickstart).   
Connect your Cloud SQL instance by using private IP to [private services such as Cloud Build or Vertex AI](https://docs.cloud.google.com/vpc/docs/private-services-access) | Not supported due to network peering intransitivity  | Supported   
Instances that are compliant with [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/supported-products) | Not supported  | Supported   
[Knowledge Catalog](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration) | Not supported  | Supported   
[Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect) | Not supported  | Supported   
Default Cloud SQL [instance quota](https://docs.cloud.google.com/sql/docs/quotas) per project  | 100  | 1000   
  
## Plan your upgrade

Before you upgrade the network architecture of your Cloud SQL instances, plan the upgrade according to the following upgrade constraints:

  * If you upgrade your network architecture, then you can expect downtime on your instance of up to 4 minutes on average.

  * If there's an ongoing data migration, then you can't upgrade the source instance to the new architecture during the data migration.

  * If you [connect to an instance from an external source](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#vpn), then verify that all peering connections are updated to enable the export of custom routes.

  * If you're using [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters), then verify that [Shared VPC host project](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#shared_vpc) is included. If this project isn't included, then the migration fails.

  * You can't upgrade the network architecture of instances on a network with more than 300 Cloud SQL instances.



  * If your network includes two or more instances that use private IP addresses in the same region, then your instance has the following limitations:

    * Cloud SQL might use an additional /24 range (or ranges) from the IP address range that you allocated for private services access. Cloud SQL uses the additional /24 range (or ranges) to host instances in the new network architecture.
    * If there are a limited number of available /24 subnetwork ranges remaining in the IP address range that you allocated for private services access, then Cloud SQL might use a Google-owned /24 range for eligible instances. You can't demote the upgraded instance to be a replica of an external instance.

These limitations are temporary and Cloud SQL removes them during a subsequent maintenance event.



  * [Legacy high-availability (HA) instances](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha) with failover replicas aren't supported for an upgrade.

  * After upgrading the network architecture, you can't create legacy HA failover replicas for upgraded instances.

  * If you're upgrading private IP instances, then the [`import-custom-routes` flag](https://docs.cloud.google.com/vpc/docs/vpc-peering#route-exchange-options) might be enabled for your peering connection with the `servicenetworking` network. If you change this setting after the upgrade, then your instance might lose connectivity. 




### Plan to upgrade all Cloud SQL instances in a network project

Your Cloud SQL instances can reside either in the same project as the VPC network or in a separate project. The project hosting the VPC network is the _network project_.

A network project can operate in _dual stack_ mode, meaning that it can host Cloud SQL instances simultaneously, using both the old and new network architectures. This occurs when at least one instance within the project uses the old architecture. As a result, Cloud SQL can't upgrade the project to the new architecture.

To query the network architecture for all instances within a project, you can use [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API.

### Considerations for dual stack projects

When using dual stack projects, keep in mind the following considerations:

  * **Upgrade an instance implicitly** : When you modify an instance's private network or enable the private IP address within a dual stack project, Cloud SQL might upgrade the instance to the new network architecture implicitly.
  * **No architecture downgrades** : Network changes never downgrade an instance's network architecture.
  * **Reject requests** : If a network change needs a downgrade to complete, then Cloud SQL rejects the request.
  * **New instances can't use IP ranges from the old network architecture** : When a project is in dual stack mode, you can't create instances that use IP ranges that are associated with service connections from the old network architecture.
  * **New network architecture enforcement** : You can force an instance to use the new network architecture when you [create the instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance) or you modify its [network configuration](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#existing-private-instance). When you use the [`--enforce-new-sql-network-architecture`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/create#--enforce-new-sql-network-architecture) flag to create or update the instance, the instance is placed in a separate subnet from instances that use the old network architecture. The separation is permanent and persists even after you upgrade the old network architecture instances to the new network architecture.

For more details on IP allocation and subnets, see [Allocated IP address ranges](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).




To avoid potential conflicts and to ensure a smooth network upgrade, we recommend that you plan to upgrade all instances in the project to the new architecture.

## Upgrade your Cloud SQL network architecture

To upgrade the network architecture of your Cloud SQL instance, do the following:

  1. Check the network architecture of either a single Cloud SQL instance or multiple Cloud SQL instances.
  2. Upgrade the network architecture of a Cloud SQL instance.



### Check the network architecture of a single Cloud SQL instance

To check the current network architecture of a single instance, use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command or the [`instances.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get) method.

### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

To check the network architecture of a single instance, run the following command: 
    
    
       gcloud sql instances describe INSTANCE_NAME
       

If the instance uses the old network architecture, then the response is similar to the following:
    
    
       name: INSTANCE_NAME
       project: PROJECT_ID
       ...
       sqlNetworkArchitecture: OLD_NETWORK_ARCHITECTURE
      

If the instance uses the new network architecture, then the response is similar to the following:
    
    
       name: INSTANCE_NAME
       project: PROJECT_ID
       ...
       sqlNetworkArchitecture: NEW_NETWORK_ARCHITECTURE
      

The `sqlNetworkArchitecture` parameter indicates whether your instance uses the old network architecture (`OLD_NETWORK_ARCHITECTURE`) or the new network architecture (`NEW_NETWORK_ARCHITECTURE`).

### REST v1

To check the network architecture of an instance, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get) method of the Cloud SQL Admin API.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID.
  * INSTANCE_NAME: The instance name.
  * NETWORK_ARCHITECTURE_TYPE: The network architecture type is defined as follows: 
    * `OLD_NETWORK_ARCHITECTURE`: The instance uses the old network architecture.
    * `NEW_NETWORK_ARCHITECTURE`: The instance uses the new network architecture.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "sqlNetworkArchitecture": "NETWORK_ARCHITECTURE_TYPE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
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
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": sql#instance
      "name": INSTANCE_NAME
      "project": PROJECT_ID
      "sqlNetworkArchitecture": enum (SqlNetworkArchitecture)
      ...
    }
    

### REST v1beta4 

To check the network architecture of an instance, use the [`instances.get`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/get) method of the Cloud SQL Admin API.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID.
  * INSTANCE_NAME: The instance name.
  * NETWORK_ARCHITECTURE_TYPE: The network architecture type is defined as follows: 
    * `OLD_NETWORK_ARCHITECTURE`: The instance uses the old network architecture.
    * `NEW_NETWORK_ARCHITECTURE`: The instance uses the new network architecture.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "sqlNetworkArchitecture": "NETWORK_ARCHITECTURE_TYPE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
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
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": sql#instance
      "name": INSTANCE_NAME
      "project": PROJECT_ID
      "sqlNetworkArchitecture": enum (SqlNetworkArchitecture)
      ...
    }
    

### Check the network architecture of multiple Cloud SQL instances

To check the network architecture of multiple instances in a project, use the [`gcloud sql instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/list) command or the [`instance.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/list) method.

### gcloud

To check the network architecture of multiple instances in a project, run the following command: 
    
    
    gcloud sql instances list --show-sql-network-architecture
    

The output looks similar to the following.
    
    
    NAME        DATABASE_VERSION LOCATION   ...     SQL_NETWORK_ARCHITECTURE
    instance_1  POSTGRES_13      asia-northeast1-b  OLD_NETWORK_ARCHITECTURE
    instance_2  MYSQL_5_7        europe-west1-d     NEW_NETWORK_ARCHITECTURE
    ...

###  REST v1 

To check the network architecture of multiple instances in a project, use the [`instance.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/list) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID.
  * NETWORK_ARCHITECTURE_TYPE: The network architecture type as follows: 
    * `OLD_NETWORK_ARCHITECTURE`: The instance uses the old network architecture.
    * `NEW_NETWORK_ARCHITECTURE`: The instance uses the new network architecture.



HTTP method and URL: 
    
    
    LIST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "sqlNetworkArchitecture": "NETWORK_ARCHITECTURE_TYPE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X LIST \  
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
        -Method LIST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": sql#instance
      "name": INSTANCE_NAME
      "project": PROJECT_ID
      "sqlNetworkArchitecture": enum (SqlNetworkArchitecture)
      ...
    }
    

###  REST v1beta4 

To check the network architecture of multiple instances in a project, use the [`instance.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/list) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID.
  * NETWORK_ARCHITECTURE_TYPE: The network architecture type is defined as follows: 
    * `OLD_NETWORK_ARCHITECTURE`: The instance uses the old network architecture.
    * `NEW_NETWORK_ARCHITECTURE`: The instance uses the new network architecture.



HTTP method and URL: 
    
    
    LIST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "sqlNetworkArchitecture": "NETWORK_ARCHITECTURE_TYPE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X LIST \  
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
        -Method LIST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": sql#instance
      "name": INSTANCE_NAME
      "project": PROJECT_ID
      "sqlNetworkArchitecture": enum (SqlNetworkArchitecture)
      ...
    }
    

### Upgrade the network architecture of a single Cloud SQL instance

To upgrade the network architecture for a single instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command, the [`instance.update`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/update) method, or the [`instance.patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method.

### gcloud

To upgrade the network architecture of an instance, run the following command: 
    
    
    gcloud sql instances patch INSTANCE_NAME --upgrade-sql-network-architecture
    

The upgrade operation takes a few minutes.

During the upgrade, a long-running operation starts, and an operation token is returned:
    
    
    operation_id

### REST v1

To upgrade the network architecture of an instance, use the [`instance.update`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/update) or the [`instance.patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method of the Cloud SQL Admin API.

When you upgrade the Cloud SQL network architecture, no additional updates to the instance are allowed in the request. The request body contains an instance of the [`DatabaseInstance`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#resource:-databaseinstance) object, with `sqlNetworkArchitecture` set to `NEW_NETWORK_ARCHITECTURE`.

During the upgrade, a long-running operation starts, and an operation token is returned:
    
    
    operation_id

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID.
  * INSTANCE_NAME: The instance name.
  * NETWORK_ARCHITECTURE_TYPE: The network architecture type is defined as follows: 
    * `OLD_NETWORK_ARCHITECTURE`: The instance uses the old network architecture.
    * `NEW_NETWORK_ARCHITECTURE`: The instance uses the new network architecture.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "sqlNetworkArchitecture": "NETWORK_ARCHITECTURE_TYPE"
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
    
    
    {
      "kind": sql#instance,
      "targetLink": string,
      "status": enum (SqlOperationStatus),
      "name": string,
      "insertTime": string,
      "startTime": string,
      "endTime": string
      ...
    }
    

If the upgrade of your instance fails, then retry the upgrade operation.

### REST v1beta4 

To upgrade the network architecture of an instance, use the [`instance.update method`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/update) or the [`instance.patch method`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) of the Cloud SQL Admin API.

When you upgrade the Cloud SQL network architecture, no additional updates to the instance are allowed in the request. The request body contains an instance of the [`DatabaseInstance`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#resource:-databaseinstance) object, with `sqlNetworkArchitecture` set to `NEW_NETWORK_ARCHITECTURE`.

During the upgrade, a long running operation starts, and the following operation token is returned:
    
    
    operation_id

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID.
  * INSTANCE_NAME: The instance name.
  * NETWORK_ARCHITECTURE_TYPE: The network architecture type is defined as follows: 
    * `OLD_NETWORK_ARCHITECTURE`: The instance uses the old network architecture.
    * `NEW_NETWORK_ARCHITECTURE`: The instance uses the new network architecture.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "sqlNetworkArchitecture": "NETWORK_ARCHITECTURE_TYPE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": sql#instance,
      "targetLink": string,
      "status": enum (SqlOperationStatus),
      "name": string,
      "insertTime": string,
      "startTime": string,
      "endTime": string
      ...
    }
    

If the upgrade of your instance fails for any reason, you can retry the upgrade operation.

## Frequently asked questions

This section provides answers to frequently asked questions about upgrading your Cloud SQL network architecture.

  * What's the impact of the upgrade on my Cloud SQL instance?
  * Do all features work the same after the upgrade?
  * Which instances use the old network architecture?
  * Are all new Cloud SQL instances created on the new network architecture?
  * Is it possible to update all instances in a project with a single command?
  * Does the replica automatically get upgraded if I upgrade the primary?
  * I received a notification that the network architecture of my Cloud SQL instances will be upgraded. What do I need to do?
  * When I attempt to upgrade my instance, I receive the error "outside the reserved IP address range". What do I need to do?



### What's the impact of the upgrade on my Cloud SQL instance?

When upgrading your network architecture, the Cloud SQL instance has a MAINTENANCE state. In this state, the instance experiences up to four minutes of downtime, on average. Any additional changes to the instance aren't allowed until the upgrade is complete. Other instances in your project or network aren't affected by the upgrade.

### Do all features work the same after the upgrade?

All features of your Cloud SQL instance work the same on the new architecture as they did on the old architecture. After you upgrade an instance to use the new network architecture, if you want to switch the network of that instance, then make sure that all instances in the destination network are also upgraded to the new network architecture.

### Which instances use the old network architecture?

Any new projects that were created after August, 2021 automatically use the new network architecture. Existing projects can contain Cloud SQL instances that are created before August 2021 and still use the old network architecture. Therefore, all instances within an existing project must be upgraded before any new instances in that project can start using the new network architecture.

### Are all new Cloud SQL instances created on the new network architecture?

By default, new Cloud SQL instances created in projects created after August 2021 use the new network architecture.

If you want to create an instance in a project created before August 2021 and use the new network architecture, then you have the following options:

  * **Update all existing instances** : Update all of the existing instances in the project to the new network architecture. If you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), then you must update all instances in the projects that are participating in the Shared VPC. After you've updated all of the existing instances in the project, wait several hours before you create additional instances in the project. New instances that you create in the project will then use the new network architecture.

  * **Enforce the use of the new network architecture** : You can force Cloud SQL use the new network architecture by using the `sqlNetworkArchitecture` field in the API or the [`--enforce-new-sql-network-architecture`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/create#--enforce-new-sql-network-architecture) flag in the gcloud CLI when you [create an instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance) or [modify the private IP network configuration](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#existing-private-instance) of an existing instance. However, when you enforce new network architecture for instances before a project is fully upgraded, you might experience instance creation failure if sufficient IP address space isn't available. For more details on IP address range allocation, see [Allocated IP address ranges](https://docs.cloud.google.com/sql/docs/mysql/configure-ip#allocated-ip-address-ranges).




If there are recently deleted instances with the old network architecture, you need to wait four days before creating a new instance with the new network architecture. This delay accommodates the process to [restore](https://docs.cloud.google.com/sql/docs/mysql/delete-instance#restore-deleted-cloud-sql-instance) a deleted instance.

### Is it possible to update all instances in a project with a single command?

No, the upgrade to the new network architecture is based on each instance.

### Does the replica automatically get upgraded if I upgrade the primary?

No, the upgrade to the new network architecture is based on each individual instance. Each replica is treated as a separate instance and must be upgraded separately. This means that if the primary is upgraded and the replica is using the old network architecture, the replica isn't affected. The opposite is also true. If you upgrade a replica, the primary won't be affected.

### I received a notification that the network architecture of my Cloud SQL instances will be upgraded. What do I need to do?

No action is required by you.

For some instances, when the automatic upgrade occurs on a private network, the request is temporarily rejected. As a workaround, you can upgrade the network architecture of your instance yourself by following the procedure in Upgrade the network architecture of a single Cloud SQL instance.

### When I attempt to upgrade my instance, I receive the error "outside the reserved IP address range". What do I need to do?

To use Cloud SQL instances in a VPC network with private IP, allocate IP address ranges when you set up private services access for the VPC network.

For example, if an IP allocated address range is changed or deleted, then you might encounter an error similar to the following:
    
    
    Network architecture upgrade not allowed for private-ip instance PROJECT_ID:INSTANCE_NAME
    whose IP address range 10.0.0.0/24 is outside the reserved IP address range for
    private services access. Re-allocate the IP address range for private services access and retry.
    

In this example, the original allocated IP address range has the name `google-managed-services-VPC_NETWORK_NAME`, and the original allocated IP address range is `10.0.0.0/16`. Then you create an instance with a private IP address of `10.0.0.1`. If the IP address range of `google-managed-services-VPC_NETWORK_NAME` is deleted, or is updated to refer to a range of **`10.1.0.0/16`** this range doesn't cover the instance's private IP address `10.0.0.1`. Afterwards, when you try to upgrade the network architecture of your instance, you encounter the `outside the reserved IP address range` error.

To resolve this issue, follow the procedure in [Configure private services access for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access#configure-access). Re-allocate an IP address range that includes the IP address of your instance into the ranges allocated for private services access. At the least, you can allocate the IP address range reported in your error message (in the previous example, `10.0.0.0/24`.)

Then retry the network architecture upgrade.

## What's next

  * Read more about [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect)
  * Read more about [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview)
  * Read more about [Configure private service access for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access)
  * Read more about [Database migration service to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quickstart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
