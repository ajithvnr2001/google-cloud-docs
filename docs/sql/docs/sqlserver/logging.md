---
url: https://docs.cloud.google.com/sql/docs/sqlserver/logging/
title: View instance logs \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:40.272765+00:00
---

# View instance logs  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  View instance logs Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/logging "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/logging "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to find and use Cloud Logging to view and query logs for your Cloud SQL instance.

Cloud SQL uses Cloud Logging. See the [cloud logging documentation](https://docs.cloud.google.com/logging/docs) for complete information and review the [Cloud SQL sample queries](https://docs.cloud.google.com/logging/docs/view/query-library-preview#sql-filters).

## View logs

To view logs for your Cloud SQL instance log entries:

### Console

  1. In the Google Cloud console, go to the **Cloud Logging** page.

[Go to Cloud Logging](https://console.cloud.google.com/logs/query)

  2. Select an existing Cloud SQL project at the top of the page.
  3. In the Query builder, add the following:
     * Resource: select **Cloud SQL Database**. In the dialog, select a Cloud SQL instance.
     * Log names: scroll to the Cloud SQL section and select appropriate log files for your instance. For example: 
       * cloudsql.googleapis.com/sqlagent.out
       * cloudsql.googleapis.com/sqlserver.err
     * Severity: select a log level.
     * Time range: select a preset or create a custom range.



### gcloud

Use the [`gcloud logging`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view log entries. In the example below, replace `PROJECT_ID`. The [`limit`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--limit) flag is an optional parameter that indicates the maximum number of entries to return.
    
    
    gcloud logging read "resource.type=cloudsql_database" \
    --project=PROJECT-ID \
    --limit=10 \
    --format=json

## View instance operations log

You can view the logs for an instance in the **Operations** pane. The **Operations** pane logs every operation performed on the instance with the following information:

  * The time the operation completed, reported in your local time zone.
  * The type of operation.
  * The status of the operation.
  * A message describing the outcome the operation.



If the operation fails, you can use the message to troubleshoot the problem.

**To view an instance operations log:**

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Operations** to change to the pane showing the operation log.

**Note:** The operations log does not include operations performed using external management tools, such as SQL Server command-line tools. Only user management and password change operations performed using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the Cloud SQL Admin API appear in the operations log. 

## View application logs

Applications that connect to Cloud SQL store their logs in different locations.

### App Engine (flexible environment)

In **Compute > App Engine > Services**:

  * In the list of services, find your service.
  * Click on the **Tools** dropdown.
  * Select **logs**



In the **Operations > Logging > Logs explorer** section of Google Cloud console, use the following query:
    
    
    resource.type="gae_app"
    resource.labels.module_id="default"
    

### Cloud Run

View the logs in the Cloud Run **Logs Explorer** section of the Google Cloud console. Note that Cloud Run reports only error messages from the Cloud SQL Auth Proxy. Use a query like the following:
    
    
    resource.type="cloud_run_revision"
    resource.labels.service_name="$SERVICE_NAME"
    resource.labels.revision_name="$REVISION_NAME"
    

### Cloud SQL Auth Proxy

In **Operations > Logging > Logs explorer**, use the following query:
    
    
    log_id("appengine.googleapis.com/cloud-sql-proxy")
    

## View audit logs

You can view the following types of audit logs for your Cloud SQL instances:

  * Admin Activity: include administrator operations that write metadata or configuration information. You can't deactivate these logs.
  * Data Access: include administrator operations that read metadata or configuration information. These logs also include operations that read or write user-provided data. To receive Data Access audit logs, you must [enable them explicitly](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable).
  * System Event: identify automated actions in Google Cloud that modify the configuration of resources. You can't deactivate these logs.



For more information about viewing Admin Activity, Data Access, and System Event audit logs, see [View logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging#viewing_logs).

## Pricing

For more information about Cloud Logging pricing, see [Cloud Logging pricing summary](https://cloud.google.com/products/observability/pricing#logs-costs).

## Troubleshoot

Issue | Troubleshooting  
Audit logs are not found. | Data-Access logs are only written if the operation is an authenticated user-driven API call that creates, modifies, or reads user-created data, or if the operation accesses configuration files or metadata of resources.   
Operations information is not found in logs. | You want to find more information about an operation. For example, a user was deleted but you can't find out who did it. The logs show the operation started but don't provide any more information. You must [enable audit logging](https://docs.cloud.google.com/logging/docs/audit) for detailed and personal identifying information (PII) like this to be logged.  
Some logs are filtered from the `error.log` log of a Cloud SQL for SQL Server instance.  | Filtered logs include AD logs without timestamps, and include: `Login failed for user 'x'. Reason: Token-based server access validation failed with an infrastructure error. Login lacks connect endpoint permission. [CLIENT: 127.0.0.1]`. These logs are filtered because they potentially can cause confusion.   
Log files are hard to read. | You'd rather view the logs as json or text.You can use the [ `gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command along with linux post-processing commands to download the logs. To download the logs as JSON:
    
    
    gcloud logging read \
    "resource.type=cloudsql_database \
    AND logName=projects/PROJECT_ID \
    /logs/cloudsql.googleapis.com%2FLOG_NAME" \
    --format json \
    --project=PROJECT_ID \
    --freshness="1d" \
    > downloaded-log.json
        

To download the logs as TEXT:
    
    
    gcloud logging read \
    "resource.type=cloudsql_database \
    AND logName=projects/PROJECT_ID \
    /logs/cloudsql.googleapis.com%2FLOG_NAME" \
    --format json \
    --project=PROJECT_ID \
    --freshness="1d"| jq -rnc --stream 'fromstream(1|truncate_stream(inputs)) \
    | .textPayload' \
    --order=asc
    > downloaded-log.txt
         
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
