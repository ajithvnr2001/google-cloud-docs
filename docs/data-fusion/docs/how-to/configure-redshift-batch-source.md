---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-redshift-batch-source/
title: Redshift batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:45.510430+00:00
---

# Redshift batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-redshift-batch-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Redshift batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to load data from an Amazon Redshift instance into Google Cloud with Cloud Data Fusion. The Redshift source connector lets you sync tables from your Redshift dataset to your destination, such as BigQuery. The connector also lets you create a configurable SQL query.

## Before you begin

  * Cloud Data Fusion versions 6.9.0 and later support the Redshift source.
  * When you configure the Redshift source connector, you can select an existing, reusable connection, or create a new, one-time connection. For more information, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections). When you reuse a connection, note the following:

    * You don't have to provide credentials.
    * The existing connection provides the schema and table name information that's used to generate the import query.



## Configure the plugin

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate_the_web_interface) and click **Studio**.

  2. Check that **Data Pipeline - Batch** is selected (not **Realtime**).

  3. In the **Source** menu, click **Redshift**. The Redshift node appears in your pipeline. If you don't see the Redshift source on the **Studio** page, [deploy the Redshift source connector from the Cloud Data Fusion Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin).

  4. To configure the source, go to the Redshift node and click **Properties**.

  5. Enter the following properties. For a complete list, see Properties.

     1. Enter a label for the Redshift node—for example, `Redshift tables`.
     2. Enter the connection details. You can set up a new, one-time connection, or an existing, reusable connection.

### New connection

To add a one-time connection to Redshift, follow these steps:

        1. Keep **Use connection** turned off.
        2. In the **JDBC driver name** field, enter the name of the driver. Redshift supports two types of JDBC drivers: CData and [Amazon](https://docs.aws.amazon.com/redshift/latest/mgmt/configuring-connections.html). For more information, see [Upload a JDBC driver](https://docs.cloud.google.com/data-fusion/docs/how-to/using-jdbc-drivers).
        3. In the **Host** field, enter the endpoint of the Redshift cluster—for example, `cdf-redshift-new.example-endpoint.eu-west-1.redshift.amazonaws.com`.
        4. Optional: In the **Port** field, enter a database port number—for example, `5439`.
        5. If your Redshift database requires authentication, do the following:

           1. In the **Username** field, enter the name for the database.
           2. In the **Password** field, enter the password for the database.
           3. Optional: In the **Arguments** field, enter key value arguments. To use the CData driver, provide the connection arguments, such as RTK or OEMKey, if applicable.
           4. In the **Name** field, enter a name—for example, `SN-PC-Source-01-01-2024`.
           5. Enter the target database name in the **Database** field—for example, `datafusiondb`.

### Reusable connection

To reuse an existing connection, follow these steps:

        1. Turn on **Use connection**.
        2. Click **Browse connections**.
        3. Click the connection name.

**Note:** For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).
        4. Optional: If a connection doesn't exist and you want to create a new reusable connection, click **Add connection** and refer to the steps in the **New connection** tab on this page.

     3. In the **Import query** field, enter a query using the schema and table names from your Redshift source—for example, `Select * from "public"."users"`.

     4. Optional: Enter **Advanced** properties, such as a bounding query or number of splits. For all property descriptions, see Properties.

  6. Optional: Click **Validate** and address any errors found.

  7. Click close **Close**. Properties are saved and you can continue to build your data pipeline in the Cloud Data Fusion web interface.




## Properties

Property | Supports macros for automation | Required property | **Description**  
---|---|---|---  
**Label** | No | Yes | The name of the node in your data pipeline.  
**Use connection** | No | No | Browse for a connection to the source. If **Use connection** is turned on, you don't need to provide credentials.  
**Connection** | Yes | Yes | Name of the connection to use. If **Use connection** is selected, this field appears. Database and table information is provided by the connection.  
**JDBC driver name** | Yes | Yes | Name of the JDBC driver to use. If **Use connection** isn't selected, this field appears.  
**Host** | Yes | Yes | The endpoint of the Amazon Redshift cluster. If **Use connection** isn't selected, this field appears.  
**Port** | Yes | No | Port that Redshift is running on. If **Use connection** isn't selected, this field appears.  
**Username** | Yes | No | User identity for connecting to the specified database. If **Use connection** isn't selected, this field appears.  
**Password** | Yes | No | Password to use to connect to the specified database. If **Use connection** isn't selected, this field appears.  
**Connection arguments** | Yes | No | A list of arbitrary string key-value pairs as connection arguments. These arguments are passed to the JDBC driver as connection arguments for JDBC drivers that might need additional configurations. If **Use connection** isn't selected, this field appears.  
**Reference name** | No | Yes | Uniquely identifies this source for lineage, annotating metadata, and other services.  
**Database** | Yes | Yes | Redshift database name. To select data, click **Browse database**.  
**Import query** | Yes | Yes | The `SELECT` query to use to import data from the specified table.  
**Bounding query** | Yes | No | SQL query that returns the min and max values from the `splitBy` field. For example, `SELECT MIN(id),MAX(id) FROM table`. Not required if `numSplits` is set to one.  
**Split column** | Yes | No | Field name that's used to generate splits. Not required if `numSplits` is set to one.  
**Number of splits** | Yes | No | Number of splits to generate.  
**Size** | Yes | No | The number of rows to fetch at a time per split. Larger fetch size can result in faster import, with the tradeoff of higher memory usage. If unspecified, the default is `1000`.  
  
## Data type mappings

The following table is a list of Redshift data types with corresponding CDAP types:

Redshift data type | CDAP schema data type  
---|---  
`bigint` | `long`  
`boolean` | `boolean`  
`character` | `string`  
`character varying` | `string`  
`date` | `date`  
`double precision` | `double`  
`geometry` | `bytes`  
`hllsketch` | `string`  
`integer` | `int`  
`json` | `string`  
`numeric`(precision, scale)/`decimal`(precision, scale) | `decimal`  
`numeric` with precision 0 | `string`  
`real` | `float`  
`smallint` | `int`  
`super` | `string`  
`text` | `string`  
`time` [ (p) ] without time zone | `time`  
`time` [ (p) ] with time zone | `string`  
`timestamp` [ (p) ] without time zone | `timestamp`  
`timestamp` [ (p) ] with time zone | `timestamp`  
`varbyte` | `byte`  
`xml` | `string`  
  
## Best practices

The following best practices apply when you connect to a Redshift cluster from Google Cloud.

### Use IP address allowlists

To prevent access from unauthorized sources and restrict access to specific IP addresses, enable access controls on the Redshift cluster.

If you use Redshift access controls, to access the cluster in Cloud Data Fusion, follow these steps:

  1. Obtain the external IP addresses of the services or machines on Google Cloud that must connect to the Redshift cluster, such as the Proxy Server IP (see [Viewing IP addresses](https://docs.cloud.google.com/compute/docs/instances/view-network-properties#view_ip_addresses)). For Managed Service for Apache Spark clusters, obtain the IP addresses of all master and child nodes.
  2. Add the IP addresses to an allowlist in the security groups by creating the inbound rules for the Google Cloud machine IP addresses.

  3. Add the connection properties in Wrangler and test them:

     1. Open the Cloud Data Fusion instance in the web interface.
     2. Click **Wrangler > Add connection** and create the new connection for Redshift.
     3. Enter all connection properties.
     4. Click **Test connection** and resolve any issues.



### To create multiple splits, use bounding queries

For multiple splits, use bounding queries to manage the multi-node cluster. In scenarios where you extract data from Redshift and distribute the load uniformly across each node, configure a bounding query in the Redshift source connector properties.

  1. In your Cloud Data Fusion pipeline on the **Studio** page, go to the Redshift node and click **Properties**.
  2. In the **Advanced** properties, specify the following:

     1. Enter the number of splits to create.
     2. Enter the fetch size for each split.
     3. Enter a bounding query to apply to the multi-node Redshift cluster.
     4. Enter the **Split column** field name.



For example, assume you have the following use case:

  * You have a table that contains 10 million records.
  * It has a unique ID column called `id`.
  * The Redshift cluster has 4 nodes.
  * **Objective** : To take advantage of the cluster's potential, you plan to generate multiple splits. To achieve this, use the following property configurations:

    * In the **Bounding query** field, enter the following query:
          
          SELECT MIN(id), MAX(id) FROM tableName
          

In this query, `id` is the name of the column where the splits are applied.

    * In the **Split column** field, enter the column name, `id`.

    * Enter the number of splits and fetch size. These properties are interconnected, letting you calculate splits based on a fetch size, or the other way around. For this example, enter the following.

**Important:** A larger fetch size can lead to a faster import. The tradeoff is the increased memory usage.
    * In the **Number of splits** field, enter `40`. In this example, where the table has ten million records, creating 40 splits results in each split containing 250,000 records.

    * In the **Fetch size** field, enter `250,000`.


**Note:** A bounding query doesn't guarantee absolute uniformity. Some splits might contain more records, based on the values in the corresponding column.

## What's next

  * Look through the [Cloud Data Fusion plugins](https://docs.cloud.google.com/data-fusion/plugins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
