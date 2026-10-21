---
url: https://docs.cloud.google.com/translate/docs/audit-logging/
title: Cloud Translation audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:14.169336+00:00
---

# Cloud Translation audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Translation audit logging

This document lists the audited methods for Cloud Translation. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

Audit logging is available only for Cloud Translation - Advanced (v3), and not for Cloud Translation - Basic (v2).

## Service name

To view the Cloud Translation audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="translate.googleapis.com"
           




## Methods by permission type

If you specify an AutoML Translation model, then calls to `TranslateText`, `BatchTranslateText`, and `GetSupportedLanguages` are not logged.

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Translation generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.translation.v3.TranslationService.GetAdaptiveMtDataset`  
`google.cloud.translation.v3.TranslationService.GetAdaptiveMtFile`  
`google.cloud.translation.v3.TranslationService.GetDataset`  
`google.cloud.translation.v3.TranslationService.GetGlossary`  
`google.cloud.translation.v3.TranslationService.GetModel`  
`google.cloud.translation.v3.TranslationService.GetSupportedLanguages`  
`google.cloud.translation.v3.TranslationService.ListAdaptiveMtDatasets`  
`google.cloud.translation.v3.TranslationService.ListAdaptiveMtFiles`  
`google.cloud.translation.v3.TranslationService.ListAdaptiveMtSentences`  
`google.cloud.translation.v3.TranslationService.ListDatasets`  
`google.cloud.translation.v3.TranslationService.ListGlossaries`  
`google.cloud.translation.v3.TranslationService.ListModels`  
`google.cloud.translation.v3beta1.TranslationService.GetGlossary`  
`google.cloud.translation.v3beta1.TranslationService.GetSupportedLanguages`  
`google.cloud.translation.v3beta1.TranslationService.ListGlossaries`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`google.longrunning.Operations.WaitOperation`  
`ADMIN_WRITE` | `google.cloud.translation.v3.TranslationService.CreateAdaptiveMtDataset`  
`google.cloud.translation.v3.TranslationService.CreateDataset`  
`google.cloud.translation.v3.TranslationService.CreateGlossary` (LRO)  
`google.cloud.translation.v3.TranslationService.CreateModel`  
`google.cloud.translation.v3.TranslationService.DeleteAdaptiveMtDataset`  
`google.cloud.translation.v3.TranslationService.DeleteAdaptiveMtFile`  
`google.cloud.translation.v3.TranslationService.DeleteDataset`  
`google.cloud.translation.v3.TranslationService.DeleteGlossary` (LRO)  
`google.cloud.translation.v3.TranslationService.DeleteModel`  
`google.cloud.translation.v3.TranslationService.ImportAdaptiveMtFile`  
`google.cloud.translation.v3beta1.TranslationService.CreateGlossary` (LRO)  
`google.cloud.translation.v3beta1.TranslationService.DeleteGlossary` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.location.Locations.GetLocation`  
`google.cloud.location.Locations.ListLocations`  
`google.cloud.translation.v3.TranslationService.AdaptiveMtTranslate`  
`google.cloud.translation.v3.TranslationService.BatchTranslateDocument` (LRO)  
`google.cloud.translation.v3.TranslationService.BatchTranslateText` (LRO)  
`google.cloud.translation.v3.TranslationService.DetectLanguage`  
`google.cloud.translation.v3.TranslationService.ExportData`  
`google.cloud.translation.v3.TranslationService.GetGlossaryEntry`  
`google.cloud.translation.v3.TranslationService.ListExamples`  
`google.cloud.translation.v3.TranslationService.ListGlossaryEntries`  
`google.cloud.translation.v3.TranslationService.TranslateDocument`  
`google.cloud.translation.v3.TranslationService.TranslateText`  
`google.cloud.translation.v3beta1.TranslationService.BatchTranslateDocument` (LRO)  
`google.cloud.translation.v3beta1.TranslationService.BatchTranslateText` (LRO)  
`google.cloud.translation.v3beta1.TranslationService.DetectLanguage`  
`google.cloud.translation.v3beta1.TranslationService.TranslateDocument`  
`google.cloud.translation.v3beta1.TranslationService.TranslateText`  
`DATA_WRITE` | `google.cloud.translation.v3.TranslationService.CreateGlossaryEntry`  
`google.cloud.translation.v3.TranslationService.DeleteGlossaryEntry`  
`google.cloud.translation.v3.TranslationService.ImportData`  
`google.cloud.translation.v3.TranslationService.UpdateGlossary`  
`google.cloud.translation.v3.TranslationService.UpdateGlossaryEntry`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Translation.

### `google.cloud.location.Locations`

The following audit logs are associated with methods belonging to `google.cloud.location.Locations`.

#### `GetLocation`

  * **Method** : `google.cloud.location.Locations.GetLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.locations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.GetLocation" `  




#### `ListLocations`

  * **Method** : `google.cloud.location.Locations.ListLocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.locations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.ListLocations" `  




### `google.cloud.translation.v3.TranslationService`

The following audit logs are associated with methods belonging to `google.cloud.translation.v3.TranslationService`.

#### `AdaptiveMtTranslate`

  * **Method** : `google.cloud.translation.v3.TranslationService.AdaptiveMtTranslate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtDatasets.predict - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.AdaptiveMtTranslate" `  




#### `BatchTranslateDocument`

  * **Method** : `google.cloud.translation.v3.TranslationService.BatchTranslateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.generalModels.batchDocPredict - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.BatchTranslateDocument" `  




#### `BatchTranslateText`

  * **Method** : `google.cloud.translation.v3.TranslationService.BatchTranslateText`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `automl.models.predict - PERMISSION_TYPE_UNSPECIFIED`
    * `cloudtranslate.generalModels.batchPredict - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.BatchTranslateText" `  




#### `CreateAdaptiveMtDataset`

  * **Method** : `google.cloud.translation.v3.TranslationService.CreateAdaptiveMtDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtDatasets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.CreateAdaptiveMtDataset" `  




#### `CreateDataset`

  * **Method** : `google.cloud.translation.v3.TranslationService.CreateDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.datasets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.CreateDataset" `  




#### `CreateGlossary`

  * **Method** : `google.cloud.translation.v3.TranslationService.CreateGlossary`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.CreateGlossary" `  




#### `CreateGlossaryEntry`

  * **Method** : `google.cloud.translation.v3.TranslationService.CreateGlossaryEntry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaryentries.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.CreateGlossaryEntry" `  




#### `CreateModel`

  * **Method** : `google.cloud.translation.v3.TranslationService.CreateModel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.customModels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.CreateModel" `  




#### `DeleteAdaptiveMtDataset`

  * **Method** : `google.cloud.translation.v3.TranslationService.DeleteAdaptiveMtDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtDatasets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.DeleteAdaptiveMtDataset" `  




#### `DeleteAdaptiveMtFile`

  * **Method** : `google.cloud.translation.v3.TranslationService.DeleteAdaptiveMtFile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtFiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.DeleteAdaptiveMtFile" `  




#### `DeleteDataset`

  * **Method** : `google.cloud.translation.v3.TranslationService.DeleteDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.datasets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.DeleteDataset" `  




#### `DeleteGlossary`

  * **Method** : `google.cloud.translation.v3.TranslationService.DeleteGlossary`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.DeleteGlossary" `  




#### `DeleteGlossaryEntry`

  * **Method** : `google.cloud.translation.v3.TranslationService.DeleteGlossaryEntry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaryentries.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.DeleteGlossaryEntry" `  




#### `DeleteModel`

  * **Method** : `google.cloud.translation.v3.TranslationService.DeleteModel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.customModels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.DeleteModel" `  




#### `DetectLanguage`

  * **Method** : `google.cloud.translation.v3.TranslationService.DetectLanguage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.languageDetectionModels.predict - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.DetectLanguage" `  




#### `ExportData`

  * **Method** : `google.cloud.translation.v3.TranslationService.ExportData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.datasets.export - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ExportData" `  




#### `GetAdaptiveMtDataset`

  * **Method** : `google.cloud.translation.v3.TranslationService.GetAdaptiveMtDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtDatasets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.GetAdaptiveMtDataset" `  




#### `GetAdaptiveMtFile`

  * **Method** : `google.cloud.translation.v3.TranslationService.GetAdaptiveMtFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtFiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.GetAdaptiveMtFile" `  




#### `GetDataset`

  * **Method** : `google.cloud.translation.v3.TranslationService.GetDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.datasets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.GetDataset" `  




#### `GetGlossary`

  * **Method** : `google.cloud.translation.v3.TranslationService.GetGlossary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.GetGlossary" `  




#### `GetGlossaryEntry`

  * **Method** : `google.cloud.translation.v3.TranslationService.GetGlossaryEntry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaryentries.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.GetGlossaryEntry" `  




#### `GetModel`

  * **Method** : `google.cloud.translation.v3.TranslationService.GetModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.customModels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.GetModel" `  




#### `GetSupportedLanguages`

  * **Method** : `google.cloud.translation.v3.TranslationService.GetSupportedLanguages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.generalModels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.GetSupportedLanguages" `  




#### `ImportAdaptiveMtFile`

  * **Method** : `google.cloud.translation.v3.TranslationService.ImportAdaptiveMtFile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtDatasets.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ImportAdaptiveMtFile" `  




#### `ImportData`

  * **Method** : `google.cloud.translation.v3.TranslationService.ImportData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.datasets.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ImportData" `  




#### `ListAdaptiveMtDatasets`

  * **Method** : `google.cloud.translation.v3.TranslationService.ListAdaptiveMtDatasets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtDatasets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ListAdaptiveMtDatasets" `  




#### `ListAdaptiveMtFiles`

  * **Method** : `google.cloud.translation.v3.TranslationService.ListAdaptiveMtFiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtFiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ListAdaptiveMtFiles" `  




#### `ListAdaptiveMtSentences`

  * **Method** : `google.cloud.translation.v3.TranslationService.ListAdaptiveMtSentences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.adaptiveMtSentences.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ListAdaptiveMtSentences" `  




#### `ListDatasets`

  * **Method** : `google.cloud.translation.v3.TranslationService.ListDatasets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.datasets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ListDatasets" `  




#### `ListExamples`

  * **Method** : `google.cloud.translation.v3.TranslationService.ListExamples`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.datasets.export - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ListExamples" `  




#### `ListGlossaries`

  * **Method** : `google.cloud.translation.v3.TranslationService.ListGlossaries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ListGlossaries" `  




#### `ListGlossaryEntries`

  * **Method** : `google.cloud.translation.v3.TranslationService.ListGlossaryEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaryentries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ListGlossaryEntries" `  




#### `ListModels`

  * **Method** : `google.cloud.translation.v3.TranslationService.ListModels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.customModels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.ListModels" `  




#### `TranslateDocument`

  * **Method** : `google.cloud.translation.v3.TranslationService.TranslateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.generalModels.docPredict - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.TranslateDocument" `  




#### `TranslateText`

  * **Method** : `google.cloud.translation.v3.TranslationService.TranslateText`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.generalModels.predict - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.TranslateText" `  




#### `UpdateGlossary`

  * **Method** : `google.cloud.translation.v3.TranslationService.UpdateGlossary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.UpdateGlossary" `  




#### `UpdateGlossaryEntry`

  * **Method** : `google.cloud.translation.v3.TranslationService.UpdateGlossaryEntry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaryentries.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3.TranslationService.UpdateGlossaryEntry" `  




### `google.cloud.translation.v3beta1.TranslationService`

The following audit logs are associated with methods belonging to `google.cloud.translation.v3beta1.TranslationService`.

#### `BatchTranslateDocument`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.BatchTranslateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.customModels.predict - DATA_READ`
    * `cloudtranslate.generalModels.batchDocPredict - DATA_READ`
    * `cloudtranslate.glossaries.batchDocPredict - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.BatchTranslateDocument" `  




#### `BatchTranslateText`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.BatchTranslateText`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `automl.models.predict - PERMISSION_TYPE_UNSPECIFIED`
    * `cloudtranslate.customModels.predict - DATA_READ`
    * `cloudtranslate.generalModels.batchPredict - DATA_READ`
    * `cloudtranslate.glossaries.batchPredict - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.BatchTranslateText" `  




#### `CreateGlossary`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.CreateGlossary`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.CreateGlossary" `  




#### `DeleteGlossary`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.DeleteGlossary`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.DeleteGlossary" `  




#### `DetectLanguage`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.DetectLanguage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.languageDetectionModels.predict - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.DetectLanguage" `  




#### `GetGlossary`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.GetGlossary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.GetGlossary" `  




#### `GetSupportedLanguages`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.GetSupportedLanguages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.generalModels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.GetSupportedLanguages" `  




#### `ListGlossaries`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.ListGlossaries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.glossaries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.ListGlossaries" `  




#### `TranslateDocument`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.TranslateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.generalModels.docPredict - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.TranslateDocument" `  




#### `TranslateText`

  * **Method** : `google.cloud.translation.v3beta1.TranslationService.TranslateText`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.generalModels.predict - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.translation.v3beta1.TranslationService.TranslateText" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtranslate.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




#### `WaitOperation`

  * **Method** : `google.longrunning.Operations.WaitOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtranslate.operations.wait - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.WaitOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.translate.v2.TranslateService.DetectLanguage`
  * `google.cloud.translate.v2.TranslateService.GetSupportedLanguages`
  * `google.cloud.translate.v2.TranslateService.TranslateText`
  * `google.cloud.translation.v3.TranslationService.RomanizeText`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
