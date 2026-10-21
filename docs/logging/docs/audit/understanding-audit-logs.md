---
url: https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs/
title: Understanding audit logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:39.708301+00:00
---

# Understanding audit logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Understanding audit logs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Cloud Audit Logs log entries in detail: their structure, how to read them, and how to interpret them.

Cloud Audit Logs provides the following audit logs for each Google Cloud project, folder, and organization:

  * Admin Activity audit logs
  * Data Access audit logs
  * System Event audit logs
  * Policy Denied audit logs



For a general overview of Cloud Audit Logs, see [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

## Format of audit log entries

An audit log entry is a type of Cloud Logging log entry. Like all Logging log entries, an audit log entry is stored in a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object. What distinguishes an audit log entry from other log entries is the `protoPayload` field. In audit log entries, the log entry's `protoPayload` field contains an [`AuditLog`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog) object that stores the audit logging data.

In short, every audit log entry is characterized by the following information:

  * The project, folder, or organization that owns the log entry.
  * The resource to which the log entry applies. This information consists of a resource type from the [Monitored resource list](https://docs.cloud.google.com/logging/docs/api/v2/resource-list) and additional values that denote a specific instance. For example, you can view audit log entries from a single Compute Engine VM instance or from all VM instances.
  * A timestamp.
  * A service: Services are individual Google Cloud products, such as Compute Engine, Cloud SQL, or Pub/Sub. Each service is identified by name: Compute Engine is `compute.googleapis.com`, Cloud SQL is `cloudsql.googleapis.com`, and so forth. This information is listed in the `protoPayload.serviceName` field of the audit log entry.

Resource types belongs to a single service, but a service can have several resource types. For a list of services and resources, go to [Mapping services to resources](https://docs.cloud.google.com/logging/docs/audit/services).

  * A payload, which is the `protoPayload` type. The payload of each audit log entry is an object of type [`AuditLog`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog), which defines a set of fields specific to Cloud Audit Logs, such as `serviceName` and `authenticationInfo`. It also has an optional field, `metadata`, that Google Cloud services use to list service-specific information in the audit log entry. Some Google Cloud services still use the older `serviceData` field to list service-specific information. For a list of services that use the `serviceData` field, see Service-specific audit data.

  * A log name: Audit log entries belong to logs within billing accounts, projects, folders, and organizations. The following table lists log names:



    
    
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

Within a billing account, project, folder, or organization, these log names are typically abbreviated as **activity** , **data_access** , **system_event** , and **policy**.

### Sample audit log entry

This section uses a sample audit log entry to explain how to find the most important information in audit log entries.

The following sample is an Admin Activity audit log entry written by [App Engine](https://docs.cloud.google.com/appengine/docs) to record a change to an Identity and Access Management (IAM) policy with PROJECT_ID `my-gcp-project-id`. For brevity, some parts of the log entry are omitted, and some fields are highlighted:
    
    
        {
          **pro toPayload**: {
            **@ type: "type.googleapis.com/google.cloud.audit.AuditLog"**,
            status: {},
            authenticationInfo: {
              principalEmail: "user@example.com"
            },
            **serviceName : "appengine.googleapis.com"**,
            **me thodName: "SetIamPolicy"**,
            authorizationInfo: [...],
            **serviceDa ta**: {
              **@ type: "type.googleapis.com/google.appengine.legacy.AuditData"**,
              policyDelta: { bindingDeltas: [
                  action: "ADD",
                  role: "roles/logging.privateLogViewer",
                  member: "user:user@example.com"
              ], }
            },
            request: {
              resource: "my-gcp-project-id",
              policy: { bindings: [...], }
            },
            response: {
              bindings: [
                {
                  role: "roles/logging.privateLogViewer",
                  members: [ "user:user@example.com" ]
                }
              ],
            }
          },
          insertId: "53179D9A9B559.AD6ACC7.B40604EF",
          **resource : {
            type: "gae_app",
            labels: { project_id: "my-gcp-project-id" }
          }**,
          timestamp: "2019-05-27T16:24:56.135Z",
          severity: "NOTICE",
          **logName : "projects/my-gcp-project-id/logs/cloudaudit.googleapis.com%2Factivity"**,
        }

Here is the query that was used to select the previous audit log entry sample. The query can be used in the Logs Explorer, Logging API, or Google Cloud CLI. The project identifier is in the log's name:
    
    
        resource.type = "gae_app"
        logName = "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"

If you are looking for audit logs from a single instance of a resource type, such as `gce_instance`, add an instance qualifier:
    
    
        resource.type = "gce_instance"
        resource.instance_id = "INSTANCE_ID"
        logName = "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"

### Interpreting the sample audit log entry

In the previous audit log entry sample, the `protoPayload`, `insertId`, `resource`, `timestamp`, `severity` and `logName` fields shown are part of the [ `LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object. The value of the `protoPayload` field is an [`AuditLog`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog) object. It encapsulates the audit logging data.

Looking at the audit log entry sample, you might have some questions:

  * **Is this an audit log entry?** It is, which you can tell in two ways:

    * The `protoPayload.@type` field is `type.googleapis.com/google.cloud.audit.AuditLog`.

    * The `logName` field includes the domain `cloudaudit.googleapis.com`.

  * **What service wrote the audit log?** The log was written by App Engine. This information is listed in the `protoPayload.serviceName` field of the audit log entry.

  * **What operation is being audited?** `SetIamPolicy`, as specified in the `protoPayload.methodName` field, is being audited. More information about the audited operation is in the `AuditData` object in `protoPayload.serviceData`.

  * **What resource is being audited?** An application running in App Engine, associated with a Google Cloud project `my-gcp-project-id`, is being audited. You can determine this from the `resource` field, which specifies the resource type `gae_app` and the project identifier `my-gcp-project-id`. In this example, you would find details on the resource type in the [monitored resource type list](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).




For more information, see the [`LogEntry` type](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry), the [`AuditLog` type](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog), and the [IAM `AuditData` type](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditData).

## Audit logs for long-running operations

APIs that are [long-running operations](https://google.aip.dev/151) emit two audit logs; one when the API is called and the operation starts, and one when the operation completes.

In this case, the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object contains an `operation` field. Log entries for the same operation have the same value for both `LogEntry.operation.id` and `LogEntry.operation.producer`. The first log entry that was written has `LogEntry.operation.first=true`, and the completion log entry has `LogEntry.operation.last=true`.

In cases where the operation completes immediately or fails, there is only one log entry containing both `LogEntry.operation.first=true` and `LogEntry.operation.last=true`.

Some services don't populate the `LogEntry.operation` field when the operation fails. However, you can determine which operations are long-running operations by referring to the [service's audit logging documentation](https://docs.cloud.google.com/logging/docs/audit/services).

These APIs implement the [Operations](https://github.com/googleapis/googleapis/blob/master/google/longrunning/operations.proto) service. This service generally emit audit log entries when called. Depending on which APIs are called, `protoPayload.methodName` is one of the following:

  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.WaitOperation`
  * `google.longrunning.Operations.DeleteOperation`



`LogEntry.operation` isn't specified in this case, as this API returns metadata about long-running operations, but is not a long-running operation itself.

See [Google Cloud services with audit logs](https://docs.cloud.google.com/logging/docs/audit/services) for details about which APIs are audited, as it can vary per service.

## Audit logs for streaming APIs

Similar to long-running operations, streaming APIs emit two audit log entries; one when the API is first called and one when the streaming connection has ended.

In this case, the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object contains an `operation` field and log entries for the same operation have the same value for both `LogEntry.operation.id` and `LogEntry.operation.producer`. The first log written has `LogEntry.operation.first=true`, and the completion log will have `LogEntry.operation.last=true`.

This API may also emit continuation log entries with neither `LogEntry.operation.first` nor `LogEntry.operation.last` set to indicate that the stream remains open.

## Service-specific audit data

Some services extend the information stored in their [`AuditLog`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog) by placing a supplementary data structure in the audit log entry's `serviceData` field. The following table lists the services that use `serviceData` field and provides a link to their `AuditData` type.

Service| Service data type | [App Engine](https://docs.cloud.google.com/appengine/docs) | [`type.googleapis.com/google.appengine.v1.AuditData`](https://docs.cloud.google.com/logging/docs/audit/api/ref_gae4/rest/Shared.Types/AuditData)  
---|---  
[App Engine (Legacy)](https://docs.cloud.google.com/appengine/docs) | [`type.googleapis.com/google.appengine.legacy.AuditData`](https://docs.cloud.google.com/logging/docs/audit/api/ref_gaeL/rest/Shared.Types/AuditData)  
[BigQuery](https://docs.cloud.google.com/bigquery/docs) | [`type.googleapis.com/google.cloud.bigquery.logging.v1.AuditData`](https://docs.cloud.google.com/logging/docs/audit/api/ref_bq/rest/Shared.Types/AuditData)  
[IAM](https://docs.cloud.google.com/iam/docs) | [`type.googleapis.com/google.iam.v1.logging.AuditData`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog)  
[Cloud Storage](https://docs.cloud.google.com/storage/docs) | [`type.googleapis.com/google.iam.v1.logging.AuditData`](https://docs.cloud.google.com/logging/docs/audit/api/ref_gae4/rest/Shared.Types/AuditData)  
  
## Viewing audit logs

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




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
