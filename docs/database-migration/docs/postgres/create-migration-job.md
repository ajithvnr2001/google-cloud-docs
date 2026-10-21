---
url: https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job/
title: Create a migration job to a new destination instance \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:39.853637+00:00
---

# Create a migration job to a new destination instance  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest)



Send feedback 

#  Create a migration job to a new destination instance Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


## Overview

Database Migration Service uses migration jobs to migrate data from your source database instance to the destination Cloud SQL database instance. **Note:** For IP connectivity, when you migrate to a Cloud SQL instance created with Database Migration Service, you can only use the [private services access method (VPC peering)](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access). If you want to use Private Service Connect with your destination cluster, first [create the destination instance directly in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect), and then follow the steps on the [Migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) page.

Creating a migration job includes:

  * Defining settings for the migration job
  * Specifying information about the connection profile that you created for your source database (source connection profile) 
  * Defining settings for the destination Cloud SQL database instance and creating the instance
  * Setting up connectivity between the source and destination database instances 
  * Testing the migration job to ensure that the connection information you provided for the job is valid



Database Migration Service wizard helps you create a migration job. The wizard consists of multiple following panes where you provide the information about your source databases, destination databases, and connectivity methods. In the wizard, you can also test your migration job before you finish creating it. Information on how to populate each pane is provided in the various sections of this page.

### Define settings for the migration job

  1. Go to the [Migration jobs](https://console.cloud.google.com/dbmigration/migrations) page in the Google Cloud Console.
  2. Click **Create migration job** at the top of the page.
  3. Provide a name for the migration job.

Choose a friendly name that helps you identify the migration job. Don't include sensitive or personally identifiable information in the job name.

  4. Keep the auto-generated **Migration job ID**. 

  5. Select the source database engine.

  6. Select the destination database engine. 

  7. Select the destination [region](https://docs.cloud.google.com/docs/geography-and-regions) for your migration. This is where the Database Migration Service instance is created, and should be selected based on the location of the services that need your data, such as Compute Engine instances and App Engine apps, and other services. After you choose the destination region, this selection can't be changed.

**Important:** If you plan to use the Cloud SQL for PostgreSQL Enterprise Plus edition, make sure your region is supported for that edition. See [Cloud SQL for PostgreSQL Enterprise Plus edition region support](https://docs.cloud.google.com/sql/docs/postgres/editions-intro#editions-regions). 
  8. Specify the migration job type: **One-time** (snapshot only) or **Continuous** (snapshot + ongoing changes). 

  9. Review the required prerequisites that are generated automatically to reflect how the environment must be prepared for a migration job. These prerequisites can include how to configure the source database and how to connect it to the destination Cloud SQL database instance. It's best to complete these prerequisites at this step, but you can complete them at any time before you test the migration job or start it. For more information about these prerequisites, see [Configure your source.](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database)

  10. Click **Save and continue**.




### Specify information about the source connection profile

  1. If you have created a connection profile, then select it from the list of existing connection profiles.

If you haven't created a connection profile, then create one by clicking **Create a connection profile** at the bottom of the drop-down list, and then perform the same steps as in [Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-source-connection-profile).

  2. In the **Customize data dump configurations** section, click **Show data dump configurations**. 

The speed of data dump parallelism is related to the amount of load on your source database. You can use the following settings:

     * **Optimal (recommended)** : Balanced performance with optimal load on the source database.
     * **Maximum** : Provides the highest dump speeds, but might cause increased load on the source database.
     * **Minimum** : Takes the lowest amount of compute resources on the source database, but might have slower dump throughput.

If you want to use adjusted data dump parallelism settings, make sure to increase the `max_replication_slots`, `max_wal_senders`, and `max_worker_processes` parameters on your source database. You can verify your configuration by  running the migration job test at the end of migration job creation. 

  3. Click **Save and continue**.



### Define and create the destination Cloud SQL instance

**Note:** **For Cloud SQL sources:** If you are migrating from a Cloud SQL instance that uses a Private IP connection to a Cloud SQL instance that uses a [non-RFC 1918 address](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) IP range, add the non-RFC 1918 range to the network configuration of your source Cloud SQL instance. See [Configure authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) in Cloud SQL documentation.

  1. From the **Type of destination instance** drop-down menu, select **New instance**.

You can also migrate to an existing instance, see [ Migration job for an existing instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance).

  2. Provide an ID for the Cloud SQL instance or use the auto-generated ID. Don't include sensitive or personally identifiable information in the ID; it's externally visible. There's no need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files).
  3. Provide an alphanumeric password for the destination Cloud SQL instance. This will be the password for the `postgres` administrator account in the instance.

You can either enter the password manually or click **Generate** to have Database Migration Service create one for you automatically.

  4. Choose the database version for the destination instance from the list of supported Database Migration Service versions for the specified database engine. [Learn more](https://docs.cloud.google.com/database-migration/docs/postgres/cross-version-support) about cross-version migration support.
  5. Select the Cloud SQL for PostgreSQL edition for your destination instance. There are two options available: **Cloud SQL for PostgreSQL Enterprise edition** and **Cloud SQL for PostgreSQL Enterprise Plus edition**. 

Cloud SQL for PostgreSQL editions come with different sets of features, available machine types, and pricing. Make sure you consult the Cloud SQL documentation to choose the edition that is appropriate for your needs. For more information, see [Introduction to Cloud SQL for PostgreSQL editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro).

  6. The instance is created in the region that you selected when you defined settings for the migration job. Select a zone within that region or leave the zone set to **Any** for Google to select one automatically.

If you are configuring your instance for [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability), select **Multiple zones (Highly available)**. You can select both the primary and the secondary zone. The following conditions apply when the secondary zone is used during instance creation: 

     * The zones default to **Any** for the primary zone and **Any (different from primary)** for the secondary zone.
     * If both the primary and secondary zones are specified, they must be different zones.
  7. Choose whether to connect to this instance with private or public IP address.
     1. If you're planning to connect with VPC-peering or Reverse SSH tunnel, then select the **Private IP** checkbox.
        1. Make sure the following is true to enable private IP:
           * Service Networking API is enabled. You can enable the [Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com) using the Google Cloud console.
           * You have the [`servicenetworking.services.addPeering` IAM permission](https://docs.cloud.google.com/iam/docs/permissions-reference).
           * You have [configured private services access](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering#configure-access) for your project, for which you need to have the `compute.networkAdmin` IAM role.
           * There's at least one non-legacy VPC network in your project, or a shared VPC network.
             * If you are using a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc), then you also need to do the following: 
               * Enable the Service Networking API for the host project.
               * Add your user to the host project.
               * Give your user the [ compute.networkAdmin](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering#network-admin-role) IAM role in the host project. 
        2. Select the associated VPC network to peer. If you plan to connect to the migration source with VPC peering, then choose the VPC where the instance resides.
        3. If a managed service network was never configured for the selected VPC, you can choose to either select an IP range and click **Connect** or use an automatically selected IP range and click **Allocate & Connect**. 
     2. If you plan to connect with IP allowlisting, select **Public IP**.

Optionally, click **Authorized networks** , and either authorize a network or a proxy to connect to the Cloud SQL instance. Cloud SQL instances accept connections only from addresses that are authorized. For more information about configuring public access to the instance, see [Configure public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip).

  8. Select the machine type for the Cloud SQL instance. The disk size must be equal to or greater than the source database size. Note: Machines available in the **Machine type** selection depend on the Cloud SQL edition you use. 

Learn more about [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#cpus-postgres) machine types. 

  9. **For Cloud SQL for PostgreSQL Enterprise Plus edition** : Select the **Enable data cache** checkbox if you want to use the data cache feature in your destination database. 

Data cache is an optional feature available for Cloud SQL for PostgreSQL Enterprise Plus edition instances that adds a high-speed local solid state drive to your destination database. This feature can introduce additional costs to your Cloud SQL. For more information on data cache, see [Data cache overview](https://docs.cloud.google.com/sql/docs/postgres/data-cache) in Cloud SQL documentation.

  10. Specify the storage type for the Cloud SQL instance. You can choose either a [ solid-state drive (SSD) or a hard disk drive (HDD).](https://cloud.google.com/sql/docs/postgres/choosing-ssd-hdd)
  11. Specify the storage capacity (in GBytes) for the Cloud SQL instance. 

Important: Make sure the instance has enough storage capacity to handle the data from your source database. You can increase this capacity at any time, but you can't decrease it.

  12. Optionally, click **SHOW OPTIONAL CONFIGURATIONS** , and then: 
     1. Specify whether you want to manage the encryption of the data that's migrated from the source to the destination. By default, your data is encrypted with a key that's managed by Google Cloud. If you want to manage your encryption, then you can use a customer-managed encryption key (CMEK). To do so:

        1. Select the **Use a customer-managed encryption key (CMEK)** check box.
        2. From the **Select a customer-managed key** menu, select your CMEK.

If you don't see your key, then click **ENTER KEY RESOURCE NAME** to provide the resource name of the key that you want to use. For example, you can enter `projects/my-project-name/locations/my-location/keyRings/my-keyring/cryptoKeys/my-key` in the **Key resource name** field, and then click **SAVE**. 

As part of creating the migration job, Database Migration Service will verify that the CMEK exists, and that Database Migration Service has permissions to use the key.

If Database Migration Service doesn't have these permissions, then information will appear, specifying that the Database Migration Service service account can't use the CMEK. Click **GRANT** to give Database Migration Service permissions to use the key. 

For more information about creating a CMEK, see [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek).

     2. Add any necessary flags that will be applied to the database server. If possible, make sure that the database flags on the created destination Cloud SQL instance are the same as those on the source database. Learn more about supported database flags for [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/flags#list-flags-postgres). 
     3. Add any [labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels?_ga=2.250215364.-371130741.1588278357) that are specific to the Cloud SQL instance. 

Labels help organize your instances. For example, you can organize labels by cost center or environment. Labels are also included in your bill so you can see the distribution of costs across your labels.

     4. Click **CREATE & CONTINUE**.

[Creating read replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica) and [enabling high availability](https://docs.cloud.google.com/sql/docs/postgres/configure-ha) is available only after you [promote the migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).

  13. In the **Create destination database** window, click **CREATE DESTINATION & CONTINUE** to create the new instance. This may take up to several minutes. 

This will create a Cloud SQL instance for which you will be charged according to the configuration specified. If the migration job creation flow is exited before completion, then use the **CANCEL** button to clean up the Cloud SQL instance. If the browser or tab is closed, **Save and exit** is clicked, or the screen is navigated away from, then the Cloud SQL instance isn't cleaned up and will need to be deleted manually from the Cloud SQL Instances page.

After the destination instance is created, the Cloud SQL instance settings can no longer be edited in the Database Migration Service console. You can still access the instance directly in the Cloud SQL console to modify it.

  14. Wait for the creation of the destination instance to finish.



### Set up connectivity between the source and destination database instances

If you're reusing a source connection profile that was used previously for heterogeneous migrations (for example, from Oracle to Cloud SQL to PostgreSQL), then in this step, you must choose a connectivity method. This method will be used for the homogeneous migration from one Cloud SQL for PostgreSQL database instance to another. You must select a connectivity method because the heterogeneous connectivity method isn't relevant for this migration job.

  1. From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the newly created Cloud SQL instance will connect to the source database. Current network connectivity methods include [IP allowlist, reverse SSH tunnel, and VPC peering](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods). 

     * If you select the IP allowlist network connectivity method, you need to specify the outgoing IP address of your destination instance. If the Cloud SQL instance you created is a high availability instance, include the outgoing IP addresses for both the primary and the secondary instance. 
     * If you select the reverse SSH tunnel network connectivity method, then select the Compute Engine VM instance that will host the tunnel.

After specifying the instance, Google will provide a script that performs the steps to set up the tunnel between the source and destination databases. You'll need to run the script in the [Google Cloud CLI](https://cloud.google.com/sdk/gcloud/?_ga=2.255980105.-371130741.1588278357).

Run the commands from a machine that has connectivity to both the source database and to Google Cloud.

     * If you select the VPC peering network connectivity method, then select the VPC network where the source database resides. The Cloud SQL instance will be updated to connect to this network.
     * Learn more about how to [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity). 
  2. After selecting the network connectivity method and providing any additional information for the method, click **CONFIGURE & CONTINUE**.




### Configure migration databases

You can select the databases that you want to migrate.

  1. From the **Databases to migrate** list, select one of the following options: 
     * **All databases** : Selects all databases that exist on the source.
     * **Specific databases** : Allows you to select specific databases from all databases that exist on the source.
  2. If you want to migrate specific databases, you can filter the list that appears and select the databases that you want Database Migration Service to migrate into a destination.

If the list doesn't appear and a database discovery error is displayed, click **Reload**. If database discovery fails, the job migrates all databases. You can continue with creating a migration job and fix connectivity errors later.

  3. Click **Save and continue**.



### Test and create the migration job

On this final step, review the summary of the migration job settings, source, destination, and connectivity method, and then test the validity of the migration job setup. If any issues are encountered, then you can modify the migration job's settings. Not all settings are editable. 

  1. Click **TEST JOB** to verify that:

     * The source database has been configured correctly, based on the prerequisites. 
     * The source and destination instances can communicate with each other. 
     * Any updates to private or public IP addresses needed on the destination are done. 
     * The migration job is valid, and the source and destination versions are compatible. 

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test.

For more information about reasons why the test may fail and how to troubleshoot any issues associated with the test failing, see [Diagnose issues for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues). 

The migration job can be created even if the test fails, but after the job is started, it may fail at some point during the run.

  2. Click **CREATE & START JOB** to create the migration job and start it immediately, or click **CREATE JOB** to create the migration job without immediately starting it.

If the job isn't started at the time that it's created, then it can be started from the **Migration jobs** page by clicking **START**.

Regardless of when the migration job starts, your organization is charged for the existence of the destination instance.

**Key Point:** When you start the migration job, Database Migration Service begins the full dump, briefly locking the source database. If your source is in Amazon RDS or Amazon Aurora, Database Migration Service additionally requires a short (approximately under a minute) write downtime at the start of the migration. 

For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#parallelism-considerations). 

  3. The migration job is added to the migration jobs list and can be viewed directly.




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


