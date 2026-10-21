---
url: https://docs.cloud.google.com/vision-ai/docs/audit-logging/
title: Gemini Enterprise Agent Platform Vision audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:36.663660+00:00
---

# Gemini Enterprise Agent Platform Vision audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/audit-logging/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Gemini Enterprise Agent Platform Vision audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Vertex AI Vision. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Vertex AI Vision audit logs use the service name `visionai.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="visionai.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Vertex AI Vision generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.visionai.v1.AppPlatform.GetApplication`  
`google.cloud.visionai.v1.AppPlatform.GetDraft`  
`google.cloud.visionai.v1.AppPlatform.ListApplications`  
`google.cloud.visionai.v1.AppPlatform.ListDrafts`  
`google.cloud.visionai.v1.AppPlatform.ListInstances`  
`google.cloud.visionai.v1.AppPlatform.ListPrebuiltProcessors`  
`google.cloud.visionai.v1.AppPlatform.ListProcessors`  
`google.cloud.visionai.v1.LiveVideoAnalytics.ResolveOperatorInfo`  
`google.cloud.visionai.v1.StreamingService.ReceiveEvents`  
`google.cloud.visionai.v1.StreamsService.GenerateStreamHlsToken`  
`google.cloud.visionai.v1.StreamsService.GetCluster`  
`google.cloud.visionai.v1.StreamsService.GetEvent`  
`google.cloud.visionai.v1.StreamsService.GetSeries`  
`google.cloud.visionai.v1.StreamsService.GetStream`  
`google.cloud.visionai.v1.StreamsService.GetStreamThumbnail`  
`google.cloud.visionai.v1.StreamsService.ListClusters`  
`google.cloud.visionai.v1.StreamsService.ListSeries`  
`google.cloud.visionai.v1.StreamsService.ListStreams`  
`google.cloud.visionai.v1.Warehouse.GetAsset`  
`google.cloud.visionai.v1.Warehouse.GetCollection`  
`google.cloud.visionai.v1.Warehouse.GetCorpus`  
`google.cloud.visionai.v1.Warehouse.GetDataSchema`  
`google.cloud.visionai.v1.Warehouse.GetIndex`  
`google.cloud.visionai.v1.Warehouse.GetIndexEndpoint`  
`google.cloud.visionai.v1.Warehouse.GetSearchConfig`  
`google.cloud.visionai.v1.Warehouse.GetSearchHypernym`  
`google.cloud.visionai.v1.Warehouse.ListAssets`  
`google.cloud.visionai.v1.Warehouse.ListCollections`  
`google.cloud.visionai.v1.Warehouse.ListCorpora`  
`google.cloud.visionai.v1.Warehouse.ListDataSchemas`  
`google.cloud.visionai.v1.Warehouse.ListIndexEndpoints`  
`google.cloud.visionai.v1.Warehouse.ListIndexes`  
`google.cloud.visionai.v1.Warehouse.ListSearchHypernyms`  
`google.cloud.visionai.v1.Warehouse.ViewCollectionItems`  
`google.cloud.visionai.v1.Warehouse.ViewIndexedAssets`  
`google.cloud.visionai.v1alpha1.AppPlatform.GetApplication`  
`google.cloud.visionai.v1alpha1.AppPlatform.GetDraft`  
`google.cloud.visionai.v1alpha1.AppPlatform.GetInstance`  
`google.cloud.visionai.v1alpha1.AppPlatform.ListApplications`  
`google.cloud.visionai.v1alpha1.AppPlatform.ListDrafts`  
`google.cloud.visionai.v1alpha1.AppPlatform.ListInstances`  
`google.cloud.visionai.v1alpha1.AppPlatform.ListPrebuiltProcessors`  
`google.cloud.visionai.v1alpha1.AppPlatform.ListProcessors`  
`google.cloud.visionai.v1alpha1.LiveVideoAnalytics.ListAnalyses`  
`google.cloud.visionai.v1alpha1.StreamsService.ListEvents`  
`google.cloud.visionai.v1alpha1.StreamsService.ListSeries`  
`google.cloud.visionai.v1alpha1.StreamsService.ListStreams`  
`google.cloud.visionai.v1alpha1.Warehouse.GetAsset`  
`google.cloud.visionai.v1alpha1.Warehouse.GetCorpus`  
`google.cloud.visionai.v1alpha1.Warehouse.GetDataSchema`  
`google.cloud.visionai.v1alpha1.Warehouse.GetSearchConfig`  
`google.cloud.visionai.v1alpha1.Warehouse.ListAssets`  
`google.cloud.visionai.v1alpha1.Warehouse.ListCorpora`  
`google.cloud.visionai.v1alpha1.Warehouse.ListDataSchemas`  
`google.cloud.visionai.v1alpha1.Warehouse.ListSearchConfigs`  
`ADMIN_WRITE` | `google.cloud.visionai.v1.AppPlatform.AddApplicationStreamInput`  
`google.cloud.visionai.v1.AppPlatform.CreateApplication`  
`google.cloud.visionai.v1.AppPlatform.CreateApplicationInstances`  
`google.cloud.visionai.v1.AppPlatform.CreateDraft`  
`google.cloud.visionai.v1.AppPlatform.CreateProcessor`  
`google.cloud.visionai.v1.AppPlatform.DeleteApplication`  
`google.cloud.visionai.v1.AppPlatform.DeleteApplicationInstances`  
`google.cloud.visionai.v1.AppPlatform.DeleteDraft`  
`google.cloud.visionai.v1.AppPlatform.DeleteProcessor`  
`google.cloud.visionai.v1.AppPlatform.DeployApplication`  
`google.cloud.visionai.v1.AppPlatform.RemoveApplicationStreamInput`  
`google.cloud.visionai.v1.AppPlatform.UndeployApplication`  
`google.cloud.visionai.v1.AppPlatform.UpdateApplication`  
`google.cloud.visionai.v1.AppPlatform.UpdateApplicationInstances`  
`google.cloud.visionai.v1.AppPlatform.UpdateDraft`  
`google.cloud.visionai.v1.AppPlatform.UpdateProcessor`  
`google.cloud.visionai.v1.LiveVideoAnalytics.CreateAnalysis`  
`google.cloud.visionai.v1.LiveVideoAnalytics.CreateOperator`  
`google.cloud.visionai.v1.LiveVideoAnalytics.CreateProcess`  
`google.cloud.visionai.v1.LiveVideoAnalytics.DeleteAnalysis`  
`google.cloud.visionai.v1.LiveVideoAnalytics.DeleteOperator`  
`google.cloud.visionai.v1.LiveVideoAnalytics.DeleteProcess`  
`google.cloud.visionai.v1.LiveVideoAnalytics.UpdateAnalysis`  
`google.cloud.visionai.v1.LiveVideoAnalytics.UpdateOperator`  
`google.cloud.visionai.v1.LiveVideoAnalytics.UpdateProcess`  
`google.cloud.visionai.v1.StreamsService.CreateCluster`  
`google.cloud.visionai.v1.StreamsService.CreateEvent`  
`google.cloud.visionai.v1.StreamsService.CreateSeries`  
`google.cloud.visionai.v1.StreamsService.CreateStream`  
`google.cloud.visionai.v1.StreamsService.DeleteCluster`  
`google.cloud.visionai.v1.StreamsService.DeleteEvent`  
`google.cloud.visionai.v1.StreamsService.DeleteSeries`  
`google.cloud.visionai.v1.StreamsService.DeleteStream`  
`google.cloud.visionai.v1.StreamsService.UpdateCluster`  
`google.cloud.visionai.v1.StreamsService.UpdateEvent`  
`google.cloud.visionai.v1.StreamsService.UpdateSeries`  
`google.cloud.visionai.v1.StreamsService.UpdateStream`  
`google.cloud.visionai.v1.Warehouse.AddCollectionItem`  
`google.cloud.visionai.v1.Warehouse.AnalyzeAsset`  
`google.cloud.visionai.v1.Warehouse.AnalyzeCorpus`  
`google.cloud.visionai.v1.Warehouse.CreateAsset`  
`google.cloud.visionai.v1.Warehouse.CreateCollection`  
`google.cloud.visionai.v1.Warehouse.CreateCorpus`  
`google.cloud.visionai.v1.Warehouse.CreateDataSchema`  
`google.cloud.visionai.v1.Warehouse.CreateIndex`  
`google.cloud.visionai.v1.Warehouse.CreateIndexEndpoint`  
`google.cloud.visionai.v1.Warehouse.CreateSearchConfig`  
`google.cloud.visionai.v1.Warehouse.CreateSearchHypernym`  
`google.cloud.visionai.v1.Warehouse.DeleteAsset`  
`google.cloud.visionai.v1.Warehouse.DeleteCollection`  
`google.cloud.visionai.v1.Warehouse.DeleteCorpus`  
`google.cloud.visionai.v1.Warehouse.DeleteDataSchema`  
`google.cloud.visionai.v1.Warehouse.DeleteIndex`  
`google.cloud.visionai.v1.Warehouse.DeleteIndexEndpoint`  
`google.cloud.visionai.v1.Warehouse.DeleteSearchConfig`  
`google.cloud.visionai.v1.Warehouse.DeleteSearchHypernym`  
`google.cloud.visionai.v1.Warehouse.DeployIndex`  
`google.cloud.visionai.v1.Warehouse.ImportAssets`  
`google.cloud.visionai.v1.Warehouse.IndexAsset`  
`google.cloud.visionai.v1.Warehouse.RemoveCollectionItem`  
`google.cloud.visionai.v1.Warehouse.RemoveIndexAsset`  
`google.cloud.visionai.v1.Warehouse.UndeployIndex`  
`google.cloud.visionai.v1.Warehouse.UpdateAsset`  
`google.cloud.visionai.v1.Warehouse.UpdateCollection`  
`google.cloud.visionai.v1.Warehouse.UpdateCorpus`  
`google.cloud.visionai.v1.Warehouse.UpdateDataSchema`  
`google.cloud.visionai.v1.Warehouse.UpdateIndex`  
`google.cloud.visionai.v1.Warehouse.UpdateIndexEndpoint`  
`google.cloud.visionai.v1.Warehouse.UpdateSearchConfig`  
`google.cloud.visionai.v1.Warehouse.UpdateSearchHypernym`  
`google.cloud.visionai.v1alpha1.AppPlatform.AddApplicationStreamInput`  
`google.cloud.visionai.v1alpha1.AppPlatform.CreateApplication`  
`google.cloud.visionai.v1alpha1.AppPlatform.CreateApplicationInstances`  
`google.cloud.visionai.v1alpha1.AppPlatform.CreateDraft`  
`google.cloud.visionai.v1alpha1.AppPlatform.CreateProcessor`  
`google.cloud.visionai.v1alpha1.AppPlatform.DeleteApplication`  
`google.cloud.visionai.v1alpha1.AppPlatform.DeleteApplicationInstances`  
`google.cloud.visionai.v1alpha1.AppPlatform.DeleteDraft`  
`google.cloud.visionai.v1alpha1.AppPlatform.DeployApplication`  
`google.cloud.visionai.v1alpha1.AppPlatform.RemoveApplicationStreamInput`  
`google.cloud.visionai.v1alpha1.AppPlatform.UndeployApplication`  
`google.cloud.visionai.v1alpha1.AppPlatform.UpdateApplication`  
`google.cloud.visionai.v1alpha1.AppPlatform.UpdateDraft`  
`google.cloud.visionai.v1alpha1.LiveVideoAnalytics.CreateAnalysis`  
`google.cloud.visionai.v1alpha1.LiveVideoAnalytics.DeleteAnalysis`  
`google.cloud.visionai.v1alpha1.StreamsService.CreateEvent`  
`google.cloud.visionai.v1alpha1.StreamsService.CreateSeries`  
`google.cloud.visionai.v1alpha1.StreamsService.CreateStream`  
`google.cloud.visionai.v1alpha1.StreamsService.DeleteCluster`  
`google.cloud.visionai.v1alpha1.StreamsService.DeleteEvent`  
`google.cloud.visionai.v1alpha1.StreamsService.DeleteSeries`  
`google.cloud.visionai.v1alpha1.StreamsService.DeleteStream`  
`google.cloud.visionai.v1alpha1.Warehouse.CreateAsset`  
`google.cloud.visionai.v1alpha1.Warehouse.CreateCorpus`  
`google.cloud.visionai.v1alpha1.Warehouse.CreateDataSchema`  
`google.cloud.visionai.v1alpha1.Warehouse.CreateSearchConfig`  
`google.cloud.visionai.v1alpha1.Warehouse.DeleteAsset`  
`google.cloud.visionai.v1alpha1.Warehouse.DeleteCorpus`  
`google.cloud.visionai.v1alpha1.Warehouse.DeleteDataSchema`  
`google.cloud.visionai.v1alpha1.Warehouse.DeleteSearchConfig`  
`google.cloud.visionai.v1alpha1.Warehouse.UpdateAsset`  
`google.cloud.visionai.v1alpha1.Warehouse.UpdateCorpus`  
`google.cloud.visionai.v1alpha1.Warehouse.UpdateDataSchema`  
`google.cloud.visionai.v1alpha1.Warehouse.UpdateSearchConfig`  
`DATA_READ` | `google.cloud.visionai.v1.StreamingService.ReceivePackets`  
`google.cloud.visionai.v1.Warehouse.ClipAsset`  
`google.cloud.visionai.v1.Warehouse.GenerateHlsUri`  
`google.cloud.visionai.v1.Warehouse.GenerateRetrievalUrl`  
`google.cloud.visionai.v1.Warehouse.GetAnnotation`  
`google.cloud.visionai.v1.Warehouse.ListAnnotations`  
`google.cloud.visionai.v1.Warehouse.SearchAssets`  
`google.cloud.visionai.v1.Warehouse.SearchIndexEndpoint`  
`google.cloud.visionai.v1alpha1.Warehouse.GetAnnotation`  
`google.cloud.visionai.v1alpha1.Warehouse.ListAnnotations`  
`google.cloud.visionai.v1alpha1.Warehouse.SearchAssets`  
`DATA_WRITE` | `google.cloud.visionai.v1.StreamingService.SendPackets`  
`google.cloud.visionai.v1.Warehouse.CreateAnnotation`  
`google.cloud.visionai.v1.Warehouse.DeleteAnnotation`  
`google.cloud.visionai.v1.Warehouse.IngestAsset`  
`google.cloud.visionai.v1.Warehouse.UpdateAnnotation`  
`google.cloud.visionai.v1.Warehouse.UploadAsset`  
`google.cloud.visionai.v1alpha1.Warehouse.CreateAnnotation`  
`google.cloud.visionai.v1alpha1.Warehouse.DeleteAnnotation`  
`google.cloud.visionai.v1alpha1.Warehouse.UpdateAnnotation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Vertex AI Vision.

### `google.cloud.visionai.v1.AppPlatform`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1.AppPlatform`.

#### `AddApplicationStreamInput`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.AddApplicationStreamInput`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.AddApplicationStreamInput" `  




#### `CreateApplication`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.CreateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.CreateApplication" `  




#### `CreateApplicationInstances`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.CreateApplicationInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.CreateApplicationInstances" `  




#### `CreateDraft`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.CreateDraft`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.drafts.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.CreateDraft" `  




#### `CreateProcessor`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.CreateProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.processors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.CreateProcessor" `  




#### `DeleteApplication`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.DeleteApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.DeleteApplication" `  




#### `DeleteApplicationInstances`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.DeleteApplicationInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.DeleteApplicationInstances" `  




#### `DeleteDraft`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.DeleteDraft`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.drafts.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.DeleteDraft" `  




#### `DeleteProcessor`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.DeleteProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.processors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.DeleteProcessor" `  




#### `DeployApplication`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.DeployApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.deploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.DeployApplication" `  




#### `GetApplication`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.GetApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.GetApplication" `  




#### `GetDraft`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.GetDraft`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.drafts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.GetDraft" `  




#### `ListApplications`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.ListApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.applications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.ListApplications" `  




#### `ListDrafts`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.ListDrafts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.drafts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.ListDrafts" `  




#### `ListInstances`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.ListInstances" `  




#### `ListPrebuiltProcessors`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.ListPrebuiltProcessors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.processors.listPrebuilt - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.ListPrebuiltProcessors" `  




#### `ListProcessors`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.ListProcessors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.processors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.ListProcessors" `  




#### `RemoveApplicationStreamInput`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.RemoveApplicationStreamInput`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.RemoveApplicationStreamInput" `  




#### `UndeployApplication`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.UndeployApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.undeploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.UndeployApplication" `  




#### `UpdateApplication`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.UpdateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.UpdateApplication" `  




#### `UpdateApplicationInstances`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.UpdateApplicationInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.UpdateApplicationInstances" `  




#### `UpdateDraft`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.UpdateDraft`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.drafts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.UpdateDraft" `  




#### `UpdateProcessor`

  * **Method** : `google.cloud.visionai.v1.AppPlatform.UpdateProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.processors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.AppPlatform.UpdateProcessor" `  




### `google.cloud.visionai.v1.LiveVideoAnalytics`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1.LiveVideoAnalytics`.

#### `CreateAnalysis`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.CreateAnalysis`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.analyses.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.CreateAnalysis" `  




#### `CreateOperator`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.CreateOperator`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.operators.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.CreateOperator" `  




#### `CreateProcess`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.CreateProcess`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.processes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.CreateProcess" `  




#### `DeleteAnalysis`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.DeleteAnalysis`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.analyses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.DeleteAnalysis" `  




#### `DeleteOperator`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.DeleteOperator`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.operators.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.DeleteOperator" `  




#### `DeleteProcess`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.DeleteProcess`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.processes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.DeleteProcess" `  




#### `ResolveOperatorInfo`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.ResolveOperatorInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.operators.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.ResolveOperatorInfo" `  




#### `UpdateAnalysis`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.UpdateAnalysis`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.analyses.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.UpdateAnalysis" `  




#### `UpdateOperator`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.UpdateOperator`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.operators.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.UpdateOperator" `  




#### `UpdateProcess`

  * **Method** : `google.cloud.visionai.v1.LiveVideoAnalytics.UpdateProcess`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.processes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.LiveVideoAnalytics.UpdateProcess" `  




### `google.cloud.visionai.v1.StreamingService`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1.StreamingService`.

#### `ReceiveEvents`

  * **Method** : `google.cloud.visionai.v1.StreamingService.ReceiveEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.googleapis.com/clusters.watch - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamingService.ReceiveEvents" `  




#### `ReceivePackets`

  * **Method** : `google.cloud.visionai.v1.StreamingService.ReceivePackets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.googleapis.com/streams.receive - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamingService.ReceivePackets" `  




#### `SendPackets`

  * **Method** : `google.cloud.visionai.v1.StreamingService.SendPackets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.googleapis.com/streams.send - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamingService.SendPackets" `  




### `google.cloud.visionai.v1.StreamsService`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1.StreamsService`.

#### `CreateCluster`

  * **Method** : `google.cloud.visionai.v1.StreamsService.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.CreateCluster" `  




#### `CreateEvent`

  * **Method** : `google.cloud.visionai.v1.StreamsService.CreateEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.events.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.CreateEvent" `  




#### `CreateSeries`

  * **Method** : `google.cloud.visionai.v1.StreamsService.CreateSeries`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.series.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.CreateSeries" `  




#### `CreateStream`

  * **Method** : `google.cloud.visionai.v1.StreamsService.CreateStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.streams.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.CreateStream" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.visionai.v1.StreamsService.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.DeleteCluster" `  




#### `DeleteEvent`

  * **Method** : `google.cloud.visionai.v1.StreamsService.DeleteEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.events.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.DeleteEvent" `  




#### `DeleteSeries`

  * **Method** : `google.cloud.visionai.v1.StreamsService.DeleteSeries`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.series.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.DeleteSeries" `  




#### `DeleteStream`

  * **Method** : `google.cloud.visionai.v1.StreamsService.DeleteStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.streams.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.DeleteStream" `  




#### `GenerateStreamHlsToken`

  * **Method** : `google.cloud.visionai.v1.StreamsService.GenerateStreamHlsToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.streams.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.GenerateStreamHlsToken" `  




#### `GetCluster`

  * **Method** : `google.cloud.visionai.v1.StreamsService.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.GetCluster" `  




#### `GetEvent`

  * **Method** : `google.cloud.visionai.v1.StreamsService.GetEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.events.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.GetEvent" `  




#### `GetSeries`

  * **Method** : `google.cloud.visionai.v1.StreamsService.GetSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.series.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.GetSeries" `  




#### `GetStream`

  * **Method** : `google.cloud.visionai.v1.StreamsService.GetStream`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.streams.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.GetStream" `  




#### `GetStreamThumbnail`

  * **Method** : `google.cloud.visionai.v1.StreamsService.GetStreamThumbnail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.streams.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.GetStreamThumbnail" `  




#### `ListClusters`

  * **Method** : `google.cloud.visionai.v1.StreamsService.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.ListClusters" `  




#### `ListSeries`

  * **Method** : `google.cloud.visionai.v1.StreamsService.ListSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.series.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.ListSeries" `  




#### `ListStreams`

  * **Method** : `google.cloud.visionai.v1.StreamsService.ListStreams`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.streams.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.ListStreams" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.visionai.v1.StreamsService.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.UpdateCluster" `  




#### `UpdateEvent`

  * **Method** : `google.cloud.visionai.v1.StreamsService.UpdateEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.events.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.UpdateEvent" `  




#### `UpdateSeries`

  * **Method** : `google.cloud.visionai.v1.StreamsService.UpdateSeries`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.series.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.UpdateSeries" `  




#### `UpdateStream`

  * **Method** : `google.cloud.visionai.v1.StreamsService.UpdateStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.streams.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.StreamsService.UpdateStream" `  




### `google.cloud.visionai.v1.Warehouse`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1.Warehouse`.

#### `AddCollectionItem`

  * **Method** : `google.cloud.visionai.v1.Warehouse.AddCollectionItem`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.collections.collect - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.AddCollectionItem" `  




#### `AnalyzeAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.AnalyzeAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.analyze - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.AnalyzeAsset" `  




#### `AnalyzeCorpus`

  * **Method** : `google.cloud.visionai.v1.Warehouse.AnalyzeCorpus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.corpora.analyze - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.AnalyzeCorpus" `  




#### `ClipAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ClipAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.clip - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ClipAsset" `  




#### `CreateAnnotation`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateAnnotation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateAnnotation" `  




#### `CreateAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateAsset" `  




#### `CreateCollection`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateCollection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.collections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateCollection" `  




#### `CreateCorpus`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateCorpus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.corpora.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateCorpus" `  




#### `CreateDataSchema`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateDataSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.dataSchemas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateDataSchema" `  




#### `CreateIndex`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateIndex`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.indexes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateIndex" `  




#### `CreateIndexEndpoint`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateIndexEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.indexEndpoints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateIndexEndpoint" `  




#### `CreateSearchConfig`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateSearchConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateSearchConfig" `  




#### `CreateSearchHypernym`

  * **Method** : `google.cloud.visionai.v1.Warehouse.CreateSearchHypernym`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchHypernyms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.CreateSearchHypernym" `  




#### `DeleteAnnotation`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteAnnotation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteAnnotation" `  




#### `DeleteAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteAsset" `  




#### `DeleteCollection`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteCollection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.collections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteCollection" `  




#### `DeleteCorpus`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteCorpus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.corpora.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteCorpus" `  




#### `DeleteDataSchema`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteDataSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.dataSchemas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteDataSchema" `  




#### `DeleteIndex`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteIndex`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.indexes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteIndex" `  




#### `DeleteIndexEndpoint`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteIndexEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.indexEndpoints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteIndexEndpoint" `  




#### `DeleteSearchConfig`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteSearchConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteSearchConfig" `  




#### `DeleteSearchHypernym`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeleteSearchHypernym`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchHypernyms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeleteSearchHypernym" `  




#### `DeployIndex`

  * **Method** : `google.cloud.visionai.v1.Warehouse.DeployIndex`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.indexEndpoints.deploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.DeployIndex" `  




#### `GenerateHlsUri`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GenerateHlsUri`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.generateHlsUri - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GenerateHlsUri" `  




#### `GenerateRetrievalUrl`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GenerateRetrievalUrl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.generateRetrievalUrl - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GenerateRetrievalUrl" `  




#### `GetAnnotation`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetAnnotation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetAnnotation" `  




#### `GetAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetAsset" `  




#### `GetCollection`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetCollection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.collections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetCollection" `  




#### `GetCorpus`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetCorpus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.corpora.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetCorpus" `  




#### `GetDataSchema`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetDataSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.dataSchemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetDataSchema" `  




#### `GetIndex`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetIndex`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.indexes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetIndex" `  




#### `GetIndexEndpoint`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetIndexEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.indexEndpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetIndexEndpoint" `  




#### `GetSearchConfig`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetSearchConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.searchConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetSearchConfig" `  




#### `GetSearchHypernym`

  * **Method** : `google.cloud.visionai.v1.Warehouse.GetSearchHypernym`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.searchHypernyms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.GetSearchHypernym" `  




#### `ImportAssets`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ImportAssets`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.corpora.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ImportAssets" `  




#### `IndexAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.IndexAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.index - ADMIN_WRITE`
    * `visionai.indexes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.IndexAsset" `  




#### `IngestAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.IngestAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.ingest - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.IngestAsset" `  




#### `ListAnnotations`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ListAnnotations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ListAnnotations" `  




#### `ListAssets`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ListAssets" `  




#### `ListCollections`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ListCollections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.collections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ListCollections" `  




#### `ListCorpora`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ListCorpora`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.corpora.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ListCorpora" `  




#### `ListDataSchemas`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ListDataSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.dataSchemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ListDataSchemas" `  




#### `ListIndexEndpoints`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ListIndexEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.indexEndpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ListIndexEndpoints" `  




#### `ListIndexes`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ListIndexes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.indexes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ListIndexes" `  




#### `ListSearchHypernyms`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ListSearchHypernyms`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.searchHypernyms.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ListSearchHypernyms" `  




#### `RemoveCollectionItem`

  * **Method** : `google.cloud.visionai.v1.Warehouse.RemoveCollectionItem`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.collections.uncollect - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.RemoveCollectionItem" `  




#### `RemoveIndexAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.RemoveIndexAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.removeIndex - ADMIN_WRITE`
    * `visionai.indexes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.RemoveIndexAsset" `  




#### `SearchAssets`

  * **Method** : `google.cloud.visionai.v1.Warehouse.SearchAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.search - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.SearchAssets" `  




#### `SearchIndexEndpoint`

  * **Method** : `google.cloud.visionai.v1.Warehouse.SearchIndexEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.indexEndpoints.search - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.SearchIndexEndpoint" `  




#### `UndeployIndex`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UndeployIndex`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.indexEndpoints.undeploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UndeployIndex" `  




#### `UpdateAnnotation`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateAnnotation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateAnnotation" `  




#### `UpdateAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateAsset" `  




#### `UpdateCollection`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateCollection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.collections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateCollection" `  




#### `UpdateCorpus`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateCorpus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.corpora.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateCorpus" `  




#### `UpdateDataSchema`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateDataSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.dataSchemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateDataSchema" `  




#### `UpdateIndex`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateIndex`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.indexes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateIndex" `  




#### `UpdateIndexEndpoint`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateIndexEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.indexEndpoints.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateIndexEndpoint" `  




#### `UpdateSearchConfig`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateSearchConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateSearchConfig" `  




#### `UpdateSearchHypernym`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UpdateSearchHypernym`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchHypernyms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UpdateSearchHypernym" `  




#### `UploadAsset`

  * **Method** : `google.cloud.visionai.v1.Warehouse.UploadAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.upload - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.UploadAsset" `  




#### `ViewCollectionItems`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ViewCollectionItems`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.collections.view - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ViewCollectionItems" `  




#### `ViewIndexedAssets`

  * **Method** : `google.cloud.visionai.v1.Warehouse.ViewIndexedAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.indexes.viewAssets - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1.Warehouse.ViewIndexedAssets" `  




### `google.cloud.visionai.v1alpha1.AppPlatform`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1alpha1.AppPlatform`.

#### `AddApplicationStreamInput`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.AddApplicationStreamInput`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.AddApplicationStreamInput" `  




#### `CreateApplication`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.CreateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.CreateApplication" `  




#### `CreateApplicationInstances`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.CreateApplicationInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.CreateApplicationInstances" `  




#### `CreateDraft`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.CreateDraft`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.drafts.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.CreateDraft" `  




#### `CreateProcessor`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.CreateProcessor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.processors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.CreateProcessor" `  




#### `DeleteApplication`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.DeleteApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.DeleteApplication" `  




#### `DeleteApplicationInstances`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.DeleteApplicationInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.DeleteApplicationInstances" `  




#### `DeleteDraft`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.DeleteDraft`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.drafts.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.DeleteDraft" `  




#### `DeployApplication`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.DeployApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.deploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.DeployApplication" `  




#### `GetApplication`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.GetApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.GetApplication" `  




#### `GetDraft`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.GetDraft`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.drafts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.GetDraft" `  




#### `GetInstance`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.GetInstance" `  




#### `ListApplications`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.ListApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.applications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.ListApplications" `  




#### `ListDrafts`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.ListDrafts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.drafts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.ListDrafts" `  




#### `ListInstances`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.ListInstances" `  




#### `ListPrebuiltProcessors`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.ListPrebuiltProcessors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.processors.listPrebuilt - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.ListPrebuiltProcessors" `  




#### `ListProcessors`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.ListProcessors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.processors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.ListProcessors" `  




#### `RemoveApplicationStreamInput`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.RemoveApplicationStreamInput`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.RemoveApplicationStreamInput" `  




#### `UndeployApplication`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.UndeployApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.undeploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.UndeployApplication" `  




#### `UpdateApplication`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.UpdateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.UpdateApplication" `  




#### `UpdateDraft`

  * **Method** : `google.cloud.visionai.v1alpha1.AppPlatform.UpdateDraft`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.drafts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.AppPlatform.UpdateDraft" `  




### `google.cloud.visionai.v1alpha1.LiveVideoAnalytics`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1alpha1.LiveVideoAnalytics`.

#### `CreateAnalysis`

  * **Method** : `google.cloud.visionai.v1alpha1.LiveVideoAnalytics.CreateAnalysis`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.analyses.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.LiveVideoAnalytics.CreateAnalysis" `  




#### `DeleteAnalysis`

  * **Method** : `google.cloud.visionai.v1alpha1.LiveVideoAnalytics.DeleteAnalysis`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.analyses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.LiveVideoAnalytics.DeleteAnalysis" `  




#### `ListAnalyses`

  * **Method** : `google.cloud.visionai.v1alpha1.LiveVideoAnalytics.ListAnalyses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.analyses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.LiveVideoAnalytics.ListAnalyses" `  




### `google.cloud.visionai.v1alpha1.StreamsService`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1alpha1.StreamsService`.

#### `CreateEvent`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.CreateEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.events.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.CreateEvent" `  




#### `CreateSeries`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.CreateSeries`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.series.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.CreateSeries" `  




#### `CreateStream`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.CreateStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.streams.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.CreateStream" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.DeleteCluster" `  




#### `DeleteEvent`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.DeleteEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.events.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.DeleteEvent" `  




#### `DeleteSeries`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.DeleteSeries`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.series.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.DeleteSeries" `  




#### `DeleteStream`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.DeleteStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.streams.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.DeleteStream" `  




#### `ListEvents`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.ListEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.events.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.ListEvents" `  




#### `ListSeries`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.ListSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.series.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.ListSeries" `  




#### `ListStreams`

  * **Method** : `google.cloud.visionai.v1alpha1.StreamsService.ListStreams`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.streams.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.StreamsService.ListStreams" `  




### `google.cloud.visionai.v1alpha1.Warehouse`

The following audit logs are associated with methods belonging to `google.cloud.visionai.v1alpha1.Warehouse`.

#### `CreateAnnotation`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.CreateAnnotation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.CreateAnnotation" `  




#### `CreateAsset`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.CreateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.CreateAsset" `  




#### `CreateCorpus`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.CreateCorpus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.corpora.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.CreateCorpus" `  




#### `CreateDataSchema`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.CreateDataSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.dataSchemas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.CreateDataSchema" `  




#### `CreateSearchConfig`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.CreateSearchConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.CreateSearchConfig" `  




#### `DeleteAnnotation`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.DeleteAnnotation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.DeleteAnnotation" `  




#### `DeleteAsset`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.DeleteAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.DeleteAsset" `  




#### `DeleteCorpus`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.DeleteCorpus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.corpora.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.DeleteCorpus" `  




#### `DeleteDataSchema`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.DeleteDataSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.dataSchemas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.DeleteDataSchema" `  




#### `DeleteSearchConfig`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.DeleteSearchConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.DeleteSearchConfig" `  




#### `GetAnnotation`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.GetAnnotation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.GetAnnotation" `  




#### `GetAsset`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.GetAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.GetAsset" `  




#### `GetCorpus`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.GetCorpus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.corpora.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.GetCorpus" `  




#### `GetDataSchema`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.GetDataSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.dataSchemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.GetDataSchema" `  




#### `GetSearchConfig`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.GetSearchConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.searchConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.GetSearchConfig" `  




#### `ListAnnotations`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.ListAnnotations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.ListAnnotations" `  




#### `ListAssets`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.ListAssets" `  




#### `ListCorpora`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.ListCorpora`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.corpora.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.ListCorpora" `  




#### `ListDataSchemas`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.ListDataSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.dataSchemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.ListDataSchemas" `  




#### `ListSearchConfigs`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.ListSearchConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.searchConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.ListSearchConfigs" `  




#### `SearchAssets`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.SearchAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.assets.search - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.SearchAssets" `  




#### `UpdateAnnotation`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.UpdateAnnotation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `visionai.annotations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.UpdateAnnotation" `  




#### `UpdateAsset`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.UpdateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.assets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.UpdateAsset" `  




#### `UpdateCorpus`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.UpdateCorpus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.corpora.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.UpdateCorpus" `  




#### `UpdateDataSchema`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.UpdateDataSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.dataSchemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.UpdateDataSchema" `  




#### `UpdateSearchConfig`

  * **Method** : `google.cloud.visionai.v1alpha1.Warehouse.UpdateSearchConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `visionai.searchConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.visionai.v1alpha1.Warehouse.UpdateSearchConfig" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
