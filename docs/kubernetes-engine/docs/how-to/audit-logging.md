---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging/
title: GKE audit logging information \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:13.671049+00:00
---

# GKE audit logging information  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  GKE audit logging information Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes the audit logs created by Google Kubernetes Engine as part of [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

## Overview

Google Cloud services write audit logs to help you answer the questions, "Who did what, where, and when?" within your Google Cloud resources.

Your Google Cloud projects contain only the audit logs for resources that are directly within the Google Cloud project. Other Google Cloud resources, such as folders, organizations, and billing accounts, contain the audit logs for the entity itself.

For a general overview of Cloud Audit Logs, see [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit). For a deeper understanding of the audit log format, see [Understand audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs).

## Available audit logs

The following types of audit logs are available for GKE:

  * Admin Activity audit logs 

Includes "admin write" operations that write metadata or configuration information. 

You can't disable Admin Activity audit logs. 

  * Data Access audit logs 

Includes "admin read" operations that read metadata or configuration information. Also includes "data read" and "data write" operations that read or write user-provided data. 

To receive Data Access audit logs, you must [ explicitly enable](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) them. 




For fuller descriptions of the audit log types, see [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types).

## Audited operations

The following table summarizes which API operations correspond to each audit log type in GKE:

Audit logs category | GKE operations  
---|---  
Admin Activity audit logs | `io.k8s.authorization.rbac.v1`   
  
| `io.k8s.authorization.rbac.v1.roles`  
**Note:** This table provides the most commonly audited operations; it isn't a complete list.

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

Kubernetes audit logs use the service name `k8s.io`.

The `k8s.io` service is used for Kubernetes audit logs. These logs are generated by the Kubernetes API Server component and they contain information about actions performed using the Kubernetes API. For example, any changes you make on a Kubernetes resource by using the `kubectl` command are recorded by the `k8s.io` service. Kubernetes audit log entries are useful for investigating suspicious API requests, for collecting statistics, or for creating monitoring alerts for unwanted API calls.

For a list of all the Cloud Logging API service names and their corresponding monitored resource type, see [Map services to resources](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#service-names).

### Resource types

Kubernetes audit logs use the **`k8s_cluster`** resource type. Log entries written by the Kubernetes API server apply to the `k8s_cluster` resource type. These log entries describe operations on Kubernetes resources in your cluster, for example, Pods, Deployments, and Secrets. 

For a list of all the Cloud Logging monitored resource types and descriptive information, see [Monitored resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

### Caller identities

The IP address of the caller is held in the `RequestMetadata.caller_ip` field of the [`AuditLog`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) object. Logging might redact certain caller identities and IP addresses.

For information about what information is redacted in audit logs, see [Caller identities in audit logs](https://docs.cloud.google.com/logging/docs/audit#user-id).

## Enable audit logging

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




## Sample queries

To use the sample queries in the following table, complete these steps:

  1. Replace the variables in the query expression with your own project information, then copy the expression using the clipboard icon _content_copy_.

  2. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  3. Enable **Show query** to open the query-editor field, then paste the expression into the query-editor field:

![The query editor where you enter sample queries.](https://docs.cloud.google.com/static/logging/docs/images/query-pane-2.png)

  4. Click **Run query**. Logs that match your query are listed in the **Query results** pane.




To find audit logs for GKE, use the following queries in the Logs Explorer:

Query/filter name | Expression  
---|---  
Workload audit logs | 
    
    
    log_id("cloudaudit.googleapis.com/activity")
    resource.type="k8s_cluster"
    resource.labels.cluster_name="CLUSTER_NAME"
    protoPayload.request.metadata.name="WORKLOAD_NAME"
      
  
Node metadata update for node object | 
    
    
    resource.type="k8s_cluster"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName="io.k8s.core.v1.nodes.update"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.location="LOCATION_NAME"
      
  
Changes to Role-Based Access Control, excluding automated system changes  | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.methodName:"io.k8s.authorization.rbac.v1"
    NOT protoPayload.authenticationInfo.principalEmail:"system"
      
  
Changes to Role-Based Access Control roles, excluding automated system changes  | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.methodName:"io.k8s.authorization.rbac.v1.roles"
    NOT protoPayload.authenticationInfo.principalEmail:"system"
      
  
Changes to Role-Based Access Control role bindings, excluding automated system changes  | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.methodName:"io.k8s.authorization.rbac.v1.rolebindings"
    NOT protoPayload.authenticationInfo.principalEmail:"system"
      
  
Certificate signing requests | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.resourceName:"certificates.k8s.io/v1beta1/certificatesigningrequests"
      
  
Unauthenticated web requests | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail:"system:anonymous"
      
  
kubelet bootstrap identity calls | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail:"kubelet"
      
  
Node authenticated requests | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail:"system:node"
      
  
Calls outside an IP address range | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.requestMetadata.callerIp!="127.0.0.1"
    protoPayload.requestMetadata.callerIp!="::1"
    NOT protoPayload.requestMetadata.callerIp:"IP_ADDRESS_PREFIX"
      
  
Admin Activity audit log entries that apply to the `k8s_cluster` resource type and describe creating a Deployment  | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.methodName:"deployments.create"
      
  
Admin Activity audit log entries that apply to the `k8s_cluster` resource type and have a `principalEmail` value of `system:anonymous`. These entries probably represent failed attempts to authenticate. | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail="system:anonymous"
      
  
Admin Activity audit log entries that apply to the `gke_cluster` resource type and have a `severity` value of `ERROR`.  | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="gke_cluster"
    severity="ERROR"
      
  
Admin Activity audit log entries that apply to the `k8s_cluster` resource type and describe a write request to a Secret. | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.methodName:"io.k8s.core.v1.secrets"
    NOT protoPayload.methodName:"get"
    NOT protoPayload.methodName:"list"
    NOT protoPayload.methodName:"watch"
      
  
Admin Activity audit log entries that apply to the `k8s_cluster` resource type and describe a Pod request from a particular user.  | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.methodName:"io.k8s.core.v1.pods"
    protoPayload.authenticationInfo.principalEmail="dev@example.com"
      
  
Admin Activity audit logs from a `kubectl exec` command execution event in a cluster. These logs include a label `command.gke.io/command` showing the `kubectl exec` command arguments.  | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    protoPayload.methodName =~ "io.k8s.core.v1.pods.exec.*"
      
  
Admin Activity audit log entries that apply to the `k8s_cluster` resource type and describe dry-run Kubernetes API requests (for example, requests submitted by using `kubectl --dry-run` command or with the `dryRun` URL parameter). GKE populates these audit entries with the `command.gke.io/dryRun` label. The Kubernetes API supports only one no-empty value for the `dryRun` parameter: `All`. This value is set when you run a `kubectl` command with the `--dry-run=server` flag. `kubectl` commands with the `--dry-run=client` flag are not logged because they don't make requests to the Kubernetes API server. | 
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
    resource.type="k8s_cluster"
    labels."command.gke.io/dryRun": *
      
  
## Route audit logs

You can [route audit logs](https://docs.cloud.google.com/logging/docs/routing/overview) to supported destinations in the same way that you can route other kinds of logs. Here are some reasons you might want to route your audit logs:

  * To keep audit logs for a longer period of time or to use more powerful search capabilities, you can route copies of your audit logs to Cloud Storage, BigQuery, or Pub/Sub. Using Pub/Sub, you can route to other applications, other repositories, and to third parties.

  * To manage your audit logs across an entire organization, you can create [aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) that can route logs from any or all Google Cloud projects in the organization.



  * If your enabled Data Access audit logs are pushing your Google Cloud projects over your log allotments, you can create sinks that exclude the Data Access audit logs from Logging.



For instructions about routing logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## Pricing

For more information about pricing, see the Cloud Logging sections in the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## Setting up metrics and alerts

To set up [metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) based on your log entries, you can use Cloud Monitoring. To set up [charts and alerts](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts), you can use log-based metrics.

## Audit policy

The Kubernetes audit policy determines which log entries are exported by the Kubernetes API server. The Kubernetes Engine audit policy determines which entries go to your Admin Activity audit log and which entries go to your Data Access audit log.

For more information about audit policies in Kubernetes Engine, see [Kubernetes Engine Audit Policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
