---
url: https://docs.cloud.google.com/functions/docs/monitoring/audit-logging/
title: Functions audit logging \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:57.658649+00:00
---

# Functions audit logging  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/monitoring/audit-logging/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Functions audit logging

**Note:** Cloud Functions (2nd gen) is now Cloud Run functions. The information on this page applies to functions created with the `gcloud functions` command or with the Cloud Functions v2 API, which is still supported for performing operations on functions. If you've created or deployed a function using Cloud Run, see [Cloud Run audit logging](https://docs.cloud.google.com/run/docs/audit-logging).

This document lists the audited methods for Cloud Run functions. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Run functions audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudfunctions.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Run functions generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.functions.v1.CloudFunctionsService.GenerateDownloadUrl`  
`google.cloud.functions.v1.CloudFunctionsService.GetFunction`  
`GetIamPolicy`  
`google.cloud.functions.v1.CloudFunctionsService.ListFunctions`  
`google.cloud.functions.v2.FunctionService.GenerateDownloadUrl`  
`google.cloud.functions.v2.FunctionService.GetFunction`  
`google.cloud.functions.v2.FunctionService.ListFunctions`  
`google.cloud.functions.v2alpha.FunctionService.GenerateDownloadUrl`  
`google.cloud.functions.v2alpha.FunctionService.GetFunction`  
`google.cloud.functions.v2alpha.FunctionService.ListFunctions`  
`google.cloud.functions.v2beta.FunctionService.GenerateDownloadUrl`  
`google.cloud.functions.v2beta.FunctionService.GetFunction`  
`google.cloud.functions.v2beta.FunctionService.ListFunctions`  
`google.cloud.location.Locations.ListLocations`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.functions.v1.CloudFunctionsService.CreateFunction` (LRO)  
`google.cloud.functions.v1.CloudFunctionsService.DeleteFunction` (LRO)  
`google.cloud.functions.v1.CloudFunctionsService.GenerateUploadUrl`  
`SetIamPolicy`  
`google.cloud.functions.v1.CloudFunctionsService.UpdateFunction` (LRO)  
`google.cloud.functions.v2.FunctionService.AbortFunctionUpgrade` (LRO)  
`google.cloud.functions.v2.FunctionService.CommitFunctionUpgrade` (LRO)  
`google.cloud.functions.v2.FunctionService.CommitFunctionUpgradeAsGen2` (LRO)  
`google.cloud.functions.v2.FunctionService.CreateFunction` (LRO)  
`google.cloud.functions.v2.FunctionService.DeleteFunction` (LRO)  
`google.cloud.functions.v2.FunctionService.DetachFunction` (LRO)  
`google.cloud.functions.v2.FunctionService.GenerateUploadUrl`  
`google.cloud.functions.v2.FunctionService.RedirectFunctionUpgradeTraffic` (LRO)  
`google.cloud.functions.v2.FunctionService.RollbackFunctionUpgradeTraffic` (LRO)  
`google.cloud.functions.v2.FunctionService.SetupFunctionUpgradeConfig` (LRO)  
`google.cloud.functions.v2.FunctionService.UpdateFunction` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.AbortFunctionUpgrade` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.CommitFunctionUpgrade` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.CommitFunctionUpgradeAsGen2` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.CreateFunction` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.DeleteFunction` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.DetachFunction` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.GenerateUploadUrl`  
`google.cloud.functions.v2alpha.FunctionService.RedirectFunctionUpgradeTraffic` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.RollbackFunctionUpgradeTraffic` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.SetupFunctionUpgradeConfig` (LRO)  
`google.cloud.functions.v2alpha.FunctionService.UpdateFunction` (LRO)  
`google.cloud.functions.v2beta.FunctionService.AbortFunctionUpgrade` (LRO)  
`google.cloud.functions.v2beta.FunctionService.CommitFunctionUpgrade` (LRO)  
`google.cloud.functions.v2beta.FunctionService.CommitFunctionUpgradeAsGen2` (LRO)  
`google.cloud.functions.v2beta.FunctionService.CreateFunction` (LRO)  
`google.cloud.functions.v2beta.FunctionService.DeleteFunction` (LRO)  
`google.cloud.functions.v2beta.FunctionService.DetachFunction` (LRO)  
`google.cloud.functions.v2beta.FunctionService.GenerateUploadUrl`  
`google.cloud.functions.v2beta.FunctionService.RedirectFunctionUpgradeTraffic` (LRO)  
`google.cloud.functions.v2beta.FunctionService.RollbackFunctionUpgradeTraffic` (LRO)  
`google.cloud.functions.v2beta.FunctionService.SetupFunctionUpgradeConfig` (LRO)  
`google.cloud.functions.v2beta.FunctionService.UpdateFunction` (LRO)  
`SetIamPolicy`  
`DATA_READ` | `google.cloud.functions.v1.CloudFunctionsService.CallFunction`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Run functions.

### `google.cloud.functions.v1.CloudFunctionsService`

The following audit logs are associated with methods belonging to `google.cloud.functions.v1.CloudFunctionsService`.

#### `CallFunction`

  * **Method** : `google.cloud.functions.v1.CloudFunctionsService.CallFunction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.call - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v1.CloudFunctionsService.CallFunction" `  




#### `CreateFunction`

  * **Method** : `google.cloud.functions.v1.CloudFunctionsService.CreateFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v1.CloudFunctionsService.CreateFunction" `  




#### `DeleteFunction`

  * **Method** : `google.cloud.functions.v1.CloudFunctionsService.DeleteFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v1.CloudFunctionsService.DeleteFunction" `  




#### `GenerateDownloadUrl`

  * **Method** : `google.cloud.functions.v1.CloudFunctionsService.GenerateDownloadUrl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.sourceCodeGet - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v1.CloudFunctionsService.GenerateDownloadUrl" `  




#### `GenerateUploadUrl`

  * **Method** : `google.cloud.functions.v1.CloudFunctionsService.GenerateUploadUrl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.sourceCodeSet - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v1.CloudFunctionsService.GenerateUploadUrl" `  




#### `GetFunction`

  * **Method** : `google.cloud.functions.v1.CloudFunctionsService.GetFunction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v1.CloudFunctionsService.GetFunction" `  




#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `ListFunctions`

  * **Method** : `google.cloud.functions.v1.CloudFunctionsService.ListFunctions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v1.CloudFunctionsService.ListFunctions" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




#### `UpdateFunction`

  * **Method** : `google.cloud.functions.v1.CloudFunctionsService.UpdateFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v1.CloudFunctionsService.UpdateFunction" `  




### `google.cloud.functions.v2.FunctionService`

The following audit logs are associated with methods belonging to `google.cloud.functions.v2.FunctionService`.

#### `AbortFunctionUpgrade`

  * **Method** : `google.cloud.functions.v2.FunctionService.AbortFunctionUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.AbortFunctionUpgrade" `  




#### `CommitFunctionUpgrade`

  * **Method** : `google.cloud.functions.v2.FunctionService.CommitFunctionUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.CommitFunctionUpgrade" `  




#### `CommitFunctionUpgradeAsGen2`

  * **Method** : `google.cloud.functions.v2.FunctionService.CommitFunctionUpgradeAsGen2`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.CommitFunctionUpgradeAsGen2" `  




#### `CreateFunction`

  * **Method** : `google.cloud.functions.v2.FunctionService.CreateFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.CreateFunction" `  




#### `DeleteFunction`

  * **Method** : `google.cloud.functions.v2.FunctionService.DeleteFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.DeleteFunction" `  




#### `DetachFunction`

  * **Method** : `google.cloud.functions.v2.FunctionService.DetachFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.DetachFunction" `  




#### `GenerateDownloadUrl`

  * **Method** : `google.cloud.functions.v2.FunctionService.GenerateDownloadUrl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.sourceCodeGet - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.GenerateDownloadUrl" `  




#### `GenerateUploadUrl`

  * **Method** : `google.cloud.functions.v2.FunctionService.GenerateUploadUrl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generateUploadUrl - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.GenerateUploadUrl" `  




#### `GetFunction`

  * **Method** : `google.cloud.functions.v2.FunctionService.GetFunction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.GetFunction" `  




#### `ListFunctions`

  * **Method** : `google.cloud.functions.v2.FunctionService.ListFunctions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.ListFunctions" `  




#### `RedirectFunctionUpgradeTraffic`

  * **Method** : `google.cloud.functions.v2.FunctionService.RedirectFunctionUpgradeTraffic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.RedirectFunctionUpgradeTraffic" `  




#### `RollbackFunctionUpgradeTraffic`

  * **Method** : `google.cloud.functions.v2.FunctionService.RollbackFunctionUpgradeTraffic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.RollbackFunctionUpgradeTraffic" `  




#### `SetupFunctionUpgradeConfig`

  * **Method** : `google.cloud.functions.v2.FunctionService.SetupFunctionUpgradeConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.SetupFunctionUpgradeConfig" `  




#### `UpdateFunction`

  * **Method** : `google.cloud.functions.v2.FunctionService.UpdateFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2.FunctionService.UpdateFunction" `  




### `google.cloud.functions.v2alpha.FunctionService`

The following audit logs are associated with methods belonging to `google.cloud.functions.v2alpha.FunctionService`.

#### `AbortFunctionUpgrade`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.AbortFunctionUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.AbortFunctionUpgrade" `  




#### `CommitFunctionUpgrade`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.CommitFunctionUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.CommitFunctionUpgrade" `  




#### `CommitFunctionUpgradeAsGen2`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.CommitFunctionUpgradeAsGen2`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.CommitFunctionUpgradeAsGen2" `  




#### `CreateFunction`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.CreateFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.CreateFunction" `  




#### `DeleteFunction`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.DeleteFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.DeleteFunction" `  




#### `DetachFunction`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.DetachFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.DetachFunction" `  




#### `GenerateDownloadUrl`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.GenerateDownloadUrl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.sourceCodeGet - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.GenerateDownloadUrl" `  




#### `GenerateUploadUrl`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.GenerateUploadUrl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generateUploadUrl - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.GenerateUploadUrl" `  




#### `GetFunction`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.GetFunction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.GetFunction" `  




#### `ListFunctions`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.ListFunctions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.ListFunctions" `  




#### `RedirectFunctionUpgradeTraffic`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.RedirectFunctionUpgradeTraffic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.RedirectFunctionUpgradeTraffic" `  




#### `RollbackFunctionUpgradeTraffic`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.RollbackFunctionUpgradeTraffic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.RollbackFunctionUpgradeTraffic" `  




#### `SetupFunctionUpgradeConfig`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.SetupFunctionUpgradeConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.SetupFunctionUpgradeConfig" `  




#### `UpdateFunction`

  * **Method** : `google.cloud.functions.v2alpha.FunctionService.UpdateFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2alpha.FunctionService.UpdateFunction" `  




### `google.cloud.functions.v2beta.FunctionService`

The following audit logs are associated with methods belonging to `google.cloud.functions.v2beta.FunctionService`.

#### `AbortFunctionUpgrade`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.AbortFunctionUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.AbortFunctionUpgrade" `  




#### `CommitFunctionUpgrade`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.CommitFunctionUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.CommitFunctionUpgrade" `  




#### `CommitFunctionUpgradeAsGen2`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.CommitFunctionUpgradeAsGen2`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.CommitFunctionUpgradeAsGen2" `  




#### `CreateFunction`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.CreateFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.CreateFunction" `  




#### `DeleteFunction`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.DeleteFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.DeleteFunction" `  




#### `DetachFunction`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.DetachFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.DetachFunction" `  




#### `GenerateDownloadUrl`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.GenerateDownloadUrl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.sourceCodeGet - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.GenerateDownloadUrl" `  




#### `GenerateUploadUrl`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.GenerateUploadUrl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generateUploadUrl - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.GenerateUploadUrl" `  




#### `GetFunction`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.GetFunction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.GetFunction" `  




#### `ListFunctions`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.ListFunctions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.ListFunctions" `  




#### `RedirectFunctionUpgradeTraffic`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.RedirectFunctionUpgradeTraffic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.RedirectFunctionUpgradeTraffic" `  




#### `RollbackFunctionUpgradeTraffic`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.RollbackFunctionUpgradeTraffic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.RollbackFunctionUpgradeTraffic" `  




#### `SetupFunctionUpgradeConfig`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.SetupFunctionUpgradeConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.generationUpgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.SetupFunctionUpgradeConfig" `  




#### `UpdateFunction`

  * **Method** : `google.cloud.functions.v2beta.FunctionService.UpdateFunction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.functions.v2beta.FunctionService.UpdateFunction" `  




### `google.cloud.location.Locations`

The following audit logs are associated with methods belonging to `google.cloud.location.Locations`.

#### `ListLocations`

  * **Method** : `google.cloud.location.Locations.ListLocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.locations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.ListLocations" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.functions.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudfunctions.functions.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudfunctions.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.functions.v1.CloudFunctionsService.TestIamPermissions`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
