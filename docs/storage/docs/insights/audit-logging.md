---
url: https://docs.cloud.google.com/storage/docs/insights/audit-logging/
title: Storage Insights audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:47:36.204542+00:00
---

# Storage Insights audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Storage Insights audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Storage Insights. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Storage Insights audit logs use the service name `storageinsights.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="storageinsights.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Storage Insights generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.location.Locations.ListLocations`  
`google.cloud.storageinsights.v1.StorageInsights.GetDatasetConfig`  
`google.cloud.storageinsights.v1.StorageInsights.GetReportConfig`  
`google.cloud.storageinsights.v1.StorageInsights.GetReportDetail`  
`google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs`  
`google.cloud.storageinsights.v1.StorageInsights.ListReportConfigs`  
`google.cloud.storageinsights.v1.StorageInsights.ListReportDetails`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.storageinsights.v1.StorageInsights.CreateDatasetConfig` (LRO)  
`google.cloud.storageinsights.v1.StorageInsights.CreateReportConfig`  
`google.cloud.storageinsights.v1.StorageInsights.DeleteDatasetConfig` (LRO)  
`google.cloud.storageinsights.v1.StorageInsights.DeleteReportConfig`  
`google.cloud.storageinsights.v1.StorageInsights.LinkDataset` (LRO)  
`google.cloud.storageinsights.v1.StorageInsights.UnlinkDataset` (LRO)  
`google.cloud.storageinsights.v1.StorageInsights.UpdateDatasetConfig` (LRO)  
`google.cloud.storageinsights.v1.StorageInsights.UpdateReportConfig`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Cloud Identity and Access Management documentation for Storage Insights.

### `google.cloud.location.Locations`

The following audit logs are associated with methods belonging to `google.cloud.location.Locations`.

#### `ListLocations`

  * **Method** : `google.cloud.location.Locations.ListLocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.locations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.ListLocations" `  




### `google.cloud.storageinsights.v1.StorageInsights`

The following audit logs are associated with methods belonging to `google.cloud.storageinsights.v1.StorageInsights`.

#### `CreateDatasetConfig`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.CreateDatasetConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `storageinsights.datasetConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.CreateDatasetConfig" `  




#### `CreateReportConfig`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.CreateReportConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `storageinsights.reportConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.CreateReportConfig" `  




#### `DeleteDatasetConfig`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.DeleteDatasetConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `storageinsights.datasetConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.DeleteDatasetConfig" `  




#### `DeleteReportConfig`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.DeleteReportConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `storageinsights.reportConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.DeleteReportConfig" `  




#### `GetDatasetConfig`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.GetDatasetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.datasetConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.GetDatasetConfig" `  




#### `GetReportConfig`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.GetReportConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.reportConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.GetReportConfig" `  




#### `GetReportDetail`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.GetReportDetail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.reportDetails.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.GetReportDetail" `  




#### `LinkDataset`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.LinkDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `storageinsights.datasetConfigs.linkDataset - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.LinkDataset" `  




#### `ListDatasetConfigs`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.datasetConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs" `  




#### `ListReportConfigs`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.ListReportConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.reportConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.ListReportConfigs" `  




#### `ListReportDetails`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.ListReportDetails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.reportDetails.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.ListReportDetails" `  




#### `UnlinkDataset`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.UnlinkDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `storageinsights.datasetConfigs.unlinkDataset - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.UnlinkDataset" `  




#### `UpdateDatasetConfig`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.UpdateDatasetConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `storageinsights.datasetConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.UpdateDatasetConfig" `  




#### `UpdateReportConfig`

  * **Method** : `google.cloud.storageinsights.v1.StorageInsights.UpdateReportConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `storageinsights.reportConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.storageinsights.v1.StorageInsights.UpdateReportConfig" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `storageinsights.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-14 UTC."],[],[]] 
