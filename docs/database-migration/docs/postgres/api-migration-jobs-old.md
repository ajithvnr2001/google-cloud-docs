---
url: https://docs.cloud.google.com/database-migration/docs/postgres/api-migration-jobs-old/
title: Manage migration jobs using the API \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:18:42.436504+00:00
---

# Manage migration jobs using the API  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/api-migration-jobs-old/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)



Send feedback 

#  Manage migration jobs using the API Stay organized with collections  Save and categorize content based on your preferences. 

**Alpha**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Database Migration Service isn't yet in scope for any Compliance certifications or reports (unlike Cloud SQL, for example). But, we're working on bringing Database Migration Service into scope. For more information on Google Cloud's Compliance programs, see [Services in Scope](https://cloud.google.com/security/compliance/services-in-scope).

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/api-migration-jobs "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/api-migration-jobs "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


## Overview

In this page, you learn how to use the Database Migration Service API to manage migration jobs for a PostgreSQL source database.

There are two ways that you can use the Database Migration Service API. You can make REST API calls or you can use the Google Cloud CLI (CLI).

To see high-level information about using `gcloud` to manage Database Migration Service migration jobs, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs).

**Note:** Some API calls for Database Migration Service can take some time to complete. Because the API is asynchronous, the call returns immediately, even if the operation is still in progress. If a subsequent API call uses a newly created object, then you must wait for the first operation to complete before proceeding.

## Create a draft of a migration job

The following shows a request to create a migration job in draft mode. This way, you don't have to create the migration job all at once. You can create a portion of it, and then update it by using the `PATCH` operation.

For example, if you want to create a migration job, but you don't have the destination database or the network connectivity method, you can use the following code:

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID
  * migration-job-name: The migration job name
  * source-connection-profile-id: The source connection profile ID
  * destination-connection-profile-id: The destination connection profile ID
  * provider: The provider associated with the classification type of the source database. 
    * For a standalone PostgreSQL instance, use `DATABASE_PROVIDER_UNSPECIFIED` because this value is associated with an on-premises database. 
    * For a Cloud SQL for PostgreSQL instance, use `CLOUDSQL`.
    * For any managed database service, use its corresponding `ENUM` value. See the [` DatabaseProvider`](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider) object reference.



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id

Request JSON body: 
    
    
    
    {
      "displayName": "migration-job-name",
      "state": "DRAFT",
      "type": "CONTINUOUS",
      "source": "projects/project-id/locations/region/connectionProfiles/source-connection-profile-id",
      //"destination":"projects/project-id/locations/region/connectionProfiles/destination-connection-profile-id",
      "sourceDatabase": {
        "engine": "POSTGRESQL",
        "provider": "provider"
      },
      //"vpcPeeringConnectivity": {
      //"vpc": "default"
      //}
    }
    
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591975557292-5a7e4b195623c-e350e3da-713dee7d",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T15:25:57.430715421Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Create a continuous migration job with VPC peering connectivity

The following shows a request to create a continuous migration job for migrating a PostgreSQL database (running on a Google Compute Engine VM) to Cloud SQL for PostgreSQL, using VPC peering connectivity.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID
  * migration-job-name: The migration job name
  * source-connection-profile-id: The source connection profile ID
  * destination-connection-profile-id: The destination connection profile ID
  * provider: The provider associated with the classification type of the source database. 
    * For a standalone PostgreSQL instance, use `DATABASE_PROVIDER_UNSPECIFIED` because this value is associated with an on-premises database. 
    * For a Cloud SQL for PostgreSQL instance, use `CLOUDSQL`.
    * For any managed database service, use its corresponding `ENUM` value. See the [` DatabaseProvider`](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider) object reference.



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id

Request JSON body: 
    
    
    
    {
      "displayName": "migration-job-name",
      "state": "NOT_STARTED",
      "type": "CONTINUOUS",
      "source": "projects/project-id/locations/region/connectionProfiles/source-connection-profile-id",
      "destination":"projects/project-id/locations/region/connectionProfiles/destination-connection-profile-id",
      "sourceDatabase": {
        "engine": "POSTGRESQL",
        "provider": "provider"
      },
      "vpcPeeringConnectivity": {
        "vpc": "default"
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
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591975557292-5a7e4b195623c-e350e3da-713dee7d",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T15:25:57.430715421Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to create Database Migration Service migration jobs, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create).

## Create a continuous migration job with reverse SSH connectivity

The following shows a request to create a continuously running migration job for migrating an Amazon RDS PostgreSQL database to Cloud SQL for PostgreSQL, using reverse SSH connectivity.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID
  * migration-job-name: The migration job name
  * source-connection-profile-id: The source connection profile ID
  * destination-connection-profile-id: The destination connection profile ID
  * vm-name: The name of the SSH VM. For example, dms-ssh-bastion.
  * vm-ip-address: The IP address of the SSH VM. For example, 11.22.33.44.
  * vm-port: The connection port of the SSH VM. For example, 3306.
  * vpc-name: The VPC network name. For example, projects/project-id/global/networks/test-network.
  * provider: The provider associated with the classification type of the source database. 
    * For a standalone PostgreSQL instance, use `DATABASE_PROVIDER_UNSPECIFIED` because this value is associated with an on-premises database. 
    * For a Cloud SQL for PostgreSQL instance, use `CLOUDSQL`.
    * For any managed database service, use its corresponding `ENUM` value. See the [` DatabaseProvider`](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider) object reference.



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id

Request JSON body: 
    
    
    
    {
      "displayName": "migration-job-name",
      "state": "NOT_STARTED",
      "type": "CONTINUOUS",
      "source": "projects/project-id/locations/region/connectionProfiles/source-connection-profile-id",
      "destination":"projects/project-id/locations/region/connectionProfiles/destination-connection-profile-id",
      
      "sourceDatabase": {
        "engine": "POSTGRESQL",
        "provider": "provider"
      },
      
      "reverseSshConnectivity": {
        "vm": "vm-name",
        "vm_ip": "vm-ip-address",
        "vm_port": vm-port,
        "vpc": "vpc-name"
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
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to create Database Migration Service migration jobs, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create).

## Create a migration job with IP allowlist connectivity

The following shows a request to create a migration job for migrating either a standalone PostgreSQL instance or a managed database service to a Cloud SQL for PostgreSQL database, using an IP allowlist.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID
  * migration-job-name: The migration job name
  * source-connection-profile-id: The source connection profile ID
  * destination-connection-profile-id: The destination connection profile ID
  * provider: The provider associated with the classification type of the source database. 
    * For a standalone PostgreSQL instance, use `DATABASE_PROVIDER_UNSPECIFIED` because this value is associated with an on-premises database. 
    * For a Cloud SQL for PostgreSQL instance, use `CLOUDSQL`.
    * For any managed database service, use its corresponding `ENUM` value. See the [` DatabaseProvider`](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider) object reference.



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id

Request JSON body: 
    
    
    
    {
      "displayName": "migration-job-name",
      "state": "NOT_STARTED",
      "type": "CONTINUOUS",
      "source": "projects/project-id/locations/region/connectionProfiles/source-connection-profile-id",
      "destination":"projects/project-id/locations/region/connectionProfiles/destination-connection-profile-id",
      "sourceDatabase": {
        "engine": "POSTGRESQL",
        "provider": "provider"
      },
      "staticIpConnectivity": {}
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?migrationJobId=migration-job-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to create Database Migration Service migration jobs, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create).

## Get information about a migration job

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    GET https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/migrationJobs/one-time-vpc-job",
      "createTime": "2020-06-12T15:48:39.666093835Z",
      "updateTime": "2020-06-12T15:48:39.666093835Z",
      "displayName": "migration-job-display-name",
      "state": "CREATING",
      "type": "CONTINUOUS",
      "source": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
      "destination": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
      
      "sourceDatabase": {
        "engine": "POSTGRESQL"
      },
      "destinationDatabase": {
        "provider": "CLOUDSQL"
      },
      
      "vpcPeeringConnectivity": {
        "vpc": "default"
      }
    }
    

### gcloud

For more information on using `gcloud` to retrieve information about your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe).

## List migration jobs

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region

You can also filter the list of migration jobs that Database Migration Service retrieves, as follows: 
  * `orderBy:` Use this filter to retrieve a listing of all migration jobs for a particular region in alphabetical order. For example, the `orderBy=name` filter returns all migration jobs, alphabetically, by name.
  * `pageSize:` Use this filter to specify the maximum number of migration jobs that Database Migration Service retrieves and displays on a page. For example, by setting `pageSize=10`, Database Migration Service will return up to 10 migration jobs for a page.

If there are more than 10 migration jobs, then they appear on other pages. At the end of each page, a `nextPageToken` parameter and a unique identifier appear (for example, `oasndfoasdnoasun1241243ojsandf`). Use the identifier to retrieve the listing of the migration jobs for the following page. On the final page, the `nextPageToken` parameter and unique identifier don't appear.




HTTP method and URL: 
    
    
    GET https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "migrationJobs": [
        {
          "name": "projects/project-id/locations/region/migrationJobs/name-of-first-migration-job",
          "createTime": "2020-06-12T15:48:39.666093835Z",
          "updateTime": "2020-06-12T15:48:39.666093835Z",
          "displayName": "display-name-of-first-migration-job",
          "state": "NOT_STARTED",
          "type": "CONTINUOUS",
          "source": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
          "destination": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
          
          "sourceDatabase": {
            "engine": "POSTGRESQL"
          },
          "destinationDatabase": {
            "provider": "CLOUDSQL"
          },
          
          "vpcPeeringConnectivity": {
            "vpc": "default"
          }
        }
        {
          "name": "projects/project-id/locations/region/migrationJobs/name-of-second-migration-job",
          "createTime": "2021-02-13T11:59:39.104613835Z",
          "updateTime": "2021-02-13T12:01:38.666093835Z",
          "displayName": "display-name-of-second-migration-job",
          "state": "RUNNING",
          "type": "CONTINUOUS",
          "source": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
          "destination": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
          
          "sourceDatabase": {
            "engine": "POSTGRESQL"
          },
          "destinationDatabase": {
            "provider": "CLOUDSQL"
          },
          
          "staticIpConnectivity": {}
            "vpc": "default"
        }
      ],
      "nextPageToken": "unique-identifier"
    }
    

### gcloud

For more information on using `gcloud` to retrieve information about all of your migration jobs, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list).

## Generate an SSH tunnel configuration script for a migration job

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:generateSshScript

Request JSON body: 
    
    
    {
      "vm":"vm-name",
      "vmCreationConfig":{
        "vmMachineType":"machine-type",
        "subnet":"subnet-name"
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
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:generateSshScript"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:generateSshScript" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "generate",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to generate an SSH script for your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script).

## Verify a migration job

The following shows a request to verify a migration job. By verifying a migration job, you can ensure that the job will start and run successfully.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:verify

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:verify"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:verify" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "verify",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to verify your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/verify).

## Update a migration job

The following shows a request to update the display name of an existing migration job. By using the `updateMask` parameter in the request, only these fields need to be included in the request body.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    PATCH https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?updateMask=displayName

Request JSON body: 
    
    
    {
      "displayName": "updated-display-name",
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?updateMask=displayName"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?updateMask=displayName" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to update your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update).

## Start a migration job

The following shows a request to start a migration job.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:start

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:start"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:start" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "start",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to start your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/start).

## Restart a failed migration job

The following shows a request to restart a migration job. A migration job can be restarted from the beginning if the migration failed and is not recoverable, or was stopped during full dump.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:restart

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:restart"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:restart" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "restart",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to restart your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/restart).

## Stop a migration job

The following shows a request to stop a migration job.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:stop

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:stop"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:stop" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "stop",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to stop your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/stop).

## Resume a migration job

The following shows a request to resume a migration job.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:resume

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:resume"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:resume" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "resume",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to resume your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/resume).

## Promote a migration job

The following shows a request to promote a migration job.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:promote

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:promote"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id:promote" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "promote",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to promote your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/promote).

## Delete a migration job

The following shows a request to delete a migration job.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * migration-job-id: The migration job ID



HTTP method and URL: 
    
    
    DELETE https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs/migration-job-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/migrationJobs/migration-job-id",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to delete your migration job, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/delete).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


