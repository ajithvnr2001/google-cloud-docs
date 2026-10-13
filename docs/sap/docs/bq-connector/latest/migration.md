---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/migration/
title: Migrate to CDC replication through Pub/Sub \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:25.116904+00:00
---

# Migrate to CDC replication through Pub/Sub  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Migrate to CDC replication through Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you migrate from [streaming data replication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#streaming-api-insert-only) to [CDC replication through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#cdc-replication-with-pubsub) when using the BigQuery Connector for SAP.

If you're an existing BigQuery Connector for SAP user and want your BigQuery table to directly reflect changes from the source SAP tables, then you can use CDC replication through Pub/Sub. When your data changes in SAP, the BigQuery Connector for SAP captures the changes, and sends them through Pub/Sub directly to your BigQuery table, applying the changes without duplicates.

**Caution:** This migration is irreversible. Once you migrate your replication settings from streaming data replication to CDC replication, you cannot go back to the streaming data replication.

## Before you begin

Before you begin, learn about [the Pub/Sub service and its terminology](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

Make sure that you or your administrators have completed the following prerequisites:

  * Update the BigQuery Connector for SAP to version 2.9 or later.
  * Enable the Google Cloud APIs.
  * Set up authentication.
  * Create a dead-letter topic.



### Update the BigQuery Connector for SAP

To use CDC replication through Pub/Sub, update your BigQuery Connector for SAP to version 2.9 or later. For information about how to update your connector, see [Update the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#bqc4sap-operations-bqc-update).

### Enable the Google Cloud APIs

For CDC replication through Pub/Sub, make sure the following APIs are enabled:

  * Pub/Sub API
  * BigQuery API
  * IAM Service Account Credentials API



For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

### Set up authentication

To use CDC replication through Pub/Sub, in addition to the existing BigQuery roles, you need to grant the Pub/Sub Editor role to the service account used for authorization. Make sure that the service account has the following roles:

  * Pub/Sub Editor
  * BigQuery Data Editor
  * BigQuery Job User



For information about how to grant a role, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

For information about the supported authentication methods and how to set up authentication, see [Set up authentication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication).

### Create a dead-letter topic

To handle messages that a BigQuery subscription fails to write to the target BigQuery table, you must create a [dead-letter topic](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#create-dead-letter-topic). This dead-letter topic serves as a separate queue where Pub/Sub automatically publishes undeliverable messages after all retries.

## Migration steps

Follow these high-level migration steps:

  1. Stop the SAP LT Replication Server replication configuration.
  2. Prepare the deduplicated CDC table.
  3. Initiate migration through the BigQuery Connector for SAP.
  4. Configure the replication settings.
  5. Activate the SAP LT Replication Server replication configuration.
  6. Check replication in BigQuery.



### Stop the SAP LT Replication Server replication configuration

  1. In the SAP GUI, enter the transaction code `LTRC`.

  2. Stop the SAP LT Replication Server replication configuration that you want to migrate.


**Note:** Intermittent data changes are still captured in the logging table even after you stop the SAP LT Replication Server replication configuration.

### Prepare the deduplicated CDC table

In BigQuery, you need to create a deduplicated CDC table from your existing BigQuery staging table. When you use CDC replication through Pub/Sub, this CDC table becomes the external table in BigQuery for your SAP data.

To prepare a deduplicated CDC table, do the following:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Click **Compose new query**.

  3. Create a CDC table from your existing BigQuery staging table:

     1. In the **Query editor** textarea, to copy your existing BigQuery staging table structure, enter the following query:
            
            CREATE TABLE CDC_TABLE LIKE STAGING_TABLE

Replace the following:

        * `CDC_TABLE`: A name for your BigQuery CDC table.
        * `STAGING_TABLE`: The name of the BigQuery staging table.
**Note:** The `CDC_TABLE` and `STAGING_TABLE` names must be qualified with their dataset names, for example, `PROJECT.DATASET.TABLE`.
     2. Click **Run**.

This step creates a CDC table structure without primary keys.

  4. Modify the CDC table definition to add primary keys:

     1. In the **Query editor** textarea, to add primary keys, enter the following query:
            
            ALTER TABLE CDC_TABLE ADD PRIMARY KEY(PRIMARY_KEYS) NOT INFORCED

Replace the following:

        * `CDC_TABLE`: The name of the CDC table.
        * `PRIMARY_KEYS`: The primary keys as a comma-separated list. You can retrieve the list of primary keys from the source SAP table.
     2. Click **Run**.

  5. Deduplicate the CDC table:

     1. In the **Query editor** textarea, to deduplicate the CDC table, enter the following query:
            
            INSERT INTO CDC_TABLE (COLUMN_NAMES )
            SELECT COLUMN_NAMES FROM STAGING_TABLE WHERE is_deleted = false QUALIFY ROW_NUMBER() OVER( PARTITION BY PRIMARY_KEYS ORDER BY recordstamp DESC ) = 1

Replace the following:

        * `CDC_TABLE`: The name of the CDC table.
        * `COLUMN_NAMES`: The column names as a comma-separated list. You can retrieve the list of column names from the SAP source system. Alternatively, use an asterisk (*) to select all columns.
        * `PRIMARY_KEYS`: The primary keys of the CDC table.
        * `STAGING_TABLE`: The name of the staging table.
     2. Click **Run**.




Alternatively, you can use the **Copy** option in [BigQuery Studio](https://docs.cloud.google.com/bigquery/docs/query-overview#bigquery-studio) to copy the source staging table structure and create a CDC table.

### Initiate migration through the BigQuery Connector for SAP

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`: 
         
         /n/GOOG/SLT_SETTINGS

  2. From the drop-down menu in the **Google Cloud Partner** field, select **BigQuery**.
  3. From the **Settings Table** drop-down menu in the launch screen for the `/GOOG/SLT_SETTINGS` transaction, select **Mass Transfers**.
  4. In the **Mass Transfer Key** field, specify the mass transfer ID of the SAP LT Replication Server replication configuration that you want to migrate.
  5. Click the **Execute** icon.
  6. In the **BigQuery Settings Maintenance - Mass Transfers** screen, click **Migrate**.
  7. In the migration confirmation dialog, click **Yes**.



### Configure the replication settings

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`: 
         
         /n/GOOG/SLT_SETTINGS

  2. From the drop-down menu in the **Google Cloud Partner** field, select **BigQuery CDC via Pub/Sub**.
  3. From the **Settings Table** drop-down menu in the launch screen for the `/GOOG/SLT_SETTINGS` transaction, select **Mass Transfers**.
  4. In the **Mass Transfer Key** field, specify the mass transfer ID of the SAP LT Replication Server replication configuration that you migrated in the section Initiate migration through the BigQuery Connector for SAP.
  5. Click the **Execute** icon. The **BigQuery Settings Maintenance - Mass Transfers** screen displays.
  6. Verify that the migrated SAP LT Replication Server replication configuration is displayed.
  7. For the SAP LT Replication Server replication configuration, specify the following table attributes:

     1. In the **External Table Name** field, enter the name of the CDC table that you created in the preceding step Prepare the deduplicated CDC table.

     2. To enable CDC replication to BigQuery through Pub/Sub, select the **Repl CPS** checkbox.

     3. In the **Pub/Sub Schema** field, enter a name for the Pub/Sub schema. The BigQuery Connector for SAP automatically creates or updates an existing Avro schema to match the SAP table definition.

     4. In the **Pub/Sub Topic** field, enter a name for the Pub/Sub topic where messages are published. The BigQuery Connector for SAP automatically creates a topic.

     5. In the **Pub/Sub Subscription** field, enter a name for the BigQuery subscription that consumes messages from the Pub/Sub topic and writes to BigQuery. The BigQuery Connector for SAP automatically creates a subscription and links it to the topic specified in the preceding step.

     6. In the **Dead Letter Queue** field, enter the name of the Pub/Sub dead-letter topic. This dead-letter topic receives messages that Pub/Sub fails to write to BigQuery through the BigQuery subscription.

     7. To enable the Change Data Capture (CDC) functionality for the table, select the **Act. CDC** (Activate CDC) checkbox.

**Note:** When active, the system validates the corresponding BigQuery table has primary keys. If primary keys don't exist in the BigQuery table, the system automatically creates them based on the SAP table definition. Additionally, any incompatible changes, such as a primary key that was deleted from the SAP source, are flagged to make sure data consistency.
     8. To optimize performance for initial loads, select the **Cache Val** (Cache Validation) checkbox.

When you select this field, the connector provides maximum performance for large data transfers. The system runs Google Cloud pipeline validations at intervals and caches the results. The connector provides rapid data transformation and sends data directly to Pub/Sub. For more information, see [Cache Validations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#cache-validations).

**Note:** For replication mode, don't select this field.



### Activate the SAP LT Replication Server replication configuration

  1. In the SAP GUI, enter the transaction code `LTRC`.

  2. Activate the configuration.

Activating the configuration creates all necessary Pub/Sub related resources and initiates replication. The configured CDC table reflects all new and unprocessed changes.




### Check replication in BigQuery

In BigQuery, verify that the values in the CDC table are the same as your source SAP table. For more information about how to do it, see [Validate the replication to BigQuery](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#validate-rep-bq).

## Troubleshoot

For information about diagnosing and resolving issues that you might encounter when you migrate replication, see [BigQuery Connector for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting).

## Get support

If you need help resolving problems with the migration steps, then collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
