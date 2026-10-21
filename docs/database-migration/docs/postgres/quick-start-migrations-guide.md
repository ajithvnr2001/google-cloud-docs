---
url: https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide/
title: Use quick-start migrations to migrate to Cloud SQL \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:09.433498+00:00
---

# Use quick-start migrations to migrate to Cloud SQL  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest)



Send feedback 

#  Use quick-start migrations to migrate to Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

  


MySQL | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quick-start-migrations-guide "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to perform quick-start migrations for homogeneous PostgreSQL migrations to Cloud SQL for PostgreSQL.

## Overview

_Quick-start migrations_ are a lightweight continuous migration flow for homogeneous PostgreSQL scenarios. With quick-start migrations, Database Migration Service can automatically set up everything you need to migrate your databases: networking components (network attachments, subnets, private connectivity configurations), connection profiles, and migration jobs.

With quick-start migrations, you can move your data to an existing Cloud SQL instance, or create a new one as you configure the migration. Quick-start migrations are best suited for:

  * Basic migrations, where you don't need to precise control over data dump parallelism settings. 
  * Migrating your database from one Google Cloud project to another. When you configure a quick-start migration, you can create your destination instance in a different project than your source and set Database Migration Service to create the network attachment and subnet in the Virtual Private Cloud (VPC) network of another project. 
  * Migrating from sources that have a private IP address in your Google Cloud Virtual Private Cloud (VPC) network, such as self-managed databases on Compute Engine, or Cloud SQL for PostgreSQL instances enabled for private networking. 

Sources hosted outside Google Cloud might need additional network components (such as a Cloud VPN connection) so that they can be reached at a private IP address within your VPC network. 

  * The source database must have a private IP address assigned in your VPC network. Database Migration Service connects to the source database using Private Service Connect interfaces (network attachments). Public IP connectivity isn't supported for quick-start migrations. 



To learn more about quick-start migrations, see [ Quick-start migrations overview](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) in the main Database Migration Service documentation.

## Before you begin

  1. Verify if quick-start migrations can fully support your scenario. See [ Quick-start migration limitations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations#limitations). 

  2. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Database Migration Service, Compute Engine, Network Connectivity Center, and Cloud SQL Admin APIs. 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,datamigration.googleapis.com,sqladmin.googleapis.com,networkconnectivity.googleapis.com)




### Required roles

To get the permissions that you need to run quick-start migrations to Cloud SQL with Database Migration Service, ask your administrator to grant the required Identity and Access Management (IAM) roles for the accounts involved in the migration in the relevant projects. For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.

**Important:** You must assign the roles directly to these accounts. Roles inherited through Google group membership aren't supported for quick-start migrations.

#### Roles and permissions in the source project

Grant the following roles to specific accounts on the Google Cloud project where your **source** database resides:

  * For the user account that performs the migration: [ Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) role (`roles/compute.networkAdmin`) 
  * For the Database Migration Service service account of the **destination** project: [ Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) 

The Database Migration Service service account is created for when you enable the Database Migration Service API. The email address associated with this account is generated automatically and can't be changed. This email address uses the following format: 
        
        service-DESTINATION_PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com




These predefined roles contain the permissions required to set up connectivity on your **source** database project as part of a quick-start migration with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions (source)** section: 

#### Required permissions (source)

The following permissions are required to perform homogeneous quick-start migrations with Database Migration Service: 

For the user account that performs the migration:

  * `compute.networks.*`
  * `compute.subnetworks.*`
  * `compute.networkAttachments.*`



For the Database Migration Service service account of the **destination** project: `compute.networkAttachments.get`. 

#### Roles and permissions in the destination project

Grant the following roles to the user account that performs the migration on the Google Cloud project where your **destination** database resides:

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) 



These predefined roles contain the permissions required to set up the required migration components on your **destination** database project as part of a quick-start migration with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions (destination)** section: 

#### Required permissions (destination)

The following permissions are required to perform homogeneous quick-start migrations with Database Migration Service: 

  * `datamigration.*`
  * `cloudsql.instances.create`
  * `cloudsql.instances.delete`
  * `cloudsql.instances.get`
  * `cloudsql.instances.list`
  * `cloudsql.instances.update`
  * `cloudsql.instances.connect`
  * `cloudsql.instances.executeSql`
  * `cloudsql.instances.export`
  * `cloudsql.instances.import`
  * `cloudsql.instances.login`
  * `cloudsql.operations.get`
  * `cloudsql.users.get`
  * `cloudsql.users.list`
  * `cloudsql.users.create`
  * `cloudsql.users.update`
  * `cloudsql.users.delete`



## Configure your source database

To configure your source PostgreSQL database, do the following:

  1. Create a dedicated migration user account in your instance. 
     * For Cloud SQL for PostgreSQL sources, see [ Create a user](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) in the Cloud SQL documentation. 
     * For other sources, see your database provider documentation or [ create and manage users](https://www.postgresql.org/docs/current/sql-createuser.html) in the PostgreSQL documentation. 
  2. Assign the necessary privileges to the dedicated migration user account. Run the following commands for each database you want to migrate: 
         
         -- Grant the REPLICATION attribute
         ALTER ROLE MIGRATION_USER REPLICATION;
         
         -- Grant database-level permissions.
         -- Repeat for each database you want to migrate.
         GRANT CONNECT, CREATE ON DATABASE DATABASE_NAME TO MIGRATION_USER;
         
         -- Grant schema-level usage.
         -- Repeat for each schema in each database you want to migrate.
         GRANT USAGE ON SCHEMA SCHEMA_NAME TO MIGRATION_USER;

Replace the following:

     * MIGRATION_USER with the name of the migration user account.
     * DATABASE_NAME with the name of the database you want to migrate.
     * SCHEMA_NAME with the name of the schema in the database you want to migrate.
  3. The migration user account needs to have ownership access to the tables you migrate. To grant this level of access, do one of the following: 
     * For sources other than Cloud SQL for PostgreSQL only: Assign the [ `SUPERUSER` PostgreSQL role](https://www.postgresql.org/docs/current/role-attributes.html#id-1.6.8.6.2.1.2.1.1) to the migration account. 
     * For all sources: Add the migration user account to the user group that owns the tables. Run the following command: 
           
           -- Grant table ownership.
           GRANT TABLE_OWNER_GROUP_NAME TO MIGRATION_USER;

Replace the following:

       * TABLE_OWNER_GROUP_NAME with the name of the user group that owns each table that you want to migrate. 
       * MIGRATION_USER with the name of the migration user account.
  4. **For tables that don't have primary keys** : By default, only `INSERT` operations are replicated for tables without primary keys during the Change Data Capture (CDC) phase. To replicate `UPDATE` and `DELETE` operations, you must set the table's [`REPLICA IDENTITY`](https://www.postgresql.org/docs/current/logical-replication-publication.html#LOGICAL-REPLICATION-PUBLICATION-REPLICA-IDENTITY) to `FULL` or `USING INDEX`: 
         
         ALTER TABLE TABLE_NAME REPLICA IDENTITY FULL;
         ALTER TABLE TABLE_NAME REPLICA IDENTITY USING INDEX INDEX_NAME;

Replace the following:

     * TABLE_NAME is the name of the table that doesn't have primary keys. 
     * INDEX_NAME is the unique index that can track rows from tables without primary keys. 
  5. Configure the replication settings using database flags. 

### Self-managed sources

Saving changes to database flags requires a full database restart. The following examples use SQL queries for changing flag values. If you can't run SQL queries directly, refer to your provider documentation for steps about changing these flags. 

     1. Set the [`wal_level`](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-WAL-LEVEL) parameter to `logical`. Run the following command: 
            
            ALTER SYSTEM SET wal_level = 'logical';

     2. Set the [`wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) parameter to `0`. This value disables the timeout mechanism that's used to terminate inactive replication connections. Run the following command: 
            
            ALTER SYSTEM SET wal_sender_timeout = 0;
                

     3. Configure the maximum number of replication slots with the [`max_replication_slots`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS) parameter. This parameter must be set to at least the number of databases you're migrating per migration job, plus some reserves for table synchronization. 

For example, if you're migrating 5 databases and there are 2 migration jobs created for the source instance, then the number of replication slots must be at least `5 * 2 = 10`, plus the number of replication slots already used by you. 

To set this parameter, run the following command:
            
            ALTER SYSTEM SET max_replication_slots = NUMBER_OF_SLOTS;
                

Where NUMBER_OF_SLOTS represents the maximum number of replication slots. 
     4. Configure the [`max_wal_senders`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS) parameter to at least the same value as `max_replication_slots`, plus the number of senders already used on your instance. 

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be `10 + 2 = 12`. 

To set this parameter, run the following command:
            
            ALTER SYSTEM SET max_wal_senders = NUMBER_OF_SENDERS;
                

Where NUMBER_OF_SENDERS represents the number of WAL sender processes running simultaneously. 
     5. Set the [`max_worker_processes`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES) to at least the number of databases that you want to migrate, plus the number of `max_worker_processes` already used on your instance. To set this parameter, run the following command: 
            
            ALTER SYSTEM SET max_worker_processes = NUMBER_OF_PROCESSES;
                

Where NUMBER_OF_PROCESSES represents the number of databases that will be migrated. 

### Cloud SQL for PostgreSQL sources

For Cloud SQL sources, you configure database flags in the Google Cloud console. You have to restart your instance after modifying database flags for the setting to take effect. For more information on setting database flags in Cloud SQL, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags) in the Cloud SQL documentation. 

     1. Set the `cloudsql.logical_decoding` flag to `on`.
     2. Set the `wal_sender_timeout` parameter to `0`. This value disables the timeout mechanism that's used to terminate inactive replication connections. 
     3. Configure the maximum number of replication slots with the `max_replication_slots` parameter. This parameter must be set to at least the number of databases you're migrating per migration job, plus some reserves for table synchronization. 

For example, if you're migrating 5 databases and there are 2 migration jobs created for the source instance, then the number of replication slots must be at least `5 * 2 = 10`, plus the number of replication slots already used by you. 

     4. Configure the `max_wal_senders` parameter to at least the same value as `max_replication_slots`, plus the number of senders already used on your instance. 

For example, if the `max_replication_slots` parameter is set to `10`, and you're already using 2 senders, then the number of WAL sender processes running at the same time would be `10 + 2 = 12`. 

     5. Set the `max_worker_processes` to at least the number of databases that you want to migrate, plus the number of `max_worker_processes` already used on your instance. 




## Create and run a quick-start migration

### Console

To create and run a quick-start migration using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Get started** page. 

[ Go to Get started ](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Source engine** menu, select **PostgreSQL**.
  3. In the **Destination engine** menu, select **CloudSQL for PostgreSQL**. 

The **Introducing quick-start PostgreSQL migration** section appears.

  4. In the **Introducing quick-start PostgreSQL migration** section, click **Start migration**. 

The **Migrate to Cloud SQL for PostgreSQL** page opens.

  5. In the **Configure migration** section, do the following: 
     1. From the **Destination region** menu, select the region of your destination Cloud SQL instance. 
     2. In the **Migration prefix** box, enter a human-friendly string that will be added to the names of all migration entities created for the quick-start migration: connection profiles, private connectivity configuration, network attachment and its subnet, and migration job. 
     3. From the **Configuration type** menu, select one of the following: 
        1. **Existing connectivity configuration** : Select this option if you already have a network attachment and a private connectivity configuration that uses Private Service Connect interfaces method. This option is best used if you previously used quick-start migrations and want to re-use the same networking resources. 
        2. **New connectivity configuration** : Select this option to create a new network attachment and the network attachment subnet in the source database VPC network. The private connectivity configuration will be created in the same project as your destination instance. 
     4. Click **Continue**.
  6. In the **Connect source** section, do the following: 
     1. Enter a **Hostname** or the private **IP address** of your source database. The source database address must be reachable from your source VPC network. 
     2. Enter the **Port** that's used to access the host. The default PostgreSQL port is `5432`.
     3. Enter the username and password for the dedicated migration account in your source database. 
     4. From the **Encryption type** menu, select one of the following: 
        * **None** : If your source database doesn't require SSL/TLS-encrypted connections.
        * **Required** : If your source database requires SSL/TLS-encrypted connections. This option doesn't require any certificate verification.
     5. In the **Databases to migrate** menu, click **Customize**. Use the side panel to select only the databases you want to migrate to Cloud SQL. 
     6. Click **Continue**.
  7. In the **Configure destination** section, you can create a new destination instance, or select an existing one. 

### New instances

If you want to create a new destination instance, do the following:

     1. From the **Destination instance type** menu, select **New instance**. 

Database Migration Service uses the default Cloud SQL configuration for a new instance. Click **Customize** to adjust instance features, such as the machine type, zonal availability, or data protection settings. For more informations on instance configuration, see [ Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance) in the Cloud SQL documentation. 

     2. In the **Password** field, enter a password for the default `postgresql` admin user. Database Migration Service connects as this user to migrate your data. 

### Existing instances

You can migrate databases to an instance that already exists. Make sure the destination instance is enabled for Private Service Connect and doesn't enforce mTLS connections. Do the following: 

     1. From the **Destination instance type** menu, select **Existing instance**. 
     2. From the **Existing instance ID** menu, select the instance identifier. 

  8. Click **Start migration**. 

Database Migration Service now creates the migration job and begins the migration process. You can monitor the migration progress in Database Migration Service migration job details. For more information, see [ Manage migration jobs](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions). 




### gcloud

To create and run a quick-start migration using the gcloud CLI, do the following:

  1. Configure the network attachment.  
Decide if you want to create a new network attachment or re-use an existing one. You need to have a network attachment in the network where your source database private IP can be reached. 

     * If you want to create a new network attachment, run the command following command (click to expand full details). 

#### `gcloud compute network-attachments create`

Before using any of the command data below, make the following replacements: 

       * NETWORK_ATTACHMENT with the name of the network attachment to create.
       * REGION with the region for the network attachment.
       * DEST_PROJECT_ID with the project ID of your destination project.
       * SOURCE_PROJECT_ID with the project ID where the source network resides.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute network-attachments create NETWORK_ATTACHMENT \
      --region=REGION \
      --connection-preference=ACCEPT_MANUAL \
      --producer-accept-list=DEST_PROJECT_ID \
      --subnets=default \
      --project=SOURCE_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute network-attachments create NETWORK_ATTACHMENT `
      --region=REGION `
      --connection-preference=ACCEPT_MANUAL `
      --producer-accept-list=DEST_PROJECT_ID `
      --subnets=default `
      --project=SOURCE_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute network-attachments create NETWORK_ATTACHMENT ^
      --region=REGION ^
      --connection-preference=ACCEPT_MANUAL ^
      --producer-accept-list=DEST_PROJECT_ID ^
      --subnets=default ^
      --project=SOURCE_PROJECT_ID

     * If you want to re-use an existing network attachment, proceed to the next step.
  2. Allow the Database Migration Service tenant project to access your network attachment.  
Your network attachment must allow connections from the Database Migration Service tenant project. Perform the following steps:

     1. Retrieve the Database Migration Service tenant project ID by performing a dry-run private connection creation (click to expand): 

#### `gcloud database-migration private-connections create --validate-only`

Before using any of the command data below, make the following replacements: 

        * PRIVATE_CONN with the name of the private connection resource.
        * REGION with the region for the private connection.
        * NETWORK_ATTACHMENT_URI with the URI of the network attachment.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration private-connections create PRIVATE_CONN \
      --region=REGION \
      --network-attachment=NETWORK_ATTACHMENT_URI \
      --display-name=PRIVATE_CONN \
      --format="value(metadata.metadata.tenant_project_id)" \
      --validate-only

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration private-connections create PRIVATE_CONN `
      --region=REGION `
      --network-attachment=NETWORK_ATTACHMENT_URI `
      --display-name=PRIVATE_CONN `
      --format="value(metadata.metadata.tenant_project_id)" `
      --validate-only

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration private-connections create PRIVATE_CONN ^
      --region=REGION ^
      --network-attachment=NETWORK_ATTACHMENT_URI ^
      --display-name=PRIVATE_CONN ^
      --format="value(metadata.metadata.tenant_project_id)" ^
      --validate-only

Save the returned tenant project ID to use with next commands.

     2. Allow the Database Migration Service tenant project and the destination project to connect to the network attachment (click to expand): 

#### `gcloud compute network-attachments update`

Before using any of the command data below, make the following replacements: 

        * NETWORK_ATTACHMENT with the name of the network attachment.
        * REGION with the region.
        * DEST_PROJECT_ID with the project ID of your destination project.
        * DMS_TENANT_ID with the retrieved Database Migration Service tenant project ID.
        * SOURCE_PROJECT_ID with the project ID where the source network resides.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute network-attachments update NETWORK_ATTACHMENT \
      --region=REGION \
      --producer-accept-list=DEST_PROJECT_ID,DMS_TENANT_ID \
      --project=SOURCE_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute network-attachments update NETWORK_ATTACHMENT `
      --region=REGION `
      --producer-accept-list=DEST_PROJECT_ID,DMS_TENANT_ID `
      --project=SOURCE_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute network-attachments update NETWORK_ATTACHMENT ^
      --region=REGION ^
      --producer-accept-list=DEST_PROJECT_ID,DMS_TENANT_ID ^
      --project=SOURCE_PROJECT_ID

  3. Create the Database Migration Service private connectivity resource.  
Run the following command (click to expand):

#### `gcloud database-migration private-connections create`

Before using any of the command data below, make the following replacements: 

     * PRIVATE_CONN with the name of the private connection resource.
     * REGION with the region for the private connection.
     * NETWORK_ATTACHMENT_URI with the URI of the network attachment.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration private-connections create PRIVATE_CONN \
      --region=REGION \
      --network-attachment=NETWORK_ATTACHMENT_URI \
      --display-name=PRIVATE_CONN

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration private-connections create PRIVATE_CONN `
      --region=REGION `
      --network-attachment=NETWORK_ATTACHMENT_URI `
      --display-name=PRIVATE_CONN

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration private-connections create PRIVATE_CONN ^
      --region=REGION ^
      --network-attachment=NETWORK_ATTACHMENT_URI ^
      --display-name=PRIVATE_CONN

  4. Create the source connection profile.  
Run the following command (click to expand):

#### `gcloud database-migration connection-profiles create postgresql`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * SOURCE_CONN_ID with your source connection profile identifier.
     * REGION with the region where you want to save the connection profile.
     * SOURCE_PRIVATE_IP with the private IP address of your source database.
     * SOURCE_PORT with the port of your source database (default is 5432).
     * SOURCE_USER with the username of the migration user on your source database.
     * SOURCE_PASSWORD with the password of the migration user on your source database.
     * PRIVATE_CONN with the name of the private connection resource.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql \
      SOURCE_CONN_ID \
      --region=REGION \
      --role=SOURCE \
      --host=SOURCE_PRIVATE_IP \
      --port=SOURCE_PORT \
      --username=SOURCE_USER \
      --password=SOURCE_PASSWORD \
      --private-connection=PRIVATE_CONN \
      --no-async

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql `
      SOURCE_CONN_ID `
      --region=REGION `
      --role=SOURCE `
      --host=SOURCE_PRIVATE_IP `
      --port=SOURCE_PORT `
      --username=SOURCE_USER `
      --password=SOURCE_PASSWORD `
      --private-connection=PRIVATE_CONN `
      --no-async

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql ^
      SOURCE_CONN_ID ^
      --region=REGION ^
      --role=SOURCE ^
      --host=SOURCE_PRIVATE_IP ^
      --port=SOURCE_PORT ^
      --username=SOURCE_USER ^
      --password=SOURCE_PASSWORD ^
      --private-connection=PRIVATE_CONN ^
      --no-async

  5. Create the destination connection profile.  
Select the tab based on whether you want to migrate to a new or an existing Cloud SQL instance:

### New instances

To use a new destination instance for the quick-start migration, first create the instance with Cloud SQL Google Cloud CLI, and then create the destination connection profile. Follow these steps: 

     1. [ Create an instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance) with Cloud SQL Google Cloud CLI. Make sure you use the [ `--enable-private-service-connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--enable-private-service-connect) flag to enable your destination instance for Private Service Connect. Quick-start migrations support only Private Service Connect-enabled instances. 
     2. Create the destination connection profile for your new instance. Expand the following section for full command details. 

#### `gcloud database-migration connection-profiles create postgresql`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

        * DEST_CONN_ID with the destination connection profile identifier.
        * REGION with the region where you want to save the connection profile. This region should be the same as your destination instance region. 
        * DEST_INSTANCE with the ID of your pre-created destination Cloud SQL instance.
        * DEST_USER with the username of the migration user on your destination database.
        * DEST_PASSWORD with the password for the migration user in the destination database.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID \
      --region=REGION \
      --cloudsql-instance=DEST_INSTANCE \
      --username=DEST_USER \
      --password=DEST_PASSWORD \
      --role=DESTINATION \
      --no-async

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID `
      --region=REGION `
      --cloudsql-instance=DEST_INSTANCE `
      --username=DEST_USER `
      --password=DEST_PASSWORD `
      --role=DESTINATION `
      --no-async

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID ^
      --region=REGION ^
      --cloudsql-instance=DEST_INSTANCE ^
      --username=DEST_USER ^
      --password=DEST_PASSWORD ^
      --role=DESTINATION ^
      --no-async

You should receive a response similar to the following:
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

### Existing instances

To migrate to an existing destination instance, create the connection profile pointing to the pre-created instance. Run the following command (click to expand):

#### `gcloud database-migration connection-profiles create postgresql`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * DEST_CONN_ID with the destination connection profile identifier.
     * REGION with the region where you want to save the connection profile. This region should be the same as your destination instance region. 
     * DEST_INSTANCE with the ID of your pre-created destination Cloud SQL instance.
     * DEST_USER with the username of the migration user on your destination database.
     * DEST_PASSWORD with the password for the migration user in the destination database.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID \
      --region=REGION \
      --cloudsql-instance=DEST_INSTANCE \
      --username=DEST_USER \
      --password=DEST_PASSWORD \
      --role=DESTINATION \
      --no-async

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID `
      --region=REGION `
      --cloudsql-instance=DEST_INSTANCE `
      --username=DEST_USER `
      --password=DEST_PASSWORD `
      --role=DESTINATION `
      --no-async

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles create postgresql DEST_CONN_ID ^
      --region=REGION ^
      --cloudsql-instance=DEST_INSTANCE ^
      --username=DEST_USER ^
      --password=DEST_PASSWORD ^
      --role=DESTINATION ^
      --no-async

You should receive a response similar to the following:
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

  6. Create the migration job.  
Run the following command (click to expand):

#### `gcloud database-migration migration-jobs create`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier.
     * REGION with the region where you want to save the migration job.
     * SOURCE_CONN_ID with the source connection profile identifier.
     * DEST_CONN_ID with the destination connection profile identifier.
     * DATABASES_LIST with a comma-separated list of databases you want to migrate.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs create \
      MIGRATION_JOB_ID \
      --region=REGION \
      --type=CONTINUOUS \
      --source=SOURCE_CONN_ID \
      --destination=DEST_CONN_ID \
      --use-postgres-native \
      --postgres-max-additional-subscriptions=10 \
      --databases-filter=DATABASES_LIST \
      --no-async

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs create `
      MIGRATION_JOB_ID `
      --region=REGION `
      --type=CONTINUOUS `
      --source=SOURCE_CONN_ID `
      --destination=DEST_CONN_ID `
      --use-postgres-native `
      --postgres-max-additional-subscriptions=10 `
      --databases-filter=DATABASES_LIST `
      --no-async

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs create ^
      MIGRATION_JOB_ID ^
      --region=REGION ^
      --type=CONTINUOUS ^
      --source=SOURCE_CONN_ID ^
      --destination=DEST_CONN_ID ^
      --use-postgres-native ^
      --postgres-max-additional-subscriptions=10 ^
      --databases-filter=DATABASES_LIST ^
      --no-async

You should receive a response similar to the following:
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    

  7. Run the migration job.  
Start the migration job (click to expand):

#### `gcloud database-migration migration-jobs start`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your connection profile is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    start MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    start MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    start MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: MIGRATION_JOB_ID
      verb: start
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

     * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
     * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.




## Finalize the migration

When you decide to switch your application to the new Cloud SQL instance, finalize the migration by following these steps:

  1. Stop all write operations on your source database. You can switch them to read-only mode to retain operational functionality. 
  2. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration). For quick-start migrations, your destination instance remains writable during the migration process. Promoting the migration job only ends the replication and doesn't have any impact on your destination instance. 
  3. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration) for completeness.



## What's next

  * [ Learn more about Cloud SQL](https://docs.cloud.google.com/alloydb/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

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



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

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
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


