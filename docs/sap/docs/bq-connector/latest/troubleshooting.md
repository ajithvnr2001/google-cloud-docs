---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting/
title: BigQuery Connector for SAP troubleshooting guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:45.988028+00:00
---

# BigQuery Connector for SAP troubleshooting guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  BigQuery Connector for SAP troubleshooting guide Stay organized with collections  Save and categorize content based on your preferences. 

You can troubleshoot issues with **version 2.15(latest)** of the BigQuery Connector for SAP by using both SAP LT Replication Server application logging and Google Cloud logs to review error and log messages.

BigQuery Connector for SAP sends all errors to the standard SAP LT Replication Server application logs.

You can also use SAP LT Replication Server debugging to isolate problems.

## Troubleshooting overview

When you troubleshoot issues with BigQuery Connector for SAP, there are several different areas in which you might need to focus your attention, depending upon the area or scope of the issue that you are investigating:

  * The infrastructure, such as the network, hardware or operating system.
  * The SAP software, including the source server and SAP LT Replication Server.
  * BigQuery Connector for SAP.
  * Pub/Sub.
  * BigQuery, including the BigQuery API and the target table.
  * Cloud Storage.



### Involve the right teams

The first thing you need to do when troubleshooting an issue is to determine in which of the preceding areas the issue is occurring and what the scope of the issue is.

To resolve an issue, you might need to work with multiple teams, such as your Basis administrators, your SAP LT Replication Server administrators, your DBAs, or your Google Cloud security administrators.

Getting the right teams and skills involved early can help you resolve your issues more quickly.

### Determine the root cause

You need to determine the root cause of your issue and make sure that what you think might be the cause is not actually just a symptom of a root cause that lies elsewhere.

SAP systems are tightly integrated, but can write logs and traces to files in multiple different locations. When you are troubleshooting, you need to determine the correct logs and trace files to look at.

### Check software requirements and prerequisites

Make sure that all system software are running at the required minimum versions and that all BigQuery Connector for SAP prerequisites have been met.

For information about BigQuery Connector for SAP installation prerequisites, see [Prerequisites](https://docs.cloud.google.com/sap/docs/bq-connector/latest/install#prereqs).

For BigQuery Connector for SAP software requirements, see [Software requirements](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#reqs-software).

If you are using older ECC software, make sure that your SAP LT Replication Server version is compatible with your ECC version. For more information, see [SAP Note 2577774 - Version compatibility for source and target systems - SLT](https://launchpad.support.sap.com/#/notes/2577774).

For the SAP source system and SAP LT Replication Server, make sure that you implement all correction notes for the ABAP-based Migration and Replication Technology. For more information, see [SAP Note 3016862 - DMIS Note Analyzers with separated scenarios for ABAP-based Migration and Replication Technology](https://launchpad.support.sap.com/#/notes/3016862).

### Read the SAP support documentation

If you have an SAP user account, you can find the resolution to many SAP software issues by reading the SAP Notes and SAP Knowledge Base Articles that are available in the [SAP ONE Support Launchpad](https://launchpad.support.sap.com).

## Logging

BigQuery Connector for SAP sends its log messages to SAP LT Replication Server, where you can view them in the SAP LT Replication Server application logs.

These messages include the messages that BigQuery Connector for SAP receives from the BigQuery API, Pub/Sub API, and Cloud Storage API.

You can view general BigQuery, Pub/Sub, and Cloud Storage log messages in the Google Cloud console.

### SAP LT Replication Server application logs

All error messages are saved to the standard SAP LT Replication Server application logs. Check the application logs to analyze and troubleshoot the root cause of issues.

You can display the application logs that are specific to your SAP LT Replication Server configuration by running transaction `LTRC`, opening your configuration, and selecting **Application Logs**.

When the logs are displayed, select a table row, and then you can click a button to display any error messages. If you click the **Application Logs** tab for a replication, then you can filter relevant runtime log messages for the replication.

### Messages generated by BigQuery Connector for SAP

Any errors that occur in BigQuery Connector for SAP before records are sent to BigQuery are prefixed by `/GOOG/SLT`.

Any errors that are returned from the BigQuery API, Pub/Sub API, or Cloud Storage API are prefixed by `/GOOG/MSG`. This includes any HTTP errors.

If an error is not prefixed by either of these values, then the error was issued by SAP LT Replication Server.

### BigQuery logs

BigQuery writes various log entries to Cloud Logging in the Google Cloud console.

To view BigQuery log entries, do the following:

  1. In the Google Cloud console, open Logging:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** editor, specify a BigQuery resource. For example:
         
         resource.type="bigquery_dataset"




For more information about BigQuery logs, see [Logs](https://docs.cloud.google.com/bigquery/docs/monitoring#logs).

### Pub/Sub logs

Pub/Sub writes various log entries to Cloud Logging in the Google Cloud console.

To view Pub/Sub log entries, do the following:

  1. In the Google Cloud console, open Logging:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** editor, specify a Pub/Sub resource. For example:
         
         resource.type="pubsub_subscription"




For more information about Pub/Sub logs, see [Monitor Pub/Sub in Cloud Monitoring](https://docs.cloud.google.com/pubsub/docs/monitoring).

### Cloud Storage logs

Cloud Storage writes various log entries to Cloud Logging in the Google Cloud console.

To view Cloud Storage log entries, do the following:

  1. In the Google Cloud console, open Logging:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** editor, specify a Cloud Storage resource. For example:
         
         resource.type="gcs_bucket"




For more information about Cloud Storage logs, see [Cloud Storage audit logging information](https://docs.cloud.google.com/storage/docs/audit-logging).

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

You can monitor several different points along the data path from the SAP data source to Google Cloud, including:

  * Infrastructure - network, hardware and operating system
  * The SAP database layer
  * The SAP application layer
  * BigQuery Connector for SAP
  * Pub/Sub
  * BigQuery
  * Cloud Storage



For more information about monitoring at each of these points, see the [BigQuery Connector for SAP operations guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#monitoring).

## Data reconciliation

There are three points at which you can check record counts:

  * The source table
  * The SAP LT Replication Server load or replication statistics in transaction `LTRC`
  * The BigQuery target table



You can use the Replication Validation tool to check and compare record counts or you can retrieve the records yourself by executing SQL queries.

For more information about data reconciliation, see the [BigQuery Connector for SAP operations guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#replication-validation).

## Common configuration issues

This section contains resolutions for common issues that can occur during the initial setup and configuration of BigQuery Connector for SAP.

### SAP LT Replication Server support for database data types

Depending on your SAP software versions, SAP LT Replication Server might not support some data types in a source database. For more information, see the _Important Considerations_ section of [SAP Note 1605140 - SAP Landscape Transformation Replication Server (SLT)](https://launchpad.support.sap.com/#/notes/1605140).

### Issue: OS command for access token not working in SAP LT Replication Server

**Issue:** You created an operating system (OS) command to print the access token, but it is not working in SAP LT Replication Server.

**Cause:** This issue can be caused by multiple issues, but is most likely caused by not having the environment variables that are required for the OS command configured correctly.

**Resolution:** Confirm that the OS Command was configured correctly.

Try running the `printenv` command both from the OS as the `SID_LCadm` and from SAP transaction `SM69` and compare the output. If the variables returned in transaction `SM69` are incomplete, then try restarting SAP LT Replication Server to register the variables.

### Issue: `/GOOG/MSG: 400 - Bad Request Request contains an invalid argument`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 400 - Bad Request Request contains an invalid argument`.

**Cause:** For your SAP workload that is running on Google Cloud, the access scope used in the client key table `/GOOG/CLIENT_KEY` is not valid.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/CLIENT_KEY`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, make sure that the value of the **Scope** field matches the access scope mentioned in [Specify access settings in `/GOOG/CLIENT_KEY`](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token#specify-clientkey-table). Make sure that there is no space entered in the field.

  5. Rerun your replication.




### Issue: `/GOOG/MSG : 400 - ICM_HTTP_CONNECTION_FAILED`

**Issue:** Data transfer failed with the error message `/GOOG/MSG : 400 - ICM_HTTP_CONNECTION_FAILED`.

**Cause:** In the [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations) that BigQuery Connector for SAP uses to connect to Google Cloud APIs, the value for the **Path Prefix** or the **Target Host** field is incorrect.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/SERVIC_MAP`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, note the RFC destination names.

  5. Enter transaction `SM59`, and then complete the following steps:

     1. Navigate to the required RFC destination that has HTTP connections to External Servers (Type `G`).
     2. Open the **Technical Settings** tab.
     3. Verify that both the **Target Host** and the **Path Prefix** fields are maintained correctly. For information about the required target host and path prefix for the Google Cloud API you're using, see [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations).
     4. Make sure that the **Path Prefix** includes leading and trailing forward slashes (`/`) where applicable.
  6. Rerun your replication or initial load.




### Issue: `/GOOG/MSG: 400 - Invalid data in message: Message failed schema validation`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 400 - Invalid data in message: Message failed schema validation` during CDC replication through Pub/Sub.

**Cause:** When you replicate data from an SAP source system to Google Cloud by using the BigQuery Connector for SAP with Pub/Sub, this error occurs if the source data contains characters that cannot be converted into the required UTF-8 Unicode format.

**Resolution:** To resolve this issue, complete the following steps:

  1. Update BigQuery Connector for SAP to **version 2.12** or later.
  2. In the SAP GUI, enter the `/GOOG/R_SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/R_SLT_SETTINGS

  3. In the **Google Cloud Partner** field, select **BigQuery via Pub/Sub**.

  4. In the **Mass Transfer ID** field, select the mass transfer ID that is failing, and then click **Display**.

  5. Select the table for which replication is failing, and then click **Display** to autopopulate the field mappings.

  6. Review the field mappings and ensure that the **AVRO type** is maintained as **string** for any fields that can contain special characters.

  7. Click **Save**.

  8. If there's an existing Pub/Sub schema for the table, then you must delete the schema. This is required because BigQuery Connector for SAP cannot overwrite the existing schema definition with the new field types. For more information, see [Delete a schema](https://docs.cloud.google.com/pubsub/docs/delete-schema).

  9. In transaction `LTRC`, restart the replication for the table.




For each table that is failing replication, repeat this procedure.

### Issue: `/GOOG/MSG : 401 - Unauthorized Request is missing required authentication credential. Expected OAuth 2 access to ken, login coo`

**Issue:** Data transfer failed with the error message `/GOOG/MSG : 401 - Unauthorized Request is missing required authentication credential. Expected OAuth 2 access to ken, login coo`.

**Cause:** The HTTP port configuration is missing.

**Resolution:** Both HTTP and HTTPS ports must be created and be active in your SAP system.

The [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) is stored on a metadata server, which is only accessible through an HTTP port. Therefore, you must ensure that an HTTP port along with an HTTPS port is created and active in order to access the VM metadata.

To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter transaction code `SMICM`.

  2. On the menu bar, click **Goto > Services**.

  3. Make sure that the HTTP and HTTPS ports are created and active. A green check in the **Actv** column indicates that the HTTP and HTTPS ports are active.

  4. Rerun your replication.




For information about configuring the HTTP and HTTPS ports, see [HTTP(S) Settings in ICM](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/4c/5bdafa97817511e10000000a42189b/frameset.htm).

### Issue: `/GOOG/MSG : 401 - ICM_HTTP_CONNECTION_BROKEN`

**Issue:** During initial load or replication, in the `LTRC` transaction, data transfer failed with the error message `/GOOG/MSG : 401 - ICM_HTTP_CONNECTION_BROKEN`.

**Cause:** For your SAP workload that is running on Google Cloud, in the RFC destinations that BigQuery Connector for SAP uses to connect to Google Cloud APIs, SSL is not activated.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/SERVIC_MAP`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, note the RFC destination names.

  5. Enter transaction `SM59`, and then for the RFC destinations that you noted in the previous step, perform the following steps:

     1. Go to the **Logon and Security** tab.

     2. For the **SSL Certificate** field, make sure that the option **DFAULT SSL Client (Standard)** is selected.

     3. For the **Service No.** field, make sure that the value `443` is specified.

  6. Rerun your replication.




### Issue `/GOOG/MSG: 110 - HTTPIO_PLG_CANCELED`

**Issue:** During initial load or replication, in the `LTRC` transaction, data transfer failed with the error message `/GOOG/MSG: 110 - HTTPIO_PLG_CANCELED`.

**Cause:** The HTTP port configuration is missing.

**Resolution:** Both HTTP and HTTPS ports must be created and be active in your SAP system.

The [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) is stored on a metadata server, which is only accessible through an HTTP port. Therefore, you must ensure that an HTTP port along with an HTTPS port is created and active in order to access the VM metadata.

To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter transaction code `SMICM`.

  2. On the menu bar, click **Goto > Services**.

  3. Make sure that the HTTP and HTTPS ports are created and active. A green check in the **Actv** column indicates that the HTTP and HTTPS ports are active.

  4. Rerun your replication.




For information about configuring the HTTP and HTTPS ports, see [HTTP(S) Settings in ICM](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/4c/5bdafa97817511e10000000a42189b/frameset.htm).

### Issue: `/GOOG/MSG: 403 - SSL is required to perform this operation`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 403 - SSL is required to perform this operation`.

**Cause:** For your SAP workload that is running on Google Cloud, in the [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations) that BigQuery Connector for SAP uses to connect to Google Cloud APIs, SSL is not activated.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/SERVIC_MAP`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, note the RFC destination names.

  5. Enter transaction `SM59`, and then for the RFC destinations that you noted in the previous step, perform the following steps:

     1. Go to the **Logon and Security** tab.

     2. For the **SSL Certificate** field, make sure that the option **DFAULT SSL Client (Standard)** is selected.

     3. For the **Service No.** field, make sure that the value `443` is specified.

  6. Rerun your replication.




### Issue: `/GOOG/MSG: 403 - Request had insufficient authentication scopes`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 403 - Request had insufficient authentication scopes`.

**Cause:** For your SAP workload that is running on Google Cloud, in the table `/GOOG/CLIENT_KEY`, the specified service account does not have the required scope to access BigQuery.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/CLIENT_KEY`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, make sure that the value specified for the **Service Account Name** field is `default`.

  5. In the Google Cloud console, go to the Compute Engine **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  6. Click the VM instance that hosts your SAP LT Replication Server.

  7. Click **Stop** , and then follow the instructions to stop the VM instance.

  8. Click **Edit** , edit the service account **Access scopes** to enable access to BigQuery, and then click **Save**.

  9. Click **Start / Resume** to restart the VM instance.

  10. Ensure that your SAP LT Replication Server is running.

  11. Rerun your replication.




### Issue: `/GOOG/MSG: 403 - Access Denied: Dataset PROJECT_ID:DATASET_NAME: Permission bigquery.tables.created denied on dataset`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 403 - Access Denied: Dataset PROJECT_ID:DATASET_NAME: Permission bigquery.tables.created denied on dataset`.

**Cause:** For your SAP workload that is running on Google Cloud, in the table `/GOOG/CLIENT_KEY`, the specified service account does not have the required permissions to access the BigQuery API.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/CLIENT_KEY`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, note the value specified for the **Service Account Name** field.

  5. In the Google Cloud console, go to the Identity and Access Management **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  6. Select the service account that you noted in a preceding step.

  7. Ensure that the service account has the IAM roles that BigQuery Connector for SAP requires to access BigQuery, as given in [Google Cloud Identity and Access Management](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#security-gcp-iam).

  8. Rerun your replication.




### `403 - Exceeded rate limits: too many table update operations for this table.`

**Issue:** Your BigQuery table updates are temporarily blocked because you've hit the BigQuery [rate limit](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#bq-quotas).

**Cause** : This usually happens when you have multiple replication mass transfer IDs for the same table in your SAP SLT system. If these different mass transfer IDs have any differences in how they define the table, such as field types or descriptions, then it causes race conditions for table definition changes between those replication jobs. This continuous, conflicting attempt to change the table's definition then causes you to exceed the BigQuery rate limit.

**Resolution** : To fix this issue, you need to make sure that the field names, types, descriptions, and partitioning settings are exactly the same across all the different mass transfer IDs that are replicating data to the target BigQuery table.

For more information about troubleshooting rate limits, see [Troubleshoot quota and limit errors](https://docs.cloud.google.com/bigquery/docs/troubleshoot-quotas).

### Issue: `/GOOG/MSG: 404 - Not Found`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 404 - Not Found`.

**Cause:** In the [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations) that BigQuery Connector for SAP uses to connect to Google Cloud APIs, the path prefix is not correct. When the path prefix is incorrect, the SAP system attempts to call a non-existent endpoint on the Google Cloud API host.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/SERVIC_MAP`.

  4. For the **Google Cloud Key Name** value that you noted in a preceding step, note the RFC destination names.

  5. Enter transaction `SM59`, and then complete the following steps:

     1. Navigate to the required RFC destination that has HTTP connections to External Servers (Type `G`).
     2. Open the **Technical Settings** tab.
     3. Verify that both the **Target Host** and the **Path Prefix** fields are maintained correctly. For information about the required target host and path prefix for the Google Cloud API you're using, see [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations).
     4. Make sure that the **Path Prefix** includes leading and trailing forward slashes (`/`) where applicable.
  6. Rerun your replication.




### Issue: `/GOOG/MSG: 404 - Table PROJECT_ID:DATASET_NAME.TABLE_NAME not found`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 404 - Table PROJECT_ID:DATASET_NAME.TABLE_NAME not found`.

**Cause:** In the [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations) that BigQuery Connector for SAP uses to connect to Google Cloud APIs, the value that you have specified for the **Target Host** field doesn't match any DNS name in Cloud DNS.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter transaction code `SE38`, and then open the report `/GOOG/R_SLT_SETTINGS`.

  2. For the `LTRC` transaction that was run, open the mass transfer ID and then note the value in the **Google Cloud Key Name** column.

  3. Enter transaction `SM30` and then open the table `/GOOG/CLIENT_KEY` in display mode.

  4. Search the table `/GOOG/SERVIC_MAP` using the Google Cloud Key Name that you noted in a preceding step, and then note the specified RFC destination names.

  5. Enter transaction code `SM59`.

  6. For the RFC destinations that you use to connect to BigQuery and IAM APIs, note down the value specified for the **Target Host** field.

  7. In the Google Cloud console, go to the Network services **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/zones)

  8. Click the private zone that contains the DNS records for the Private Service Connect endpoints, which you created to allow BigQuery Connector for SAP to privately connect to the BigQuery and IAM APIs.

  9. Ensure that there is a DNS record, with matching **DNS name** , for each of the target host values that you noted in a preceding step.

  10. Rerun your replication.




### Issue: `/GOOG/MSG: 404 - Not Found Requested entity was not found`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 404 - Not Found Requested entity was not found`.

**Cause:** For your workload that is running on Google Cloud, the service account used in the client key table `/GOOG/CLIENT_KEY` is not valid.

**Resolution:** To resolve this issue, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. For the mass transfer ID that failed in transaction `LTRC`, note the value of **Google Cloud Key Name** field.

  3. Enter transaction `SM30`, and then open the table `/GOOG/CLIENT_KEY`.

  4. For the **Service Account Name** field, make sure that the value specified is the email address of the service account that was created for BigQuery Connector for SAP in the step [Create a service account](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token#create-service-account-target-project).

  5. Rerun your replication.




### Issue: `/GOOG/MSG: 418` \- Data transfer failed with error message from SAP

**Issue:** Data transfer failed with an error message from SAP, for example `No OS command defined for the key`.

**Cause:** For your SAP workload that is not running on Google Cloud, this issue can be caused by the following circumstances:

  * OS command that prints access token is not configured correctly
  * RFC is not configured correctly



#### OS command that prints access token is not configured correctly

**Causes:** This issue can be caused by the following circumstances:

  * You have created an operating system (OS) command to print access token but have not added it to the access settings in the [client key table `/GOOG/CLIENT_KEY`](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token#specify-clientkey-table).

  * The OS command that you created in transaction `SM69` failed to retrieve an access token from Google Cloud.




**Resolution:** In the client key table `/GOOG/CLIENT_KEY`, for the field **Command name** , make sure that the value entered matches the name of the command that you created to print access token.

#### RFC is not configured correctly

**Cause:** For your SAP workload that is running on Google Cloud, in the [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations) that BigQuery Connector for SAP uses to connect to Google Cloud APIs, the **Target Host** field value is incorrect.

**Resolution:** To resolve this issue:

  1. In the SAP GUI, enter transaction `SE38`, and then open the report `/GOOG/R_SLT_SETTINGS`.

  2. For the `LTRC` transaction that was run, open the mass transfer ID and note the value of **Google Cloud Key Name**.

  3. Enter transaction `SM30` and then open the table `/GOOG/CLIENT_KEY` in display mode.

  4. Search the table `/GOOG/SERVIC_MAP` using the Google Cloud Key Name that you noted in a preceding step, and then note the specified RFC destination names.

  5. Enter transaction code `SM59`, and then open the RFC destinations that you noted in the previous step.

  6. For the **Target Host** field, correct the specified URL.

  7. Rerun your replication.




### Issue: `/GOOG/MSG: 413 - Request Entity Too Large`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 413 - Request Entity Too Large`.

**Cause:** This issue can be caused when the byte size of the chunk that is sent by BigQuery Connector for SAP exceeded the maximum byte size for HTTP requests that BigQuery accepts. This can occur when the size of the table records or the amount of data the records contain causes the byte size of a chunk to grow beyond the BigQuery limit.

**Resolution:** Reduce the size of the chunks that are sent by BigQuery Connector for SAP for your table. You can adjust the chunk size by running the transaction `/GOOG/SLT_SETTINGS` or enable dynamic chunk size to automatically adjust the chunk size. For more information, see:

  * [Chunk size in BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#chunk-size-bqc4sap)
  * [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#dynamic-chunk-size)



### Issue: `/GOOG/MSG: 503 - HTTP Communication Failure - SSL client SSL Client (Standard)`

**Issue:** Data transfer failed with the error message `/GOOG/MSG: 503 - HTTP Communication Failure - SSL client SSL Client (Standard)`.

**Cause:** For your SAP workload that is running on Google Cloud, in the [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations) that BigQuery Connector for SAP uses to connect to Google Cloud APIs, the **Target Host** field value is incorrect.

**Resolution:** To resolve this issue, see the resolution steps in RFC is not configured correctly.

### Issue: `/GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the request sending`

**Issue:** Data transfer failed with an error message `/GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the request sending`.

**Cause:** This issue can be caused by connection or network issues.

**Resolution:** Validate your connection and make sure that your network is set up correctly, is running without errors, and is not congested.

### Issue: `/GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the response receiving`

**Issue:** Data transfer failed with an error message `/GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the response receiving`.

This issue can be caused by the following circumstances:

  * SSL is not activated in your RFC destinations
  * SSL handshake failed
  * Byte size of chunks exceeded the maximum byte size for HTTP requests that BigQuery accepts



#### SSL is not activated in your RFC destinations

**Cause:** In the [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations) that BigQuery Connector for SAP uses to connect to Google Cloud APIs, the security option for using SSL certificate is not activated.

**Resolution:** To resolve this issue, see the resolutions steps in Issue: `/GOOG/MSG: 403` \- SSL is required to perform this operation.

#### SSL handshake failed

**Cause:** When the SSL handshake failed between the SAP LT Replication Server host and the BigQuery API endpoint. This occurs when the certificate presented by the TLS server is not valid for the target hostname that is supplied by the SAP LT Replication Server, possibly because client-side sending of the optional TLS extension SNI is not implemented on your NetWeaver kernel.

**Resolution:** In transaction `SMICM`, look for the return code, `SSLERR_SERVER_CERT_MISMATCH`. If you find the return code `SSLERR_SERVER_CERT_MISMATCH`, then you need to enable sending of TLS extension SNI. Also, make sure that your NetWeaver kernel implements client-side sending of the optional TLS extension SNI.

To enable sending of TLS extension SNI, set the profile parameter `icm/HTTPS/client_sni_enabled` or `ssl/client_sni_enabled` to `TRUE`, depending upon your NetWeaver kernel version. For more information from SAP, see:

  * [SAP Note 510007 - Additional considerations for setting up SSL on Application Server ABAP](https://launchpad.support.sap.com/#/notes/510007)
  * [SAP Note 2582368 - SapSSL update for client-side sending of TLS extension SNI by saphttp, sapkprotp](https://launchpad.support.sap.com/#/notes/2582368)
  * [SAP Note 2124480 - ICM / Web Dispatcher: TLS Extension Server Name Indication (SNI) as client](https://launchpad.support.sap.com/#/notes/2124480)



#### Byte size of chunks exceeded the maximum byte size for HTTP requests that BigQuery accepts

**Cause:** When the byte size of the chunk that is sent by BigQuery Connector for SAP exceeded the maximum byte size for HTTP requests that BigQuery accepts. This can occur when the size of the table records or the amount of data the records contain causes the byte size of a chunk to grow beyond the BigQuery limit.

**Resolution:** Reduce the size of the chunks that are sent by BigQuery Connector for SAP for this table. You can adjust the chunk size by running the transaction `/GOOG/SLT_SETTINGS` or enable dynamic chunk size to automatically adjust the chunk size. For more information, see:

  * [Chunk size in BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#chunk-size-bqc4sap)
  * [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#dynamic-chunk-size)



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

### Issue: `/GOOG/MSG: DESCRIPTION_OF_ISSUE error occurred in chunk ranging START_INDEX_OF_FAILED_CHUNK - END_INDEX_OF_FAILED_CHUNK`

**Issue:** Replication of a chunk failed with an error message `/GOOG/MSG: DESCRIPTION_OF_ISSUE error occurred in chunk ranging START_INDEX_OF_FAILED_CHUNK - END_INDEX_OF_FAILED_CHUNK`.

**Cause:** This can have more than one cause, including `Invalid JSON Payload`, `Quota Exceeded`, `Request Entity Too Large`, or `HTTP Communication Failure`. The error message for the chunk that failed to replicate to BigQuery is shown with the start and end index of the chunk.

This error message is shown if you have not set the `BREAK` flag in transaction `/GOOG/SLT_SETTINGS`. When the `BREAK` flag is not set, BigQuery Connector for SAP continues sending records to BigQuery by sending the next chunk even when an error is encountered.

**Resolution:** Try the following resolutions:

  * For `Quota Exceeded`, `Request Entity Too Large`, or `HTTP Communication Failure` issues, follow the appropriate troubleshooting steps:

    * Issue: /GOOG/MSG: 413 - Request Entity Too Large
    * Issue: /GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the request sending
    * Issue: /GOOG/MSG: 503 - HTTP Communication Failure exception occurred during the response receiving
  * Stop the current load, delete the target table from BigQuery, and then restart a fresh load.

  * To stop sending data to BigQuery and terminate the replication job when a chunk with an error is encountered, set the `BREAK` flag, which is recommended in production environments.

For information about configuring the `BREAK` flag, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#configure-connection).




### Issue: `DESCRIPTION_OF_ISSUE while signing JWT using profile KEY_FILE_NAME.pse. Check JWT config in `STRUST``

**Issue:** You receive the error `DESCRIPTION_OF_ISSUE while signing JWT using profile KEY_FILE_NAME .pse. Check JWT config in `STRUST``.

**Cause:** The JWT configuration and service account key settings are not configured correctly in `STRUST`.

**Resolution:** Confirm that the JWT configuration and service account key are configured as explained in [Authentication using JWT to obtain access tokens](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt).

### Issue: `Bad Request invalid_grant. Invalid JWT Signature`

**Issue:** You receive the error `Bad Request invalid_grant. Invalid JWT Signature`.

**Cause:** The PSE or P12 key file imported into `STRUST` does not belong to the service account that you used for signing the JWT.

**Resolution:** Make sure to import the correct service account key file into `STRUST`. For information about importing the service account key into `STRUST`, see [Import the service account key into STRUST](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt#jwt-import-service-account-key-strust).

### Issue: `/GOOG/MSG : 400 - Bad Request invalid_grant Invalid grant: account not found`

**Issue:** You are not able to connect to Google Cloud APIs.

**Cause:** The service account used for JWT signing is either incorrect or it does not have required permissions.

**Resolution:** Make sure that the service account that you specified for JWT based token retrieval is correctly maintained against the parameter `JWT_SERVC_ACCT` in the table `/GOOG/BQ_PARAM`. For more information, see [Enable JWT signing for the service account on the SAP LT Replication Server host](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt#jwt-enable-jwt-signing-service-account).

### Issue: `OAuth RFC HTTP Destination not maintained in `/GOOG/SERVIC_MAP``

**Issue:** You receive the error `OAuth RFC HTTP Destination not maintained in `/GOOG/SERVIC_MAP``.

**Cause:** The RFC destination for OAuth 2.0 is not available in the service mapping table `/GOOG/SERVIC_MAP`.

**Resolution:** Update the RFC destination for OAuth 2.0 in the service mapping table `/GOOG/SERVIC_MAP` and re-run the load. For information about specifying RFC destinations, see [Specify RFC destinations in `/GOOG/SERVIC_MAP`](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt#configure_rfc_destinations).

### Issue: For non-English logon languages, field descriptions are garbled when you upload data using a CSV file

**Issue:** For non-English logon languages, when you upload BigQuery target table field types and field descriptions using the [file upload option](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#edit-field-definitions-in-csv), the field descriptions from the CSV file are not uploaded accurately. You find garbled characters and symbols in the uploaded descriptions.

**Cause:** For non-English logon languages, the file upload utility is not able to interpret the characters in the CSV file accurately.

**Resolution:** To upload BigQuery target table field types and field descriptions in a non-English language, use the UTF-8 encoding format with Byte Order Mark (BOM) for your CSV file. Save the CSV file in UTF-8 with BOM format and then upload the file.

### Issue: Authentication error due to root CA certificates not being valid

**Issue:** You cannot authenticate to Google Cloud and have encountered the following:

  * You received the error message `/GOOG/MSG: 421 - SSL handshake with iamcredentials.googleapis.com: 443 failed: SSSLERR_PEER_CERT_UNTRUSTED`.
  * In transaction `SMICM`, you find the error message `ERROR: The chain of certificates is incomplete or untrusted, missing certificate of CN-GTS Root R4.`



**Cause:** The latest Google root CA certificates are not correctly installed in `STRUST`.

**Resolution:** Download all latest root CA certificates from [Google Trust Services repository](https://pki.goog/repository/) and upload them in your `STRUST` transaction. Make sure that you don't use existing certificates. For information about how to do this, see [Authenticate with JSON Web Tokens: Set up TLS/SSL certificates](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt#jwt-set-up-ssl) or [Authenticate with access tokens: Set up TLS/SSL certificates](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token#set_up_tlsssl_certificates_and_https).

### Issue: `/GOOG/MSG : 400 - Schema mismatch for table TABLE_ID. Please delete the schema from Pub/Sub and try again.`

**Issue** : You cannot replicate data from your source SAP table.

**Cause** : This error occurs when the existing Pub/Sub schema for a specific table does not match the schema derived from the SAP table definition. This can also happen if there are inconsistencies in the time partitioning settings between the two schemas.

**Resolution** : To resolve the issue, complete the following steps:

  1. Delete the existing schema for the specified table from Pub/Sub. For information about how to delete a schema from Pub/Sub, see [Delete a schema](https://docs.cloud.google.com/pubsub/docs/delete-schema).

  2. Rerun your replication. The system automatically recreates the schema based on the SAP table definition.




### Issue: `/GOOG/MSG : 400 - Compatibility checking failed to commit a schema revision for (schema="SCHEMA_NAME"). (reason="Revision is incompatible with previous revision: SCHEMA_NAME. Failed with error").`

**Issue** : You cannot replicate data from your source SAP table.

**Cause** : Pub/Sub rejected the new schema revision because it is incompatible with the previous schema revision.

**Resolution** : To resolve this issue, make sure that the schema changes in the transaction `/GOOG/SLT_SETTINGS` are [compatible](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility) with the Avro schema in Pub/Sub.

Verify that the Avro field mappings are in line with the [Schema Resolution](https://avro.apache.org/docs/++version++/specification/#schema-resolution).

### Issue: `/GOOG/MSG : 429 - You have exceeded your revisions per schema quota (schema="SCHEMA_NAME").`

**Issue** : You cannot replicate data from your source SAP table.

**Cause** : Pub/Sub schema has exceeded the maximum allowed number of revisions.

**Resolution** : To fix this, you need to either delete any unused existing schema revisions or delete the entire schema, and then configure a new schema in the `/GOOG/SLT_SETTINGS` transaction. For more information, see [Manage Pub/Sub schema for table structure changes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#handle-pubsub-schema-changes).

### Issue: `/GOOG/MSG : 400 - Incompatible schema type for field FIELD_NAME: AVRO_TYPE vs. BQ_TYPE`

**Issue** : You cannot replicate data from your source SAP table.

**Cause** : This issue error occurs when the data type mapping for a specific field between the Avro schema and the BigQuery target table schema is incompatible.

**Resolution** : To resolve the issue, complete the following steps:

  1. In the `/GOOG/SLT_SETTINGS` transaction, fix the field mappings so that Avro and BigQuery data types are compatible with each other.

For more information, see [Customize the default field mapping](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#field-mapping).

For information about schema compatibility between Avro types and BigQuery data types, see [Schema compatibility](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).

  2. Rerun your replication.




### Issue: `/GOOG/SLT : 461 - Unicode Conversion Issue: ERROR_TEXT`

**Issue:** Data replication failed with the error message `/GOOG/SLT : 461 - Unicode Conversion Issue:ERROR_TEXT`.

**Cause:** When you replicate data from an SAP source system to Google Cloud by using the BigQuery Connector for SAP with CDC and Pub/Sub, this error occurs if the source data contains characters that cannot be converted into the required UTF-8 Unicode format.

**Resolution:** To resolve this issue, identify and correct the unprocessed records:

  1. To identify the exact data that didn't replicate, use the unprocessed records captured in the SLT logging table: 
     1. In the SAP GUI, execute the `LTRC` transaction code.
     2. Open the mass transfer ID for the affected replication.
     3. Go to the **Expert Functions** tab.
     4. Select the **View Unprocessed Logging Table Records** option to retrieve the records.
  2. Examine the records displayed to validate the data.
  3. Correct the corrupted or unconvertible data directly in the source SAP table.



### Issue: Replication to Cloud Storage fails due to permission error or invalid path

**Issue:** When you use the connector for file-based replication to Cloud Storage, the replication job fails with a `403` error message. For example:

  * `/GOOG/MSG : 403 - SERVICE_ACCOUNT_NAME does not have storage.objects.create access to the Google Cloud Storage object.`
  * `/GOOG/MSG : 403 - SERVICE_ACCOUNT_NAME does not have storage.buckets.get access to the Google Cloud Storage bucket.`



**Cause:** This issue can be caused by the following circumstances:

  * **Insufficient permissions** : The IAM service account that the connector is using lacks the necessary roles to verify the bucket's existence or upload the JSON files.
  * **Missing infrastructure** : In transaction `/GOOG/SLT_SETTINGS`, the Cloud Storage URI that you specified in the **Cloud Storage URI** field doesn't exist. Replication fails in such cases because BigQuery Connector for SAP does not create Cloud Storage buckets or folders.



**Resolution:** To resolve this issue, verify and correct the following:

  * **IAM roles** :

    1. Verify that the service account specified in your Client Key configuration has the following IAM roles for the target bucket: 
       * **Storage Object Creator** (`roles/storage.objectCreator`): Required to upload the JSON files.
       * **Storage Viewer** (`roles/storage.viewer`): Required to verify the existence of the bucket and folder structure.
    2. If the service account lacks any of these roles, then grant the required roles. For more information, see [Grant or revoke multiple IAM roles using the Google Cloud console](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#multiple-roles-console).
    3. After granting the required roles, restart the replication.
  * **Cloud Storage path** :

    1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

    2. Confirm that the bucket name and the entire folder hierarchy exactly match the path entered in the `/GOOG/SLT_SETTINGS` transaction.

    3. If any part of the path is missing, then manually create the required bucket or folders. When creating these artifacts, ensure that they exactly match the path specified in the **Cloud Storage URI** field in transaction `/GOOG/SLT_SETTINGS`. For more information, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) and [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).

    4. Restart the replication.




## Common operational issues

This section contains resolutions for common issues that can occur after the initial setup of BigQuery Connector for SAP.

### Issue: Too many API requests per user per method for this user_method (TableService.getTable)

**Issue:** Your replication job failed due to BigQuery API quota limit error.

**Cause:** For [streaming data replication to BigQuery](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#streaming-api-insert-only), the connector performs `tables.get` calls to the BigQuery API to verify table existence and retrieve schema definitions. In high-volume replication scenarios, these frequent requests can exceed the BigQuery API quota for the `tables.get` method.

**Resolution:** To resolve the quota limit error, enable table schema caching to reduce the number of `tables.get` calls to the BigQuery API.

For information about how to enable table schema caching, see [Table schema caching](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#table-schema-caching).

### Issue: Missing records in BigQuery after SAP LT Replication Server DMIS upgrade

**Issue** : After upgrading to SAP LT Replication Server **DMIS 2018 SP12-SP13** or **DMIS 2020 SP08-SP09** , you might find missing records in BigQuery. You can identify this issue by observing the following:

  * Records are missing in the target BigQuery table, but the SAP LT Replication Server application log does not show any errors.
  * Because there are no errors, SAP LT Replication Server does not retain and retrigger the missing entries.
  * In Cloud Logging and SAP HTTP Trace Files, you might find `503 service unavailable` errors. However, these errors are not logged in the SAP LT Replication Server application log.



**Cause** : In SAP LT Replication Server **DMIS 2018 SP12-SP13** or **DMIS 2020 SP08-SP09** , the generated code does not include necessary error handling logic.

**Resolution** : To resolve this issue, follow the instructions provided in the [SAP Note 3631963 - Missing records in the target when using BAdi scenario](https://me.sap.com/notes/0003631963). If this note is not available in your environment, then [contact SAP](https://docs.cloud.google.com/sap/docs/getting-support-from-sap) to obtain the note.

Because this issue is related to the SAP LT Replication Server's internal handling, it doesn't require any action or fix from Google Cloud.

### Issue: `503 - Service is unavailable Please retry`

**Issue:** Data replication to BigQuery is interrupted, and the application logs show the error message `503 - Service is unavailable Please retry`.

**Cause:** This error indicates a temporary issue with the BigQuery service.

**Resolution:** No manual intervention is required. The SAP LT Replication Server automatically retries sending any records that fail with this error. For more details on BigQuery errors, see [BigQuery error messages](https://docs.cloud.google.com/bigquery/docs/error-messages#errortable).

### Issue: Empty source tables in SAP are not created in the BigQuery dataset

**Issue:** Empty source tables in SAP are not created in the BigQuery dataset.

**Cause:** For empty source tables in SAP, the SAP SLT prevents the creation of target tables in BigQuery.

**Resolution:** To create target tables in the BigQuery dataset for empty source tables in SAP, you can use the Create Table tool. For information about how to run the Create Table tool, see [Create Table tool](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#create-table-tool).

### Issue: Incorrect number of writes in BigQuery

**Issue:** The number of records that are written to BigQuery is higher than the number of records that are shown in the SAP LT Replication Server logs.

**Cause:** This can have more than one cause, including transitory connection issues that cause SAP LT Replication Server to send records more than once or the fact that the BigQuery table accepts only inserts, and each change to a single record in the source is inserted as a separate entry in the target table.

**Resolution:** If the difference in record counts is not extreme and there are not fewer records in BigQuery than in the source table, this is expected behavior and not a problem.

To accurately reconcile the number of records in BigQuery with the number of records in the source table, query the BigQuery table as described in [SQL queries for record counts](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#query-record-counts).

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

For more information about configuring fields and partitions in a target BigQuery table, see [BigQuery replication configurations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#bq-replication-config).

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
  * If the error occurred due to a mismatch between the data and the data type, then use transaction `/GOOG/SLT_SETTINGS` to specify an appropriate data type. For more information about data type mapping, see [Data type mapping](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#data-type-mapping).



### Issue: The value of a field displayed in the transaction `SE16` or `SE16N` is different from the value that is shown in BigQuery

**Issue** : When comparing data in the SAP transaction `SE16` or `SE16N` with BigQuery, you might encounter the following discrepancies:

  * The value of a field displayed in the transaction `SE16` or `SE16N` might differ from its corresponding value in BigQuery.
  * The value of a field in the transaction `SE16` or `SE16N` might appear blank, while the corresponding field contains a value in BigQuery.



**Cause** : You notice this behavior because of the following reasons:

#### Standard SLT behavior with SAP compatibility views

In the SAP S/4HANA source system, tables such as `MARD`, `MARC`, `MBEW`, and `MBEWH`, have [compatibility views](https://help.sap.com/doc/9d634180094347038e7b8c96661dc36b/3.0.11/en-US/Compatibility_Views_and_SAP_LT_Replication_Server.pdf) that display values in transaction `SE16` or `SE16N`. For such tables, the values displayed in transaction `SE16` or `SE16N` are calculated within the compatibility views using join conditions, which include several other underlying tables.

When a table with a compatibility view is configured in SLT for replication to BigQuery, SLT does not replicate the data from the compatibility view. Instead, SLT replicates data from each of the underlying tables separately, and hence you might notice that some fields have different values in `SE16` or `SE16N` as compared to what is shown in BigQuery. This is a standard SLT behavior.

#### Unconverted values sent from the database to BigQuery

SLT extracts the unconverted values directly from the database and sends them to BigQuery following the data conversion logic maintained by you or the [default mapping rules](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#data-type-mapping). Consequently, even if a field appears blank or shows a different value in the transaction `SE16` or `SE16N`, the underlying unconverted value is sent to BigQuery.

For example, in the database, unconverted material numbers usually have leading zeros. The conversion process removes leading zeros before displaying the value in `SE16N`. To view the original value with leading zeros, double-click the entry in `SE16N`. For more information, see Blank fields or different values shown in `SE16` or `SE16N` due to unconverted values sent from the database to BigQuery.

**Resolution** : To resolve the issue, perform the following actions as appropriate:

#### Different field values shown in `SE16` or `SE16N` due to standard SLT behavior with SAP compatibility views

To resolve the issue, complete the following steps:

  1. In the SAP GUI, execute transaction code `LTRS`.
  2. Select the mass transfer settings for BigQuery replication.
  3. Go to **Advanced Replication Settings > Table Settings**.
  4. Select the table that uses compatibility views. If the table that you need isn't listed, then add the table.
  5. In the **Processing Settings** section, enter values for the following fields:

     * **View for Initial Load** : the value of compatibility view for the table from `SE16` or `SE16N`.
     * **View for Replication** : the value of compatibility view for the table from `SE16` or `SE16N`.
  6. Save the settings.




Alternatively, replicate all underlying tables of the compatibility view to BigQuery. In BigQuery, join these tables using the same join conditions as the compatibility view.

To find the compatibility view for a table, do the following:

  1. In the SAP GUI, execute the transaction code `SE16` or `SE16N`.
  2. In the **Search in Table** field, enter `DD02L`, and then press **Enter**.
  3. In the **Table Name** or **TABNAME** field, enter the name of the table you need to find the compatibility view for.
  4. Click the **Execute** button. The column **View Name** or **VIEWREF** shows the compatibility view, if one exists for the table.



For more information from SAP about some well known tables and their compatibility views, see [SAP Note 2595627 - Accessing table from SE16/SE16N shows different results to SAP HANA database](https://launchpad.support.sap.com/#/notes/2595627).

#### Blank fields or different values shown in `SE16` or `SE16N` due to unconverted values sent from the database to BigQuery

To resolve the issue, complete the following steps:

  1. In the SAP GUI, execute the transaction code `SE16N`.
  2. In the **Table Name** field, enter the name of the SAP table that you want to inspect, and then press **Enter**.
  3. Locate the row where a field displays blank or shows a different value.
  4. Double-click the specific row that you have identified.
  5. In the detailed view of the row, look for the column **Value Unconverted**. This column shows the unconverted value as it is stored in the underlying database for the corresponding field.



### Issue: After upgrading your SLT or SAP source system, you cannot maintain compatibility views in the `LTRS` transaction

**Issue:** After upgrading your SLT or SAP source system, you cannot maintain compatibility views in the `LTRS` transaction.

**Cause:** This issue occurs because SAP switched the Change Data Capture (CDC) mechanism to a different value after the upgrade.

**Resolution:** To maintain compatibility views in the `LTRS` transaction after an upgrade, follow the instructions in the SAP note [3169933 - What is report IUUC_REPL_SWITCH_REC_MCHNSM ? - SLT](https://me.sap.com/notes/3169933).

### Issue: `Failed to create proxy table TARGET_TABLE_NAME for object SOURCE_TABLE_NAME`

**Issue:** While transferring data from SAP HANA to BigQuery by using the BigQuery Connector for SAP, table loading failed with the error message `Failed to create proxy table TARGET_TABLE_NAME for object SOURCE_TABLE_NAME`.

**Cause:** The number of characters in one or more fields of the source table exceeds the 30-character restriction set by SLT.

**Resolution:** Try the following resolutions:

  * If the number of characters in the key fields of a table exceeds 30, then you cannot load or replicate such tables. This is a known limitation of SLT.
  * If the number of characters in other fields of a table exceeds 30, then create a view to map the field names that exceed 30 characters to shorter field names.



For more information, see the SAP Note [1768805 - SAP Landscape Transformation Replication Server (SLT): Non ABAP-based Sources](https://me.sap.com/notes/1768805/E).

### Issue: `NULL` fields found in replicated data in BigQuery

**Issue:** When you replicate data to BigQuery by using the BigQuery Connector for SAP, you see `NULL` values in your BigQuery tables.

**Cause:** This happens when the **Send Uncompressed Flag** flag is disabled in your BigQuery Connector for SAP settings, which is the default. When this flag is disabled, the BigQuery Connector for SAP omits empty fields from source records sent to BigQuery. Consequently, BigQuery initializes these omitted fields as `NULL` in the target table.

**Resolution:** To resolve this issue, disable record compression by selecting the **Send Uncompressed Flag** in your BigQuery settings.

Selecting the **Send Uncompressed Flag** can negatively impact replication performance. For optimal performance, avoid disabling record compression at the table level. If you only require uncompressed data for specific fields, then enable the **Send Uncompressed Flag** for those individual fields at the field level instead.

For more details, see [Record compression](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#record_compression).

## Get support

If you need help resolving problems with replication and the BigQuery Connector for SAP, then collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/bq-connector/latest/getting-support-diag-info) and contact Cloud Customer Care.

For more information about contacting Cloud Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
