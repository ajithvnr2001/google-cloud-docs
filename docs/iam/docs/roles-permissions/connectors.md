---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/connectors/
title: Connectors roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:36.566974+00:00
---

# Connectors roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Connectors roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Connectors. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Connectors roles

Role | Permissions  
---|---  
  
#### Connector Admin 

(`roles/connectors.admin`) Full access to all resources of Connectors Service.  |  `connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.create` `connectors.connections.delete` `connectors.connections.executeSqlQuery` `connectors.connections.generateOpenAPISpec` `connectors.connections.get` `connectors.connections.getConnectionSchemaMetadata` `connectors.connections.getIamPolicy` `connectors.connections.getRuntimeActionSchema` `connectors.connections.getRuntimeEntitySchema` `connectors.connections.list` `connectors.connections.setIamPolicy` `connectors.connections.update` `connectors.connectors.*`

  * `connectors.connectors.get`
  * `connectors.connectors.list`

`connectors.customConnectorVersions.*`

  * `connectors.customConnectorVersions.create`
  * `connectors.customConnectorVersions.delete`
  * `connectors.customConnectorVersions.get`
  * `connectors.customConnectorVersions.getIamPolicy`
  * `connectors.customConnectorVersions.list`
  * `connectors.customConnectorVersions.setIamPolicy`
  * `connectors.customConnectorVersions.update`

`connectors.customConnectors.*`

  * `connectors.customConnectors.create`
  * `connectors.customConnectors.delete`
  * `connectors.customConnectors.get`
  * `connectors.customConnectors.getIamPolicy`
  * `connectors.customConnectors.list`
  * `connectors.customConnectors.setIamPolicy`
  * `connectors.customConnectors.update`

`connectors.endpointAttachments.*`

  * `connectors.endpointAttachments.create`
  * `connectors.endpointAttachments.delete`
  * `connectors.endpointAttachments.get`
  * `connectors.endpointAttachments.getIamPolicy`
  * `connectors.endpointAttachments.list`
  * `connectors.endpointAttachments.setIamPolicy`
  * `connectors.endpointAttachments.update`

`connectors.entities.*`

  * `connectors.entities.create`
  * `connectors.entities.delete`
  * `connectors.entities.deleteEntitiesWithConditions`
  * `connectors.entities.get`
  * `connectors.entities.list`
  * `connectors.entities.update`
  * `connectors.entities.updateEntitiesWithConditions`

`connectors.entityTypes.list` `connectors.eventSubscriptions.*`

  * `connectors.eventSubscriptions.create`
  * `connectors.eventSubscriptions.delete`
  * `connectors.eventSubscriptions.get`
  * `connectors.eventSubscriptions.list`
  * `connectors.eventSubscriptions.update`

`connectors.eventtypes.*`

  * `connectors.eventtypes.get`
  * `connectors.eventtypes.list`

`connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

`connectors.managedZones.*`

  * `connectors.managedZones.create`
  * `connectors.managedZones.delete`
  * `connectors.managedZones.get`
  * `connectors.managedZones.getIamPolicy`
  * `connectors.managedZones.list`
  * `connectors.managedZones.setIamPolicy`
  * `connectors.managedZones.update`

`connectors.operations.*`

  * `connectors.operations.cancel`
  * `connectors.operations.delete`
  * `connectors.operations.get`
  * `connectors.operations.list`

`connectors.providers.*`

  * `connectors.providers.get`
  * `connectors.providers.list`

`connectors.regionalSettings.*`

  * `connectors.regionalSettings.get`
  * `connectors.regionalSettings.update`

`connectors.runtimeconfig.get` `connectors.schemaMetadata.refresh` `connectors.settings.*`

  * `connectors.settings.get`
  * `connectors.settings.update`

`connectors.versions.*`

  * `connectors.versions.get`
  * `connectors.versions.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `secretmanager.secrets.getIamPolicy`  
  
#### Connectors Editor 

(`roles/connectors.editor`) Editor role for connectors  |  `connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.create` `connectors.connections.delete` `connectors.connections.executeSqlQuery` `connectors.connections.generateOpenAPISpec` `connectors.connections.get` `connectors.connections.getConnectionSchemaMetadata` `connectors.connections.getIamPolicy` `connectors.connections.getRuntimeActionSchema` `connectors.connections.getRuntimeEntitySchema` `connectors.connections.list` `connectors.connections.listenEvent` `connectors.connections.update` `connectors.connectors.*`

  * `connectors.connectors.get`
  * `connectors.connectors.list`

`connectors.customConnectorVersions.create` `connectors.customConnectorVersions.delete` `connectors.customConnectorVersions.get` `connectors.customConnectorVersions.getIamPolicy` `connectors.customConnectorVersions.list` `connectors.customConnectorVersions.update` `connectors.customConnectors.create` `connectors.customConnectors.delete` `connectors.customConnectors.get` `connectors.customConnectors.getIamPolicy` `connectors.customConnectors.list` `connectors.customConnectors.update` `connectors.endpointAttachments.create` `connectors.endpointAttachments.delete` `connectors.endpointAttachments.get` `connectors.endpointAttachments.getIamPolicy` `connectors.endpointAttachments.list` `connectors.endpointAttachments.update` `connectors.entities.*`

  * `connectors.entities.create`
  * `connectors.entities.delete`
  * `connectors.entities.deleteEntitiesWithConditions`
  * `connectors.entities.get`
  * `connectors.entities.list`
  * `connectors.entities.update`
  * `connectors.entities.updateEntitiesWithConditions`

`connectors.entityTypes.list` `connectors.eventSubscriptions.*`

  * `connectors.eventSubscriptions.create`
  * `connectors.eventSubscriptions.delete`
  * `connectors.eventSubscriptions.get`
  * `connectors.eventSubscriptions.list`
  * `connectors.eventSubscriptions.update`

`connectors.eventtypes.*`

  * `connectors.eventtypes.get`
  * `connectors.eventtypes.list`

`connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

`connectors.managedZones.create` `connectors.managedZones.delete` `connectors.managedZones.get` `connectors.managedZones.getIamPolicy` `connectors.managedZones.list` `connectors.managedZones.update` `connectors.operations.*`

  * `connectors.operations.cancel`
  * `connectors.operations.delete`
  * `connectors.operations.get`
  * `connectors.operations.list`

`connectors.providers.*`

  * `connectors.providers.get`
  * `connectors.providers.list`

`connectors.regionalSettings.*`

  * `connectors.regionalSettings.get`
  * `connectors.regionalSettings.update`

`connectors.runtimeconfig.get` `connectors.schemaMetadata.refresh` `connectors.settings.*`

  * `connectors.settings.get`
  * `connectors.settings.update`

`connectors.versions.*`

  * `connectors.versions.get`
  * `connectors.versions.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Connectors Viewer 

(`roles/connectors.viewer`) Read-only access to Connectors all resources.  |  `connectors.actions.list` `connectors.connections.generateOpenAPISpec` `connectors.connections.get` `connectors.connections.getConnectionSchemaMetadata` `connectors.connections.getIamPolicy` `connectors.connections.getRuntimeActionSchema` `connectors.connections.getRuntimeEntitySchema` `connectors.connections.list` `connectors.connectors.*`

  * `connectors.connectors.get`
  * `connectors.connectors.list`

`connectors.customConnectorVersions.get` `connectors.customConnectorVersions.getIamPolicy` `connectors.customConnectorVersions.list` `connectors.customConnectors.get` `connectors.customConnectors.getIamPolicy` `connectors.customConnectors.list` `connectors.endpointAttachments.get` `connectors.endpointAttachments.getIamPolicy` `connectors.endpointAttachments.list` `connectors.entities.get` `connectors.entities.list` `connectors.entityTypes.list` `connectors.eventSubscriptions.get` `connectors.eventSubscriptions.list` `connectors.eventtypes.*`

  * `connectors.eventtypes.get`
  * `connectors.eventtypes.list`

`connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

`connectors.managedZones.get` `connectors.managedZones.getIamPolicy` `connectors.managedZones.list` `connectors.operations.get` `connectors.operations.list` `connectors.providers.*`

  * `connectors.providers.get`
  * `connectors.providers.list`

`connectors.regionalSettings.get` `connectors.runtimeconfig.get` `connectors.settings.get` `connectors.versions.*`

  * `connectors.versions.get`
  * `connectors.versions.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Custom Connectors Admin 

(`roles/connectors.customConnectorAdmin`) Custom Connector is a global resource which creates custom connector within the given target project. This role grants Admin access to Custom Connector resources  |  `connectors.customConnectorVersions.*`

  * `connectors.customConnectorVersions.create`
  * `connectors.customConnectorVersions.delete`
  * `connectors.customConnectorVersions.get`
  * `connectors.customConnectorVersions.getIamPolicy`
  * `connectors.customConnectorVersions.list`
  * `connectors.customConnectorVersions.setIamPolicy`
  * `connectors.customConnectorVersions.update`

`connectors.customConnectors.*`

  * `connectors.customConnectors.create`
  * `connectors.customConnectors.delete`
  * `connectors.customConnectors.get`
  * `connectors.customConnectors.getIamPolicy`
  * `connectors.customConnectors.list`
  * `connectors.customConnectors.setIamPolicy`
  * `connectors.customConnectors.update`

`connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

  
  
#### Custom Connector Viewer 

(`roles/connectors.customConnectorViewer`) Custom Connector is a global resource which creates custom connector within the given target project. This role grants Read-only access to Custom Connector & Custom Connector Version resources.  |  `connectors.customConnectorVersions.get` `connectors.customConnectorVersions.getIamPolicy` `connectors.customConnectorVersions.list` `connectors.customConnectors.get` `connectors.customConnectors.getIamPolicy` `connectors.customConnectors.list` `connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

  
  
#### Connectors Endpoint Attachment Admin 

(`roles/connectors.endpointAttachmentAdmin`) Endpoint Attachment is a regional resource which creates PSC connection endpoint for the given PSC Service Attachment. This role grants Admin access to Connectors Endpoint Attachment resources.  |  `connectors.endpointAttachments.*`

  * `connectors.endpointAttachments.create`
  * `connectors.endpointAttachments.delete`
  * `connectors.endpointAttachments.get`
  * `connectors.endpointAttachments.getIamPolicy`
  * `connectors.endpointAttachments.list`
  * `connectors.endpointAttachments.setIamPolicy`
  * `connectors.endpointAttachments.update`

`connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

  
  
#### Connectors Endpoint Attachment Viewer 

(`roles/connectors.endpointAttachmentViewer`) Endpoint Attachment is a regional resource which creates PSC connection endpoint for the given PSC Service Attachment. This role grants Read-only access to Connectors Endpoint Attachment resources  |  `connectors.endpointAttachments.get` `connectors.endpointAttachments.getIamPolicy` `connectors.endpointAttachments.list` `connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

  
  
#### Connectors Event Subscriptions Admin 

(`roles/connectors.eventSubscriptionAdmin`) Event Subscription is a regional resource which creates subscriptions on events for a given connection within the given target project. This role grants Admin access to Connectors Subscription resources  |  `connectors.eventSubscriptions.*`

  * `connectors.eventSubscriptions.create`
  * `connectors.eventSubscriptions.delete`
  * `connectors.eventSubscriptions.get`
  * `connectors.eventSubscriptions.list`
  * `connectors.eventSubscriptions.update`

  
  
#### Connectors Event Subscriptions Viewer 

(`roles/connectors.eventSubscriptionViewer`) Event Subscription is a regional resource which creates subscriptions on events for a given connection within the given target project. This role grants Read-only access to Event Subscription resources.  |  `connectors.eventSubscriptions.get` `connectors.eventSubscriptions.list`  
  
#### Connector Invoker 

(`roles/connectors.invoker`) Full Access to invoke all operations on Connections.  |  `connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.executeSqlQuery` `connectors.entities.*`

  * `connectors.entities.create`
  * `connectors.entities.delete`
  * `connectors.entities.deleteEntitiesWithConditions`
  * `connectors.entities.get`
  * `connectors.entities.list`
  * `connectors.entities.update`
  * `connectors.entities.updateEntitiesWithConditions`

`connectors.entityTypes.list`  
  
#### Connector Event Listener 

(`roles/connectors.listener`) Full Access to listen events by connections.  |  `connectors.connections.listenEvent`  
  
#### Connectors Managed Zone Admin 

(`roles/connectors.managedZoneAdmin`) Managed Zone is a global resource which creates Cloud DNS Peering Zone with the given target project. This role grants Admin access to Connectors Managed Zone resources  |  `connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

`connectors.managedZones.*`

  * `connectors.managedZones.create`
  * `connectors.managedZones.delete`
  * `connectors.managedZones.get`
  * `connectors.managedZones.getIamPolicy`
  * `connectors.managedZones.list`
  * `connectors.managedZones.setIamPolicy`
  * `connectors.managedZones.update`

  
  
#### Connectors Managed Zone Viewer 

(`roles/connectors.managedZoneViewer`) Managed Zone is a global resource which creates Cloud DNS Peering Zone with the given target project. This role grants Read-only access to Connectors Managed Zone resources.  |  `connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

`connectors.managedZones.get` `connectors.managedZones.getIamPolicy` `connectors.managedZones.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Connectors Platform Service Agent 

(`roles/connectors.serviceAgent`) Grants Connectors Platform service account to manage customer resources  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.get` `connectors.connections.getConnectionSchemaMetadata` `connectors.connections.list` `connectors.connectors.*`

  * `connectors.connectors.get`
  * `connectors.connectors.list`

`connectors.customConnectorVersions.get` `connectors.customConnectorVersions.list` `connectors.customConnectors.get` `connectors.customConnectors.list` `connectors.endpointAttachments.get` `connectors.endpointAttachments.list` `connectors.entities.get` `connectors.entityTypes.list` `connectors.eventSubscriptions.get` `connectors.eventSubscriptions.list` `connectors.eventtypes.*`

  * `connectors.eventtypes.get`
  * `connectors.eventtypes.list`

`connectors.locations.*`

  * `connectors.locations.get`
  * `connectors.locations.list`

`connectors.managedZones.get` `connectors.managedZones.list` `connectors.providers.*`

  * `connectors.providers.get`
  * `connectors.providers.list`

`connectors.runtimeconfig.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.implicitDelegation` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create`  
  
## Connectors permissions

Permission | Included in roles  
---|---  
  
#### `connectors.actions.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.actions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.connections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)   
  
#### `connectors.connections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)   
  
#### `connectors.connections.executeSqlQuery`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.connections.generateOpenAPISpec`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `connectors.connections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.connections.getConnectionSchemaMetadata`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.connections.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.connections.getRuntimeActionSchema`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.connections.getRuntimeEntitySchema`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.connections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.connections.listenEvent`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connector Event Listener](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.listener) (`roles/connectors.listener`)   
  
#### `connectors.connections.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `connectors.connections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)   
  
#### `connectors.connectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.connectors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.customConnectorVersions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)   
  
#### `connectors.customConnectorVersions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)   
  
#### `connectors.customConnectorVersions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)  [Custom Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorViewer) (`roles/connectors.customConnectorViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.customConnectorVersions.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)  [Custom Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorViewer) (`roles/connectors.customConnectorViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.customConnectorVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)  [Custom Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorViewer) (`roles/connectors.customConnectorViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.customConnectorVersions.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)   
  
#### `connectors.customConnectorVersions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)   
  
#### `connectors.customConnectors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)   
  
#### `connectors.customConnectors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)   
  
#### `connectors.customConnectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)  [Custom Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorViewer) (`roles/connectors.customConnectorViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.customConnectors.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)  [Custom Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorViewer) (`roles/connectors.customConnectorViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.customConnectors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)  [Custom Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorViewer) (`roles/connectors.customConnectorViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.customConnectors.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)   
  
#### `connectors.customConnectors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)   
  
#### `connectors.endpointAttachments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)   
  
#### `connectors.endpointAttachments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)   
  
#### `connectors.endpointAttachments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)  [Connectors Endpoint Attachment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentViewer) (`roles/connectors.endpointAttachmentViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.endpointAttachments.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)  [Connectors Endpoint Attachment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentViewer) (`roles/connectors.endpointAttachmentViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.endpointAttachments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)  [Connectors Endpoint Attachment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentViewer) (`roles/connectors.endpointAttachmentViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.endpointAttachments.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)   
  
#### `connectors.endpointAttachments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)   
  
#### `connectors.entities.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.entities.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.entities.deleteEntitiesWithConditions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.entities.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.entities.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.entities.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.entities.updateEntitiesWithConditions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.entityTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.invoker) (`roles/connectors.invoker`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `connectors.eventSubscriptions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Event Subscriptions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.eventSubscriptionAdmin) (`roles/connectors.eventSubscriptionAdmin`)   
  
#### `connectors.eventSubscriptions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Event Subscriptions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.eventSubscriptionAdmin) (`roles/connectors.eventSubscriptionAdmin`)   
  
#### `connectors.eventSubscriptions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Connectors Event Subscriptions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.eventSubscriptionAdmin) (`roles/connectors.eventSubscriptionAdmin`)  [Connectors Event Subscriptions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.eventSubscriptionViewer) (`roles/connectors.eventSubscriptionViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.eventSubscriptions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connectors Event Subscriptions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.eventSubscriptionAdmin) (`roles/connectors.eventSubscriptionAdmin`)  [Connectors Event Subscriptions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.eventSubscriptionViewer) (`roles/connectors.eventSubscriptionViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.eventSubscriptions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Event Subscriptions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.eventSubscriptionAdmin) (`roles/connectors.eventSubscriptionAdmin`)   
  
#### `connectors.eventtypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.eventtypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)  [Custom Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorViewer) (`roles/connectors.customConnectorViewer`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)  [Connectors Endpoint Attachment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentViewer) (`roles/connectors.endpointAttachmentViewer`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)  [Connectors Managed Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneViewer) (`roles/connectors.managedZoneViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Custom Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorAdmin) (`roles/connectors.customConnectorAdmin`)  [Custom Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.customConnectorViewer) (`roles/connectors.customConnectorViewer`)  [Connectors Endpoint Attachment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentAdmin) (`roles/connectors.endpointAttachmentAdmin`)  [Connectors Endpoint Attachment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.endpointAttachmentViewer) (`roles/connectors.endpointAttachmentViewer`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)  [Connectors Managed Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneViewer) (`roles/connectors.managedZoneViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.managedZones.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)   
  
#### `connectors.managedZones.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)   
  
#### `connectors.managedZones.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)  [Connectors Managed Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneViewer) (`roles/connectors.managedZoneViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.managedZones.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)  [Connectors Managed Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneViewer) (`roles/connectors.managedZoneViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.managedZones.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)  [Connectors Managed Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneViewer) (`roles/connectors.managedZoneViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.managedZones.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)   
  
#### `connectors.managedZones.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Managed Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.managedZoneAdmin) (`roles/connectors.managedZoneAdmin`)   
  
#### `connectors.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)   
  
#### `connectors.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)   
  
#### `connectors.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `connectors.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.providers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.providers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.regionalSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.regionalSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)   
  
#### `connectors.runtimeconfig.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Connectors Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.serviceAgent) (`roles/connectors.serviceAgent`) 

  
  
#### `connectors.schemaMetadata.refresh`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)   
  
#### `connectors.settings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `connectors.settings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)   
  
#### `connectors.versions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `connectors.versions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.editor) (`roles/connectors.editor`)  [Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.viewer) (`roles/connectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
