---
url: https://docs.cloud.google.com/application-design-center/docs/audit-logging/
title: App Design Center audit logging \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:31.170259+00:00
---

# App Design Center audit logging  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  App Design Center audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Design Center. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Design Center audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="designcenter.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Design Center generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.designcenter.v1.DesignCenter.ExportApplicationTemplateRevisionIaC` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.FetchApplicationAssessmentReport`  
`google.cloud.designcenter.v1.DesignCenter.FetchFrameworks`  
`google.cloud.designcenter.v1.DesignCenter.GenerateApplicationAssessmentReport` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.GenerateApplicationIaC`  
`google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateAssessmentReport` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateIaC`  
`google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateRevisionIaC`  
`google.cloud.designcenter.v1.DesignCenter.GenerateAssessmentReport` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.GenerateTerraformPlanAssessmentReport` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.GetApplication`  
`google.cloud.designcenter.v1.DesignCenter.GetApplicationTemplate`  
`google.cloud.designcenter.v1.DesignCenter.GetApplicationTemplateRevision`  
`google.cloud.designcenter.v1.DesignCenter.GetCatalog`  
`google.cloud.designcenter.v1.DesignCenter.GetCatalogTemplate`  
`google.cloud.designcenter.v1.DesignCenter.GetCatalogTemplateRevision`  
`google.cloud.designcenter.v1.DesignCenter.GetComponent`  
`google.cloud.designcenter.v1.DesignCenter.GetConnection`  
`google.cloud.designcenter.v1.DesignCenter.GetPolicy`  
`google.cloud.designcenter.v1.DesignCenter.GetShare`  
`google.cloud.designcenter.v1.DesignCenter.GetSharedTemplate`  
`google.cloud.designcenter.v1.DesignCenter.GetSharedTemplateRevision`  
`google.cloud.designcenter.v1.DesignCenter.GetSpace`  
`google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplateRevisions`  
`google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplateSystemRevisions`  
`google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplates`  
`google.cloud.designcenter.v1.DesignCenter.ListApplications`  
`google.cloud.designcenter.v1.DesignCenter.ListCatalogTemplateRevisions`  
`google.cloud.designcenter.v1.DesignCenter.ListCatalogTemplates`  
`google.cloud.designcenter.v1.DesignCenter.ListCatalogs`  
`google.cloud.designcenter.v1.DesignCenter.ListComponents`  
`google.cloud.designcenter.v1.DesignCenter.ListConnections`  
`google.cloud.designcenter.v1.DesignCenter.ListPolicies`  
`google.cloud.designcenter.v1.DesignCenter.ListSharedTemplateRevisions`  
`google.cloud.designcenter.v1.DesignCenter.ListSharedTemplates`  
`google.cloud.designcenter.v1.DesignCenter.ListShares`  
`google.cloud.designcenter.v1.DesignCenter.ListSpaces`  
`google.cloud.designcenter.v1.DesignCenter.RecommendIAMRoles` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.RegisterAppHubApplicationResources` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.SyncShare` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.ExportApplicationTemplateRevisionIaC` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.FetchApplicationAssessmentReport`  
`google.cloud.designcenter.v1alpha.DesignCenter.FetchFrameworks`  
`google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationAssessmentReport` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationIaC`  
`google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateAssessmentReport` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateIaC`  
`google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateRevisionIaC`  
`google.cloud.designcenter.v1alpha.DesignCenter.GenerateAssessmentReport` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.GenerateTerraformPlanAssessmentReport` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.GetApplication`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetApplicationTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetApplicationTemplateRevision`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetCatalog`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetCatalogTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetCatalogTemplateRevision`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetComponent`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetConnection`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetPolicy`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetShare`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetSharedTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetSharedTemplateRevision`  
`google.cloud.designcenter.v1alpha.DesignCenter.GetSpace`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplateRevisions`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplateSystemRevisions`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplates`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListApplications`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogTemplateRevisions`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogTemplates`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogs`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListComponents`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListConnections`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListPolicies`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListSharedTemplateRevisions`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListSharedTemplates`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListShares`  
`google.cloud.designcenter.v1alpha.DesignCenter.ListSpaces`  
`google.cloud.designcenter.v1alpha.DesignCenter.RecommendIAMRoles` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.RegisterAppHubApplicationResources` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.RegisterDeployedResources` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.SyncShare` (LRO)  
`ADMIN_WRITE` | `google.cloud.designcenter.v1.DesignCenter.CommitApplicationTemplate`  
`google.cloud.designcenter.v1.DesignCenter.CreateApplication`  
`google.cloud.designcenter.v1.DesignCenter.CreateApplicationTemplate`  
`google.cloud.designcenter.v1.DesignCenter.CreateCatalog`  
`google.cloud.designcenter.v1.DesignCenter.CreateCatalogTemplate`  
`google.cloud.designcenter.v1.DesignCenter.CreateCatalogTemplateRevision` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.CreateComponent`  
`google.cloud.designcenter.v1.DesignCenter.CreateConnection`  
`google.cloud.designcenter.v1.DesignCenter.CreatePolicy`  
`google.cloud.designcenter.v1.DesignCenter.CreateSpace`  
`google.cloud.designcenter.v1.DesignCenter.DeleteApplication` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.DeleteApplicationTemplate`  
`google.cloud.designcenter.v1.DesignCenter.DeleteApplicationTemplateRevision`  
`google.cloud.designcenter.v1.DesignCenter.DeleteCatalog` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.DeleteCatalogTemplate` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.DeleteCatalogTemplateRevision` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.DeleteComponent`  
`google.cloud.designcenter.v1.DesignCenter.DeleteConnection`  
`google.cloud.designcenter.v1.DesignCenter.DeletePolicy`  
`google.cloud.designcenter.v1.DesignCenter.DeleteSpace`  
`google.cloud.designcenter.v1.DesignCenter.DeployApplication` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.ExportApplicationTemplateIaC` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.ImportApplicationIaC`  
`google.cloud.designcenter.v1.DesignCenter.ImportApplicationTemplate`  
`google.cloud.designcenter.v1.DesignCenter.ImportApplicationTemplateIaC`  
`google.cloud.designcenter.v1.DesignCenter.PreviewApplication` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.SnapshotApplicationTemplate` (LRO)  
`google.cloud.designcenter.v1.DesignCenter.UpdateApplication`  
`google.cloud.designcenter.v1.DesignCenter.UpdateApplicationTemplate`  
`google.cloud.designcenter.v1.DesignCenter.UpdateCatalog`  
`google.cloud.designcenter.v1.DesignCenter.UpdateCatalogTemplate`  
`google.cloud.designcenter.v1.DesignCenter.UpdateComponent`  
`google.cloud.designcenter.v1.DesignCenter.UpdateConnection`  
`google.cloud.designcenter.v1.DesignCenter.UpdatePolicy`  
`google.cloud.designcenter.v1.DesignCenter.UpdateSpace`  
`google.cloud.designcenter.v1alpha.DesignCenter.CommitApplicationTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.CreateApplication`  
`google.cloud.designcenter.v1alpha.DesignCenter.CreateApplicationTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalog`  
`google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalogTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalogTemplateRevision` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.CreateComponent`  
`google.cloud.designcenter.v1alpha.DesignCenter.CreateConnection`  
`google.cloud.designcenter.v1alpha.DesignCenter.CreatePolicy`  
`google.cloud.designcenter.v1alpha.DesignCenter.CreateSpace`  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplication` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplicationTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplicationTemplateRevision`  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalog` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalogTemplate` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalogTemplateRevision` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteComponent`  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteConnection`  
`google.cloud.designcenter.v1alpha.DesignCenter.DeletePolicy`  
`google.cloud.designcenter.v1alpha.DesignCenter.DeleteSpace`  
`google.cloud.designcenter.v1alpha.DesignCenter.DeployApplication` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.ExportApplicationTemplateIaC` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationIaC`  
`google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationTemplateIaC`  
`google.cloud.designcenter.v1alpha.DesignCenter.InferConnections` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.PreviewApplication` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.RegisterDeployedApplication` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.SnapshotApplicationTemplate` (LRO)  
`google.cloud.designcenter.v1alpha.DesignCenter.UpdateApplication`  
`google.cloud.designcenter.v1alpha.DesignCenter.UpdateApplicationTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.UpdateCatalog`  
`google.cloud.designcenter.v1alpha.DesignCenter.UpdateCatalogTemplate`  
`google.cloud.designcenter.v1alpha.DesignCenter.UpdateComponent`  
`google.cloud.designcenter.v1alpha.DesignCenter.UpdateConnection`  
`google.cloud.designcenter.v1alpha.DesignCenter.UpdatePolicy`  
`google.cloud.designcenter.v1alpha.DesignCenter.UpdateSpace`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Design Center.

### `google.cloud.designcenter.v1.DesignCenter`

The following audit logs are associated with methods belonging to `google.cloud.designcenter.v1.DesignCenter`.

#### `CommitApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CommitApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CommitApplicationTemplate" `  




#### `CreateApplication`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateApplication" `  




#### `CreateApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateApplicationTemplate" `  




#### `CreateCatalog`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateCatalog`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateCatalog" `  




#### `CreateCatalogTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateCatalogTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateCatalogTemplate" `  




#### `CreateCatalogTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateCatalogTemplateRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplateRevisions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateCatalogTemplateRevision" `  




#### `CreateComponent`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateComponent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.components.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateComponent" `  




#### `CreateConnection`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.connections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateConnection" `  




#### `CreatePolicy`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.policies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreatePolicy" `  




#### `CreateShare`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateShare`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateShare" `  




#### `CreateSpace`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.CreateSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.spaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.CreateSpace" `  




#### `DeleteApplication`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteApplication" `  




#### `DeleteApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteApplicationTemplate" `  




#### `DeleteApplicationTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteApplicationTemplateRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteApplicationTemplateRevision" `  




#### `DeleteCatalog`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteCatalog`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteCatalog" `  




#### `DeleteCatalogTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteCatalogTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteCatalogTemplate" `  




#### `DeleteCatalogTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteCatalogTemplateRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplateRevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteCatalogTemplateRevision" `  




#### `DeleteComponent`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteComponent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.components.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteComponent" `  




#### `DeleteConnection`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.connections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteConnection" `  




#### `DeletePolicy`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeletePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.policies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeletePolicy" `  




#### `DeleteShare`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteShare" `  




#### `DeleteSpace`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeleteSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.spaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeleteSpace" `  




#### `DeployApplication`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.DeployApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.DeployApplication" `  




#### `ExportApplicationTemplateIaC`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ExportApplicationTemplateIaC`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ExportApplicationTemplateIaC" `  




#### `ExportApplicationTemplateRevisionIaC`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ExportApplicationTemplateRevisionIaC`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ExportApplicationTemplateRevisionIaC" `  




#### `FetchApplicationAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.FetchApplicationAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.FetchApplicationAssessmentReport" `  




#### `FetchFrameworks`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.FetchFrameworks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.locations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.FetchFrameworks" `  




#### `GenerateApplicationAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GenerateApplicationAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.generateAssessment - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GenerateApplicationAssessmentReport" `  




#### `GenerateApplicationIaC`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GenerateApplicationIaC`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GenerateApplicationIaC" `  




#### `GenerateApplicationTemplateAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.generateAssessment - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateAssessmentReport" `  




#### `GenerateApplicationTemplateIaC`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateIaC`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateIaC" `  




#### `GenerateApplicationTemplateRevisionIaC`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateRevisionIaC`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GenerateApplicationTemplateRevisionIaC" `  




#### `GenerateAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GenerateAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.generateAssessment - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GenerateAssessmentReport" `  




#### `GenerateTerraformPlanAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GenerateTerraformPlanAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.generateAssessment - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GenerateTerraformPlanAssessmentReport" `  




#### `GetApplication`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetApplication" `  




#### `GetApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetApplicationTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetApplicationTemplate" `  




#### `GetApplicationTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetApplicationTemplateRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetApplicationTemplateRevision" `  




#### `GetCatalog`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetCatalog`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetCatalog" `  




#### `GetCatalogTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetCatalogTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetCatalogTemplate" `  




#### `GetCatalogTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetCatalogTemplateRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetCatalogTemplateRevision" `  




#### `GetComponent`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetComponent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.components.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetComponent" `  




#### `GetConnection`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.connections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetConnection" `  




#### `GetPolicy`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.policies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetPolicy" `  




#### `GetShare`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.shares.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetShare" `  




#### `GetSharedTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetSharedTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.sharedTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetSharedTemplate" `  




#### `GetSharedTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetSharedTemplateRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.sharedTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetSharedTemplateRevision" `  




#### `GetSpace`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.GetSpace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.GetSpace" `  




#### `ImportApplicationIaC`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ImportApplicationIaC`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ImportApplicationIaC" `  




#### `ImportApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ImportApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ImportApplicationTemplate" `  




#### `ImportApplicationTemplateIaC`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ImportApplicationTemplateIaC`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ImportApplicationTemplateIaC" `  




#### `ListApplicationTemplateRevisions`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplateRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplateRevisions" `  




#### `ListApplicationTemplateSystemRevisions`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplateSystemRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplateSystemRevisions" `  




#### `ListApplicationTemplates`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListApplicationTemplates" `  




#### `ListApplications`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListApplications" `  




#### `ListCatalogTemplateRevisions`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListCatalogTemplateRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogTemplateRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListCatalogTemplateRevisions" `  




#### `ListCatalogTemplates`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListCatalogTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListCatalogTemplates" `  




#### `ListCatalogs`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListCatalogs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListCatalogs" `  




#### `ListComponents`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListComponents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.components.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListComponents" `  




#### `ListConnections`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.connections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListConnections" `  




#### `ListPolicies`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.policies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListPolicies" `  




#### `ListSharedTemplateRevisions`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListSharedTemplateRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.sharedTemplateRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListSharedTemplateRevisions" `  




#### `ListSharedTemplates`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListSharedTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.sharedTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListSharedTemplates" `  




#### `ListShares`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListShares`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.shares.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListShares" `  




#### `ListSpaces`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.ListSpaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.ListSpaces" `  




#### `PreviewApplication`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.PreviewApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.PreviewApplication" `  




#### `RecommendIAMRoles`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.RecommendIAMRoles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.RecommendIAMRoles" `  




#### `RegisterAppHubApplicationResources`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.RegisterAppHubApplicationResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.locations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.RegisterAppHubApplicationResources" `  




#### `SnapshotApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.SnapshotApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.SnapshotApplicationTemplate" `  




#### `SyncShare`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.SyncShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.shares.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.SyncShare" `  




#### `UpdateApplication`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.UpdateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.UpdateApplication" `  




#### `UpdateApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.UpdateApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.UpdateApplicationTemplate" `  




#### `UpdateCatalog`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.UpdateCatalog`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.UpdateCatalog" `  




#### `UpdateCatalogTemplate`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.UpdateCatalogTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.UpdateCatalogTemplate" `  




#### `UpdateComponent`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.UpdateComponent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.components.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.UpdateComponent" `  




#### `UpdateConnection`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.UpdateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.connections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.UpdateConnection" `  




#### `UpdatePolicy`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.UpdatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.UpdatePolicy" `  




#### `UpdateSpace`

  * **Method** : `google.cloud.designcenter.v1.DesignCenter.UpdateSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.spaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1.DesignCenter.UpdateSpace" `  




### `google.cloud.designcenter.v1alpha.DesignCenter`

The following audit logs are associated with methods belonging to `google.cloud.designcenter.v1alpha.DesignCenter`.

#### `CommitApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CommitApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CommitApplicationTemplate" `  




#### `CreateApplication`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateApplication" `  




#### `CreateApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateApplicationTemplate" `  




#### `CreateCatalog`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalog`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalog" `  




#### `CreateCatalogTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalogTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalogTemplate" `  




#### `CreateCatalogTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalogTemplateRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplateRevisions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateCatalogTemplateRevision" `  




#### `CreateComponent`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateComponent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.components.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateComponent" `  




#### `CreateConnection`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.connections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateConnection" `  




#### `CreatePolicy`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.policies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreatePolicy" `  




#### `CreateShare`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateShare`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateShare" `  




#### `CreateSpace`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.CreateSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.spaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.CreateSpace" `  




#### `DeleteApplication`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplication" `  




#### `DeleteApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplicationTemplate" `  




#### `DeleteApplicationTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplicationTemplateRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteApplicationTemplateRevision" `  




#### `DeleteCatalog`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalog`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalog" `  




#### `DeleteCatalogTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalogTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalogTemplate" `  




#### `DeleteCatalogTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalogTemplateRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplateRevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteCatalogTemplateRevision" `  




#### `DeleteComponent`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteComponent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.components.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteComponent" `  




#### `DeleteConnection`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.connections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteConnection" `  




#### `DeletePolicy`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeletePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.policies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeletePolicy" `  




#### `DeleteShare`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteShare" `  




#### `DeleteSpace`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeleteSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.spaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeleteSpace" `  




#### `DeployApplication`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.DeployApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.DeployApplication" `  




#### `ExportApplicationTemplateIaC`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ExportApplicationTemplateIaC`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ExportApplicationTemplateIaC" `  




#### `ExportApplicationTemplateRevisionIaC`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ExportApplicationTemplateRevisionIaC`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ExportApplicationTemplateRevisionIaC" `  




#### `FetchApplicationAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.FetchApplicationAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.FetchApplicationAssessmentReport" `  




#### `FetchFrameworks`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.FetchFrameworks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.locations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.FetchFrameworks" `  




#### `GenerateApplicationAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.generateAssessment - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationAssessmentReport" `  




#### `GenerateApplicationIaC`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationIaC`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationIaC" `  




#### `GenerateApplicationTemplateAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.generateAssessment - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateAssessmentReport" `  




#### `GenerateApplicationTemplateIaC`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateIaC`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateIaC" `  




#### `GenerateApplicationTemplateRevisionIaC`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateRevisionIaC`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GenerateApplicationTemplateRevisionIaC" `  




#### `GenerateAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GenerateAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.generateAssessment - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GenerateAssessmentReport" `  




#### `GenerateTerraformPlanAssessmentReport`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GenerateTerraformPlanAssessmentReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.generateAssessment - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GenerateTerraformPlanAssessmentReport" `  




#### `GetApplication`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetApplication" `  




#### `GetApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetApplicationTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetApplicationTemplate" `  




#### `GetApplicationTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetApplicationTemplateRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetApplicationTemplateRevision" `  




#### `GetCatalog`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetCatalog`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetCatalog" `  




#### `GetCatalogTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetCatalogTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetCatalogTemplate" `  




#### `GetCatalogTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetCatalogTemplateRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetCatalogTemplateRevision" `  




#### `GetComponent`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetComponent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.components.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetComponent" `  




#### `GetConnection`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.connections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetConnection" `  




#### `GetPolicy`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.policies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetPolicy" `  




#### `GetShare`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.shares.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetShare" `  




#### `GetSharedTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetSharedTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.sharedTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetSharedTemplate" `  




#### `GetSharedTemplateRevision`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetSharedTemplateRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.sharedTemplateRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetSharedTemplateRevision" `  




#### `GetSpace`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.GetSpace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.GetSpace" `  




#### `ImportApplicationIaC`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationIaC`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationIaC" `  




#### `ImportApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationTemplate" `  




#### `ImportApplicationTemplateIaC`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationTemplateIaC`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ImportApplicationTemplateIaC" `  




#### `InferConnections`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.InferConnections`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.InferConnections" `  




#### `ListApplicationTemplateRevisions`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplateRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplateRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplateRevisions" `  




#### `ListApplicationTemplateSystemRevisions`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplateSystemRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplateSystemRevisions" `  




#### `ListApplicationTemplates`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListApplicationTemplates" `  




#### `ListApplications`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListApplications" `  




#### `ListCatalogTemplateRevisions`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogTemplateRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogTemplateRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogTemplateRevisions" `  




#### `ListCatalogTemplates`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogTemplates" `  




#### `ListCatalogs`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.catalogs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListCatalogs" `  




#### `ListComponents`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListComponents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.components.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListComponents" `  




#### `ListConnections`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.connections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListConnections" `  




#### `ListPolicies`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.policies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListPolicies" `  




#### `ListSharedTemplateRevisions`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListSharedTemplateRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.sharedTemplateRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListSharedTemplateRevisions" `  




#### `ListSharedTemplates`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListSharedTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.sharedTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListSharedTemplates" `  




#### `ListShares`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListShares`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.shares.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListShares" `  




#### `ListSpaces`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.ListSpaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.ListSpaces" `  




#### `PreviewApplication`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.PreviewApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.PreviewApplication" `  




#### `RecommendIAMRoles`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.RecommendIAMRoles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.RecommendIAMRoles" `  




#### `RegisterAppHubApplicationResources`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.RegisterAppHubApplicationResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.locations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.RegisterAppHubApplicationResources" `  




#### `RegisterDeployedApplication`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.RegisterDeployedApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.RegisterDeployedApplication" `  




#### `RegisterDeployedResources`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.RegisterDeployedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.spaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.RegisterDeployedResources" `  




#### `SnapshotApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.SnapshotApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.SnapshotApplicationTemplate" `  




#### `SyncShare`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.SyncShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `designcenter.shares.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.SyncShare" `  




#### `UpdateApplication`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.UpdateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.UpdateApplication" `  




#### `UpdateApplicationTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.UpdateApplicationTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.applicationTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.UpdateApplicationTemplate" `  




#### `UpdateCatalog`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.UpdateCatalog`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.UpdateCatalog" `  




#### `UpdateCatalogTemplate`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.UpdateCatalogTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.catalogTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.UpdateCatalogTemplate" `  




#### `UpdateComponent`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.UpdateComponent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.components.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.UpdateComponent" `  




#### `UpdateConnection`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.UpdateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.connections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.UpdateConnection" `  




#### `UpdatePolicy`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.UpdatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.UpdatePolicy" `  




#### `UpdateSpace`

  * **Method** : `google.cloud.designcenter.v1alpha.DesignCenter.UpdateSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `designcenter.spaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.designcenter.v1alpha.DesignCenter.UpdateSpace" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.iam.v1.IAMPolicy.SetIamPolicy`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



## What's next

  * Define permissions and grant roles by [controlling access with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).
  * Track your workloads by [monitoring application health and performance](https://docs.cloud.google.com/application-design-center/docs/monitor-applications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
