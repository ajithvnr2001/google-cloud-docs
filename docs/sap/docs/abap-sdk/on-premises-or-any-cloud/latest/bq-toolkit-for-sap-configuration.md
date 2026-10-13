---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration/
title: Install and configure the BigQuery Toolkit for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:33.648539+00:00
---

# Install and configure the BigQuery Toolkit for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install and configure the BigQuery Toolkit for SAP Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-toolkit-for-sap-configuration)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration)



This document describes how to install and configure the BigQuery Toolkit for SAP.

## Install the BigQuery Toolkit for SAP

When you install the version 1.9 of the on-premises or any cloud edition of ABAP SDK for Google Cloud, the BigQuery Toolkit for SAP is installed for you by default. For information about the installation steps, see [Install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

If you're already using version 1.8 or earlier of the on-premises or any cloud edition of ABAP SDK for Google Cloud, then you must update your SDK to the latest version to get the BigQuery Toolkit for SAP. For more information, see [Update ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#abap-sdk-update).

## Enable the BigQuery API

You must enable the BigQuery API in your Google Cloud project. For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).

## Set up authentication

Once you set up authentication to access Google Cloud APIs in your on-premises or any cloud edition of ABAP SDK for Google Cloud, the BigQuery Toolkit for SAP uses the same authentication method to access the BigQuery API. For information about how to set up authentication in the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [Authentication overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

Make sure the service account configured in ABAP SDK for Google Cloud client key configuration has the following roles:

  * BigQuery Data Editor
  * BigQuery Job User



Make a note of the client key that you've created as part of the authentication setup. You use this client key when configuring the BigQuery Data Transfer configuration module of the BigQuery Toolkit for SAP in your SAP system.

## Create a BigQuery dataset

To create a BigQuery dataset, your user account must have the proper IAM permissions for BigQuery. For more information, see [Required permissions](https://docs.cloud.google.com/bigquery/docs/datasets#required_permissions).

To create a BigQuery dataset, do the following:

  1. In the Google Cloud console, go to the BigQuery page:

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Next to your project ID, click the **View actions** icon, more_vert, and then click **Create dataset**.

![Create dataset](https://docs.cloud.google.com/static/sap/docs/images/bqc4sap-dataset-create.png)

  3. In the **Dataset ID** field, enter a unique name. For more information, see [Name datasets](https://docs.cloud.google.com/bigquery/docs/datasets#dataset-naming).




For more information about creating BigQuery datasets, see [Creating datasets](https://docs.cloud.google.com/bigquery/docs/datasets).

## Configure the BigQuery Data Transfer module

The BigQuery Data Transfer module of the BigQuery Toolkit for SAP lets you build a data pipeline from your SAP system to BigQuery. In this process, you create a mass transfer configuration where you can specify which SAP data sources to replicate, map fields between your SAP and BigQuery tables, and optimize performance by configuring data replication settings.

### Select the initial mass transfer options

Select the part of the mass transfer configuration that you need to edit.

**Tip:** To access the **BigQuery Data Transfer: Settings Maintenance** screen in SAP GUI, you can execute the transaction code `/GOOG/BQTR_SETTINGS` preceded by `/n`.

To select the part of the mass transfer configuration, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > BigQuery Data Transfer: Settings Maintenance**.

  3. From the **Settings Table** drop-down menu, select **Mass Transfers**.

For a new mass transfer configuration, leave the **Mass Transfer Key** field blank.

  4. Click the **Execute** icon. The **BigQuery Data Transfer Settings Maintenance - Mass Transfers** screen displays.




### Specify table creation and other general attributes

In the initial section of a BigQuery mass transfer configuration, you identify the mass transfer configuration and specify the associated client key, as well as certain properties related to the creation of the target BigQuery table.

Your SAP server saves the mass transfer configuration as a record in the `/GOOG/BQTR_MASTR` custom configuration table.

The fields that you specify in the following steps are required for a mass transfer configuration.

To specify table attributes, do the following:

  1. In the **BigQuery Data Transfer Settings Maintenance - Mass Transfers** screen, click the **Append Row** icon.

  2. In the displayed row, specify the following settings:

     1. In the **Mass Transfer Key** field, define a name for this transfer. This name becomes the primary key of the mass transfer.
     2. To use the labels or short descriptions of the source fields as the names for the target fields in BigQuery, click the **Use Custom Names Flag** checkbox. For more information about field names, see [Default naming options for fields](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#default-field-names).
     3. To store the type of change that triggered an insert and to enable the validation of record counts between the source table, SAP server statistics, and the BigQuery table, select the **Extra Fields Flag** checkbox.

When this flag is set, the BigQuery Toolkit for SAP adds columns to the BigQuery table schema. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#fields-for-changes-and-counts).

     4. To stop sending data when a record with a data error is encountered, the **Break at First Error Flag** checkbox is checked by default. We recommend leaving this checked. For more information, see [The BREAK flag](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#break-flag).

     5. Optionally, to automatically reduce the chunk size when the byte size of a chunk exceeds the maximum byte size for HTTP requests that BigQuery accepts, click the **Dynamic Chunk Size Flag** checkbox. For more information about dynamic chunk size, see [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#dynamic-chunk-size).

     6. When a record with a data error is encountered, to skip the record and continue inserting records into the BigQuery table, click the **Skip Invalid Records Flag** checkbox. We recommend leaving this unchecked. For more information, see [The SKIP flag](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#skip-flag).

     7. In the **Google Cloud Key Name** field, enter the name of the corresponding client key configuration.

BigQuery Toolkit for SAP retrieves the Google Cloud project identifier from the client key configuration.

     8. In the **BigQuery Dataset** field, enter the name of the target BigQuery dataset that you created in the section Create a BigQuery dataset.

     9. In the **Is Setting Active Flag** field, enable the mass transfer configuration by clicking the checkbox.

     10. Click **Save**.

A mass transfer record is appended in the `/GOOG/BQTR_MASTR` table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.

     11. Click **Display Table**.

The new mass transfer record is displayed followed by the table attribute entry panel.




### Specify table attributes

You can specify table attributes, such as table name and table partitioning, as well as the number of records to include in each transmission or chunk that is sent to BigQuery.

The settings that you specify are stored as a record in the `/GOOG/BQTR_TABLE` configuration table.

These settings are optional for a mass transfer configuration.

To specify table attributes, do the following:

  1. Click the **Append row** icon.

  2. In the **SAP Data Source Name** field, enter the name of the source SAP dictionary objects such as tables, dictionary views, CDS views, or CDS entities.

**Note:** For CDS views, the **SAP Data Source Name** is the name of the underlying SQL view, which is defined in the DDL source of the CDS view. For standard SAP tables, dictionary views, and CDS view entities, the **SAP Data Source Name** is the object's name itself.
  3. In the **External Table Name** field, enter the name of the target BigQuery table. If the target table doesn't already exist, the BigQuery Toolkit for SAP creates the table with this name. For the BigQuery naming conventions for tables, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming).

  4. To send uncompressed data for all fields in a table, select **Send Uncompressed Flag**. With this setting enabled, the BigQuery Toolkit for SAP replicates any empty fields in the source records with the values that the fields are initialized with in the source table. For better performance, don't select this flag.

If you need to send uncompressed data for only specific fields, then don't select **Send Uncompressed Flag** at the table level. Instead, select **Send Uncompressed Flag** for those specific fields at field level. This option lets you retain the initial values of specific fields when replicating data to BigQuery, even if you're compressing the rest of the table data. For information about how to modify record compression at field level, see Change record compression at field level.

For more information about the record compression behavior, see [Record compression](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#record-compression).

  5. Optionally, in the **Chunk Size** field, specify the maximum number of records to include in each chunk that is sent to BigQuery. We recommend that you use the default chunk size with BigQuery Toolkit for SAP, which is 10,000 records. If you need to, you can increase the chunk size up to 50,000 records, which is the maximum chunk size that BigQuery Toolkit for SAP allows.

If the source records have a large number of fields, the number of fields can increase the overall byte size of the chunks, which can cause chunk errors. If this occurs, try reducing the chunk size to reduce the byte size. For more information, see [Data transfer chunk size](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#data-transfer-chunk-size). Alternatively, to automatically adjust the chunk size, enable dynamic chunk size. For more information, see [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#dynamic-chunk-size).

  6. Optionally, in the **Partition Type** field, specify an increment of time to use for partitioning. Valid values are `HOUR`, `DAY`, `MONTH`, or `YEAR`. For more information, see [Table partitioning](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#table_partitioning).

  7. Optionally, in the **Partition Field** field, specify the name of a field in the target BigQuery table that contains a timestamp to use for partitioning. When you specify **Partition Field** , you must also specify **Partition Type**. For more information, see [Table partitioning](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#table_partitioning).

  8. In the **Is Setting Active Flag** field, enable the table attributes by clicking the checkbox. If the **Is Setting Active Flag** box is not checked, BigQuery Toolkit for SAP creates the BigQuery table with the name of the SAP source table, the default chunk size, and no partitioning.

  9. Click **Save**.

Your attributes are stored as a record in the `/GOOG/BQTR_TABLE` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.

  10. Click **Display Fields**.

The new table attribute record is displayed, followed by the field mapping entry panel.




### Customize the default field mapping

If the source SAP table contains timestamp fields or booleans, change the default data type mapping to accurately reflect the data type in the target BigQuery table.

You can also change other data types, as well as the names that are used for target fields.

You can edit the default mapping directly in the SAP GUI or you can export the default mapping to a spreadsheet or a text file so that others can edit the values without requiring access to your SAP server.

For more information about the default field mapping and the changes you can make, see [Field mapping](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#data-type-mapping).

To customize the default mapping for the target BigQuery fields, do the following:

  1. In the **BigQuery Data Transfer Settings Maintenance - Fields** screen, display the default field mappings for the mass transfer you're configuring.

  2. Edit the default target data types in the **External Data Element** column as needed. In particular, change the target data type for the following data types:

     * **Timestamps.** Change the default target data type from `NUMERIC` to `TIMESTAMP` or `TIMESTAMP (LONG)`.
     * **Booleans.** Change the default target data type from `STRING` to `BOOLEAN`.
     * **Hexadecimals.** Change the default target data type from `STRING` to `BYTES`.

To edit the default data type mapping:

     1. On the row of the field that you need to edit, click the **External Data Element** field.
     2. In the dialog for data types, select the BigQuery data type that you need.
     3. Confirm your changes, and then click **Save**.
  3. If you specified the **Custom Names** flag in the **BigQuery Data Transfer Settings Maintenance** screen, edit the default target field names in the **Temporary Field Name** column as needed.

The values that you specify override the default names that are shown in the **External Field Name** column.

  4. Edit the default target field descriptions in the **Field Description** column as needed.

  5. Optionally, export the field map for external editing. For instructions, see [Edit the BigQuery field map in a CSV file](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#edit-fields-in-csv).

  6. After all changes are complete and any externally edited values have been uploaded, confirm that the **Is Setting Active Flag** checkbox is selected. If **Is Setting Active Flag** is not selected, the BigQuery Toolkit for SAP creates target tables with the default values.

  7. Click **Save**.

The changes are stored in the `/GOOG/BQTR_FIELD` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.




### Change record compression at field level

To improve replication performance, the BigQuery Toolkit for SAP compresses records by omitting all empty fields in the source record, which are then initialized with `null` in the target table in BigQuery. However, if you need to replicate some empty fields with their initial values to BigQuery while still using record compression, then you can select **Send Uncompressed Flag** for those specific fields.

For more information about the record compression behavior, see [Record compression](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#record-compression).

To change record compression at field level, do the following:

  1. In the **BigQuery Data Transfer Settings Maintenance - Fields** screen, display the list of fields for the table whose mass transfer you're configuring.

  2. To send uncompressed data for a field, select **Send Uncompressed Flag** corresponding to the field.

  3. Click **Save**.




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
