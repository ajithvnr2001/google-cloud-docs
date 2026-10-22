---
url: https://docs.cloud.google.com/document-ai/docs/audit-logging/
title: Document AI audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:49.220196+00:00
---

# Document AI audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Document AI audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Document AI. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Document AI audit logs use the service name `documentai.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="documentai.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Document AI generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_WRITE` | `google.cloud.documentai.uiv1beta3.DocumentProcessorService.CreateLabelerPool` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.CreateProcessor`  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteLabelerPool` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteProcessor` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteProcessorVersion` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeployProcessorVersion` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.DisableProcessor` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.EnableProcessor` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.EvaluateProcessorVersion` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.ImportProcessorVersion` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.SetDefaultProcessorVersion` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.TrainProcessorVersion` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentProcessorService.UndeployProcessorVersion` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.BatchMoveDocuments` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.SampleDocuments` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.UpdateDataset` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.UpdateDatasetSchema`  
`google.cloud.documentai.v1.DocumentProcessorService.CreateProcessor`  
`google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessor` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersion` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.EvaluateProcessorVersion` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersion` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.CreateProcessor`  
`google.cloud.documentai.v1beta3.DocumentProcessorService.DeleteProcessor` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.DeleteProcessorVersion` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.DeployProcessorVersion` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.DisableProcessor` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.EnableProcessor` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.EvaluateProcessorVersion` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.ImportProcessorVersion` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.SetDefaultProcessorVersion` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.TrainProcessorVersion` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.UndeployProcessorVersion` (LRO)  
`google.cloud.documentai.v1beta3.DocumentService.UpdateDataset` (LRO)  
`google.cloud.documentai.v1beta3.DocumentService.UpdateDatasetSchema`  
`google.longrunning.Operations.CancelOperation`  
`DATA_READ` | `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ProcessDocument`  
`google.cloud.documentai.uiv1beta3.DocumentService.ExportDocuments` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.GetDocument`  
`google.cloud.documentai.uiv1beta3.DocumentService.GetThumbnails`  
`google.cloud.documentai.uiv1beta3.DocumentService.ListDocuments`  
`google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments` (LRO)  
`google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument`  
`google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.BatchProcessDocuments` (LRO)  
`google.cloud.documentai.v1beta3.DocumentProcessorService.ProcessDocument`  
`google.cloud.documentai.v1beta3.DocumentProcessorService.ReviewDocument` (LRO)  
`google.cloud.documentai.v1beta3.DocumentService.GetDocument`  
`google.cloud.documentai.v1beta3.DocumentService.ListDocuments`  
`DATA_WRITE` | `google.cloud.documentai.uiv1beta3.DocumentService.AutoLabelDocuments` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.BatchDeleteDocuments` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.ImportDocuments` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.ResyncDataset` (LRO)  
`google.cloud.documentai.uiv1beta3.DocumentService.UpdateDocument`  
`google.cloud.documentai.v1beta3.DocumentService.BatchDeleteDocuments` (LRO)  
`google.cloud.documentai.v1beta3.DocumentService.ImportDocuments` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Document AI.

### `google.cloud.documentai.uiv1beta3.DocumentProcessorService`

The following audit logs are associated with methods belonging to `google.cloud.documentai.uiv1beta3.DocumentProcessorService`.

#### `CreateLabelerPool`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.CreateLabelerPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.labelerPools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.CreateLabelerPool" `  




#### `CreateProcessor`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.CreateProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.CreateProcessor" `  




#### `DeleteLabelerPool`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteLabelerPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.labelerPools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteLabelerPool" `  




#### `DeleteProcessor`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteProcessor" `  




#### `DeleteProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeleteProcessorVersion" `  




#### `DeployProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeployProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.DeployProcessorVersion" `  




#### `DisableProcessor`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.DisableProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.DisableProcessor" `  




#### `EnableProcessor`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.EnableProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.EnableProcessor" `  




#### `EvaluateProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.EvaluateProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.evaluations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.EvaluateProcessorVersion" `  




#### `ExportProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ExportProcessorVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.ExportProcessorVersion" `  




#### `FetchHumanReviewDetails`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.FetchHumanReviewDetails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processors.fetchHumanReviewDetails - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.FetchHumanReviewDetails" `  




#### `GetEvaluation`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.evaluations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetEvaluation" `  




#### `GetEvaluationDocument`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetEvaluationDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.evaluationDocuments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetEvaluationDocument" `  




#### `GetHumanReviewConfig`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetHumanReviewConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.humanReviewConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetHumanReviewConfig" `  




#### `GetLabelerPool`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetLabelerPool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.labelerPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetLabelerPool" `  




#### `GetProcessor`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetProcessor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetProcessor" `  




#### `GetProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetProcessorVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetProcessorVersion" `  




#### `ImportProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ImportProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.ImportProcessorVersion" `  




#### `ListEvaluations`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.evaluations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListEvaluations" `  




#### `ListLabelerPools`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListLabelerPools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.labelerPools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListLabelerPools" `  




#### `ListProcessorVersions`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListProcessorVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListProcessorVersions" `  




#### `ListProcessors`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListProcessors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListProcessors" `  




#### `ProcessDocument`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ProcessDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.processOnline - DATA_READ`
    * `documentai.processors.processOnline - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.ProcessDocument" `  




#### `SearchEvaluationDocuments`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.SearchEvaluationDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.evaluations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.SearchEvaluationDocuments" `  




#### `SetDefaultProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.SetDefaultProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.SetDefaultProcessorVersion" `  




#### `TrainProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.TrainProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.TrainProcessorVersion" `  




#### `UndeployProcessorVersion`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentProcessorService.UndeployProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentProcessorService.UndeployProcessorVersion" `  




### `google.cloud.documentai.uiv1beta3.DocumentService`

The following audit logs are associated with methods belonging to `google.cloud.documentai.uiv1beta3.DocumentService`.

#### `AutoLabelDocuments`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.AutoLabelDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.updateDocuments - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.AutoLabelDocuments" `  




#### `BatchDeleteDocuments`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.BatchDeleteDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.deleteDocuments - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.BatchDeleteDocuments" `  




#### `BatchMoveDocuments`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.BatchMoveDocuments`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.datasets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.BatchMoveDocuments" `  




#### `ExportDocuments`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.ExportDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.listDocuments - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.ExportDocuments" `  




#### `GetAllDatasetSplitStats`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.GetAllDatasetSplitStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.GetAllDatasetSplitStats" `  




#### `GetDataset`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.GetDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.GetDataset" `  




#### `GetDatasetSchema`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.GetDatasetSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasetSchemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.GetDatasetSchema" `  




#### `GetDocument`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.getDocuments - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.GetDocument" `  




#### `GetThumbnails`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.GetThumbnails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.getDocuments - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.GetThumbnails" `  




#### `ImportDocuments`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.ImportDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.createDocuments - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.ImportDocuments" `  




#### `ListDocuments`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.ListDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.listDocuments - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.ListDocuments" `  




#### `ResyncDataset`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.ResyncDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.updateDocuments - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.ResyncDataset" `  




#### `SampleDocuments`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.SampleDocuments`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.datasets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.SampleDocuments" `  




#### `UpdateDataset`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.UpdateDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.datasets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.UpdateDataset" `  




#### `UpdateDatasetSchema`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.UpdateDatasetSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.datasetSchemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.UpdateDatasetSchema" `  




#### `UpdateDocument`

  * **Method** : `google.cloud.documentai.uiv1beta3.DocumentService.UpdateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.updateDocuments - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.uiv1beta3.DocumentService.UpdateDocument" `  




### `google.cloud.documentai.v1.DocumentProcessorService`

The following audit logs are associated with methods belonging to `google.cloud.documentai.v1.DocumentProcessorService`.

#### `BatchProcessDocuments`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.processBatch - DATA_READ`
    * `documentai.processors.processBatch - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments" `  




#### `CreateProcessor`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.CreateProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.CreateProcessor" `  




#### `DeleteProcessor`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessor" `  




#### `DeleteProcessorVersion`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersion" `  




#### `DeployProcessorVersion`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion" `  




#### `DisableProcessor`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor" `  




#### `EnableProcessor`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor" `  




#### `EvaluateProcessorVersion`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.EvaluateProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.evaluations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.EvaluateProcessorVersion" `  




#### `GetEvaluation`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.GetEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.evaluations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.GetEvaluation" `  




#### `GetProcessor`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.GetProcessor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.GetProcessor" `  




#### `GetProcessorVersion`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.GetProcessorVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.GetProcessorVersion" `  




#### `ListEvaluations`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.ListEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.evaluations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.ListEvaluations" `  




#### `ListProcessorVersions`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.ListProcessorVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.ListProcessorVersions" `  




#### `ListProcessors`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.ListProcessors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.ListProcessors" `  




#### `ProcessDocument`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.processOnline - DATA_READ`
    * `documentai.processors.processOnline - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument" `  




#### `ReviewDocument`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.humanReviewConfigs.review - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument" `  




#### `SetDefaultProcessorVersion`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion" `  




#### `TrainProcessorVersion`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersion" `  




#### `UndeployProcessorVersion`

  * **Method** : `google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion" `  




### `google.cloud.documentai.v1beta3.DocumentProcessorService`

The following audit logs are associated with methods belonging to `google.cloud.documentai.v1beta3.DocumentProcessorService`.

#### `BatchProcessDocuments`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.BatchProcessDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.processBatch - DATA_READ`
    * `documentai.processors.processBatch - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.BatchProcessDocuments" `  




#### `CreateProcessor`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.CreateProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.CreateProcessor" `  




#### `DeleteProcessor`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.DeleteProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.DeleteProcessor" `  




#### `DeleteProcessorVersion`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.DeleteProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.DeleteProcessorVersion" `  




#### `DeployProcessorVersion`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.DeployProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.DeployProcessorVersion" `  




#### `DisableProcessor`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.DisableProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.DisableProcessor" `  




#### `EnableProcessor`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.EnableProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.EnableProcessor" `  




#### `EvaluateProcessorVersion`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.EvaluateProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.evaluations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.EvaluateProcessorVersion" `  




#### `GetEvaluation`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.GetEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.evaluations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.GetEvaluation" `  




#### `GetProcessor`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.GetProcessor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.GetProcessor" `  




#### `GetProcessorVersion`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.GetProcessorVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.GetProcessorVersion" `  




#### `ImportProcessorVersion`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.ImportProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.ImportProcessorVersion" `  




#### `ListEvaluations`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.ListEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.evaluations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.ListEvaluations" `  




#### `ListProcessorVersions`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.ListProcessorVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.ListProcessorVersions" `  




#### `ListProcessors`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.ListProcessors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.ListProcessors" `  




#### `ProcessDocument`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.ProcessDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.processorVersions.processOnline - DATA_READ`
    * `documentai.processors.processOnline - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.ProcessDocument" `  




#### `ReviewDocument`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.ReviewDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.humanReviewConfigs.review - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.ReviewDocument" `  




#### `SetDefaultProcessorVersion`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.SetDefaultProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.SetDefaultProcessorVersion" `  




#### `TrainProcessorVersion`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.TrainProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.TrainProcessorVersion" `  




#### `UndeployProcessorVersion`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentProcessorService.UndeployProcessorVersion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentProcessorService.UndeployProcessorVersion" `  




### `google.cloud.documentai.v1beta3.DocumentService`

The following audit logs are associated with methods belonging to `google.cloud.documentai.v1beta3.DocumentService`.

#### `BatchDeleteDocuments`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentService.BatchDeleteDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.deleteDocuments - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentService.BatchDeleteDocuments" `  




#### `GetDatasetSchema`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentService.GetDatasetSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasetSchemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentService.GetDatasetSchema" `  




#### `GetDocument`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentService.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.getDocuments - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentService.GetDocument" `  




#### `ImportDocuments`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentService.ImportDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.createDocuments - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentService.ImportDocuments" `  




#### `ListDocuments`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentService.ListDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `documentai.datasets.listDocuments - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentService.ListDocuments" `  




#### `UpdateDataset`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentService.UpdateDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.datasets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentService.UpdateDataset" `  




#### `UpdateDatasetSchema`

  * **Method** : `google.cloud.documentai.v1beta3.DocumentService.UpdateDatasetSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.datasetSchemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.documentai.v1beta3.DocumentService.UpdateDatasetSchema" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `documentai.processorVersions.create - ADMIN_WRITE`
    * `documentai.processorVersions.processBatch - DATA_READ`
    * `documentai.processors.processBatch - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.documentai.uiv1beta3.DocumentProcessorService.FetchProcessorTypes`
  * `google.cloud.documentai.uiv1beta3.DocumentProcessorService.GetProcessorType`
  * `google.cloud.documentai.uiv1beta3.DocumentProcessorService.ListProcessorTypes`
  * `google.cloud.documentai.uiv1beta3.DocumentStorageService.AddDocumentStorageView`
  * `google.cloud.documentai.uiv1beta3.DocumentStorageService.CreateDocumentStorage`
  * `google.cloud.documentai.uiv1beta3.DocumentStorageService.GetDocumentStorageView`
  * `google.cloud.documentai.uiv1beta3.DocumentStorageService.ListRevisions`
  * `google.cloud.documentai.uiv1beta3.DocumentStorageService.RewriteDocumentStorageBase`
  * `google.cloud.documentai.uiv1beta3.DocumentStorageService.UpdateThumbnails`
  * `google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes`
  * `google.cloud.documentai.v1.DocumentProcessorService.GetProcessorType`
  * `google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes`
  * `google.cloud.documentai.v1beta3.DocumentProcessorService.FetchProcessorTypes`
  * `google.cloud.documentai.v1beta3.DocumentProcessorService.GetProcessorType`
  * `google.cloud.documentai.v1beta3.DocumentProcessorService.ListProcessorTypes`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`



[ Previous arrow_back  Customer-managed encryption keys (CMEK)  ](https://docs.cloud.google.com/document-ai/docs/cmek)

[ Next Create custom organization policies  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/custom-org-policies)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
