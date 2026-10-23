---
url: https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging/
title: VPC Service Controls audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:50.374625+00:00
---

# VPC Service Controls audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  VPC Service Controls audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the audit logs created by VPC Service Controls as part of [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

## Overview

Google Cloud services write audit logs to help you answer the questions, "Who did what, where, and when?" within your Google Cloud resources.

Your Google Cloud projects contain only the audit logs for resources that are directly within the Google Cloud project. Other Google Cloud resources, such as folders, organizations, and billing accounts, contain the audit logs for the entity itself.

For a general overview of Cloud Audit Logs, see [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit). For a deeper understanding of the audit log format, see [Understand audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs).

## Available audit logs

The following types of audit logs are available for VPC Service Controls:

  * Policy Denied audit logs 

Identifies when a user or [service account](https://docs.cloud.google.com/iam/docs/service-accounts) is denied access because of a security policy violation. The service name and method name in Policy Denied audit logs indicate the names of the resource that the user or service account was denied access to. 

You can't disable Policy Denied audit logs. However, you can add the following to the [ exclusion filter](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) on your `_Default` sink to exclude Policy Denied audit logs: `LOG_ID("cloudaudit.googleapis.com/policy")`. You can also [ disable the `_Default` sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#stopping_logs_ingestion) for Cloud Logging, which prevents logs from being routed to the `_Default` bucket. 




For fuller descriptions of the audit log types, see [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types).

## Audited operations

The following table summarizes which API operations correspond to each audit log type in VPC Service Controls:

Audit logs category | VPC Service Controls methods  
---|---  
Policy Denied audit logs | The methods of the services that integrate with VPC Service Controls are supported.  
  
## Audit log record content

Each audit log record contains information that can be divided into two major categories: the information about the original call, and information about security policy violations. It is filled by VPC Service Controls API as follows:

Audit log field  | Description   
---|---  
**`serviceName`** | The service to which access is restricted by a service perimeter. The request to this service has violated a VPC Service Controls check and resulted in the creation of this audit log.   
**`methodName`** | The name of the method call that resulted in the security policy violation described in the record. Often, `methodName` is the method associated with the Google Cloud service specified in the `serviceName` field.   
**`authenticationInfo.principalEmail`** | The email address of the user or service account that issued the request.  
Some email addresses might be redacted. For more information, see [Caller identities in audit logs](https://docs.cloud.google.com/logging/docs/audit#user-id).   
**`resourceName`** | The Google Cloud resource specified in the original request from the client. The `resourceName` can be a project, folder, organization, or a resource like a Google Cloud bucket.   
**`requestMetadata.callerIp`** |  The IP address of the caller. If the call originated from the internet, then `requestMetadata.callerIp` is a public IPv4 or IPv6 address.  If the call originated from a Compute Engine VM, then `requestMetadata.callerIp` is a VM IP address. The VM IP address can be an internal IP address or an external IP address.  If the call originated from within Google's internal production network, then the value in this field is `private`. This case occurs when the call is sent from one Google Cloud service to another.   
**`request_metadata.caller_network`** | The name of the network of the caller. This value is set only if the network host project belongs to the same Google Cloud organization or project that the accessed resource belongs to. For more information, see [VPC networks](https://docs.cloud.google.com/compute/docs/vpc).   
**`status`** | The overall status of handling an operation described in the record.   
**`metadata`** |  The information about the security policy violation.   
**`metadata.resourceNames`** |  The names of resources involved in the security policy violation described in the record.   
**`metadata.dryRun`** |  A boolean value that is `True` if the audit log is for a dry run policy check. For more information, see [Dry run mode for service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).   
**`metadata.vpcServiceControlsTroubleshootToken`** |  A troubleshooting token that lets you diagnose the violation using the [violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).   
**`metadata.vpcServiceControlsUniqueId`** | The unique identifier of the VPC Service Controls violation described in the record.   
**`metadata.violationReason`** | The reason for the violation. For example, `RESOURCE_NOT_IN_SAME_SERVICE_PERIMETER` means that the resources being accessed don't belong to the same service perimeter.   
**`metadata.securityPolicyInfo`** | The name of the service perimeter for which the violation occurred and the unique identifier of the organization to which the perimeter belongs.   
**`metadata.egressViolations`** |  An egress violation usually occurs when a request fails because the source is protected by a service perimeter and the target resource is outside the perimeter. The source can be a project or a VPC network.   
**`metadata.ingressViolations`** |  The violation type. Often, this violation occurs if the request is trying to access a target resource that is protected by a service perimeter. The source can be either a project or a VPC network. This field contains a structure that explains the ingress violation.   
**`metadata.servicePerimeter`** |  The name of the service perimeter that's involved in the violation.   
**`metadata.source`** |  This field contains the source of the request, which can either be a project or a VPC network.   
**`metadata.targetResource`** |  The resource that the request targeted, which caused the violation. This field can be a project.   
**`metadata.targetResourcePermissions`** |  The list of IAM permissions that are required to access the target resource. To resolve the violation, configure ingress or egress rules to allow the [IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions) containing these permissions. If the required IAM permission is unknown or from an unsupported service or method, VPC Service Controls logs `vpcsc.permissions.unavailable` in this field. You can ignore the `vpcsc.permissions.unavailable` violation unless you [use IAM roles in the ingress or egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles). If you encounter this violation for a request that an ingress or egress rule should allow based on IAM roles, contact [Cloud Customer Care](https://cloud.google.com/support-hub).  
**`metadata.accessLevels`** |  All matching access levels under the organization that belongs to the same access policy. These access levels might not be specified in the violated perimeter and can cause a `NO_MATCHING_ACCESS_LEVEL` violation.   
**`metadata.intermediateServices`** |  The list of the services involved in the request chain. This field is empty for user-initiated requests.   
**`metadata.deviceState`** |  The state of the device that creates the request when the device policy is enabled. The default value for this field is `Unknown`.   
  
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

VPC Service Controls audit logs use the service names of the [services that integrate with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). 

For a list of all the Cloud Logging API service names and their corresponding monitored resource type, see [Map services to resources](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#service-names).

### Resource types

VPC Service Controls audit logs use the resource types supported by the services that integrate with VPC Service Controls. 

For a list of all the Cloud Logging monitored resource types and descriptive information, see [Monitored resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

### Caller identities

The IP address of the caller is held in the `RequestMetadata.caller_ip` field of the [`AuditLog`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) object. Logging might redact certain caller identities and IP addresses.

For information about what information is redacted in audit logs, see [Caller identities in audit logs](https://docs.cloud.google.com/logging/docs/audit#user-id).

## Enable audit logging

Admin Activity audit logs are always enabled; you can't disable them.

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




To find audit logs for VPC Service Controls, use the following queries in the Logs Explorer:

Query description | Expression  
---|---  
Violation details based on a denial ID | 
    
    
    log_id("cloudaudit.googleapis.com/policy") severity=ERROR
    resource.type="audited_resource"
    protoPayload.metadata."@type"="type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
    protoPayload.metadata.vpcServiceControlsUniqueId="UNIQUE_ID" 

Replace `UNIQUE_ID` with the unique ID of the denial.  
Violations for an IP address | 
    
    
    log_id("cloudaudit.googleapis.com/policy")
    severity=ERROR
    resource.type="audited_resource"
    protoPayload.metadata."@type"="type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
    protoPayload.requestMetadata.callerIp="IP_ADDRESS"

Replace `IP_ADDRESS` with the IP address of the caller.  
Violations for a service | 
    
    
    log_id("cloudaudit.googleapis.com/policy")
    severity=ERROR
    resource.type="audited_resource"
    protoPayload.metadata."@type"="type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
    protoPayload.serviceName="SERVICE_NAME"

Replace `SERVICE_NAME` with the name of the restricted service.  
Access level change made to a perimeter | 
    
    
    logName="organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity"
    severity=NOTICE
    protoPayload.serviceName="accesscontextmanager.googleapis.com"
    protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.UpdateServicePerimeter"
    -protoPayload.metadata.previousState:"ACCESS_LEVEL"
    protoPayload.request.servicePerimeter.status.accessLevels:"ACCESS_LEVEL"

Replace `ORGANIZATION_ID` with the numeric ID of your organization and `ACCESS_LEVEL` with the unique name of the access level.  
Perimeter CRUD operations | 
    
    
    logName="organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity"
    severity=NOTICE
    protoPayload.serviceName="accesscontextmanager.googleapis.com"
    protoPayload.methodName=~"google.identity.accesscontextmanager.v1.AccessContextManager.*ServicePerimeter"
    protoPayload.request.servicePerimeter.name=~".*PERIMETER_NAME$"

Replace `PERIMETER_NAME` with the name of the perimeter.  
Access level CRUD operations | 
    
    
    logName="organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity"
    severity=NOTICE
    protoPayload.serviceName="accesscontextmanager.googleapis.com"
    protoPayload.methodName=~"google.identity.accesscontextmanager.v1.AccessContextManager.*AccessLevel"
    protoPayload.request.accessLevel.name=~".*ACCESS_LEVEL$"  
  
Create and update operations for ingress rules | 
    
    
    logName="organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity"
    protoPayload.serviceName="accesscontextmanager.googleapis.com"
    protoPayload.methodName=~"google.identity.accesscontextmanager.v1.AccessContextManager.*ServicePerimeter"
    protoPayload.request.servicePerimeter.status.ingressPolicies:"*"  
  
Create and update operations for egress rules | 
    
    
    logName="organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity"
    protoPayload.serviceName="accesscontextmanager.googleapis.com"
    protoPayload.methodName=~"google.identity.accesscontextmanager.v1.AccessContextManager.*ServicePerimeter"
    protoPayload.request.servicePerimeter.status.egressPolicies:"*"  
  
## Route audit logs

You can [route audit logs](https://docs.cloud.google.com/logging/docs/routing/overview) to supported destinations in the same way that you can route other kinds of logs. Here are some reasons you might want to route your audit logs:

  * To keep audit logs for a longer period of time or to use more powerful search capabilities, you can route copies of your audit logs to Cloud Storage, BigQuery, or Pub/Sub. Using Pub/Sub, you can route to other applications, other repositories, and to third parties.

  * To manage your audit logs across an entire organization, you can create [aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) that can route logs from any or all Google Cloud projects in the organization.




For instructions about routing logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## Pricing

For more information about pricing, see the Cloud Logging sections in the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## Limitations

  * For violations involving requests to unsupported services (such as when using the private VIP with [service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services#service-patterns)), the generated audit log records still contain the `SERVICE_NOT_ALLOWED_FROM_VPC` violation reason but might not contain complete details. For example, they might omit the specific resource names or method names involved in the violation.

The following fields in `protoPayload.metadata` might be missing or incomplete:

    * `methodName`
    * `authenticationInfo.principalEmail`
    * `metadata.resourceNames`
    * `metadata.accessLevels`
    * `metadata.deviceState`

The `protoPayload.request.url` field often contains the full URL path, which can help in diagnosing the violation. Use the `metadata.vpcServiceControlsUniqueId` to search for logs.




## What's next

  * Watch a video to [learn about auditing and allowlisting best practices](https://youtu.be/blVP-sTCgmk). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
