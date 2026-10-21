---
url: https://docs.cloud.google.com/database-migration/docs/postgres/api-connection-profiles-old/
title: Manage connection profiles using the API \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:57:11.089380+00:00
---

# Manage connection profiles using the API  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/api-connection-profiles-old/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)



Send feedback 

#  Manage connection profiles using the API Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Database Migration Service isn't yet in scope for any Compliance certifications or reports (unlike Cloud SQL, for example). But, we're working on bringing Database Migration Service into scope. For more information on Google Cloud's Compliance programs, see [Services in Scope](https://cloud.google.com/security/compliance/services-in-scope).

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/api-connection-profiles "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/api-connection-profiles "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


## Overview

In this page, you learn how to use the Database Migration Service API to manage connection profiles for a PostgreSQL source database and a PostgreSQL destination.

There are two ways that you can use the Database Migration Service API. You can make REST API calls or you can use the Google Cloud CLI (CLI). 

To see high-level information about using `gcloud` to manage Database Migration Serviceconnection profiles, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles).

Some API calls for Database Migration Service can take some time to complete. Because the API is asynchronous, the call returns immediately, even if the operation is still in progress. If a subsequent API call uses a newly created object, then you must wait for the first operation to complete before proceeding.

## Create a connection profile for a PostgreSQL source database

The following shows a request to create a connection profile for a PostgreSQL source database. 

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * connection-profile-id: The connection profile ID
  * connection-profile-display-name: The connection profile display name
  * host-ip-address: The source IP address
  * username: The database user name
  * password: The database user password
  * client-key: The unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate. If this field is used then the `clientCertificate` field is mandatory.
  * client-certificate: The x509 PEM-encoded certificate that will be used by the replica to authenticate against the source database server.If this field is used then the `clientKey` field is mandatory.
  * ca-certificate: Required. The x509 PEM-encoded certificate of the CA that signed the source database server's certificate. The replica will use this certificate to verify it's connecting to the right host.



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id

Request JSON body: 
    
    
    
    {
    "displayName": "connection-profile-display-name",
      "postgres": {
          "host": "host-ip-address",
          "port": 5432,
          "username": "username",
          "password": "password",
          "ssl": {
            "clientKey": "client-key",
            "clientCertificate": "client-certificate",
            "caCertificate": "ca-certificate"
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
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

To see high-level information about using `gcloud` to create Database Migration Service connection profiles, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create).

After creation, you can view the information about your connection profile by calling the [`connectionProfiles/get`](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/get) method.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * connection-profile-id: The connection profile ID



HTTP method and URL: 
    
    
    GET https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
      "createTime": "2019-12-22T16:17:37.159786963Z",
      "updateTime": "2019-12-24T13:13:39.455857411Z",
      "state": "READY",
      "displayName": "connection-profile-display-name",
      "postgres": {
        "host": "host-ip-address",
        "port": 5432,
        "username": "username"
      }
    }
    
    

### gcloud

For more information on using `gcloud` to retrieve information about your connection profile, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/describe).

## Create a connection profile for a Cloud SQL for PostgreSQL source database

The following shows a request to create a connection profile for a Cloud SQL for PostgreSQL source database. This example uses a PostgreSQL connection profile because it connects to the PostgreSQL database engine, and not the Cloud SQL management layer. 

To create the pairing between the source and replica using Cloud SQL, you must provide the instance ID for your Cloud SQL database. You can find the instance ID value by using the [`databases/list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/databases/list) method of the Cloud SQL Admin API.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * connection-profile-id: The connection profile ID
  * connection-profile-display-name: The connection profile display name
  * host-ip-address: The source IP address
  * username: The database user name
  * password: The database user password
  * cloud-sql-instance-id: The Cloud SQL instance ID



HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id

Request JSON body: 
    
    
    
    {
    "displayName": "connection-profile-display-name",
      "postgres": {
          "host": "host-ip-address",
          "port": 5432,
          "username": "username",
          "password": "password",
          "cloud_sql_id": "cloud-sql-instance-id"
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
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

To see high-level information about using `gcloud` to create Database Migration Service connection profiles, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create).

For more information on using `gcloud` to create a connection profile for a Cloud SQL for PostgreSQL source database, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql).

## Create a connection profile for Cloud SQL for PostgreSQL destination

The following shows a request to create a connection profile for a Cloud SQL for PostgreSQL destination. Database Migration Service uses the information in this request to create a new Cloud SQL for PostgreSQL instance.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * connection-profile-id: The connection profile ID
  * connection-profile-display-name: The connection profile display name
  * database-version: The database version. For example, POSTGRES_12.
  * tier: The machine type. For example, db-custom-1-4096.
  * data-disk-type: The data disk type. For example, PD_SSD.
  * data-disk-size-gb: The data disk size, in Gb. For example, 20.
  * zone: The zone in the project region
  * cmek_key_name: _Optional_ : The full path and name of a customer-managed encryption key (CMEK). For example, "projects/project-id/locations/location/keyRings/ring/cryptoKeys/customer-managed-encryption-key".



All data stored within Google Cloud is encrypted at rest using the same hardened key management systems that we use for our own encrypted data. These key-management systems provide strict key access controls and auditing, and encrypt user data at rest using AES-256 encryption standards. No setup, configuration, or management is required. Google Cloud's default encryption at rest is the best choice for users who don't have specific requirements related to compliance or locality of cryptographic material.

If you need more control over the keys used to encrypt data at rest within a Google Cloud project, then Database Migration Service offers the ability to protect your data using encryption keys managed by you within [Cloud Key Management Service (KMS)](https://docs.cloud.google.com/kms/docs). These encryption keys are called customer-managed encryption keys (CMEK). When you protect data in Database Migration Service with CMEK, the CMEK is within your control.

The `cmek_key_name` parameter is associated with having a CMEK that Database Migration Service can use to encrypt data that's migrated from the source to the destination. The CMEK is represented by the customer-managed-encryption-key placeholder.

The ring placeholder represents the key ring for your CMEK. A key ring organizes keys in a specific Google Cloud location and allows you to manage access control on groups of keys. A key ring's name doesn't need to be unique across a Google Cloud project, but must be unique within a given location. For more information about key rings, see [Cloud KMS resources](https://docs.cloud.google.com/kms/docs/resource-hierarchy).

As part of creating the connection profile, Database Migration Service will verify that the CMEK exists, and that Database Migration Service has permissions to use the key.

If either of these conditions aren't met, then the following error message will be returned:
    
    
    CMEK_DOES_NOT_EXIST_OR_MISSING_PERMISSIONS

To resolve this issue, verify that the key that you provided exists, and that the Database Migration Service service account has the `cloudkms.cryptoKeys.get` permission for the key.

If you prefer to use Google Cloud's internal key management system instead of a CMEK to encrypt your data, then don't include the `cmek_key_name` parameter and value in your API request.

HTTP method and URL: 
    
    
    POST https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id

Request JSON body: 
    
    
    {
      "displayName": "connection-profile-display-name",
      "cloudsql": {
        "settings": {
          "databaseVersion": "database-version",
          "tier": "machine-type",
          "storageAutoResizeLimit": 0,
          "activationPolicy": "ALWAYS",
          "ipConfig":
            {
            "authorizedNetworks": [],
            "enableIpv4": true,
            "privateNetwork": null
          },
          "autoStorageIncrease": false,
          "dataDiskType": "data-disk-type",
          "dataDiskSizeGb": "data-disk-size",
          "zone": "zone",
          "sourceId": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
          "cmek_key_name": "projects/project-id/locations/location/keyRings/ring/cryptoKeys/customer-managed-encryption-key"
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
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles?connectionProfileId=connection-profile-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591975557292-5a7e4b195623c-e350e3da-713dee7d",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T15:25:57.430715421Z",
        "target": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

To see high-level information about using `gcloud` to create Database Migration Service connection profiles, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create).

## Get information about a connection profile

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * connection-profile-id: The connection profile ID



HTTP method and URL: 
    
    
    GET https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
      "createTime": "2019-12-22T16:17:37.159786963Z",
      "updateTime": "2019-12-24T13:13:39.455857411Z",
      "state": "READY",
      "displayName": "connection-profile-display-name",
      "postgres": {
        "host": "host-ip-address",
        "port": 5432,
        "username": "username"
      }
    }
    
    

### gcloud

For more information on using `gcloud` to retrieve information about your connection profile, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/describe).

## List connection profiles

The following shows a request to retrieve information about all of your connection profiles.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region

You can also filter the list of connection profiles that Database Migration Service retrieves, as follows: 
  * `orderBy:` Use this filter to retrieve a listing of all connection profiles for a particular region in alphabetical order. For example, the `orderBy=name` filter returns all connection profiles, alphabetically, by name.
  * `pageSize:` Use this filter to specify the maximum number of connection profiles that Database Migration Service retrieves and displays on a page. For example, by setting `pageSize=10`, Database Migration Service will return up to 10 connection profiles for a page.

If there are more than 10 connection profiles, then they appear on other pages. At the end of each page, a `nextPageToken` parameter and unique identifier appear. Use the identifier to retrieve the listing of the connection profiles for the following page.




HTTP method and URL: 
    
    
    GET https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "connectionProfiles": [
        {
          "name": "projects/project-id/locations/region/connectionProfiles/name-of-first-connection-profile",
          "createTime": "2019-12-22T16:17:37.159786963Z",
          "updateTime": "2019-12-24T13:13:39.455857411Z",
          "state": "READY",
          "displayName": "display-name-of-first-connection-profile",
          "postgres": {
            "host": "host-ip-address-of-first-connection-profile",
            "port": port-number-of-first-connection-profile,
            "username": "username-of-first-connection-profile",
            "password_set": "true"
          }
        }
        {
          "name": "projects/project-id/locations/region/connectionProfiles/name-of-second-connection-profile",
          "createTime": "2020-11-21T19:22:25.153824963Z",
          "updateTime": "2020-11-11T11:15:14.451046111Z",
          "state": "READY",
          "displayName": "display-name-of-second-connection-profile",
          "postgres": {
            "host": "host-ip-address-of-second-connection-profile",
            "port": port-number-of-second-connection-profile,
            "username": "username-of-second-connection-profile",
            "password_set": "true"
          }
        }
      ]
    }
    
    

### gcloud

For more information on using `gcloud` to retrieve information about all of your connection profiles, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/list).

## Update a connection profile

The following shows a request to update the username and password fields of an existing connection profile. By using the `updateMask` parameter in the request, only these fields need to be included in the request body.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * connection-profile-id: The connection profile ID
  * username: The database user name
  * password: The database user password



HTTP method and URL: 
    
    
    PATCH https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?updateMask=postgres.username,postgres.password

Request JSON body: 
    
    
    
    {
      "postgres" {
        "username": "username",
        "password": "password"
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
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?updateMask=postgres.username,postgres.password"

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
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?updateMask=postgres.username,postgres.password" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to update your connection profile, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update).

## Delete a connection profile

**Important:** You can delete a connection profile only if there are no active migration jobs associated with the profile. If a connection profile has active migration jobs, then [promote](https://docs.cloud.google.com/database-migration/docs/postgres/api-migration-jobs#promotemigrationjob) or [delete](https://docs.cloud.google.com/database-migration/docs/postgres/api-migration-jobs#deletemigrationjob) the jobs.

To see whether a connection profile has any active migration jobs associated with it, run the following command:

`  
GET https://datamigration.googleapis.com/v1/projects/project-id/locations/region/migrationJobs?filter=state:STATE_NAME OR state:STATE_NAME AND source:projects/project-id/locations/region/connectionProfiles/connection-profile-id`

For example:

`GET https://datamigration.googleapis.com/v1/projects/myproject/locations/myregion/migrationJobs?filter=state:RUNNING OR state:FAILED AND source:projects/myproject/locations/myregion/connectionProfiles/postgres-src1`

The various states (statuses) of the migration job are:

  * `NOT STARTED:` The migration job is created, but it hasn't been started.
  * `STARTING:` The migration job is in the process of being started.
  * `RUNNING:` The migration job is running and can be used to migrate data from the source database to the destination database.
  * `STOPPING:` The migration job is in the process of being stopped.
  * `STOPPED:` The migration job is paused, and is no longer migrating data to the destination database.
  * `RESUMING:` The paused migration job is running.
  * `FAILED:` A problem occurred while the migration job was running.
  * `RESTARTING:` Database Migration Service takes a new snapshot of the source database, loads the initial dump into the destination database, and processes ongoing changes of data from the source database to the destination database.



If a user has a migration job in any of these statuses, and if the user attempts to delete the connection profile, then it will fail.

### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * connection-profile-id: The connection profile ID



HTTP method and URL: 
    
    
    DELETE https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to delete your connection profile, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/delete).

## Delete a connection profile and the associated Cloud SQL instance

The following shows a request to delete a destination connection profile, as well as cascade-deleting the associated Cloud SQL instance.

**Important:** Before deleting the connection profile, make sure that you:

  * Promote all migration jobs that are using the destination connection profile.
  * Complete or delete any migration job drafts associated with the connection profile.



### REST

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * region: The project region
  * connection-profile-id: The connection profile ID



HTTP method and URL: 
    
    
    DELETE https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?force=true

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?force=true"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://datamigration.googleapis.com/v1/projects/project-id/locations/region/connectionProfiles/connection-profile-id?force=true" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/region/operations/operation-1591973161667-5a7e422cb0ba4-3004980d-2ae97165",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata",
        "createTime": "2020-06-12T14:46:01.744267779Z",
        "target": "projects/project-id/locations/region/connectionProfiles/connection-profile-id",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### gcloud

For more information on using `gcloud` to delete both your connection profile and the associated Cloud SQL instance, click [here](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/delete).

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


