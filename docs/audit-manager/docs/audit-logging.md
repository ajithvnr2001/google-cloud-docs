---
url: https://docs.cloud.google.com/audit-manager/docs/audit-logging/
title: Audit Manager audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:41.209856+00:00
---

# Audit Manager audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Audit Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Audit Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Audit Manager audit logs use the service name `auditmanager.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="auditmanager.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Audit Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_WRITE` | `google.cloud.auditmanager.v1.AuditManager.EnrollResource`  
`google.cloud.auditmanager.v1alpha.AuditManager.EnrollResource`  
`DATA_READ` | `google.cloud.auditmanager.v1.AuditManager.GetAuditReport`  
`google.cloud.auditmanager.v1.AuditManager.GetResourceEnrollmentStatus`  
`google.cloud.auditmanager.v1.AuditManager.ListAuditReports`  
`google.cloud.auditmanager.v1.AuditManager.ListControls`  
`google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses`  
`google.cloud.auditmanager.v1alpha.AuditManager.GetAuditReport`  
`google.cloud.auditmanager.v1alpha.AuditManager.GetResourceEnrollmentStatus`  
`google.cloud.auditmanager.v1alpha.AuditManager.ListAuditReports`  
`google.cloud.auditmanager.v1alpha.AuditManager.ListControls`  
`google.cloud.auditmanager.v1alpha.AuditManager.ListResourceEnrollmentStatuses`  
`DATA_WRITE` | `google.cloud.auditmanager.v1.AuditManager.GenerateAuditReport` (LRO)  
`google.cloud.auditmanager.v1.AuditManager.GenerateAuditScopeReport`  
`google.cloud.auditmanager.v1alpha.AuditManager.GenerateAuditReport` (LRO)  
`google.cloud.auditmanager.v1alpha.AuditManager.GenerateAuditScopeReport`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Audit Manager.

### `google.cloud.auditmanager.v1.AuditManager`

The following audit logs are associated with methods belonging to `google.cloud.auditmanager.v1.AuditManager`.

#### `EnrollResource`

  * **Method** : `google.cloud.auditmanager.v1.AuditManager.EnrollResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `auditmanager.locations.enrollResource - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1.AuditManager.EnrollResource" `  




#### `GenerateAuditReport`

  * **Method** : `google.cloud.auditmanager.v1.AuditManager.GenerateAuditReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.auditReports.generate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1.AuditManager.GenerateAuditReport" `  




#### `GenerateAuditScopeReport`

  * **Method** : `google.cloud.auditmanager.v1.AuditManager.GenerateAuditScopeReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.auditScopeReports.generate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1.AuditManager.GenerateAuditScopeReport" `  




#### `GetAuditReport`

  * **Method** : `google.cloud.auditmanager.v1.AuditManager.GetAuditReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.auditReports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1.AuditManager.GetAuditReport" `  




#### `GetResourceEnrollmentStatus`

  * **Method** : `google.cloud.auditmanager.v1.AuditManager.GetResourceEnrollmentStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.resourceEnrollmentStatuses.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1.AuditManager.GetResourceEnrollmentStatus" `  




#### `ListAuditReports`

  * **Method** : `google.cloud.auditmanager.v1.AuditManager.ListAuditReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.auditReports.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1.AuditManager.ListAuditReports" `  




#### `ListControls`

  * **Method** : `google.cloud.auditmanager.v1.AuditManager.ListControls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.controls.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1.AuditManager.ListControls" `  




#### `ListResourceEnrollmentStatuses`

  * **Method** : `google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.resourceEnrollmentStatuses.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses" `  




### `google.cloud.auditmanager.v1alpha.AuditManager`

The following audit logs are associated with methods belonging to `google.cloud.auditmanager.v1alpha.AuditManager`.

#### `EnrollResource`

  * **Method** : `google.cloud.auditmanager.v1alpha.AuditManager.EnrollResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `auditmanager.locations.enrollResource - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1alpha.AuditManager.EnrollResource" `  




#### `GenerateAuditReport`

  * **Method** : `google.cloud.auditmanager.v1alpha.AuditManager.GenerateAuditReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.auditReports.generate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1alpha.AuditManager.GenerateAuditReport" `  




#### `GenerateAuditScopeReport`

  * **Method** : `google.cloud.auditmanager.v1alpha.AuditManager.GenerateAuditScopeReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.auditScopeReports.generate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1alpha.AuditManager.GenerateAuditScopeReport" `  




#### `GetAuditReport`

  * **Method** : `google.cloud.auditmanager.v1alpha.AuditManager.GetAuditReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.auditReports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1alpha.AuditManager.GetAuditReport" `  




#### `GetResourceEnrollmentStatus`

  * **Method** : `google.cloud.auditmanager.v1alpha.AuditManager.GetResourceEnrollmentStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.resourceEnrollmentStatuses.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1alpha.AuditManager.GetResourceEnrollmentStatus" `  




#### `ListAuditReports`

  * **Method** : `google.cloud.auditmanager.v1alpha.AuditManager.ListAuditReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.auditReports.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1alpha.AuditManager.ListAuditReports" `  




#### `ListControls`

  * **Method** : `google.cloud.auditmanager.v1alpha.AuditManager.ListControls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.controls.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1alpha.AuditManager.ListControls" `  




#### `ListResourceEnrollmentStatuses`

  * **Method** : `google.cloud.auditmanager.v1alpha.AuditManager.ListResourceEnrollmentStatuses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `auditmanager.resourceEnrollmentStatuses.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.auditmanager.v1alpha.AuditManager.ListResourceEnrollmentStatuses" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.auditmanager.v1.AuditManager.GetOperation`
  * `google.cloud.auditmanager.v1alpha.AuditManager.GetOperation`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
