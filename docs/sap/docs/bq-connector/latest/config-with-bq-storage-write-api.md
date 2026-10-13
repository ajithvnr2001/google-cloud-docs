---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api/
title: Configure the connector for CDC replication through Pub/Sub \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:24.766835+00:00
---

# Configure the connector for CDC replication through Pub/Sub  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure the connector for CDC replication through Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure CDC replication through Pub/Sub, by using the BigQuery Connector for SAP.

## Before you begin

Learn about [the Pub/Sub service and its terminology](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

Make sure that you or your administrators have completed the following prerequisites:

  * Install the BigQuery Connector for SAP.
  * Set up authentication.
  * Create a dead-letter topic.



### Install the BigQuery Connector for SAP

To replicate data to BigQuery using Pub/Sub, install the BigQuery Connector for SAP version 2.9 or later in your SAP environment. For installation instructions, see [Install the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/install).

If you're using streaming data replication with BigQuery Connector for SAP version 2.8 or earlier, then to use CDC replication through Pub/Sub, you must update your connector to the latest version, and then follow the migration steps.

  * For information about updating your connector, see [Update the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#bqc4sap-operations-bqc-update).
  * For information about migrating your replication, see [Migrate to CDC replication through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/migration).



### Set up authentication

To access the Pub/Sub API, you need to set up authentication to Google Cloud. For information about the supported authentication methods and how to set up authentication, see [Authentication overview for the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication).

### Create a dead-letter topic

When a BigQuery subscription fails to write messages to the target BigQuery table, Pub/Sub automatically publishes these undeliverable messages to a [dead-letter topic](https://en.wikipedia.org/wiki/Dead_letter_queue) after all retries. You must manually create this dead-letter topic.

To create a dead-letter topic, you need to [create a standard Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic). This dead-letter topic is functionally identical to any other Pub/Sub topic, but its purpose is specifically for storing dead-letter messages. You can use a single dead-letter topic for multiple replication loads, or configure dedicated dead-letter topics for each replication load based on your requirements.

You specify this dead-letter topic in the **Dead Letter Queue** field when you specify table attributes, so that the dead-letter topic receives any messages that Pub/Sub fails to write to BigQuery through the BigQuery subscription.

To analyze failed messages, reprocess them, or debug issues, you can create another BigQuery subscription on the dead-letter topic. This automates the process of taking messages from the dead-letter topic and writing them into a dedicated BigQuery table. For more information, see [Monitor dead-letter topic for failed messages](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#monitor-dead-letter-topic).

For more information about dead-letter topics, see [Dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures).

## Create SAP roles and authorizations for BigQuery Connector for SAP

To work with BigQuery Connector for SAP, in addition to the standard SAP LT Replication Server authorizations, users need access to the custom transactions that are provided with BigQuery Connector for SAP: `/GOOG/SLT_SETTINGS` and `/GOOG/REPLIC_VALID`.

By default, users that have access to the custom transactions `/GOOG/SLT_SETTINGS` and `/GOOG/REPLIC_VALID`can modify the settings of any configuration, so if you need to, you can restrict access to specific configurations. For users who only need to view the BigQuery Connector for SAP settings, you can grant them read-only access to the custom transaction `/GOOG/SLT_SETT_DISP`.

The BigQuery Connector for SAP transport files include the `Google BigQuery Settings Authorization` object, `ZGOOG_MTID`, for authorizations that are specific to BigQuery Connector for SAP.

To grant access to the custom transactions and restrict access to specific configurations, perform the following steps:

  1. Using SAP transaction code `PFCG`, define a role for the BigQuery Connector for SAP.

  2. Grant the role access to the custom transactions `/GOOG/SLT_SETTINGS` and `/GOOG/REPLIC_VALID` .

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

### Create a mass transfer configuration for BigQuery

Use the custom `/GOOG/SLT_SETTINGS` transaction to configure a mass transfer for BigQuery and specify the table and field mappings.

#### Select the initial mass transfer options

When you first enter the `/GOOG/SLT_SETTINGS` transaction, you select which part of the BigQuery mass transfer configuration you need to edit.

To select the part of the mass transfer configuration, do the following:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. From the drop-down menu in the **Google Cloud Partner** field, select **BigQuery CDC via Pub/Sub**. 

  3. From the **Settings Table** drop-down menu in the launch screen for the `/GOOG/SLT_SETTINGS` transaction, select **Mass Transfers**.

For a new mass transfer configuration, leave the **Mass Transfer Key** field blank.

  4. Click the **Execute** icon. The **BigQuery Settings Maintenance - Mass Transfers** screen displays.




#### Specify table creation and other general attributes

In the initial section of a BigQuery mass transfer configuration, you identify the mass transfer configuration and specify the associated client key, as well as certain properties related to the creation of the target BigQuery table.

SAP LT Replication Server saves the mass transfer configuration as a record in the `/GOOG/BQ_MASTR` custom configuration table.

  1. In the **BigQuery Settings Maintenance - Mass Transfers** screen, click the **Append Row** icon.

  2. In the **Mass Transfer Key** field, define a name for this transfer. This name becomes the primary key of the mass transfer.

  3. In the **Mass Transfer ID** field, enter the three-digit ID that was generated when you create the corresponding SAP LT Replication Server replication configuration.

  4. To use the labels or short descriptions of the source fields as the names for the target fields in BigQuery, click the **Use Custom Names Flag** checkbox. For more information about field names, see [Default naming options for fields](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#default-field-names).

  5. To store the type of change that triggered an insert and to enable the validation of record counts between the source table, SAP LT Replication Server statistics, and the BigQuery table, select the **Extra Fields Flag** checkbox.

When this flag is set, BigQuery Connector for SAP adds columns to the BigQuery table schema. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#add-fields-for-changes-and-counts).

  6. To stop sending data when a record with a data error is encountered, the **Break at First Error Flag** checkbox is checked by default. We recommend leaving this checked. For more information, see [The BREAK flag](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#break-flag).

  7. Optionally, to automatically reduce the chunk size when the byte size of a chunk exceeds the maximum byte size for HTTP requests that Pub/Sub accepts, click the **Dynamic Chunk Size Flag** checkbox. For more information about dynamic chunk size, see [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#dynamic-chunk-size).

  8. When a record with a data error is encountered, to skip the record and continue inserting records into the BigQuery table, click the **Skip Invalid Records Flag** checkbox. We recommend leaving this unchecked. For more information, see [The SKIP flag](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#skip-flag).

  9. In the **Google Cloud Key Name** field, enter the name of the client key specified in the `/GOOG/CLIENT_KEY` configuration.

BigQuery Connector for SAP retrieves the Google Cloud **Project Identifier** automatically from the `/GOOG/CLIENT_KEY` configuration.

  10. In the **BigQuery Dataset** field, enter the name of the target BigQuery dataset where you want to store your replicated SAP data. For information about how to create a BigQuery dataset, see the relevant authentication guide:

     * [Authenticate with JSON Web Tokens: Create a BigQuery dataset](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt#create-bq-dataset)
     * [Authenticate with access tokens: Create a BigQuery dataset](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token#create-bq-dataset)
  11. In the **Is Setting Active Flag** field, enable the mass transfer configuration by clicking the checkbox.

  12. Click **Save**.

A mass transfer record is appended in the `/GOOG/BQ_MASTR` table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.

  13. Click **Display Table**.

The new mass transfer record is displayed followed by the table attribute entry panel. 




### Specify table attributes

You can specify table attributes, such as table name and table partitioning, as well as the number of records to include in each transmission or _chunk_ that is sent to BigQuery, in the second section of the `/GOOG/SLT_SETTINGS` transaction.

The settings that you specify are stored as a record in the `/GOOG/BQ_TABLE` configuration table.

To specify table attributes, do the following:

  1. Click the **Append row** icon.

  2. In the **SAP Table Name** field, enter the name of the source SAP table.

  3. In the **External Table Name** field, provide the target BigQuery table name. If the target table doesn't already exist, BigQuery Connector for SAP creates this table inline with the SAP table definition. It also defines the primary keys in this table to enable `UPSERT` or `DELETE` operations. The table supports composite primary keys containing up to 16 columns. For the BigQuery naming conventions for tables, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming).

  4. Skip the **Send Uncompressed Flag**. For CDC replication through Pub/Sub, the record compression feature is not supported. 

  5. Optionally, in the **Chunk Size** field, specify the maximum number of records to include in each chunk that is sent to Pub/Sub. We recommend that you use the default chunk size with BigQuery Connector for SAP, which is 1,000 records. This is the maximum number of records that Pub/Sub allows.

If the source records have a large number of fields, the number of fields can increase the overall byte size of the chunks, which can cause chunk errors. If this occurs, try reducing the chunk size to reduce the byte size. For more information, see [Chunk size in the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#chunk-size-bqc4sap). Alternatively, to automatically adjust the chunk size, enable dynamic chunk size. For more information, see [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#dynamic-chunk-size).

  6. Optionally, in the **Partition Type** field, specify an increment of time to use for partitioning. Valid values are `HOUR`, `DAY`, `MONTH`, or `YEAR`. For more information, see [Table partitioning](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#table_partitioning).

  7. Optionally, in the **Partition Field** field, specify the name of a field in the target BigQuery table that contains a timestamp to use for partitioning. When you specify **Partition Field** , you must also specify **Partition Type**. For more information, see [Table partitioning](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#table_partitioning).

  8. In the **Is Setting Active Flag** field, enable the table attributes by clicking the checkbox. If the **Is Setting Active Flag** box is not selected, BigQuery Connector for SAP creates the BigQuery table with the name of the SAP source table, the default chunk size, and no partitioning.

  9. For CDC replication through Pub/Sub, specify the following attributes:

     1. To enable CDC replication to BigQuery through Pub/Sub, select the **Repl CPS** (Replication Cloud Pub/Sub) checkbox.

If this checkbox is cleared, the BigQuery Connector for SAP uses [streaming data replication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#streaming-api-insert-only), and Pub/Sub-related configuration fields are disabled.

     2. In the **Pub/Sub Schema** field, enter a name for the Pub/Sub schema. The BigQuery Connector for SAP automatically creates or updates an existing Avro schema to match the SAP table definition.

     3. In the **Pub/Sub Topic** field, enter a name for the Pub/Sub topic where messages are published. The BigQuery Connector for SAP automatically creates a topic.

     4. In the **Pub/Sub Subscription** field, enter a name for the BigQuery subscription that consumes messages from the Pub/Sub topic and writes to BigQuery. The BigQuery Connector for SAP automatically creates a subscription and links it to the topic specified in the preceding step.

     5. In the **Dead Letter Queue** field, enter the name of the Pub/Sub dead-letter topic that you created in the Create a dead-letter topic section. This dead-letter topic receives messages that Pub/Sub fails to write to BigQuery through the BigQuery subscription.

You must manually create a dead-letter topic. For more information about dead-letter topics, see Create a dead-letter topic.

**Warning:** Not configuring a dead-letter topic can result in data loss that you cannot recover.
     6. To enable the Change Data Capture (CDC) functionality for the table, select the **Act. CDC** (Activate CDC) checkbox.

**Note:** When active, the system validates the corresponding BigQuery table has primary keys. If primary keys don't exist in the BigQuery table, the system automatically creates them based on the SAP table definition. Additionally, any incompatible changes, such as a primary key that was deleted from the SAP source, are flagged to make sure data consistency.
     7. To optimize performance for initial loads, select the **Cache Val** (Cache Validation) checkbox.

When you select this field, the connector provides maximum performance for large data transfers. The system runs Google Cloud pipeline validations at intervals and caches the results. The connector provides rapid data transformation and sends data directly to Pub/Sub. For more information, see [Cache Validations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#cache-validations).

**Note:** For replication mode, don't select this field.
  10. Click **Save**.

Your attributes are stored as a record in the `/GOOG/BQ_TABLE` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.

  11. To verify the table attributes that you entered, click **Display Fields**.

The new table attribute record is displayed, followed by the field mapping entry panel. 




### Customize the default field mapping

If the source SAP table contains timestamp or boolean fields, then change the default data type mapping to accurately reflect the data type in the target BigQuery table. 

You can also change other data types, as well as the names that are used for target fields.

You can edit the default mapping directly in the SAP GUI or you can export the default mapping to a spreadsheet or a text file so that others can edit the values without requiring access to SAP LT Replication Server.

For more information about the default field mapping and the changes you can make, see [Data type mapping](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#data-type-mapping).

To customize the default mapping for the target BigQuery fields:

  1. In the **BigQuery Settings Maintenance - Fields** page of the transaction `/GOOG/SLT_SETTINGS`, display the default field mappings for the mass transfer you are configuring.

  2. Edit the target Avro type for a field in the **AVRO type** column as needed. In particular, change the target Avro type for the following Avro types:

     * **Booleans.** Change the default target Avro type from `STRING` to `BOOLEAN`.
     * **Hexadecimals.** Change the default target Avro type from `STRING` to `BYTES`.

To edit the Avro type:

     1. On the row of the field that you need to edit, click the **Avro type** field.
     2. In the dialog for Avro type, select the BigQuery data type that you need.
     3. Confirm your changes, and then click **Save**.
  3. Edit the default target data types in the **External Data Element** column as needed. In particular, change the target data type for the following data types:

     * **Timestamps.** Change the default target data type from `NUMERIC` to `TIMESTAMP` or `TIMESTAMP (LONG)`.
     * **Booleans.** Change the default target data type from `STRING` to `BOOLEAN`.
     * **Hexadecimals.** Change the default target data type from `STRING` to `BYTES`.

To edit the default data type mapping:

     1. On the row of the field that you need to edit, click the **External Data Element** field. 
     2. In the dialog for data types, select the BigQuery data type that you need.
     3. Confirm your changes, and then click **Save**.
  4. If you specified the **Custom Names** flag in the **BigQuery Settings Maintenance** page, edit the default target field names in the **Temporary Field Name** column as needed.

The values that you specify override the default names that are shown in the **External Field Name** column.

  5. Edit the default target field descriptions in the **Field Description** column as needed.

  6. Optionally, export the field map for external editing. For instructions, see [Edit field mapping in a CSV file](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#edit-field-definitions-in-csv).

  7. After all changes are complete and any externally edited values have been uploaded, confirm that the **Is Setting Active Flag** checkbox is selected. If **Is Setting Active Flag** is not selected, BigQuery Connector for SAP creates target tables with the default values.

  8. Click **Save**.

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

If the table doesn't exist in BigQuery, then the BigQuery Connector for SAP creates the table from a schema that it builds from the table and field attributes that you previously defined with the `/GOOG/SLT_SETTINGS` transaction. The length of time that an initial load of a table takes depends on the size of the table and its records. 
    
    
       Messages are written to the SAP LT Replication Server **Application Logs**
       section in transaction `LTRC`.
    

## Validate replication

You can validate replication using the following methods:

  * In SAP LT Replication Server: 
    * Monitor the replication on the **Data Provisioning** screen.
    * Check for error messages in the **Application Logs** screen.
  * On the table information tab in BigQuery:

    * Check the **Schema** tab to ensure that the schema looks right.
    * Check the **Preview** tab to see a preview of the inserted rows.
    * Check the **Details** tab for the number of rows inserted, the size of the table, and other information.



### Check replication in SAP LT Replication Server

Use transaction `LTRC` to see the progress of initial load or replication jobs after you start them and to check for error messages.

You can see the status of the load under the **Load Statistics** tab and the progress of the job under the **Data Transfer Monitor** tab in SAP LT Replication Server.

On the **Application Logs** screen of transaction `LTRC`, you can see all of the messages that are returned by BigQuery, the BigQuery Connector for SAP, and SAP LT Replication Server.

Messages that are issued by BigQuery Connector for SAP code in SAP LT Replication Server start with the prefix `/GOOG/SLT`. Messages that are returned from the BigQuery API start with the prefix `/GOOG/MSG`.

Messages that are returned by SAP LT Replication Server don't start with a `/GOOG/` prefix.

### Check replication in BigQuery

In the Google Cloud console, confirm that the table was created and that BigQuery is inserting data into it.

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the search field of the **Explorer** section, type the name of the target BigQuery table, and then press `Enter`.

The table information is displayed under a tab in the content pane on the right side of the page.

  3. In the table information section, click the following headings to check the table and row insertion:

     * **Preview** , which shows the rows and fields that are inserted into the BigQuery table.
     * **Schema** , which shows the field names and data types.
     * **Details** , which shows the table size, the total number of rows, and other details.



## Troubleshoot

For information about diagnosing and resolving issues that you might encounter when you configure the BigQuery Connector for SAP, see [BigQuery Connector for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting).

## Get support

If you need help resolving problems with configuring the BigQuery Connector for SAP, collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
