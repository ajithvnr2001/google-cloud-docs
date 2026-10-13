---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job/
title: Create a migration job to a new destination instance \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:31.955065+00:00
---

# Create a migration job to a new destination instance  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Create a migration job to a new destination instance Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


## Overview

Database Migration Service uses migration jobs to migrate data from your source database instance to the destination AlloyDB database instance. 

For private IP connectivity, when you migrate to an AlloyDB for PostgreSQL cluster created with Database Migration Service, you can only use the [private services access method](https://docs.cloud.google.com/alloydb/docs/private-ip#private-service-access). If you want to use Private Service Connect with your destination cluster, first [create the AlloyDB for PostgreSQL destination outside Database Migration Service](https://docs.cloud.google.com/alloydb/docs/cluster-create), and then follow the [Migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance) flow.

Creating a migration job includes:

  * Defining settings for the migration job
  * Specifying information about the connection profile that you created for your source database (source connection profile) 
  * Defining settings for the destination AlloyDB database instance and creating the instance
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

  6. Select **AlloyDB for PostgreSQL** as the destination engine. 

  7. Select the destination [region](https://docs.cloud.google.com/docs/geography-and-regions) for your migration. This is where the Database Migration Service instance is created, and should be selected based on the location of the services that need your data, such as Compute Engine instances and App Engine apps, and other services. After you choose the destination region, this selection can't be changed.

  8. Choose **Continuous** (snapshot + ongoing changes) as the migration job type. 

  9. Review the required prerequisites that are generated automatically to reflect how the environment must be prepared for a migration job. These prerequisites can include how to configure the source database and how to connect it to the destination AlloyDB database instance. It's best to complete these prerequisites at this step, but you can complete them at any time before you test the migration job or start it. For more information about these prerequisites, see [Configure your source.](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database)

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

### Define and create the destination AlloyDB instance

You will now create a new destination AlloyDB cluster for your migration job. Clusters are the top-level resources in AlloyDB. They contain a single primary instance for read/write access to the database you create during the migration process.

To create a destination cluster: 

  1. Choose a cluster type. Database Migration Service currently supports **Highly available** AlloyDB clusters. They can serve data from more than one zone in a region, with no read pools.
  2. Click **CONTINUE**.
  3. Configure your cluster: 
     1. In the **Cluster ID** field, enter an ID for your cluster.
     2. In the **Password** field, enter a password for the default `postgres` user. You will need the password to log in to your database.
     3. In the **Network** field: 
        1. Select a network path to define which resources are available when setting the migration connectivity. Clusters can only be configured with a private IP network path. If you plan to connect to the source database with VPC peering, select the VPC where it resides.
        2. If your network isn't configured for [ private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), click **Set up connection** and follow the connection configuration wizard.
        3. If a managed service network was never configured for the selected VPC, you can choose to either select an IP range and click **Connect** or use an automatically selected IP range and click **Allocate & Connect**. 
     4. Optional: In the **Encryption** section, specify whether you want to manage the encryption of the data that's migrated from the source to the destination. By default, your data is encrypted with a key that's managed by Google Cloud. 

If you want to manage your encryption, you can use a customer-managed encryption key (CMEK). The key must be in the same location as your AlloyDB cluster. For example, for clusters located in **us-west1** can use only keys in **us-west1**.

        1. Select the **Use a customer-managed encryption key (CMEK)** radio button.
        2. From the **Select a customer-managed key** menu, select your CMEK.

If you don't see your key, then click **ENTER KEY RESOURCE NAME** to provide the resource name of the key that you want to use. For example, you can enter `projects/my-project-name/locations/my-location/keyRings/my-keyring/cryptoKeys/my-key` in the **Key resource name** field, and then click **SAVE**. 

As part of creating the migration job, Database Migration Service will verify that the CMEK exists, and that Database Migration Service has permissions to use the key.

If Database Migration Service doesn't have these permissions, then information will appear, specifying that the Database Migration Service service account can't use the CMEK. Click **GRANT** to give Database Migration Service permissions to use the key. 

For more information about encryption keys, see [Use CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek) in AlloyDB documentation.

  4. Click **CONTINUE**.


* Configure your primary instance. A primary instance determines a cluster's compute capacity and supports read and write operations:

  1. In the **Instance ID** field, enter an ID for your primary instance.
  2. Select a machine type.
  3. If you plan to use the **IP allowlist** connectivity method, select the **Enable outbound public IP** checkbox.
  4. Optional: Set flags for your instance. You can use flags to customize your instance. For information on supported flags, see [AlloyDB documentation](https://docs.cloud.google.com/alloydb/docs/reference/database-flags). For each flag: 
     1. Click **ADD FLAG**.
     2. Select a flag from the **New database flag** list.
     3. Provide a value for the flag.
     4. Click **DONE**.


* Click **Save and continue**.
* Confirm your choice by clicking **CREATE DESTINATION & CONTINUE**.
* Wait for the creation of the destination instance to finish.
Your AlloyDB cluster will be in a "Bootstrapping" state while it's being managed by Database Migration Service. While in "Bootstrapping", you will not be able to perform any operations on your cluster. If you still wish to delete the cluster, you can do so using gcloud with the `--force` option.

### Set up connectivity between the source and destination database instances

If you're reusing a source connection profile that was used previously for heterogeneous migrations (for example, from Oracle to Cloud SQL PostgreSQL), then in this step, you must choose a connectivity method. This method will be used for the homogeneous migration from Cloud SQL for PostgreSQL database to AlloyDB. You must select a connectivity method because the heterogeneous connectivity method isn't relevant for this migration job.

  1. From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how the newly created AlloyDB instance will connect to the source database. Current network connectivity methods include [IP allowlist, VPC peering, reverse SSH tunnel, and TCP proxy through a cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods). 

  2. If you select the IP allowlist network connectivity method, you need to specify the outgoing IP address of your destination instance. Copy the outgoing IP addresses for both the primary and the secondary instance and use them to configure the network firewall for your source database server and in the `pg_hba.conf` file, so that the source can accept connections from these addresses. 
  3. If you select the reverse SSH tunnel network connectivity method, then select the Compute Engine VM instance that will host the tunnel.

After specifying the instance, Google will provide a script that performs the steps to set up the tunnel between the source and destination databases. You'll need to run the script in the [Google Cloud CLI](https://cloud.google.com/sdk/gcloud/?_ga=2.255980105.-371130741.1588278357).

Run the commands from a machine that has connectivity to both the source database and to Google Cloud.

  4. If you select the VPC peering network connectivity method, then select the VPC network where the source database resides. The Cloud SQL instance will be updated to connect to this network.
  5. If you select the TCP Proxy through the cloud-hosted VM connectivity method, then enter the required details for the new Compute Engine VM instance that will host the TCP proxy.

After specifying the details, the Google Cloud console will provide a script that performs the steps to set up the proxy between the source and destination databases. You'll need to run the script on a machine with an updated [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

After running the script, it will output the newly created VM's private IP. Enter the IP and click **Configure & continue**.

  6. Learn more about how to [Configure connectivity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity). Note: In case your source is Cloud SQL for PostgreSQL, depending on whether your Cloud SQL source instance is on the old network architecture or the new network architecture, the connectivity options are limited to **VPC Peering** and **TCP Proxy via a cloud-hosted VM**.
  7. After selecting the network connectivity method and providing any additional information for the method, click **CONFIGURE & CONTINUE**.




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
     * Any updates to private IP addresses needed on the destination are done. 
     * The migration job is valid, and the source and destination versions are compatible. 

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test.

For more information about reasons why the test may fail and how to troubleshoot any issues associated with the test failing, see [Diagnose issues for AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues). 

The migration job can be created even if the test fails, but after the job is started, it may fail at some point during the run.

  2. Click **CREATE & START JOB** to create the migration job and start it immediately, or click **CREATE JOB** to create the migration job without immediately starting it.

If the job isn't started at the time that it's created, then it can be started from the **Migration jobs** page by clicking **START**.

Regardless of when the migration job starts, your organization is charged for the existence of the destination instance.

**Key Point:** When you start the migration job, Database Migration Service begins the full dump, briefly locking the source database. If your source is in Amazon RDS or Amazon Aurora, Database Migration Service additionally requires a short (approximately under a minute) write downtime at the start of the migration. 

For more information, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#parallelism-considerations). 

  3. The migration job is added to the migration jobs list and can be viewed directly.




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


