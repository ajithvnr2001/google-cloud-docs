---
url: https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job/
title: Create a migration job to a new destination instance \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:16.244202+00:00
---

# Create a migration job to a new destination instance  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Create a migration job to a new destination instance Stay organized with collections  Save and categorize content based on your preferences. 

When you create your destination instance with Database Migration Service, that instance isn't demoted and doesn't run in read-only mode, but executing certain operations during the migration process might result in migration errors. As you migrate to a new destination instance, keep the following operational considerations in mind:

  * **Avoid write operations on migrating data:** Don't perform write operations (such as `INSERT`, `UPDATE`, `DELETE`, or DDL schema changes) in the destination instance on tables or databases included in the migration. Such operations might lead to replication conflicts with data coming from the source. 
  * **Manage database users:** You can create and manage database users at any time using standard `psql` commands or through Cloud SQL in the Google Cloud console. For more information, see [Manage users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) in the Cloud SQL documentation.
  * **Backups and read replicas:** Automated backups and point-in-time recovery (PITR) are suspended during continuous replication, and you can't create Cloud SQL read replicas from the destination instance until the migration job is promoted.



For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations). 

Creating a migration job includes:

  1. Defining settings for the migration job.
  2. Defining source settings and selecting databases to migrate.
  3. Defining settings for the destination Cloud SQL database instance and creating the instance.
  4. Setting up connectivity between the source and destination database instances.
  5. Testing the migration job to ensure that the connection information you provided for the job is valid.

**Note:** For private IP connectivity, when you migrate to a Cloud SQL instance created with Database Migration Service, you can only use the [private services access method (VPC peering)](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access). If you want to use Private Service Connect with your destination cluster, first [create the destination instance directly in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect), and then follow the steps on the [Migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance) page.

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

     3. From the **Source database engine** list, select **PostgreSQL**. 

The **Destination database engine** field is populated automatically with **Cloud SQL for PostgreSQL** and can't be changed.

     4. Select the [region](https://docs.cloud.google.com/docs/geography-and-regions) where you save the migration job. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases) must be saved in a single region. Select the region based on the location of the services that need your data, such as Compute Engine instances or App Engine apps, and other services. After you choose the destination region, this selection can't be changed. 

**Important:** If you plan to use the Cloud SQL for PostgreSQL Enterprise Plus edition, make sure your region is supported for that edition. See [Cloud SQL for PostgreSQL Enterprise Plus edition region support](https://docs.cloud.google.com/sql/docs/postgres/editions-intro#editions-regions). 
     5. Specify the migration job type: **One-time** or **Continuous**. 
     6. Review the prerequisites generated for your environment. Make sure your source database is configured appropriately. For more information, see [Configure source database](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database). 
  4. Click **Save and continue**.



### Specify information about the source connection profile

On the **Define a source** page, perform the following steps:

  1. From the **Source connection profile** drop-down menu, select the connection profile for your source database (or click **Create a connection profile** , see [Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles)). 
  2. In the **Customize parallelism configurations** section, click **Show parallelism configurations**. 

The speed of data dump parallelism is related to the amount of load induced on your source database. You can use the following settings:

     * **Optimal (recommended)** : Balanced performance with optimal load on the source database.
     * **Maximum** : Provides the highest dump speeds, but might cause increased load on the source database.
     * **Minimum** : Takes the lowest amount of compute resources on the source database, but might have slower dump throughput.

If you choose adjusted parallelism settings, make sure to increase the `max_replication_slots`, `max_wal_senders`, and `max_worker_processes` parameters on your source database. You can verify your configuration by running the migration job test at the end of migration job creation. 

  3. Click **Save and continue**.



### Configure and create the destination Cloud SQL instance

  1. On the **Define a destination** page, from the **Type of destination instance** drop-down menu, select **New instance**. Define all the relevant settings: 
     1. In the **Destination instance ID** field, provide an identifier for the Cloud SQL instance or use the auto-generated identifier. 

Don't include sensitive or personally identifiable information in the identifier. You don't need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files).

     2. In the **Password** field, provide an alphanumeric password for the destination Cloud SQL instance. This is the password for the `postgres` administrator account in the instance. 

You can either enter the password manually or click **Generate** to have Database Migration Service create one for you automatically.

     3. From the **Database version** drop-down menu, choose the database version for the destination instance. 

[Learn more](https://docs.cloud.google.com/database-migration/docs/postgres/cross-version-support) about cross-version migration support.

     4. Select the Cloud SQL for PostgreSQL edition for your destination instance. There are two options available: **Cloud SQL for PostgreSQL Enterprise edition** and **Cloud SQL for PostgreSQL Enterprise Plus edition**. 

Cloud SQL for PostgreSQL editions come with different sets of features, available machine types, and pricing. Make sure you consult the Cloud SQL documentation to choose the edition that is appropriate for your needs. For more information, see [Introduction to Cloud SQL for PostgreSQL editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro).

     5. The **Region** menu shows the same region you selected on the **Get started** page. 

If you are configuring your instance for [high availability](https://docs.cloud.google.com/sql/docs/postgres/high-availability), select **Multiple zones (Highly available)**. You can select both the primary and the secondary zone. The following conditions apply when the secondary zone is used during instance creation:

        * The zones default to **Any** for the primary zone and **Any (different from primary)** for the secondary zone.
        * If both the primary and secondary zones are specified, they must be different zones.
     6. In the **Connections** section, choose whether to add a public or a private IP address for your destination instance. You can configure your instance to have both types of IP addresses, but at least one type is required for the migration. Select one of the following: 
        * If you want to migrate by using VPC peering or a reverse SSH tunnel, select [**Private IP**](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#private_ip). 
          * To enable private IP connectivity, make sure you meet all the additional networking requirements. 

#### Expand this section for full private IP requirements.

            * Service Networking API is enabled. You can enable the [Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com) by using the Google Cloud console.
            * You have the [`servicenetworking.services.addPeering` IAM permission](https://docs.cloud.google.com/iam/docs/permissions-reference).
            * You have [configured private services access](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering#configure-access) for your project, for which you need to have the `compute.networkAdmin` IAM role.
            * There's at least one non-legacy VPC network in your project, or a /vpc/docs/shared-vpc network.
            * If you are using a [/vpc/docs/shared-vpc network](https://docs.cloud.google.com/vpc/docs/shared-vpc), then you also need to do the following: 
              * Enable the Service Networking API for the host project.
              * Add your user to the host project.
              * Give your user the [compute.networkAdmin](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering#network-admin-role) IAM role in the host project.

          * Select the associated VPC network to peer. If you plan to connect to the migration source by using VPC peering, then choose the VPC where the instance resides. 
          * If a managed service network was never configured for the selected VPC, you can choose to either select an IP range and click **Connect** or use an automatically selected IP range and click **Allocate & Connect**. 
        * If you want to migrate over the Internet by using an IP allowlist, select [**Public IP**](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods).   


Optionally, under **Public IP** click the **Authorized networks** field, and either authorize a network or a proxy to connect to the Cloud SQL instance. Networks are only authorized with the addresses that you provide. See [Configure public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) in the Cloud SQL documentation.

You configure the migration job connectivity in a later step. To learn more about available networking methods, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods). 

  2. Select the machine type for the Cloud SQL instance. Learn more about [PostgreSQL machine types](https://docs.cloud.google.com/sql/docs/postgres/create-instance#machine-types). **Note:** Machines available in the **Machine type** selection depend on the Cloud SQL edition you use. 
  3. **For Cloud SQL for PostgreSQL Enterprise Plus edition** : Select the **Enable data cache** checkbox if you want to use the data cache feature in your destination database. 

Data cache is an optional feature available for Cloud SQL for PostgreSQL Enterprise Plus edition instances that adds a high-speed local solid state drive to your destination database. This feature can introduce additional costs to your Cloud SQL. For more information on data cache, see [Data cache overview](https://docs.cloud.google.com/sql/docs/postgres/data-cache) in Cloud SQL documentation.

  4. Specify the storage type for the Cloud SQL instance. You can choose either a [solid-state drive (SSD) or a hard disk drive (HDD)](https://docs.cloud.google.com/sql/docs/postgres/choosing-ssd-hdd).
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

For more information about creating a CMEK, see [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek).

     2. Add any necessary flags to be applied to the database server. If possible, make sure that the database flags on the created destination Cloud SQL instance are the same as those on the source database. Learn more about supported database flags for [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/flags#list-flags). 
     3. Add any [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) that are specific to the Cloud SQL instance. 

Labels help organize your instances. For example, you can organize labels by cost center or environment. Labels are also included in your bill so you can see the distribution of costs across your labels.

  7. Click **Create destination and continue**. Database Migration Service is now creating your Cloud SQL destination instance. This process can take several minutes. **Key point:**
     * Database Migration Service creates a Cloud SQL instance for which you will be charged according to the configuration specified. If the migration job creation flow is exited before completion, then use the **Cancel** button to clean up the Cloud SQL instance. If the browser or tab is closed, **Save and exit** is clicked, or the screen is navigated away from, then the Cloud SQL instance isn't cleaned up and will need to be deleted manually from the Cloud SQL Instances page. 
     * After the destination instance is created, the Cloud SQL instance settings can no longer be edited in the Database Migration Service console. You can still access the instance directly in the Cloud SQL console to modify it. 



### Set up connectivity between the source and destination database instances

From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the newly created Cloud SQL instance will connect to the source database. Current network connectivity methods for migrating to a new instance include [ IP allowlist, reverse SSH tunnel, and VPC peering](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods).

If you want to use...| Then...  
---|---  
The IP allowlist network connectivity method, | You need to specify the outgoing IP address of your destination instance. If the Cloud SQL instance you created is a high availability instance, include the outgoing IP addresses for both the primary and the secondary instance.  
The reverse SSH tunnel network connectivity method, | You need to select the Compute Engine VM instance that will host the tunnel. After specifying the instance, Google will provide a script that performs the steps to set up the tunnel between the source and destination databases. You'll need to run the script in the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).  Run the commands from a machine that has connectivity to both the source database and to Google Cloud.  
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

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test. For information troubleshooting a failing migration job test, see [Diagnose issues for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues). 

  2. When the migration job test finishes, click **Create and start job** to create the migration job and start it immediately, or click **Create job** to create the migration job without immediately starting it. 

If the job isn't started at the time that it's created, then it can be started from the **Migration jobs** page by clicking **START**. Regardless of when the migration job starts, your organization is charged for the existence of the destination instance. 

Your migration is now in progress. When you start the migration job, Database Migration Service begins the initial full dump and replication. For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#parallelism-considerations).

**Caution:** If you used Terraform to provision your destination database, you might experience configuration drift during the migration job execution. Don't try to re-apply Terraform settings before the migration is complete. For more information, see [Terraform configuration drift](https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues#existing-instance-terraform-config-drift). 
  3. Proceed to [Review the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions). 



### Google Cloud CLI

  1. Create the destination connection profile.  
When you migrate to a new destination instance with Google Cloud CLI, you create the destination instance and the connection profile in a single action.  
Run the following command (click the link to expand):

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
    

  2. Create the migration job.   
If you use VPC peering or a reverse-SSH tunnel connectivity, make sure to add the required flags, such as `--peer-vpc`, or `--vm`, `--vm-ip`, `--vm-port`, `--vpc`. For more information, see [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods) and [Google Cloud CLI examples](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create#EXAMPLES).  
Run the following command (click the link to expand): 

#### `gcloud database-migration migration-jobs create`

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.
     * REGION with the region identifier where you want to save the migration job.
     * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
     * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile. For more information, see [Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles).
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
      --type=CONTINUOUS

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    create MIGRATION_JOB_ID `
      --no-async `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME `
      --source=SOURCE_CONNECTION_PROFILE_ID `
      --destination=DESTINATION_CONNECTION_PROFILE_ID `
      --type=CONTINUOUS

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    create MIGRATION_JOB_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME ^
      --source=SOURCE_CONNECTION_PROFILE_ID ^
      --destination=DESTINATION_CONNECTION_PROFILE_ID ^
      --type=CONTINUOUS

You should receive a response similar to the following:
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
