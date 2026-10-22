---
url: https://docs.cloud.google.com/agent-registry/audit-logging/
title: Agent Registry audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:23.729939+00:00
---

# Agent Registry audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Agent Registry audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Agent Registry. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Agent Registry audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="agentregistry.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Agent Registry generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.agentregistry.v1.AgentRegistry.FetchAvailableBindings`  
`google.cloud.agentregistry.v1.AgentRegistry.GetAgent`  
`google.cloud.agentregistry.v1.AgentRegistry.GetBinding`  
`google.cloud.agentregistry.v1.AgentRegistry.GetEndpoint`  
`google.cloud.agentregistry.v1.AgentRegistry.GetMcpServer`  
`google.cloud.agentregistry.v1.AgentRegistry.GetService`  
`google.cloud.agentregistry.v1.AgentRegistry.ListAgents`  
`google.cloud.agentregistry.v1.AgentRegistry.ListBindings`  
`google.cloud.agentregistry.v1.AgentRegistry.ListEndpoints`  
`google.cloud.agentregistry.v1.AgentRegistry.ListMcpServers`  
`google.cloud.agentregistry.v1.AgentRegistry.ListServices`  
`google.cloud.agentregistry.v1.AgentRegistry.SearchAgents`  
`google.cloud.agentregistry.v1.AgentRegistry.SearchMcpServers`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.FetchAvailableBindings`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.GetAgent`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.GetBinding`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.GetEndpoint`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.GetMcpServer`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.GetPublisher`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.GetService`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.GetSkill`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.GetSkillRevision`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.ListAgents`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.ListBindings`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.ListEndpoints`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.ListMcpServers`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.ListPublishers`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.ListServices`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.ListSkillRevisions`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.ListSkills`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.SearchAgents`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.SearchMcpServers`  
`google.cloud.agentregistry.v1alpha.AgentRegistry.SearchSkills`  
`ADMIN_WRITE` | `google.cloud.agentregistry.v1.AgentRegistry.CreateBinding` (LRO)  
`google.cloud.agentregistry.v1.AgentRegistry.CreateService` (LRO)  
`google.cloud.agentregistry.v1.AgentRegistry.DeleteBinding` (LRO)  
`google.cloud.agentregistry.v1.AgentRegistry.DeleteService` (LRO)  
`google.cloud.agentregistry.v1.AgentRegistry.UpdateBinding` (LRO)  
`google.cloud.agentregistry.v1.AgentRegistry.UpdateService` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.CreateBinding` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.CreateService` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.CreateSkill` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.CreateSkillRevision` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteBinding` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteService` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteSkill` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteSkillRevision` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateBinding` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateService` (LRO)  
`google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateSkill` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Agent Registry.

### `google.cloud.agentregistry.v1.AgentRegistry`

The following audit logs are associated with methods belonging to `google.cloud.agentregistry.v1.AgentRegistry`.

#### `CreateBinding`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.CreateBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.bindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.CreateBinding" `  




#### `CreateService`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.CreateService" `  




#### `DeleteBinding`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.DeleteBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.bindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.DeleteBinding" `  




#### `DeleteService`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.DeleteService" `  




#### `FetchAvailableBindings`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.FetchAvailableBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.bindings.fetchAvailable - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.FetchAvailableBindings" `  




#### `GetAgent`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.GetAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.GetAgent" `  




#### `GetBinding`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.GetBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.bindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.GetBinding" `  




#### `GetEndpoint`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.GetEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.endpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.GetEndpoint" `  




#### `GetMcpServer`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.GetMcpServer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.mcpServers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.GetMcpServer" `  




#### `GetService`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.GetService" `  




#### `ListAgents`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.ListAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.agents.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.ListAgents" `  




#### `ListBindings`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.ListBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.bindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.ListBindings" `  




#### `ListEndpoints`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.ListEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.endpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.ListEndpoints" `  




#### `ListMcpServers`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.ListMcpServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.mcpServers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.ListMcpServers" `  




#### `ListServices`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.ListServices" `  




#### `SearchAgents`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.SearchAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.agents.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.SearchAgents" `  




#### `SearchMcpServers`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.SearchMcpServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.mcpServers.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.SearchMcpServers" `  




#### `UpdateBinding`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.UpdateBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.bindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.UpdateBinding" `  




#### `UpdateService`

  * **Method** : `google.cloud.agentregistry.v1.AgentRegistry.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1.AgentRegistry.UpdateService" `  




### `google.cloud.agentregistry.v1alpha.AgentRegistry`

The following audit logs are associated with methods belonging to `google.cloud.agentregistry.v1alpha.AgentRegistry`.

#### `CreateBinding`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.CreateBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.bindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.CreateBinding" `  




#### `CreateService`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.CreateService" `  




#### `CreateSkill`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.CreateSkill`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.skills.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.CreateSkill" `  




#### `CreateSkillRevision`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.CreateSkillRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.skillRevisions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.CreateSkillRevision" `  




#### `DeleteBinding`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.bindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteBinding" `  




#### `DeleteService`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteService" `  




#### `DeleteSkill`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteSkill`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.skills.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteSkill" `  




#### `DeleteSkillRevision`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteSkillRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.skillRevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.DeleteSkillRevision" `  




#### `FetchAvailableBindings`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.FetchAvailableBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.bindings.fetchAvailable - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.FetchAvailableBindings" `  




#### `GetAgent`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.GetAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.GetAgent" `  




#### `GetBinding`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.GetBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.bindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.GetBinding" `  




#### `GetEndpoint`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.GetEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.endpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.GetEndpoint" `  




#### `GetMcpServer`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.GetMcpServer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.mcpServers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.GetMcpServer" `  




#### `GetPublisher`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.GetPublisher`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.publishers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.GetPublisher" `  




#### `GetService`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.GetService" `  




#### `GetSkill`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.GetSkill`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.skills.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.GetSkill" `  




#### `GetSkillRevision`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.GetSkillRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.skillRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.GetSkillRevision" `  




#### `ListAgents`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.ListAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.agents.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.ListAgents" `  




#### `ListBindings`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.ListBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.bindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.ListBindings" `  




#### `ListEndpoints`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.ListEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.endpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.ListEndpoints" `  




#### `ListMcpServers`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.ListMcpServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.mcpServers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.ListMcpServers" `  




#### `ListPublishers`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.ListPublishers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.publishers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.ListPublishers" `  




#### `ListServices`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.ListServices" `  




#### `ListSkillRevisions`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.ListSkillRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.skillRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.ListSkillRevisions" `  




#### `ListSkills`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.ListSkills`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.skills.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.ListSkills" `  




#### `SearchAgents`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.SearchAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.agents.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.SearchAgents" `  




#### `SearchMcpServers`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.SearchMcpServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.mcpServers.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.SearchMcpServers" `  




#### `SearchSkills`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.SearchSkills`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `agentregistry.skills.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.SearchSkills" `  




#### `UpdateBinding`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.bindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateBinding" `  




#### `UpdateService`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateService" `  




#### `UpdateSkill`

  * **Method** : `google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateSkill`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `agentregistry.skills.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.agentregistry.v1alpha.AgentRegistry.UpdateSkill" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
