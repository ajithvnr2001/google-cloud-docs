---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance/
title: Create a migration job to an existing destination instance \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:26.238905+00:00
---

# Create a migration job to an existing destination instance  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Create a migration job to an existing destination instance Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


## Overview

Database Migration Service uses migration jobs to migrate data from your source database instance to the destination database instance.

Creating a migration job for an existing destination instance includes:

  * Defining settings for the migration job
  * Selecting the source database connection profile
  * Selecting the existing destination database instance
  * Demoting the existing instance to convert it into a read replica
  * Setting up connectivity between the source and destination database instances
  * Testing the migration job to ensure that the connection information you provided for the job is valid



There are certain limitations that you should consider when you want to migrate to a destination instance created outside of Database Migration Service. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#existing-instance-limitations).

Database Migration Service wizard helps you create a migration job. This wizard consists of the following panes: **Get started** , **Define a source** , **Create a destination** , **Define connectivity method** , **Configure migration databases** , and **Test and create migration job**. Information on how to populate each pane is provided in the following sections of this page.

## Create a migration job by using the Google Cloud console

You can pause the creation of a migration job by clicking **Save and exit**. All of the data that was populated until that point is saved in a draft migration job, and you can access this job in a **Drafts** tab.

To finish creating a migration job, navigate to the tab, and then click the job. The creation flow resumes from where it was left off. The job remains a draft until you click **Create** or **Create and start**.

### Define settings for the migration job

  1. Go to the [Migration jobs](https://console.cloud.google.com/dbmigration/migrations) in the Google Cloud console.

  2. Click **Create migration job** at the top of the page.

  3. Provide a name for the migration job. Choose a friendly name that helps you identify the migration job. Don't include sensitive or personally identifiable information in the job name.

  4. Keep the auto-generated **Migration job ID**. 

  5. Select the source database engine.

  6. Select **AlloyDB for PostgreSQL** as the destination engine. 

  7. Select the destination region for your migration. This region must be the same as the one where your destination database is located. After you choose the destination region, this selection can't be changed. 

  8. Choose **Continuous** (snapshot + ongoing changes) as the migration job type. 

  9. In the **Before you continue, review the prerequisites** section, click **Open** to view automatically generated instructions that can help guide you through preparing your source database for the migration. It's best to complete these prerequisites at this step, but you can complete them at any time before you test, or start, the migration job. For more information, see [Configure your source](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/postgresql-to-alloydb/configure-source-database).

  10. Click **Save and continue**.




### Specify information about the source connection profile

  1. If you have created a connection profile, then select it from the list of existing connection profiles.

If you haven't created a connection profile, then create one by clicking **Create a connection profile** at the bottom of the drop-down list, and then perform the same steps as in [Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-source-connection-profile).

It is recommended to create a designated connection profile for your AlloyDB migration.

  2. In the **Customize data dump configurations** section, click **Show data dump configurations**. 

The speed of data dump parallelism is related to the amount of load on your source database. You can use the following settings:

     * **Optimal (recommended)** : Balanced performance with optimal load on the source database.
     * **Maximum** : Provides the highest dump speeds, but might cause increased load on the source database.
     * **Minimum** : Takes the lowest amount of compute resources on the source database, but might have slower dump throughput.

If you want to use adjusted data dump parallelism settings, make sure to increase the `max_replication_slots`, `max_wal_senders`, and `max_worker_processes` parameters on your source database. You can verify your configuration by  running the migration job test at the end of migration job creation. 

  3. Click **Save and continue**.



If your source database is a Cloud SQL instance and has only public IP enabled, make sure to [enable its private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip) before continuing to the next section. Remember to update the connection profile with the private IP.

### Select the destination instance

**For Cloud SQL sources:** If you are migrating from a Cloud SQL instance that uses a Private IP connection to a Cloud SQL instance that uses a [non-RFC 1918 address](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) IP range, add the non-RFC 1918 range to the network configuration of your source Cloud SQL instance. See [Configure authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) in Cloud SQL documentation.

  1. From the **Type of destination cluster** menu, select **Existing cluster**.
  2. In the **Select destination cluster** section, select your destination cluster.
  3. Review the information about your cluster, and click **Select and continue**.
  4. To migrate to an existing destination database, Database Migration Service demotes the target instance and converts it to a replica. To signify that the demotion can be safely performed, in the confirmation window, enter the destination instance identifier.
  5. Click **Confirm and continue**.



### Set up connectivity between the source and destination database instances

Note: In case your source is Cloud SQL for PostgreSQL, depending on whether your Cloud SQL source instance is on the old network architecture or the new network architecture, the connectivity options are limited to **VPC Peering** and **TCP Proxy via a cloud-hosted VM**. 

  1. From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the newly created AlloyDB cluster will connect to the source database. Current network connectivity methods include [IP allowlist, VPC peering, Private Service Connect interfaces, reverse SSH tunnel, and TCP proxy through a cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods). 
  2. If you select the IP allowlist network connectivity method, you need to specify the outgoing IP address of your destination instance. Copy the outgoing IP addresses for both the primary and the secondary instance and use them to configure the network firewall for your source database server and in the `pg_hba.conf` file, so that the source can accept connections from these addresses. 
  3. If you select the reverse SSH tunnel network connectivity method, then select the Compute Engine VM instance that will host the tunnel.

After specifying the instance, Google will provide a script that performs the steps to set up the tunnel between the source and destination databases. You'll need to run the script in the [Google Cloud CLI](https://cloud.google.com/sdk/gcloud/?_ga=2.255980105.-371130741.1588278357).

Run the commands from a machine that has connectivity to both the source database and to Google Cloud.

  4. If you use one of the [private IP connectivity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering) methods, select **VPC peering** or **PSC interface**.
  5. If you select the VPC peering network connectivity method, then select the VPC network where the source database resides. The Cloud SQL instance will be updated to connect to this network. 
  6. If you select the TCP Proxy via cloud-hosted VM connectivity method, then enter the required details for the new Compute Engine VM instance that will host the TCP proxy.

After specifying the details, the Google Cloud console will provide a script that performs the steps to set up the proxy between the source and destination databases. You'll need to run the script on a machine with an updated [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

After running the script, it will output the newly created VM's private IP. Enter the IP and click **Configure & continue**.

  7. After selecting the network connectivity method and providing any additional information for the method, click **CONFIGURE & CONTINUE**. 



### Configure migration databases

You can select the databases that you want to migrate.

  1. From the **Databases to migrate** list, select one of the following options: 
     * **All databases** : Selects all databases that exist on the source.
     * **Specific databases** : Lets you select specific databases from all databases that exist on the source.
  2. If you want to migrate specific databases, you can filter the list that appears and select the databases that you want Database Migration Service to migrate into your destination.

If the list doesn't appear and a database discovery error is displayed, click **Reload**. If database discovery fails, the job migrates all databases. You can continue with creating a migration job and fix connectivity errors later.

  3. Click **Save and continue**.



### Test and create the migration job

On this final step, review the summary of the migration job settings, source, destination, and connectivity method, and then test the validity of the migration job setup. If any issues are encountered, then you can modify the migration job's settings. Not all settings are editable.

  1. Click **TEST JOB** to verify that:

     * The source database has been configured correctly, based on the prerequisites. 
     * The source and destination instances can communicate with each other. 
     * Any updates to private IP addresses needed on the destination are done. 
     * The migration job is valid, and the source and destination versions are compatible. 

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test.

For more information about reasons why the test might fail and how to troubleshoot any issues associated with the test failing, see [ Diagnose issues for AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues).

The migration job can be created even if the test fails, but after the job is started, it may fail at some point during the run.

  2. Click **CREATE & START JOB** to create the migration job and start it immediately, or click **CREATE JOB** to create the migration job without immediately starting it.

If the job isn't started at the time that it's created, then it can be started from the **Migration jobs** page by clicking **START**.

Regardless of when the migration job starts, your organization is charged for the existence of the destination instance.

When you start the migration job, Database Migration Service begins the full dump, briefly locking the source database. If your source is in Amazon RDS or Amazon Aurora, Database Migration Service additionally requires a short (approximately under a minute) write downtime at the start of the migration. For more information, see [ Data dump parallelism considerations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#parallelism-considerations).

  3. The migration job is added to the migration jobs list and can be viewed directly.

  4. Proceed to [Review the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/review-migration-job).




## Create a migration job by using Google Cloud CLI

When you migrate to an existing instance by using Google Cloud CLI, you must manually create the connection profile for the destination instance. This isn't required when you use the Google Cloud console, as Database Migration Service takes care of creating and removing the destination connection profile for you.

### Before you begin

Before you use gcloud CLI to create a migration job to an existing destination database instance, make sure you:

  * Create your destination database instance.
  * Prepare your source database instance. See: 
    * [Configure your source](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database)
    * [Create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-source-connection-profile) (Source connection profile identifier is required to create a migration job.)
    * [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity)



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
    create postgresql CONNECTION_PROFILE_ID \
      --no-async \
      --alloydb-cluster=DESTINATION_INSTANCE_ID \
      --region=REGION \
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles `
    create postgresql CONNECTION_PROFILE_ID `
      --no-async `
      --alloydb-cluster=DESTINATION_INSTANCE_ID `
      --region=REGION `
      --display-name=CONNECTION_PROFILE_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration connection-profiles ^
    create postgresql CONNECTION_PROFILE_ID ^
      --no-async ^
      --alloydb-cluster=DESTINATION_INSTANCE_ID ^
      --region=REGION ^
      --display-name=CONNECTION_PROFILE_NAME

You should receive a response similar to the following:
    
    
    Waiting for connection profile [CONNECTION_PROFILE_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created connection profile CONNECTION_PROFILE_ID [OPERATION_ID]
    

### Create the migration job

**Note:** The following examples represent a migration scenario where you use the Private IP connectivity between the source and destination databases. If you use a different connectivity type (for example VPC peering or a reverse-SSH tunnel), make sure to add the required flags, such as `--peer-vpc`, or `--vm, --vm-ip, --vm-port, --vpc`. For more informations, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity) and [Google Cloud CLI examples](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#EXAMPLES).**Note:** Only [continuous migration type](https://docs.cloud.google.com/database-migration/docs/postgres/migration-types#continuous-migration) is supported for migrations to AlloyDB.

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
      --type=CONTINUOUS \

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    create MIGRATION_JOB_ID `
      --no-async `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME `
      --source=SOURCE_CONNECTION_PROFILE_ID `
      --destination=DESTINATION_CONNECTION_PROFILE_ID `
      --type=CONTINUOUS `

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    create MIGRATION_JOB_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME ^
      --source=SOURCE_CONNECTION_PROFILE_ID ^
      --destination=DESTINATION_CONNECTION_PROFILE_ID ^
      --type=CONTINUOUS ^

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

At this point, your migration job is configured and connected to your destination database instance. You can manage it by using the following operations:

  1. Optional: Verify the migration job.  
We recommend that you first verify your migration job by running the [`gcloud database-migration migration-jobs verify`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/verify) command.

For more information, expand the following section:

#### `gcloud database-migration migration-jobs verify`

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

  2. Optional: Retrieve information about databases selected for migration.  
When you migrate specific databases, Database Migration Service needs to retrieve the details about the databases that you selected for the migration job by using the `--database-filter` flag.

Before you start the migration job, run the [`gcloud database-migration migration-jobs fetch-source-objects`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/fetch-source-objects) command.

For more information, expand the following section:

#### `gcloud database-migration migration-jobs fetch-source-objects`

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your connection profile is saved.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    fetch-source-objects MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    fetch-source-objects MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    fetch-source-objects MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The output is similar to the following: 
    
    Waiting for migration job MIGRATION_JOB_ID
    to fetch source objects with OPERATION_ID
    
    Waiting for operation OPERATION_ID to complete...done.
    
    SOURCE_OBJECT                                      STATE         PHASE              ERROR
    {'database': 'DATABASE_NAME', 'type': 'DATABASE'}  NOT_SELECTED  PHASE_UNSPECIFIED
    {'database': 'DATABASE_NAME', 'type': 'DATABASE'}  STOPPED       CDC                {'code': 1, 'message': 'Internal error'}
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

     * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
     * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.

  3. Start the migration job.  
Start the migration job by running the [`gcloud database-migration migration-jobs start`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/start) command.

For more information, expand the following section:

#### `gcloud database-migration migration-jobs start`

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

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
    * [ Builders Hub ](https://me.developers.google.com/)
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


