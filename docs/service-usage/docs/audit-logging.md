---
url: https://docs.cloud.google.com/service-usage/docs/audit-logging/
title: Service Usage audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:24.452954+00:00
---

# Service Usage audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service Usage audit logging

This document lists the audited methods for Service Usage. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Service Usage audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="serviceusage.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Service Usage generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_WRITE` | `google.api.serviceusage.v1.ServiceUsage.BatchEnableServices` (LRO)  
`google.api.serviceusage.v1.ServiceUsage.DisableService` (LRO)  
`google.api.serviceusage.v1.ServiceUsage.EnableService` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.BatchEnableServices` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.CreateAdminOverride` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.CreateConsumerOverride` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.DeleteAdminOverride` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.DeleteConsumerOverride` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.DisableService` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.EnableService` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.ImportAdminOverrides` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.ImportConsumerOverrides` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.UpdateAdminOverride` (LRO)  
`google.api.serviceusage.v1beta1.ServiceUsage.UpdateConsumerOverride` (LRO)  
`google.api.serviceusage.v2beta.ServiceUsage.UpdateConsumerPolicy` (LRO)  
`google.api.serviceusage.v2beta.ServiceUsage.UpdateContentSecurityPolicy` (LRO)  
`google.api.serviceusage.v2beta.ServiceUsage.UpdateMcpPolicy` (LRO)  
`google.longrunning.Operations.GetOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Service Usage.

### `google.api.serviceusage.v1.ServiceUsage`

The following audit logs are associated with methods belonging to `google.api.serviceusage.v1.ServiceUsage`.

#### `BatchEnableServices`

  * **Method** : `google.api.serviceusage.v1.ServiceUsage.BatchEnableServices`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicemanagement.services.bind - DATA_WRITE`
    * `serviceusage.services.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.BatchEnableServices" `  




#### `DisableService`

  * **Method** : `google.api.serviceusage.v1.ServiceUsage.DisableService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.services.disable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.DisableService" `  




#### `EnableService`

  * **Method** : `google.api.serviceusage.v1.ServiceUsage.EnableService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.services.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.EnableService" `  




### `google.api.serviceusage.v1beta1.ServiceUsage`

The following audit logs are associated with methods belonging to `google.api.serviceusage.v1beta1.ServiceUsage`.

#### `BatchEnableServices`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.BatchEnableServices`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicemanagement.services.bind - DATA_WRITE`
    * `serviceusage.services.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.BatchEnableServices" `  




#### `CreateAdminOverride`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.CreateAdminOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.quotas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.CreateAdminOverride" `  




#### `CreateConsumerOverride`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.CreateConsumerOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.quotas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.CreateConsumerOverride" `  




#### `DeleteAdminOverride`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.DeleteAdminOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.quotas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.DeleteAdminOverride" `  




#### `DeleteConsumerOverride`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.DeleteConsumerOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.quotas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.DeleteConsumerOverride" `  




#### `DisableService`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.DisableService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.services.disable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.DisableService" `  




#### `EnableService`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.EnableService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `servicemanagement.services.bind - DATA_WRITE`
    * `serviceusage.services.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.EnableService" `  




#### `ImportAdminOverrides`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.ImportAdminOverrides`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.quotas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.ImportAdminOverrides" `  




#### `ImportConsumerOverrides`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.ImportConsumerOverrides`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.quotas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.ImportConsumerOverrides" `  




#### `UpdateAdminOverride`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.UpdateAdminOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.quotas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.UpdateAdminOverride" `  




#### `UpdateConsumerOverride`

  * **Method** : `google.api.serviceusage.v1beta1.ServiceUsage.UpdateConsumerOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.quotas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v1beta1.ServiceUsage.UpdateConsumerOverride" `  




### `google.api.serviceusage.v2beta.ServiceUsage`

The following audit logs are associated with methods belonging to `google.api.serviceusage.v2beta.ServiceUsage`.

#### `UpdateConsumerPolicy`

  * **Method** : `google.api.serviceusage.v2beta.ServiceUsage.UpdateConsumerPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.consumerpolicy.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v2beta.ServiceUsage.UpdateConsumerPolicy" `  




#### `UpdateContentSecurityPolicy`

  * **Method** : `google.api.serviceusage.v2beta.ServiceUsage.UpdateContentSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.contentsecuritypolicy.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v2beta.ServiceUsage.UpdateContentSecurityPolicy" `  




#### `UpdateMcpPolicy`

  * **Method** : `google.api.serviceusage.v2beta.ServiceUsage.UpdateMcpPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.mcppolicy.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.api.serviceusage.v2beta.ServiceUsage.UpdateMcpPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `serviceusage.operations.get - DATA_READ`
    * `serviceusage.services.enable - ADMIN_WRITE`
    * `serviceusage.services.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.api.serviceusage.v1.ServiceUsage.BatchGetServices`
  * `google.api.serviceusage.v1.ServiceUsage.GetService`
  * `google.api.serviceusage.v1.ServiceUsage.ListServices`
  * `google.api.serviceusage.v1beta1.ServiceUsage.GenerateServiceIdentity`
  * `google.api.serviceusage.v1beta1.ServiceUsage.GetConsumerQuotaLimit`
  * `google.api.serviceusage.v1beta1.ServiceUsage.GetConsumerQuotaMetric`
  * `google.api.serviceusage.v1beta1.ServiceUsage.GetService`
  * `google.api.serviceusage.v1beta1.ServiceUsage.ListAdminOverrides`
  * `google.api.serviceusage.v1beta1.ServiceUsage.ListConsumerOverrides`
  * `google.api.serviceusage.v1beta1.ServiceUsage.ListConsumerQuotaMetrics`
  * `google.api.serviceusage.v1beta1.ServiceUsage.ListServices`
  * `google.api.serviceusage.v2beta.ServiceUsage.AnalyzeConsumerPolicy`
  * `google.api.serviceusage.v2beta.ServiceUsage.BatchGetServices`
  * `google.api.serviceusage.v2beta.ServiceUsage.GetConsumerPolicy`
  * `google.api.serviceusage.v2beta.ServiceUsage.GetContentSecurityPolicy`
  * `google.api.serviceusage.v2beta.ServiceUsage.GetEffectiveMcpPolicy`
  * `google.api.serviceusage.v2beta.ServiceUsage.GetEffectivePolicy`
  * `google.api.serviceusage.v2beta.ServiceUsage.GetMcpPolicy`
  * `google.api.serviceusage.v2beta.ServiceUsage.GetService`
  * `google.api.serviceusage.v2beta.ServiceUsage.ListCatalogMembers`
  * `google.api.serviceusage.v2beta.ServiceUsage.ListDependentServices`
  * `google.api.serviceusage.v2beta.ServiceUsage.ListExpandedMembers`
  * `google.api.serviceusage.v2beta.ServiceUsage.ListGroupMembers`
  * `google.api.serviceusage.v2beta.ServiceUsage.ListPublicServices`
  * `google.api.serviceusage.v2beta.ServiceUsage.ListServiceGroups`
  * `google.api.serviceusage.v2beta.ServiceUsage.ListSharedServices`
  * `google.api.serviceusage.v2beta.ServiceUsage.TestEnabled`
  * `google.api.serviceusage.v2beta.ServiceUsage.TestMcpEnabled`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
