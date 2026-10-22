---
url: https://docs.cloud.google.com/model-armor/audit-logging-model-armor/
title: Model Armor audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:43.069594+00:00
---

# Model Armor audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/audit-logging-model-armor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Model Armor audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Model Armor. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Model Armor audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="modelarmor.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Model Armor generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.modelarmor.v1.ModelArmor.GetFloorSetting`  
`google.cloud.modelarmor.v1.ModelArmor.GetTemplate`  
`google.cloud.modelarmor.v1.ModelArmor.ListTemplates`  
`google.cloud.modelarmor.v1alpha.ModelArmor.GetFloorSetting`  
`google.cloud.modelarmor.v1alpha.ModelArmor.GetTemplate`  
`google.cloud.modelarmor.v1alpha.ModelArmor.ListTemplates`  
`google.cloud.modelarmor.v1beta.ModelArmor.GetFloorSetting`  
`google.cloud.modelarmor.v1beta.ModelArmor.GetTemplate`  
`google.cloud.modelarmor.v1beta.ModelArmor.ListTemplates`  
`ADMIN_WRITE` | `google.cloud.modelarmor.v1.ModelArmor.CreateTemplate`  
`google.cloud.modelarmor.v1.ModelArmor.DeleteTemplate`  
`google.cloud.modelarmor.v1.ModelArmor.UpdateFloorSetting`  
`google.cloud.modelarmor.v1.ModelArmor.UpdateTemplate`  
`google.cloud.modelarmor.v1alpha.ModelArmor.CreateTemplate`  
`google.cloud.modelarmor.v1alpha.ModelArmor.DeleteTemplate`  
`google.cloud.modelarmor.v1alpha.ModelArmor.UpdateFloorSetting`  
`google.cloud.modelarmor.v1alpha.ModelArmor.UpdateTemplate`  
`google.cloud.modelarmor.v1beta.ModelArmor.CreateTemplate`  
`google.cloud.modelarmor.v1beta.ModelArmor.DeleteTemplate`  
`google.cloud.modelarmor.v1beta.ModelArmor.UpdateFloorSetting`  
`google.cloud.modelarmor.v1beta.ModelArmor.UpdateTemplate`  
`DATA_READ` | `google.cloud.modelarmor.v1.ModelArmor.SanitizeModelResponse`  
`google.cloud.modelarmor.v1.ModelArmor.SanitizeUserPrompt`  
`google.cloud.modelarmor.v1.ModelArmor.StreamSanitizeModelResponse`  
`google.cloud.modelarmor.v1.ModelArmor.StreamSanitizeUserPrompt`  
`google.cloud.modelarmor.v1alpha.ModelArmor.SanitizeModelResponse`  
`google.cloud.modelarmor.v1alpha.ModelArmor.SanitizeUserPrompt`  
`google.cloud.modelarmor.v1beta.ModelArmor.SanitizeModelResponse`  
`google.cloud.modelarmor.v1beta.ModelArmor.SanitizeUserPrompt`  
`google.cloud.modelarmor.v1beta.ModelArmor.StreamSanitizeModelResponse`  
`google.cloud.modelarmor.v1beta.ModelArmor.StreamSanitizeUserPrompt`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Model Armor.

### `google.cloud.modelarmor.v1.ModelArmor`

The following audit logs are associated with methods belonging to `google.cloud.modelarmor.v1.ModelArmor`.

#### `CreateTemplate`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.CreateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.CreateTemplate" `  




#### `DeleteTemplate`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.DeleteTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.DeleteTemplate" `  




#### `GetFloorSetting`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.GetFloorSetting`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.floorSettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.GetFloorSetting" `  




#### `GetTemplate`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.GetTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.GetTemplate" `  




#### `ListTemplates`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.ListTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.ListTemplates" `  




#### `SanitizeModelResponse`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.SanitizeModelResponse`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToSanitizeModelResponse - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.SanitizeModelResponse" `  




#### `SanitizeUserPrompt`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.SanitizeUserPrompt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToSanitizeUserPrompt - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.SanitizeUserPrompt" `  




#### `StreamSanitizeModelResponse`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.StreamSanitizeModelResponse`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToStreamSanitizeModelResponse - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.StreamSanitizeModelResponse" `  




#### `StreamSanitizeUserPrompt`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.StreamSanitizeUserPrompt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToStreamSanitizeUserPrompt - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.StreamSanitizeUserPrompt" `  




#### `UpdateFloorSetting`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.UpdateFloorSetting`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.floorSettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.UpdateFloorSetting" `  




#### `UpdateTemplate`

  * **Method** : `google.cloud.modelarmor.v1.ModelArmor.UpdateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1.ModelArmor.UpdateTemplate" `  




### `google.cloud.modelarmor.v1alpha.ModelArmor`

The following audit logs are associated with methods belonging to `google.cloud.modelarmor.v1alpha.ModelArmor`.

#### `CreateTemplate`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.CreateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.CreateTemplate" `  




#### `DeleteTemplate`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.DeleteTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.DeleteTemplate" `  




#### `GetFloorSetting`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.GetFloorSetting`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.floorSettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.GetFloorSetting" `  




#### `GetTemplate`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.GetTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.GetTemplate" `  




#### `ListTemplates`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.ListTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.ListTemplates" `  




#### `SanitizeModelResponse`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.SanitizeModelResponse`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToSanitizeModelResponse - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.SanitizeModelResponse" `  




#### `SanitizeUserPrompt`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.SanitizeUserPrompt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToSanitizeUserPrompt - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.SanitizeUserPrompt" `  




#### `UpdateFloorSetting`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.UpdateFloorSetting`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.floorSettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.UpdateFloorSetting" `  




#### `UpdateTemplate`

  * **Method** : `google.cloud.modelarmor.v1alpha.ModelArmor.UpdateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1alpha.ModelArmor.UpdateTemplate" `  




### `google.cloud.modelarmor.v1beta.ModelArmor`

The following audit logs are associated with methods belonging to `google.cloud.modelarmor.v1beta.ModelArmor`.

#### `CreateTemplate`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.CreateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.CreateTemplate" `  




#### `DeleteTemplate`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.DeleteTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.DeleteTemplate" `  




#### `GetFloorSetting`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.GetFloorSetting`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.floorSettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.GetFloorSetting" `  




#### `GetTemplate`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.GetTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.GetTemplate" `  




#### `ListTemplates`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.ListTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.ListTemplates" `  




#### `SanitizeModelResponse`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.SanitizeModelResponse`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToSanitizeModelResponse - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.SanitizeModelResponse" `  




#### `SanitizeUserPrompt`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.SanitizeUserPrompt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToSanitizeUserPrompt - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.SanitizeUserPrompt" `  




#### `StreamSanitizeModelResponse`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.StreamSanitizeModelResponse`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToStreamSanitizeModelResponse - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.StreamSanitizeModelResponse" `  




#### `StreamSanitizeUserPrompt`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.StreamSanitizeUserPrompt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `modelarmor.templates.useToStreamSanitizeUserPrompt - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.StreamSanitizeUserPrompt" `  




#### `UpdateFloorSetting`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.UpdateFloorSetting`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.floorSettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.UpdateFloorSetting" `  




#### `UpdateTemplate`

  * **Method** : `google.cloud.modelarmor.v1beta.ModelArmor.UpdateTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `modelarmor.templates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.modelarmor.v1beta.ModelArmor.UpdateTemplate" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `envoy.service.ext_proc.v3.ExternalProcessor.Process`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
