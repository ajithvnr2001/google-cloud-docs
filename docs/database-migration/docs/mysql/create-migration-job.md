---
url: https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job/
title: Create a migration job to a new destination instance \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:51.119213+00:00
---

# Create a migration job to a new destination instance  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Create a migration job to a new destination instance Stay organized with collections  Save and categorize content based on your preferences. 

When you create your destination instance with Database Migration Service, that instance is automatically demoted and runs as a read-only replica. This means that some operations are limited. For example, if you want to create users in your new destination while the migration is in progress, then use Cloud SQL in the Google Cloud console. For more information, see [Manage users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users) in the Cloud SQL documentation.

Database Migration Service uses migration jobs to migrate data from your source database instance to the destination database instance. Creating a migration job for a new destination instance includes:

  * Defining settings for the migration job
  * Selecting the source database connection profile
  * Defining settings for the destination Cloud SQL database instance and creating the instance
  * Setting up connectivity between the source and destination database instances
  * Testing the migration job to ensure that the connection information you provided for the job is valid

**Note:** For private IP connectivity, when you migrate to a Cloud SQL instance created with Database Migration Service, you can only use the [ private services access method (VPC peering)](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access). If you want to use Private Service Connect with your destination cluster, first [create the destination instance directly in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect), and then follow the steps on the [ Migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) page.

## Before you begin

Before you create a migration job to a new destination database instance, make sure you:

  1. Verify that this migration type can support your scenario. For more details, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations). 
  2. Configure your source database and establish network connectivity. Creating a migration job is one of the steps in the full migration process. We recommend you follow the step-by-step migration walkthrough and return to this procedure when you reach the migration job step. See [ Migrate to a new instance](https://docs.cloud.google.com/database-migration/docs/mysql/guide-to-new-instance). 



To create a migration job to a new destination instance, do the following:

### Console

### Define settings for the migration job

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Click **Create migration job**. 

The migration job configuration wizard page opens. This wizard contains multiple panels that walk you through each configuration step.

You can pause the creation of a migration job at any point by clicking **Save and exit**. All of the data that you enter up to that point is saved in a draft migration job. You can finish your draft migration job later.

  3. On the **Get started** page, enter the following information: 
     1. Migration job name 

This is a human-readable name for your migration job. This value is displayed in the Google Cloud console.

     2. Migration job ID 

This is a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.

     3. From the **Source database engine** list, select **MySQL**. 

The **Destination database engine** field is populated automatically and can't be changed.

     4. Select the [region](https://docs.cloud.google.com/docs/geography-and-regions) where you save the migration job. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases) must be saved in a single region. Select the region based on the location of the services that need your data, such as Compute Engine instances or App Engine apps, and other services. After you choose the destination region, this selection can't be changed. 

**Important:** If you plan to use the Cloud SQL for MySQL Enterprise Plus edition, make sure your region is supported for that edition. See [Cloud SQL for MySQL Enterprise Plus edition region support](https://docs.cloud.google.com/sql/docs/mysql/editions-intro#editions-regions)
  4. Click **Save and continue**.



### Specify information about the source connection profile

On the **Define a source** page, perform the following steps:

  1. From the **Source connection profile** drop-down menu, select the connection profile for your source database.
  2. In the **Customize full dump configuration** section, click **Edit configuration**.
  3. In the **Edit full dump configuration** panel, from the **Full dump method** drop-down menu, select one of the following: 
     * **Physical based** : Select this option if you want to use Percona XtraBackup utility to provide your own backup file. This approach requires additional preparation steps. For the full guide on using physical backup files generated by Percona XtraBackup, see [Migrate your databases by using a Percona XtraBackup physical file](https://docs.cloud.google.com/database-migration/docs/mysql/migrate-with-physical-xtrabackup).
     * **Logical based** : Select this option if you want to use a logical backup file created by the `mysqldump` utility. Database Migration Service can auto-generate this backup file for you, or you can provide your own copy. 
  4. Edit the rest of the dump settings. Perform one of the following: 
     * If you use the physical backup file, in the **Provide your folder** click **Browse** , and then select the folder where you uploaded your full dump file. Make sure you select the dedicated folder that contains the full backup file, and not the storage bucket itself. 
     * If you use a logical backup file, configure the data dump parallelism or dump flags.

#### Expand this section for full logical backup file steps

In the **Choose how to generate your dump file** section, use one of the following options:

       1. **Auto-generate the initial dump (recommended)**

This option is recommended because Database Migration Service always generates an initial database dump file after the migration job is created and started.

Database Migration Service uses this file to reproduce the original object definitions and table data of your source database so that this information can be migrated into a destination Cloud SQL database instance.

If you use the auto-generated dump, select the type of operation Database Migration Service should perform in the **Configure data dump operation** section:

          * **Data dump parallelism** : use a high-performance parallelism option, available when migrating to MySQL versions 5.7 or 8. If you choose to use load parallelism, make sure you provide the necessary privileges on the source database for your scenario (such as `LOCK_TABLES`). For more information on required permissions for source databases, see [ Configure source database for one-time migrations](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database) or [ Configure source database for continuous migrations](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database-continuous). 

The speed of data parallelism is related to the amount of load induced on your source database:

            * **Optimal (recommended)** : Balanced performance with optimal load on the source database.
            * **Maximum** : Provides the highest dump speeds, but might cause increased load on the source database.
            * **Minimum** : Takes the lowest amount of compute resources on the source database, but might have slower dump throughput.
          * **Dump flags** : This option is exclusive with **Data dump parallelism**. Use this setting to directly configure flags for the `mysqldump` utility that's used to create the dump file. 

To add a flag:

            1. Click **ADD FLAG**.
            2. Select one of the following flags:

               * `add-locks:` This flag surrounds each table that's contained in the dump file with `LOCK TABLES` and `UNLOCK TABLES` statements. This results in faster inserts when the dump file is loaded into the destination instance. 
               * `ignore-error:` Use this flag to enter a list of comma-separated error numbers. These numbers represent the errors that the `mysqldump` utility will ignore. 
               * `max-allowed-packet:` Use this flag to set the maximum size of the buffer for communication between the MySQL client and the source MySQL database. The default size of the buffer is 24 MB; the maximum size is 1 GB. If you're using large `BLOB` columns or long strings in the tables of the source database, then you must increase the size of the buffer for this flag.
For more information about these flags, see the documentation about the [`mysqldump`](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) utility in the 
            3. Click **DONE**.
            4. Repeat these steps for each flag that you want to add.

To remove a flag, click the trashcan icon to the right of the row that contains the flag.

       2. **Provide your own**

This option is **not recommended** because by default Database Migration Service performs an initial dump as part of the migration job run.

If you want to use your own dump file, select **Provide your own** , click **BROWSE** , select your file (or the whole Cloud Storage folder if you use multiple files), and then click **SELECT**.

Make sure the dump was generated within the last 24 hours and adheres to the [dump requirements](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump). 

  5. Click **Save and continue**.



### Configure and create the destination Cloud SQL instance

  1. On the **Define a destination** page, from the **Type of destination instance** drop-down menu, select **New instance**. Define all the relevant settings: 
     1. In the **Destination Instance ID** field, provide an identifier for the Cloud SQL instance or use the auto-generated identifier. 

Don't include sensitive or personally identifiable information in the identifier. There's no need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files).

     2. In the **Password** field, provide an alphanumeric password for the destination Cloud SQL instance. This is the password for the `root` administrator account in the instance. 

You can either enter the password manually or click **Generate** to have Database Migration Service create one for you automatically.

     3. From the **Database version** drop-down menu, choose the database version for the destination instance. 

Click **Show minor versions** to view all minor versions. Learn more about [ cross-version migration support](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest).

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
            * You have [configured private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) for your project, for which you need to have the `compute.networkAdmin` IAM role.
            * There's at least one non-legacy VPC network in your project, or a Shared VPC network.
            * If you are using a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc), then you also need to do the following: 
              * Enable the Service Networking API for the host project.
              * Add your user to the host project.
              * Give your user the `compute.networkAdmin` IAM role in the host project.

          * Select the associated VPC network to peer. If you plan on connecting to the migration source by using VPC peering, then choose the VPC where the instance resides. 
          * If a managed service network was never configured for the selected VPC, you can choose to either select an IP range and click **Connect** or use an automatically selected IP range and click **Allocate & Connect**. 
        * If you want to migrate over the Internet by using an IP allowlist, select **Public IP**.   


Optionally, under **Public IP** click the **Authorized networks** field, and either authorize a network or a proxy to connect to the Cloud SQL instance. Networks are only authorized with the addresses that you provide. See [Configure public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) in the Cloud SQL documentation.

You configure the migration job connectivity in a later step. To learn more about available networking methods, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods). 

  2. Select the machine type for the Cloud SQL instance. The disk size must be equal to or greater than the source database size. Learn more about [MySQL](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen) machine types. **Note:** Machines available in the **Machine type** selection depend on the Cloud SQL edition you use. 
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
     3. Add any [ labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) that are specific to the Cloud SQL instance. 

Labels help organize your instances. For example, you can organize labels by cost center or environment. Labels are also included in your bill so you can see the distribution of costs across your labels.

  7. Click **Create destination and continue**. Database Migration Service is now creating your Cloud SQL destination instance. This process can take several minutes. **Key point:**
     * Database Migration Service creates a Cloud SQL instance for which you will be charged according to the configuration specified. If the migration job creation flow is exited before completion, then use the **Cancel** button to clean up the Cloud SQL instance. If the browser or tab is closed, **Save and exit** is clicked, or the screen is navigated away from, then the Cloud SQL instance isn't cleaned up and will need to be deleted manually from the Cloud SQL Instances page. 
     * After the destination instance is created, the Cloud SQL instance settings can no longer be edited in the Database Migration Service console. You can still access the instance directly in the Cloud SQL console to modify it. 



### Set up connectivity between the source and destination database instances

From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the newly created Cloud SQL instance will connect to the source database. Current network connectivity methods for migrating to a new instance include [ IP allowlist, reverse SSH tunnel, VPC peering, and _specialized VPC peering for Cloud SQL for MySQL sources only_](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).

If you want to use...| Then...  
---|---  
The IP allowlist network connectivity method, | You need to specify the outgoing IP address of your destination instance. If the Cloud SQL instance you created is a high availability instance, include the outgoing IP addresses for both the primary and the secondary instance.  
The reverse SSH tunnel network connectivity method, | You need to select the Compute Engine VM instance that will host the tunnel. After specifying the instance, Google will provide a script that performs the steps to set up the tunnel between the source and destination databases. You'll need to run the script in the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) Run the commands from a machine that has connectivity to both the source database and to Google Cloud.  
The VPC peering network connectivity method, | You need to select the VPC network where the source database resides. The Cloud SQL instance will be updated to connect to this network.  
  
After you select and configure network connectivity, click **Configure and continue**.

### Configure migration databases

You can migrate all databases from your source instance, or choose only specific databases. Your destination instance can't contain any databases that share the name with the databases you choose for migration. If Database Migration Service encounters a database name collision, the offending database is dropped in the destination before the migration. 

  1. From the **Databases to migrate** list, select one of the following options: 
     * **All databases** : Selects all databases that exist on the source.
     * **Specific databases** : Lets you select specific databases from all databases that exist on the source.
  2. If you want to migrate specific databases, you can filter the list that appears and select the databases that you want Database Migration Service to migrate into your destination.

If the list doesn't appear and a database discovery error is displayed, click **Reload**. If database discovery fails, the job migrates all databases. You can continue with creating a migration job and fix connectivity errors later.

  3. Click **Save and continue**.



### Test, create, and run the migration job

On this final step, review the summary of the migration job settings, source, destination, and connectivity method, and then test the validity of the migration job setup. If any issues are encountered, then you can modify the migration job's settings. Not all settings are editable. 

  1. On the **Test and create migration job** page, click **Test job**. 

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test. For information troubleshooting a failing migration job test, see [Diagnose issues for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues)

  2. When the migration job test finishes, click **Create and start job** to create the migration job and start it immediately, or click **Create job** to create the migration job without immediately starting it. 

If the job isn't started at the time that it's created, then it can be started from the **Migration jobs** page by clicking **START**. Regardless of when the migration job starts, your organization is charged for the existence of the destination instance. 

Your migration is now in progress. When you start the migration job, Database Migration Service begins the full dump, briefly locking the source database. If your source is in Amazon RDS or Amazon Aurora, Database Migration Service additionally requires a short (approximately under a minute) write downtime at the start of the migration. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations#parallelism-considerations).

**Caution:** If you used Terraform to provision your destination database, you might experience configuration drift during the migration job execution. Don't try to re-apply Terraform settings before the migration is complete. For more information, see [Terraform configuration drift](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#existing-instance-terraform-config-drift)
  3. Proceed to [Review the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-actions). 



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
    

  2. Create the migration job.   
If you use VPC peering or a reverse-SSH tunnel connectivity, make sure to add the required flags, such as `--peer-vpc`, or `--vm`, `--vm-ip`, `--vm-port`, `--vpc`. For more information, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods) and [Google Cloud CLI examples](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#EXAMPLES).  
Run the following command (click the link to expand): 

#### `gcloud database-migration migration-jobs create`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.
     * REGION with the region identifier where you want to save the migration job.
     * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
     * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile.
     * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
     * Optional: Database Migration Service migrates all databases in your source by default. If you want to migrate only specific databases, use the `--databases-filter` flag and specify their identifiers as a comma-separated list.

For example: `--databases-filter=my-business-database,my-other-database`

You can later edit migration jobs that you created with the `--databases-filter` flag by using the [`gcloud database-migration migration-jobs update`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update) command.

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

You should receive a response similar to the following:
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
