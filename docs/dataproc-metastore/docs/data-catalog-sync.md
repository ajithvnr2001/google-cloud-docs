---
url: https://docs.cloud.google.com/dataproc-metastore/docs/data-catalog-sync/
title: Sync Dataproc Metastore to Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:42.596155+00:00
---

# Sync Dataproc Metastore to Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/data-catalog-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Sync Dataproc Metastore to Data Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Data Catalog is [deprecated](https://docs.cloud.google.com/data-catalog/docs/deprecations) in favor of [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview). Knowledge Catalog is also integrated with Dataproc Metastore, offering similar capabilities. You can use Knowledge Catalog to enrich your data with aspects, which are the equivalent of Data Catalog tags. For more information, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata). 

This document shows you how to sync Dataproc Metastore metadata with Data Catalog.

After you sync these two services together, you can use Data Catalog to manage your Dataproc Metastore metadata. For example, by using Data Catalog, you can tag and search for specific Dataproc Metastore resources, such as databases and tables.

## What is Data Catalog

Data Catalog is a fully managed, scalable metadata management service. It provides a unified view and tagging mechanisms for technical and business metadata.

For more information, see the following Data Catalog feature guides:

  * [How to search with Data Catalog](https://docs.cloud.google.com/data-catalog/docs/how-to/search).
  * [Tags and tag templates](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates).



## Before you begin

  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).
  * [Import metadata into Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata).



### Required roles

To get the permissions that you need to sync Dataproc Metastore metadata with Data Catalog, ask your administrator to grant you the [View synced Dataproc Metastore entries in Data Catalog ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataViewer) (`roles/metastore.metadataViewer`) IAM role on your project, based on the principle of least privilege. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to sync Dataproc Metastore metadata with Data Catalog. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to sync Dataproc Metastore metadata with Data Catalog:

  * To get Dataproc Metastore databases: `metastore.databases.get`
  * To list Dataproc Metastore databases: `metastore.databases.list`
  * To get Dataproc Metastore tables: `metastore.tables.get`
  * To list Dataproc Metastore tables: `metastore.tables.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Manage access with IAM](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

### How permissions work between the services

Data Catalog abides by Dataproc Metastore level permissions. For metadata that is synced from Dataproc Metastore to Data Catalog, IAM permissions specified in Dataproc Metastore apply to the metadata in Data Catalog as well.

Data Catalog checks the permissions for each metastore database and table at the time of access so that only users with access to the Dataproc Metastore service are able to see the synced service resources as entries in Data Catalog.

## How Data Catalog sync works with Dataproc Metastore

You can enable Dataproc Metastore to Data Catalog sync when you create or update a Dataproc Metastore service using the Google Cloud console. You can disable the sync in the same way.

After enabling Data Catalog sync, database and table metadata are automatically synced from Dataproc Metastore to Data Catalog.

**Note:** It can take up to 6 hours before the metadata in Dataproc Metastore is fully ingested to Data Catalog.

Data Catalog syncs the following metadata:

  * Instances.
  * Databases, including name and description.
  * Tables, including name, description, and schema (columns with descriptions).



The following table shows the resource mapping between Dataproc Metastore and Data Catalog:

Dataproc Metastore Resource | Data Catalog Resource  
---|---  
Instance | Entry group  
Entry  
Database | Entry  
Table | Entry  
Column | Schema  
  
### Considerations

  * It can take up to 6 hours before your Dataproc Metastore metadata is fully synced with Data Catalog. After the initial sync is done, incremental changes are synced on demand (such as table or database updates). If an on-demand sync fails, the sync is included in a batch rerun that occurs every 6 hours.

  * If you suspect that there is a problem with the sync, check the metadata publishing logs in Dataproc Metastore Cloud Logging with the filter `textPayload=~".*Publish.*"`. For more information on accessing logs, see [Access job logs in Logging](https://docs.cloud.google.com/dataproc-metastore/docs/logging#access-job-logs-in-logging).

  * If you disable Data Catalog sync, your metadata stops syncing from Dataproc Metastore to Data Catalog. However, metadata that was already synced remains in Data Catalog.

  * If you delete a Dataproc Metastore instance, then the corresponding instance, database, and table entries are also removed from Data Catalog.

  * Dataproc Metastore metadata stored in Data Catalog adheres to standard Google Cloud retention periods.

  * There are no additional costs to enabling Data Catalog sync for Dataproc Metastore.




## Create a service with Data Catalog sync enabled

Data Catalog sync is disabled by default.

To enable Data Catalog sync for a new service, use the following instructions.

### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Go to Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. At the top of the **Dataproc Metastore** page, click **Create**.

The **Create service** page opens.

  3. Select the version of Dataproc Metastore that you want to use.

  4. Under **Metadata integration** , click **Data Catalog sync**.

  5. For the remaining service configuration options, use the provided defaults. Or [Configure your service as needed](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).

  6. Click **Submit**.




## Enable or disable Data Catalog sync for an existing service

To enable or disable Data Catalog sync for an existing service, use the following instructions.

### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Go to Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the service you want to update.

The **Service detail** page for that service opens.

  3. Under the **Configuration** tab, click **Edit**.

The **Edit service** page opens.

  4. Under **Metadata integration** , toggle **Data Catalog sync** on or off.

  5. Click **Submit**.




## Search with Data Catalog

You can search synced Dataproc Metastore metadata using Data Catalog.

Although there are no custom search options for Dataproc Metastore, there are multiple ways to search for different Dataproc Metastore resources, including the following:

  * **Dataproc Metastore instance**
    * By display name
    * Standard Data Catalog functions — for example, by using tags.
  * **Database**
    * By display name
    * By description
    * By Dataproc Metastore instance
    * Standard Data Catalog functions — for example, by using tags.
  * **Table**
    * By display name
    * By description
    * By column name
    * By column description
    * By database
    * By Dataproc Metastore instance
    * Standard Data Catalog functions — for example, by using tags.



## What's next

  * [Data Catalog overview](https://docs.cloud.google.com/data-catalog/docs/concepts/overview)
  * [Create a service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
