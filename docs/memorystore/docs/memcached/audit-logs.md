---
url: https://docs.cloud.google.com/memorystore/docs/memcached/audit-logs/
title: Memorystore for Memcached audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:51.045751+00:00
---

# Memorystore for Memcached audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/audit-logs/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Memorystore for Memcached audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Memorystore for Memcached. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Memorystore for Memcached audit logs use the service name `memcache.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="memcache.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Memorystore for Memcached generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.memcache.v1.CloudMemcache.GetInstance`  
`google.cloud.memcache.v1.CloudMemcache.ListInstances`  
`google.cloud.memcache.v1beta2.CloudMemcache.GetInstance`  
`google.cloud.memcache.v1beta2.CloudMemcache.ListInstances`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.memcache.v1.CloudMemcache.ApplyParameters` (LRO)  
`google.cloud.memcache.v1.CloudMemcache.CreateInstance` (LRO)  
`google.cloud.memcache.v1.CloudMemcache.DeleteInstance` (LRO)  
`google.cloud.memcache.v1.CloudMemcache.UpdateInstance` (LRO)  
`google.cloud.memcache.v1.CloudMemcache.UpdateParameters` (LRO)  
`google.cloud.memcache.v1.CloudMemcache.UpgradeInstance` (LRO)  
`google.cloud.memcache.v1beta2.CloudMemcache.ApplyParameters` (LRO)  
`google.cloud.memcache.v1beta2.CloudMemcache.ApplySoftwareUpdate`  
`google.cloud.memcache.v1beta2.CloudMemcache.CreateInstance` (LRO)  
`google.cloud.memcache.v1beta2.CloudMemcache.DeleteInstance` (LRO)  
`google.cloud.memcache.v1beta2.CloudMemcache.UpdateInstance` (LRO)  
`google.cloud.memcache.v1beta2.CloudMemcache.UpdateParameters` (LRO)  
`google.cloud.memcache.v1beta2.CloudMemcache.UpgradeInstance`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Memorystore for Memcached.

### `google.cloud.memcache.v1.CloudMemcache`

The following audit logs are associated with methods belonging to `google.cloud.memcache.v1.CloudMemcache`.

#### `ApplyParameters`

  * **Method** : `google.cloud.memcache.v1.CloudMemcache.ApplyParameters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.applyParameters - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1.CloudMemcache.ApplyParameters" `  




#### `CreateInstance`

  * **Method** : `google.cloud.memcache.v1.CloudMemcache.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1.CloudMemcache.CreateInstance" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.memcache.v1.CloudMemcache.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1.CloudMemcache.DeleteInstance" `  




#### `GetInstance`

  * **Method** : `google.cloud.memcache.v1.CloudMemcache.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `memcache.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1.CloudMemcache.GetInstance" `  




#### `ListInstances`

  * **Method** : `google.cloud.memcache.v1.CloudMemcache.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `memcache.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1.CloudMemcache.ListInstances" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.memcache.v1.CloudMemcache.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1.CloudMemcache.UpdateInstance" `  




#### `UpdateParameters`

  * **Method** : `google.cloud.memcache.v1.CloudMemcache.UpdateParameters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.updateParameters - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1.CloudMemcache.UpdateParameters" `  




#### `UpgradeInstance`

  * **Method** : `google.cloud.memcache.v1.CloudMemcache.UpgradeInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1.CloudMemcache.UpgradeInstance" `  




### `google.cloud.memcache.v1beta2.CloudMemcache`

The following audit logs are associated with methods belonging to `google.cloud.memcache.v1beta2.CloudMemcache`.

#### `ApplyParameters`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.ApplyParameters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.applyParameters - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.ApplyParameters" `  




#### `ApplySoftwareUpdate`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.ApplySoftwareUpdate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.applySoftwareUpdate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.ApplySoftwareUpdate" `  




#### `CreateInstance`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.CreateInstance" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.DeleteInstance" `  




#### `GetInstance`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `memcache.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.GetInstance" `  




#### `ListInstances`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `memcache.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.ListInstances" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.UpdateInstance" `  




#### `UpdateParameters`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.UpdateParameters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.updateParameters - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.UpdateParameters" `  




#### `UpgradeInstance`

  * **Method** : `google.cloud.memcache.v1beta2.CloudMemcache.UpgradeInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.instances.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.memcache.v1beta2.CloudMemcache.UpgradeInstance" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `memcache.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `memcache.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `memcache.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
