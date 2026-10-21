---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source/
title: Salesforce batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:27.076094+00:00
---

# Salesforce batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Salesforce batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to load data from [Salesforce sObjects](https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_sobjects) into Google Cloud with Cloud Data Fusion. The Salesforce batch source plugin reads sObjects from Salesforce. The sObjects are the Salesforce tables that you plan to pull from. Some examples of sObjects include opportunities, contacts, accounts, leads, and custom objects.

The Salesforce batch source plugin supports reading data with [Salesforce Object Query Language (SOQL)](https://docs.cloud.google.com/data-fusion/docs/use-case/salesforce-soql-queries) queries and incremental or range date filters.

## Before you begin

  * The Cloud Data Fusion Salesforce batch source uses the Salesforce Bulk API V1.
  * Set up Salesforce before deploying and using Cloud Data Fusion Salesforce plugin. For more information, see [Create a Salesforce connected app for Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/create-salesforce-app-for-plugin).



## Configure the plugin

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and click **Studio**.
  2. Check that **Data Pipeline - Batch** is selected (not **Realtime**).
  3. In the **Source** menu, click **Salesforce**. The Salesforce node appears in your pipeline. If you don't see the Salesforce source on the **Studio** page, [deploy the Salesforce plugins from the Cloud Data Fusion Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin).
  4. To configure the source, go to the Salesforce node and click **Properties**.
  5. Enter the following properties. For a complete list, see Properties.

     1. Enter a **Label** for the Salesforce node—for example, `Salesforce tables`.
     2. Enter a **Reference name** for the Salesforce source for lineage—for example, `Salesforce tables`.
     3. Enter the connection details. You can set up a new, one-time connection, or an existing, reusable connection.

### New connection

To add a one-time connection to Salesforce, follow these steps:

        1. Keep **Use connection** turned off.
        2. In the **Connection** section, enter the following information from the Salesforce account in these fields:

           * **Username**
           * **Password**
           * **Security token**
           * **Consumer key**
           * **Consumer secret**

To get the credentials from Salesforce, see [Get properties from Salesforce](https://docs.cloud.google.com/data-fusion/docs/how-to/create-salesforce-app-for-plugin#get-salesforce-information).

### Reusable connection

To reuse an existing connection, follow these steps:

        1. Turn on **Use connection**.
        2. Click **Browse connections**.
        3. Click the connection name.

**Note:** For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).
        4. Optional: If a connection doesn't exist and you want to create a new reusable connection, click **Add connection** and refer to the steps in the **New connection** tab.

     4. Enter the **SObject name** to load all the columns from the object.

     5. Optional: If you select the sObject name, you can filter the data with the following fields:

        * **Last modified after** : Only include records that were last modified after a given time.
        * **Last modified before** : Only include records that were last modified earlier than a given time.
        * **Duration** : Only include records that were last modified within a time window of the specified size.
        * **Offset** : Only include records where the Last modified date is less than the logical start time of the pipeline, minus the given offset.
     6. Optional: For supported sObjects, to improve the performance of a pipeline, turn on **Enable PK chunking**. For more information, see [Improve performance with PK chunking](https://docs.cloud.google.com/data-fusion/docs/concepts/best-practice-salesforce#pk-chunking).

     7. Optional: Instead of specifying the sObject Name, you can enter a SOQL query, such as `SELECT LastName from Contact`. For more information, see [SOQL queries for the Salesforce source](https://docs.cloud.google.com/data-fusion/docs/use-case/salesforce-soql-queries).

     8. To test connectivity, click **Get schema**. Cloud Data Fusion connects to Salesforce and pulls the schema for the listed table (technically, an sObject).




### Properties

Property | Macro enabled | Required property | Description  
---|---|---|---  
Reference name | No | Yes | Used to uniquely identify this source for tasks, such as lineage, annotating metadata.  
Use connection | No | No | Use an existing connection. If a connection is used, you don't need to provide the credentials.  
Browse connections | Yes | No | Name of the connection to use.  
Username | Yes | Yes | Salesforce username.  
Password | Yes | Yes | Salesforce password.  
Security token | Yes | No | Salesforce security token. If the password doesn't contain the security token Cloud Data Fusion appends the token before authenticating with Salesforce.  
Consumer key | Yes | Yes | Application Consumer Key. This is also called the OAuth client ID. To obtain a consumer key, [create a Salesforce connected application](https://docs.cloud.google.com/data-fusion/docs/how-to/create-salesforce-app-for-plugin).   
Consumer secret | Yes | Yes | Application Consumer Secret. This is also called the OAuth client secret. To obtain a client secret [create a Salesforce connected application](https://docs.cloud.google.com/data-fusion/docs/how-to/create-salesforce-app-for-plugin).   
Login URL | Yes | Yes | Salesforce OAuth2 login URL.  
The default is `https://login.salesforce.com/services/oauth2/token`  
Connection timeout | Yes | No | Maximum time, in milliseconds, to wait for connection initialization before it times out.  
Default is 30000 milliseconds.  
Proxy URL | Yes | No | Proxy URL, which contain a protocol, address, and port.  
SOQL | Yes | No | An SOQL query to fetch data into source.  
Examples:  


  * `SELECT Id, Name, BillingCity FROM Account`
  * `SELECT Id FROM Contact WHERE Name LIKE 'A%' AND MailingCity = 'California'`

  
SObject name | Yes | No | Salesforce object name to read. If value is provided, the connector gets all fields for this object from Salesforce and generates a SOQL query, such as `select FIELD_1, FIELD_2 from ${sObjectName}`. Ignored if SOQL query is provided.  
There are also sObjects that aren't supported in the Salesforce Bulk API. Creating a job with an unsupported object causes the following error: `Entity is not supported by the Bulk API`. These objects also aren't supported by Einstein Analytics, which uses Bulk API for querying data.  
**Cases when BULK API isn't used:** When query length sends the query to Salesforce to receive the array of batch information, the Bulk API isn't used in one case. If the query is within the limit, it executes the original query. Otherwise, it switches to wide object logic. For example, it generates an ID query that only retrieves batch information for IDs that will be used later for retrieving data through the SOAP API.   
Last modified after | Yes | No | Filter data to only include records where the system field, `LastModifiedDate`, is greater than or equal to the specified date. Use the Salesforce date format (see examples). If no value is provided, no lower-bound date is applied.  
Last modified before | Yes | No | Filter data to only include records where the system field, `LastModifiedDate`, is less than the specified date. Use the Salesforce date format (see examples). Specifying this value with the **Last modified after** property lets you read data that was modified within a window of time. If no value is provided, no upper-bound date is applied.  
Duration | Yes | No | Filter data to only read records that were last modified within a window of time of the specified size. For example, if the duration is `6 hours` and the pipeline runs at 9 AM, it will read data that was last updated from 3 AM (inclusive) to 9 AM (exclusive). Specify the duration with numbers and the following time units: 

  * `seconds`
  * `minutes`
  * `hours`
  * `days`
  * `months`
  * `years`

Several units can be specified, but each unit can only be used once. For example, `2 days, 1 hours, 30 minutes`. If a value is already specified for **Last modified after** or **Last modified before** , the duration is ignored.  
Offset | Yes | No | Filter data to only read records where the system field, `LastModifiedDate`, is less than the logical start time of the pipeline, minus the given offset. For example, if duration is `6 hours`, the offset is `1 hours`, and the pipeline runs at 9 AM, data that was last modified between 2 AM (inclusive) and 8 AM (exclusive) is read.  
Specify the duration using numbers and the following units of time: 

  * `seconds`
  * `minutes`
  * `hours`
  * `days`
  * `months`
  * `years`

Several units can be specified, but each unit can only be used once. For example, `2 days, 1 hours, 30 minutes`. If a value is already specified for **Last modified after** or **Last modified before** , the offset is ignored.  
SOQL operation type | No | No | Specify the query operation to run on the table. If a query is selected, only current records are returned. Selecting `queryAll` returns all current and deleted records.  
The default operation is `query`.  
Enable PK chunking | Yes | No | Primary key (PK) chunking splits a query on large tables into pieces, or chunks, based on record IDs, or primary keys, of the queried records.  
Salesforce recommends that you enable PK chunking when querying tables with more than 10 million records, or when a bulk query constantly times out. For more information, see [ PK chunking](https://docs.cloud.google.com/data-fusion/docs/concepts/best-practice-salesforce#pk-chunking). PK chunking only works with queries that don't include `SELECT` clauses, or conditions other than `WHERE`. Chunking is supported for custom objects and any Sharing and History tables that support standard objects.  
Chunk size | Yes | No | Specify size of chunk. Maximum size is 250,000. Default size is 100,000.  
SObject parent name | Yes | No | Parent of the Salesforce Object. This is used to enable chunking for history tables or shared objects.  
  
### Salesforce date format examples

Format syntax | Example  
---|---  
`YYYY-MM-DDThh:mm:ss+hh:mm` | `1999-01-01T23:01:01+01:00`  
`YYYY-MM-DDThh:mm:ss-hh:mm` | `1999-01-01T23:01:01-08:00`  
`YYYY-MM-DDThh:mm:ssZ` | `1999-01-01T23:01:01Z`  
  
### Data type mappings

The following table is a list of Salesforce data types with corresponding CDAP types.

Salesforce data type | CDAP schema data type  
---|---  
`_bool` | `boolean`  
`_int` | `int`  
`_long` | `long`  
`_double`, `currency`, `percent`, `geolocation` (latitude), `geolocation` (longitude) | `double`  
`date` | `date`  
`datetime` | `timestamp` (microseconds)  
`time` | `time` (microseconds)  
`picklist` | `string`  
`multipicklist` | `string`  
`combobox` | `string`  
`reference` | `string`  
`base64` | `string`  
`textarea` | `string`  
`phone` | `string`  
`id` | `string`  
`url` | `string`  
`email` | `string`  
`encryptedstring` | `string`  
`datacategorygroupreference` | `string`  
`location` | `string`  
`address` | `string`  
`anyType` | `string`  
`json` | `string`  
`complexvalue` | `string`  
  
## Use cases

See the following use cases for the Salesforce batch source:

  * [Use the Salesforce batch source plugin to analyze leads data in BigQuery](https://docs.cloud.google.com/data-fusion/docs/tutorials/connect-salesforce-to-bq)

  * [Use SOQL queries for the Salesforce source](https://docs.cloud.google.com/data-fusion/docs/use-case/salesforce-soql-queries)




## Prerequisites for upgrading to the Salesforce plugin version 1.7.0

The Salesforce plugin version 1.7.0 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the upgrade of Salesforce Bulk API V1 version from 62.0 to 64.0.

Salesforce has deprecated certain fields in the API version 64.0. Upgrading to the Salesforce plugin version 1.7.0 might cause pipelines that use these fields to fail. To ensure your pipelines continue to work, manually update your pipeline schema to either load a new schema or remove the deprecated fields.

### Deprecated fields in Salesforce API version 64.0

Salesforce has deprecated the following fields in the API version 64.0:

Object name | Field names  
---|---  
MobSecurityCertPinConfig | EffectiveDate  
Profile | PermissionsAllowObjectDetectionTraining  
PermissionsAllowObjectDetection  
PermissionSet | PermissionsAllowObjectDetectionTraining  
PermissionsAllowObjectDetection  
PermissionSetLicense | MaximumPermissionsAllowObjectDetectionTraining  
MaximumPermissionsAllowObjectDetection  
UserPermissionAccess | PermissionsAllowObjectDetectionTraining  
PermissionsAllowObjectDetection  
MutingPermissionSet | PermissionsAllowObjectDetectionTraining  
PermissionsAllowObjectDetection  
Domain | OptionsHstsHeaders  
User | UserPreferencesHideInvoicesRedirectConfirmation  
UserPreferencesHideStatementsRedirectConfirmation  
UserChangeEvent | UserPreferencesHideInvoicesRedirectConfirmation  
UserPreferencesHideStatementsRedirectConfirmation  
  
### Update pipeline schema

If your pipeline uses any deprecated fields, then update the pipeline schema by either loading a fresh schema or by removing the deprecated fields:

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and click **List**.

  2. To view the deployed pipelines, click the **Deployed** tab.

  3. For the pipeline you want to update, click more_vert > **Edit**.

  4. In the **Studio** view, hold the pointer over the Salesforce source plugin, and click **Properties**.

The configuration window for the Salesforce plugin opens.

  5. To load a new schema, follow these steps:

     1. In the **Output schema** tab, click more_vert > **Clear** , and then click **Validate**. This loads the latest schema from Salesforce.

     2. After the schema loads, in the **Output schema** tab, click more_vert > **Propagate**.

This automatically updates the schema for all subsequent plugins in the pipeline, which might overwrite manual schema changes in plugins like Wrangler.

  6. To manually remove the deprecated fields, follow this step:

     1. In the **Output schema** tab, for each of the deprecated fields, click delete. This removes the fields from all subsequent stages.



## Best practices

For more information about improving performance in the Salesforce batch source, see the [best practices](https://docs.cloud.google.com/data-fusion/docs/concepts/best-practice-salesforce).

## Release notes

  * [September 09, 2025](https://docs.cloud.google.com/data-fusion/docs/release-notes#September_09_2025)
  * [June 02, 2025](https://docs.cloud.google.com/data-fusion/docs/release-notes#June_02_2025)
  * [March 14, 2024](https://docs.cloud.google.com/data-fusion/docs/release-notes#March_14_2024)
  * [August 7, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#August-7%2C-2023)
  * [August 4, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#August-4%2C-2023)
  * [July 7, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#July-7%2C-2023)
  * [June 7, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#June-7%2C-2023)
  * [May 25, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#May-25%2C-2023)
  * [April 13, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#April-13%2C-2023)
  * [March 20, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#March-20%2C-2023)



## What's next

  * Work through a [Salesforce plugin tutorial](https://docs.cloud.google.com/data-fusion/docs/tutorials/connect-salesforce-to-bq).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
