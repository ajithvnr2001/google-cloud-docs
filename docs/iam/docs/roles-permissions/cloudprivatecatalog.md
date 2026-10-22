---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog/
title: Service Catalog roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:27.726552+00:00
---

# Service Catalog roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Service Catalog roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Service Catalog. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Service Catalog roles

Role | Permissions  
---|---  
  
#### Catalog Admin Beta

(`roles/cloudprivatecatalog.admin`) Admin role for Cloud Private Catalog  |  `cloudprivatecatalog.targets.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Catalog Viewer Beta

(`roles/cloudprivatecatalog.viewer`) Viewer role for Cloud Private Catalog  |  `cloudprivatecatalog.targets.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Catalog Admin Beta

(`roles/cloudprivatecatalogproducer.admin`) Can manage catalog and view its associations.  |  `cloudprivatecatalog.targets.get` `cloudprivatecatalogproducer.associations.*`

  * `cloudprivatecatalogproducer.associations.create`
  * `cloudprivatecatalogproducer.associations.delete`
  * `cloudprivatecatalogproducer.associations.get`
  * `cloudprivatecatalogproducer.associations.list`

`cloudprivatecatalogproducer.catalogAssociations.*`

  * `cloudprivatecatalogproducer.catalogAssociations.create`
  * `cloudprivatecatalogproducer.catalogAssociations.delete`
  * `cloudprivatecatalogproducer.catalogAssociations.get`
  * `cloudprivatecatalogproducer.catalogAssociations.list`

`cloudprivatecatalogproducer.catalogs.*`

  * `cloudprivatecatalogproducer.catalogs.create`
  * `cloudprivatecatalogproducer.catalogs.delete`
  * `cloudprivatecatalogproducer.catalogs.get`
  * `cloudprivatecatalogproducer.catalogs.getIamPolicy`
  * `cloudprivatecatalogproducer.catalogs.list`
  * `cloudprivatecatalogproducer.catalogs.setIamPolicy`
  * `cloudprivatecatalogproducer.catalogs.undelete`
  * `cloudprivatecatalogproducer.catalogs.update`

`cloudprivatecatalogproducer.producerCatalogs.*`

  * `cloudprivatecatalogproducer.producerCatalogs.attachProduct`
  * `cloudprivatecatalogproducer.producerCatalogs.create`
  * `cloudprivatecatalogproducer.producerCatalogs.delete`
  * `cloudprivatecatalogproducer.producerCatalogs.detachProduct`
  * `cloudprivatecatalogproducer.producerCatalogs.get`
  * `cloudprivatecatalogproducer.producerCatalogs.getIamPolicy`
  * `cloudprivatecatalogproducer.producerCatalogs.list`
  * `cloudprivatecatalogproducer.producerCatalogs.setIamPolicy`
  * `cloudprivatecatalogproducer.producerCatalogs.update`

`cloudprivatecatalogproducer.products.*`

  * `cloudprivatecatalogproducer.products.create`
  * `cloudprivatecatalogproducer.products.delete`
  * `cloudprivatecatalogproducer.products.get`
  * `cloudprivatecatalogproducer.products.getIamPolicy`
  * `cloudprivatecatalogproducer.products.list`
  * `cloudprivatecatalogproducer.products.setIamPolicy`
  * `cloudprivatecatalogproducer.products.update`

`cloudprivatecatalogproducer.targets.*`

  * `cloudprivatecatalogproducer.targets.associate`
  * `cloudprivatecatalogproducer.targets.unassociate`

`resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Catalog Editor Beta

(`roles/cloudprivatecatalogproducer.editor`) Editor role for Cloud Private Catalog  |  `cloudprivatecatalogproducer.associations.*`

  * `cloudprivatecatalogproducer.associations.create`
  * `cloudprivatecatalogproducer.associations.delete`
  * `cloudprivatecatalogproducer.associations.get`
  * `cloudprivatecatalogproducer.associations.list`

`cloudprivatecatalogproducer.catalogAssociations.*`

  * `cloudprivatecatalogproducer.catalogAssociations.create`
  * `cloudprivatecatalogproducer.catalogAssociations.delete`
  * `cloudprivatecatalogproducer.catalogAssociations.get`
  * `cloudprivatecatalogproducer.catalogAssociations.list`

`cloudprivatecatalogproducer.catalogs.create` `cloudprivatecatalogproducer.catalogs.delete` `cloudprivatecatalogproducer.catalogs.get` `cloudprivatecatalogproducer.catalogs.getIamPolicy` `cloudprivatecatalogproducer.catalogs.list` `cloudprivatecatalogproducer.catalogs.undelete` `cloudprivatecatalogproducer.catalogs.update` `cloudprivatecatalogproducer.producerCatalogs.attachProduct` `cloudprivatecatalogproducer.producerCatalogs.create` `cloudprivatecatalogproducer.producerCatalogs.delete` `cloudprivatecatalogproducer.producerCatalogs.detachProduct` `cloudprivatecatalogproducer.producerCatalogs.get` `cloudprivatecatalogproducer.producerCatalogs.getIamPolicy` `cloudprivatecatalogproducer.producerCatalogs.list` `cloudprivatecatalogproducer.producerCatalogs.update` `cloudprivatecatalogproducer.products.create` `cloudprivatecatalogproducer.products.delete` `cloudprivatecatalogproducer.products.get` `cloudprivatecatalogproducer.products.getIamPolicy` `cloudprivatecatalogproducer.products.list` `cloudprivatecatalogproducer.products.update` `cloudprivatecatalogproducer.settings.*`

  * `cloudprivatecatalogproducer.settings.get`
  * `cloudprivatecatalogproducer.settings.update`

`cloudprivatecatalogproducer.targets.*`

  * `cloudprivatecatalogproducer.targets.associate`
  * `cloudprivatecatalogproducer.targets.unassociate`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Catalog Viewer Beta

(`roles/cloudprivatecatalogproducer.viewer`) Viewer role for Cloud Private Catalog  |  `cloudprivatecatalogproducer.associations.get` `cloudprivatecatalogproducer.associations.list` `cloudprivatecatalogproducer.catalogAssociations.get` `cloudprivatecatalogproducer.catalogAssociations.list` `cloudprivatecatalogproducer.catalogs.get` `cloudprivatecatalogproducer.catalogs.getIamPolicy` `cloudprivatecatalogproducer.catalogs.list` `cloudprivatecatalogproducer.producerCatalogs.get` `cloudprivatecatalogproducer.producerCatalogs.getIamPolicy` `cloudprivatecatalogproducer.producerCatalogs.list` `cloudprivatecatalogproducer.products.get` `cloudprivatecatalogproducer.products.getIamPolicy` `cloudprivatecatalogproducer.products.list` `cloudprivatecatalogproducer.settings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Catalog Consumer Beta

(`roles/cloudprivatecatalog.consumer`) Can browse catalogs in the target resource context.  |  `cloudprivatecatalog.targets.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Catalog Manager Beta

(`roles/cloudprivatecatalogproducer.manager`) Can manage associations between a catalog and a target resource.  |  `cloudprivatecatalog.targets.get` `cloudprivatecatalogproducer.associations.*`

  * `cloudprivatecatalogproducer.associations.create`
  * `cloudprivatecatalogproducer.associations.delete`
  * `cloudprivatecatalogproducer.associations.get`
  * `cloudprivatecatalogproducer.associations.list`

`cloudprivatecatalogproducer.catalogAssociations.*`

  * `cloudprivatecatalogproducer.catalogAssociations.create`
  * `cloudprivatecatalogproducer.catalogAssociations.delete`
  * `cloudprivatecatalogproducer.catalogAssociations.get`
  * `cloudprivatecatalogproducer.catalogAssociations.list`

`cloudprivatecatalogproducer.catalogs.get` `cloudprivatecatalogproducer.catalogs.list` `cloudprivatecatalogproducer.producerCatalogs.get` `cloudprivatecatalogproducer.producerCatalogs.list` `cloudprivatecatalogproducer.targets.*`

  * `cloudprivatecatalogproducer.targets.associate`
  * `cloudprivatecatalogproducer.targets.unassociate`

`resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Catalog Org Admin Beta

(`roles/cloudprivatecatalogproducer.orgAdmin`) Can manage catalog org settings.  |  `cloudprivatecatalog.targets.get` `cloudprivatecatalogproducer.*`

  * `cloudprivatecatalogproducer.associations.create`
  * `cloudprivatecatalogproducer.associations.delete`
  * `cloudprivatecatalogproducer.associations.get`
  * `cloudprivatecatalogproducer.associations.list`
  * `cloudprivatecatalogproducer.catalogAssociations.create`
  * `cloudprivatecatalogproducer.catalogAssociations.delete`
  * `cloudprivatecatalogproducer.catalogAssociations.get`
  * `cloudprivatecatalogproducer.catalogAssociations.list`
  * `cloudprivatecatalogproducer.catalogs.create`
  * `cloudprivatecatalogproducer.catalogs.delete`
  * `cloudprivatecatalogproducer.catalogs.get`
  * `cloudprivatecatalogproducer.catalogs.getIamPolicy`
  * `cloudprivatecatalogproducer.catalogs.list`
  * `cloudprivatecatalogproducer.catalogs.setIamPolicy`
  * `cloudprivatecatalogproducer.catalogs.undelete`
  * `cloudprivatecatalogproducer.catalogs.update`
  * `cloudprivatecatalogproducer.producerCatalogs.attachProduct`
  * `cloudprivatecatalogproducer.producerCatalogs.create`
  * `cloudprivatecatalogproducer.producerCatalogs.delete`
  * `cloudprivatecatalogproducer.producerCatalogs.detachProduct`
  * `cloudprivatecatalogproducer.producerCatalogs.get`
  * `cloudprivatecatalogproducer.producerCatalogs.getIamPolicy`
  * `cloudprivatecatalogproducer.producerCatalogs.list`
  * `cloudprivatecatalogproducer.producerCatalogs.setIamPolicy`
  * `cloudprivatecatalogproducer.producerCatalogs.update`
  * `cloudprivatecatalogproducer.products.create`
  * `cloudprivatecatalogproducer.products.delete`
  * `cloudprivatecatalogproducer.products.get`
  * `cloudprivatecatalogproducer.products.getIamPolicy`
  * `cloudprivatecatalogproducer.products.list`
  * `cloudprivatecatalogproducer.products.setIamPolicy`
  * `cloudprivatecatalogproducer.products.update`
  * `cloudprivatecatalogproducer.settings.get`
  * `cloudprivatecatalogproducer.settings.update`
  * `cloudprivatecatalogproducer.targets.associate`
  * `cloudprivatecatalogproducer.targets.unassociate`

`commerceorggovernance.organizationSettings.*`

  * `commerceorggovernance.organizationSettings.get`
  * `commerceorggovernance.organizationSettings.update`

`resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Service Catalog permissions

Permission | Included in roles  
---|---  
  
#### `cloudprivatecatalog.targets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalog.admin) (`roles/cloudprivatecatalog.admin`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalog.viewer) (`roles/cloudprivatecatalog.viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalog.consumer) (`roles/cloudprivatecatalog.consumer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `cloudprivatecatalogproducer.associations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.associations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.associations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.associations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.catalogAssociations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.catalogAssociations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.catalogAssociations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.catalogAssociations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.catalogs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.catalogs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.catalogs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.catalogs.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.catalogs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.catalogs.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.catalogs.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.catalogs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.attachProduct`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.detachProduct`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.producerCatalogs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.products.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.products.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.products.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.products.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.products.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.products.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.products.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.settings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.viewer) (`roles/cloudprivatecatalogproducer.viewer`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprivatecatalogproducer.settings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.targets.associate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
#### `cloudprivatecatalogproducer.targets.unassociate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Catalog Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.admin) (`roles/cloudprivatecatalogproducer.admin`)  [Catalog Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.editor) (`roles/cloudprivatecatalogproducer.editor`)  [Catalog Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.manager) (`roles/cloudprivatecatalogproducer.manager`)  [Catalog Org Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprivatecatalog#cloudprivatecatalogproducer.orgAdmin) (`roles/cloudprivatecatalogproducer.orgAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
