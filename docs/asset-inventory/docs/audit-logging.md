---
url: https://docs.cloud.google.com/asset-inventory/docs/audit-logging/
title: Cloud Asset Inventory audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:05:33.041896+00:00
---

# Cloud Asset Inventory audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  Cloud Asset Inventory audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud Asset Inventory. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Asset Inventory audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudasset.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Asset Inventory generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.asset.v1.AssetService.AnalyzeIamPolicy`  
`google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning`  
`AnalyzeMove`  
`google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies`  
`google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets`  
`google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers`  
`google.cloud.asset.v1.AssetService.BatchGetAssetsHistory`  
`google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies`  
`google.cloud.asset.v1.AssetService.ExportAssets`  
`google.cloud.asset.v1.AssetService.GetFeed`  
`google.cloud.asset.v1.AssetService.GetSavedQuery`  
`google.cloud.asset.v1.AssetService.ListAssets`  
`google.cloud.asset.v1.AssetService.ListFeeds`  
`google.cloud.asset.v1.AssetService.ListSavedQueries`  
`google.cloud.asset.v1.AssetService.QueryAssets`  
`google.cloud.asset.v1.AssetService.SearchAllIamPolicies`  
`google.cloud.asset.v1.AssetService.SearchAllResources`  
`google.cloud.asset.v1beta1.AssetService.BatchGetAssetsHistory`  
`google.cloud.asset.v1beta1.AssetService.ExportAssets`  
`google.cloud.asset.v1p2beta1.AssetService.GetFeed`  
`google.cloud.asset.v1p2beta1.AssetService.ListFeeds`  
`google.cloud.asset.v1p5beta1.AssetService.ListAssets`  
`google.cloud.asset.v1p7beta1.AssetService.ExportAssets`  
`ADMIN_WRITE` | `google.cloud.asset.v1.AssetService.CreateFeed`  
`google.cloud.asset.v1.AssetService.CreateSavedQuery`  
`google.cloud.asset.v1.AssetService.DeleteFeed`  
`google.cloud.asset.v1.AssetService.DeleteSavedQuery`  
`google.cloud.asset.v1.AssetService.UpdateFeed`  
`google.cloud.asset.v1.AssetService.UpdateSavedQuery`  
`google.cloud.asset.v1p2beta1.AssetService.CreateFeed`  
`google.cloud.asset.v1p2beta1.AssetService.DeleteFeed`  
`google.cloud.asset.v1p2beta1.AssetService.UpdateFeed`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Asset Inventory.

### `google.cloud.asset.v1.AssetService`

The following audit logs are associated with methods belonging to `google.cloud.asset.v1.AssetService`.

#### `AnalyzeIamPolicy`

  * **Method** : `google.cloud.asset.v1.AssetService.AnalyzeIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.analyzeIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.AnalyzeIamPolicy" `  




#### `AnalyzeIamPolicyLongrunning`

  * **Method** : `google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.analyzeIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning" `  




#### `AnalyzeMove`

  * **Method** : `AnalyzeMove`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.analyzeMove - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="AnalyzeMove" `  




#### `AnalyzeOrgPolicies`

  * **Method** : `google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.analyzeOrgPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies" `  




#### `AnalyzeOrgPolicyGovernedAssets`

  * **Method** : `google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.analyzeOrgPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets" `  




#### `AnalyzeOrgPolicyGovernedContainers`

  * **Method** : `google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.analyzeOrgPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers" `  




#### `BatchGetAssetsHistory`

  * **Method** : `google.cloud.asset.v1.AssetService.BatchGetAssetsHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.exportResource - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.BatchGetAssetsHistory" `  




#### `BatchGetEffectiveIamPolicies`

  * **Method** : `google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.analyzeIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies" `  




#### `CreateFeed`

  * **Method** : `google.cloud.asset.v1.AssetService.CreateFeed`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.assets.exportResource - ADMIN_READ`
    * `cloudasset.feeds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.CreateFeed" `  




#### `CreateSavedQuery`

  * **Method** : `google.cloud.asset.v1.AssetService.CreateSavedQuery`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.savedqueries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.CreateSavedQuery" `  




#### `DeleteFeed`

  * **Method** : `google.cloud.asset.v1.AssetService.DeleteFeed`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.feeds.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.DeleteFeed" `  




#### `DeleteSavedQuery`

  * **Method** : `google.cloud.asset.v1.AssetService.DeleteSavedQuery`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.savedqueries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.DeleteSavedQuery" `  




#### `ExportAssets`

  * **Method** : `google.cloud.asset.v1.AssetService.ExportAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.exportAccessPolicy - ADMIN_READ`
    * `cloudasset.assets.exportIamPolicy - ADMIN_READ`
    * `cloudasset.assets.exportResource - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.ExportAssets" `  




#### `GetFeed`

  * **Method** : `google.cloud.asset.v1.AssetService.GetFeed`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.feeds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.GetFeed" `  




#### `GetSavedQuery`

  * **Method** : `google.cloud.asset.v1.AssetService.GetSavedQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.savedqueries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.GetSavedQuery" `  




#### `ListAssets`

  * **Method** : `google.cloud.asset.v1.AssetService.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.listIamPolicy - ADMIN_READ`
    * `cloudasset.assets.listResource - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.ListAssets" `  




#### `ListFeeds`

  * **Method** : `google.cloud.asset.v1.AssetService.ListFeeds`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.feeds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.ListFeeds" `  




#### `ListSavedQueries`

  * **Method** : `google.cloud.asset.v1.AssetService.ListSavedQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.savedqueries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.ListSavedQueries" `  




#### `QueryAssets`

  * **Method** : `google.cloud.asset.v1.AssetService.QueryAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.queryResource - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.QueryAssets" `  




#### `SearchAllIamPolicies`

  * **Method** : `google.cloud.asset.v1.AssetService.SearchAllIamPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.searchAllIamPolicies - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.SearchAllIamPolicies" `  




#### `SearchAllResources`

  * **Method** : `google.cloud.asset.v1.AssetService.SearchAllResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.searchAllResources - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.SearchAllResources" `  




#### `UpdateFeed`

  * **Method** : `google.cloud.asset.v1.AssetService.UpdateFeed`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.feeds.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.UpdateFeed" `  




#### `UpdateSavedQuery`

  * **Method** : `google.cloud.asset.v1.AssetService.UpdateSavedQuery`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.savedqueries.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1.AssetService.UpdateSavedQuery" `  




### `google.cloud.asset.v1beta1.AssetService`

The following audit logs are associated with methods belonging to `google.cloud.asset.v1beta1.AssetService`.

#### `BatchGetAssetsHistory`

  * **Method** : `google.cloud.asset.v1beta1.AssetService.BatchGetAssetsHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.exportAll - ADMIN_READ`
    * `cloudasset.assets.exportResource - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1beta1.AssetService.BatchGetAssetsHistory" `  




#### `ExportAssets`

  * **Method** : `google.cloud.asset.v1beta1.AssetService.ExportAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.exportAll - ADMIN_READ`
    * `cloudasset.assets.exportResource - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1beta1.AssetService.ExportAssets" `  




### `google.cloud.asset.v1p2beta1.AssetService`

The following audit logs are associated with methods belonging to `google.cloud.asset.v1p2beta1.AssetService`.

#### `CreateFeed`

  * **Method** : `google.cloud.asset.v1p2beta1.AssetService.CreateFeed`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.assets.exportResource - ADMIN_READ`
    * `cloudasset.feeds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1p2beta1.AssetService.CreateFeed" `  




#### `DeleteFeed`

  * **Method** : `google.cloud.asset.v1p2beta1.AssetService.DeleteFeed`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.feeds.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1p2beta1.AssetService.DeleteFeed" `  




#### `GetFeed`

  * **Method** : `google.cloud.asset.v1p2beta1.AssetService.GetFeed`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.feeds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1p2beta1.AssetService.GetFeed" `  




#### `ListFeeds`

  * **Method** : `google.cloud.asset.v1p2beta1.AssetService.ListFeeds`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.feeds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1p2beta1.AssetService.ListFeeds" `  




#### `UpdateFeed`

  * **Method** : `google.cloud.asset.v1p2beta1.AssetService.UpdateFeed`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudasset.feeds.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1p2beta1.AssetService.UpdateFeed" `  




### `google.cloud.asset.v1p5beta1.AssetService`

The following audit logs are associated with methods belonging to `google.cloud.asset.v1p5beta1.AssetService`.

#### `ListAssets`

  * **Method** : `google.cloud.asset.v1p5beta1.AssetService.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.listResource - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1p5beta1.AssetService.ListAssets" `  




### `google.cloud.asset.v1p7beta1.AssetService`

The following audit logs are associated with methods belonging to `google.cloud.asset.v1p7beta1.AssetService`.

#### `ExportAssets`

  * **Method** : `google.cloud.asset.v1p7beta1.AssetService.ExportAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudasset.assets.exportDiscoveryengineCollections - ADMIN_READ`
    * `cloudasset.assets.exportIamPolicy - ADMIN_READ`
    * `cloudasset.assets.exportResource - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.asset.v1p7beta1.AssetService.ExportAssets" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.longrunning.Operations.GetOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
