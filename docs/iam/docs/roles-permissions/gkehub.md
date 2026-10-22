---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub/
title: GKE Hub roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:35.342472+00:00
---

# GKE Hub roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  GKE Hub roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for GKE Hub. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## GKE Hub roles

Role | Permissions  
---|---  
  
#### Fleet Admin (formerly GKE Hub Admin) 

(`roles/gkehub.admin`) Full access to Fleet resources.  |  `gkehub.endpoints.connect` `gkehub.features.*`

  * `gkehub.features.create`
  * `gkehub.features.delete`
  * `gkehub.features.get`
  * `gkehub.features.getIamPolicy`
  * `gkehub.features.list`
  * `gkehub.features.setIamPolicy`
  * `gkehub.features.update`

`gkehub.fleet.*`

  * `gkehub.fleet.create`
  * `gkehub.fleet.createFreeTrial`
  * `gkehub.fleet.delete`
  * `gkehub.fleet.get`
  * `gkehub.fleet.getFreeTrial`
  * `gkehub.fleet.update`
  * `gkehub.fleet.updateFreeTrial`

`gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.membershipbindings.*`

  * `gkehub.membershipbindings.create`
  * `gkehub.membershipbindings.delete`
  * `gkehub.membershipbindings.get`
  * `gkehub.membershipbindings.list`
  * `gkehub.membershipbindings.update`

`gkehub.membershipfeatures.*`

  * `gkehub.membershipfeatures.create`
  * `gkehub.membershipfeatures.delete`
  * `gkehub.membershipfeatures.get`
  * `gkehub.membershipfeatures.list`
  * `gkehub.membershipfeatures.update`

`gkehub.memberships.*`

  * `gkehub.memberships.create`
  * `gkehub.memberships.delete`
  * `gkehub.memberships.generateConnectManifest`
  * `gkehub.memberships.get`
  * `gkehub.memberships.getIamPolicy`
  * `gkehub.memberships.list`
  * `gkehub.memberships.setIamPolicy`
  * `gkehub.memberships.update`

`gkehub.namespaces.*`

  * `gkehub.namespaces.create`
  * `gkehub.namespaces.delete`
  * `gkehub.namespaces.get`
  * `gkehub.namespaces.list`
  * `gkehub.namespaces.update`

`gkehub.operations.*`

  * `gkehub.operations.cancel`
  * `gkehub.operations.delete`
  * `gkehub.operations.get`
  * `gkehub.operations.list`

`gkehub.rbacrolebindings.*`

  * `gkehub.rbacrolebindings.create`
  * `gkehub.rbacrolebindings.delete`
  * `gkehub.rbacrolebindings.get`
  * `gkehub.rbacrolebindings.list`
  * `gkehub.rbacrolebindings.update`

`gkehub.scopes.*`

  * `gkehub.scopes.create`
  * `gkehub.scopes.delete`
  * `gkehub.scopes.get`
  * `gkehub.scopes.getIamPolicy`
  * `gkehub.scopes.list`
  * `gkehub.scopes.listBoundMemberships`
  * `gkehub.scopes.setIamPolicy`
  * `gkehub.scopes.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Fleet Editor (formerly GKE Hub Editor) 

(`roles/gkehub.editor`) Edit access to Fleet resources.  |  `gkehub.features.create` `gkehub.features.delete` `gkehub.features.get` `gkehub.features.getIamPolicy` `gkehub.features.list` `gkehub.features.update` `gkehub.fleet.*`

  * `gkehub.fleet.create`
  * `gkehub.fleet.createFreeTrial`
  * `gkehub.fleet.delete`
  * `gkehub.fleet.get`
  * `gkehub.fleet.getFreeTrial`
  * `gkehub.fleet.update`
  * `gkehub.fleet.updateFreeTrial`

`gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.membershipbindings.*`

  * `gkehub.membershipbindings.create`
  * `gkehub.membershipbindings.delete`
  * `gkehub.membershipbindings.get`
  * `gkehub.membershipbindings.list`
  * `gkehub.membershipbindings.update`

`gkehub.membershipfeatures.*`

  * `gkehub.membershipfeatures.create`
  * `gkehub.membershipfeatures.delete`
  * `gkehub.membershipfeatures.get`
  * `gkehub.membershipfeatures.list`
  * `gkehub.membershipfeatures.update`

`gkehub.memberships.create` `gkehub.memberships.delete` `gkehub.memberships.generateConnectManifest` `gkehub.memberships.get` `gkehub.memberships.getIamPolicy` `gkehub.memberships.list` `gkehub.memberships.update` `gkehub.namespaces.*`

  * `gkehub.namespaces.create`
  * `gkehub.namespaces.delete`
  * `gkehub.namespaces.get`
  * `gkehub.namespaces.list`
  * `gkehub.namespaces.update`

`gkehub.operations.*`

  * `gkehub.operations.cancel`
  * `gkehub.operations.delete`
  * `gkehub.operations.get`
  * `gkehub.operations.list`

`gkehub.rbacrolebindings.*`

  * `gkehub.rbacrolebindings.create`
  * `gkehub.rbacrolebindings.delete`
  * `gkehub.rbacrolebindings.get`
  * `gkehub.rbacrolebindings.list`
  * `gkehub.rbacrolebindings.update`

`gkehub.scopes.create` `gkehub.scopes.delete` `gkehub.scopes.get` `gkehub.scopes.getIamPolicy` `gkehub.scopes.list` `gkehub.scopes.listBoundMemberships` `gkehub.scopes.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Fleet Viewer (formerly GKE Hub Viewer) 

(`roles/gkehub.viewer`) Read-only access to Fleets and related resources.  |  `gkehub.features.get` `gkehub.features.getIamPolicy` `gkehub.features.list` `gkehub.fleet.get` `gkehub.fleet.getFreeTrial` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.membershipbindings.get` `gkehub.membershipbindings.list` `gkehub.membershipfeatures.get` `gkehub.membershipfeatures.list` `gkehub.memberships.generateConnectManifest` `gkehub.memberships.get` `gkehub.memberships.getIamPolicy` `gkehub.memberships.list` `gkehub.namespaces.get` `gkehub.namespaces.list` `gkehub.operations.get` `gkehub.operations.list` `gkehub.rbacrolebindings.get` `gkehub.rbacrolebindings.list` `gkehub.scopes.get` `gkehub.scopes.getIamPolicy` `gkehub.scopes.list` `gkehub.scopes.listBoundMemberships` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GKE Connect Agent 

(`roles/gkehub.connect`) Ability to set up GKE Connect between external clusters and Google.  |  `gkehub.endpoints.connect`  
  
#### Connect Gateway Admin 

(`roles/gkehub.gatewayAdmin`) Full access to Connect Gateway.  |  `gkehub.gateway.*`

  * `gkehub.gateway.delete`
  * `gkehub.gateway.generateCredentials`
  * `gkehub.gateway.get`
  * `gkehub.gateway.patch`
  * `gkehub.gateway.post`
  * `gkehub.gateway.put`
  * `gkehub.gateway.stream`

`gkehub.memberships.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Connect Gateway Editor 

(`roles/gkehub.gatewayEditor`) Edit access to Connect Gateway.  |  `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.memberships.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Connect Gateway Reader 

(`roles/gkehub.gatewayReader`) Read-only access to Connect Gateway.  |  `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.memberships.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Fleet Scope Admin 

(`roles/gkehub.scopeAdmin`) Admin access to Fleet Scopes to set IAM Bindings and RBACRoleBindings.  |  `gkehub.namespaces.create` `gkehub.namespaces.delete` `gkehub.namespaces.get` `gkehub.namespaces.list` `gkehub.rbacrolebindings.*`

  * `gkehub.rbacrolebindings.create`
  * `gkehub.rbacrolebindings.delete`
  * `gkehub.rbacrolebindings.get`
  * `gkehub.rbacrolebindings.list`
  * `gkehub.rbacrolebindings.update`

`gkehub.scopes.get` `gkehub.scopes.getIamPolicy` `gkehub.scopes.listBoundMemberships` `gkehub.scopes.setIamPolicy`  
  
#### Fleet Scope Editor 

(`roles/gkehub.scopeEditor`) Edit access to Namespaces under Fleet Scopes.  |  `gkehub.namespaces.create` `gkehub.namespaces.delete` `gkehub.namespaces.get` `gkehub.namespaces.list` `gkehub.rbacrolebindings.get` `gkehub.rbacrolebindings.list` `gkehub.scopes.get` `gkehub.scopes.getIamPolicy` `gkehub.scopes.listBoundMemberships`  
  
#### Fleet Project-level Scope Editor 

(`roles/gkehub.scopeEditorProjectLevel`) Role for project-level permissions for editor of Fleet Scopes.  |  `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.memberships.get` `gkehub.operations.get` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Fleet Scope Viewer 

(`roles/gkehub.scopeViewer`) Viewer of Fleet Scopes and associated resources.  |  `gkehub.namespaces.get` `gkehub.namespaces.list` `gkehub.rbacrolebindings.get` `gkehub.rbacrolebindings.list` `gkehub.scopes.get` `gkehub.scopes.getIamPolicy` `gkehub.scopes.listBoundMemberships`  
  
#### Fleet Project-level Scope Viewer 

(`roles/gkehub.scopeViewerProjectLevel`) Role for project-level permissions for viewer of Fleet Scopes.  |  `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.memberships.get` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### GKE Hub Cross Project Service Agent 

(`roles/gkehub.crossProjectServiceAgent`) Gives the GKE Hub service agent permission to manage the project for cross-project fleet registration.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.setIamPolicy`  
  
#### GKE Hub Service Agent 

(`roles/gkehub.serviceAgent`) Gives the GKE Hub service agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `container.clusterRoleBindings.*`

  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`

`container.clusterRoles.*`

  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`

`container.clusters.connect` `container.clusters.get` `container.clusters.list` `container.clusters.update` `container.customResourceDefinitions.create` `container.customResourceDefinitions.delete` `container.customResourceDefinitions.get` `container.customResourceDefinitions.list` `container.customResourceDefinitions.update` `container.namespaces.get` `container.operations.get` `container.thirdPartyObjects.*`

  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`

`gkehub.features.create` `gkehub.features.get` `gkehub.features.list` `gkehub.fleet.create` `gkehub.fleet.get` `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.create` `gkehub.memberships.generateConnectManifest` `gkehub.memberships.get` `gkehub.memberships.list` `gkehub.operations.get` `gkemulticloud.awsClusters.get` `gkemulticloud.azureClusters.get` `gkeonprem.bareMetalClusters.get` `gkeonprem.vmwareClusters.get` `logging.buckets.create` `logging.buckets.get` `logging.buckets.list` `logging.buckets.update` `logging.exclusions.*`

  * `logging.exclusions.create`
  * `logging.exclusions.delete`
  * `logging.exclusions.get`
  * `logging.exclusions.list`
  * `logging.exclusions.update`

`logging.sinks.*`

  * `logging.sinks.create`
  * `logging.sinks.delete`
  * `logging.sinks.get`
  * `logging.sinks.list`
  * `logging.sinks.update`

`logging.views.create` `logging.views.get` `logging.views.list` `logging.views.update` `monitoring.metricsScopes.link` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## GKE Hub permissions

Permission | Included in roles  
---|---  
  
#### `gkehub.endpoints.connect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Velostrata Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.inframanager) (`roles/cloudmigration.inframanager`)  [Velostrata Manager Connection Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudmigration#cloudmigration.velostrataconnect) (`roles/cloudmigration.velostrataconnect`)  [GKE Connect Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.connect) (`roles/gkehub.connect`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.features.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.features.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.features.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthos#anthos.serviceAgent) (`roles/anthos.serviceAgent`) 
  * [Anthos Audit Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosaudit#anthosaudit.serviceAgent) (`roles/anthosaudit.serviceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `gkehub.features.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.features.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.features.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.features.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.fleet.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `gkehub.fleet.createFreeTrial`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.fleet.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.fleet.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `gkehub.fleet.getFreeTrial`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.fleet.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.fleet.updateFreeTrial`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.gateway.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connect Gateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`)  [Connect Gateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayEditor) (`roles/gkehub.gatewayEditor`)  [Fleet Project-level Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) (`roles/gkehub.scopeEditorProjectLevel`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `gkehub.gateway.generateCredentials`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connect Gateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`)  [Connect Gateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayEditor) (`roles/gkehub.gatewayEditor`)  [Connect Gateway Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayReader) (`roles/gkehub.gatewayReader`)  [Fleet Project-level Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) (`roles/gkehub.scopeEditorProjectLevel`)  [Fleet Project-level Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewerProjectLevel) (`roles/gkehub.scopeViewerProjectLevel`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `gkehub.gateway.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connect Gateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`)  [Connect Gateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayEditor) (`roles/gkehub.gatewayEditor`)  [Connect Gateway Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayReader) (`roles/gkehub.gatewayReader`)  [Fleet Project-level Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) (`roles/gkehub.scopeEditorProjectLevel`)  [Fleet Project-level Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewerProjectLevel) (`roles/gkehub.scopeViewerProjectLevel`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `gkehub.gateway.patch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connect Gateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`)  [Connect Gateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayEditor) (`roles/gkehub.gatewayEditor`)  [Fleet Project-level Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) (`roles/gkehub.scopeEditorProjectLevel`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `gkehub.gateway.post`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connect Gateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`)  [Connect Gateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayEditor) (`roles/gkehub.gatewayEditor`)  [Fleet Project-level Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) (`roles/gkehub.scopeEditorProjectLevel`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `gkehub.gateway.put`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connect Gateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`)  [Connect Gateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayEditor) (`roles/gkehub.gatewayEditor`)  [Fleet Project-level Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) (`roles/gkehub.scopeEditorProjectLevel`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `gkehub.gateway.stream`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connect Gateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthos#anthos.serviceAgent) (`roles/anthos.serviceAgent`) 
  * [Anthos Audit Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosaudit#anthosaudit.serviceAgent) (`roles/anthosaudit.serviceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `gkehub.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthos#anthos.serviceAgent) (`roles/anthos.serviceAgent`) 
  * [Anthos Audit Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosaudit#anthosaudit.serviceAgent) (`roles/anthosaudit.serviceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `gkehub.membershipbindings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.membershipbindings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.membershipbindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.membershipbindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.membershipbindings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.membershipfeatures.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.membershipfeatures.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.membershipfeatures.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.membershipfeatures.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.membershipfeatures.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.memberships.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.memberships.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.memberships.generateConnectManifest`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.memberships.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Connect Gateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayAdmin) (`roles/gkehub.gatewayAdmin`)  [Connect Gateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayEditor) (`roles/gkehub.gatewayEditor`)  [Connect Gateway Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.gatewayReader) (`roles/gkehub.gatewayReader`)  [Fleet Project-level Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) (`roles/gkehub.scopeEditorProjectLevel`)  [Fleet Project-level Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewerProjectLevel) (`roles/gkehub.scopeViewerProjectLevel`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthos#anthos.serviceAgent) (`roles/anthos.serviceAgent`) 
  * [Anthos Audit Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosaudit#anthosaudit.serviceAgent) (`roles/anthosaudit.serviceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Config Delivery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.serviceAgent) (`roles/configdelivery.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `gkehub.memberships.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.memberships.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Online Prediction Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.onlinePredictionServiceAgent) (`roles/aiplatform.onlinePredictionServiceAgent`) 
  * [Anthos Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthos#anthos.serviceAgent) (`roles/anthos.serviceAgent`) 
  * [Anthos Audit Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosaudit#anthosaudit.serviceAgent) (`roles/anthosaudit.serviceAgent`) 
  * [Anthos Config Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosconfigmanagement#anthosconfigmanagement.serviceAgent) (`roles/anthosconfigmanagement.serviceAgent`) 
  * [Anthos Identity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosidentityservice#anthosidentityservice.serviceAgent) (`roles/anthosidentityservice.serviceAgent`) 
  * [Anthos Policy Controller Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthospolicycontroller#anthospolicycontroller.serviceAgent) (`roles/anthospolicycontroller.serviceAgent`) 
  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [App Development Experience Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appdevelopmentexperience#appdevelopmentexperience.serviceAgent) (`roles/appdevelopmentexperience.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Multi Cluster Ingress Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusteringress#multiclusteringress.serviceAgent) (`roles/multiclusteringress.serviceAgent`) 
  * [Multi-cluster metering Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclustermetering#multiclustermetering.serviceAgent) (`roles/multiclustermetering.serviceAgent`) 
  * [Multi-Cluster Service Discovery Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/multiclusterservicediscovery#multiclusterservicediscovery.serviceAgent) (`roles/multiclusterservicediscovery.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `gkehub.memberships.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.memberships.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.namespaces.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.namespaces.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.namespaces.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  [Fleet Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer) (`roles/gkehub.scopeViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.namespaces.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  [Fleet Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer) (`roles/gkehub.scopeViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.namespaces.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Fleet Project-level Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditorProjectLevel) (`roles/gkehub.scopeEditorProjectLevel`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `gkehub.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Edge Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.rbacrolebindings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.rbacrolebindings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.rbacrolebindings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  [Fleet Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer) (`roles/gkehub.scopeViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.rbacrolebindings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  [Fleet Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer) (`roles/gkehub.scopeViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.rbacrolebindings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.scopes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.scopes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
#### `gkehub.scopes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  [Fleet Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer) (`roles/gkehub.scopeViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.scopes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  [Fleet Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer) (`roles/gkehub.scopeViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.scopes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.scopes.listBoundMemberships`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  [Fleet Viewer (formerly GKE Hub Viewer)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) (`roles/gkehub.viewer`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)  [Fleet Scope Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeEditor) (`roles/gkehub.scopeEditor`)  [Fleet Scope Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeViewer) (`roles/gkehub.scopeViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Support Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthossupport#anthossupport.serviceAgent) (`roles/anthossupport.serviceAgent`) 
  * [Game Services Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gameservices#gameservices.serviceAgent) (`roles/gameservices.serviceAgent`) 
  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 
  * [Mesh Managed Control Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane#meshcontrolplane.serviceAgent) (`roles/meshcontrolplane.serviceAgent`) 

  
  
#### `gkehub.scopes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Fleet Scope Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.scopeAdmin) (`roles/gkehub.scopeAdmin`)   
  
#### `gkehub.scopes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Fleet Admin (formerly GKE Hub Admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`)  [Fleet Editor (formerly GKE Hub Editor)](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.editor) (`roles/gkehub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 
  * [KRM API Hosting AnthosApiEndpoint Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.anthosApiEndpointServiceAgent) (`roles/krmapihosting.anthosApiEndpointServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
