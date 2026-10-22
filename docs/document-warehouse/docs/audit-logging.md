---
url: https://docs.cloud.google.com/document-warehouse/docs/audit-logging/
title: Document AI Warehouse audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:48.902314+00:00
---

# Document AI Warehouse audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/document-warehouse/docs/overview)



Send feedback 

#  Document AI Warehouse audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Document AI Warehouse. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Document AI Warehouse audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="contentwarehouse.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Document AI Warehouse generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.contentwarehouse.v1.DocumentSchemaService.GetDocumentSchema`  
`google.cloud.contentwarehouse.v1.DocumentSchemaService.ListDocumentSchemas`  
`google.cloud.contentwarehouse.v1.DocumentService.FetchAcl`  
`google.cloud.contentwarehouse.v1.ProjectService.GetProjectStatus`  
`google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.GetDocumentSchema`  
`google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.ListDocumentSchemas`  
`google.cloud.contentwarehouse.v1beta1.DocumentService.FetchAcl`  
`google.longrunning.Operations.GetOperation`  
`ADMIN_WRITE` | `google.cloud.contentwarehouse.v1.DocumentSchemaService.CreateDocumentSchema`  
`google.cloud.contentwarehouse.v1.DocumentSchemaService.DeleteDocumentSchema`  
`google.cloud.contentwarehouse.v1.DocumentSchemaService.UpdateDocumentSchema`  
`google.cloud.contentwarehouse.v1.DocumentService.SetAcl`  
`google.cloud.contentwarehouse.v1.ProjectService.InitializeProject` (LRO)  
`google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.CreateDocumentSchema`  
`google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.DeleteDocumentSchema`  
`google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.UpdateDocumentSchema`  
`google.cloud.contentwarehouse.v1beta1.DocumentService.SetAcl`  
`google.cloud.contentwarehouse.v1beta1.ProjectService.InitializeProject` (LRO)  
`DATA_READ` | `google.cloud.contentwarehouse.v1.DocumentLinkService.ListLinkedSources`  
`google.cloud.contentwarehouse.v1.DocumentLinkService.ListLinkedTargets`  
`google.cloud.contentwarehouse.v1.DocumentService.GetDocument`  
`google.cloud.contentwarehouse.v1.DocumentService.SearchDocuments`  
`google.cloud.contentwarehouse.v1.RuleSetService.GetRuleSet`  
`google.cloud.contentwarehouse.v1.RuleSetService.ListRuleSets`  
`google.cloud.contentwarehouse.v1.SynonymSetService.GetSynonymSet`  
`google.cloud.contentwarehouse.v1.SynonymSetService.ListSynonymSets`  
`google.cloud.contentwarehouse.v1beta1.DocumentLinkService.ListLinkedSources`  
`google.cloud.contentwarehouse.v1beta1.DocumentLinkService.ListLinkedTargets`  
`google.cloud.contentwarehouse.v1beta1.DocumentService.GetDocument`  
`google.cloud.contentwarehouse.v1beta1.DocumentService.SearchDocuments`  
`google.cloud.contentwarehouse.v1beta1.RuleSetService.GetRuleSet`  
`google.cloud.contentwarehouse.v1beta1.RuleSetService.ListRuleSets`  
`google.cloud.contentwarehouse.v1beta1.SynonymSetService.GetSynonymSet`  
`google.cloud.contentwarehouse.v1beta1.SynonymSetService.ListSynonymSets`  
`gview.DocumentProviderService.GetDocument`  
`DATA_WRITE` | `google.cloud.contentwarehouse.v1.DocumentLinkService.CreateDocumentLink`  
`google.cloud.contentwarehouse.v1.DocumentLinkService.DeleteDocumentLink`  
`google.cloud.contentwarehouse.v1.DocumentService.CreateDocument`  
`google.cloud.contentwarehouse.v1.DocumentService.DeleteDocument`  
`google.cloud.contentwarehouse.v1.DocumentService.LockDocument`  
`google.cloud.contentwarehouse.v1.DocumentService.UpdateDocument`  
`google.cloud.contentwarehouse.v1.RuleSetService.CreateRuleSet`  
`google.cloud.contentwarehouse.v1.RuleSetService.DeleteRuleSet`  
`google.cloud.contentwarehouse.v1.RuleSetService.UpdateRuleSet`  
`google.cloud.contentwarehouse.v1.SynonymSetService.CreateSynonymSet`  
`google.cloud.contentwarehouse.v1.SynonymSetService.DeleteSynonymSet`  
`google.cloud.contentwarehouse.v1.SynonymSetService.UpdateSynonymSet`  
`google.cloud.contentwarehouse.v1beta1.DocumentLinkService.CreateDocumentLink`  
`google.cloud.contentwarehouse.v1beta1.DocumentLinkService.DeleteDocumentLink`  
`google.cloud.contentwarehouse.v1beta1.DocumentService.CreateDocument`  
`google.cloud.contentwarehouse.v1beta1.DocumentService.DeleteDocument`  
`google.cloud.contentwarehouse.v1beta1.DocumentService.UpdateDocument`  
`google.cloud.contentwarehouse.v1beta1.RuleSetService.CreateRuleSet`  
`google.cloud.contentwarehouse.v1beta1.RuleSetService.DeleteRuleSet`  
`google.cloud.contentwarehouse.v1beta1.RuleSetService.UpdateRuleSet`  
`google.cloud.contentwarehouse.v1beta1.SynonymSetService.CreateSynonymSet`  
`google.cloud.contentwarehouse.v1beta1.SynonymSetService.DeleteSynonymSet`  
`google.cloud.contentwarehouse.v1beta1.SynonymSetService.UpdateSynonymSet`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Document AI Warehouse.

### `google.cloud.contentwarehouse.v1.DocumentLinkService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1.DocumentLinkService`.

#### `CreateDocumentLink`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentLinkService.CreateDocumentLink`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentLinkService.CreateDocumentLink" `  




#### `DeleteDocumentLink`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentLinkService.DeleteDocumentLink`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentLinkService.DeleteDocumentLink" `  




#### `ListLinkedSources`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentLinkService.ListLinkedSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentLinkService.ListLinkedSources" `  




#### `ListLinkedTargets`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentLinkService.ListLinkedTargets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentLinkService.ListLinkedTargets" `  




### `google.cloud.contentwarehouse.v1.DocumentSchemaService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1.DocumentSchemaService`.

#### `CreateDocumentSchema`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentSchemaService.CreateDocumentSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentSchemaService.CreateDocumentSchema" `  




#### `DeleteDocumentSchema`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentSchemaService.DeleteDocumentSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentSchemaService.DeleteDocumentSchema" `  




#### `GetDocumentSchema`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentSchemaService.GetDocumentSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentSchemaService.GetDocumentSchema" `  




#### `ListDocumentSchemas`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentSchemaService.ListDocumentSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentSchemaService.ListDocumentSchemas" `  




#### `UpdateDocumentSchema`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentSchemaService.UpdateDocumentSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentSchemaService.UpdateDocumentSchema" `  




### `google.cloud.contentwarehouse.v1.DocumentService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1.DocumentService`.

#### `CreateDocument`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentService.CreateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentService.CreateDocument" `  




#### `DeleteDocument`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentService.DeleteDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentService.DeleteDocument" `  




#### `FetchAcl`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentService.FetchAcl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentService.FetchAcl" `  




#### `GetDocument`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentService.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentService.GetDocument" `  




#### `LockDocument`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentService.LockDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentService.LockDocument" `  




#### `SearchDocuments`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentService.SearchDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentService.SearchDocuments" `  




#### `SetAcl`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentService.SetAcl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.documents.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentService.SetAcl" `  




#### `UpdateDocument`

  * **Method** : `google.cloud.contentwarehouse.v1.DocumentService.UpdateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.DocumentService.UpdateDocument" `  




### `google.cloud.contentwarehouse.v1.PipelineService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1.PipelineService`.

#### `RunPipeline`

  * **Method** : `google.cloud.contentwarehouse.v1.PipelineService.RunPipeline`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.PipelineService.RunPipeline" `  




### `google.cloud.contentwarehouse.v1.ProjectService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1.ProjectService`.

#### `GetProjectStatus`

  * **Method** : `google.cloud.contentwarehouse.v1.ProjectService.GetProjectStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.locations.getStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.ProjectService.GetProjectStatus" `  




#### `InitializeProject`

  * **Method** : `google.cloud.contentwarehouse.v1.ProjectService.InitializeProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.locations.initialize - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.ProjectService.InitializeProject" `  




### `google.cloud.contentwarehouse.v1.RuleSetService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1.RuleSetService`.

#### `CreateRuleSet`

  * **Method** : `google.cloud.contentwarehouse.v1.RuleSetService.CreateRuleSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.RuleSetService.CreateRuleSet" `  




#### `DeleteRuleSet`

  * **Method** : `google.cloud.contentwarehouse.v1.RuleSetService.DeleteRuleSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.RuleSetService.DeleteRuleSet" `  




#### `GetRuleSet`

  * **Method** : `google.cloud.contentwarehouse.v1.RuleSetService.GetRuleSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.RuleSetService.GetRuleSet" `  




#### `ListRuleSets`

  * **Method** : `google.cloud.contentwarehouse.v1.RuleSetService.ListRuleSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.RuleSetService.ListRuleSets" `  




#### `UpdateRuleSet`

  * **Method** : `google.cloud.contentwarehouse.v1.RuleSetService.UpdateRuleSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.RuleSetService.UpdateRuleSet" `  




### `google.cloud.contentwarehouse.v1.SynonymSetService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1.SynonymSetService`.

#### `CreateSynonymSet`

  * **Method** : `google.cloud.contentwarehouse.v1.SynonymSetService.CreateSynonymSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.SynonymSetService.CreateSynonymSet" `  




#### `DeleteSynonymSet`

  * **Method** : `google.cloud.contentwarehouse.v1.SynonymSetService.DeleteSynonymSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.SynonymSetService.DeleteSynonymSet" `  




#### `GetSynonymSet`

  * **Method** : `google.cloud.contentwarehouse.v1.SynonymSetService.GetSynonymSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.SynonymSetService.GetSynonymSet" `  




#### `ListSynonymSets`

  * **Method** : `google.cloud.contentwarehouse.v1.SynonymSetService.ListSynonymSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.SynonymSetService.ListSynonymSets" `  




#### `UpdateSynonymSet`

  * **Method** : `google.cloud.contentwarehouse.v1.SynonymSetService.UpdateSynonymSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1.SynonymSetService.UpdateSynonymSet" `  




### `google.cloud.contentwarehouse.v1beta1.DocumentLinkService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1beta1.DocumentLinkService`.

#### `CreateDocumentLink`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentLinkService.CreateDocumentLink`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentLinkService.CreateDocumentLink" `  




#### `DeleteDocumentLink`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentLinkService.DeleteDocumentLink`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentLinkService.DeleteDocumentLink" `  




#### `ListLinkedSources`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentLinkService.ListLinkedSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentLinkService.ListLinkedSources" `  




#### `ListLinkedTargets`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentLinkService.ListLinkedTargets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentLinkService.ListLinkedTargets" `  




### `google.cloud.contentwarehouse.v1beta1.DocumentSchemaService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1beta1.DocumentSchemaService`.

#### `CreateDocumentSchema`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.CreateDocumentSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.CreateDocumentSchema" `  




#### `DeleteDocumentSchema`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.DeleteDocumentSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.DeleteDocumentSchema" `  




#### `GetDocumentSchema`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.GetDocumentSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.GetDocumentSchema" `  




#### `ListDocumentSchemas`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.ListDocumentSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.ListDocumentSchemas" `  




#### `UpdateDocumentSchema`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.UpdateDocumentSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.documentSchemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentSchemaService.UpdateDocumentSchema" `  




### `google.cloud.contentwarehouse.v1beta1.DocumentService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1beta1.DocumentService`.

#### `CreateDocument`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentService.CreateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentService.CreateDocument" `  




#### `DeleteDocument`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentService.DeleteDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentService.DeleteDocument" `  




#### `FetchAcl`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentService.FetchAcl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentService.FetchAcl" `  




#### `GetDocument`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentService.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentService.GetDocument" `  




#### `SearchDocuments`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentService.SearchDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentService.SearchDocuments" `  




#### `SetAcl`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentService.SetAcl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.documents.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentService.SetAcl" `  




#### `UpdateDocument`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.DocumentService.UpdateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.DocumentService.UpdateDocument" `  




### `google.cloud.contentwarehouse.v1beta1.ProjectService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1beta1.ProjectService`.

#### `InitializeProject`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.ProjectService.InitializeProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contentwarehouse.locations.initialize - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.ProjectService.InitializeProject" `  




### `google.cloud.contentwarehouse.v1beta1.RuleSetService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1beta1.RuleSetService`.

#### `CreateRuleSet`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.RuleSetService.CreateRuleSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.RuleSetService.CreateRuleSet" `  




#### `DeleteRuleSet`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.RuleSetService.DeleteRuleSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.RuleSetService.DeleteRuleSet" `  




#### `GetRuleSet`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.RuleSetService.GetRuleSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.RuleSetService.GetRuleSet" `  




#### `ListRuleSets`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.RuleSetService.ListRuleSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.RuleSetService.ListRuleSets" `  




#### `UpdateRuleSet`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.RuleSetService.UpdateRuleSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.ruleSets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.RuleSetService.UpdateRuleSet" `  




### `google.cloud.contentwarehouse.v1beta1.SynonymSetService`

The following audit logs are associated with methods belonging to `google.cloud.contentwarehouse.v1beta1.SynonymSetService`.

#### `CreateSynonymSet`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.SynonymSetService.CreateSynonymSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.SynonymSetService.CreateSynonymSet" `  




#### `DeleteSynonymSet`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.SynonymSetService.DeleteSynonymSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.SynonymSetService.DeleteSynonymSet" `  




#### `GetSynonymSet`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.SynonymSetService.GetSynonymSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.SynonymSetService.GetSynonymSet" `  




#### `ListSynonymSets`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.SynonymSetService.ListSynonymSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.SynonymSetService.ListSynonymSets" `  




#### `UpdateSynonymSet`

  * **Method** : `google.cloud.contentwarehouse.v1beta1.SynonymSetService.UpdateSynonymSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.synonymSets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contentwarehouse.v1beta1.SynonymSetService.UpdateSynonymSet" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




### `gview.DocumentProviderService`

The following audit logs are associated with methods belonging to `gview.DocumentProviderService`.

#### `GetDocument`

  * **Method** : `gview.DocumentProviderService.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contentwarehouse.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="gview.DocumentProviderService.GetDocument" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
