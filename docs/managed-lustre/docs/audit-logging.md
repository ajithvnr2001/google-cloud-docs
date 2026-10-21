---
url: https://docs.cloud.google.com/managed-lustre/docs/audit-logging/
title: Audit logging \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:58.897963+00:00
---

# Audit logging  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Google Cloud Managed Lustre. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Google Cloud Managed Lustre audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="lustre.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Cloud Managed Lustre generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.lustre.v1.Lustre.GetInstance`  
`google.cloud.lustre.v1.Lustre.ListInstances`  
`google.cloud.lustre.v1alpha.Lustre.GetInstance`  
`google.cloud.lustre.v1alpha.Lustre.ListInstances`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.lustre.v1.Lustre.CreateInstance` (LRO)  
`google.cloud.lustre.v1.Lustre.DeleteInstance` (LRO)  
`google.cloud.lustre.v1.Lustre.RescheduleMaintenance`  
`google.cloud.lustre.v1.Lustre.UpdateInstance` (LRO)  
`google.cloud.lustre.v1alpha.Lustre.CreateInstance` (LRO)  
`google.cloud.lustre.v1alpha.Lustre.DeleteInstance` (LRO)  
`google.cloud.lustre.v1alpha.Lustre.RescheduleMaintenance`  
`google.cloud.lustre.v1alpha.Lustre.UpdateInstance` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.lustre.v1.Lustre.ExportData` (LRO)  
`google.cloud.lustre.v1alpha.Lustre.ExportData` (LRO)  
`DATA_WRITE` | `google.cloud.lustre.v1.Lustre.ImportData` (LRO)  
`google.cloud.lustre.v1alpha.Lustre.ImportData` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Cloud Managed Lustre.

### `google.cloud.lustre.v1.Lustre`

The following audit logs are associated with methods belonging to `google.cloud.lustre.v1.Lustre`.

#### `CreateInstance`

  * **Method** : `google.cloud.lustre.v1.Lustre.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1.Lustre.CreateInstance" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.lustre.v1.Lustre.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1.Lustre.DeleteInstance" `  




#### `ExportData`

  * **Method** : `google.cloud.lustre.v1.Lustre.ExportData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.instances.exportData - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1.Lustre.ExportData" `  




#### `GetInstance`

  * **Method** : `google.cloud.lustre.v1.Lustre.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1.Lustre.GetInstance" `  




#### `ImportData`

  * **Method** : `google.cloud.lustre.v1.Lustre.ImportData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.instances.importData - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1.Lustre.ImportData" `  




#### `ListInstances`

  * **Method** : `google.cloud.lustre.v1.Lustre.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1.Lustre.ListInstances" `  




#### `RescheduleMaintenance`

  * **Method** : `google.cloud.lustre.v1.Lustre.RescheduleMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.instances.rescheduleMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1.Lustre.RescheduleMaintenance" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.lustre.v1.Lustre.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1.Lustre.UpdateInstance" `  




### `google.cloud.lustre.v1alpha.Lustre`

The following audit logs are associated with methods belonging to `google.cloud.lustre.v1alpha.Lustre`.

#### `CreateInstance`

  * **Method** : `google.cloud.lustre.v1alpha.Lustre.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1alpha.Lustre.CreateInstance" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.lustre.v1alpha.Lustre.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1alpha.Lustre.DeleteInstance" `  




#### `ExportData`

  * **Method** : `google.cloud.lustre.v1alpha.Lustre.ExportData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.instances.exportData - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1alpha.Lustre.ExportData" `  




#### `GetInstance`

  * **Method** : `google.cloud.lustre.v1alpha.Lustre.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1alpha.Lustre.GetInstance" `  




#### `ImportData`

  * **Method** : `google.cloud.lustre.v1alpha.Lustre.ImportData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.instances.importData - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1alpha.Lustre.ImportData" `  




#### `ListInstances`

  * **Method** : `google.cloud.lustre.v1alpha.Lustre.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1alpha.Lustre.ListInstances" `  




#### `RescheduleMaintenance`

  * **Method** : `google.cloud.lustre.v1alpha.Lustre.RescheduleMaintenance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.instances.rescheduleMaintenance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1alpha.Lustre.RescheduleMaintenance" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.lustre.v1alpha.Lustre.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.lustre.v1alpha.Lustre.UpdateInstance" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lustre.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `lustre.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.lustre.v1.Lustre.CreateMirror`
  * `google.cloud.lustre.v1.Lustre.DeleteMirror`
  * `google.cloud.lustre.v1.Lustre.GetDirectoryPolicy`
  * `google.cloud.lustre.v1.Lustre.GetMirror`
  * `google.cloud.lustre.v1.Lustre.ListDirectoryPolicies`
  * `google.cloud.lustre.v1.Lustre.ListMirrors`
  * `google.cloud.lustre.v1.Lustre.UpdateMirror`
  * `google.cloud.lustre.v1alpha.Lustre.CreateMirror`
  * `google.cloud.lustre.v1alpha.Lustre.DeleteMirror`
  * `google.cloud.lustre.v1alpha.Lustre.GetDirectoryPolicy`
  * `google.cloud.lustre.v1alpha.Lustre.GetMirror`
  * `google.cloud.lustre.v1alpha.Lustre.ListDirectoryPolicies`
  * `google.cloud.lustre.v1alpha.Lustre.ListMirrors`
  * `google.cloud.lustre.v1alpha.Lustre.UpdateMirror`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
