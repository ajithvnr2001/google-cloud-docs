---
url: https://docs.cloud.google.com/oracle/database/docs/clone-autonomous-database/
title: Clone an Autonomous AI Database \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:06.961860+00:00
---

# Clone an Autonomous AI Database  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/clone-autonomous-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Clone an Autonomous AI Database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create clones of Autonomous AI Databases in Google Cloud.

Oracle Database@Google Cloud lets you create clones of your existing Autonomous AI Databases. Cloning an Autonomous AI Database creates a new version of the database, leaving the source database intact.

You can create the following types of clones:

  * Full clone: includes all of the source database's data and metadata.
  * Metadata clone: includes the source database's metadata (users, roles, tables, and other database structures) but doesn't contain any of the source database's data.
  * Refreshable clone: Autonomous AI Database serverless refreshable clones are read-only copies of a source database that can be updated incrementally to stay in sync with the primary environment without the overhead of a full re-cloning. These clones operate on their own independent compute and storage resources, making them ideal for offloading reporting workloads, providing up-to-date test environments, or sharing production data across business units without impacting the performance of the source system.



## Limitations

  * A clone can only be created within the same Google Cloud project.
  * Cloning a standby database instance is not supported. The source database must be a primary database in a data guard configuration.
  * The clone operation can create the clone in any available region, based on the availability of Autonomous AI Database Service in that region and the region you've subscribed to in Oracle Cloud Infrastructure (OCI).
  * Changing the encryption key for databases that are the source of refreshable clones is not supported.
  * Creating multiple clones concurrently is not supported. Cloning operations must be performed sequentially.



## Before you begin

  * Make sure that you've an existing Autonomous AI Database that serves as the source databases for cloning.
  * Make sure that you have the following Identity and Access Management (IAM) role required to perform clone operations:

    * `roles/oracledatabase.autonomousDatabaseAdmin`

To learn how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## Create a clone

Clones can have different properties from that of the source database. Some of the attributes that you might want to change when cloning include the following:

  * [Database workload type](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/autonomous-clone-cross-workload-type.html)

You can clone between the following workload types:

Source database workload | Clone database workload  
---|---  
Autonomous AI Lakehouse | Autonomous AI Transaction Processing  
Autonomous AI Transaction Processing | Autonomous AI Lakehouse  
Autonomous AI JSON Database | Autonomous AI Transaction Processing  
Autonomous AI Lakehouse  
APEX Service   
APEX Service | Autonomous AI JSON Database  
Autonomous AI Transaction Processing  
Autonomous AI Lakehouse   
  * Database version

  * Licensing model (BYOL or license included)

  * Backup retention period

  * Network connectivity type (public access or private endpoint only)

  * ODB Network and subnet




For full clones and metadata clones, you can use the following sources to create a clone:

  * Clone from a database instance
  * Clone from a backup



You can create refreshable clones only from database instances.

You can create clones from databases configured with customer-managed encryption keys (CMEK) as well as Oracle Managed Encryption (OMK). For more information, see [Cloning databases configured with CMEK](https://docs.cloud.google.com/oracle/database/docs/clone-autonomous-database#clone-cmek-database).

The time required to clone an Autonomous AI Database can change depending on many factors, including the amount of data stored within the database. You can expect a cloning operation to take longer than creating a new Autonomous AI Database.

**Note:** When performing cloning operations with the Google Cloud CLI, we recommend that you include the `--async` argument so that the operations are performed in the background. This argument is included in the examples in this guide.

## Clone from a database instance

You can create full clones and metadata clones from a database instance.

### Basic full clone

To create a basic full clone from a database instance, do the following:

### gcloud

Use the `gcloud oracle-database autonomous-databases create` command to create a basic full clone from a database instance.
    
    
    gcloud oracle-database autonomous-databases create CLONE_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --admin-password=ADMIN_PASSWORD \
        --database=CLONE_NAME \
        --display-name=DISPLAY_NAME \
        --properties-license-type=LICENSE_TYPE \
        --properties-compute-count=COMPUTE_COUNT \
        --properties-db-version=DATABASE_VERSION \
        --properties-db-workload=WORKLOAD_TYPE \
        --properties-data-storage-size-gb=STORAGE_SIZE \
        --properties-mtls-connection-required \
        --source-config-autonomous-database="projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID" \
        --source-config-type="CLONE_DATABASE" \
        --source-config-clone-type="FULL"
    

Replace the following:

  * CLONE_ID: a unique ID for your clone.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `--source-config-autonomous-database` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.



###  API 

To create a basic full clone from a database instance, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
    -d \
    '{
      "name": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID",
      "admin_password": "ADMIN_PASSWORD",
      "database": "CLONE_NAME",
      "displayName": "DISPLAY_NAME",
      "properties": {
        "licenseType": "LICENSE_TYPE",
        "computeCount": COMPUTE_COUNT,
        "dbVersion": "DATABASE_VERSION",
        "dbWorkload": "WORKLOAD_TYPE",
        "dataStorageSizeTb": STORAGE_SIZE,
        "mtlsConnectionRequired": true
       },
      "sourceConfig": {
        "sourceType": "CLONE_DATABASE",
        "autonomousDatabase": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID",
        "cloneType": "FULL"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_ID: a unique ID for the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `autonomousDatabase` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * BACKUP_ID: the ID of the source database.



### Basic metadata clone

To create a basic metadata clone from a database instance, do the following:

### gcloud

Use the `gcloud oracle-database autonomous-databases create` command to create a basic metadata clone from a database instance.
    
    
    gcloud oracle-database autonomous-databases create CLONE_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --admin-password=ADMIN_PASSWORD \
        --database=CLONE_NAME \
        --display-name=DISPLAY_NAME \
        --properties-license-type=LICENSE_TYPE \
        --properties-compute-count=COMPUTE_COUNT \
        --properties-db-version=DATABASE_VERSION \
        --properties-db-workload=WORKLOAD_TYPE \
        --properties-data-storage-size-gb=STORAGE_SIZE \
        --properties-mtls-connection-required \
        --source-config-autonomous-database="projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID" \
        --source-config-type="CLONE_DATABASE" \
        --source-config-clone-type="METADATA"
    

Replace the following:

  * CLONE_ID: a unique ID for your clone.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `--source-config-autonomous-database` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.



###  API 

To create a basic metadata clone from a database instance, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
    -d \
    '{
      "name": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID",
      "admin_password": "ADMIN_PASSWORD",
      "database": "CLONE_NAME",
      "displayName": "DISPLAY_NAME",
      "properties": {
        "licenseType": "LICENSE_TYPE",
        "computeCount": COMPUTE_COUNT,
        "dbVersion": "DATABASE_VERSION",
        "dbWorkload": "WORKLOAD_TYPE",
        "dataStorageSizeTb": STORAGE_SIZE,
        "mtlsConnectionRequired": true
       },
      "sourceConfig": {
        "sourceType": "CLONE_DATABASE",
        "autonomousDatabase": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID",
        "cloneType": "METADATA"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_ID: a unique ID for the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `autonomousDatabase` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.



## Clone from a backup

To create a clone, you can use existing automatic backups of a database as follows:

  * Clone from a backup resource
  * Clone from a backup timestamp
  * Clone from the latest available backup



Because the clone utilizes the backup data, the cloning process doesn't consume resources or impact the performance of the active source database. Once the clone is provisioned, it functions as a standalone database with its own dedicated compute and storage, entirely decoupled from the lifecycle of the source database.

### Clone from a backup resource

To create a full or metadata clone from a backup ID, do the following:

### gcloud

Use the `gcloud oracle-database autonomous-databases create` command to create a full clone from a backup resource.
    
    
    gcloud oracle-database autonomous-databases create CLONE_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --admin-password=ADMIN_PASSWORD \
        --database=CLONE_NAME \
        --display-name=DISPLAY_NAME \
        --properties-license-type=LICENSE_TYPE \
        --properties-compute-count=COMPUTE_COUNT \
        --properties-db-version=DATABASE_VERSION \
        --properties-db-workload="WORKLOAD_TYPE" \
        --properties-data-storage-size-gb=STORAGE_SIZE \
        --properties-mtls-connection-required \
        --source-config-type="BACKUP_FROM_ID" \
        --source-config-autonomous-database-backup="projects/PROJECT_ID/locations/REGION/autonomousDatabaseBackups/BACKUP_ID" \
        --source-config-clone-type="CLONE_TYPE" \
        --async
    

Replace the following:

  * CLONE_ID: a unique ID for your clone.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `--source-config-autonomous-database-backup` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * BACKUP_ID: the ID of the database backup.
  * CLONE_TYPE: the type of the clone - `FULL` or `METADATA`.




###  API 

To create full clone from a backup resource, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
    -d \
    '{
      "name": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID",
      "admin_password": "ADMIN_PASSWORD",
      "database": "CLONE_NAME",
      "displayName": "DISPLAY_NAME",
      "properties": {
        "licenseType": "LICENSE_TYPE",
        "computeCount": COMPUTE_COUNT,
        "dbVersion": "DATABASE_VERSION",
        "dbWorkload": "WORKLOAD_TYPE",
        "dataStorageSizeTb": STORAGE_SIZE,
        "mtlsConnectionRequired": true
       },
      "sourceConfig": {
        "sourceType": "BACKUP_FROM_ID",
        "autonomousDatabaseBackup": "projects/PROJECT_ID/locations/REGION/autonomousDatabaseBackups/BACKUP_ID",
        "cloneType": "CLONE_TYPE"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_ID: a unique ID for the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `autonomousDatabaseBackup` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * BACKUP_ID: the ID of the database backup.
  * CLONE_TYPE: the type of the clone - `FULL` or `METADATA`.




### Clone from a backup timestamp

To create a full or metadata clone from a backup timestamp, do the following:

### gcloud

Use the `gcloud oracle-database autonomous-databases create` command to create a full or metadata clone from a backup timestamp.
    
    
    gcloud oracle-database autonomous-databases create CLONE_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --admin-password=ADMIN_PASSWORD \
        --database=CLONE_NAME \
        --display-name=DISPLAY_NAME \
        --properties-license-type=LICENSE_TYPE \
        --properties-compute-count=COMPUTE_COUNT \
        --properties-db-version=DATABASE_VERSION \
        --properties-db-workload="WORKLOAD_TYPE" \
        --properties-data-storage-size-gb=STORAGE_SIZE \
        --properties-mtls-connection-required \
        --source-config-type="BACKUP_FROM_TIMESTAMP" \
        --source-config-autonomous-database="projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID" \
        --source-config-backup-time="BACKUP_TIMESTAMP" \
        --source-config-clone-type="CLONE_TYPE" \
        --async
    

Replace the following:

  * CLONE_ID: a unique ID for your clone.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `--source-config-autonomous-database` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.
  * BACKUP_TIMESTAMP: the backup timestamp of the source database.

  * CLONE_TYPE: the type of the clone - `FULL` or `METADATA`.




###  API 

To a full or metadata clone from a backup timestamp, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
    -d \
    '{
      "name": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID",
      "admin_password": "ADMIN_PASSWORD",
      "database": "CLONE_NAME",
      "displayName": "DISPLAY_NAME",
      "properties": {
        "licenseType": "LICENSE_TYPE",
        "computeCount": COMPUTE_COUNT,
        "dbVersion": "DATABASE_VERSION",
        "dbWorkload": "WORKLOAD_TYPE",
        "dataStorageSizeTb": STORAGE_SIZE,
        "mtlsConnectionRequired": true
       },
      "sourceConfig": {
        "sourceType": "BACKUP_FROM_TIMESTAMP",
        "autonomousDatabase": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID",
        "backupTime": "BACKUP_TIMESTAMP",
        "cloneType": "CLONE_TYPE"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_ID: a unique ID for the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `autonomousDatabase` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.
  * BACKUP_TIMESTAMP: the backup timestamp of the source database.

  * CLONE_TYPE: the type of the clone - `FULL` or `METADATA`.




### Clone from latest available backup

To create a full or metadata clone from the latest available backup, do the following:

### gcloud

Use the `gcloud oracle-database autonomous-databases create` command to create a full or metadata clone from the latest available backup.
    
    
    gcloud oracle-database autonomous-databases create CLONE_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --admin-password=ADMIN_PASSWORD \
        --database=CLONE_NAME \
        --display-name=DISPLAY_NAME \
        --properties-license-type=LICENSE_TYPE \
        --properties-compute-count=COMPUTE_COUNT \
        --properties-db-version=DATABASE_VERSION \
        --properties-db-workload="WORKLOAD_TYPE" \
        --properties-data-storage-size-gb=STORAGE_SIZE \
        --properties-mtls-connection-required \
        --source-config-type="BACKUP_FROM_TIMESTAMP" \
        --source-config-autonomous-database="projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID" \
        --source-config-use-latest-available-backup \
        --source-config-clone-type="CLONE_TYPE" \
        --async
    

Replace the following:

  * CLONE_ID: a unique ID for your clone.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `--source-config-autonomous-database` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.
  * CLONE_TYPE: the type of the clone - `FULL` or `METADATA`.




###  API 

To create a full or metadata clone from the latest available backup, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
    -d \
    '{
      "name": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID",
      "admin_password": "ADMIN_PASSWORD",
      "database": "CLONE_NAME",
      "displayName": "DISPLAY_NAME",
      "properties": {
        "licenseType": "LICENSE_TYPE",
        "computeCount": COMPUTE_COUNT,
        "dbVersion": "DATABASE_VERSION",
        "dbWorkload": "WORKLOAD_TYPE",
        "dataStorageSizeTb": STORAGE_SIZE,
        "mtlsConnectionRequired": true
       },
      "sourceConfig": {
        "sourceType": "BACKUP_FROM_TIMESTAMP",
        "autonomousDatabase": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID",
        "useLatestAvailableBackup": true,
        "cloneType": "CLONE_TYPE"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_ID: a unique ID for the clone.
  * ADMIN_PASSWORD: the password for the default administrator user of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `autonomousDatabase` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.
  * CLONE_TYPE: the type of the clone - `FULL` or `METADATA`.




## Refreshable clones

You can create a refreshable clone with either manual or automatic refresh policy with frequencies ranging from one hour to seven days. Refreshable clones use an incremental mechanism that only pulls in changes made since the last update to minimize data transfer.

**Important:** If a clone is not refreshed within seven days, it becomes permanently disconnected from the source and converts into a standalone, read-write database.

Refreshable clones can contain the full database or only the metadata of the source.

### Refreshable clone with automatic refresh mode

Automatic refreshable clones remain in a read-only state and refresh from the source on a regular interval.

To create a refreshable clone with automatic refresh mode, do the following:

### gcloud

Use the `gcloud oracle-database autonomous-databases create` command to create a refreshable clone with automatic refresh mode.
    
    
    gcloud oracle-database autonomous-databases create CLONE_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --database=CLONE_NAME \
        --display-name=DISPLAY_NAME \
        --properties-license-type=LICENSE_TYPE \
        --properties-compute-count=COMPUTE_COUNT \
        --properties-db-version=DATABASE_VERSION \
        --properties-db-workload="WORKLOAD_TYPE" \
        --properties-data-storage-size-gb=STORAGE_SIZE \
        --properties-mtls-connection-required \
        --source-config-autonomous-database="projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID" \
        --source-config-type="CLONE_TO_REFRESHABLE" \
        --source-config-clone-type="CLONE_TYPE"
        --source-config-refreshable-mode=AUTOMATIC \
        --source-config-auto-refresh-frequency-seconds=FREQUENCY \
        --source-config-auto-refresh-point-lag-seconds=LAG \
        --source-config-auto-refresh-start-time="START_TIME" \
        --async
    

Replace the following:

  * CLONE_ID: a unique ID for your clone.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `--source-config-autonomous-database` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.
  * CLONE_TYPE: the type of clone - `FULL` or `METADATA`.

  * FREQUENCY: the refresh frequency (in seconds) at which the clone is refreshed. This value must be greater than 3600 (1 hour) and less than 604800 (7 days).

  * LAG: the time (in seconds) by which the data of the automatic refreshable clone lags the source database at the point of refresh. Set this value to 0 if you want the clone to refresh to the latest timestamp.

  * START_TIME: the date and time at which auto-refreshing begins for the clone. This value controls only the start time for the first refresh operation.

Uses RFC 3339, where generated output is always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. For examples, `2014-10-02T15:01:23Z`, `2014-10-02T15:01:23.045123456Z` or `2014-10-02T15:01:23+05:30`.




###  API 

To create a refreshable clone with automatic refresh mode, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
    -d \
    '{
      "name": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID",
      "database": "CLONE_NAME",
      "displayName": "DISPLAY_NAME",
      "properties": {
        "licenseType": "LICENSE_TYPE",
        "computeCount": COMPUTE_COUNT,
        "dbVersion": "DATABASE_VERSION",
        "dbWorkload": "WORKLOAD_TYPE",
        "dataStorageSizeTb": STORAGE_SIZE,
        "mtlsConnectionRequired": true
       },
      "sourceConfig": {
        "sourceType": "CLONE_TO_REFRESHABLE",
        "autonomousDatabase": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID",
        "cloneType": "CLONE_TYPE",
        "refreshableMode": "AUTOMATIC",
        "autoRefreshFrequencySeconds": FREQUENCY,
        "autoRefreshPointLagSeconds": LAG,
        "autoRefreshStartTime": "START_TIME"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_ID: a unique ID for the clone.
  * For `name` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project.
    * REGION: the region where you want to create the clone.
    * CLONE_ID: the ID of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `autonomousDatabase` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of your source database.
  * CLONE_TYPE: the type of clone `FULL` or `METADATA`.

  * FREQUENCY: the refresh frequency (in seconds) at which the clone is refreshed. This value must be greater than 3600 (1 hour) and less than 604800 (7 days).

  * LAG: the time (in seconds) by which the data of the automatic refreshable clone lags the source database at the point of refresh. Set this value to 0 if you want the clone to refresh to the latest timestamp.

  * START_TIME: the date and time at which auto-refreshing begins for the clone. This value controls only the start time for the first refresh operation.

Uses RFC 3339, where generated output is always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. For examples, `2014-10-02T15:01:23Z`, `2014-10-02T15:01:23.045123456Z` or `2014-10-02T15:01:23+05:30`.




### Refreshable clone with manual Refresh Mode

Manual refreshable clones remain in a read-only state and only refresh from the source when a refresh is triggered.

To create a refreshable clone with manual refresh mode, do the following:

### gcloud

Use the `gcloud oracle-database autonomous-databases create` command to create a refreshable clone with manual refresh mode.
    
    
    gcloud oracle-database autonomous-databases create CLONE_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --database=CLONE_NAME \
        --display-name=DISPLAY_NAME \
        --properties-license-type=LICENSE_TYPE \
        --properties-compute-count=COMPUTE_COUNT \
        --properties-db-version=DATABASE_VERSION \
        --properties-db-workload="WORKLOAD_TYPE" \
        --properties-data-storage-size-gb=STORAGE_SIZE \
        --properties-mtls-connection-required \
        --source-config-autonomous-database="projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID" \
        --source-config-type="CLONE_TO_REFRESHABLE" \
        --source-config-clone-type="CLONE_TYPE" \
        --source-config-refreshable-mode=MANUAL \
        --async
    

Replace the following:

  * CLONE_ID: a unique ID for your clone.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `--source-config-autonomous-database` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of the source database.
  * CLONE_TYPE: the type of clone - `FULL` or `METADATA`.




###  API 

To create a refreshable clone with manual refresh mode, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID"
    -d \
    '{
      "name": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/CLONE_ID",
      "database": "CLONE_NAME",
      "displayName": "DISPLAY_NAME",
      "properties": {
        "licenseType": "LICENSE_TYPE",
        "computeCount": COMPUTE_COUNT,
        "dbVersion": "DATABASE_VERSION",
        "dbWorkload": "WORKLOAD_TYPE",
        "dataStorageSizeTb": STORAGE_SIZE,
        "mtlsConnectionRequired": true
       },
      "sourceConfig": {
        "sourceType": "CLONE_TO_REFRESHABLE",
        "autonomousDatabase": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/SOURCE_DATABASE_ID",
        "cloneType": "CLONE_TYPE",
        "refreshableMode": "MANUAL"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region in which to create the clone.
  * CLONE_ID: a unique ID for the clone.
  * For `name` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project.
    * REGION: the region where you want to create the clone.
    * CLONE_ID: the ID of the clone.
  * CLONE_NAME: a name for the clone. Consider the following guidelines:

    * Must begin with an alphabetic character.
    * Contain up to 30 alphanumeric characters.
    * Must not include special characters.
    * Must be unique in your OCI tenancy.
    * Not required if you're creating a cross-region disaster recovery standby instance or cross-region Autonomous Data Guard standby instance.
  * DISPLAY_NAME: the name of the clone that appears in the Google Cloud console.

  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. Only accepted values are `bring-your-own-license` or `license-included`.

  * COMPUTE_COUNT: the compute capacity for the clone.

  * DATABASE_VERSION: the Oracle database version for the clone.

  * WORKLOAD_TYPE: the workload type for the clone that must be one of the following:

    * `ajd`: Autonomous JSON Database
    * `apex`: Autonomous Database with Oracle APEX Application Development workload type
    * `dw`: Autonomous Data Warehouse database
    * `oltp`: Autonomous Transaction Processing database
  * STORAGE_SIZE: the preferred storage count. Storage can range from 0.02 TiB to 384 TiB.

For Data Warehouse workloads only, storage is measured in terabyte (TiB) increments and must range from 1 TiB to 384 TiB.

  * For `autonomousDatabase` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains your source Autonomous AI Database. If you're using a Shared VPC, then this is the ID of your host project.
    * REGION: the region where the source database is located.
    * SOURCE_DATABASE_ID: the ID of your source database.
  * CLONE_TYPE: the type of clone - `FULL` or `METADATA`.




To learn how to view, delete, disconnect, reconnect, and refresh refreshable clones, see [Manage clones](https://docs.cloud.google.com/oracle/database/docs/manage-clones).

## Cloning databases configured with CMEK

The following conditions apply to cloning Autonomous AI Databases configured with [Google Cloud customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/oracle/database/docs/cmek).

  * **Basic clones and clones created from the backup of databases using CMEK:**

Clones created from a source database and from backup of databases using CMEK are created using an Oracle-managed encryption key. After a clone has been created, you can configure it to use CMEK. For more information, see [Use CMEK](https://docs.cloud.google.com/oracle/database/docs/use-cmek).

  * **Refreshable clones of databases using CMEK:**

Refreshable clones of databases using CMEK are created using the same encryption key and service account as that of the source database. You can't change the encryption key configuration of a refreshable clone.




## Example commands

This section describes some examples of cloning an Autonomous AI Database.

The following example commands use gcloud CLI and only use a subset of the options available when creating an Autonomous AI Database. For a full set of arguments available to create a database, see the [Oracle Database@Google Cloud reference guide](https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/create).

Due to line breaks, and copy and paste issues, we recommended that you use a text editor or a shell script and execute the commands with `bash -x my_shell_script.sh`.

The examples rely on a source database `mysourceadb1` that is configured with the following options:

  * Region: `us-east4`
  * Database ID: `mysourceadb1`
  * Database version: 19c
  * Workload type: transaction processing
  * Licensing model: license included
  * Network connectivity: private network access

    * ODB Network: `odbn1`
    * ODB Subnet: `client1`



The database is described using the following command:
    
    
    gcloud oracle-database autonomous-databases describe mysourceadb1 --location=us-east4
    
    
    
    database: mysourceadb1
    displayName: mysourceadb1
    name: projects/myproj1/locations/us-east4/autonomousDatabases/mysourceadb1
    odbNetwork: projects/myproj1/locations/us-east4/odbNetworks/odbn1
    odbSubnet: projects/myproj1/locations/us-east4/odbNetworks/odbn1/odbSubnets/client1
    properties:
      backupRetentionPeriodDays: 1
      characterSet: AL32UTF8
      computeCount: 2.0
      dataSafeState: NOT_REGISTERED
      dataStorageSizeGb: 20
      dbVersion: 19c
      dbWorkload: OLTP
      encryptionKey:
        provider: ORACLE_MANAGED
      isAutoScalingEnabled: true
      licenseType: LICENSE_INCLUDED
      maintenanceScheduleType: REGULAR
      nCharacterSet: AL16UTF16
      ocid: ocid1.autonomousdatabase.oc1.iad.anuwcljt3mpunqqadduwtarvvgmyofkegxvlz4xmnb3vjb5hfuquxw7syjca
      openMode: READ_WRITE
      privateEndpoint: mysourceadb1.adb.us-ashburn-1.oraclecloud.com
      privateEndpointIp: 10.0.0.106
      privateEndpointLabel: mysourceadb1
      state: AVAILABLE
      supportedCloneRegions:
      - AGA
      - KQQ
      - FRA
    

### Full clone with private network

Creating a full clone with a private network is the most common type of database clone that is performed. Databases can be cloned into different ODB Networks and ODB Subnets.

The following example creates a full clone named `clonepriv1` that resides in the same ODB Network as the source database.
    
    
    export CLONE_ADB_ID=clonepriv1
    export ADB_PROJECT_ID=myproj1
    export GCP_REGION=us-east4
    export ADB_PW=My53cur3Pa55w0rd
    export SOURCE_ADB_ID=mysourceadb1
    export ODB_NETWORK_PROJECT_ID=my-network-project
    export ODB_NETWORK_ID=odbn1
    export ODB_SUBNET_ID=client1
    
    gcloud alpha oracle-database autonomous-databases create $CLONE_ADB_ID \
      --project=$ADB_PROJECT_ID \
      --location=$GCP_REGION \
      --admin-password=$ADB_PW \
      --database=$CLONE_ADB_ID \
      --display-name=$CLONE_ADB_ID \
      --odb-subnet=projects/$ODB_NETWORK_PROJECT_ID/locations/$GCP_REGION/odbNetworks/$ODB_NETWORK_ID/odbSubnets/$ODB_SUBNET_ID \
      --properties-private-endpoint-label=$CLONE_ADB_ID \
      --properties-license-type=LICENSE_INCLUDED \
      --properties-compute-count=2 \
      --properties-db-version=19c \
      --properties-db-workload=OLTP \
      --properties-data-storage-size-gb=20 \
      --source-config-autonomous-database=projects/$ADB_PROJECT_ID/locations/$GCP_REGION/autonomousDatabases/$SOURCE_ADB_ID \
      --source-config-type=CLONE_DATABASE \
      --source-config-clone-type=FULL \
      --async
    

### Full clone with public network

The following example creates a full copy of the source database with public internet access. Public internet availability is achieved by removing the `--odb-subnet parameter`.

An Autonomous AI Database created with public access must enable mutual TLS using the `--properties-mtls-connection-required` parameter unless allowlisted IP addresses are specified using the `--properties-allowlisted-ips` parameter.
    
    
    export CLONE_ADB_ID=clonepub1
    export ADB_PROJECT_ID=myproj1
    export GCP_REGION=us-east4
    export ADB_PW=My53cur3Pa55w0rd
    export SOURCE_ADB_ID=mysourceadb1
    
    gcloud alpha oracle-database autonomous-databases create $CLONE_ADB_ID \
      --project=$ADB_PROJECT_ID \
      --location=$GCP_REGION \
      --admin-password=$ADB_PW \
      --database=$CLONE_ADB_ID \
      --display-name=$CLONE_ADB_ID \
      --properties-license-type=LICENSE_INCLUDED \
      --properties-compute-count=2 \
      --properties-db-version=19c \
      --properties-db-workload=OLTP \
      --properties-data-storage-size-gb=20 \ 
      --properties-mtls-connection-required \
      --source-config-autonomous-database=projects/$ADB_PROJECT_ID/locations/$GCP_REGION/autonomousDatabases/$SOURCE_ADB_ID \
      --source-config-type=CLONE_DATABASE \
      --source-config-clone-type=FULL \
      --async
    

### Metadata clone with private network

The following example creates a metadata clone in which all existing database users and their objects are created, but the objects contain no data.
    
    
    export CLONE_ADB_ID=metaclonepriv1
    export ADB_PROJECT_ID=myproj1
    export GCP_REGION=us-east4
    export ADB_PW=My53cur3Pa55w0rd
    export SOURCE_ADB_ID=mysourceadb1
    export ODB_NETWORK_PROJECT_ID=my-network-project
    export ODB_NETWORK_ID=odbn1
    export ODB_SUBNET_ID=client1
    
    gcloud alpha oracle-database autonomous-databases create $CLONE_ADB_ID \
      --project=$ADB_PROJECT_ID \
      --location=$GCP_REGION \
      --admin-password=$ADB_PW \
      --database=$CLONE_ADB_ID \
      --display-name=$CLONE_ADB_ID \
      --odb-subnet=projects/$ODB_NETWORK_PROJECT_ID/locations/$GCP_REGION/odbNetworks/$ODB_NETWORK_ID/odbSubnets/$ODB_SUBNET_ID \
      --properties-license-type=LICENSE_INCLUDED \
      --properties-compute-count=2 \
      --properties-db-version=19c \
      --properties-db-workload=OLTP \
      --properties-data-storage-size-gb=20 \
      --source-config-autonomous-database=projects/$ADB_PROJECT_ID/locations/$GCP_REGION/autonomousDatabases/$SOURCE_ADB_ID \
      --properties-private-endpoint-label=$CLONE_ADB_ID \
      --source-config-type=CLONE_DATABASE \
      --source-config-clone-type=METADATA \
      --async
    

### Metadata clone with public network

The following example creates a metadata clone of the source database with public internet access. Public internet availability is achieved by removing the `--odb-subnet parameter`.

An Autonomous AI Database created with public access must enable mutual TLS using the `--properties-mtls-connection-required` parameter unless allowlisted IP addresses are specified using the `--properties-allowlisted-ips` parameter.
    
    
    export CLONE_ADB_ID=metaclonepub1
    export ADB_PROJECT_ID=myproj1
    export GCP_REGION=us-east4
    export ADB_PW=My53cur3Pa55w0rd
    export SOURCE_ADB_ID=mysourceadb1
    
    gcloud alpha oracle-database autonomous-databases create $CLONE_ADB_ID \
      --project=$ADB_PROJECT_ID \
      --location=$GCP_REGION \
      --admin-password=$ADB_PW \
      --database=$CLONE_ADB_ID \
      --display-name=$CLONE_ADB_ID \
      --properties-license-type=LICENSE_INCLUDED \
      --properties-compute-count=2 \
      --properties-db-version=19c \
      --properties-db-workload=OLTP \
      --properties-data-storage-size-gb=20 \ 
      --properties-mtls-connection-required \
      --source-config-autonomous-database=projects/$ADB_PROJECT_ID/locations/$GCP_REGION/autonomousDatabases/$SOURCE_ADB_ID \
      --source-config-type=CLONE_DATABASE \
      --source-config-clone-type=METADATA \
      --async
    

### Refreshable clone with automatic refresh mode
    
    
    export CLONE_ADB_ID=autorefcl1
    export ADB_PROJECT_ID=myproj1
    export GCP_REGION=us-east4
    export SOURCE_ADB_ID=mysourceadb1
    export ODB_NETWORK_PROJECT_ID=my-network-project
    export ODB_NETWORK_ID=odbn1
    export ODB_SUBNET_ID=client1
    
    gcloud alpha oracle-database autonomous-databases create $CLONE_ADB_ID \
      --project=$ADB_PROJECT_ID \
      --location=$GCP_REGION \
      --database=$CLONE_ADB_ID \
      --display-name=$CLONE_ADB_ID \
      --odb-subnet=projects/$ODB_NETWORK_PROJECT_ID/locations/$GCP_REGION/odbNetworks/$ODB_NETWORK_ID/odbSubnets/$ODB_SUBNET_ID \
      --properties-license-type=LICENSE_INCLUDED \
      --properties-compute-count=2 \
      --properties-db-version=19c \
      --properties-db-workload=OLTP \
      --properties-data-storage-size-gb=20 \ 
      --properties-mtls-connection-required \
      --source-config-autonomous-database=projects/$ADB_PROJECT_ID/locations/$GCP_REGION/autonomousDatabases/$SOURCE_ADB_ID \
      --source-config-type=CLONE_TO_REFRESHABLE \
      --source-config-clone-type=FULL \
      --source-config-refreshable-mode=AUTOMATIC \
      --source-config-auto-refresh-frequency-seconds=3600 \
      --source-config-auto-refresh-point-lag-seconds=60 \
      --source-config-auto-refresh-start-time="2026-02-27T10:00:00Z" \
      --async
    

### Refreshable clone with manual refresh mode
    
    
    export CLONE_ADB_ID=manrefcl1
    export ADB_PROJECT_ID=myproj1
    export GCP_REGION=us-east4
    export SOURCE_ADB_ID=mysourceadb1
    export ODB_NETWORK_PROJECT_ID=my-network-project
    export ODB_NETWORK_ID=odbn1
    export ODB_SUBNET_ID=client1
    
    gcloud alpha oracle-database autonomous-databases create $CLONE_ADB_ID \
      --project=$ADB_PROJECT_ID \
      --location=$GCP_REGION \
      --database=$CLONE_ADB_ID \
      --display-name=$CLONE_ADB_ID \
      --odb-subnet=projects/$ODB_NETWORK_PROJECT_ID/locations/$GCP_REGION/odbNetworks/$ODB_NETWORK_ID/odbSubnets/$ODB_SUBNET_ID \
      --properties-license-type=LICENSE_INCLUDED \
      --properties-compute-count=2 \
      --properties-db-version=19c \
      --properties-db-workload=OLTP \
      --properties-data-storage-size-gb=20 \ 
      --properties-mtls-connection-required \
      --source-config-autonomous-database=projects/$ADB_PROJECT_ID/locations/$GCP_REGION/autonomousDatabases/$SOURCE_ADB_ID \
      --source-config-type=CLONE_TO_REFRESHABLE \
      --source-config-clone-type=FULL \
      --source-config-refreshable-mode=MANUAL \
      --async
    

## What's next

  * Learn how to [manage refreshable clones](https://docs.cloud.google.com/oracle/database/docs/manage-clones).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
