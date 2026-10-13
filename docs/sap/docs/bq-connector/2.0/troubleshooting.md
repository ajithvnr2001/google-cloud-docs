---
url: https://docs.cloud.google.com/sap/docs/bq-connector/2.0/troubleshooting/
title: Version 2.0: BigQuery Connector for SAP troubleshooting guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:26.546473+00:00
---

# Version 2.0: BigQuery Connector for SAP troubleshooting guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/2.0/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  Version 2.0: BigQuery Connector for SAP troubleshooting guide Stay organized with collections  Save and categorize content based on your preferences. 

You can troubleshoot issues with **versions 2.0 and 2.1** of the BigQuery Connector for SAP by using both SAP LT Replication Server application logging and Google Cloud logs to review error and log messages.

BigQuery Connector for SAP sends all errors to the standard SAP LT Replication Server application logs.

You can also use SAP LT Replication Server debugging to isolate problems.

## Troubleshooting overview

When you troubleshoot issues with BigQuery Connector for SAP, there are several different areas in which you might need to focus your attention, depending upon the area or scope of the issue that you are investigating:

  * The infrastructure, such as the network, hardware or operating system.
  * The SAP software, including the source server and SAP LT Replication Server.
  * BigQuery Connector for SAP.
  * BigQuery, including the BigQuery API and the target table.



### Involve the right teams

The first thing you need to do when troubleshooting an issue is to determine in which of the preceding areas the issue is occurring and what the scope of the issue is.

To resolve an issue, you might need to work with multiple teams, such as your Basis administrators, your SAP LT Replication Server administrators, your DBAs, or your Google Cloud security administrators.

Getting the right teams and skills involved early can help you resolve your issues more quickly.

### Determine the root cause

You need to determine the root cause of your issue and make sure that what you think might be the cause is not actually just a symptom of a root cause that lies elsewhere.

SAP systems are tightly integrated, but can write logs and traces to files in multiple different locations. When you are troubleshooting, you need to determine the correct logs and trace files to look at.

### Check software requirements and prerequisites

Make sure that all system software are running at the required minimum versions and that all BigQuery Connector for SAP prerequisites have been met.

For information about BigQuery Connector for SAP installation prerequisites, see:

  * If SAP LT Replication Server is running on a Compute Engine VM, see [Prerequisites](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#prereqs).

  * If SAP LT Replication Server is running on a host that is external to Google Cloud, see [Prerequisites](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-off-gc#prereqs).




For BigQuery Connector for SAP software requirements, see [Software requirements](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#reqs-software).

If you are using older ECC software, make sure that your SAP LT Replication Server version is compatible with your ECC version. For more information, see [SAP Note 2577774 - Version compatibility for source and target systems \- SLT](https://launchpad.support.sap.com/#/notes/2577774).

### Read the SAP support documentation

If you have an SAP user account, you can find the resolution to many SAP software issues by reading the SAP Notes and SAP Knowledge Base Articles that are available in the [SAP ONE Support Launchpad](https://launchpad.support.sap.com).

## Logging

BigQuery Connector for SAP sends its log messages to SAP LT Replication Server, where you can view them in the SAP LT Replication Server application logs.

These messages include the messages that BigQuery Connector for SAP receives from the BigQuery API.

General BigQuery log messages can be viewed in the Google Cloud console.

### SAP LT Replication Server application logs

All error messages are saved to the standard SAP LT Replication Server application logs. Check the application logs to analyze and troubleshoot the root cause of issues.

You can display the application logs that are specific to your SAP LT Replication Server configuration by running transaction `LTRC`, opening your configuration, and selecting **Application Logs**.

When the logs are displayed, select a table row, and then you can click a button to display any error messages. If you click the **Application Logs** tab for a replication, then you can filter relevant runtime log messages for the replication.

### Messages generated by BigQuery Connector for SAP

Any errors that occur in BigQuery Connector for SAP before records are sent to BigQuery are prefixed by `/GOOG/SLT`.

Any errors that are returned from the BigQuery API are prefixed by `/GOOG/MSG`. This includes any HTTP errors.

If an error is not prefixed by either of these values, then the error was issued by SAP LT Replication Server.

### BigQuery logs

BigQuery writes various log entries to the Cloud Logging in the Google Cloud console.

To view BigQuery log entries:

  1. In the Google Cloud console, open Logging:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** editor, specify a BigQuery resource. For example:
         
         resource.type="bigquery_dataset"




For more information about BigQuery logs, see [Logs](https://docs.cloud.google.com/bigquery/docs/monitoring#logs).

## HTTP trace

While troubleshooting errors, you can enable the HTTP trace in transaction `SMICM` or `ST05`.

To limit the impact on performance, disable HTTP trace as soon as you are done.

## Debugging

If you have the required authorization, you can debug the Business Add-In (BAdI) code of BigQuery Connector for SAP.

To debug the BAdI code:

  1. If you don't already have the SAP authorizations that are required for debugging BAdI code, request them from your SAP administrator.

  2. Enable debugging by typing `/h` in the transaction entry field in the SAP GUI, and then pressing `Enter`.

  3. In the **Settings** menu, select **Change Debugger Profile/ Settings**.

  4. Under **Debug Modes** , make sure that **System Debugging** is selected.

  5. Set external breakpoints in the code as needed.




## Monitoring

You can monitor several different points along the data path from the SAP data source to the target BigQuery table, including:

  * Infrastructure - network, hardware and operating system
  * The SAP database layer
  * The SAP application layer
  * BigQuery Connector for SAP
  * BigQuery



For more information about monitoring at each of these points, see the [BigQuery Connector for SAP operations guide](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#monitoring).

## Data reconciliation

There are three points at which you can check record counts:

  * The source table
  * The SAP LT Replication Server load or replication statistics in transaction `LTRC`
  * The BigQuery target table



You can use the Replication Validation tool to check and compare record counts or you can retrieve the records yourself by executing SQL queries.

For more information about data reconciliation, see the [BigQuery Connector for SAP operations guide](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#data_reconciliation).

## Common configuration issues

This section contains resolutions for common issues that can occur during the initial setup and configuration of BigQuery Connector for SAP.

### SAP LT Replication Server support for database data types

Depending your SAP software versions, SAP LT Replication Server might not support some data types in a source database. For more information, see the _Important Considerations_ section of [SAP Note 1605140 - SAP Landscape Transformation Replication Server (SLT)](https://launchpad.support.sap.com/#/notes/1605140).

### Issue: OS command for access token not working in SAP LT Replication Server

**Issue:** You [created an operating system (OS) command to print the access token](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-off-gc#create-os-command), but it is not working in SAP LT Replication Server.

**Cause:** This issue can be caused by multiple issues, but is most likely caused by not having the environment variables that are required for the OS command configured correctly.

**Resolution:** Confirm that the OS Command was configured correctly. For the configuration steps, see [Create an OS command to print access token](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-off-gc#create-os-command).

Try running the `printenv` command both from the OS as the `sidadm` and from SAP transaction `SM69` and compare the output.

If the variables returned in transaction `SM69` are incomplete, try restarting SAP LT Replication Server to register the variables.

### Issue: `/GOOG/MSG: 413 - Request Entity Too Large`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 413 - Request Entity Too Large`.

**Cause:** This issue can be caused when the byte size of the chunk that is sent by BigQuery Connector for SAP exceeded the maximum byte size for HTTP requests that BigQuery accepts. This can occur when the size of the table records or the amount of data the records contain causes the byte size of a chunk to grow beyond the BigQuery limit.

**Resolution:** Reduce the size of the chunks that are sent by BigQuery Connector for SAP for your table. You can adjust the chunk size by running the transaction `/GOOG/SLT_SETTINGS`.

For information about sizing chunks, see [Chunk size in BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#chunk-size-bqc4sap).

### Issue: `/GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the request sending`

**Issue:** Data transfer failed with an error message `/GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the request sending`.

**Cause:** This issue can be caused by connection or network issues.

**Resolution:** Validate your connection and make sure that your network is set up correctly, is running without errors, and is not congested.

### Issue: `/GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the response receiving`

**Issue:** Data transfer failed with an error message `/GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the response receiving`.

This issue can be caused by the following circumstances:

  * SSL handshake failed
  * Byte size of chunks exceeded the maximum byte size for HTTP requests that BigQuery accepts



#### SSL handshake failed

**Cause:** When the SSL handshake failed between the SAP LT Replication Server host and the BigQuery API endpoint. This occurs when the certificate presented by the TLS server is not valid for the target hostname that is supplied by the SAP LT Replication Server, possibly because client-side sending of the optional TLS extension SNI is not implemented on your NetWeaver kernel.

**Resolution:** In transaction `SMICM`, look for the return code, `SSLERR_SERVER_CERT_MISMATCH`. If you find the return code `SSLERR_SERVER_CERT_MISMATCH`, then you need to enable sending of TLS extension SNI. Also, make sure that your NetWeaver kernel implements client-side sending of the optional TLS extension SNI.

To enable sending of TLS extension SNI, set the profile parameter `icm/HTTPS/client_sni_enabled` or `ssl/client_sni_enabled` to `TRUE`, depending upon your NetWeaver kernel version. For more information from SAP, see:

  * [SAP Note 510007 - Additional considerations for setting up SSL on Application Server ABAP](https://launchpad.support.sap.com/#/notes/510007)
  * [SAP Note 2582368 - SapSSL update for client-side sending of TLS extension SNI by saphttp, sapkprotp](https://launchpad.support.sap.com/#/notes/2582368)
  * [SAP Note 2124480 - ICM / Web Dispatcher: TLS Extension Server Name Indication (SNI) as client](https://launchpad.support.sap.com/#/notes/2124480)



#### Byte size of chunks exceeded the maximum byte size for HTTP requests that BigQuery accepts

**Cause:** When the byte size of the chunk that is sent by BigQuery Connector for SAP exceeded the maximum byte size for HTTP requests that BigQuery accepts. This can occur when the size of the table records or the amount of data the records contain causes the byte size of a chunk to grow beyond the BigQuery limit.

**Resolution:** Reduce the size of the chunks that are sent by BigQuery Connector for SAP for this table. You can adjust the chunk size by running the transaction `/GOOG/SLT_SETTINGS`. For more information, see [Chunk size in BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#chunk-size-bqc4sap).

### Issue: `/GOOG/MSG: 404 - Not found: Dataset DATASET_NAME`

**Issue:** When attempting to either validate Google Cloud security or to load data into a BigQuery table, you receive message `/GOOG/MSG: 404 - Not found: Dataset DATASET_NAME`.

**Cause:** This issue can be caused by the following circumstances:

  * The BigQuery dataset was not created yet.
  * The dataset name is not specified correctly in the mass transfer configuration.
  * The replication configuration in SAP LT Replication Server needs to be activated.



**Resolution:** Try the following resolutions:

  * Confirm that the dataset has been created in BigQuery.
  * Check that the dataset name in the mass transfer configuration is the same as the dataset name in BigQuery.
  * Run the `LTRC` transaction and deactivate and reactivate the replication configuration.



### Issue: `Mass Transfer Key can not be found for Mass Transfer ID XXX`

**Issue:** You receive the error `/GOOG/SLT: Mass Transfer Key can not be found for Mass Transfer ID XXX`.

**Cause:** This issue can be caused by the following circumstances:

  * A mass transfer configuration does not exist for the specified mass transfer ID.
  * The corresponding replication configuration is not active.



**Resolution:** To resolve the issue, perform one of the following actions:

  * Run the `/GOOG/SLT_SETTINGS` transaction and confirm that the mass transfer ID is correctly specified.
  * Run the `LTRC` transaction and deactivate and reactivate the replication configuration.



### Issue: `/GOOG/SLT : Unable to interpret VALUE as a BOOLEAN`

**Issue:** The load or replication of a record fails with the message `/GOOG/SLT : Unable to interpret VALUE as a BOOLEAN`.

**Cause:** This issue is caused by the mapping of a field in the source table to the BigQuery data type `BOOLEAN`, but the data in the source field does not resolve to a boolean.

**Resolution:** To resolve the issue, use transaction /GOOG/SLT_SETTINGS to either change the data type that the source field is mapped to or remove the data type mapping and accept the default data type.

### Issue: `/GOOG/SLT: Failed to convert field SAP_FIELD_NAME value to field BIGQUERY_FIELD_NAME: ERROR_DETAILS`

**Issue:** The load or replication of a record fails with the message `/GOOG/SLT: Failed to convert field SAP_FIELD_NAME value to field BIGQUERY_FIELD_NAME: ERROR_DETAILS`.

**Cause:** Either the source field contains an invalid value or the source field is mapped to a BigQuery data type that is not a valid mapping for the data that the source field contains.

**Resolution:** To resolve the issue, use transaction `/GOOG/SLT_SETTINGS` to change the data type that the source field is mapped to or remove the data type mapping and accept the default mapping for the data type.

### Issue: `/GOOG/MSG : Client key is not found in /GOOG/CLIENT_KEY table`

**Issue:** A load or replication does not start with the message `/GOOG/MSG: Client key is not found in /GOOG/CLIENT_KEY table`.

**Cause:** Either the client key does not exist or it was specified incorrectly in the mass transfer configuration of transaction `/GOOG/SLT_SETTINGS`.

**Resolution:** To resolve the issue, either use transaction `SM30` to create the client key or use transaction `/GOOG/SLT_SETTINGS` to correct the specification of the client key value in the mass transfer configuration.

## Common operational issues

This section contains resolutions for common issues that can occur after the initial setup of BigQuery Connector for SAP.

### Issue: Incorrect number of writes in BigQuery

**Issue:** The number of records that are written to BigQuery is higher than the number of records that are shown in the SAP LT Replication Server logs.

**Cause:** This can have more than one cause, including transitory connection issues that cause SAP LT Replication Server to send records more than once or the fact that the BigQuery table accepts only inserts, and each change to a single record in the source is inserted as a separate entry in the target table.

**Resolution:** If the difference in record counts is not extreme and there are not fewer records in BigQuery than in the source table, this is expected behavior and not a problem.

To accurately reconcile the number of records in BigQuery with the number of records in the source table, query the BigQuery table as described in SQL queries for record counts.

For more information about possible causes for this issue, see [Special considerations for ABAP sources/targets on HANA](https://blogs.sap.com/2016/05/25/special-considerations-for-abap-sourcestargets-on-hana/).

### Issue: `/GOOG/MSG : 400 - Schema mismatch for table TABLE_NAME`

**Issue:** You receive error message `/GOOG/MSG : 400 - Schema mismatch for table TABLE_NAME. Please delete the table from BigQuery and try again.`

**Cause:** One of the following changes was entered for an existing BigQuery table:

  * Deletion of a field
  * Renaming of a field
  * Change in the data type of a field
  * Change in the partition type of a table



The preceding changes cannot be applied to an existing BigQuery table.

**Resolution:** If you need to change any of these field attributes in an existing table, then you need to delete the existing table and reload the records into a new table.

If the change was a mistake, then back out the change in SAP LT Replication Server.

For more information about configuring fields and partitions in a target BigQuery table, see [BigQuery replication configurations](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#bq-replication-config).

### Issue: Error messages related to invalid data

**Issue:** In the application logs, you receive an error message: `/GOOG/MSG/: DESCRIPTION_OF_INVALID_DATA error occurred in FIELD_NAME in record RECORD_KEYS`.

**Cause:** This error message is issued by BigQuery when inserting the records with any invalid data into the target table. The data might be invalid due to one of the following reasons:

  * The data in the field of a particular record is not compatible with the data type in BigQuery. For example, BigQuery generates error messages when: 
    * A string is maintained in a field of type `DATE`, `INTEGER`, or `BOOLEAN`.
    * An invalid date (`00/00/0000`) is maintained in a field of type `DATE`.
  * An incorrect target data type is maintained in the field mappings in transaction `/GOOG/SLT_SETTINGS`.



An error message is issued by BigQuery for each record that contains a field with invalid data.

**Resolution:** Analyze the error message, `DESCRIPTION_OF_INVALID_DATA`, to understand the possible cause for invalid data. To identify the record with the field that contains the invalid data, use `RECORD_KEYS`, which includes the contents of first five fields of the record. If the table has five fields or less, then the contents of all fields are included in the `RECORD_KEYS`.

  * If the data in the field is not compatible with the data type in BigQuery, then correct the data in the source table.
  * If the error occurred due to a mismatch between the data and the data type, then use transaction `/GOOG/SLT_SETTINGS` to specify an appropriate data type. For more information about data type mapping, see [Data type mapping](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#data_type_mapping).



## Get support

If you need help resolving problems with replication and the BigQuery Connector for SAP, collect all available diagnostic information and contact Cloud Customer Care.

For more information about contacting Cloud Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
