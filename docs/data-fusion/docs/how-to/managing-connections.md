---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections/
title: Create and manage connections \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:11.321276+00:00
---

# Create and manage connections  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Create and manage connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage connections in Cloud Data Fusion version 6.5 and later.

A connection stores information, such as user credentials and host information, which is needed to connect to data sources. When you use a connection in a plugin, the plugin inherits all of the properties configured in the connection. After you create the connection, you can reuse it for other pipelines in the namespace. When you export a pipeline that has a plugin that uses a connection, the pipeline configuration JSON includes all of the properties.

You can manage connections for each namespace on the following pages in the Cloud Data Fusion Studio:

  * The **Namespace Admin** page lets you add, edit, delete, duplicate, export, and import connections for each namespace.

  * The **Wrangler** workspace page lets you add, edit, delete, duplicate, and export connections for each namespace.

  * The **Studio** page lets you add and import connections for supported plugins for each namespace.


**Note:** Role-based access control (RBAC) is supported for connections. For more information, see the [Role-based access control (RBAC) overview](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac).

## Before you begin

  * Before you add a connection for a database source, you must upload the JDBC driver to Cloud Data Fusion. You can upload the driver from the Hub or the **Namespace Admin** page.



### Supported plugins

The following plugins support reusable connections:

  * Amazon S3
  * BigQuery
  * Spanner
  * Cloud Storage
  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL
  * Database
  * Kafka
  * Microsoft SQL Server
  * MySQL
  * Oracle
  * PostgreSQL
  * Salesforce
  * SAP Ariba
  * SAP BW Open Hub Batch Source
  * SAP ODP
  * SAP Table
  * Zendesk



## Create a connection

To create a new connection, follow these steps:

  1. In the Cloud Data Fusion Studio, click menu **Menu** > **Namespace Admin** > **Connections**.
  2. Click **Add connection**.
  3. From the **Add connection** page, select the type of connection to create.
  4. Configure the connection properties.

**Note:** Connection names must be unique in a namespace and can only include letters, numbers, underscores, and hyphens.
  5. Optional: to make sure the connection works, click **Test connection**.

  6. Click **Create**.




The connection appears in the **Connection type** field and is available for all users in the namespace. The connection is available for use on the **Wrangler** workspace page and on the **Studio** page in the Wrangler plugin properties.

**Note:** You can create a connection from the **Studio** , **Wrangler** , or **Namespace Admin** pages in the Cloud Data Fusion Studio.

## Use a connection in a plugin

When you use a connection in a plugin, the plugin inherits the connection properties that you configured in the previous step.

To use a connection in one of the supported plugins, follow these steps:

  1. In the Cloud Data Fusion Studio interface, open a pipeline on the **Studio** page.
  2. In the plugin pallet, expand the menu **Source** menu, and select a supported batch source plugin.
  3. Hold the pointer over the source node that appears and click **Properties**.
  4. Set **Use connection** to **Yes**.
  5. Click **Browse connections**. You can select an existing connection or create a new one. After you select the connection, all properties associated with the connection no longer appear. The connection properties are stored in the connection.
  6. Configure the rest of the required plugin properties.
  7. Optional: to test the connection, click **Validate**.
  8. Click close **Close**.

**Note:** You can edit, delete, duplicate, import, or export each connection.

## What's next

  * Learn more about using [macros in plugins](https://docs.cloud.google.com/data-fusion/docs/concepts/macros).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
