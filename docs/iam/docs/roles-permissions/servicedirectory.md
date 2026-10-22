---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory/
title: Service Directory roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:56.441342+00:00
---

# Service Directory roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Service Directory roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Service Directory. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Service Directory roles

Role | Permissions  
---|---  
  
#### Service Directory Admin 

(`roles/servicedirectory.admin`) Full control of all Service Directory resources and permissions.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.*`

  * `servicedirectory.endpoints.create`
  * `servicedirectory.endpoints.delete`
  * `servicedirectory.endpoints.get`
  * `servicedirectory.endpoints.getIamPolicy`
  * `servicedirectory.endpoints.list`
  * `servicedirectory.endpoints.setIamPolicy`
  * `servicedirectory.endpoints.update`

`servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.*`

  * `servicedirectory.namespaces.associatePrivateZone`
  * `servicedirectory.namespaces.create`
  * `servicedirectory.namespaces.delete`
  * `servicedirectory.namespaces.get`
  * `servicedirectory.namespaces.getIamPolicy`
  * `servicedirectory.namespaces.list`
  * `servicedirectory.namespaces.setIamPolicy`
  * `servicedirectory.namespaces.update`

`servicedirectory.networks.attach` `servicedirectory.services.*`

  * `servicedirectory.services.bind`
  * `servicedirectory.services.create`
  * `servicedirectory.services.delete`
  * `servicedirectory.services.get`
  * `servicedirectory.services.getIamPolicy`
  * `servicedirectory.services.list`
  * `servicedirectory.services.resolve`
  * `servicedirectory.services.setIamPolicy`
  * `servicedirectory.services.update`

  
  
#### Service Directory Editor 

(`roles/servicedirectory.editor`) Edit Service Directory resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.create` `servicedirectory.endpoints.delete` `servicedirectory.endpoints.get` `servicedirectory.endpoints.getIamPolicy` `servicedirectory.endpoints.list` `servicedirectory.endpoints.update` `servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.associatePrivateZone` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.namespaces.get` `servicedirectory.namespaces.getIamPolicy` `servicedirectory.namespaces.list` `servicedirectory.namespaces.update` `servicedirectory.networks.attach` `servicedirectory.services.bind` `servicedirectory.services.create` `servicedirectory.services.delete` `servicedirectory.services.get` `servicedirectory.services.getIamPolicy` `servicedirectory.services.list` `servicedirectory.services.resolve` `servicedirectory.services.update`  
  
#### Service Directory Viewer 

(`roles/servicedirectory.viewer`) View Service Directory resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.get` `servicedirectory.endpoints.getIamPolicy` `servicedirectory.endpoints.list` `servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.get` `servicedirectory.namespaces.getIamPolicy` `servicedirectory.namespaces.list` `servicedirectory.services.get` `servicedirectory.services.getIamPolicy` `servicedirectory.services.list` `servicedirectory.services.resolve`  
  
#### Service Directory Network Attacher 

(`roles/servicedirectory.networkAttacher`) Gives access to attach VPC Networks to Service Directory Endpoints  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.networks.attach`  
  
#### Private Service Connect Authorized Service 

(`roles/servicedirectory.pscAuthorizedService`) Gives access to VPC Networks via Service Directory  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.networks.access`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Service Directory Service Agent 

(`roles/servicedirectory.serviceAgent`) Give the Service Directory service agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `container.clusters.get` `gkehub.features.get` `gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.get` `gkehub.memberships.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `servicedirectory.endpoints.create` `servicedirectory.endpoints.delete` `servicedirectory.endpoints.get` `servicedirectory.endpoints.getIamPolicy` `servicedirectory.endpoints.list` `servicedirectory.endpoints.update` `servicedirectory.locations.*`

  * `servicedirectory.locations.get`
  * `servicedirectory.locations.list`

`servicedirectory.namespaces.associatePrivateZone` `servicedirectory.namespaces.create` `servicedirectory.namespaces.delete` `servicedirectory.namespaces.get` `servicedirectory.namespaces.getIamPolicy` `servicedirectory.namespaces.list` `servicedirectory.namespaces.update` `servicedirectory.networks.attach` `servicedirectory.services.bind` `servicedirectory.services.create` `servicedirectory.services.delete` `servicedirectory.services.get` `servicedirectory.services.getIamPolicy` `servicedirectory.services.list` `servicedirectory.services.resolve` `servicedirectory.services.update`  
  
## Service Directory permissions

Permission | Included in roles  
---|---  
  
#### `servicedirectory.endpoints.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.endpoints.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.endpoints.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.endpoints.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.endpoints.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.endpoints.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)   
  
#### `servicedirectory.endpoints.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.namespaces.associatePrivateZone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.namespaces.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Compute Peer Subnet Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.peerSubnetMigrationAdmin) (`roles/compute.peerSubnetMigrationAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Cloud Workstations Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.networkAdmin) (`roles/workstations.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workstations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.serviceAgent) (`roles/workstations.serviceAgent`) 

  
  
#### `servicedirectory.namespaces.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Cloud Workstations Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.networkAdmin) (`roles/workstations.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workstations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.serviceAgent) (`roles/workstations.serviceAgent`) 

  
  
#### `servicedirectory.namespaces.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.namespaces.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.namespaces.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.namespaces.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)   
  
#### `servicedirectory.namespaces.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.networks.access`

|  [Private Service Connect Authorized Service](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.pscAuthorizedService) (`roles/servicedirectory.pscAuthorizedService`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent) (`roles/monitoring.notificationServiceAgent`) 

  
  
#### `servicedirectory.networks.attach`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Network Attacher](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.networkAttacher) (`roles/servicedirectory.networkAttacher`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.services.bind`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.services.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Compute Peer Subnet Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.peerSubnetMigrationAdmin) (`roles/compute.peerSubnetMigrationAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Cloud Workstations Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.networkAdmin) (`roles/workstations.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workstations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.serviceAgent) (`roles/workstations.serviceAgent`) 

  
  
#### `servicedirectory.services.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Compute Peer Subnet Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.peerSubnetMigrationAdmin) (`roles/compute.peerSubnetMigrationAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Cloud Workstations Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.networkAdmin) (`roles/workstations.networkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud TPU V2 API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#cloudtpu.serviceAgent) (`roles/cloudtpu.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) (`roles/managedkafka.serviceAgent`) 
  * [Dataproc Metastore Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.serviceAgent) (`roles/metastore.serviceAgent`) 
  * [Network Connectivity Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity#networkconnectivity.serviceAgent) (`roles/networkconnectivity.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 
  * [Workstations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.serviceAgent) (`roles/workstations.serviceAgent`) 

  
  
#### `servicedirectory.services.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.services.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.services.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.services.resolve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  [Service Directory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent) (`roles/monitoring.notificationServiceAgent`) 
  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
#### `servicedirectory.services.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)   
  
#### `servicedirectory.services.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Directory Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.admin) (`roles/servicedirectory.admin`)  [Service Directory Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Service Directory Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.serviceAgent) (`roles/servicedirectory.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
