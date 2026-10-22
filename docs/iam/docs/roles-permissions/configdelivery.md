---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery/
title: Config Delivery roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:28.429693+00:00
---

# Config Delivery roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Config Delivery roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Config Delivery. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Config Delivery roles

Role | Permissions  
---|---  
  
#### Configdelivery Admin 

(`roles/configdelivery.admin`) Admin role for configdelivery  |  `configdelivery.*`

  * `configdelivery.fleetPackages.create`
  * `configdelivery.fleetPackages.delete`
  * `configdelivery.fleetPackages.get`
  * `configdelivery.fleetPackages.list`
  * `configdelivery.fleetPackages.update`
  * `configdelivery.locations.get`
  * `configdelivery.locations.list`
  * `configdelivery.operations.cancel`
  * `configdelivery.operations.delete`
  * `configdelivery.operations.get`
  * `configdelivery.operations.list`
  * `configdelivery.releases.create`
  * `configdelivery.releases.delete`
  * `configdelivery.releases.get`
  * `configdelivery.releases.list`
  * `configdelivery.releases.update`
  * `configdelivery.resourceBundles.create`
  * `configdelivery.resourceBundles.delete`
  * `configdelivery.resourceBundles.get`
  * `configdelivery.resourceBundles.list`
  * `configdelivery.resourceBundles.update`
  * `configdelivery.rollouts.abort`
  * `configdelivery.rollouts.get`
  * `configdelivery.rollouts.list`
  * `configdelivery.rollouts.resume`
  * `configdelivery.rollouts.suspend`
  * `configdelivery.variants.create`
  * `configdelivery.variants.delete`
  * `configdelivery.variants.get`
  * `configdelivery.variants.list`
  * `configdelivery.variants.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Configdelivery Viewer 

(`roles/configdelivery.viewer`) Viewer role for configdelivery  |  `configdelivery.fleetPackages.get` `configdelivery.fleetPackages.list` `configdelivery.locations.*`

  * `configdelivery.locations.get`
  * `configdelivery.locations.list`

`configdelivery.operations.get` `configdelivery.operations.list` `configdelivery.releases.get` `configdelivery.releases.list` `configdelivery.resourceBundles.get` `configdelivery.resourceBundles.list` `configdelivery.rollouts.get` `configdelivery.rollouts.list` `configdelivery.variants.get` `configdelivery.variants.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### ConfigDelivery Admin 

(`roles/configdelivery.configDeliveryAdmin`) Grants full access to all Config Delivery resources. Lets users create, remove and manage fleet packages and resource bundles.  |  `configdelivery.*`

  * `configdelivery.fleetPackages.create`
  * `configdelivery.fleetPackages.delete`
  * `configdelivery.fleetPackages.get`
  * `configdelivery.fleetPackages.list`
  * `configdelivery.fleetPackages.update`
  * `configdelivery.locations.get`
  * `configdelivery.locations.list`
  * `configdelivery.operations.cancel`
  * `configdelivery.operations.delete`
  * `configdelivery.operations.get`
  * `configdelivery.operations.list`
  * `configdelivery.releases.create`
  * `configdelivery.releases.delete`
  * `configdelivery.releases.get`
  * `configdelivery.releases.list`
  * `configdelivery.releases.update`
  * `configdelivery.resourceBundles.create`
  * `configdelivery.resourceBundles.delete`
  * `configdelivery.resourceBundles.get`
  * `configdelivery.resourceBundles.list`
  * `configdelivery.resourceBundles.update`
  * `configdelivery.rollouts.abort`
  * `configdelivery.rollouts.get`
  * `configdelivery.rollouts.list`
  * `configdelivery.rollouts.resume`
  * `configdelivery.rollouts.suspend`
  * `configdelivery.variants.create`
  * `configdelivery.variants.delete`
  * `configdelivery.variants.get`
  * `configdelivery.variants.list`
  * `configdelivery.variants.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### ConfigDelivery Viewer 

(`roles/configdelivery.configDeliveryViewer`) Grants read access to all Config Delivery resources. Lets users view existing fleet packages and resource bundles, but they will not be able to make any changes.  |  `configdelivery.fleetPackages.get` `configdelivery.fleetPackages.list` `configdelivery.locations.*`

  * `configdelivery.locations.get`
  * `configdelivery.locations.list`

`configdelivery.operations.get` `configdelivery.operations.list` `configdelivery.releases.get` `configdelivery.releases.list` `configdelivery.resourceBundles.get` `configdelivery.resourceBundles.list` `configdelivery.rollouts.get` `configdelivery.rollouts.list` `configdelivery.variants.get` `configdelivery.variants.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Config Delivery Resource Bundle Publisher 

(`roles/configdelivery.resourceBundlePublisher`) Grants read and write permissions to Config Delivery ResourceBundles and Releases.  |  `configdelivery.locations.*`

  * `configdelivery.locations.get`
  * `configdelivery.locations.list`

`configdelivery.operations.get` `configdelivery.operations.list` `configdelivery.releases.create` `configdelivery.releases.get` `configdelivery.releases.list` `configdelivery.releases.update` `configdelivery.resourceBundles.create` `configdelivery.resourceBundles.get` `configdelivery.resourceBundles.list` `configdelivery.resourceBundles.update` `configdelivery.variants.create` `configdelivery.variants.get` `configdelivery.variants.list` `configdelivery.variants.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Config Delivery Service Agent 

(`roles/configdelivery.serviceAgent`) Gives the Config Delivery service account permission to manage resources  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.projectsettings.get` `artifactregistry.repositories.create` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.getIamPolicy` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.setIamPolicy` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.*`

  * `artifactregistry.tags.create`
  * `artifactregistry.tags.delete`
  * `artifactregistry.tags.get`
  * `artifactregistry.tags.list`
  * `artifactregistry.tags.update`

`artifactregistry.versions.delete` `artifactregistry.versions.get` `artifactregistry.versions.list` `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.repositories.get` `container.customResourceDefinitions.get` `container.customResourceDefinitions.list` `container.serviceAccounts.get` `container.serviceAccounts.list` `container.thirdPartyObjects.*`

  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`

`gkehub.gateway.delete` `gkehub.gateway.generateCredentials` `gkehub.gateway.get` `gkehub.gateway.patch` `gkehub.gateway.post` `gkehub.gateway.put` `gkehub.memberships.get` `iam.serviceAccounts.actAs`  
  
## Config Delivery permissions

Permission | Included in roles  
---|---  
  
#### `configdelivery.fleetPackages.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.fleetPackages.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.fleetPackages.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.fleetPackages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.fleetPackages.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.releases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)   
  
#### `configdelivery.releases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.releases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.releases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.releases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)   
  
#### `configdelivery.resourceBundles.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)   
  
#### `configdelivery.resourceBundles.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.resourceBundles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.resourceBundles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.resourceBundles.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)   
  
#### `configdelivery.rollouts.abort`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.rollouts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.rollouts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.rollouts.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.rollouts.suspend`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.variants.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)   
  
#### `configdelivery.variants.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)   
  
#### `configdelivery.variants.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.variants.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [Configdelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.viewer) (`roles/configdelivery.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [ConfigDelivery Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryViewer) (`roles/configdelivery.configDeliveryViewer`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `configdelivery.variants.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Configdelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.admin) (`roles/configdelivery.admin`)  [ConfigDelivery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.configDeliveryAdmin) (`roles/configdelivery.configDeliveryAdmin`)  [Config Delivery Resource Bundle Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/configdelivery#configdelivery.resourceBundlePublisher) (`roles/configdelivery.resourceBundlePublisher`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
