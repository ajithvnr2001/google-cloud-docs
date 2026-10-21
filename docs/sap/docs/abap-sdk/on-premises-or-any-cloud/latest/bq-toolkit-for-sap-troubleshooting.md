---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-troubleshooting/
title: Troubleshooting the BigQuery Toolkit for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:30.640963+00:00
---

# Troubleshooting the BigQuery Toolkit for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  Troubleshooting the BigQuery Toolkit for SAP Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-toolkit-for-sap-troubleshooting)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-troubleshooting)



This document shows SAP administrators, SAP developers, or others how to troubleshoot problems with the BigQuery Toolkit for SAP.

## Common issues

This section lists common error messages and their resolution specific to the BigQuery Toolkit for SAP.

For information about troubleshooting the ABAP SDK for Google Cloud issues in general, see [Troubleshooting the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).

### `/GOOG/BQTR: Mass Transfer Key is required. Use Tcode /GOOG/BQTR_SETTINGS to maintain`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: Mass Transfer Key is required. Use Tcode /GOOG/BQTR_SETTINGS to maintain`.

**Cause:** The mass transfer key is not provided in the `IV_MASS_TR_KEY` parameter when calling the data load class `/GOOG/CL_BQTR_DATA_LOAD`.

**Resolution:** To resolve this issue, pass a mass transfer key that is saved in the transaction `/GOOG/BQTR_SETTINGS`. For more information, see [Call the data replication method](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-replication#call_replication_method).

### `/GOOG/BQTR: Data Source is required. Pass a dictionary object`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: Data Source is required. Pass a dictionary object`.

**Cause:** The data source is not provided in the `IV_DATA_SOURCE` parameter when calling the data load class `/GOOG/CL_BQTR_DATA_LOAD`.

**Resolution:** To resolve this issue, pass the name of the dictionary object such as CDS view or table as the data source. For more information, see [Call the data replication method](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-replication#call_replication_method).

### `/GOOG/BQTR: Mass Transfer Key MASS_TRANSFER_KEY not found. Use Tcode /GOOG/BQTR_SETTINGS to maintain`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: Mass Transfer Key MASS_TRANSFER_KEY not found. Use Tcode /GOOG/BQTR_SETTINGS to maintain`.

**Cause:** The mass transfer key passed to the data load class `/GOOG/CL_BQTR_DATA_LOAD` is not maintained in the BigQuery Data Transfer module.

**Resolution:** To resolve this issue, maintain a mass transfer key by using the transaction code `/GOOG/BQTR_SETTINGS`. For more information, see [Configure the BigQuery Data Transfer module](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration#configure-bq-toolkit-data-transfer-module).

### `/GOOG/BQTR: DATA_SOURCE does not exist in data dictionary`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: DATA_SOURCE does not exist in data dictionary`.

**Cause:** The data source passed to the data load class `/GOOG/CL_BQTR_DATA_LOAD` is not a valid data dictionary object.

**Resolution:** To resolve this issue, pass the name of the data source that exists in the data dictionary. Only tables, dictionary views, and CDS views are supported.

### `/GOOG/BQTR: Nested Tables are not supported`

**Issue:** You receive the error message `/GOOG/BQTR: Nested Tables are not supported`.

**Cause:** The dictionary object passed as the input to the data load class `/GOOG/CL_BQTR_DATA_LOAD` is not a flat structure.

**Resolution:** To resolve this issue, use a dictionary object that has a [flat structure](https://help.sap.com/doc/abapdocu_751_index_htm/7.51/en-us/abendata_objects_structure.htm).

### `/GOOG/BQTR: Error creating target table definition`

**Issue:** You receive the error message `/GOOG/BQTR: Error creating target table definition`.

**Cause:** The BigQuery Toolkit for SAP is unable to create the target table definition for the given data source.

**Resolution:** To resolve this issue, validate that the input source is a valid dictionary object with one or more fields.

### `/GOOG/BQTR: 400 - Table creation failed in BQ. Could not pull the table metadata from BQ`

**Issue:** You receive the error message `/GOOG/BQTR: 400 - Table creation failed in BQ. Could not pull the table metadata from BQ`.

**Cause:** This error is raised if the BigQuery Data Transfer module is unable to get the table definition from BigQuery. This might be caused due to a temporary server overload in BigQuery.

**Resolution:** To resolve this issue, restart the BigQuery data load operation.

### `/GOOG/BQTR: 400 - Scope must be provided`

**Issue:** You receive the error message `/GOOG/BQTR: 400 - Scope must be provided`.

**Cause:** In the client key configuration, **Google Cloud Scope** is empty.

**Resolution:** To resolve this issue, for the client key configuration that you're using, in the **Google Cloud Scope** field, specify the corresponding scope — for example, `https://www.googleapis.com/auth/cloud-platform`.

### `/GOOG/BQTR: 400 - Schema mismatch for table TABLE_NAME`

**Issue:** You receive the error message `/GOOG/BQTR: 400 - Schema mismatch for table TABLE_NAME. Please delete the table from BigQuery and try again.`

**Cause:** One of the following changes was entered for an existing BigQuery table:

  * Deletion of a field
  * Renaming of a field
  * Change in the data type of a field
  * Change in the partition type of a table



The preceding changes cannot be applied to an existing BigQuery table.

**Resolution:** If you need to change any of these field attributes in an existing table, then you need to delete the existing table and reload the records into a new table.

### Error messages related to invalid data

**Issue:** In the application logs, you receive an error message: `/GOOG/BQTR/: DESCRIPTION_OF_INVALID_DATA error occurred in FIELD_NAME in record RECORD_KEYS`.

**Cause:** This error message is issued by BigQuery when inserting the records with any invalid data into the target table. The data might be invalid due to one of the following reasons:

  * The data in the field of a particular record is not compatible with the data type in BigQuery. For example, BigQuery generates error messages when: 
    * A string is maintained in a field of type `DATE`, `INTEGER`, or `BOOLEAN`.
    * An invalid date (`00/00/0000`) is maintained in a field of type `DATE`.
  * An incorrect target data type is maintained in the field mappings in transaction `/GOOG/BQTR_SETTINGS`.



An error message is issued by BigQuery for each record that contains a field with invalid data.

**Resolution:** Analyze the error message, `DESCRIPTION_OF_INVALID_DATA`, to understand the possible cause for invalid data. To identify the record with the field that contains the invalid data, use `RECORD_KEYS`, which includes the contents of the first five fields of the record. If the table has five fields or less, then the contents of all fields are included in the `RECORD_KEYS`.

  * If the data in the field is not compatible with the data type in BigQuery, then correct the data in the source table.
  * If the error occurred due to a mismatch between the data and the data type, then use transaction `/GOOG/BQTR_SETTINGS` to specify an appropriate data type.



### `/GOOG/BQTR: 403 - Access Denied: Dataset PROJECT_ID:DATASET_NAME: Permission bigquery.tables.created denied on dataset`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: 403 - Access Denied: Dataset PROJECT_ID:DATASET_NAME: Permission bigquery.tables.created denied on dataset`.

**Cause:** For your SAP workload that is running on Google Cloud, in the table `/GOOG/CLIENT_KEY`, the specified service account does not have the required permissions to access the BigQuery API.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/BQTR_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/BQTR_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/CLIENT_KEY`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, note the value specified for the **Service Account Name** field.

  5. In the Google Cloud console, go to the Identity and Access Management **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  6. Select the service account that you noted in a preceding step.

  7. Ensure that the service account has the IAM roles that BigQuery Toolkit for SAP requires to access BigQuery, as given in [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration#set-up-authentication).

  8. Rerun your replication.




### `403 - Exceeded rate limits: too many table update operations for this table.`

**Issue:** Your BigQuery table updates are temporarily blocked because you've hit the BigQuery [rate limit](https://docs.cloud.google.com/bigquery/quotas).

**Cause** : This usually happens when you have multiple replication mass transfer IDs for the same table in your system. If these different mass transfer IDs have any differences in how they define the table, such as field types or descriptions, then it causes race conditions for table definition changes between those replication jobs. This continuous, conflicting attempt to change the table's definition then causes you to exceed the BigQuery rate limit.

**Resolution** : To fix this issue, you need to make sure that the field names, types, descriptions, and partitioning settings are exactly the same across all the different mass transfer IDs that are replicating data to the target BigQuery table.

For more information about troubleshooting rate limits, see [Troubleshoot quota and limit errors](https://docs.cloud.google.com/bigquery/docs/troubleshoot-quotas).

### `/GOOG/BQTR: 404 - Not Found`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: 404 - Not Found`.

**Cause:** In the [RFC destinations](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#create_rfc_destinations) that ABAP SDK for Google Cloud uses to connect to Google Cloud APIs, the path prefix is not correct.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/BQTR_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/BQTR_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/SERVIC_MAP`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, note the RFC destination names.

  5. Enter transaction `SM59`, and then complete the following steps:

     * For the RFC destination that connects to BigQuery, make sure that the **Path Prefix** field value is `/bigquery/v2/`.
     * For the RFC destination that connects to IAM, make sure that the **Path Prefix** field value is `/v1/`.
  6. Rerun your replication.




### `/GOOG/BQTR: 404 - Table PROJECT_ID:DATASET_NAME.TABLE_NAME not found`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: 404 - Table PROJECT_ID:DATASET_NAME.TABLE_NAME not found`.

**Cause:** In the [RFC destinations](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#create_rfc_destinations) that ABAP SDK for Google Cloud uses to connect to Google Cloud APIs, the value that you have specified for the **Target Host** field doesn't match any DNS name in Cloud DNS.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the transaction code `/GOOG/BQTR_SETTINGS`.

  2. Enter the mass transfer key for which you received this error.

  3. Click the **Execute** icon. Note the value in the **Google Cloud Key Name** column.

  4. Enter transaction `SM30` and then open the table `/GOOG/CLIENT_KEY` in display mode.

  5. Search the table `/GOOG/SERVIC_MAP` by using the **Google Cloud Key Name** that you noted in a preceding step, and then note the specified RFC destination names.

  6. Enter transaction code `SM59`.

  7. For the RFC destinations that you use to connect to BigQuery and IAM APIs, note down the value specified for the **Target Host** field.

  8. In the Google Cloud console, go to the Network services **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/zones)

  9. Click the private zone that contains the DNS records for the Private Service Connect endpoints, which you created to allow BigQuery Toolkit for SAP to privately connect to the BigQuery and IAM APIs.

  10. Ensure that there is a DNS record, with matching **DNS name** , for each of the target host values that you noted in a preceding step.

  11. Rerun your replication.




### `/GOOG/BQTR: 404 - Not Found Requested entity was not found`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: 404 - Not Found Requested entity was not found`.

**Cause:** For your workload that is running on Google Cloud, the service account used in the client key table `/GOOG/CLIENT_KEY` is not valid.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/BQTR_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/BQTR_SETTINGS

  2. Enter the mass transfer key for which you received this error.

  3. Click the **Execute** icon. Note the value in the **Google Cloud Key Name** column.

  4. Enter transaction `SM30`, and then open the table `/GOOG/CLIENT_KEY`.

  5. For the **Service Account Name** field, make sure that the value specified is the email address of the service account that was created for BigQuery Toolkit for SAP.

  6. Rerun your replication.




### `/GOOG/BQTR: 413 - Request Entity Too Large`

**Issue:** Data transfer failed with the error message `/GOOG/BQTR: 413 - Request Entity Too Large`.

**Cause:** This issue can be caused when the byte size of the chunk that is sent by BigQuery Toolkit for SAP exceeded the maximum byte size for HTTP requests that BigQuery accepts. This can occur when the size of the table records or the amount of data the records contain causes the byte size of a chunk to grow beyond the BigQuery limit.

**Resolution:** Reduce the size of the chunks that are sent by BigQuery Toolkit for SAP for your table. You can adjust the chunk size by running the transaction `/GOOG/BQTR_SETTINGS` or enable dynamic chunk size to automatically adjust the chunk size. For more information, see:

  * [Data transfer chunk size](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#data-transfer-chunk-size)
  * [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-operations#dynamic-chunk-size)



### `/GOOG/BQTR: 404 - Not found: Dataset DATASET_NAME`

**Issue:** When attempting to either validate Google Cloud security or to load data into a BigQuery table, you receive message `/GOOG/BQTR: 404 - Not found: Dataset DATASET_NAME`.

**Cause:** This issue can be caused by the following circumstances:

  * The BigQuery dataset was not created yet.
  * The dataset name is not specified correctly in the mass transfer configuration.
  * The replication configuration in the BigQuery Data Transfer module needs to be activated.



**Resolution:** Try the following resolutions:

  * Confirm that the dataset has been created in BigQuery.
  * Check that the dataset name in the mass transfer configuration is the same as the dataset name in BigQuery.



### `/GOOG/BQTR : Unable to interpret VALUE as a BOOLEAN`

**Issue:** The load or replication of a record fails with the message `/GOOG/BQTR : Unable to interpret VALUE as a BOOLEAN`.

**Cause:** This issue is caused by the mapping of a field in the source table to the BigQuery data type `BOOLEAN`, but the data in the source field does not resolve to a boolean.

**Resolution:** To resolve the issue, use transaction `/GOOG/BQTR_SETTINGS` to either change the data type that the source field is mapped to or remove the data type mapping and accept the default data type.

### `/GOOG/BQTR: Failed to convert field SAP_FIELD_NAME value to field BIGQUERY_FIELD_NAME: ERROR_DETAILS`

**Issue:** The load or replication of a record fails with the message `/GOOG/BQTR: Failed to convert field SAP_FIELD_NAME value to field BIGQUERY_FIELD_NAME: ERROR_DETAILS`.

**Cause:** Either the source field contains an invalid value or the source field is mapped to a BigQuery data type that is not a valid mapping for the data that the source field contains.

**Resolution:** To resolve the issue, use transaction `/GOOG/BQTR_SETTINGS` to change the data type that the source field is mapped to or remove the data type mapping and accept the default mapping for the data type.

### `/GOOG/BQTR: DESCRIPTION_OF_ISSUE error occurred in chunk ranging START_INDEX_OF_FAILED_CHUNK - END_INDEX_OF_FAILED_CHUNK`

**Issue:** Replication of a chunk failed with an error message `/GOOG/BQTR: DESCRIPTION_OF_ISSUE error occurred in chunk ranging START_INDEX_OF_FAILED_CHUNK - END_INDEX_OF_FAILED_CHUNK`.

**Cause:** This can have more than one cause, including `Invalid JSON Payload`, `Quota Exceeded`, `Request Entity Too Large`, or `HTTP Communication Failure`. The error message for the chunk that failed to replicate to BigQuery is shown with the start and end index of the chunk.

This error message is shown if you have not set the `BREAK` flag in transaction `/GOOG/BQTR_SETTINGS`. When the `BREAK` flag is not set, BigQuery Toolkit for SAP continues sending records to BigQuery by sending the next chunk even when an error is encountered.

**Resolution:** Try the following resolutions:

  * For `Quota Exceeded`, `Request Entity Too Large`, or `HTTP Communication Failure` issues, follow the troubleshooting steps for /GOOG/BQTR: 413 - Request Entity Too Large.
  * Stop the current load, delete the target table from BigQuery, and then restart a fresh load.
  * To stop sending data to BigQuery and terminate the replication job when a chunk with an error is encountered, set the `BREAK` flag, which is recommended in production environments.



For information about configuring the `BREAK` flag, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-configuration#configure-connection).

## Get support from the community

Ask your questions and discuss BigQuery Toolkit for SAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

## Get support

Google Cloud offers support for issues and questions related to the installation, configuration, operation, and maintenance of the BigQuery Toolkit for SAP.

For issues originating from SAP-managed components or third-party software, Google Cloud Customer Care makes its best effort to identify the root cause. To resolve these issues, contact the respective vendor or support provider.

If you need help resolving problems with the BigQuery Toolkit for SAP, then collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/getting-support-diag-info) and contact Cloud Customer Care.

For more information about contacting Cloud Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
