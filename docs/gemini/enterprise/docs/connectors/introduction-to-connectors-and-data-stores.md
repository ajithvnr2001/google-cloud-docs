---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores/
title: Introduction to connectors and data stores \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:29.460402+00:00
---

# Introduction to connectors and data stores  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Introduction to connectors and data stores Stay organized with collections  Save and categorize content based on your preferences. 

Connectors get data from Google and third-party data sources into Gemini Enterprise, storing it in dedicated data stores. This document provides an overview of these connectors. Centralizing your data in Gemini Enterprise enhances data accessibility, search functionality, and analytical capabilities.

![An overview image that shows how the connectors get data into Gemini Enterprise.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/connectors-overview.png)Connector overview

## Connector and data store concepts

###### Data stores  
  
---  
Each data source supports a set of entity types. For example, Jira Cloud has entities such as issues, attachments, comments, and worklogs, which are unique to the data source. Gemini Enterprise creates a separate data store for each entity. Therefore, when you create a data store using the Google Cloud console, you get a collection of data stores representing these ingested data entities.  
  
######  Data federation versus ingestion (indexing)   
  
Data federation directly retrieves information from the specified data source. Because data isn't copied into the Gemini Enterprise index, you don't need to worry about data storage. However, because the data is not indexed, search quality might be lower.  
  
Data ingestion (indexing) copies data into the Gemini Enterprise index. This can result in improved search quality. However, this process consumes more storage and time.  
  
If the connector supports both data federation and data ingestion, select your preferred data connection method.  
  
**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.  
  
###### Unstructured data  
  
The supported data format is specific to the data source and the entity type. If the content in an entity is stored in an unstructured format—such as PDF, HTML, DOCX, PPTX, XLSX, and XLSM—an unstructured data store is created by Gemini Enterprise. For more information and supported file types, see [Unstructured search](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/prepare-data#unstructured).   
  
###### Structured data  
  
The supported data format is specific to the data source and the entity type. If the content in an entity is stored in a structured format, a structured data store is created by Gemini Enterprise. For more information, see [Structured search](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/prepare-data#structured).   
  
###### Data schemas  
  
The data schema defines the data structure. When you import structured data using Gemini Enterprise, the system auto-detects the schema. You can use the auto-detected schema or define the schema using the API. For more information, see [Provide or auto-detect a schema](https://docs.cloud.google.com/gemini/enterprise/docs/provide-schema).   
  
###### Data store regions  
  
When ingesting data, you need to select the region where you want to store the data, such as global, the US, or the EU. For more information, see [ Data residency and ML regional processing commitments](https://docs.cloud.google.com/gemini/enterprise/docs/locations). Data stored in the US or EU regions require data encryption. The default encryption is with Google-owned and Google-managed encryption keys, but alternatively, you can use [customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek).   
  
###### Data syncs  
  
A data sync pulls and updates identity data (such as roles, permissions, and users) and entity data (such as data related to a specific data source) from the original data source. For more information, see Data sync types and schedules.  
  
## Data sync types and schedules

A data sync captures entity data, identity data, or both, and updates the contents of the data store in Gemini Enterprise.

### Sync types

Data stores in Gemini Enterprise use two essential types of data sync:

  * A _full sync_ captures the entire state of the third-party app or service. This includes additions, updates, and deletions. A full sync replaces the existing contents of the data store.

  * An _incremental sync_ periodically captures entity data that has been added or updated since the last sync. It does not sync identity data or deletions of entity data.




You can schedule a full sync separately for the following data types:

  * An _entity sync_ captures data specific to the third-party data source. For example, a data store for a system like Jira can sync issues, worklogs, comments, and attachments. Entity syncs don't include identity information.

  * An _identity sync_ captures data about user accounts associated with an ACL group.




#### Interaction between identity sync and full sync

To understand how an individual identity sync run works with a full sync run, consider an example scenario including two pages: `page_1`, linked to an ACL group `group_1`; and `page_2`, linked to an ACL group `group_2`.

  1. An initial identity sync runs, and retrieves information about groups `group_1` and `group_2`.

     * Assume that `group_1` contains user `user_1`.

     * Assume that `group_2` contains user `user_2`.

This identity sync establishes the following mapping:

     * `user_1` maps to `group_1`.

     * `user_2` maps to `group_2`.

  2. Alongside the identity sync, a full sync runs, fetching both `page_1` and `page_2`.

This full sync establishes the following mapping:

     * `user_1` has access to `page_1` (via `group_1`).

     * `user_2` has access to `page_2` (via `group_2`).




### Sync schedules

For each data store, you can select a frequency for different sync types:

  * Full syncs of all identity data and entity data can be scheduled simultaneously for every 3 hours, 6 hours, 12 hours, 1 day, or 3 days.

  * Independent full syncs of all identity data, and independent full syncs of all entity data, can be scheduled separately using any of the following custom sync frequencies:

    * Entity data: Every 3 hours, 6 hours, 12 hours, 1 day, 3 days, 5 days, and every 7 days.

    * Identity data: Every 30 minutes, 1 hour, 3 hours, 6 hours, 12 hours, 1 day, 3 days, 5 days, and every 7 days.

  * Incremental syncs of updated or added entity data can be scheduled for every 3 hours, 6 hours, 12 hours, 1 day, 3 days, 5 days, or every 7 days. By default, an incremental sync is performed every 3 hours.

**Note:** Incremental syncs must be scheduled to occur more frequently than full sync. For example, if you have scheduled full syncs for every 12 hours, you can only schedule incremental syncs for every 3 hours or every 6 hours.

If you schedule incremental sync and full sync for the same frequency, incremental sync will be automatically paused and require manual intervention to resume.




#### Frequency recommendations

Choose a data sync frequency that aligns with the volume of records fetched and the recommended queries per second (QPS).

The following table shows the typical number of records retrieved for one, three, five, and seven-day syncs. The actual number of records may vary depending on the data source and its configuration.

QPS | Record volume for 1-day sync  | Record volume for 3-day sync  | Record volume for 5-day sync  | Record volume for 7-day sync   
---|---|---|---|---  
5  | 432k  | 1.296M  | 2.16M  | 3M   
10  | 864k  | 2.592M  | 4.32M  | 6M   
20  | 1.7M  | 5.1M  | 8.5M  | 11.9M   
50  | 4.3M  | 12.9M  | 21.5M  | 30.1M   
100  | 8.6M  | 25.8M  | 43M  | 60.2M   
  
### Pausing and resuming syncs

You can pause, and resume, both full syncs and incremental syncs:

  * When you pause a sync type, the data store cancels ongoing syncs of that type and stops scheduling new syncs of that type.

  * When you resume a sync type, the data store schedules the new sync based on the last scheduled sync time, but does not continue the previously interrupted sync.




For example, if you pause full sync while a full sync is occurring, the data store cancels that sync. If you later resume full sync, the data store automatically schedules a new full sync according to the full sync schedule.

## Google data sources

You can connect to Google data sources, such as BigQuery, Spanner, and Google Drive.

### Checklist for Google data sources

Before sending data to Gemini Enterprise, go through the following checklist:

  * Set up access control for your data source. For more information see, [Identity and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/identity).

  * Decide whether data should be federated or ingested (indexed).

  * Decide how often the data should be synced.

  * If you are using customer-managed encryption keys (CMEK), create multi-region keys. For more information, see [Register single-region keys for third-party data sources](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).

  * If you have personally identifiable information (PII) and intend to use autocomplete for query suggestions, see [protect against PII leaks](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#pii).




### Supported Google data sources

**Note:** For more information on the Google data sources, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store).**Google Drive** | **Gmail** | **Google Calendar** | **People search**  
---|---|---|---  
[![The icon for Google Drive.](https://www.gstatic.com/images/branding/productlogos/drive_round_2020q4/v6/192px.svg)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive) |  [![The icon for Gmail.](https://www.gstatic.com/images/branding/productlogos/gmail_round_2020q4/v7/192px.svg)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail) |  [![The icon for Google Calendar.](https://www.gstatic.com/images/branding/productlogos/calendar_round_2020q4/v9/192px.svg)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal) |  [![The icon for People search.](https://www.gstatic.com/images/branding/productlogos/groups_round/v1/192px.svg)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people)  
  
## Third party data sources

Third-party data stores ingest third-party application data into Gemini Enterprise.

### Checklist for third-party data sources

Before connecting a third-party data source to Gemini Enterprise, go through the following checklist:

  * Specific scopes and permissions must be configured for certain data sources. An administrator of the third-party application must review the required credentials to connect a data source and set up authentication and permissions. For information about the specific scopes and permissions, see the respective third-party data source documentation.

  * Set up access control for your data store. For more information, see [Identity and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/identity)

  * Decide whether data should be federated or ingested (indexed).

  * If data is ingested, make sure that resources aren't restricted for the user credential that you use to ingest data into the data source.

  * Decide how often the data should be synced.

  * If you are using customer-managed encryption keys (CMEK), create multi-region and single-region keys. For more information, see [Register single-region keys for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).

  * If you have personally identifiable information (PII) and intend to use autocomplete for query suggestions, see [protect against PII leaks](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#pii).

  * If you want outbound traffic from the data store to originate from a fixed set of IP addresses (for example, to allowlist them on the source system), and if the data store supports it, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress).




### Supported third-party data sources

**Note:** For the complete list of supported third-party data sources, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).**Microsoft Entra ID** | **Microsoft OneDrive** | **Microsoft Outlook** | **Microsoft SharePoint**  
---|---|---|---  
[![The icon for Microsoft Entra ID.](https://www.gstatic.com/vertexaisearch/icons/64px/azure_ad_light.png)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id) |  [![The icon for OneDrive.](https://gstatic.com/vertexaisearch/icons/64px/one_drive_light.png)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive) |  [![The icon for Microsoft Outlook.](https://gstatic.com/vertexaisearch/icons/64px/outlook_light.png)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook) |  [![The icon for SharePoint.](https://gstatic.com/vertexaisearch/icons/64px/sharepoint.png)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint)  
**Jira Cloud** | **Confluence Cloud** | **ServiceNow** |   
[![The icon for Jira Cloud.](https://gstatic.com/vertexaisearch/icons/64px/jira.png)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud) |  [![The icon for Confluence Cloud.](https://gstatic.com/vertexaisearch/icons/64px/confluence_light.png)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud) |  [![The icon for ServiceNow.](https://gstatic.com/vertexaisearch/icons/64px/service_now_light.png)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
