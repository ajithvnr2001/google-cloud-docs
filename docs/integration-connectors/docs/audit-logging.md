---
url: https://docs.cloud.google.com/integration-connectors/docs/audit-logging/
title: Integration Connectors audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:28.466320+00:00
---

# Integration Connectors audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration Connectors audit logging

This document describes audit logging for Integration Connectors. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Integration Connectors audit logs use the service name `connectors.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="connectors.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Integration Connectors generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `cloud.connectors.runtime.v2.ActionService.GetAction`  
`cloud.connectors.runtime.v2.ActionService.ListActions`  
`cloud.connectors.runtime.v2.EntityService.GetEntityType`  
`cloud.connectors.runtime.v2.EntityService.ListEntities`  
`cloud.connectors.runtime.v2.EntityService.ListEntityTypes`  
`google.cloud.connectors.v1.Connectors.GetConnection`  
`google.cloud.connectors.v1.Connectors.GetConnector`  
`google.cloud.connectors.v1.Connectors.GetConnectorVersion`  
`google.cloud.connectors.v1.Connectors.GetEndpointAttachment`  
`google.cloud.connectors.v1.Connectors.GetEventSubscription`  
`google.cloud.connectors.v1.Connectors.GetEventType`  
`google.cloud.connectors.v1.Connectors.GetGlobalSettings`  
`google.cloud.connectors.v1.Connectors.GetManagedZone`  
`google.cloud.connectors.v1.Connectors.GetProvider`  
`google.cloud.connectors.v1.Connectors.GetRegionalSettings`  
`google.cloud.connectors.v1.Connectors.GetRuntimeConfig`  
`google.cloud.connectors.v1.Connectors.ListConnections`  
`google.cloud.connectors.v1.Connectors.ListConnectorVersions`  
`google.cloud.connectors.v1.Connectors.ListConnectors`  
`google.cloud.connectors.v1.Connectors.ListEndpointAttachments`  
`google.cloud.connectors.v1.Connectors.ListEventSubscriptions`  
`google.cloud.connectors.v1.Connectors.ListEventTypes`  
`google.cloud.connectors.v1.Connectors.ListManagedZones`  
`google.cloud.connectors.v1.Connectors.ListProviders`  
`google.cloud.connectors.v1.Connectors.SearchConnections`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.connectors.v1.Connectors.CreateConnection` (LRO)  
`google.cloud.connectors.v1.Connectors.CreateEndpointAttachment` (LRO)  
`google.cloud.connectors.v1.Connectors.CreateEventSubscription` (LRO)  
`google.cloud.connectors.v1.Connectors.CreateManagedZone` (LRO)  
`google.cloud.connectors.v1.Connectors.DeleteConnection` (LRO)  
`google.cloud.connectors.v1.Connectors.DeleteEndpointAttachment` (LRO)  
`google.cloud.connectors.v1.Connectors.DeleteEventSubscription` (LRO)  
`google.cloud.connectors.v1.Connectors.DeleteManagedZone` (LRO)  
`google.cloud.connectors.v1.Connectors.RepairEventing` (LRO)  
`google.cloud.connectors.v1.Connectors.RetryEventSubscription` (LRO)  
`google.cloud.connectors.v1.Connectors.UpdateConnection` (LRO)  
`google.cloud.connectors.v1.Connectors.UpdateEndpointAttachment` (LRO)  
`google.cloud.connectors.v1.Connectors.UpdateEventSubscription` (LRO)  
`google.cloud.connectors.v1.Connectors.UpdateGlobalSettings` (LRO)  
`google.cloud.connectors.v1.Connectors.UpdateManagedZone` (LRO)  
`google.cloud.connectors.v1.Connectors.UpdateRegionalSettings` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `cloud.connectors.runtime.v2.EntityService.GetEntity`  
`google.cloud.connectors.v1.Connectors.GetAction` (LRO)  
`google.cloud.connectors.v1.Connectors.GetConnectionSchemaMetadata`  
`google.cloud.connectors.v1.Connectors.GetEntityType` (LRO)  
`google.cloud.connectors.v1.Connectors.ListActions`  
`google.cloud.connectors.v1.Connectors.ListEntityTypes`  
`google.cloud.connectors.v1.Connectors.ListRuntimeActionSchemas`  
`google.cloud.connectors.v1.Connectors.ListRuntimeEntitySchemas`  
`DATA_WRITE` | `cloud.connectors.runtime.v2.ActionService.ExecuteAction`  
`cloud.connectors.runtime.v2.EntityService.CreateEntity`  
`cloud.connectors.runtime.v2.EntityService.DeleteEntitiesWithConditions`  
`cloud.connectors.runtime.v2.EntityService.DeleteEntity`  
`cloud.connectors.runtime.v2.EntityService.UpdateEntitiesWithConditions`  
`cloud.connectors.runtime.v2.EntityService.UpdateEntity`  
`google.cloud.connectors.v1.Connectors.RefreshConnectionSchemaMetadata` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Integration Connectors.

### `cloud.connectors.runtime.v2.ActionService`

The following audit logs are associated with methods belonging to `cloud.connectors.runtime.v2.ActionService`.

#### `ExecuteAction`

  * **Method** : `cloud.connectors.runtime.v2.ActionService.ExecuteAction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/actions.execute - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.ActionService.ExecuteAction" `  




#### `GetAction`

  * **Method** : `cloud.connectors.runtime.v2.ActionService.GetAction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/actions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.ActionService.GetAction" `  




#### `ListActions`

  * **Method** : `cloud.connectors.runtime.v2.ActionService.ListActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/actions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.ActionService.ListActions" `  




### `cloud.connectors.runtime.v2.EntityService`

The following audit logs are associated with methods belonging to `cloud.connectors.runtime.v2.EntityService`.

#### `CreateEntity`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.CreateEntity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entities.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.CreateEntity" `  




#### `DeleteEntitiesWithConditions`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.DeleteEntitiesWithConditions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entities.deleteEntitiesWithConditions - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.DeleteEntitiesWithConditions" `  




#### `DeleteEntity`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.DeleteEntity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entities.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.DeleteEntity" `  




#### `GetEntity`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.GetEntity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entities.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.GetEntity" `  




#### `GetEntityType`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.GetEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entityTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.GetEntityType" `  




#### `ListEntities`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.ListEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entities.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.ListEntities" `  




#### `ListEntityTypes`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.ListEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entityTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.ListEntityTypes" `  




#### `UpdateEntitiesWithConditions`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.UpdateEntitiesWithConditions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entities.updateEntitiesWithConditions - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.UpdateEntitiesWithConditions" `  




#### `UpdateEntity`

  * **Method** : `cloud.connectors.runtime.v2.EntityService.UpdateEntity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.googleapis.com/entities.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="cloud.connectors.runtime.v2.EntityService.UpdateEntity" `  




### `google.cloud.connectors.v1.Connectors`

The following audit logs are associated with methods belonging to `google.cloud.connectors.v1.Connectors`.

#### `CreateConnection`

  * **Method** : `google.cloud.connectors.v1.Connectors.CreateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.connections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.CreateConnection" `  




#### `CreateEndpointAttachment`

  * **Method** : `google.cloud.connectors.v1.Connectors.CreateEndpointAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.endpointAttachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.CreateEndpointAttachment" `  




#### `CreateEventSubscription`

  * **Method** : `google.cloud.connectors.v1.Connectors.CreateEventSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.eventSubscriptions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.CreateEventSubscription" `  




#### `CreateManagedZone`

  * **Method** : `google.cloud.connectors.v1.Connectors.CreateManagedZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.managedZones.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.CreateManagedZone" `  




#### `DeleteConnection`

  * **Method** : `google.cloud.connectors.v1.Connectors.DeleteConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.connections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.DeleteConnection" `  




#### `DeleteEndpointAttachment`

  * **Method** : `google.cloud.connectors.v1.Connectors.DeleteEndpointAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.endpointAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.DeleteEndpointAttachment" `  




#### `DeleteEventSubscription`

  * **Method** : `google.cloud.connectors.v1.Connectors.DeleteEventSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.eventSubscriptions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.DeleteEventSubscription" `  




#### `DeleteManagedZone`

  * **Method** : `google.cloud.connectors.v1.Connectors.DeleteManagedZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.managedZones.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.DeleteManagedZone" `  




#### `GetAction`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetAction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.getRuntimeActionSchema - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetAction" `  




#### `GetConnection`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetConnection" `  




#### `GetConnectionSchemaMetadata`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetConnectionSchemaMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.getConnectionSchemaMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetConnectionSchemaMetadata" `  




#### `GetConnector`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetConnector" `  




#### `GetConnectorVersion`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetConnectorVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.versions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetConnectorVersion" `  




#### `GetEndpointAttachment`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetEndpointAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.endpointAttachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetEndpointAttachment" `  




#### `GetEntityType`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.getRuntimeEntitySchema - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetEntityType" `  




#### `GetEventSubscription`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetEventSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.eventSubscriptions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetEventSubscription" `  




#### `GetEventType`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetEventType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.eventtypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetEventType" `  




#### `GetGlobalSettings`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetGlobalSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.settings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetGlobalSettings" `  




#### `GetManagedZone`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetManagedZone`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.managedZones.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetManagedZone" `  




#### `GetProvider`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetProvider`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.providers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetProvider" `  




#### `GetRegionalSettings`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetRegionalSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.regionalSettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetRegionalSettings" `  




#### `GetRuntimeConfig`

  * **Method** : `google.cloud.connectors.v1.Connectors.GetRuntimeConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.runtimeconfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.GetRuntimeConfig" `  




#### `ListActions`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.getConnectionSchemaMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListActions" `  




#### `ListConnections`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListConnections" `  




#### `ListConnectorVersions`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListConnectorVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.versions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListConnectorVersions" `  




#### `ListConnectors`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListConnectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListConnectors" `  




#### `ListEndpointAttachments`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListEndpointAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.endpointAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListEndpointAttachments" `  




#### `ListEntityTypes`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.getConnectionSchemaMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListEntityTypes" `  




#### `ListEventSubscriptions`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListEventSubscriptions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.eventSubscriptions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListEventSubscriptions" `  




#### `ListEventTypes`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListEventTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.eventtypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListEventTypes" `  




#### `ListManagedZones`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListManagedZones`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.managedZones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListManagedZones" `  




#### `ListProviders`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListProviders`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.providers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListProviders" `  




#### `ListRuntimeActionSchemas`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListRuntimeActionSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.getRuntimeActionSchema - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListRuntimeActionSchemas" `  




#### `ListRuntimeEntitySchemas`

  * **Method** : `google.cloud.connectors.v1.Connectors.ListRuntimeEntitySchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.getRuntimeEntitySchema - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.ListRuntimeEntitySchemas" `  




#### `RefreshConnectionSchemaMetadata`

  * **Method** : `google.cloud.connectors.v1.Connectors.RefreshConnectionSchemaMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.schemaMetadata.refresh - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.RefreshConnectionSchemaMetadata" `  




#### `RepairEventing`

  * **Method** : `google.cloud.connectors.v1.Connectors.RepairEventing`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.eventSubscriptions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.RepairEventing" `  




#### `RetryEventSubscription`

  * **Method** : `google.cloud.connectors.v1.Connectors.RetryEventSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.eventSubscriptions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.RetryEventSubscription" `  




#### `SearchConnections`

  * **Method** : `google.cloud.connectors.v1.Connectors.SearchConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.SearchConnections" `  




#### `UpdateConnection`

  * **Method** : `google.cloud.connectors.v1.Connectors.UpdateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.connections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.UpdateConnection" `  




#### `UpdateEndpointAttachment`

  * **Method** : `google.cloud.connectors.v1.Connectors.UpdateEndpointAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.endpointAttachments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.UpdateEndpointAttachment" `  




#### `UpdateEventSubscription`

  * **Method** : `google.cloud.connectors.v1.Connectors.UpdateEventSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.eventSubscriptions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.UpdateEventSubscription" `  




#### `UpdateGlobalSettings`

  * **Method** : `google.cloud.connectors.v1.Connectors.UpdateGlobalSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.settings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.UpdateGlobalSettings" `  




#### `UpdateManagedZone`

  * **Method** : `google.cloud.connectors.v1.Connectors.UpdateManagedZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.managedZones.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.UpdateManagedZone" `  




#### `UpdateRegionalSettings`

  * **Method** : `google.cloud.connectors.v1.Connectors.UpdateRegionalSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.regionalSettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.connectors.v1.Connectors.UpdateRegionalSettings" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.connections.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.connections.setIamPolicy - ADMIN_WRITE`
    * `connectors.providers.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `connectors.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `connectors.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `cloud.connectors.runtime.v2.AdminService.CheckReadiness`
  * `cloud.connectors.runtime.v2.AdminService.CheckStatus`
  * `cloud.connectors.runtime.v2.AuthCodeFlowService.ExchangeAuthCode`
  * `cloud.connectors.runtime.v2.AuthCodeFlowService.RefreshAccessToken`
  * `google.cloud.connectors.v1.EventService.ListenEvent`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
