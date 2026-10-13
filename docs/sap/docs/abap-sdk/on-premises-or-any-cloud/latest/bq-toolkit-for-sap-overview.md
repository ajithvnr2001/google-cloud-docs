---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview/
title: BigQuery Toolkit for SAP overview \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:33.864761+00:00
---

# BigQuery Toolkit for SAP overview  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  BigQuery Toolkit for SAP overview Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-toolkit-for-sap-overview)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview)



The BigQuery Toolkit for SAP lets you programmatically access [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) resources within your SAP environment using [ABAP](https://training.sap.com/content/abap-programming-training). You can access BigQuery resources from SAP without having to write boilerplate code for common operations such as the following:

  * **Table definition synchronization** : Keep your SAP and BigQuery tables in sync.
  * **Data type mapping** : Map data types between SAP and BigQuery.
  * **Data chunking** : Efficiently transfer large datasets.
  * **Error handling** : Manage potential errors during data replication.



Unlike [BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning), which requires an [SAP Landscape Transformation Replication Server](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US), you can use the BigQuery Toolkit for SAP within any SAP ERP system where ABAP is supported.

The BigQuery Toolkit for SAP uses the [BigQuery streaming API](https://docs.cloud.google.com/bigquery/streaming-data-into-bigquery), which supports append-only operations for streaming data to BigQuery.

The BigQuery Toolkit for SAP is shipped as a subpackage of the on-premises or any cloud edition of ABAP SDK for Google Cloud. To use the toolkit, you need to install the SDK in your SAP environment. For information about the installation steps, see [Install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

The BigQuery Toolkit for SAP is only available with the on-premises or any cloud edition of ABAP SDK for Google Cloud.

## Data replication from SAP to BigQuery

The BigQuery Data Transfer module of the BigQuery Toolkit for SAP lets you replicate data from SAP to BigQuery for analysis and reporting.

The following diagram shows the data transfer configurations and data replication flow in the BigQuery Data Transfer module:

![Data transfer configurations and replication flow in the BigQuery Data Transfer module](https://docs.cloud.google.com/static/sap/docs/images/bq-toolkit-for-sap-data-transfer-module.svg)

**Data transfer configurations**

As shown in the diagram in the previous section, to establish data replication from SAP to BigQuery, administrators perform the following configurations:

  1. In Google Cloud, the cloud administrator configures BigQuery and grants necessary IAM permissions.
  2. In the SAP system, the SAP system administrator configures ABAP SDK for Google Cloud to allow communication with Google Cloud.
  3. In the SAP system, the SAP system administrator configures the BigQuery Data Transfer module to manage the data transfer settings and BigQuery resource details. These configurations are stored in the following tables: 
     * `/GOOG/BQTR_MASTER`
     * `/GOOG/BQTR_TABLE`
     * `/GOOG/BQTR_FIELD`
     * `/GOOG/BQTR_PARAMS`



When the ABAP code runs, the BigQuery data load class reads the configurations from these tables to guide the data replication process.

**Data replication flow**

As shown in the diagram in the previous section, to replicate data from SAP systems to BigQuery, ABAP developers write custom ABAP code that does the following:

  1. Reads data from standard or custom SAP tables.
  2. Uses the BigQuery data load class `/GOOG/CL_BQTR_DATA_LOAD` to replicate selected data to BigQuery. This class:

     * Uses the configuration stored in BigQuery Data Transfer configuration tables.
     * Uses the `/GOOG/CL_BIGQUERY_V2` class to perform table definition sync and data replication.
  3. Implements follow-on business logic.

  4. Handles errors and exceptions.




## Supported sources for data replication

You can use the BigQuery Data Transfer module of the BigQuery Toolkit for SAP to programmatically load data from ABAP dictionary objects such as tables, dictionary views, CDS views, CDS entities, or from any data objects with a [flat structure](https://help.sap.com/doc/abapdocu_751_index_htm/7.51/en-us/abendata_objects_structure.htm) type into BigQuery.

You can use the BigQuery Toolkit for SAP for data replication in the following ways:

  * As a plug-in within SAP enhancement frameworks such as Business Add-Ins (BAdIs), user exits, and routines. For example, the toolkit can be plugged into Business Warehouse (BW) routines to send the data being processed by BW Data Transfer Process (DTP).
  * For batch loading data from a custom ABAP program.



## Performance planning

The BigQuery Toolkit for SAP provides the final stage of the transmission of data to BigQuery by making synchronous calls to the [BigQuery streaming API](https://docs.cloud.google.com/bigquery/streaming-data-into-bigquery).

When you use the BigQuery Toolkit for SAP within your custom ABAP application, you can optimize the performance of data replication both within your SAP workload and through the BigQuery Data Transfer configurations.

### Performance tuning options with your SAP workload and custom application

To optimize the performance of your SAP workload and custom applications, consider the following options:

  * Run your SAP workload, the source system from which data is replicated to BigQuery, on Google Cloud.
  * If your SAP workload is on Google Cloud, create your BigQuery dataset in the same region as your SAP workload.
  * If you cannot run your SAP workload on Google Cloud, then do the following: 
    * Create your BigQuery dataset in a Google Cloud region that is closest to your SAP workload.
    * Connect to Google Cloud by using Cloud Interconnect.
  * Size your SAP server system [optimally](https://www.sap.com/about/benchmark/sizing/decision-tree.html) for your workload.
  * Implement [parallel processing](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/4d/909309eba36e73e10000000a15822b/content.htm?no_cache=true) to call the BigQuery Data Transfer module in multiple parallel threads to increase throughput.



Because BigQuery Toolkit for SAP provides the final stage of the transmission of data to BigQuery, its performance is influenced by various factors within your specific environment. These factors can include the following:

  * **Network infrastructure** : Bandwidth limitations, latency, and overall network stability play a significant role in replication speed and efficiency.

  * **Source systems** : The performance of your source databases, including their hardware, configuration, and current load, can impact replication performance.

  * **Data volume and change rate** : The amount of data being replicated and the frequency of changes affect the time and resources required for replication.

  * **Other components** : Firewalls, security policies, load balancers, and other infrastructure elements can all contribute to the overall performance of data replication.




You're responsible for performance testing the BigQuery Toolkit for SAP in your own environment. For optimal results, consider and optimize all relevant components of your environment.

### Performance tuning options available through the BigQuery Data Transfer configurations

The BigQuery Data Transfer configurations provide the following options to control the replication performance:

#### Data transfer chunk size

BigQuery Toolkit for SAP sends data to BigQuery as chunks of records. We recommend that you use the default chunk size with BigQuery Toolkit for SAP, which is 10,000 records. If the records in a source table contain very few fields or the fields contain very small size data values, then you can use a larger chunk size up to the maximum chunk size that BigQuery Toolkit for SAP allows, which is 50,000 records.

If the number of records in a given chunk resolves to a byte size that exceeds the BigQuery limit on the byte size for HTTP requests, you might receive either a `quotaExceeded` error or an `invalid` error. This can happen if the records in a source table contain a lot of fields or the fields contain a lot of data.

If you get an error related to chunk size, try reducing the chunk size that is specified in the mass transfer configuration for that table. Alternatively, you can enable dynamic chunk size for that table to automatically adjust the chunk size. For more information, see [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#dynamic-chunk-size).

If you have not enabled dynamic chunk size, then for SAP source tables like `MSEG`, `ACDOCA`, and `MATDOC`, which can have large records with a lot of fields per record, you might need to specify a chunk size as low as 2,000.

You can specify a chunk size by running the `/GOOG/BQTR_SETTINGS` transaction. The chunk size is specified in the **Chunk Size** field on the **Table Attributes** screen.

#### Record compression

By default, BigQuery Toolkit for SAP improves replication performance by compressing the records that it sends to BigQuery. When record compression is enabled at table level, which is the default setting, BigQuery Toolkit for SAP omits all fields that are empty in the source record from the records that are sent to BigQuery. When the record is inserted into BigQuery, the fields that were omitted from the sent data, are initialized with `null` in the target table in BigQuery.

However, if you need to replicate some empty fields with their initial values to BigQuery while still using record compression at the table level, then you can change the record compression setting for those specific fields. As a result, the empty values in the specified fields are not omitted from the sent data, and retain whatever value they are initialized in the source table.

In your [mass transfer configuration](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration#configure-connection), you can control the record compression behavior by using the **Send Uncompressed Flag** setting available at the table level and field level. The following table summarizes the record compression behavior depending on the **Send Uncompressed Flag** setting:

Send Uncompressed Flag at table level | Send Uncompressed Flag at field level | Record compression behavior  
---|---|---  
Yes | No | All fields are sent as uncompressed.  
Yes | Yes | All fields are sent as uncompressed.  
No | Yes | Only the selected fields at the field level are sent as uncompressed.  
No | No | All fields are sent as compressed.  
  
When you send the uncompressed data replication, except for date fields and timestamp fields, the empty fields retain whatever value they were initialized with in the source table. The initialized value for date and timestamp fields receive the following values:

  * **Date field initialization value:** `DATE 1970-01-01`
  * **Timestamp field initialization value:** `TIMESTAMP 1970-01-01 00:00:00 UTC`



The following screenshot shows an example of the record compression behavior:

![Diagram is described in the preceding text](https://docs.cloud.google.com/static/sap/docs/images/record-compression-example.png)

The preceding image shows the following: 

  * **Row #1** : All fields are uncompressed. The **Send Uncompressed Flag** is selected at table level.
  * **Row #2** : All fields are compressed. The **Send Uncompressed Flag** is clear at table level.
  * **Row #3** : The following fields are uncompressed: `int2_value`, `curr_value_154`, `currency`, `float_value`, and `lang_value`. For these fields, **Send Uncompressed Flag** is selected at field level.



For better performance, we recommend that you don't disable record compression by selecting **Send Uncompressed Flag** at the table level. It can have a negative impact on replication performance. If you need to send uncompressed data for only specific fields, then select **Send Uncompressed Flag** for those specific fields at the field level.

## Target table properties

When you configure replication in the BigQuery Data Transfer module of BigQuery Toolkit for SAP, you can specify settings that apply when BigQuery Toolkit for SAP creates the target table in BigQuery.

For example, you can specify the following properties for a target BigQuery table:

  * Table name
  * The default naming option for fields
  * Extra fields to capture record changes and to enable record count queries
  * Table partitioning



### Default naming options for fields

You can configure BigQuery Toolkit for SAP to create the names for the fields in the target BigQuery table either from the names of the source fields or the labels and descriptions of the source fields. The labels and descriptions are usually more informative about the contents of the field.

By default, BigQuery Toolkit for SAP uses the names of the source fields. You can change the default by specifying the **Custom Names** flag when you specify in table creation attributes in the mass transfer configuration of the `/GOOG/BQTR_SETTINGS` transaction. This specification is stored in the `/GOOG/BQTR_MASTR` configuration table.

When creating the names, BigQuery Toolkit for SAP modifies them to conform to the BigQuery naming convention.

Before the BigQuery Toolkit for SAP creates a table in BigQuery, you can edit the field names in the field mapping screen of the `/GOOG/BQTR_SETTINGS` transaction.

When the **Custom Names** flag is specified, the names that the BigQuery Toolkit for SAP is going to use when it creates the target table are shown in the **External Field Name** column of the field mapping screen.

BigQuery Toolkit for SAP creates the names in the **External Field Name** column from the _medium_ field label of each source field. If a medium field label is not specified in the source field definition, then the _short description_ for the field is used. If the short description isn't specified either, then the shortest specified label is used. If nothing is specified, then the name of the source field is used.

For more information about customizing target field names, see Customizing target field names.

### Capturing record changes and enabling record counts

To capture the type of change in the source table that triggered replication and to be able to query record counts in the BigQuery table for comparison with the record counts in the source table, specify the **Extra Fields Flag** option in the `/GOOG/BQTR_SETTINGS` transaction when you're configuring replication.

When you specify the **Extra Fields Flag** option, the following columns are added to the schema for the target BigQuery table:

Field name | Data type | Description  
---|---|---  
`operation_flag` |  `STRING` |  Identifies the type of change in the source table that triggered the load or replication of the record into BigQuery.  To count records that were inserted in replication mode, query records that have a value of `I`, `U`, or `D` in the `operation_flag` field. For an example query, see [Query the number of records inserted in replication mode](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#query-replicated-records).  To count records that were inserted in initial load mode, query records that have a value of `L` in the `operation_flag` field. For an example query, see [Query the count of records inserted in initial load mode](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#query-loaded-records).   
`is_deleted` |  `BOOLEAN` | When `true`, indicates that the source record was deleted from the source table.  To count only records in a BigQuery table that have not been deleted from the source table, use the `is_deleted` field to exclude deleted source records. For an example query, see [Query the total count of records in a BigQuery table](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#query-total-records).   
`recordstamp` |  `TIMESTAMP` |  The time when the BigQuery Toolkit for SAP sent the record to BigQuery.  To count the number of unique records in a BigQuery table, query only the most recently inserted instance of each record. For an example query, see [Query the total count of records in a BigQuery table](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#query-total-records).   
  
The current setting of the **Extra Fields Flag** option is stored in the `/GOOG/BQTR_MASTR` configuration table.

For more information about how to specify the **Extra Fields Flag** , see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration#configure-connection).

The BigQuery Toolkit for SAP doesn't automatically create primary key constraints in BigQuery based on the source SAP table definition. The toolkit replicates data into staging tables, which by design, don't include these constraints.

To maintain data integrity for reporting, you can implement a Change Data Capture (CDC) pattern by using BigQuery [`MERGE` statements](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#merge_statement) to process records from the staging table into a target table that has [informational (non-enforced) primary keys](https://docs.cloud.google.com/bigquery/docs/primary-foreign-keys) defined in its schema.

### Table partitioning

You can create BigQuery tables in one of the following ways:

  * Tables that are partitioned by either a timestamp field in the source table, which creates a _time-unit column-partitioned_ table.
  * Tables that are partitioned by the time at which the records are inserted into BigQuery, which creates an _ingestion-time partitioned_ table.



You enable partitioning by specifying a partition type in the **Partition Type** field in the `/GOOG/BQTR_TABLE` when you configure the replication properties.

The partition types that you can specify adjust the granularity of the partitioning by hour, day, month, or year.

To use a timestamp from the source table for time-unit column partitioning, specify the name of the source field in the **Partition Field** field.

To use a BigQuery insertion time for ingestion-time partitioning, you can leave **Partition Field** blank. The BigQuery Toolkit for SAP creates a field in the target table to store the insertion time.

## Target field properties

By default, BigQuery Toolkit for SAP uses the field names and data types in the SAP source table as the field names and data types in the target BigQuery.

Optionally, before the target table is created, you can customize field names or change the BigQuery data type.

### Customizing target field names

Before a table is created, you can customize target field names.

If necessary, BigQuery Toolkit for SAP modifies the custom names that you specify to conform to the BigQuery naming convention.

When you configure replication, you can view the field names in the field mapping screen of the `/GOOG/BQTR_SETTINGS` transaction. The BigQuery Toolkit for SAP stores your settings in the `/GOOG/BQTR_FIELD` configuration table.

Before a table is created in BigQuery, you can specify a custom field name by editing the generated name in the **Temporary Field Name** column of the field mapping screen. If you delete a value and leave the **Temporary Field Name** field blank, then BigQuery Toolkit for SAP uses the name of the source field for the name of that target field.

After you make any edits to the **Temporary Field Name** column, when you click **Save** , BigQuery Toolkit for SAP validates the value, applies BigQuery naming conventions as necessary, and saves the changes. You can validate a value without saving it by pressing **Enter** on your keyboard.

For more information about setting the default naming method for the target fields, see Default naming options for fields.

### Use a spreadsheet or text file to edit the BigQuery field map

Optionally, before you create a target BigQuery table, you can save the default data types, names, and descriptions of the target fields to a spreadsheet or text file. This approach lets BigQuery data engineers or administrators edit the values even if they don't have access to your SAP server.

After the values are edited, you need to convert the file and its contents to the comma-separated values (CSV) format. You can then apply the updates to the mass transfer settings by uploading the CSV file by using the custom transaction `/GOOG/BQTR_SETTINGS`.

To use a CSV file to edit the BigQuery field map, do the following:

  1. Create a spreadsheet or text file with the default field mappings.
  2. Edit the values in the spreadsheet or text file.
  3. Convert the spreadsheet or text file to CSV format.
  4. In the **BigQuery Data Transfer: Settings Maintenance** screen, upload the CSV file.



For more information about this process, see [Edit the BigQuery field map in a CSV file](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#edit-fields-in-csv).

### The BigQuery naming convention for fields

The BigQuery naming convention uses only lowercase letters, numbers, and underscores.

BigQuery Toolkit for SAP applies the BigQuery naming conventions to any input value to be used for the name of a target field.

For example, if you enter `FIELD-@#!*123` as a custom field name, then the BigQuery Toolkit for SAP changes the name to `field_123`.

For more information about the BigQuery naming convention for fields, see [Column names](https://docs.cloud.google.com/bigquery/docs/schemas#column_names).

## Data type mapping

By default, BigQuery Toolkit for SAP assigns data types to the target BigQuery fields based on the _SAP type kind_ or the _SAP data type_ of the source SAP field.

When you configure replication, you can view the data types in the field mapping screen of the `/GOOG/BQTR_SETTINGS` transaction. The BigQuery Toolkit for SAP stores your settings in the `/GOOG/BQTR_FIELD` configuration table.

Before the BigQuery Toolkit for SAP creates a table in BigQuery, you can change the default data type specification to a different BigQuery data type in the **External Data Element** column of the field mapping screen.

**Booleans and timestamps:** To accurately reflect the data types of booleans and timestamps in the target table, before the target table is created, you need to manually change their target data types to `BOOLEAN` and `TIMESTAMP`, respectively. For more information, see Data types that require special handling.

### Data types that require special handling

To ensure accuracy and compatibility with the target BigQuery tables, several SAP data types require special handling or conversion during the replication process.

While the BigQuery Toolkit for SAP automatically handles some of these conversions for you, others require your attention and manual configuration.

You need to manually handle conversions for the following data types:

#### Booleans

For booleans, SAP uses the data type `CHAR`. By default, the BigQuery Toolkit for SAP maps this data type to the `STRING` data type in the target BigQuery table.

Consequently, when you configure replication for booleans by using the `/GOOG/BQTR_SETTINGS` transaction, you must change the default data type assignment for boolean fields from `STRING` to `BOOLEAN` in the field mapping screen.

#### Timestamps

For timestamps, SAP uses the data types `P` (packed decimal) or `DEC` (decimal). By default, BigQuery Toolkit for SAP maps these data types to `NUMERIC` in the target BigQuery table.

Consequently, for timestamps, when you configure replication by using the `/GOOG/BQTR_SETTINGS` transaction, you must change the default data type assignment for timestamp fields from `NUMERIC` to `TIMESTAMP` or `TIMESTAMP (LONG)` in the field mapping screen.

#### `X` SAP type kind

The `X` SAP type kind is a hexadecimal and is represented by the `RAW`, `RAWSTRING`, or `LRAW` SAP data types. By default, BigQuery Toolkit for SAP maps these data types to `STRING` in the source BigQuery table.

If you need a source field with the `X` SAP type kind to map to `BYTES` instead, you must change the default data type assignment for the field in the field mapping screen of the `/GOOG/BQTR_SETTINGS` transaction.

The `X` SAP type kind is also sometimes used in SAP to represent integers. In this case, BigQuery Toolkit for SAP checks the data type of the source field for one of the SAP data types for integers, `INT1`, `INT2`, `INT4`, `INT8` and assigns the `INTEGER` data type in the target BigQuery table.

#### `y` SAP type kind

The `y` SAP type kind is a byte string and is represented by the `RAW`, `RAWSTRING`, or `LRAW` SAP data types. By default, BigQuery Toolkit for SAP maps these data types to `STRING` in the source BigQuery table.

If you need a source field with the `y` SAP type kind to map to `BYTES` instead, you need to change the default data type assignment for the field in the field mapping screen of the `/GOOG/BQTR_SETTINGS` transaction.

### Default data type mapping

The following table shows the default data type conversion of the BigQuery Toolkit for SAP:

SAP type kind | SAP data type | BigQuery data type | Notes  
---|---|---|---  
`b` (1 byte integer)  
`s` (2 byte integer)  
`I` (4 byte Integer)  
`8` (8 byte integer)  | `INT1`  
`INT2`  
`INT4`  
`INT8` | `INTEGER` |   
`F` (float)  | `FLTP` | `FLOAT` |   
`P` (packed)  | `CURR`  
`DEC`  
`QUAN` | `NUMERIC` | By default, the SAP type kind `P` is mapped to the BigQuery data type `NUMERIC` and converted to a number in the external format.  
`a` (decimal floating number, 16 places)  | `DECFLOAT16`  
| `NUMERIC` |   
`e` (decimal floating number, 16 places)  | `DECFLOAT34`  
| `NUMERIC` |   
`N` (numeric) | `NUMC` | `STRING` |   
`X` (hexadecimal)  
`y` (byte string)  | `RAW`  
`RAWSTRING`  
`LRAW` | `STRING` | If the SAP type kind is `X`, but the data-type name covers pattern `'INT*'` (`INT1`, `INT2`, `INT4`), a source data element is replaced with a new data element `TYPINT8` with `TYPEKIND '8'`, which is mapped to the BigQuery data type `INTEGER`.  
`C` (character)  
`g` (character string)  
`?` (csequence)  
`&` (clike)  | `CHARSTRING` | `STRING` |   
`D` (date) | `DATS` | `DATE` |   
`T` (time) | `TIMS` | `TIME` |   
**Note:** While BigQuery Toolkit for SAP maps `LRAW` fields to `STRING` by default, the toolkit does not support replication for tables where an `LRAW` column is part of the primary key. This is a standard limitation inherited from SAP Embedded BW, which prohibits `RAW` and `LRAW` types in key fields or indexes. For more information about `RAW` and `LRAW` data types in SAP, see [Defining Keys](https://help.sap.com/docs/SAP_BW4HANA/107a6e8a38b74ede94c833ca3b7b6f51/eda398dc0f6d49ff9acef7a27246704a.html?version=2021.06).

## Community resources

To accelerate the implementation of BigQuery Toolkit-based applications within SAP S/4HANA systems that use Embedded BW, you can use the [open-source generation tools available on GitHub](https://github.com/googlecloudplatform/abap-sdk-bigquery-toolkit-samples).

## Get support

Google Cloud offers support for issues and questions related to the installation, configuration, operation, and maintenance of the BigQuery Toolkit for SAP.

For issues originating from SAP-managed components or third-party software, Google Cloud Customer Care makes its best effort to identify the root cause. To resolve these issues, contact the respective vendor or support provider.

To troubleshoot problems with the BigQuery Toolkit for SAP, see [Troubleshooting the BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-troubleshooting).

If you need help resolving problems with the on-premises or any cloud edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ on-premises or any cloud edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
