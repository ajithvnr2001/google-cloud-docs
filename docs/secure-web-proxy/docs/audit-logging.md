---
url: https://docs.cloud.google.com/secure-web-proxy/docs/audit-logging/
title: Secure Web Proxy audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:50.816679+00:00
---

# Secure Web Proxy audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Secure Web Proxy audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Secure Web Proxy. Google Cloud services generate audit logs that record administrative and access activities for your Google Cloud resources. For more information about Cloud Audit Logs, see the following pages:

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://cloud.google.com/products/observability/pricing#cloud-logging-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Cloud Audit Logs

Cloud Audit Logs for Secure Web Proxy tracks the following activities and changes:

  * Information related to the API calls made to the infrastructure and proxy setup, the creation and modification of policies, and monitoring checks. To capture the interactions, Cloud Audit Logs uses Google Cloud CLI commands, the [Network Services API](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-services/rest), and the [Network Security API](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest).

  * Information related to creating and deleting Secure Web Proxy instances, modifying settings, and applying updates. Google Cloud console logs capture console activity that's related to the Secure Web Proxy configuration.

  * Insights into changes made to the Secure Web Proxy infrastructure.

  * Details about adjustments made to Secure Web Proxy settings, rules, and parameters that shape the behavior of Secure Web Proxy.

  * Records of modifications to user privileges and access controls within Secure Web Proxy.

  * Documentation about policy modifications, including the capture of pre-edit and post-edit details.




## Types of audit logs

Secure Web Proxy writes two types of audit logs: Admin Activity audit logs and Data Access audit logs. For more information about various audit log types, see [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types).

### Admin Activity audit logs

[Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) record API calls and other administrative actions that modify the configuration or metadata of your Secure Web Proxy resources. Admin Activity logs are always enabled.

These logs contain information about the following operations:

  * Creating, updating, or deleting `Gateway`, `GatewaySecurityPolicy`, `GatewaySecurityPolicyRule`, `TlsInspectionPolicy`, and `UrlList` resources.
  * Modifying Identity and Access Management (IAM) policies on Secure Web Proxy resources.



### Data Access audit logs

[Data Access audit logging](https://docs.cloud.google.com/logging/docs/audit#data-access) isn't activated by default for Secure Web Proxy. To enable Data Access audit logs for Secure Web Proxy, see [Enable audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable).

## Audit log format

Secure Web Proxy Cloud Audit Logs follows the standard Google Cloud audit log structure. Each log entry is an object of type `LogEntry`.

A log entry contains the following key fields:

  * **`logName`** : contains the resource ID and indicates the type of audit log, either `activity` or `data_access`.

  * **`resource`** : specifies the target of the audited operation.

  * **`timeStamp`** : specifies the time at which the audited operation occurred.

  * **`protoPayload`** : contains the primary audit information and is stored within an `AuditLog` object.

The `AuditLog` object within `protoPayload` contains the following fields:

    * **`serviceName`** : specifies the name of the Google Cloud service. For Secure Web Proxy operations, this is typically `networkservices.googleapis.com`.

    * **`methodName`** : identifies the name of the API method that was called, such as `CreateGateway` or `UpdatePolicy`.

    * **`resourceName`** : indicates the full name of the resource that's being acted upon.

    * **`status`, `authenticationInfo`, and `authorizationInfo`**: provide additional standard details about the result of the operation.




For more information about other fields in these objects and how to interpret them, see [Understanding audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs).

### Log name

Secure Web Proxy audit log names include resource identifiers that indicate the Google Cloud project, folder, or organization that owns the audit logs. These audit log names also indicate whether a log contains admin activity, data access, system event, or Policy Denied audit logging data.

The following are the audit log names, including variables for the resource identifiers:
    
    
      projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity
      projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access
      projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
      projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    
      folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Factivity
      folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fdata_access
      folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
      folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    
      organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity
      organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fdata_access
      organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
      organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    

## Roles and permissions

To view Secure Web Proxy audit logs, make sure that you have the following roles and permissions:

  * **For admin activity logs** : [Logs Viewer role](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer) (`roles/logging.viewer`) or a custom role with the `logging.logEntries.list` permission.

  * **For data access logs** : [Private Logs Viewer role](https://docs.cloud.google.com/logging/docs/access-control#logging.privateLogViewer) (`roles/logging.privateLogViewer`) or a custom role with the `logging.privateLogEntries.list` permission.




## Service name

Secure Web Proxy audit logs, particularly for gateway operations and configurations, use the `networkservices.googleapis.com` service name.

To filter for this service, use the following:
    
    
    protoPayload.serviceName="networkservices.googleapis.com"
    

In addition, you can filter Secure Web Proxy audit logs by resource type for the gateway:
    
    
    resource.type="networkservices.googleapis.com/Gateway"
    

## View audit logs

You can query for all Secure Web Proxy audit logs or for specific logs by their audit log name. The audit log name includes the resource identifier of the Google Cloud project, folder, billing account, or organization for which you want to view audit logging information. Your queries can specify indexed `LogEntry` fields. If you use the **Log Analytics** page, which supports SQL queries, then you can view your query results as a chart.

For more information about querying your logs, see the following pages:

  * [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries)
  * [Query and view logs in Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view)
  * [Sample queries for security insights](https://docs.cloud.google.com/logging/docs/analyze/analyze-audit-logs)



You can view audit logs in Cloud Logging by using the Google Cloud console, the Google Cloud CLI, or the Logging API.

###  Console 

In the Google Cloud console, you can use the Logs Explorer to retrieve your audit log entries for your Google Cloud project, folder, or organization.

**Note:** You can't view audit logs for Cloud Billing accounts in the Google Cloud console. You must use either the API or the gcloud CLI.

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select your Google Cloud project, folder, or organization.

  3. To display all Secure Web Proxy audit logs, enter the following general query in the query editor field and then click **Run query** :
         
         logName:"cloudaudit.googleapis.com"
         resource.type="networkservices.googleapis.com/Gateway"
         

Alternatively, to use the query builder to display the audit logs for a specific resource and audit log type, follow these steps:

     1. For **Resource type** , select `networkservices.googleapis.com/Gateway`.

     2. For **Log name** , select the audit log type that you want to view. Only the log types that are available in your project are listed.

        * For Admin Activity audit logs, select **activity**.
        * For data access audit logs, select **data_access**.
        * For system event audit logs, select **system_event**.
        * For policy denied audit logs, select **policy**.
     3. Click **Run query**.




If you face any issues when trying to view logs in the Logs Explorer, then see the [troubleshooting](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#troubleshooting) details.

For more information about querying by using the Logs Explorer, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).

###  gcloud 

The Google Cloud CLI provides a command-line interface to the Logging API. Specify a valid resource identifier in each log name.

To read your project-level Secure Web Proxy audit log entries, use the [`gcloud logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).
    
    
    gcloud logging read 'logName:projects/PROJECT_ID/logs/cloudaudit.googleapis.com AND resource.type="networkservices.googleapis.com/Gateway"' \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with the ID of your Google Cloud project.

Add the [`--freshness` flag](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--freshness) to your command to read logs that are more than one day old.

### API

To use the Cloud Logging API to view your Secure Web Proxy audit log entries, specify the appropriate `PROJECT_ID` in the `resourceNames` field and filter the results.

For example, to use the Logging API to view your project-level audit log entries, follow these steps:

  1. On the [`entries.list` method](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) page, go to the **Try this API** section.

  2. For **Request body** , enter the following snippet:
         
         {
           "resourceNames": [
             "projects/PROJECT_ID"
           ],
           "pageSize": 5,
           "filter": "logName : projects/PROJECT_ID/logs/cloudaudit.googleapis.com AND
           resource.type=\"networkservices.googleapis.com/Gateway\""
         }
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  3. Click **Execute**.




## What's next?

  * [Logs and metrics overview](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs)
  * [View proxy transaction logs](https://docs.cloud.google.com/secure-web-proxy/docs/view-proxy-transaction-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
