---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations/
title: Manage BigQuery Toolkit for SAP operations \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:34.247076+00:00
---

# Manage BigQuery Toolkit for SAP operations  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Manage BigQuery Toolkit for SAP operations Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-toolkit-for-sap-operations)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations)



As an SAP administrator or developer, you can perform operational tasks for the BigQuery Toolkit for SAP to manage data replication from your SAP systems to BigQuery. These tasks include configuring replication settings, validating data transfer, editing field mappings, managing schema changes, and implementing custom code exits.

## Dynamic chunk size

If you come across errors because the byte size of the chunks exceeds the maximum byte size for HTTP requests that BigQuery accepts, then you need to reduce the byte size manually by reducing the chunk size. The dynamic chunk size feature lets you automatically reduce the chunk size and retry replication to BigQuery when the byte size of a chunk exceeds the maximum byte size for HTTP requests that BigQuery accepts. Dynamic chunk size helps you prevent most replication failures due to exceeding byte size of a request. You might receive an error only if the chunk size reaches 1, but the byte size remains more than the BigQuery limit on the number of bytes in each HTTP request.

You enable dynamic chunk size in the data transfer configuration for a table by using transaction `/GOOG/BQTR_SETTINGS`. Dynamic chunk size is an optional setting. For information about how to enable dynamic chunk size, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration#configure-connection).

When the BigQuery Toolkit for SAP reduces the chunk size, the following information message is returned to the calling ABAP application in parameter `et_return`:

`Dynamic chunking triggered. Chunk size reduced from INITIAL_CHUNK_SIZE_VALUE to FINAL_REDUCED_CHUNK_SIZE_VALUE`

## Transport mass transfer settings to production

To transport the BigQuery Toolkit for SAP mass transfer settings to production, you first export the settings from a development system, and then import them into the production system.

You can, optionally, import two separate parts of the settings of a mass transfer into production:

  * The client key settings from the `/GOOG/CLIENT_KEY` table, which can be accessed by using the `SM30` transaction.
  * The BigQuery Toolkit for SAP mass transfer settings, which can be accessed by using the `/GOOG/BQTR_SETTINGS` transaction.

**Note:** Before you move mass transfer settings to production, validate the settings in a QA or sandbox environment.

### Export mass transfer settings from a development system

In your SAP development system, export each part of the mass transfer settings:

  1. Export the BigQuery Toolkit for SAP mass transfer settings:

     1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

     2. Click **ABAP SDK for Google Cloud > Basic Settings > BigQuery Data Transfer: Settings Maintenance**.

     3. In the **Settings Table** field, select **Mass Transfer**.

     4. Select the mass transfer records that you're transporting to production.

     5. Click **Transport Mass Transfer**.

     6. In the **Prompt for Workbench request** , enter the transport request number and click the **Continue** icon. For each selected mass transfer record, the settings from the following custom configuration tables are included in the transport:

        * `/GOOG/BQTR_MASTR`
        * `/GOOG/BQTR_TABLE`
        * `/GOOG/BQTR_FIELD`

The mass transfer settings are saved to a transport request.

  2. Export the client key settings by manually including the contents of the `/GOOG/CLIENT_KEY` table in the transport request.

  3. Save the files to your local workstation.




### Import mass transfer settings into a production system

Import the transport request that contains the mass transfer settings.

In the SAP production system, import each part of the mass transfer settings:

  1. In SAP GUI, import the transport request that contains the mass transfer settings.

  2. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  3. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.

  4. Update the client key settings as necessary for the production environment.

  5. Click **ABAP SDK for Google Cloud > Basic Settings > BigQuery Data Transfer: Settings Maintenance**.

  6. Verify that the correct mass transfers are displayed in the **Mass Transfers** screen.

  7. In the subsequent **Tables** and **Fields** settings screens, update other values for the table and field mapping as necessary for the production environment.

  8. Test the configuration by running your data load program that calls BigQuery Toolkit for SAP.




## View the BigQuery Data Transfer settings

To view the mass transfer settings of BigQuery Data Transfer module, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > BigQuery Data Transfer: Settings Display**.




Alternatively, you can view the settings by using the `/GOOG/BQTR_SETTINGS` transaction.

## Replication validation

When you specify the **Extra Fields Flag** option in your mass transfer configuration, the BigQuery Toolkit for SAP adds extra columns to the table schema in BigQuery. These columns capture the following details:

  * Information about the type of change that triggered replication for each record.
  * A timestamp indicating when the BigQuery Toolkit for SAP received the portion containing that record.



By using the information in these columns, you can validate the replication process, ensuring data integrity and consistency between your SAP system and BigQuery. You can use the change types and the timestamp to query the following types of record counts:

  * The number of records that are loaded into a BigQuery table during an initial load.
  * The number of records replicated on a specified day into a BigQuery table.
  * The total number of unique records in a BigQuery table.



To get these counts, you can query the BigQuery table directly by submitting SQL queries in the Google Cloud console.

For an overview of the **Extra Fields Flag** , see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#fields-for-changes-and-counts).

### SQL queries for record counts

You can run SQL queries to check the record counts in your BigQuery tables by using the BigQuery **SQL Editor** page in the Google Cloud console.

**Required table setting for record counts** : The SQL queries in this section require that you specify the **Extra Fields Flag** when you specify the BigQuery table options during replication configuration. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#fields-for-changes-and-counts). 

#### Query the count of records inserted in initial load mode

When a BigQuery table schema includes the optional `operation_flag` column, records that are inserted into the table in initial load mode include the `L` operation flag.

To get the count of records that were received by BigQuery during an initial load, execute the following query:
    
    
    SELECT COUNT(*)
      FROM
          `PROJECT.DATASET.TABLE`
      WHERE operation_flag = 'L'

#### Query the number of records inserted in replication mode

When a BigQuery table schema includes the optional `operation_flag` column, records that are inserted into the table in replication mode include one of the following operation flags:

  * **`I`** : the record was inserted into the source table.
  * **`D`** : the record was deleted from the source table.
  * **`U`** : the record was updated in the source table.



To get the count of records that were received by BigQuery in replication mode, run the following query:
    
    
    SELECT COUNT(*)
      FROM
          `PROJECT.DATASET.TABLE`
      WHERE operation_flag = 'I' | 'D' | 'U'

#### Query the total count of records in a BigQuery table

When a BigQuery table schema includes the optional `recordstamp` column, the corresponding `recordstamp` field of each record that is inserted into the table contains a timestamp that indicates when the record was sent by BigQuery Toolkit for SAP to BigQuery.

To get a total count of the records in a BigQuery table that you can compare with the total count of records in a source table, you can use the `recordstamp` and `is_deleted` fields to count the unique records in the BigQuery table that have not been deleted from the source table.

If the source table is being actively updated or replication is active when you query the records, the count of records in the source and target tables might not match exactly.

To get the current count of unique records in the BigQuery target table, run the following query:
    
    
    SELECT COUNT(*)
      FROM (
        SELECT
          *,
          ROW_NUMBER() OVER (PARTITION BY KEY_FIELD_1, ..., KEY_FIELD_N ORDER BY recordstamp DESC) row_num
        FROM
          `PROJECT.DATASET.TABLE` )
      WHERE row_num = 1 AND is_deleted = false

## Edit the BigQuery field map in a CSV file

The following sections describe how to export the default field mapping so that data engineers or BigQuery administrators can edit the target field values without the need for access to the SAP system.

When editing the target field values, adhere to the following rules:

  * Don't modify values in the **SAP Data Source Name** and **SAP Field Name** columns.
  * In the **Send Uncompressed Flag** column, to enable record compression, mark the field with only an `X`. Otherwise, leave the field blank.



### Create a spreadsheet or text file of the default field mappings

To create a CSV file for editing outside of your SAP server, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > BigQuery Data Transfer: Settings Maintenance**.

  3. In the **BigQuery Data Transfer Settings Maintenance** screen, specify the following values:

     * In the **Settings Table** field, specify **Fields**.
     * In the **Mass Transfer Key** field, specify the ID of the mass transfer that you're updating.
     * In the **Table Name** field, either leave the field blank to work with all fields from all tables or specify a table name to work with a specific table.
     * Leave all other fields blank.
  4. Click the **Execute** icon. The **BigQuery Data Transfer Settings Maintenance - Fields** screen displays.

  5. On the **BigQuery Data Transfer Settings Maintenance - Fields** screen, hide all columns except for those in the following list by right-clicking on the column headings and selecting **Hide** from the drop-down menu:

     * SAP Data Source Name
     * SAP Field Name
     * External Data Element
     * External Field Name
     * Field Description
     * Send Uncompressed Flag
  6. With the six remaining columns displayed, click the **Export** icon.

  7. From the **Export** menu, select one of the following options:

     * **Spreadsheet**
     * **Local file**. For ease of converting the file contents to CSV format, we recommend saving the file in the **Text with tabs** format.
  8. Save the default field mappings by clicking the **Checkmark** icon.




### Convert the spreadsheet or text file to CSV format

To upload edited field mappings by using the custom transaction `/GOOG/BQTR_SETTINGS`, the field mappings must be in CSV format.

If you're using a spreadsheet, save the spreadsheet as a CSV file before you upload the file.

If you're using a local file in a tab-separated format or any other format, you need to modify the file to conform to CSV format.

For example:
    
    
    SAP Table,SAP Field Name,External Data Element,External Field Name,Field Description, Send Uncompressed Flag
    SAP_TABLE_NAME,SAP_FIELD_NAME1,BIGQUERY_DATA_TYPE,BIGQUERY_FIELD_NAME1,BIGQUERY_FIELD_DESCRIPTION1, SEND_UNCOMPRESSED_FLAG1
    SAP_TABLE_NAME,SAP_FIELD_NAME2,BIGQUERY_DATA_TYPE,BIGQUERY_FIELD_NAME2,BIGQUERY_FIELD_DESCRIPTION2, SEND_UNCOMPRESSED_FLAG2
    SAP_TABLE_NAME,SAP_FIELD_NAME3,BIGQUERY_DATA_TYPE,BIGQUERY_FIELD_NAME3,BIGQUERY_FIELD_DESCRIPTION3, SEND_UNCOMPRESSED_FLAG3
    

### Upload the CSV file

To upload an edited CSV file, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > BigQuery Data Transfer: Settings Maintenance**.

  3. In the **BigQuery Data Transfer: Settings Maintenance** screen, specify the following values:

     * In the **Settings Table** field, specify **Fields**.
     * In the **Mass Transfer Key** field, specify the ID of the mass transfer that you're updating.
     * Select the **Upload from file** checkbox.
  4. Click the **Execute** icon. The **Select File to Upload** dialog opens.

  5. In the **Select File to Upload** dialog, select the CSV file that contains the edited field values.

  6. Click **Open**.

  7. If you receive a security warning, click **Allow**. The file loads and the modified values in the file appear on the applicable rows in the **BigQuery Settings Maintenance - Fields** screen.

  8. Click the **Save** icon.

  9. To confirm the values are applied, compare the values in the CSV file with the values that are displayed in your SAP system.




## Handling errors in the source data

When the BigQuery streaming API receives a chunk of records from BigQuery Toolkit for SAP, it checks for data errors before inserting any records into the BigQuery table.

You can control how the BigQuery API and the BigQuery Toolkit for SAP respond when data errors are found by specifying the following flags in mass transfer settings:

  * The `Skip Invalid Records` (`SKIP`) flag
  * The `Break at First Error Flag` (`BREAK`) flag



### The `SKIP` flag

If you specify the `SKIP` flag, when the BigQuery API receives a chunk of records and finds a record with a data error, then the BigQuery API discards, or _skips_ , the record with the error and continues inserting all other records from the chunk into the BigQuery table.

If you don't specify the `SKIP` flag, when BigQuery finds a record with a data error, BigQuery discards the entire chunk without inserting any records from it into the BigQuery table. This behavior is the default.

Specifying the `SKIP` flag is best for development and QA environments and is not recommended for production environments.

You can specify the `SKIP` flag in the `/GOOG/BQTR_SETTINGS` transaction when you're configuring replication. The specification is stored in the `/GOOG/BQTR_MASTR` configuration table.

To see how `SKIP` specifications interact with `BREAK` specifications, see Matrix table for `SKIP` and `BREAK` interactions.

### The `BREAK` flag

If you specify the `BREAK` flag, when BigQuery Toolkit for SAP is notified by the BigQuery API that a data error was found in a record, BigQuery Toolkit for SAP stops sending records to BigQuery and terminates the replication job. This behavior is the default.

If you don't specify the `BREAK` flag, when BigQuery Toolkit for SAP is notified by BigQuery that a data error was found in a record, BigQuery Toolkit for SAP continues sending records to BigQuery by sending the next chunk and the replication job continues.

Specifying the `BREAK` flag is recommended in production environments.

You can specify the `BREAK` flag in the `/GOOG/BQTR_SETTINGS` transaction when you're configuring replication. When you create a new mass transfer key, the `BREAK` flag is enabled by default.

The specification is stored in the `/GOOG/BQTR_MASTR` configuration table.

To see how `BREAK` specifications interact with `SKIP` specifications, see Matrix table for `SKIP` and `BREAK` interactions.

### Matrix table for `SKIP` and `BREAK` interactions

You can configure BigQuery Data Transfer module to handle data errors in the following ways:

`SKIP` flag | `BREAK` flag | Behavior  
---|---|---  
FALSE | TRUE |  BigQuery discards the current chunk of records without inserting any records from the current chunk into the BigQuery table.  BigQuery Toolkit for SAP sends no more chunks of records from the current portion and terminates the replication job.  This is the default and recommended setting.   
FALSE | FALSE |  BigQuery discards the current chunk of records without inserting any records from the current chunk into the BigQuery table.  BigQuery Toolkit for SAP sends any remaining chunks of records from the current portion and retrieves the next portion. BigQuery Toolkit for SAP does not terminate the replication job.   
TRUE | TRUE |  BigQuery discards only the record that contains the error and inserts the rest of the records in the current chunk into the BigQuery table.  BigQuery Toolkit for SAP sends no more chunks of records from the current portion and terminates the replication job.   
TRUE | FALSE |  BigQuery discards only the record that contains the error and inserts the rest of the records in the current chunk into the BigQuery table.  BigQuery Toolkit for SAP sends any remaining chunks of records from the current portion and retrieves the next portion. BigQuery Toolkit for SAP does not terminate the replication job.   
  
### SAP dictionary object structure changes

This section explains how to handle changes to the definition of your dictionary objects in SAP.

#### Add a column to dictionary object

If you're adding a column to a dictionary object, do the following:

  1. Stop your custom data replication application that uses the data load class `/GOOG/CL_BQTR_DATA_LOAD`.
  2. Add a new column to the dictionary object in SAP.
  3. Optionally, update the field level mapping in the transaction `/GOOG/BQTR_SETTINGS`.
  4. Restart your custom data replication application.
  5. Validate the replication result in BigQuery.



#### Delete a column from dictionary object

To delete an existing column from a dictionary object, do the following:

  1. Stop your custom data replication application that uses the data load class `/GOOG/CL_BQTR_DATA_LOAD`.
  2. Delete a column from the dictionary object.
  3. In BigQuery, delete the column from the target BigQuery table. For more information about the steps to delete a column from an existing table, see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/managing-table-schemas#delete_a_column).
  4. Optionally, update the field level mapping in the transaction `/GOOG/BQTR_SETTINGS`.
  5. Restart your custom data replication application.
  6. Validate the replication result in BigQuery.



#### Change the data type of an existing column

When you change the data type of an existing column in SAP dictionary object, you need to follow specific steps depending on whether you're changing the data type to a compatible or non-compatible data type with the target BigQuery table.

A data type is compatible with the data type in the target BigQuery table when the existing data type and new data type of an existing column map to the same data type in the target BigQuery table. For example, if the data type of a column is changed from `INT1` to `INT2` in a source table, then both the data types are compatible with the data type `INTEGER` in the target BigQuery table.

For more information about data type mapping in the BigQuery Data Transfer module, see [Data type mapping](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#data-type-mapping).

#### Change the data type to a compatible data type

To change the data type of an existing column to a compatible data type, do the following:

  1. Optionally, stop your custom data replication application that uses the data load class `/GOOG/CL_BQTR_DATA_LOAD`.
  2. Change the data type to a compatible data type in the source system. 
  3. Optionally, update the field level mapping in the transaction `/GOOG/BQTR_SETTINGS`.
  4. If you had stopped the custom data replication application, then restart the application. 
  5. Validate the replication result in BigQuery.



#### Change the data type to a non-compatible data type

To change the data type of an existing column to a non-compatible data type, do the following:

  1. Stop your custom data replication application that uses the data load class `/GOOG/CL_BQTR_DATA_LOAD`.
  2. In BigQuery, delete the target table.
  3. Change the data type in the source system.
  4. Optionally, update the field level mapping in the transaction `/GOOG/BQTR_SETTINGS`.
  5. Start your custom data replication application. As needed, you might need to start an initial load of existing data.



## Enhancement exits

The BigQuery Toolkit for SAP provides several enhancement points in its code where an ABAP developer can insert code to add custom features.

**Important:** You're responsible for any custom code written within the implementation of these enhancement points. We strongly recommend that you test your custom code thoroughly in a non-production environment before deploying it to production. Google Cloud does not provide support for custom features.

### Classes

The following table lists the functions that the enhancement points support, the methods, and the class that contains the enhancement point.

Function | Class | Method | Spot | Option  
---|---|---|---|---  
Update the mapping for a field, such as the external field name, and the data type. | `/GOOG/CL_BQTR_DATA_LOAD_BASE` | `CREATE_FLD_MAPPINGS` | `/GOOG/ES_BQTR_DATA_LOAD_BASE` | `/GOOG/UPDATE_FIELD_MAPPING`  
Update the mapping for the field table by adding or removing fields.  | `/GOOG/CL_BQTR_DATA_LOAD_BASE` | `CREATE_FLD_MAPPINGS` | `/GOOG/ES_BQTR_DATA_LOAD_BASE` | `/GOOG/UPDATE_FIELD_MAPPINGS`  
Change the value of a source field before the field is converted to a target field. | `/GOOG/CL_BQTR_DATA_LOAD` | `FILL_TARGET_RECORDS` | `/GOOG/ES_BQTR_DATA_LOAD` | `/GOOG/CHANGE_SOURCE_FIELD`  
After a source field is converted to a target field in the target table, change the value of the target field. | `/GOOG/CL_BQTR_DATA_LOAD` | `FILL_TARGET_RECORDS` | `/GOOG/ES_BQTR_DATA_LOAD` | `/GOOG/FILL_TARGET_FIELD`  
Add a field to the target table that does not exist in the source table during the source-to-target table conversion. | `/GOOG/CL_BQTR_DATA_LOAD` | `FILL_TARGET_RECORDS` | `/GOOG/ES_BQTR_DATA_LOAD` | `/GOOG/FILL_EXTRA_FIELD`  
Prepare a BigQuery schema field before the BigQuery table is created. | `/GOOG/CL_BQTR_CLIENT_BQ_BASE` | `PREP_BQ_TABLE_SCHEMA` | `/GOOG/ES_BQTR_CLIENT_BQ` | `/GOOG/PREPARE_SCHEMA_FIELD`  
In case of HTTP errors originating on the BigQuery server side, for troubleshooting the issue, you can collect logging data after the HTTP calls to the BigQuery API.  | `/GOOG/CL_BQTR_CLIENT_BQ_REPL` | `INSERT_TABLEDATA` | `/GOOG/ES_BQTR_CLIENT_BQ_REPL` | `/GOOG/LOG_INSERT_ERROR`  
  
### Reports

The following table lists the functions that the enhancement points support, the methods, and the reports that contain the enhancement point.

Function | Report | Method | Spot | Option  
---|---|---|---|---  
To add authority checks to the BigQuery Data Transfer settings program. | `/GOOG/R_BQTR_SETTINGS` | `AUTHORITY_CHECK` | `/GOOG/ES_BQTR_SETTINGS` | `/GOOG/AUTHORITY_CHECK`  
  
## Advanced settings

Optionally, you can modify the advanced settings for BigQuery Toolkit for SAP. We recommend that you modify the advanced settings parameters only after a comprehensive analysis and impact of new values on performance. You're responsible for ensuring that the new advanced settings for BigQuery Toolkit for SAP don't cause failures and performance issues.

**Warning:** Don't modify the advanced settings for BigQuery Toolkit for SAP when an initial load is in progress.

Advanced settings for BigQuery Toolkit for SAP are applied at the system level and are common for all mass transfer keys. If the advanced settings parameters are not modified, then BigQuery Toolkit for SAP works with the default settings.

To modify advanced settings parameters, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > BigQuery Data Transfer: Settings Maintenance**.

  3. From the **Settings Table** drop-down menu, select **Parameters**.

  4. Click the **Execute** icon. The **BigQuery Data Transfer Settings Maintenance - Parameters** screen displays.

  5. Click the **Insert Row** icon.

  6. In the displayed row, specify the following settings:

     1. In the **Parameter Name** field, enter the name of the parameter. The parameter description is automatically populated.
     2. In the **Parameter Value** field, enter a value.

To know about the Advanced settings parameters, see Advanced settings parameters.

  7. Click **Save**.

Your advanced settings are stored as a record in the `/GOOG/BQ_PARAM` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.




### Advanced settings parameters

The following table shows the advanced settings parameters for the BigQuery Toolkit for SAP.

**Parameter name** | **Description** | **Default value** | **Valid value**  
---|---|---|---  
`CHUNK_SIZE_DEF` | This setting is the default chunk size the BigQuery Toolkit for SAP supports.  
If a chunk size is not maintained in the settings, the default chunk size is used. | 10,000 | The value must be within the [BigQuery Quota limits](https://docs.cloud.google.com/bigquery/quotas).   
`PERC_REDUC_DEF` | The chunk size percentage reduction.  
If dynamic chunk size is enabled, the chunk size is reduced by this percentage until an ideal chunk size is reached and the data in the chunk is transferred to BigQuery successfully. | 50 | The value must be from 1 to 99.  
  
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
