---
url: https://docs.cloud.google.com/datastream/docs/create-alloydb-stream-automated/
title: Create an AlloyDB stream using the automated flow \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:54.193982+00:00
---

# Create an AlloyDB stream using the automated flow  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/create-alloydb-stream-automated/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Create an AlloyDB stream using the automated flow Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an AlloyDB for PostgreSQL stream using the automated setup flow.

**Note:** To use the automated stream setup flow when replicating from an AlloyDB for PostgreSQL cluster, your primary instance must be [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) enabled and must use the [Private Service Connect interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces) connectivity type.

The automated stream setup simplifies the process of moving data from AlloyDB for PostgreSQL clusters to BigQuery by reducing the number of steps that you need to perform. The flow lets you create a stream directly from the overview page of your AlloyDB for PostgreSQL cluster.

An AlloyDB for PostgreSQL deployment consists of a primary cluster, which contains a primary instance. It can also include secondary clusters and secondary instances. Datastream always creates the stream from the primary instance in the primary cluster.

Datastream automates securing the VPC connection between the stream and the source cluster, creating database configurations and stream connection resources.

## Free Tier

Datastream lets you stream from AlloyDB for PostgreSQL to BigQuery using the Free Tier, providing up to 100 GiB of change data capture data free every month. For more information, see [Datastream pricing](https://cloud.google.com/datastream/pricing).

## Before you begin

  1. Enable the Datastream, Network Connectivity, and Compute Engine APIs.
  2. Ensure that you have the required Identity and Access Management (IAM) permissions to create and manage Datastream resources. See the section that follows for more details.
  3. Create and configure a source AlloyDB for PostgreSQL cluster for replication. For more information, see [Configure a AlloyDB for PostgreSQL database for CDC](https://docs.cloud.google.com/datastream/docs/configure-alloydb-psql).
  4. We recommend that you enable logical replication for your cluster prior to creating the stream. If you don't enable logical replication, Datastream enables it for you, which restarts your source instance.

For information about enabling logical replication for an AlloyDB for PostgreSQL cluster, see [Configure an AlloyDB for PostgreSQL database for CDC](https://docs.cloud.google.com/datastream/docs/configure-alloydb-psql).

  5. Make sure that your source cluster is configured to use [private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).




## Required permissions

To use the automated stream creation flow, you need the following Identity and Access Management (IAM) roles or permissions:

  * `serviceusage.services.enable`, `compute.networkAdmin` for enabling the required APIs and performing network configuration tasks.
  * `alloydb.admin` for cluster and instance configuration tasks.
  * `datastream.admin` for administration tasks that Datastream performs on your behalf.



Make sure that all schemas and tables in the selected database are granted to either the `postgres` or `alloydbsuperuser` role. Because the automated flow includes all schemas and tables in the database by default, stream creation fails if the automatically created user lacks permissions on any schema or table.

If you choose to customize the stream settings, your database administrator user also needs `GRANT` permissions for the schema that you want to replicate and some additional permissions for administrative and structural tasks within the source database. Connect to your source database and run the following:
    
    
      GRANT alloydbsuperuser TO "USER_NAME";
      ALTER ROLE "USER_NAME" CREATEROLE;
      GRANT SELECT on ALL TABLES IN SCHEMA "SCHEMA_NAME" to "USER_NAME" WITH GRANT OPTION;
      ALTER DEFAULT PRIVILEGES
      IN SCHEMA "SCHEMA_NAME"
      GRANT SELECT ON TABLES TO "USER_NAME" WITH GRANT OPTION;
      GRANT CREATE ON DATABASE "DATABASE_NAME" TO "USER_NAME";
      

**Note:** The `alloydbsuperuser` role is required for Datastream to create the publication for all tables in your database instance.

### Future tables

Future tables are automatically added to the stream only if they're created by the user whose account details you provide to authenticate during the automated flow. If a future table is created by a different user, then that user must explicitly grant the Datastream reader user `SELECT` permission on the table.

## Create and start the stream

To create and start a stream, perform the following steps:

### Console

  1. Go to your source AlloyDB for PostgreSQL clusters overview page.

[Go to AlloyDB for PostgreSQL](https://console.cloud.google.com/alloydb)

  2. Click the primary cluster from which you want to stream data.

  3. Create and start your stream automatically, in one of the following ways:

     * In the **Cluster details** page, under **Data replication** , click **Start stream**.
     * In the **Integrations** section, click **Start stream** under **Replicate data to BigQuery**.
     * On the **Launchpad** tab, under **Seamlessly integrate with other Google Cloud products** , click **Replicate data to BigQuery**.
  4. The **Start stream to replicate data** pane opens.

  5. Under **Stream settings** , review the default settings for the stream that you create.

**Note:** If the `alloydb.logical_decoding` flag isn't enabled, you see a corresponding notification at the top of the pane.
  6. You can change the source database by expanding the corresponding drop-down and selecting a different value.

  7. If you're ready to create and start your stream, click **Start stream**.

**Note:** If you don't need to customize the settings, Datastream uses the credentials of the logged-in user for all database configurations. You don't need to provide any further IAM or built-in database authentication details. When using this flow, Datastream creates a database user with the `alloydbsuperuser` and `postgres` roles. Make sure that you granted access permissions to all schemas and tables in the selected database to either the `postgres` or `alloydbsuperuser` role.



If you need to change the stream settings, click **Customize**.

### Customize stream settings

When you click **Customize** , the **Customize stream settings** page appears. Make sure that you have the required permissions to customize the stream settings.

#### Get started

  1. On the **Get started** page, provide the name for your stream in the **Stream name** field. The **Stream ID** field gets populated automatically.
  2. In the **Provide the instance user account details** section, select the authentication method:

     * **IAM database authentication** : this option is available if your user has the Identity and Access Management (IAM) principal identity assigned. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview). If you select this option, you must manually grant the `alloydbsuperuser` role and the `CREATEROLE` permission to your user:

       1. In Google Cloud console, go to the **AlloyDB for PostgreSQL Clusters** page.

[Go to AlloyDB for PostgreSQL](https://console.cloud.google.com/alloydb)

       1. Select your AlloyDB for PostgreSQL cluster.
       2. In the navigation menu, click **AlloyDB for PostgreSQL Studio** and sign in.
       3. In the **Explorer** pane, run the following query for your user:
    
    GRANT alloydbsuperuser TO "USER_NAME";
    ALTER ROLE "USER_NAME" CREATEROLE;

     * **Built-in database authentication** : provide the username and the password of a user with the `alloydbsuperuser` role. If your user doesn't have the `alloydbsuperuser` role, follow the steps described in the IAM database authentication section to grant it manually. If you select built-in database authentication, also make sure that the user has `GRANT` permissions on the tables that they want to replicate.
  3. Review additional stream details, such as region, encryption and labels. Expand the **Additional stream details** section to apply changes, if required.

  4. Click **Continue**.




#### Configure source

  1. On the **Configure source** page, select the database from which you want to replicate data.

**Note:** Datastream displays only the databases for which your user has the required permissions. If you can't see a database that you want to use, it might mean that your user is missing permissions. Also, Datastream doesn't display system tables, because it doesn't support replication from system tables.
  2. The **Selected objects** list selects all available objects by default. The objects on the list are the objects for which you have the necessary permissions to stream. To change the selected objects, modify the selections in the list.

  3. Review advanced stream configurations, such as backfill mode and the maximum number of concurrent backfill connections. Expand the **Advanced stream configurations** section to apply changes, if required.

  4. Click **Continue**.




#### Configure destination

  1. On the **Configure destination** page, adjust the BigQuery destination settings, if required. For more information, see [Configure information about the destination for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuredestinfo).



#### Create and start the stream

  1. Click **Create and start** to create and start your stream, or **Create without starting** to create your stream and start it later in Datastream.

**Important:** Clicking **Create and start** restarts your AlloyDB for PostgreSQL instance. If you don't have the logical decoding enabled for your instance, Datastream enables it for you.
  2. You're notified about the tasks that are automatically performed for you:

     * Datastream creates the required Virtual Private Cloud resources, such as an internal IP address range, subnetwork and network attachment.
     * Datastream configures tables for CDC, sets up replication slots, sets up a publication for all tables in the database, and creates a dedicated Datastream user.
     * Datastream creates a private connectivity configuration and source and destination connection profiles.
  3. Confirm that you want to create and start your stream.




## Monitor the stream

You can monitor basic stream details from your source instance overview page in the Google Cloud console. The page displays information such as stream status, stream name, destination BigQuery dataset, and destination project identifier.

From the overview page, you can also perform actions such as starting or pausing the stream. For more granular monitoring information, click the stream name to navigate to Datastream.

## Delete the stream

When you delete a stream that you created using the automated flow, some resources, such as the PostgreSQL replication slot are deleted automatically. However, there are resources that you need to manually delete:

  * The publication. The publication is created using the database administrator user, and can be deleted only by its owner, so by default, the user who created it.
  * The Datastream reader user.
  * The Datastream source and destination connection profiles
  * The private connectivity resources.
  * All the network resources created during the automated flow, such as the subnetwork and the network attachment.



## What's next

  * Learn how to [create a stream manually](https://docs.cloud.google.com/datastream/docs/create-a-stream).
  * Learn how to configure an [AlloyDB for PostgreSQL source](https://docs.cloud.google.com/datastream/docs/configure-alloydb-psql).
  * Learn more about how to [monitor streams](https://docs.cloud.google.com/datastream/docs/monitor-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
