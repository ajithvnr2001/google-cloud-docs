---
url: https://docs.cloud.google.com/assured-workloads/docs/audit-logging/
title: Assured Workloads audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:29.905123+00:00
---

# Assured Workloads audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/audit-logging/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Assured Workloads audit logging 

This document describes audit logging for Assured Workloads. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Assured Workloads audit logs use the service name `assuredworkloads.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="assuredworkloads.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Assured Workloads generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.AnalyzeWorkloadMove`  
`google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.GetWorkload`  
`google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.ListWorkloads`  
`google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.GetWorkload`  
`google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.ListWorkloads`  
`ADMIN_WRITE` | `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.EnableComplianceUpdates`  
`google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.EnableResourceMonitoring`  
`google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.EnableComplianceUpdates`  
`google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.EnableResourceMonitoring`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Assured Workloads.

### `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService`

The following audit logs are associated with methods belonging to `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService`.

#### `AnalyzeWorkloadMove`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.AnalyzeWorkloadMove`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `assuredworkloads.workload.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.AnalyzeWorkloadMove" `  




#### `EnableComplianceUpdates`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.EnableComplianceUpdates`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `assuredworkloads.workload.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.EnableComplianceUpdates" `  




#### `EnableResourceMonitoring`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.EnableResourceMonitoring`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `assuredworkloads.workload.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.EnableResourceMonitoring" `  




#### `GetWorkload`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.GetWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `assuredworkloads.workload.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.GetWorkload" `  




#### `ListWorkloads`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.ListWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `assuredworkloads.workload.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.ListWorkloads" `  




### `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService`

The following audit logs are associated with methods belonging to `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService`.

#### `EnableComplianceUpdates`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.EnableComplianceUpdates`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `assuredworkloads.workload.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.EnableComplianceUpdates" `  




#### `EnableResourceMonitoring`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.EnableResourceMonitoring`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `assuredworkloads.workload.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.EnableResourceMonitoring" `  




#### `GetWorkload`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.GetWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `assuredworkloads.workload.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.GetWorkload" `  




#### `ListWorkloads`

  * **Method** : `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.ListWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `assuredworkloads.workload.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.ListWorkloads" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.AcknowledgeViolation`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.ApplyWorkloadUpdate`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.CreateWorkload`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.DeleteWorkload`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.GetViolation`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.ListViolations`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.ListWorkloadUpdates`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.MutatePartnerPermissions`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.RestrictAllowedResources`
  * `google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.UpdateWorkload`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.AcknowledgeViolation`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.ApplyWorkloadUpdate`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.CreateWorkload`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.DeleteWorkload`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.GetViolation`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.ListViolations`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.MutatePartnerPermissions`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.RestrictAllowedResources`
  * `google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.UpdateWorkload`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
