---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication/
title: Configure the connector for file-based replication to Cloud Storage \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:25.332638+00:00
---

# Configure the connector for file-based replication to Cloud Storage  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure the connector for file-based replication to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure file-based replication from SAP to Cloud Storage by using BigQuery Connector for SAP.

## Before you begin

Make sure that you or your administrators have completed the following prerequisites:

  * [Installed](https://docs.cloud.google.com/sap/docs/bq-connector/latest/install) the BigQuery Connector for SAP in your SAP environment.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication) to access the Cloud Storage JSON API.
  * Created a target [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) and [folder structure](https://docs.cloud.google.com/storage/docs/create-folders) for the replicated SAP data. The connector doesn't auto-create these resources.

The full path to the target bucket and folder structure must not exceed 255 characters. This character limit is specific to the BigQuery Connector for SAP and is more restrictive than the limits of Cloud Storage.




## Create SAP roles and authorizations for BigQuery Connector for SAP

To work with BigQuery Connector for SAP, in addition to the standard SAP LT Replication Server authorizations, users need access to the custom transactions that are provided with BigQuery Connector for SAP: `/GOOG/SLT_SETTINGS` and `/GOOG/REPLIC_VALID`.

By default, users that have access to the custom transactions `/GOOG/SLT_SETTINGS` and `/GOOG/REPLIC_VALID`can modify the settings of any configuration, so if you need to, you can restrict access to specific configurations. For users who only need to view the BigQuery Connector for SAP settings, you can grant them read-only access to the custom transaction `/GOOG/SLT_SETT_DISP`.

The BigQuery Connector for SAP transport files include the `Google BigQuery Settings Authorization` object, `ZGOOG_MTID`, for authorizations that are specific to BigQuery Connector for SAP.

To grant access to the custom transactions and restrict access to specific configurations, perform the following steps:

  1. Using SAP transaction code `PFCG`, define a role for the BigQuery Connector for SAP.

  2. Grant the role access to the custom transactions .

  3. To limit the access of a role, specify the authorization group of each configuration that the role can access by using the `ZGOOG_MTID` authorization object. For example:

     * Authorization object for BigQuery Connector for SAP (`ZGOOG_MTID`): 
       * `Activity 01`
       * `Authorization Group AUTH_GROUP_1,AUTH_GROUP_N`

The `AUTH_GROUP_01` and `AUTH_GROUP_N` are values that are defined in the SAP LT Replication Server configuration.

The authorization groups specified for `ZGOOG_MTID` must match the authorization groups that are specified for the role in the SAP `S_DMIS_SLT` authorization object.




### Create SAP roles and authorizations for viewing BigQuery Connector for SAP settings

To grant read-only access for the custom transaction `/GOOG/SLT_SETT_DISP`, perform the following steps:

  1. Using SAP transaction code `PFCG`, define a role for viewing the BigQuery Connector for SAP settings.

  2. Grant the role access to the custom transaction `/GOOG/SLT_SETT_DISP`.

  3. Add the authorization object for BigQuery Connector for SAP (`ZGOOG_MTID`) with the following attributes:

     * `Activity 03`
     * `Authorization Group = *`
  4. Generate the role profile and assign relevant users to the role.




### Manage authorizations for configuration tables

To provide granular control over sensitive configuration data, BigQuery Connector for SAP assigns the tables `/GOOG/CLIENT_KEY` and `/GOOG/SERVIC_MAP` to the custom authorization group `ZSGC`. These tables hold critical settings, which are used to authenticate and connect to Google Cloud APIs. To maintain or grant access to these settings, administrators must update user roles to include authorization for the `ZSGC` group.

To grant access to the BigQuery Connector for SAP configuration tables, perform the following steps:

  1. Identify the users and roles that require access to the tables `/GOOG/CLIENT_KEY` and `/GOOG/SERVIC_MAP`.
  2. In the SAP GUI, enter transaction code `PFCG`.
  3. Open the relevant role for editing and go to the **Authorizations** tab.
  4. Click **Change Authorization Data**.
  5. Add the authorization object `S_TABU_DIS` with the following attributes: 
     * **Activity** : `02` (Change) or `03` (Display).
     * **Authorization Group** : `ZSGC`.
  6. Click **Save** and then click the **Generate** icon to update the role profile.



## Configure replication

To configure replication, you specify both BigQuery Connector for SAP and SAP LT Replication Server settings.

### Create an SAP LT Replication Server replication configuration

Use SAP transaction `LTRC` to create an SAP LT Replication Server replication configuration.

If SAP LT Replication Server is running on a different server than the source SAP system, before you create a replication configuration, confirm that you have an RFC connection between the two systems.

Some of the settings in the replication configuration affect performance. To determine appropriate setting values for your installation, see the _Performance Optimization Guide_ for your version of SAP LT Replication Server in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

The interface and configuration options for SAP LT Replication Server might be slightly different depending on which version you are using.

To configure replication, use the procedure for your version of SAP LT Replication Server:

  * Configure replication in DMIS 2011 SP17, DMIS 2018 SP02, or later
  * Configure replication in DMIS 2011 SP16, DMIS 2018 SP01, or earlier



#### Configure replication in DMIS 2011 SP17, DMIS 2018 SP02, or later

The following steps configure replication in later versions of SAP LT Replication Server. If you are using an earlier version, see Configure replication in DMIS 2011 SP16, DMIS 2018 SP01, or earlier.

  1. In the SAP GUI, enter transaction code `LTRC`.

  2. Click the **Create configuration** icon. The **Create Configuration** wizard opens.

  3. In the **Specify General Data** panel:

     1. In the **Configuration Name** and **Description** fields, enter a name and a description for the configuration.
     2. Optional: To restrict access, in the **Authorization Group** field, specify an authorization group.
     3. If the **Application** field appears in this panel, such as in SAP S/4HANA systems, then enter `/GOOG/SLT_BQ` or `ZGOOG_SLT_BQ`.

In SAP ECC systems, you specify this field later in the **Specify Transfer Settings** panel.

     4. Click **Next**.

  4. In the **Source System Connection Details** panel:

     1. Select the **RFC Connection** radio button.
     2. In the **RFC Destination** field, specify the name of the RFC connection to the source system.
     3. Select the checkboxes for **Allow Multiple Usage** and **Read from Single Client** as appropriate. For more information, see the [SAP LT Replication Server documentation](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).
     4. Click **Next**.

These steps are for an RFC connection, but if your source is a database, you can select **DB Connection** if you have already defined a connection by using transaction `DBACOCKPIT` instead.

  5. In the **Target System Connection Details** panel:

     1. Select the radio button for **Other**.
     2. In the **Scenario** field, select **SLT SDK** from the drop-down menu.
     3. Click **Next**.
  6. In the **Specify Transfer Settings** panel:

     1. If the **Application** field appears in the **Data Transfer Settings** section, such as in SAP ECC systems, then enter `/GOOG/SLT_BQ` or `ZGOOG_SLT_BQ`.

In SAP S/4HANA systems, you already specified this field in the **Specify General Data** panel.

     2. In the **Job options** section, enter starting values in each of the following fields:

        * **Number of Data Transfer Jobs**
        * **Number of Initial Load Jobs**
        * **Number of Calculation Jobs**
     3. In the **Replication Options** section, select the **Real Time** radio button.

     4. Click **Next**.

  7. After reviewing the configuration, click **Save**.

  8. Make a note of the three-digit ID in the **Mass Transfer** column. You use it in a later step.




For more information, see the PDF attached to [SAP Note 2652704](https://launchpad.support.sap.com/#/notes/2652704): _Replicating Data Using SLT SDK - DMIS 2011 SP17, DMIS 2018 SP02.pdf_.

#### Configure replication in DMIS 2011 SP16, DMIS 2018 SP01, or earlier

The following steps configure replication in earlier versions of SAP LT Replication Server. If you are using a later version, see Configure replication in DMIS 2011 SP17, DMIS 2018 SP02, or later.

  1. In the SAP GUI, enter transaction code `LTRC`.
  2. Click **New**. A dialog opens for specifying a new configuration.
  3. In the step **Specify Source System** : 
     * Choose **RFC Connection** as the connection type.
     * Enter the RFC connection name.
     * Ensure that the field **Allow Multiple Usage** is selected.
  4. In the step **Specify Target System** : 
     * Enter the connection data to the target system.
     * Choose **RFC Connection** as the connection type.
     * In the field **Scenario for RFC Communication** , select the value **Write Data to Target Using BAdI** from the drop-down list. The RFC connection is automatically set to **NONE**.
  5. In the step **Specify Transfer Settings** , press **F4 Help**. The application that you defined previously is displayed in the **Application** field.
  6. Make a note of the three-digit ID in the **Mass Transfer** column. You use it in a later step.



For more information, see the PDF attached to [SAP Note 2652704](https://launchpad.support.sap.com/#/notes/2652704): _Replicating Data Using SLT SDK - DMIS 2011 SP15, SP16, DMIS 2018 SP00, SP01.pdf_.

### Create a mass transfer configuration for Cloud Storage

Use the custom `/GOOG/SLT_SETTINGS` transaction to configure a mass transfer for Cloud Storage.

#### Select the initial mass transfer options

When you first enter the `/GOOG/SLT_SETTINGS` transaction, you select which part of the Cloud Storage mass transfer configuration you need to edit.

To select the part of the mass transfer configuration, do the following:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. From the drop-down menu in the **Google Cloud Partner** field, select **Cloud Storage**.

  3. From the **Settings Table** drop-down menu in the launch screen for the `/GOOG/SLT_SETTINGS` transaction, select **Mass Transfers**.

For a new mass transfer configuration, leave the **Mass Transfer Key** field blank.

  4. Click the **Execute** icon. The **Cloud Storage Settings Maintenance - Mass Transfers** screen appears.




#### Specify general attributes

In the initial section of a Cloud Storage mass transfer configuration, you identify the mass transfer configuration and specify the associated client key.

SAP LT Replication Server saves the mass transfer configuration as a record in the `/GOOG/BQ_MASTR` custom configuration table.

The **Extra Fields Flag** is enabled by default and you cannot deselect this field. This setting ensures that the timestamps required for downstream deduplication in BigQuery are always captured in your JSON files.

To specify the general attributes, do the following:

  1. In the **Cloud Storage Settings Maintenance - Mass Transfers** screen, click the **Append Row** icon.

  2. In the **Mass Transfer Key** field, define a name for this transfer. This name becomes the primary key of the mass transfer.

  3. In the **Mass Transfer ID** field, enter the three-digit ID that was generated when you created the corresponding SAP LT Replication Server replication configuration.

  4. To use the labels or short descriptions of the source fields as the names for the target fields in JSON files, click the **Use Custom Names Flag** checkbox.

  5. Optionally, to automatically reduce the chunk size when the byte size of a chunk exceeds the maximum byte size for HTTP requests that Cloud Storage accepts, click the **Dynamic Chunk Size Flag** checkbox. For more information about dynamic chunk size, see [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#dynamic-chunk-size).

  6. In the **Google Cloud Key Name** field, enter the name of the client key specified in the `/GOOG/CLIENT_KEY` configuration.

BigQuery Connector for SAP retrieves the Google Cloud **Project Identifier** automatically from the `/GOOG/CLIENT_KEY` configuration.

  7. In the **Is Setting Active Flag** field, enable the mass transfer configuration by clicking the checkbox.

  8. Click **Save**.

A mass transfer record is appended in the `/GOOG/BQ_MASTR` table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.

  9. Click **Display Table**.

The new mass transfer record is displayed followed by the table attribute entry panel. 




### Specify table attributes

In the second section of the `/GOOG/SLT_SETTINGS` transaction, you specify SAP source table, target Cloud Storage bucket URI, and _chunk_ that is sent to Cloud Storage.

To specify table attributes, do the following:

  1. Click the **Append row** icon.

  2. In the **SAP Table Name** field, enter the name of the source SAP table.

  3. Optionally, in the **Chunk Size** field, specify the maximum number of records to include in each chunk that is sent to Cloud Storage. We recommend that you use the default chunk size with BigQuery Connector for SAP, which is 50,000 records.

  4. In the **Cloud Storage URI** field, enter the full path to your target Cloud Storage bucket and folder structure, in one of the following formats:

     * `BUCKET_NAME/FOLDER_NAME`
     * `gs://BUCKET_NAME/FOLDER_NAME`
**Note:** Ensure that the full path to your target bucket and folder structure doesn't exceed 255 characters.
  5. In the **Is Setting Active Flag** field, enable the table attributes by clicking the checkbox.

  6. Click **Save**.

Your attributes are stored as a record in the `/GOOG/BQ_TABLE` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.

  7. To verify the table attributes that you entered, click **Display Fields**. The new table attribute record is displayed, followed by the field definitions panel.




### Customize the default field definitions

If the source SAP table contains timestamp or boolean fields, then change the default field definitions to accurately reflect the intended data format in the target JSON files. 

You can edit the default field definitions directly in the SAP GUI or you can export the default field definitions to a spreadsheet or a text file so that others can edit the values without requiring access to SAP LT Replication Server.

For more information about the default field definitions and the changes that you can make, see [Field properties](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#field-properties-gcs).

To edit the default field definitions, do the following:

  1. In the **Cloud Storage Settings Maintenance - Fields** page of the transaction `/GOOG/SLT_SETTINGS`, display the default field definitions for the mass transfer that you are configuring.

  2. In the **External Data Element** column, edit the data formats, as needed. In particular, change the following:

     * **Timestamps.** Change from `NUMERIC` to `TIMESTAMP` or `TIMESTAMP (LONG)`.
     * **Booleans.** Change from `STRING` to `BOOLEAN`.
     * **Hexadecimals.** Change from `STRING` to `BYTES`.

To edit the default data format:

     1. On the row of the field that you need to edit, click the **External Data Element** field.
     2. Select the data format required for your JSON output.
     3. Confirm your changes, and then click **Save**.
  3. If you specified **Use Custom Names Flag** in the **Cloud Storage Settings Maintenance** page, then edit the default target field names in the **Temporary Field Name** column, as needed.

The values that you specify override the default names that are shown in the **External Field Name** column.

  4. Optionally, export the field definitions for external editing. For instructions, see [Edit field definitions in a CSV file](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#edit-field-definitions-in-csv).

  5. After all changes are complete and any externally edited values have been uploaded, confirm that the **Is Setting Active Flag** checkbox is selected. If **Is Setting Active Flag** is not selected, then the BigQuery Connector for SAP creates target JSON files using default values.

  6. Click **Save**.

The changes are stored in the `/GOOG/BQ_FIELD` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.




### Enable token caching

To improve replication performance, we recommend that you enable caching for the access token that you retrieve from Google Cloud.

Enabling token caching makes sure that an access token is reused until the access token expires or is revoked, which in turn reduces the number of HTTP calls made to retrieve new access tokens.

To enable token caching, select the **Token Caching** flag in the [client key table `/GOOG/CLIENT_KEY`](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token#specify-clientkey-table).

When you enable token caching, the access token is cached in the Shared Memory of your SAP LT Replication Server application server for the duration that is set for the **Token Refresh Seconds** field in the `/GOOG/CLIENT_KEY` table. If **Token Refresh Seconds** is not specified or is set to `0`, then the access token is cached for the value specified in the `CMD_SECS_DEFLT` parameter in [advanced settings](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#advanced-settings).

For SAP workloads that are not running on Google Cloud, the cached access tokens also prevent technical issues that might arise while replicating huge data loads, where several processes of SAP LT Replication Server can simultaneously request for an access token at any given time.

For SAP workloads that are running on Google Cloud and use a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-created) to access Google Cloud, token caching can bring a significant improvement as retrieving an access token in this scenario involves making two HTTP calls.

#### Clear the cached access token

When token caching is enabled and you update the roles assigned to the service account that BigQuery Connector for SAP uses to access Google Cloud, the new access token that corresponds to the updated roles is retrieved only after the existing cached token expires. In such situations, you can clear the access token manually.

To clear the cached access token, enter transaction `SE38` and then run the program `/GOOG/R_CLEAR_TOKEN_CACHE`.

## Test replication configuration

Test the replication configuration by starting data provisioning:

  1. Open the SAP LT Replication Server Cockpit (transaction `LTRC`) in the SAP GUI.

  2. Click the mass transfer configuration for the table replication that you are testing.

  3. Click **Data Provisioning**.

  4. In the **Data Provisioning** panel, start data provisioning:

     1. Enter the name of the source table.
     2. Click the radio button for the type of data provisioning that you want to test. For example, **Start Load**.
     3. Click the **Execute** icon. The data transfer begins and the progress is displayed on the **Participating objects** screen.

If the target bucket doesn't exist in Cloud Storage, then the replication fails. You must manually create your target Cloud Storage bucket and folder structure. The length of time that an initial load of a table takes depends on the size of the table and its records. 
    
    
       Messages are written to the SAP LT Replication Server **Application Logs**
       section in transaction `LTRC`.
    

## Validate replication

You can validate replication by using the following methods:

  * In SAP LT Replication Server: 
    * Monitor the replication on the **Data Provisioning** screen.
    * Check for error messages in the **Application Logs** screen.
  * In Cloud Storage, check object details: 
    * Preview the text content of the JSON file to confirm that records include source SAP field names and the mandatory record timestamp.
    * Check object metadata, including **Size** , **Creation time** , and **Storage class**.



### Check replication status in SAP LT Replication Server

To see the progress of initial load or replication jobs and to check for error messages, use transaction `LTRC` as follows:

  * To view the status of the load, see the **Load Statistics** tab.
  * To view the progress of the job, see the **Data Transfer Monitor** tab.
  * To view all of the messages that are returned by Cloud Storage, the BigQuery Connector for SAP, and SAP LT Replication Server, see the **Application Logs** screen.



Messages that are issued by BigQuery Connector for SAP code in SAP LT Replication Server start with the prefix `/GOOG/SLT`. Messages that are returned from the Cloud Storage JSON API start with the prefix `/GOOG/MSG`.

Messages that are returned by SAP LT Replication Server don't start with a `/GOOG/` prefix.

### Check replication status in Cloud Storage

In the Google Cloud console, confirm that the JSON files were created and that the BigQuery Connector for SAP is uploading data into your specified bucket:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you specified during the configuration of your table attributes.

  3. Navigate through the folder hierarchy to the path that you defined in the **Cloud Storage URI** field.

  4. Verify that the replicated data appears as JSON files. The files use the naming convention `SLT\_CONNECTOR\_SAP_TABLE_NAME\_TIMESTAMP_IN_YYYYMMDDHHMMSS.json`.

  5. Click a filename to open the **Object details** page.

  6. On the **Live object** tab, verify the metadata, including the **Size** , **Creation time** , and **Storage class**.




## What's next

File-based replication to Cloud Storage provides a staged approach for replicating SAP data to BigQuery. The BigQuery Connector for SAP automates the initial stage of this process by capturing SAP changes and delivering them to your bucket as JSON files. The connector's delivery cycle is complete when the JSON files are available in your bucket. From this point, you assume ownership of the integration to BigQuery using your choice of ingestion and deduplication methods.

**Format compatibility** : The connector delivers data in Newline Delimited JSON (NDJSON) format, which meets the standard requirements for BigQuery ingestion. This format lets you use standard tools like BigQuery Data Transfer Service (DTS) or batch load jobs to move your data from Cloud Storage into your analytics tables with minimal configuration.

To move data from Cloud Storage to BigQuery for analytics, perform the following steps:

  1. **Ingest data into BigQuery:** To move your JSON files from Cloud Storage into a BigQuery table, use one of the following methods: 
     * **BigQuery Data Transfer Service (DTS):** Schedule and automate recurring data loads. For more information, see [Load Cloud Storage data into BigQuery](https://docs.cloud.google.com/bigquery/docs/cloud-storage-transfer).
     * **Batch load jobs:** Perform one-time loads or integrate data through custom automation pipelines. For more information, see [Loading JSON data from Cloud Storage](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-json).
  2. **Deduplicate data:** To ensure that your BigQuery tables accurately reflect the current state of your source system, implement a deduplication logic in BigQuery. You need to implement this logic because standard ingestion methods append data by default, and SAP system updates result in new files rather than modifying existing ones.

**Note:** To identify the most recent record during your deduplication process, use the record timestamps provided by the **Extra Fields Flag**. 

## Troubleshoot

For information about diagnosing and resolving issues that you might encounter when you configure the BigQuery Connector for SAP, see [BigQuery Connector for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting).

## Get support

If you need help resolving problems with configuring the BigQuery Connector for SAP, collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
