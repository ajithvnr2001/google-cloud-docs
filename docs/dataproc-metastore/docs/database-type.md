---
url: https://docs.cloud.google.com/dataproc-metastore/docs/database-type/
title: Database types \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:50:40.816581+00:00
---

# Database types  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/database-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Database types Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Dataproc Metastore service, you must choose to use either the MySQL database type or the Spanner database type.

This choice affects the features that you can integrate and use with your Dataproc Metastore service. It's important to note that you can't update your database type after you create a Dataproc Metastore service. Make sure you choose the appropriate database type for your needs.

This page explains the differences between these database types and how to select one for your service.

## Differences between MySQL and Spanner

### MySQL

The Dataproc Metastore MySQL database type is an implementation of [Cloud SQL](https://docs.cloud.google.com/sql). Note the following when using a MySQL database:

  * MySQL is the default database type when creating a Dataproc Metastore.
  * MySQL is supported by all Hive versions.
  * MySQL supports all Dataproc Metastore features.
  * MySQL supports Dataproc Metastore encryption, such as using customer-managed encryption keys (CMEK).



### Spanner

The Dataproc Metastore Spanner database type is an implementation of [Spanner](https://docs.cloud.google.com/spanner). Note the following when using a Spanner database:

  * Spanner is only supported on Hive versions 2.3.6 and 3.1.2.
  * Spanner only supports Avro imports.
  * The maximum supported number of columns in a table is 5,000.



### Additional details

The following table provides additional details about these differences.

| MySQL | Spanner  
---|---|---  
**Reliability (uptime)** | Cloud SQL SLO 99.95%* | Spanner SLO 99.99%*  
**Maintenance windows** | Required | Not Required  
  
Notes:

  * *The Cloud SQL and Spanner SLOs don't directly translate to Dataproc Metastore SLOs. Dataproc Metastore Your database type selection does not affect Dataproc Metastore SLOs.
  * There's no pricing difference between the two database types.



## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Understand networking requirements](https://docs.cloud.google.com/dataproc-metastore/docs/access-service) specific to your project.



### Required Roles

To get the permission that you need to create a Dataproc Metastore, ask your administrator to grant you the following IAM roles on your project, based on the principle of least privilege: 

  * [Grant full control of Dataproc Metastore resources ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)
  * [Grant full access to all Dataproc Metastore resources, including IAM policy administration ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `metastore.services.create` permission, which is required to create a Dataproc Metastore. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Manage Managed Service for Apache Spark access with IAM](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## Choose your database type

You choose your database type when you first create a Dataproc Metastore service.

The following example shows an abbreviated version of the steps that you follow to choose a database type. For complete step-by-step instructions, see [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).

**Caution:** You can't update your database type after you create a Dataproc Metastore service. Make sure you choose the appropriate database type for your requirements. To change your database type, you must delete and recreate your service.

### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. In the navigation bar, click **Create**.

The **Create service** page opens.

  3. For **Database type** , select either **MySQL** or **Spanner**.

MySQL is the default database type.

  4. Choose the [remaining configurations](https://docs.cloud.google.com/dataproc-metastore/docs/create-service#create-a-service) for your service, as needed.

  5. Click **Submit**.




### gcloud CLI

  1. Run the following [`gcloud metastore services create`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/create) command:
         
         gcloud metastore services create SERVICE_ID \
            --location=LOCATION \
            --database-type=DATABASE_TYPE; default="mysql"
         

Replace the following:

     * `SERVICE_ID`: the name or ID for your Dataproc Metastore service.
     * `LOCATION`: the region that your Dataproc Metastore service resides in.
     * `DATABASE_TYPE`: the database type that you want to set for your Dataproc Metastore service. Accepted values include `mysql` and `spanner`. The default value is `mysql`.



## What's next

  * [Create a service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Data storage for internal tables](https://docs.cloud.google.com/dataproc-metastore/docs/data-storage-internal-tables)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
