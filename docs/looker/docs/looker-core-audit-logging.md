---
url: https://docs.cloud.google.com/looker/docs/looker-core-audit-logging/
title: Looker audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:23.687323+00:00
---

# Looker audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Looker (Google Cloud core) audit logging

This document describes the audit logs created by Looker (Google Cloud core) as part of [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

## Overview

Google Cloud services write audit logs to help you answer the questions, "Who did what, where, and when?" within your Google Cloud resources.

Your Google Cloud projects contain only the audit logs for resources that are directly within the Google Cloud project. Other Google Cloud resources, such as folders, organizations, and billing accounts, contain the audit logs for the entity itself.

For a general overview of Cloud Audit Logs, see [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit). For a deeper understanding of the audit log format, see [Understand audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs).

## Available audit logs

The following types of audit logs are available for Looker (Google Cloud core):

  * Admin Activity audit logs 

Includes "admin write" operations that write metadata or configuration information. 

You can't disable Admin Activity audit logs. 

  * Data Access audit logs 

Includes "admin read" operations that read metadata or configuration information. Also includes "data read" and "data write" operations that read or write user-provided data. 

To receive Data Access audit logs, you must [ explicitly enable](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) them. 

  * System Event audit logs 

Identifies automated Google Cloud actions that modify the configuration of resources. 

You can't disable System Event audit logs. 




For fuller descriptions of the audit log types, see [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types).

## Audited operations

The following table summarizes which API operations correspond to each audit log type in Looker (Google Cloud core):

Audit logs category | Looker (Google Cloud core) operations  
---|---  
Admin Activity (ADMIN_WRITE) audit logs | 

  * CreateInstance
  * DeleteInstance
  * UpdateInstance
  * RestartInstance
  * lookerapp.api.add_group_group
  * lookerapp.api.add_group_user
  * lookerapp.api.create_connection
  * lookerapp.api.delete_group
  * lookerapp.api.delete_group_user
  * lookerapp.api.delete_user
  * lookerapp.api.delete_user_attribute_user_value
  * lookerapp.api.delete_user_session
  * lookerapp.api.set_setting
  * lookerapp.api.set_user_roles
  * lookerapp.api.update_connection
  * lookerapp.api.update_group
  * lookerapp.api.update_user
  * lookerapp.event.settings.disable_login_notification
  * lookerapp.event.settings.enable_login_notification
  * lookerapp.event.settings.remove_login_notification_text
  * lookerapp.event.settings.set_login_notification_text

  
Data Access (ADMIN_READ) audit logs | 

  * ListInstance
  * GetInstance
  * lookerapp.api.search_credentials_email

  
Data Access (DATA_READ) audit logs | 

  * lookerapp.api.all_connections
  * lookerapp.api.all_group_groups
  * lookerapp.api.all_looks
  * lookerapp.api.all_projects
  * lookerapp.api.all_users
  * lookerapp.api.board
  * lookerapp.api.connection
  * lookerapp.api.dashboard
  * lookerapp.api.dashboard_element
  * lookerapp.api.group
  * lookerapp.api.look
  * lookerapp.api.me
  * lookerapp.api.merge_query
  * lookerapp.api.project
  * lookerapp.api.query
  * lookerapp.api.query_aggregate_table_lookml
  * lookerapp.api.query_cost
  * lookerapp.api.query_task
  * lookerapp.api.role
  * lookerapp.api.run_look
  * lookerapp.api.run_query
  * lookerapp.api.search_boards
  * lookerapp.api.search_connections
  * lookerapp.api.search_dashboards
  * lookerapp.api.search_groups
  * lookerapp.api.search_looks
  * lookerapp.api.search_projects
  * lookerapp.api.search_queries
  * lookerapp.api.search_roles
  * lookerapp.api.search_scheduled_plans
  * lookerapp.api.search_users
  * lookerapp.api.session
  * lookerapp.api.sql_query
  * lookerapp.api.user
  * lookerapp.api.user_attribute
  * lookerapp.api.user_roles

  
Data Access (DATA_WRITE) audit logs | 

  * lookerapp.api.create_board
  * lookerapp.api.create_dashboard
  * lookerapp.api.create_group
  * lookerapp.api.create_look
  * lookerapp.api.create_merge_query
  * lookerapp.api.create_project
  * lookerapp.api.create_query
  * lookerapp.api.create_query_task
  * lookerapp.api.create_role
  * lookerapp.api.create_scheduled_plan
  * lookerapp.api.create_sql_query
  * lookerapp.api.create_user
  * lookerapp.api.create_user_attribute
  * lookerapp.api.delete_board
  * lookerapp.api.delete_connection
  * lookerapp.api.delete_dashboard
  * lookerapp.api.delete_git_branch
  * lookerapp.api.delete_look
  * lookerapp.api.delete_project
  * lookerapp.api.delete_repository_credential
  * lookerapp.api.delete_role
  * lookerapp.api.delete_scheduled_plan
  * lookerapp.api.delete_user_attribute
  * lookerapp.api.deploy_to_production
  * lookerapp.api.kill_query
  * lookerapp.api.login
  * lookerapp.api.logout
  * lookerapp.api.run_inline_query
  * lookerapp.api.run_inline_query_v2
  * lookerapp.api.run_sql_query
  * lookerapp.api.scheduled_plan_run_once
  * lookerapp.api.set_user_attribute_group_values
  * lookerapp.api.update_board
  * lookerapp.api.update_dashboard
  * lookerapp.api.update_look
  * lookerapp.api.update_project
  * lookerapp.api.update_role
  * lookerapp.api.update_scheduled_plan
  * lookerapp.api.update_session
  * lookerapp.api.update_user_attribute
  * lookerapp.api.validate_project
  * lookerapp.event.authentication.login
  * lookerapp.event.authentication.login_failure
  * lookerapp.event.scheduler.scheduler_deliver
  * lookerapp.event.scheduler.scheduler_execute

  
System Event audit logs | 

  * lookerapp.event.authentication.inactivity_logout

  
  
In addition to the operations listed in the preceding table, all [Looker 4.0 API methods](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) and [Looker events](https://docs.cloud.google.com/looker/docs/events) may be audited.

## Audit log format

Audit log entries include the following objects:

  * The log entry itself, which is an object of type [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). Useful fields include the following:

    * The `logName` contains the resource ID and audit log type. The resource is a project, folder, organization, or billing account.
    * The `resource` contains the target of the audited operation.
    * The `timeStamp` contains the time of the audited operation.
    * The `protoPayload` contains the audited information.
  * The audit logging data, which is an [`AuditLog`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) object held in the `protoPayload` field of the log entry.

    * The `@type` field is set to `"type.googleapis.com/google.cloud.audit.AuditLog"`.
    * The `serviceName` field identifies the service that wrote the audit log. The format of this field is service specific.
  * Optional service-specific audit information, which is a service-specific object. For earlier integrations, this object is held in the `serviceData` field of the `AuditLog` object; later integrations use the `metadata` field.




For other fields in these objects, and how to interpret them, review [Understand audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs).

### Log name

Cloud Audit Logs log names include resource identifiers indicating the Google Cloud project or other Google Cloud entity that owns the audit logs, and whether the log contains Admin Activity, Data Access, Policy Denied, or System Event audit logging data.

The following are the audit log names, including variables for the resource identifiers:
    
    
       projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity
       projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access
       projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
       projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    
       folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Factivity
       folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fdata_access
       folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
       folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    
       billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com%2Factivity
       billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com%2Fdata_access
       billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
       billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    
       organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity
       organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fdata_access
       organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
       organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    

**Note:** The part of the log name following `/logs/` must be URL-encoded. The forward-slash character, `/`, must be written as `%2F`.

### Service name

Looker (Google Cloud core) audit logs use the service name `looker.googleapis.com`. 

For a list of all the Cloud Logging API service names and their corresponding monitored resource type, see [Map services to resources](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#service-names).

### Resource types

Looker (Google Cloud core) audit logs use the resource type `audited_resource` for all audit logs. 

For a list of all the Cloud Logging monitored resource types and descriptive information, see [Monitored resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

### Caller identities

The IP address of the caller is held in the `RequestMetadata.caller_ip` field of the [`AuditLog`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) object. Logging might redact certain caller identities and IP addresses.

For information about what information is redacted in audit logs, see [Caller identities in audit logs](https://docs.cloud.google.com/logging/docs/audit#user-id).

## Enable audit logging

System Event audit logs are always enabled; you can't disable them.

Admin Activity audit logs are always enabled; you can't disable them.

Data Access audit logs are disabled by default and aren't written unless explicitly enabled (the exception is Data Access audit logs for BigQuery, which can't be disabled).

For information about enabling some or all of your Data Access audit logs, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## Permissions and roles

[IAM](https://docs.cloud.google.com/iam/docs) permissions and roles determine your ability to access audit logs data in Google Cloud resources.

When deciding which [Logging-specific permissions and roles](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) apply to your use case, consider the following:

  * The Logs Viewer role (`roles/logging.viewer`) gives you read-only access to Admin Activity, Policy Denied, and System Event audit logs. If you have just this role, you cannot view Data Access audit logs that are in the `_Default` bucket.

  * The Private Logs Viewer role`(roles/logging.privateLogViewer`) includes the permissions contained in `roles/logging.viewer`, plus the ability to read Data Access audit logs in the `_Default` bucket.

Note that if these private logs are stored in user-defined buckets, then any user who has permissions to read logs in those buckets can read the private logs. For more information about log buckets, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).




For more information about the IAM permissions and roles that apply to audit logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View logs

You can query for all audit logs or you can query for logs by their audit log name. The audit log name includes the [resource identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project, folder, billing account, or organization for which you want to view audit logging information. Your queries can specify indexed [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields. For more information about querying your logs, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries)

The Logs Explorer lets you view filter individual log entries. If you want to use SQL to analyze groups of log entries, then use the **Log Analytics** page. For more information, see:

  * [Query and view logs in Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).
  * [Sample queries for security insights](https://docs.cloud.google.com/logging/docs/analyze/analyze-audit-logs).
  * [Chart query results](https://docs.cloud.google.com/logging/docs/analyze/charts).



Most audit logs can be viewed in Cloud Logging by using the Google Cloud console, the Google Cloud CLI, or the Logging API. However, for audit logs related to billing, you can only use the Google Cloud CLI or the Logging API.

###  Console 

In the Google Cloud console, you can use the Logs Explorer to retrieve your audit log entries for your Google Cloud project, folder, or organization:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select an existing Google Cloud project, folder, or organization.

  3. To display all audit logs, enter either of the following queries into the query-editor field, and then click **Run query** :
         
         logName:"cloudaudit.googleapis.com"
         
         
         protoPayload."@type"="type.googleapis.com/google.cloud.audit.AuditLog"
         

  4. To display the audit logs for a specific resource and audit log type, in the **Query builder** pane, do the following:

     * In **Resource type** , select the Google Cloud resource whose audit logs you want to see.

     * In **Log name** , select the audit log type that you want to see:

       * For Admin Activity audit logs, select **activity**.
       * For Data Access audit logs, select **data_access**.
       * For System Event audit logs, select **system_event**.
       * For Policy Denied audit logs, select **policy**.
     * Click **Run query**.

If you don't see these options, then there aren't any audit logs of that type available in the Google Cloud project, folder, or organization.

If you're experiencing issues when trying to view logs in the Logs Explorer, see the [troubleshooting](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#troubleshooting) information.

For more information about querying by using the Logs Explorer, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).




###  gcloud 

The Google Cloud CLI provides a command-line interface to the Logging API. Supply a valid resource identifier in each of the log names. For example, if your query includes a PROJECT_ID, then the project identifier you supply must refer to the currently selected Google Cloud project.

To read your Google Cloud project-level audit log entries, run the following command:
    
    
    gcloud logging read "logName : projects/PROJECT_ID/logs/cloudaudit.googleapis.com" \
        --project=PROJECT_ID
    

To read your folder-level audit log entries, run the following command:
    
    
    gcloud logging read "logName : folders/FOLDER_ID/logs/cloudaudit.googleapis.com" \
        --folder=FOLDER_ID
    

To read your organization-level audit log entries, run the following command:
    
    
    gcloud logging read "logName : organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com" \
        --organization=ORGANIZATION_ID
    

To read your Cloud Billing account-level audit log entries, run the following command:
    
    
    gcloud logging read "logName : billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com" \
        --billing-account=BILLING_ACCOUNT_ID
    

Add the [`--freshness` flag](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--freshness) to your command to read logs that are more than 1 day old.

For more information about using the gcloud CLI, see [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).

###  REST 

When building your queries, supply a valid resource identifier in each of the log names. For example, if your query includes a PROJECT_ID, then the project identifier you supply must refer to the currently selected Google Cloud project.

For example, to use the Logging API to view your project-level audit log entries, do the following:

  1. Go to the **Try this API** section in the documentation for the [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method.

  2. Put the following into the **Request body** part of the **Try this API** form. Clicking this [prepopulated form](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list?apix_params=%7B%22resource%22%3A%7B%22resourceNames%22%3A%5B%22projects%2F%5BPROJECT_ID%5D%22%5D%2C%22pageSize%22%3A5%2C%22filter%22%3A%22logName%3D\(projects%2F%5BPROJECT_ID%5D%2Flogs%2Fcloudaudit.googleapis.com%252Factivity%20OR%20projects%2F%5BPROJECT_ID%5D%2Flogs%2Fcloudaudit.googleapis.com%252Fsystem_events%20OR%20projects%2F%5BPROJECT_ID%5D%2Flogs%2Fcloudaudit.googleapis.com%252Fdata_access\)%22%7D%7D) automatically fills the request body, but you need to supply a valid PROJECT_ID in each of the log names.
         
         {
           "resourceNames": [
             "projects/PROJECT_ID"
           ],
           "pageSize": 5,
           "filter": "logName : projects/PROJECT_ID/logs/cloudaudit.googleapis.com"
         }
         

  3. Click **Execute**.




For example, to view all the project-level audit logs for Looker (Google Cloud core), use the following query, supplying a valid resource identifier in each of the log names: 
    
    
    logName=("projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    OR "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access"
    OR "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
    OR "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fpolicy")
    protoPayload.serviceName="looker.googleapis.com"

## Sample queries

To use the sample queries in the following table, complete these steps:

  1. Replace the variables in the query expression with your own project information, then copy the expression using the clipboard icon _content_copy_.

  2. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  3. Enable **Show query** to open the query-editor field, then paste the expression into the query-editor field:

![The query editor where you enter sample queries.](https://docs.cloud.google.com/static/logging/docs/images/query-pane-2.png)

  4. Click **Run query**. Logs that match your query are listed in the **Query results** pane.




To find audit logs for Looker (Google Cloud core), use the following queries in the Logs Explorer:

Query/filter name | Expression | Audit log type  
---|---|---  
MCP tool settings changes | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    protoPayload.serviceName="looker.googleapis.com"
    protoPayload.methodName="lookerapp.api.set_setting"
    mcp_tools

| Admin Activity  
Managed MCP server interactions | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    OR logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access"
    OR logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
    OR logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fpolicy"
    protoPayload.serviceName="looker.googleapis.com"
    protoPayload.metadata.event.attributes.value="Managed MCP server"

| All  
  
## Route audit logs

You can [route audit logs](https://docs.cloud.google.com/logging/docs/routing/overview) to supported destinations in the same way that you can route other kinds of logs. Here are some reasons you might want to route your audit logs:

  * To keep audit logs for a longer period of time or to use more powerful search capabilities, you can route copies of your audit logs to Cloud Storage, BigQuery, or Pub/Sub. Using Pub/Sub, you can route to other applications, other repositories, and to third parties.

  * To manage your audit logs across an entire organization, you can create [aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) that can route logs from any or all Google Cloud projects in the organization.



  * If your enabled Data Access audit logs are pushing your Google Cloud projects over your log allotments, you can create sinks that exclude the Data Access audit logs from Logging.



For instructions about routing logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## Pricing

For more information about pricing, see the Cloud Logging sections in the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## Limitations

Looker (Google Cloud core) audit logging has the following limitations:

  * Undefined HTTP request parameters are redacted by default. For documentation on each Looker API endpoint, see the [Looker API documentation](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest).
  * Looker (Google Cloud core) supports redacting entire fields, not specific nested fields.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
