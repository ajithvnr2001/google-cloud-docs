---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/audit-logging/
title: Conversational Analytics API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:24:38.554146+00:00
---

# Conversational Analytics API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Conversational Analytics API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Gemini Data Analytics. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Gemini Data Analytics audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="geminidataanalytics.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Gemini Data Analytics generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.geminidataanalytics.v1.DataAgentService.GetDataAgent`  
`google.cloud.geminidataanalytics.v1.DataAgentService.GetIamPolicy`  
`google.cloud.geminidataanalytics.v1.DataAgentService.ListAccessibleDataAgents`  
`google.cloud.geminidataanalytics.v1.DataAgentService.ListDataAgents`  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.GetDataAgent`  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.GetIamPolicy`  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.ListDataAgents`  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.GetDataAgent`  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.GetIamPolicy`  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.ListDataAgents`  
`ADMIN_WRITE` | `google.cloud.geminidataanalytics.v1.DataAgentService.CreateDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1.DataAgentService.CreateDataAgentSync`  
`google.cloud.geminidataanalytics.v1.DataAgentService.DeleteDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1.DataAgentService.DeleteDataAgentSync`  
`google.cloud.geminidataanalytics.v1.DataAgentService.SetIamPolicy`  
`google.cloud.geminidataanalytics.v1.DataAgentService.UpdateDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1.DataAgentService.UpdateDataAgentSync`  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.CreateDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.CreateDataAgentSync`  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.DeleteDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.DeleteDataAgentSync`  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.SetIamPolicy`  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.UpdateDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1alpha.DataAgentService.UpdateDataAgentSync`  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.CreateDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.CreateDataAgentSync`  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.DeleteDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.DeleteDataAgentSync`  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.SetIamPolicy`  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.UpdateDataAgent` (LRO)  
`google.cloud.geminidataanalytics.v1beta.DataAgentService.UpdateDataAgentSync`  
`DATA_READ` | `a2a.v1.A2AService.SendMessage`  
`a2a.v1.A2AService.SendStreamingMessage`  
`google.cloud.geminidataanalytics.v1.DataChatService.Chat`  
`google.cloud.geminidataanalytics.v1alpha.DataChatService.Chat`  
`google.cloud.geminidataanalytics.v1beta.DataChatService.Chat`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control) for Gemini Data Analytics.

### `a2a.v1.A2AService`

The following audit logs are associated with methods belonging to `a2a.v1.A2AService`.

#### `SendMessage`

  * **Method** : `a2a.v1.A2AService.SendMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.chat - DATA_READ`
    * `geminidataanalytics.locations.chat - DATA_READ`
    * `geminidataanalytics.locations.useDataEngineeringAgent - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="a2a.v1.A2AService.SendMessage" `  




#### `SendStreamingMessage`

  * **Method** : `a2a.v1.A2AService.SendStreamingMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.chat - DATA_READ`
    * `geminidataanalytics.locations.chat - DATA_READ`
    * `geminidataanalytics.locations.useDataEngineeringAgent - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="a2a.v1.A2AService.SendStreamingMessage" `  




### `google.cloud.geminidataanalytics.v1.DataAgentService`

The following audit logs are associated with methods belonging to `google.cloud.geminidataanalytics.v1.DataAgentService`.

#### `CreateDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.CreateDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.CreateDataAgent" `  




#### `CreateDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.CreateDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.CreateDataAgentSync" `  




#### `DeleteDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.DeleteDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.DeleteDataAgent" `  




#### `DeleteDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.DeleteDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.DeleteDataAgentSync" `  




#### `GetDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.GetDataAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.GetDataAgent" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.GetIamPolicy" `  




#### `ListAccessibleDataAgents`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.ListAccessibleDataAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.ListAccessibleDataAgents" `  




#### `ListDataAgents`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.ListDataAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.ListDataAgents" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.SetIamPolicy" `  




#### `UpdateDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.UpdateDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.UpdateDataAgent" `  




#### `UpdateDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataAgentService.UpdateDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataAgentService.UpdateDataAgentSync" `  




### `google.cloud.geminidataanalytics.v1.DataChatService`

The following audit logs are associated with methods belonging to `google.cloud.geminidataanalytics.v1.DataChatService`.

#### `Chat`

  * **Method** : `google.cloud.geminidataanalytics.v1.DataChatService.Chat`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.chat - DATA_READ`
    * `geminidataanalytics.locations.chat - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1.DataChatService.Chat" `  




### `google.cloud.geminidataanalytics.v1alpha.DataAgentService`

The following audit logs are associated with methods belonging to `google.cloud.geminidataanalytics.v1alpha.DataAgentService`.

#### `CreateDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.CreateDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.CreateDataAgent" `  




#### `CreateDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.CreateDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.CreateDataAgentSync" `  




#### `DeleteDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.DeleteDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.DeleteDataAgent" `  




#### `DeleteDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.DeleteDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.DeleteDataAgentSync" `  




#### `GetDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.GetDataAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.GetDataAgent" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.GetIamPolicy" `  




#### `ListDataAgents`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.ListDataAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.ListDataAgents" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.SetIamPolicy" `  




#### `UpdateDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.UpdateDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.UpdateDataAgent" `  




#### `UpdateDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataAgentService.UpdateDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataAgentService.UpdateDataAgentSync" `  




### `google.cloud.geminidataanalytics.v1alpha.DataChatService`

The following audit logs are associated with methods belonging to `google.cloud.geminidataanalytics.v1alpha.DataChatService`.

#### `Chat`

  * **Method** : `google.cloud.geminidataanalytics.v1alpha.DataChatService.Chat`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.chat - DATA_READ`
    * `geminidataanalytics.locations.chat - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1alpha.DataChatService.Chat" `  




### `google.cloud.geminidataanalytics.v1beta.DataAgentService`

The following audit logs are associated with methods belonging to `google.cloud.geminidataanalytics.v1beta.DataAgentService`.

#### `CreateDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.CreateDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.CreateDataAgent" `  




#### `CreateDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.CreateDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.CreateDataAgentSync" `  




#### `DeleteDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.DeleteDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.DeleteDataAgent" `  




#### `DeleteDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.DeleteDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.DeleteDataAgentSync" `  




#### `GetDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.GetDataAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.GetDataAgent" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.GetIamPolicy" `  




#### `ListDataAgents`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.ListDataAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.ListDataAgents" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.SetIamPolicy" `  




#### `UpdateDataAgent`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.UpdateDataAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.UpdateDataAgent" `  




#### `UpdateDataAgentSync`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataAgentService.UpdateDataAgentSync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataAgentService.UpdateDataAgentSync" `  




### `google.cloud.geminidataanalytics.v1beta.DataChatService`

The following audit logs are associated with methods belonging to `google.cloud.geminidataanalytics.v1beta.DataChatService`.

#### `Chat`

  * **Method** : `google.cloud.geminidataanalytics.v1beta.DataChatService.Chat`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminidataanalytics.dataAgents.chat - DATA_READ`
    * `geminidataanalytics.locations.chat - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminidataanalytics.v1beta.DataChatService.Chat" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.geminidataanalytics.v1.DataChatService.CreateConversation`
  * `google.cloud.geminidataanalytics.v1.DataChatService.DeleteConversation`
  * `google.cloud.geminidataanalytics.v1.DataChatService.GetConversation`
  * `google.cloud.geminidataanalytics.v1.DataChatService.ListConversations`
  * `google.cloud.geminidataanalytics.v1.DataChatService.ListMessages`
  * `google.cloud.geminidataanalytics.v1alpha.DataAgentService.ListAccessibleDataAgents`
  * `google.cloud.geminidataanalytics.v1alpha.DataChatService.CreateConversation`
  * `google.cloud.geminidataanalytics.v1alpha.DataChatService.DeleteConversation`
  * `google.cloud.geminidataanalytics.v1alpha.DataChatService.GetConversation`
  * `google.cloud.geminidataanalytics.v1alpha.DataChatService.ListConversations`
  * `google.cloud.geminidataanalytics.v1alpha.DataChatService.ListMessages`
  * `google.cloud.geminidataanalytics.v1alpha.DataChatService.QueryData`
  * `google.cloud.geminidataanalytics.v1beta.DataAgentService.ListAccessibleDataAgents`
  * `google.cloud.geminidataanalytics.v1beta.DataChatService.CreateConversation`
  * `google.cloud.geminidataanalytics.v1beta.DataChatService.DeleteConversation`
  * `google.cloud.geminidataanalytics.v1beta.DataChatService.GetConversation`
  * `google.cloud.geminidataanalytics.v1beta.DataChatService.ListConversations`
  * `google.cloud.geminidataanalytics.v1beta.DataChatService.ListMessages`
  * `google.cloud.geminidataanalytics.v1beta.DataChatService.QueryData`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
