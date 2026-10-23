---
url: https://docs.cloud.google.com/database-migration/docs/mysql/migrate-with-physical-xtrabackup/
title: Migrate your databases by using a Percona XtraBackup physical file \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:54.809593+00:00
---

# Migrate your databases by using a Percona XtraBackup physical file  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/migrate-with-physical-xtrabackup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Migrate your databases by using a Percona XtraBackup physical file Stay organized with collections  Save and categorize content based on your preferences. 

You can migrate your MySQL databases to Cloud SQL by using physical database backup files created with the [Percona XtraBackup for MySQL](https://www.percona.com/mysql/software/percona-xtrabackup) utility. Migrating with physical backup files offers increased data restoration speeds over migrations that use logical backup files. This makes them a great choice for moving big databases that contain multiple terabytes of data.

This migration flow involves the following tasks:

  1. Backing up your source MySQL instance and preparing the physical backup files by using the [Percona XtraBackup for MySQL](https://www.percona.com/mysql/software/percona-xtrabackup) utility.

  2. Uploading your backup files to a Cloud Storage bucket.

  3. Creating and running the migration job in Database Migration Service.

Depending on your scenario, you can create the destination instance on your own, or have Database Migration Service create the destination instance for you as a part of the migration job creation flow. For more information, see the Configure and run the migration job step.

  4. Promoting the migration job after the data is fully migrated.




### Offline migrations

This guide describes migration scenarios for environments where you can ensure network connectivity between your source and destination database instances.

It is possible to perform a test migration where Database Migration Service doesn't connect to your source instance. Instead, Database Migration Service only reads the backup files you upload to the Cloud Storage bucket and replicates their contents to the Cloud SQL for MySQL destination. A migration flow that doesn't use network connectivity isn't recommended for production migrations, as Database Migration Service can't fully perform data validation.

If you want to try to perform an offline migration job, adjust the procedures in the following way:

  * When you create the source connection profile, use a sample IP address, port, username and password. For example:

    * IP: `0.0.0.0`
    * Port: `1234`
    * Migration username: `test-user`
  * When you create the migration job:

    * Use public IP connectivity. Don't configure any additional networking options.
    * Use the [one-time migration job type](https://docs.cloud.google.com/database-migration/docs/mysql/migration-types).



## Limitations

This section lists limitations for the migrations that use Percona XtraBackup physical files:

  * Migrating to MySQL 5.6, 8.4, or 9.7 with a physical backup file is not supported. See [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations).

  * Cross-version considerations:

    * You can only migrate within the same database major version, for example from MySQL 8.0.30 to MySQL 8.0.35, or MySQL 5.7.0 to MySQL 5.7.1.
    * You can't migrate from MySQL 5.7 to MySQL 8.0.

    * Migration is not supported to earlier database major or minor versions. For example, you can't migrate from MySQL 8.0 to 5.7 or from MySQL 8.0.36 to 8.0.16.

  * Cross-architecture considerations: Cloud SQL supports ARM architecture. You can only migrate databases between machines of the same architecture type. For example, if your database is hosted on an ARM64 machine, then you must migrate to an ARM64 machine.

  * The disk size of the destination database must be equal to or greater than the source database size. For more information, see [MySQL machine types](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen) for your Cloud SQL edition.

  * Backups that contain files bigger than 5 TB aren't supported.

Maximum file size for Cloud Storage uploads is 5 TB. This limitation regards only the size of the backup files, not the total database size. You might be able to follow this migration scenario even if the total size of your database exceeds 5 TB. The backup file sizes are determined (among other settings) by the `innodb_file_per_table` flag:

    * If `innodb_file_per_table` is set to `OFF`, multiple tables can be saved to a single file. In that case, if your database is bigger than 5 TB, it might not be supported for this scenario.
    * When `innodb_file_per_table` is set to `ON`, every table is put into a separate `*.ibd` file. If you don't have a single table whose size exceeds 5 TB, your backup files should be eligible for uploading to Cloud Storage.

If your database total size exceeds 5 TB, and your data includes exceptionally big tables, we recommend that you first perform a dry-run backup to a local volume. This way you can verify that no backup file exceeds the 5 TB Cloud Storage limitation.

  * You must use Percona XtraBackup to backup up your data to the Cloud Storage bucket. Other backup utilities are not supported.

  * Make sure you upload the backup files to a dedicated Cloud Storage folder that doesn't contain any other files.

  * Database migration from a Percona XtraBackup physical file is only supported for on-premises or self-managed VM MySQL databases. Migration from Amazon Aurora or MySQL on Amazon RDS databases is not supported.

  * You can only migrate from a full backup. Other backup types, such as incremental or partial backups, are not supported.

  * Database migration does not include database users or privileges.

  * You must set the binary log format to `ROW`. If you configure the binary log to any other format, such as `STATEMENT` or `MIXED`, then replication might fail.

  * The `innodb_page_size` parameter on your source instance must be configured with the default value `16384`.

  * You can't migrate any plugins from your external database.




## Costs

For homogenous migrations to Cloud SQL, Database Migration Service is offered at no additional charge. However, Cloud SQL and Cloud Storage pricing applies for network charges as well as Cloud SQL and Cloud Storage entities created for migration purposes.

In this document, you use the following billable components of Google Cloud: 

  * Cloud Storage
  * Cloud SQL



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Consider in which [region](https://docs.cloud.google.com/docs/geography-and-regions) you want to create the destination database. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, storage buckets) must be saved in a single region. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Database Migration Service, Compute Engine, and Cloud SQL Admin APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,datamigration.googleapis.com,sqladmin.googleapis.com,storage.googleapis.com)




### Required roles

To get the permissions that you need to perform homogeneous MySQL migrations by using physical backup files, ask your administrator to grant you the following IAM roles on your project: 

  * User account that performs the migration: 
    * [Database Migration Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`)
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)
    * [Cloud SQL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform homogeneous MySQL migrations by using physical backup files. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous MySQL migrations by using physical backup files:

  * User account that performs the migration: 
    * `datamigration.*`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `cloudsql.instances.create`
    * `cloudsql.instances.get`
    * `cloudsql.instances.list`
    * `compute.machineTypes.list`
    * `compute.machineTypes.get`
    * `compute.projects.get`
    * `storage.buckets.create`
    * `storage.buckets.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Step 1. Consider your network connectivity requirements

There are different networking methods you can use to configure connectivity between your source and the Cloud SQL destination instances. Depending on which method you use, there might be additional steps you need to perform during the migration process.

Consider which connectivity method is right for your scenario before you proceed to the next steps, as your choice might impact the settings you need to use. For more information, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).

## Step 2. Prepare your source data

To prepare your data for migration, perform the following steps:

  1. Install the correct version of the Percona XtraBackup utility on your source instance. You must use a version of Percona XtraBackup that is equal to or later than your source instance version. For more information, see [Server version and backup version comparison](https://docs.percona.com/percona-xtrabackup/8.0/server-backup-version-comparison.html) in the Percona XtraBackup documentation. 
     * For MySQL 5.7, install [Percona XtraBackup 2.4](https://docs.percona.com/percona-xtrabackup/2.4/installation.html).
     * For MySQL 8.0, install [Percona XtraBackup 8.0](https://docs.percona.com/percona-xtrabackup/8.0/installation.html).
  2. Export and prepare the physical backup file of your source instance by using Percona XtraBackup. For complete information on using Percona XtraBackup, refer to the tool's [documentation](https://docs.percona.com/percona-xtrabackup/8.0/create-full-backup.html). You can also expand the following section for an example of recommended steps. 

####  Sample recommended steps for creating and preparing physical backup files by using Percona XtraBackup

Before using any of the command data below, make the following replacements:

     * TARGET_DIR with the path where you want to save the output backup file.
     * USERNAME with a user that has the `BACKUP_ADMIN` privilege on the source instance.
     * PASSWORD with the password for the USERNAME account.
     1. Perform a full physical backup of your source instance. Run the following command: 
            
            xtrabackup --backup \
                --target-dir=TARGET_DIR \
                --user=USERNAME \
                --password=PASSWORD
                  

     2. When the backup file is ready, use the `--prepare` command to ensure file consistency. Run the following command: 
            
            xtrabackup --prepare --target-dir=TARGET_DIR
                  

  3. [Create your bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store the backup files. Make sure you use the same region as the one where you intend to create your destination Cloud SQL for MySQL instance. 

Database Migration Service is a fully-regional product, meaning that all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, storage buckets for backup files) must be saved in a single region.

  4. Upload the backup files to your Cloud Storage bucket. Make sure you upload the backup files to a dedicated Cloud Storage folder that doesn't contain any other files. See [Upload objects from a file system](https://docs.cloud.google.com/storage/docs/uploading-objects) in the Cloud Storage documentation. 
  5. Create the source connection profile for your source database instance. 

### Console

To create a source connection profile, follow these steps:

     1. Go to the [Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles) page in the Google Cloud Console.
     2. Click **Create profile**.
     3. On the **Create a connection profile** page, from the **Database engine** drop-down menu, select **MySQL**
     4. In the **Connection profile name** field, enter a human-readable name for your connection profile. This value is displayed in the connection profile list.
     5. Keep the auto-generated **Connection profile ID**.
     6. Enter a **Hostname** or **IP address**. 
        * If the source database is hosted in Google Cloud, or if a reverse SSH tunnel is used to connect the destination database to the source database, then specify the private (internal) IP address for the source database. This address will be accessible by the Cloud SQL destination. For more information, see [Configure connectivity using VPC peering](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).

For other connectivity methods, such as [IP allowlist](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods), provide the public IP address.

     7. Enter the **Port** that's used to access the host. The default MySQL default port is 3306.
     8. Enter a username and password for the destination database. The user account must have the required privileges to access your data. For more information, see [ Configure source database for one-time migrations](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database) or [ Configure source database for continuous migrations](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database-continuous). 
     9. In the **Connection profile region** section of the page, select the region where you want to save the connection profile. Connection profiles, like all resources, are saved in a region. Region selection doesn't impact which migration jobs can use them, or which regions can connect to the data location itself, but can impact availability in the case of regional downtime.
     10. Optional: If the connection is made over a public network (by using IP allowlists), then we recommend using SSL/TLS encryption for the connection between the source and destination databases.

There are three options for the SSL/TLS configuration that you can select from the **Secure your connection** section of the page:

        1. None: The Cloud SQL destination instance connects to the source database without encryption.
        2. Server-only authentication: When the Cloud SQL destination instance connects to the source database, the instance authenticates the source, ensuring that the instance is connecting to the correct host securely. This prevents person-in-the-middle attacks. For server-only authentication, the source doesn't authenticate the instance.

To use server-only authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the external server's certificate.

For more information about creating certificates and keys for your external server, see [Creating SSL and RSA Certificates and Keys using MySQL](https://dev.mysql.com/doc/refman/5.7/en/creating-ssl-rsa-files-using-mysql.html).
        3. Server-client authentication: When the destination instance connects to the source, the instance authenticates the source and the source authenticates the instance. 

Server-client authentication provides the strongest security. However, if you don't want to provide the client certificate and private key when you create the Cloud SQL destination instance, you can still use server-only authentication.

To use server-client authentication, you must provide the following items when you create the destination connection profile:

           * The certificate of the CA that signed the source database server's certificate (the CA certificate).
           * The certificate used by the instance to authenticate against the source database server (the client certificate).
           * The private key associated with the client certificate (the client key).
For more information about creating certificates and keys for your source database server, see [ Creating SSL and RSA Certificates and Keys using MySQL](https://dev.mysql.com/doc/refman/5.7/en/creating-ssl-rsa-files-using-mysql.html).

If you're having trouble uploading the key, then select the **Enter manually** option, and copy and paste the key into the text area.

     11. Click **Create**. Your connection profile is now created.

### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile.
     * REGION with the identifier of the region where you want to save the connection profile.
     * HOST_IP_ADDRESS with the IP address where Database Migration Service can reach your source database instance. This value can vary depending on which [ connectivity method](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods) you use for your migration.
     * PORT_NUMBER with the port number where your source database accepts incoming connections. The default MySQL port is 3306.
     * USERNAME with the name of the database user account you want Database Migration Service to connect as to your source database instance.
     * PASSWORD with the password for the database user account.
     * (Optional) CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in the Google Cloud console. 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles \
    create mysql CONNECTION_PROFILE_ID \
      --no-async \
      --region=REGION \
      --host=HOST_IP_ADDRESS \
      --port=PORT_NUMBER \
      --username=USERNAME \
      --password=PASSWORD \
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles `
    create mysql CONNECTION_PROFILE_ID `
      --no-async `
      --region=REGION `
      --host=HOST_IP_ADDRESS `
      --port=PORT_NUMBER `
      --username=USERNAME `
      --password=PASSWORD `
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles ^
    create mysql CONNECTION_PROFILE_ID ^
      --no-async ^
      --region=REGION ^
      --host=HOST_IP_ADDRESS ^
      --port=PORT_NUMBER ^
      --username=USERNAME ^
      --password=PASSWORD ^
      --display-name=CONNECTION_PROFILE_NAME

You should receive a response similar to the following:
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    




## Step 3. Configure and run the migration job

When you migrate with Percona XtraBackup, you might want to create the Cloud SQL destination instance on your own, or have Database Migration Service create it for you. For more information, see [Migration job creation overview](https://docs.cloud.google.com/database-migration/docs/mysql/about-migration-jobs).

Each of these approaches requires you to follow a slightly different set of procedures. Use the drop-down menu to show the procedures relevant for your scenario:

  * If you want Database Migration Service to create the destination database for you, select **Migrate to a new destination instance**.
  * If you want to migrate to a destination database created outside Database Migration Service, select **Migrate to an existing destination instance**.

Make a selectionMigrate to a new destination instanceMigrate to an existing destination instance

  *   
When you migrate to a new destination instance, Database Migration Service creates the destination Cloud SQL for MySQL instance for you during the migration job creation flow. 

### Step 3a. Create the migration job to a new destination instance

To create a migration job to a new destination instance, follow these steps: 

### Console

### Define settings for the migration job

    1. In the Google Cloud console, go to the **Migration jobs** page. 

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

    2. Click **Create migration job**. 

The migration job configuration wizard page opens. This wizard contains multiple panels that walk you through each configuration step.

You can pause the creation of a migration job at any point by clicking **SAVE & EXIT**. All of the data that you enter up to that point is saved in a draft migration job. You can finish your draft migration job later.

    3. On the **Get started** page, enter the following information: 
       1. Migration job name 

This is a human-readable name for your migration job. This value is displayed in the Google Cloud console.

       2. Migration job ID 

This is a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.

       3. From the **Source database engine** list, select **MySQL**. 

The **Destination database engine** field is populated automatically and can't be changed.

       4. Select the region where you save the migration job. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases) must be saved in a single region. Select the region based on the location of the services that need your data, such as Compute Engine instances or App Engine apps, and other services. After you choose the destination region, this selection can't be changed. 

**Important:** If you plan to use the Cloud SQL for MySQL Enterprise Plus edition, make sure your region is supported for that edition. See [Cloud SQL for MySQL Enterprise Plus edition region support](https://docs.cloud.google.com/sql/docs/mysql/editions-intro#editions-regions). 
    4. Click **Save and continue**.

### Specify information about the source connection profile

    1. On the **Define a source** page, perform the following steps: 
       1. From the **Source connection profile** drop-down menu, select the connection profile for your source database.
       2. In the **Customize full dump configuration** section, click **Edit configuration**.
       3. In the **Edit full dump configuration** panel, from the **Full dump method** drop-down menu, select **Physical based**. 
       4. In the **Provide your folder** click **Browse** , and then select the folder where you uploaded your full dump file (step 3 in the Prepare your source data section). **Important:** Make sure you select the dedicated folder that contains the full backup file, and not the storage bucket itself. 
       5. Click **Save**.
    2. Click **Save and continue**.

### Configure and create the destination Cloud SQL instance

    1. On the **Define a destination** page, from the **Type of destination instance** drop-down menu, select **New instance**. Define all the relevant settings: 
       1. In the **Destination Instance ID** field, provide an identifier for the Cloud SQL instance or use the auto-generated identifier. 

Don't include sensitive or personally identifiable information in the identifier. There's no need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files).

       2. In the **Password** field, provide an alphanumeric password for the destination Cloud SQL instance. This is the password for the `root` administrator account in the instance. 

You can either enter the password manually or click **Generate** to have Database Migration Service create one for you automatically.

       3. From the **Database version** drop-down menu, choose the database version for the destination instance. 

Click **Show minor versions** to view all minor versions. [Learn more](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) about cross-version migration support.

       4. Select the Cloud SQL for MySQL edition for your destination instance. There are two options available: **Cloud SQL for MySQL Enterprise edition** and **Cloud SQL for MySQL Enterprise Plus edition**. 

Cloud SQL for MySQL editions come with different sets of features, available machine types, and pricing. Make sure you consult the Cloud SQL documentation to choose the edition that is appropriate for your needs. For more information, see [Introduction to Cloud SQL for MySQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).

       5. The **Region** menu shows the same region you selected on the **Get started** page. 

If you are configuring your instance for [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability), select **Multiple zones (Highly available)**. You can select both the primary and the secondary zone. The following conditions apply when the secondary zone is used during instance creation:

          * The zones default to **Any** for the primary zone and **Any (different from primary)** for the secondary zone.
          * If both the primary and secondary zones are specified, they must be different zones.
       6. In the **Connections** section, choose whether to add a public or a private IP address for your destination instance. You can configure your instance to have both types of IP addresses, but at least one type is required for the migration. Select one of the following: 
          * If you want to migrate by using VPC peering or a reverse SSH tunnel, select [**Private IP**](https://docs.cloud.google.com/sql/docs/mysql/connect-overview#private_ip). 
            * To enable private IP connectivity, make sure you meet all the additional networking requirements. 

#### Expand this section for full private IP requirements.

              * Service Networking API is enabled. You can enable the [Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com) by using the Google Cloud console.
              * You have the [`servicenetworking.services.addPeering` IAM permission](https://docs.cloud.google.com/iam/docs/permissions-reference).
              * You have [configured private services access](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods#configure-vpc-peering) for your project, for which you need to have the `compute.networkAdmin` IAM role.
              * There's at least one non-legacy VPC network in your project, or a Shared VPC network.
              * If you are using a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc), then you also need to do the following: 
                * Enable the Service Networking API for the host project.
                * Add your user to the host project.
                * Give your user the [compute.networkAdmin](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods#vpc-peering-requirements) IAM role in the host project.

            * Select the associated VPC network to peer. If you plan on connecting to the migration source by using VPC peering, then choose the VPC where the instance resides. 
            * If a managed service network was never configured for the selected VPC, you can choose to either select an IP range and click **Connect** or use an automatically selected IP range and click **Allocate & Connect**. 
          * If you want to migrate over the Internet by using an IP allowlist, select [**Public IP**](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).   


Optionally, under **Public IP** click the **Authorized networks** field, and either authorize a network or a proxy to connect to the Cloud SQL instance. Networks are only authorized with the addresses that you provide. See [Configure public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) in the Cloud SQL documentation.

You configure the migration job connectivity in a later step. To learn more about available networking methods, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods). 

    2. Select the machine type for the Cloud SQL instance.

For more information, see Limitations.

    3. **For Cloud SQL for MySQL Enterprise Plus edition** : Select the **Enable data cache** checkbox if you want to use the data cache feature in your destination database. 

Data cache is an optional feature available for Cloud SQL for MySQL Enterprise Plus edition instances that adds a high-speed local solid state drive to your destination database. This feature can introduce additional costs to your Cloud SQL. For more information on data cache, see [Data cache overview](https://docs.cloud.google.com/sql/docs/mysql/data-cache) in Cloud SQL documentation.

    4. Specify the storage type for the Cloud SQL instance. You can choose either a [solid-state drive (SSD) or a hard disk drive (HDD)](https://docs.cloud.google.com/sql/docs/mysql/choosing-ssd-hdd).
    5. Specify the storage capacity (in GBytes) for the Cloud SQL instance. 

Make sure the instance has enough storage capacity to handle the data from your source database. You can increase this capacity at any time, but you can't decrease it.

    6. (Optional) Configure data encryption options or [resource labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) for your destination instance. 

#### Expand this section to see the optional steps.

Click **Show optional configurations** , and then:

       1. Specify whether you want to manage the encryption of the data that's migrated from the source to the destination. By default, your data is encrypted with a key that's managed by Google Cloud. If you want to manage your encryption, then you can use a customer-managed encryption key (CMEK). To do so:

          1. Select the **Use a customer-managed encryption key (CMEK)** checkbox.
          2. From the **Select a customer-managed key** menu, select your CMEK.

If you don't see your key, then click **Enter key resource name** to provide the resource name of the key that you want to use. Example key resource name: `projects/my-project-name/locations/my-location/keyRings/my-keyring/cryptoKeys/my-key`.

As part of creating the migration job, Database Migration Service verifies that the CMEK exists, and that Database Migration Service has permissions to use the key. 

If Database Migration Service doesn't have these permissions, then information will appear, specifying that the Database Migration Service service account can't use the CMEK. Click **Grant** to give Database Migration Service permissions to use the key.

For more information about creating a CMEK, see [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek).

       2. Add any necessary flags to be applied to the database server. If possible, make sure that the database flags on the created destination Cloud SQL instance are the same as those on the source database. Learn more about supported database flags for [MySQL](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags). 
       3. Add any [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) that are specific to the Cloud SQL instance. 

Labels help organize your instances. For example, you can organize labels by cost center or environment. Labels are also included in your bill so you can see the distribution of costs across your labels. 

    7. Click **Create destination and continue**. Database Migration Service is now creating your Cloud SQL destination instance. This process can take several minutes. 
       * Database Migration Service creates a Cloud SQL instance for which you will be charged according to the configuration specified. If the migration job creation flow is exited before completion, then use the **Cancel** button to clean up the Cloud SQL instance. If the browser or tab is closed, **Save and exit** is clicked, or the screen is navigated away from, then the Cloud SQL instance isn't cleaned up and will need to be deleted manually from the Cloud SQL Instances page. 
       * After the destination instance is created, the Cloud SQL instance settings can no longer be edited in the Database Migration Service console. You can still access the instance directly in the Cloud SQL console to modify it. 

### Set up connectivity between the source and destination database instances

From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the newly created Cloud SQL instance will connect to the source database. Current network connectivity methods include [IP allowlist, reverse SSH tunnel, and VPC peering](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).

If you want to use...| Then...  
---|---  
The IP allowlist network connectivity method, | You need to specify the outgoing IP address of your destination instance. If the Cloud SQL instance you created is a high availability instance, include the outgoing IP addresses for both the primary and the secondary instance.  
The reverse SSH tunnel network connectivity method, | You need to select the Compute Engine VM instance that will host the tunnel. After specifying the instance, Google will provide a script that performs the steps to set up the tunnel between the source and destination databases. You'll need to run the script in the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).  Run the commands from a machine that has connectivity to both the source database and to Google Cloud.  
The VPC peering network connectivity method, | You need to select the VPC network where the source database resides. The Cloud SQL instance will be updated to connect to this network.  
  
After you select and configure network connectivity, click **Configure and continue**.

### Create the migration job

On the **Test and create migration job** , verify the settings for the migration job. At this point, testing the migration job will fail, because the service account associated with the Cloud SQL destination instance doesn't have the necessary permissions.

Perform one of the following actions before testing the job in order to validate job the configuration:

    * If you want to test your migration job by using the Google Cloud console after you assign the permissions to the destination instance service account, click **Save and exit**. This action saves your migration job as draft. You can come back to this screen later, test your migration job and run it.
    * If you want to test your migration job by using Google Cloud CLI after you assign the permissions to the destination instance service account,click **Create**. With Google Cloud CLI, you can test a migration job that is created but not yet started.

### gcloud

    1. Create the destination connection profile.  
When you migrate to a new destination instance with Google Cloud CLI, you create the destination instance and the connection profile in a single action.  
Run the following command (click the link to expand):

#### `gcloud database-migration connection-profiles create cloudsql`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

       * CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile.
       * DATABASE_VERSION with the MySQL version that you want to use in the destination instance. Database versions are specified as strings that include both the major, and the minor version. For example: `MYSQL_8_0`, `MYSQL_8_0_32`, `MYSQL_8_0_36`. 

For all possible MySQL versions, see the [ \--database-version flag reference](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--database-version).

       * (Optional) EDITION By default, new instances you create with Google Cloud CLI use Cloud SQL for MySQL Enterprise Plus edition. If you plan to use Cloud SQL for MySQL Enterprise Plus edition, make sure your region is supported for that edition. See [Cloud SQL for MySQL Enterprise Plus edition region support](https://docs.cloud.google.com/sql/docs/mysql/editions-intro#editions-regions). 

You can change your edition by using the `--edition` flag with one of the following values:

         * `enterprise-plus` for the Cloud SQL for MySQL Enterprise Plus edition
         * `enterprise` for the Cloud SQL for MySQL Enterprise edition
       * TIER with the name of the Cloud SQL machine type you want to use. Machine types are specified as strings that follow the Cloud SQL convention, for example `db-n1-standard-1`, `db-perf-optimized-N-2`. For a full list of available machine types and their identifiers for use with Google Cloud CLI, see [ Machine types](https://docs.cloud.google.com/sql/docs/mysql/create-instance#machine-types) in Cloud SQL for MySQL documentation. 

Instances created with Google Cloud CLI by default use the Cloud SQL for MySQL Enterprise Plus edition that has different machine types available. If you want to use a machine type that is available only in the Cloud SQL for MySQL Enterprise edition, use the optional `--edition=enterprise` flag to specify the edition. 

       * REGION with the identifier of the region where you want to save the connection profile. 

By default, new instances you create with Google Cloud CLI use Cloud SQL for MySQL Enterprise Plus edition. If you plan to use Cloud SQL for MySQL Enterprise Plus edition, make sure your region is supported for that edition. See [Cloud SQL for MySQL Enterprise Plus edition region support](https://docs.cloud.google.com/sql/docs/mysql/editions-intro#editions-regions). You can change the edition by using the optional `--edition` flag.

       * (Optional) CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in the Google Cloud console. 
       * **Networking configuration**

By default, new instances you create with Google Cloud CLI have a public IP address assigned, and are configured to use public IP connectivity. You can use other connectivity methods. For more information, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity).

You don't need to use additional flags if you want to use public IP connectivity. If you want to use private IP connectivity with VPC Network Peering or a reverse-SSH tunnel, make sure you meet the following additional network requirements for enabling private IP connectivity and include additional flags in your command. 

#### Expand this section for full private IP requirements.

         * Service Networking API is enabled. You can enable the [ Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com) by using the Google Cloud console.
         * You have the [ `servicenetworking.services.addPeering` IAM permission](https://docs.cloud.google.com/iam/docs/permissions-reference).
         * You have [ configured private services access](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-vpc-peering#configure-access) for your project, for which you need to have the `compute.networkAdmin` IAM role.
         * There's at least one non-legacy VPC network in your project, or a Shared VPC network.
         * If you are using a [ Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc), then you also need to do the following: 
           * Enable the Service Networking API for the host project.
           * Add your user to the host project.
           * Give your user the [ compute.networkAdmin](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-vpc-peering#network-admin-role) IAM role in the host project. 

Include the following additional flags if you want to use private IP connectivity (**with VPC Network Peering** or **with a reverse-SSH tunnel on a Compute Engine VM**):

         * [ `--no-enable-ip-v4`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--enable-ip-v4): (Optional) To **not** assign a public IP address to your destination instance. You can have both a public and a private IP address assigned to your destination instance, but you might not want a public IP address if you use private IP connectivity.
         * [ `--private-network`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--private-network): To assign a private IP address to your destination instance, specify the name of the Virtual Private Cloud where you want to have a private IP address assigned. 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles \
    create mysql CONNECTION_PROFILE_ID \
      --no-async \
      --region=REGION \
      --database-version=DATABASE_VERSION \
      --tier=TIER \
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles `
    create mysql CONNECTION_PROFILE_ID `
      --no-async `
      --region=REGION `
      --database-version=DATABASE_VERSION `
      --tier=TIER `
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles ^
    create mysql CONNECTION_PROFILE_ID ^
      --no-async ^
      --region=REGION ^
      --database-version=DATABASE_VERSION ^
      --tier=TIER ^
      --display-name=CONNECTION_PROFILE_NAME

You should receive a response similar to the following:
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

    2. Complete the network configuration setup.

Depending on what network connectivity you want to use, there might be additional steps you need to follow before you create the migration job.

       * If you use the default **public IP connectivity** , configure your source database instance to allow connections from your Cloud SQL destination's public address and port. For more information, see [Configure connectivity using IP allowlists](https://docs.cloud.google.com/database-migration/docs/mysql/configure-src-connection-self-hosted#ip-allowlist).
       * If you use a **reverse SSH tunnel** , set up the tunnel on a Compute Engine VM. For more information, see [Configure connectivity using a reverse SSH tunnel](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-reverse-ssh-tunnel).
    3. Create the migration job.   
Run the following command (click the link to expand): 

#### `gcloud database-migration migration-jobs create`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

       * MIGRATION_JOB_ID with a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.
       * REGION with the region identifier where you want to save the migration job.
       * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
       * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile.
       * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
       * MIGRATION_JOB_TYPE with the type of your migration job. Two values are allowed: `ONE_TIME` or `CONTINUOUS`. For more information, see [ Types of migration](https://docs.cloud.google.com/database-migration/docs/mysql/migration-types#continuous-migration).
       * PATH_TO_THE_FOLDER_IN_STORAGE_BUCKET_WITH_PHYSICAL_BACKUP_FILES with the path to your physical backup files stored in a folder in a Cloud Storage bucket. Use the following format: `gs://<[bucket_name](https://docs.cloud.google.com/storage/docs/buckets#naming)>/<[path_to_backup_file_folder>](https://docs.cloud.google.com/storage/docs/objects#namespace)`. 
       * **Networking configuration**

If you use private IP connectivity with VPC Network Peering or a reverse-SSH tunnel, add the following flags to your command:

Private IP connectivity with VPC Network Peering
    Use the [ `--peer-vpc`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--peer-vpc) flag to specify the name of the network you want to peer with. 
Reverse-SSH tunnel on a Compute Engine VM
    Use the following flags to provide networking details for the Compute Engine: [ `--vm-ip`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm-ip), [ `--vm-port`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm-port), [ `--vpc`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vpc). You can also use the optional [ `--vm`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm) flag to specify the name of the VM. 

For more usage examples, see [ Google Cloud CLI examples](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#EXAMPLES). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    create MIGRATION_JOB_ID \
      --no-async \
      --region=REGION \
      --display-name=MIGRATION_JOB_NAME \
      --source=SOURCE_CONNECTION_PROFILE_ID \
      --destination=DESTINATION_CONNECTION_PROFILE_ID \
      --type=MIGRATION_JOB_TYPE
      --dump-type=PHYSICAL
      --dump-path=PATH_TO_THE_FOLDER_IN_STORAGE_BUCKET_WITH_PHYSICAL_BACKUP_FILES

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    create MIGRATION_JOB_ID `
      --no-async `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME `
      --source=SOURCE_CONNECTION_PROFILE_ID `
      --destination=DESTINATION_CONNECTION_PROFILE_ID `
      --type=MIGRATION_JOB_TYPE
      --dump-type=PHYSICAL
      --dump-path=PATH_TO_THE_FOLDER_IN_STORAGE_BUCKET_WITH_PHYSICAL_BACKUP_FILES

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    create MIGRATION_JOB_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME ^
      --source=SOURCE_CONNECTION_PROFILE_ID ^
      --destination=DESTINATION_CONNECTION_PROFILE_ID ^
      --type=MIGRATION_JOB_TYPE
      --dump-type=PHYSICAL
      --dump-path=PATH_TO_THE_FOLDER_IN_STORAGE_BUCKET_WITH_PHYSICAL_BACKUP_FILES

You should receive a response similar to the following:
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    

### Step 3b. Grant the required permissions to the Cloud SQL instance service account

When you create the migration job to a new instance, Database Migration Service also creates the destination Cloud SQL instance for you. Before you can run the migration, you need to assign Cloud Storage permissions for the instance's service account.

To grant the Cloud Storage permissions to the service account associated with your destination instance, follow these steps: 

    1. Find the service account email address for your Cloud SQL instance on the Cloud SQL instance detail page. This address uses the following format: `<project-identifier>@gcp-sa-cloud-sql.iam.gserviceaccount.com`. See [View instance information](https://docs.cloud.google.com/sql/docs/mysql/instance-info#service_account) in the Cloud SQL documentation. 
    2. Add the **Storage Object Viewer** (`roles/storage.objectViewer`) IAM role to the service account. For information on how to manage access with Identity and Access Management, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation. 

### Step 3c. (Optional) Test the migration job

Before you run the migration job, you can perform a test operation to check if Database Migration Service can reach all the necessary source and destination entities. With gcloud CLI, you can test migration jobs that are created, but not yet started.

### Console

In the Google Cloud console, you can only test draft migration jobs that you create in the migration job creation wizard. If you didn't save your job as a draft, but fully created it in the wizard, you can only perform the test by using Google Cloud CLI.

To test a draft migration job, follow these steps:

    1. In the Google Cloud console, go to the **Migration jobs** page. 

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

    2. In the **Drafts** tab, click the display name of the migration job that you want to finish creating. 

The migration job creation wizard opens.

    3. On the **Test and create migration job** page, click **Test job**. Database Migration Service now checks whether your destination instance has all the required permissions and can connect to the source database.
    4. When the test finishes, click **Create**. 

The migration job is now created and ready to be started.

### gcloud

Before using any of the command data below, make the following replacements: 

    * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

    * REGION with the identifier of the region where your connection profile is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    verify MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    verify MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    verify MIGRATION_JOB_ID ^
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
      verb: verify
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

    * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
    * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.

### Step 3d. Start the migration job

When your migration job is fully created (that is, it isn't saved in a draft state), you can start it at any time to begin migrating data. 

To start a migration job, perform the following steps:

### Console

    1. In the Google Cloud console, go to the **Migration jobs** page. 

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

    2. In the **Jobs** tab, click the display name of the migration job that you want to start. 

The migration job details page opens.

    3. Click **Start**.
    4. In the dialog, click **Start**.

### gcloud

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

  *   
To migrate to an existing destination instance, you first need to create and configure your destination instance. 

### Step 3a. Prepare your destination instance

To configure your destination Cloud SQL instance, perform the following steps:

    1. Create your Cloud SQL for MySQL destination instance. Make sure you use enough compute and memory resources to cover your migration needs. See [Create an instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance) in Cloud SQL documentation. 

Depending on what connectivity method you want to use for your migration, you might need to add a public or a private IP address to your destination instance. For more information on connectivity methods, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).

    2. Grant the Cloud Storage permissions to the service account associated with your destination instance. This account is created after you create the destination instance. 
       1. Find the service account email address for your Cloud SQL instance on the Cloud SQL instance detail page. This address uses the following format: `<project-identifier>@gcp-sa-cloud-sql.iam.gserviceaccount.com`. See [View instance information](https://docs.cloud.google.com/sql/docs/mysql/instance-info#service_account) in the Cloud SQL documentation. 
       2. Add the **Storage Object Viewer** (`roles/storage.objectViewer`) IAM role to the service account. For information on how to manage access with Identity and Access Management, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation. 
    3. Create a destination connection profile for your Cloud SQL instance. 

### Console

You don't need to create the destination connection profile. When you create a migration job in the Google Cloud console, you use the destination instance identifier and Database Migration Service manages the connection profile for you.

Proceed to the Create and run migration job section.

### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

       * CONNECTION_PROFILE_ID with a machine-readable identifier for your connection profile.
       * REGION with the identifier of the region where you want to save the connection profile.
       * DESTINATION_INSTANCE_ID with the instance identifier of your destination instance. 
       * (Optional) CONNECTION_PROFILE_NAME with a human-readable name for your connection profile. This value is displayed in the Google Cloud console. 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles \
    create mysql CONNECTION_PROFILE_ID \
      --no-async \
      --cloudsql-instance=DESTINATION_INSTANCE_ID \
      --region=REGION \
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles `
    create mysql CONNECTION_PROFILE_ID `
      --no-async `
      --cloudsql-instance=DESTINATION_INSTANCE_ID `
      --region=REGION `
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration connection-profiles ^
    create mysql CONNECTION_PROFILE_ID ^
      --no-async ^
      --cloudsql-instance=DESTINATION_INSTANCE_ID ^
      --region=REGION ^
      --display-name=CONNECTION_PROFILE_NAME

You should receive a response similar to the following:
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

### Step 3b. Create and run the migration job

### Console

### Define settings for the migration job

    1. In the Google Cloud console, go to the **Migration jobs** page. 

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

    2. Click **Create migration job**. 

The migration job configuration wizard page opens. This wizard contains multiple panels that walk you through each configuration step.

You can pause the creation of a migration job at any point by clicking **SAVE & EXIT**. All of the data that you enter up to that point is saved in a draft migration job. You can finish your draft migration job later.

    3. On the **Get started** page, enter the following information: 
       1. Migration job name 

This is a human-readable name for your migration job. This value is displayed in the Google Cloud console.

       2. Migration job ID 

This is a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.

       3. From the **Source database engine** list, select **MySQL**. 

The **Destination database engine** field is populated automatically and can't be changed.

       4. Select the region where you save the migration job. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases) must be saved in a single region. Select the region based on the location of the services that need your data, such as Compute Engine instances or App Engine apps, and other services. After you choose the destination region, this selection can't be changed. 

**Important:** If you plan to use the Cloud SQL for MySQL Enterprise Plus edition, make sure your region is supported for that edition. See [Cloud SQL for MySQL Enterprise Plus edition region support](https://docs.cloud.google.com/sql/docs/mysql/editions-intro#editions-regions). 
    4. Click **Save and continue**.

### Specify information about the source connection profile

    1. On the **Define a source** page, perform the following steps: 
       1. From the **Source connection profile** drop-down menu, select the connection profile for your source database.
       2. In the **Customize full dump configuration** section, click **Edit configuration**.
       3. In the **Edit full dump configuration** panel, from the **Full dump method** drop-down menu, select **Physical based**. 
       4. In the **Provide your folder** click **Browse** , and then select the folder where you uploaded your full dump file (step 4 in the Prepare your source data section). **Important:** Make sure you select the dedicated folder that contains the full backup file, and not the storage bucket itself. 
       5. Click **Save**.
    2. Click **Save and continue**.

### Select the destination Cloud SQL instance

    1. From the **Type of destination instance** menu, select **Existing instance**. 
    2. In the **Select destination instance** section, select your destination instance. 
    3. Review the information in the **Instance details** section, and click **Select and continue**. 
    4. To migrate to an existing destination database, Database Migration Service demotes the target instance and converts it to a replica. To signify that the demotion can be safely performed, in the confirmation window, enter the destination instance identifier. 
    5. Click **Confirm and continue**.

### Set up connectivity between the source and destination database instances

From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the newly created Cloud SQL instance will connect to the source database. Current network connectivity methods include [IP allowlist, reverse SSH tunnel, and VPC peering](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).

If you want to use...| Then...  
---|---  
The IP allowlist network connectivity method, | You need to specify the outgoing IP address of your destination instance. If the Cloud SQL instance you created is a high availability instance, include the outgoing IP addresses for both the primary and the secondary instance.  
The reverse SSH tunnel network connectivity method, | You need to select the Compute Engine VM instance that will host the tunnel. After specifying the instance, Google will provide a script that performs the steps to set up the tunnel between the source and destination databases. You'll need to run the script in the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).  Run the commands from a machine that has connectivity to both the source database and to Google Cloud.  
The VPC peering network connectivity method, | You need to select the VPC network where the source database resides. The Cloud SQL instance will be updated to connect to this network.  
  
After you select and configure network connectivity, click **Configure and continue**.

### Test, create, and run the migration job

On this final step, review the summary of the migration job settings, source, destination, and connectivity method, and then test the validity of the migration job setup. If any issues are encountered, then you can modify the migration job's settings. Not all settings are editable. 

    1. On the **Test and create migration job** page, click **Test job**. 

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test. For information troubleshooting a failing migration job test, see [Diagnose issues for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues). 

    2. When the migration job test finishes, click **Create and start job**. 

Your migration is now in progress. When you start the migration job, Database Migration Service begins the full dump, briefly locking the source database.

**Caution:** If you used Terraform to provision your destination database, you might experience configuration drift during the migration job execution. Don't try to re-apply Terraform settings before the migration is complete. For more information, see [Terraform configuration drift](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#existing-instance-terraform-config-drift). 

### gcloud

To configure and run your migration, perform the following steps: 

    1. Create the migration job.   
Run the following command (click the link to expand): 

#### `gcloud database-migration migration-jobs create`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

       * MIGRATION_JOB_ID with a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.
       * REGION with the region identifier where you want to save the migration job.
       * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
       * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile.
       * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
       * MIGRATION_JOB_TYPE with the type of your migration job. Two values are allowed: `ONE_TIME` or `CONTINUOUS`. For more information, see [ Types of migration](https://docs.cloud.google.com/database-migration/docs/mysql/migration-types#continuous-migration).
       * PATH_TO_THE_FOLDER_IN_STORAGE_BUCKET_WITH_PHYSICAL_BACKUP_FILES with the path to your physical backup files stored in a folder in a Cloud Storage bucket. Use the following format: `gs://<[bucket_name](https://docs.cloud.google.com/storage/docs/buckets#naming)>/<[path_to_backup_file_folder>](https://docs.cloud.google.com/storage/docs/objects#namespace)`. 
       * **Networking configuration**

If you use private IP connectivity with VPC Network Peering or a reverse-SSH tunnel, add the following flags to your command:

Private IP connectivity with VPC Network Peering
    Use the [ `--peer-vpc`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--peer-vpc) flag to specify the name of the network you want to peer with. 
Reverse-SSH tunnel on a Compute Engine VM
    Use the following flags to provide networking details for the Compute Engine: [ `--vm-ip`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm-ip), [ `--vm-port`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm-port), [ `--vpc`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vpc). You can also use the optional [ `--vm`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#--vm) flag to specify the name of the VM. 

For more usage examples, see [ Google Cloud CLI examples](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#EXAMPLES). 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    create MIGRATION_JOB_ID \
      --no-async \
      --region=REGION \
      --display-name=MIGRATION_JOB_NAME \
      --source=SOURCE_CONNECTION_PROFILE_ID \
      --destination=DESTINATION_CONNECTION_PROFILE_ID \
      --type=MIGRATION_JOB_TYPE
      --dump-type=PHYSICAL
      --dump-path=PATH_TO_THE_FOLDER_IN_STORAGE_BUCKET_WITH_PHYSICAL_BACKUP_FILES

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    create MIGRATION_JOB_ID `
      --no-async `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME `
      --source=SOURCE_CONNECTION_PROFILE_ID `
      --destination=DESTINATION_CONNECTION_PROFILE_ID `
      --type=MIGRATION_JOB_TYPE
      --dump-type=PHYSICAL
      --dump-path=PATH_TO_THE_FOLDER_IN_STORAGE_BUCKET_WITH_PHYSICAL_BACKUP_FILES

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    create MIGRATION_JOB_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME ^
      --source=SOURCE_CONNECTION_PROFILE_ID ^
      --destination=DESTINATION_CONNECTION_PROFILE_ID ^
      --type=MIGRATION_JOB_TYPE
      --dump-type=PHYSICAL
      --dump-path=PATH_TO_THE_FOLDER_IN_STORAGE_BUCKET_WITH_PHYSICAL_BACKUP_FILES

You should receive a response similar to the following:
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    

    2. Demote your Cloud SQL destination instance.  
Run the following command (click the link to expand): 

#### `gcloud database-migration migration-jobs demote-destination`

Before using any of the command data below, make the following replacements: 

       * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

       * REGION with the identifier of the region where your connection profile is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    demote-destination MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    demote-destination MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    demote-destination MIGRATION_JOB_ID ^
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
      verb: demote-destination
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

       * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
       * Use the [ `gcloud database-migration operations describe`](https://cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.

    3. (Optional) Perform a migration job test  
You can run a check to verify if Database Migration Service can reach all the necessary source and destination entities. Run the following command (click the link to expand): 

#### gcloud database-migration migration-jobs verify

Before using any of the command data below, make the following replacements: 

       * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

       * REGION with the identifier of the region where your connection profile is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    verify MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    verify MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    verify MIGRATION_JOB_ID ^
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
      verb: verify
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

       * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
       * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.

    4. Start the migration job.  
Run the following command (click the link to expand): 

#### gcloud database-migration migration-jobs start

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

When you start the migration job, your destination Cloud SQL instance is put into a read-only mode where it is fully managed by Database Migration Service. You can promote it to a standalone instance when your data is fully migrated. 

Note: You can monitor the migration progress, as well as your destination instance health with Database Migration Service observability features. See [Migration job metrics](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-metrics). 




## Step 4. (Optional) Stop the migration

You can stop and delete your migration job at any point if you want to cancel the data migration process. You can manage the migration job in the Google Cloud console or with Google Cloud CLI.

  * For information on managing migration jobs in the Google Cloud console, see [Manage migration jobs](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-actions).

  * For information on managing migration jobs with Google Cloud CLI, see [`gcloud database-migration migration-jobs` reference](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/stop).




## Step 5. Finalize the migration

When the migration job completes successfully, finalize the migration job by performing one of the following steps:

  * **For one-time migrations** : Migration job status changes to **Complete**. No further actions required, you can clean up the migration job and connection profile resources.

  * **For continuous migrations** : [Promote the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/promote-migration) to switch your application to the new database instance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
