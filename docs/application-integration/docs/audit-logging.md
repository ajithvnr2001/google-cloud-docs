---
url: https://docs.cloud.google.com/application-integration/docs/audit-logging/
title: Application Integration audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:52.556426+00:00
---

# Application Integration audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Application Integration audit logging 

This document describes audit logging for Application Integration. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Application Integration audit logs use the service name `integrations.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="integrations.googleapis.com"
      

## Methods by permission type

Only `cloud.integrations.v1` operations are supported for the Application Integration REST API. The `cloud.integrations.v1alpha` gRPC operations listed below as subject to audit logging are UI calls.

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Application Integration generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.integrations.v1alpha.AuthConfigs.GetAuthConfig`  
`google.cloud.integrations.v1alpha.AuthConfigs.ListAuthConfigs`  
`google.cloud.integrations.v1alpha.Certificates.GetCertificate`  
`google.cloud.integrations.v1alpha.Certificates.ListCertificates`  
`google.cloud.integrations.v1alpha.Client.GetClient`  
`google.cloud.integrations.v1alpha.Client.GetClientMetadata`  
`google.cloud.integrations.v1alpha.SfdcChannels.GetSfdcChannel`  
`google.cloud.integrations.v1alpha.SfdcChannels.ListSfdcChannels`  
`google.cloud.integrations.v1alpha.SfdcInstances.GetSfdcInstance`  
`google.cloud.integrations.v1alpha.SfdcInstances.ListSfdcInstances`  
`ADMIN_WRITE` | `google.cloud.integrations.v1alpha.AuthConfigs.CreateAuthConfig`  
`google.cloud.integrations.v1alpha.AuthConfigs.DeleteAuthConfig`  
`google.cloud.integrations.v1alpha.AuthConfigs.UpdateAuthConfig`  
`google.cloud.integrations.v1alpha.Certificates.CreateCertificate`  
`google.cloud.integrations.v1alpha.Certificates.DeleteCertificate`  
`google.cloud.integrations.v1alpha.Certificates.UpdateCertificate`  
`google.cloud.integrations.v1alpha.Client.DeprovisionClient`  
`google.cloud.integrations.v1alpha.Client.ProvisionClient`  
`google.cloud.integrations.v1alpha.Client.ReplaceServiceAccount`  
`google.cloud.integrations.v1alpha.Client.SwitchEncryption`  
`google.cloud.integrations.v1alpha.Client.SwitchVariableMasking`  
`google.cloud.integrations.v1alpha.SfdcChannels.CreateSfdcChannel`  
`google.cloud.integrations.v1alpha.SfdcChannels.DeleteSfdcChannel`  
`google.cloud.integrations.v1alpha.SfdcChannels.UpdateSfdcChannel`  
`google.cloud.integrations.v1alpha.SfdcInstances.CreateSfdcInstance`  
`google.cloud.integrations.v1alpha.SfdcInstances.DeleteSfdcInstance`  
`google.cloud.integrations.v1alpha.SfdcInstances.UpdateSfdcInstance`  
`DATA_READ` | `google.cloud.integrations.v1alpha.Condition.ValidateCondition`  
`google.cloud.integrations.v1alpha.Executions.DownloadExecution`  
`google.cloud.integrations.v1alpha.Executions.GetExecution`  
`google.cloud.integrations.v1alpha.Executions.ListExecutions`  
`google.cloud.integrations.v1alpha.Experiment.ListExperiments`  
`google.cloud.integrations.v1alpha.IntegrationVersions.DownloadIntegrationVersion`  
`google.cloud.integrations.v1alpha.IntegrationVersions.DownloadJsonPackage`  
`google.cloud.integrations.v1alpha.IntegrationVersions.GetIntegrationVersion`  
`google.cloud.integrations.v1alpha.IntegrationVersions.ListIntegrationVersions`  
`google.cloud.integrations.v1alpha.Integrations.ListIntegrations`  
`google.cloud.integrations.v1alpha.Integrations.ListTaskEntities`  
`google.cloud.integrations.v1alpha.JsonSchema.GenerateJsonSchema`  
`google.cloud.integrations.v1alpha.Suspensions.ListSuspensions`  
`google.cloud.integrations.v1alpha.TemplateService.DownloadTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.GetTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.ListTemplates`  
`google.cloud.integrations.v1alpha.TemplateService.SearchTemplates`  
`google.cloud.integrations.v1alpha.TransformFunction.ListTransformFunctionDefinitions`  
`google.cloud.integrations.v1alpha.TransformFunction.ListTransformFunctions`  
`google.cloud.integrations.v2.Executions.ListExecutions`  
`DATA_WRITE` | `google.cloud.integrations.v1alpha.CloudFunctions.CreateCloudFunction`  
`google.cloud.integrations.v1alpha.Executions.ExecuteEvent`  
`google.cloud.integrations.v1alpha.Executions.ExecuteIntegrations`  
`google.cloud.integrations.v1alpha.Executions.ScheduleIntegrations`  
`google.cloud.integrations.v1alpha.Executions.TestIntegrations`  
`google.cloud.integrations.v1alpha.IntegrationVersions.CreateIntegrationVersion`  
`google.cloud.integrations.v1alpha.IntegrationVersions.DeleteIntegrationVersion`  
`google.cloud.integrations.v1alpha.IntegrationVersions.PublishIntegrationVersion`  
`google.cloud.integrations.v1alpha.IntegrationVersions.TakeoverEditLock`  
`google.cloud.integrations.v1alpha.IntegrationVersions.UnpublishIntegrationVersion`  
`google.cloud.integrations.v1alpha.IntegrationVersions.UpdateIntegrationVersion`  
`google.cloud.integrations.v1alpha.IntegrationVersions.UploadIntegrationVersion`  
`google.cloud.integrations.v1alpha.Integrations.DeleteIntegration`  
`google.cloud.integrations.v1alpha.Suspensions.LiftSuspension`  
`google.cloud.integrations.v1alpha.Suspensions.ResolveSuspension`  
`google.cloud.integrations.v1alpha.TemplateService.CreateTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.DeleteTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.ImportTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.ShareTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.UnshareTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.UpdateTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.UploadTemplate`  
`google.cloud.integrations.v1alpha.TemplateService.UseTemplate`  
`google.cloud.integrations.v2.Executions.ExecuteIntegration`  
`google.cloud.integrations.v2.Executions.ScheduleIntegration`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Application Integration.

### `google.cloud.integrations.v1alpha.AuthConfigs`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.AuthConfigs`.

#### `CreateAuthConfig`

  * **Method** : `google.cloud.integrations.v1alpha.AuthConfigs.CreateAuthConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.authConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.AuthConfigs.CreateAuthConfig" `  




#### `DeleteAuthConfig`

  * **Method** : `google.cloud.integrations.v1alpha.AuthConfigs.DeleteAuthConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.authConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.AuthConfigs.DeleteAuthConfig" `  




#### `GetAuthConfig`

  * **Method** : `google.cloud.integrations.v1alpha.AuthConfigs.GetAuthConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.authConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.AuthConfigs.GetAuthConfig" `  




#### `ListAuthConfigs`

  * **Method** : `google.cloud.integrations.v1alpha.AuthConfigs.ListAuthConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.authConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.AuthConfigs.ListAuthConfigs" `  




#### `UpdateAuthConfig`

  * **Method** : `google.cloud.integrations.v1alpha.AuthConfigs.UpdateAuthConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.authConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.AuthConfigs.UpdateAuthConfig" `  




### `google.cloud.integrations.v1alpha.Certificates`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.Certificates`.

#### `CreateCertificate`

  * **Method** : `google.cloud.integrations.v1alpha.Certificates.CreateCertificate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.certificates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Certificates.CreateCertificate" `  




#### `DeleteCertificate`

  * **Method** : `google.cloud.integrations.v1alpha.Certificates.DeleteCertificate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.certificates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Certificates.DeleteCertificate" `  




#### `GetCertificate`

  * **Method** : `google.cloud.integrations.v1alpha.Certificates.GetCertificate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.certificates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Certificates.GetCertificate" `  




#### `ListCertificates`

  * **Method** : `google.cloud.integrations.v1alpha.Certificates.ListCertificates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.certificates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Certificates.ListCertificates" `  




#### `UpdateCertificate`

  * **Method** : `google.cloud.integrations.v1alpha.Certificates.UpdateCertificate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.certificates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Certificates.UpdateCertificate" `  




### `google.cloud.integrations.v1alpha.Client`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.Client`.

#### `DeprovisionClient`

  * **Method** : `google.cloud.integrations.v1alpha.Client.DeprovisionClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.authConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Client.DeprovisionClient" `  




#### `GetClient`

  * **Method** : `google.cloud.integrations.v1alpha.Client.GetClient`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.authConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Client.GetClient" `  




#### `GetClientMetadata`

  * **Method** : `google.cloud.integrations.v1alpha.Client.GetClientMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Client.GetClientMetadata" `  




#### `ProvisionClient`

  * **Method** : `google.cloud.integrations.v1alpha.Client.ProvisionClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.authConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Client.ProvisionClient" `  




#### `ReplaceServiceAccount`

  * **Method** : `google.cloud.integrations.v1alpha.Client.ReplaceServiceAccount`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.authConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Client.ReplaceServiceAccount" `  




#### `SwitchEncryption`

  * **Method** : `google.cloud.integrations.v1alpha.Client.SwitchEncryption`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.authConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Client.SwitchEncryption" `  




#### `SwitchVariableMasking`

  * **Method** : `google.cloud.integrations.v1alpha.Client.SwitchVariableMasking`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.authConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Client.SwitchVariableMasking" `  




### `google.cloud.integrations.v1alpha.CloudFunctions`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.CloudFunctions`.

#### `CreateCloudFunction`

  * **Method** : `google.cloud.integrations.v1alpha.CloudFunctions.CreateCloudFunction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.CloudFunctions.CreateCloudFunction" `  




### `google.cloud.integrations.v1alpha.Condition`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.Condition`.

#### `ValidateCondition`

  * **Method** : `google.cloud.integrations.v1alpha.Condition.ValidateCondition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Condition.ValidateCondition" `  




### `google.cloud.integrations.v1alpha.Executions`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.Executions`.

#### `DownloadExecution`

  * **Method** : `google.cloud.integrations.v1alpha.Executions.DownloadExecution`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.executions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Executions.DownloadExecution" `  




#### `ExecuteEvent`

  * **Method** : `google.cloud.integrations.v1alpha.Executions.ExecuteEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.invoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Executions.ExecuteEvent" `  




#### `ExecuteIntegrations`

  * **Method** : `google.cloud.integrations.v1alpha.Executions.ExecuteIntegrations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.invoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Executions.ExecuteIntegrations" `  




#### `GetExecution`

  * **Method** : `google.cloud.integrations.v1alpha.Executions.GetExecution`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.executions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Executions.GetExecution" `  




#### `ListExecutions`

  * **Method** : `google.cloud.integrations.v1alpha.Executions.ListExecutions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.executions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Executions.ListExecutions" `  




#### `ScheduleIntegrations`

  * **Method** : `google.cloud.integrations.v1alpha.Executions.ScheduleIntegrations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.invoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Executions.ScheduleIntegrations" `  




#### `TestIntegrations`

  * **Method** : `google.cloud.integrations.v1alpha.Executions.TestIntegrations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.invoke - DATA_WRITE`
    * `integrations.integrations.invoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Executions.TestIntegrations" `  




### `google.cloud.integrations.v1alpha.Experiment`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.Experiment`.

#### `ListExperiments`

  * **Method** : `google.cloud.integrations.v1alpha.Experiment.ListExperiments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Experiment.ListExperiments" `  




### `google.cloud.integrations.v1alpha.IntegrationVersions`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.IntegrationVersions`.

#### `CreateIntegrationVersion`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.CreateIntegrationVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.CreateIntegrationVersion" `  




#### `DeleteIntegrationVersion`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.DeleteIntegrationVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.DeleteIntegrationVersion" `  




#### `DownloadIntegrationVersion`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.DownloadIntegrationVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.DownloadIntegrationVersion" `  




#### `DownloadJsonPackage`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.DownloadJsonPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.DownloadJsonPackage" `  




#### `GetIntegrationVersion`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.GetIntegrationVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.GetIntegrationVersion" `  




#### `ListIntegrationVersions`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.ListIntegrationVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.ListIntegrationVersions" `  




#### `PublishIntegrationVersion`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.PublishIntegrationVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.deploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.PublishIntegrationVersion" `  




#### `TakeoverEditLock`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.TakeoverEditLock`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.TakeoverEditLock" `  




#### `UnpublishIntegrationVersion`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.UnpublishIntegrationVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.deploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.UnpublishIntegrationVersion" `  




#### `UpdateIntegrationVersion`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.UpdateIntegrationVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.UpdateIntegrationVersion" `  




#### `UploadIntegrationVersion`

  * **Method** : `google.cloud.integrations.v1alpha.IntegrationVersions.UploadIntegrationVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrationVersions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.IntegrationVersions.UploadIntegrationVersion" `  




### `google.cloud.integrations.v1alpha.Integrations`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.Integrations`.

#### `DeleteIntegration`

  * **Method** : `google.cloud.integrations.v1alpha.Integrations.DeleteIntegration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Integrations.DeleteIntegration" `  




#### `ListIntegrations`

  * **Method** : `google.cloud.integrations.v1alpha.Integrations.ListIntegrations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Integrations.ListIntegrations" `  




#### `ListTaskEntities`

  * **Method** : `google.cloud.integrations.v1alpha.Integrations.ListTaskEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Integrations.ListTaskEntities" `  




### `google.cloud.integrations.v1alpha.JsonSchema`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.JsonSchema`.

#### `GenerateJsonSchema`

  * **Method** : `google.cloud.integrations.v1alpha.JsonSchema.GenerateJsonSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.JsonSchema.GenerateJsonSchema" `  




### `google.cloud.integrations.v1alpha.SfdcChannels`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.SfdcChannels`.

#### `CreateSfdcChannel`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcChannels.CreateSfdcChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.sfdcChannels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcChannels.CreateSfdcChannel" `  




#### `DeleteSfdcChannel`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcChannels.DeleteSfdcChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.sfdcChannels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcChannels.DeleteSfdcChannel" `  




#### `GetSfdcChannel`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcChannels.GetSfdcChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.sfdcChannels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcChannels.GetSfdcChannel" `  




#### `ListSfdcChannels`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcChannels.ListSfdcChannels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.sfdcChannels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcChannels.ListSfdcChannels" `  




#### `UpdateSfdcChannel`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcChannels.UpdateSfdcChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.sfdcChannels.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcChannels.UpdateSfdcChannel" `  




### `google.cloud.integrations.v1alpha.SfdcInstances`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.SfdcInstances`.

#### `CreateSfdcInstance`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcInstances.CreateSfdcInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.sfdcInstances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcInstances.CreateSfdcInstance" `  




#### `DeleteSfdcInstance`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcInstances.DeleteSfdcInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.sfdcInstances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcInstances.DeleteSfdcInstance" `  




#### `GetSfdcInstance`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcInstances.GetSfdcInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.sfdcInstances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcInstances.GetSfdcInstance" `  




#### `ListSfdcInstances`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcInstances.ListSfdcInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.sfdcInstances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcInstances.ListSfdcInstances" `  




#### `UpdateSfdcInstance`

  * **Method** : `google.cloud.integrations.v1alpha.SfdcInstances.UpdateSfdcInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `integrations.sfdcInstances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.SfdcInstances.UpdateSfdcInstance" `  




### `google.cloud.integrations.v1alpha.Suspensions`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.Suspensions`.

#### `LiftSuspension`

  * **Method** : `google.cloud.integrations.v1alpha.Suspensions.LiftSuspension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.suspensions.lift - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Suspensions.LiftSuspension" `  




#### `ListSuspensions`

  * **Method** : `google.cloud.integrations.v1alpha.Suspensions.ListSuspensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.suspensions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Suspensions.ListSuspensions" `  




#### `ResolveSuspension`

  * **Method** : `google.cloud.integrations.v1alpha.Suspensions.ResolveSuspension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.suspensions.resolve - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.Suspensions.ResolveSuspension" `  




### `google.cloud.integrations.v1alpha.TemplateService`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.TemplateService`.

#### `CreateTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.CreateTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.CreateTemplate" `  




#### `DeleteTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.DeleteTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.DeleteTemplate" `  




#### `DownloadTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.DownloadTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.DownloadTemplate" `  




#### `GetTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.GetTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.GetTemplate" `  




#### `ImportTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.ImportTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.use - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.ImportTemplate" `  




#### `ListTemplates`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.ListTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.ListTemplates" `  




#### `SearchTemplates`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.SearchTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.SearchTemplates" `  




#### `ShareTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.ShareTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.share - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.ShareTemplate" `  




#### `UnshareTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.UnshareTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.unshare - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.UnshareTemplate" `  




#### `UpdateTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.UpdateTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.UpdateTemplate" `  




#### `UploadTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.UploadTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.UploadTemplate" `  




#### `UseTemplate`

  * **Method** : `google.cloud.integrations.v1alpha.TemplateService.UseTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.templates.use - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TemplateService.UseTemplate" `  




### `google.cloud.integrations.v1alpha.TransformFunction`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v1alpha.TransformFunction`.

#### `ListTransformFunctionDefinitions`

  * **Method** : `google.cloud.integrations.v1alpha.TransformFunction.ListTransformFunctionDefinitions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TransformFunction.ListTransformFunctionDefinitions" `  




#### `ListTransformFunctions`

  * **Method** : `google.cloud.integrations.v1alpha.TransformFunction.ListTransformFunctions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v1alpha.TransformFunction.ListTransformFunctions" `  




### `google.cloud.integrations.v2.Executions`

The following audit logs are associated with methods belonging to `google.cloud.integrations.v2.Executions`.

#### `ExecuteIntegration`

  * **Method** : `google.cloud.integrations.v2.Executions.ExecuteIntegration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.invoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v2.Executions.ExecuteIntegration" `  




#### `ListExecutions`

  * **Method** : `google.cloud.integrations.v2.Executions.ListExecutions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.executions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v2.Executions.ListExecutions" `  




#### `ScheduleIntegration`

  * **Method** : `google.cloud.integrations.v2.Executions.ScheduleIntegration`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `integrations.integrations.invoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.integrations.v2.Executions.ScheduleIntegration" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.integrations.v1alpha.AppsScriptIntegration.CreateAppsScriptProject`
  * `google.cloud.integrations.v1alpha.AppsScriptIntegration.LinkAppsScriptProject`
  * `google.cloud.integrations.v1alpha.Connectors.EnumerateConnectorPlatformRegions`
  * `google.cloud.integrations.v1alpha.Connectors.GetConnectionSchemaMetadata`
  * `google.cloud.integrations.v1alpha.Connectors.ListConnections`
  * `google.cloud.integrations.v1alpha.Connectors.ListRuntimeActionSchemas`
  * `google.cloud.integrations.v1alpha.Connectors.ListRuntimeEntitySchemas`
  * `google.cloud.integrations.v1alpha.EventbusOAuthCodeRedirectService.GenerateToken`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
