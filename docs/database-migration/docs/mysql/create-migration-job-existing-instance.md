---
url: https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance/
title: Create a migration job to an existing destination instance \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:15.667019+00:00
---

# Create a migration job to an existing destination instance  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Create a migration job to an existing destination instance Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service uses migration jobs to migrate data from your source database instance to the destination database instance. Creating a migration job for an existing destination instance includes:

  * Defining settings for the migration job
  * Selecting the source database connection profile
  * Selecting the existing destination database instance
  * Demoting the existing instance to convert it into a read replica
  * Setting up connectivity between the source and destination database instances
  * Testing the migration job to ensure that the connection information you provided for the job is valid



## Before you begin

Before you create a migration job to an existing destination database instance, make sure you:

  1. Verify that this migration type can support your scenario. For example, when you want to migrate to a database created outside Database Migration Service, the Cloud SQL destination instance must be empty or contain only system configuration data. For more details, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations#existing-instance-limitations). 
  2. Create the necessary resources, configure your source database and establish network connectivity. Creating a migration job is one of the steps in the full migration process. We recommend you follow the step-by-step migration walkthrough and return to this procedure when you reach the migration job step. See [ Migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/mysql/guide-to-existing-instance). 



## Create a migration job with the Google Cloud console

When you migrate to an existing instance with the Google Cloud console, Database Migration Service automatically manages the destination connection profile for you. To create a migration job to an existing instance with the Google Cloud console, do the following:

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

       1. **Auto-generated (recommended)**

This option is recommended because Database Migration Service always generates an initial database dump file after the migration job is created and started.

Database Migration Service uses this file to reproduce the original object definitions and table data of your source database so that this information can be migrated into a destination Cloud SQL database instance.

If you use the auto-generated dump, select the type of operation Database Migration Service should perform in the **Configure data dump operation** section:

          * **Data dump parallelism** : use a high-performance parallelism option, available when migrating to MySQL versions 5.7 or 8. If you choose to use data dump parallelism, make sure you provide the necessary privileges on the source database for your scenario (such as `LOCK_TABLES`). For more information on required permissions for source databases, see [ Configure source database for one-time migrations](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database) or [ Configure source database for continuous migrations](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database-continuous). 

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



### Select the destination Cloud SQL instance

  1. From the **Type of destination instance** menu, select **Existing instance**. 
  2. In the **Select destination instance** section, select your destination instance. 
  3. Review the information in the **Instance details** section, and click **Select and continue**. 

To migrate to an existing destination database, Database Migration Service demotes the target instance and converts it to a replica. To signify that the demotion can be safely performed, in the confirmation window, enter the destination instance identifier. 

  4. Click **Confirm and continue**.



### Set up connectivity between the source and destination database instances

From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the newly created Cloud SQL instance will connect to the source database. Current network connectivity methods include [IP allowlist, reverse SSH tunnel, Private Service Connect interfaces, and VPC peering](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods)

If you want to use...| Then...  
---|---  
The IP allowlist network connectivity method, | You need to specify the outgoing IP address of your destination instance. If the Cloud SQL instance you created is a high availability instance, include the outgoing IP addresses for both the primary and the secondary instance.  
The reverse SSH tunnel network connectivity method, | You need to select the Compute Engine VM instance that will host the tunnel. After specifying the instance, Google will provide a script that performs the steps to set up the tunnel between the source and destination databases. You'll need to run the script in the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).  Run the commands from a machine that has connectivity to both the source database and to Google Cloud.  
The Private Service Connect interfaces connectivity method, | Database Migration Service automatically establishes the required connections. This connectivity method is only available if you have the Private Service Connect-enabled instance with a network attachment. For more information on Private Service Connect interfaces, see [Private Service Connect outbound connections](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-outbound) in the Cloud SQL documentation.   
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



## Create a migration job by using Google Cloud CLI

When you migrate to an existing instance by using Google Cloud CLI, you must manually create the connection profile for the destination instance. This isn't required when you use the Google Cloud console, as Database Migration Service takes care of creating and removing the destination connection profile for you.

### Create destination connection profile

Create the destination connection profile for your existing destination instance by running the [`gcloud database-migration connection-profiles create`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create) command:

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
    

### Create the migration job

**Note:** The following examples represent a migration scenario where you use the Private IP connectivity between the source and destination databases. If you use a different connectivity type (for example VPC peering or a reverse-SSH tunnel), make sure to add the required flags, such as `--peer-vpc`, or `--vm, --vm-ip, --vm-port, --vpc`. For more information, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods) and [Google Cloud CLI examples](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#EXAMPLES).

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
      --type= \

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    create MIGRATION_JOB_ID `
      --no-async `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME `
      --source=SOURCE_CONNECTION_PROFILE_ID `
      --destination=DESTINATION_CONNECTION_PROFILE_ID `
      --type= `

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    create MIGRATION_JOB_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME ^
      --source=SOURCE_CONNECTION_PROFILE_ID ^
      --destination=DESTINATION_CONNECTION_PROFILE_ID ^
      --type= ^

You should receive a response similar to the following:
    
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    

### Demote the destination database

Database Migration Service requires that the destination database instance works as a read replica for the time of migration. Before you start the migration job, run the `gcloud database-migration migration-jobs demote-destination` command to demote the destination database instance.

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



### Manage migration jobs

At this point, your migration job is configured and connected to your destination database instance. You can manage it by using the [`verify`,`start`, `stop`, `restart`, and `resume` operations](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs).

#### Verify the migration job

We recommend you first verify your migration job, by running the [`gcloud database-migration migration-jobs verify`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/verify) command.

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



#### Start the migration job

Start the migration job by running the [`gcloud database-migration migration-jobs start`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/start) command.

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



### Promote the migration job

Once the migration reaches the Change Data Capture (CDC) phase, you can promote the destination database instance from a read replica to a standalone instance. Run the [`gcloud database-migration migration-jobs promote`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/promote) command:

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    promote MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    promote MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    promote MIGRATION_JOB_ID ^
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
