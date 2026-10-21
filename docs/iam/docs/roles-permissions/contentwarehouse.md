---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse/
title: Content Warehouse roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:41:17.507505+00:00
---

# Content Warehouse roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Content Warehouse roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Content Warehouse. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Content Warehouse roles

Role | Permissions  
---|---  
  
#### Content Warehouse Admin 

(`roles/contentwarehouse.admin`) Grants full access to all the resources in Content Warehouse  |  `contentwarehouse.*`

  * `contentwarehouse.corpora.create`
  * `contentwarehouse.corpora.delete`
  * `contentwarehouse.corpora.get`
  * `contentwarehouse.corpora.list`
  * `contentwarehouse.corpora.update`
  * `contentwarehouse.dataExportJobs.create`
  * `contentwarehouse.dataExportJobs.update`
  * `contentwarehouse.documentSchemas.create`
  * `contentwarehouse.documentSchemas.delete`
  * `contentwarehouse.documentSchemas.get`
  * `contentwarehouse.documentSchemas.list`
  * `contentwarehouse.documentSchemas.update`
  * `contentwarehouse.documents.create`
  * `contentwarehouse.documents.delete`
  * `contentwarehouse.documents.get`
  * `contentwarehouse.documents.getIamPolicy`
  * `contentwarehouse.documents.list`
  * `contentwarehouse.documents.setIamPolicy`
  * `contentwarehouse.documents.update`
  * `contentwarehouse.links.create`
  * `contentwarehouse.links.delete`
  * `contentwarehouse.links.get`
  * `contentwarehouse.links.update`
  * `contentwarehouse.locations.getStatus`
  * `contentwarehouse.locations.initialize`
  * `contentwarehouse.operations.get`
  * `contentwarehouse.rawDocuments.download`
  * `contentwarehouse.rawDocuments.upload`
  * `contentwarehouse.ruleSets.create`
  * `contentwarehouse.ruleSets.delete`
  * `contentwarehouse.ruleSets.get`
  * `contentwarehouse.ruleSets.list`
  * `contentwarehouse.ruleSets.update`
  * `contentwarehouse.synonymSets.create`
  * `contentwarehouse.synonymSets.delete`
  * `contentwarehouse.synonymSets.get`
  * `contentwarehouse.synonymSets.list`
  * `contentwarehouse.synonymSets.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Content Warehouse Document Admin 

(`roles/contentwarehouse.documentAdmin`) Grants full access to the document resource in Content Warehouse  |  `contentwarehouse.documentSchemas.get` `contentwarehouse.documents.create` `contentwarehouse.documents.delete` `contentwarehouse.documents.get` `contentwarehouse.documents.getIamPolicy` `contentwarehouse.documents.setIamPolicy` `contentwarehouse.documents.update` `contentwarehouse.links.*`

  * `contentwarehouse.links.create`
  * `contentwarehouse.links.delete`
  * `contentwarehouse.links.get`
  * `contentwarehouse.links.update`

`contentwarehouse.locations.getStatus` `contentwarehouse.rawDocuments.*`

  * `contentwarehouse.rawDocuments.download`
  * `contentwarehouse.rawDocuments.upload`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Content Warehouse document creator 

(`roles/contentwarehouse.documentCreator`) Grants access to create document in Content Warehouse  |  `contentwarehouse.documentSchemas.get` `contentwarehouse.documentSchemas.list` `contentwarehouse.documents.create` `contentwarehouse.locations.getStatus` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Content Warehouse Document Editor 

(`roles/contentwarehouse.documentEditor`) Grants access to update document resource in Content Warehouse  |  `contentwarehouse.documentSchemas.get` `contentwarehouse.documents.get` `contentwarehouse.documents.getIamPolicy` `contentwarehouse.documents.update` `contentwarehouse.links.*`

  * `contentwarehouse.links.create`
  * `contentwarehouse.links.delete`
  * `contentwarehouse.links.get`
  * `contentwarehouse.links.update`

`contentwarehouse.locations.getStatus` `contentwarehouse.rawDocuments.*`

  * `contentwarehouse.rawDocuments.download`
  * `contentwarehouse.rawDocuments.upload`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Content Warehouse document schema viewer 

(`roles/contentwarehouse.documentSchemaViewer`) Grants access to view the document schemas in Content Warehouse  |  `contentwarehouse.documentSchemas.get` `contentwarehouse.documentSchemas.list` `contentwarehouse.locations.getStatus` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Content Warehouse Viewer 

(`roles/contentwarehouse.documentViewer`) Grants access to view all the resources in Content Warehouse  |  `contentwarehouse.documentSchemas.get` `contentwarehouse.documents.get` `contentwarehouse.documents.getIamPolicy` `contentwarehouse.links.get` `contentwarehouse.locations.getStatus` `contentwarehouse.rawDocuments.download` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Content Warehouse Service Agent 

(`roles/contentwarehouse.serviceAgent`) Gives the Content Warehouse service account to manage customer resources  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudfunctions.functions.invoke` `documentai.datasets.createDocuments` `documentai.processors.get` `documentai.processors.processBatch` `pubsub.topics.publish` `pubsublite.topics.publish` `storage.buckets.get` `storage.buckets.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Content Warehouse permissions

Permission | Included in roles  
---|---  
  
#### `contentwarehouse.corpora.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.corpora.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.corpora.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.corpora.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.corpora.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.dataExportJobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.dataExportJobs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.documentSchemas.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.documentSchemas.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.documentSchemas.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse document creator](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentCreator) (`roles/contentwarehouse.documentCreator`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)  [Content Warehouse document schema viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentSchemaViewer) (`roles/contentwarehouse.documentSchemaViewer`)  [Content Warehouse Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentViewer) (`roles/contentwarehouse.documentViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.documentSchemas.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Content Warehouse document creator](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentCreator) (`roles/contentwarehouse.documentCreator`)  [Content Warehouse document schema viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentSchemaViewer) (`roles/contentwarehouse.documentSchemaViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.documentSchemas.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.documents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse document creator](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentCreator) (`roles/contentwarehouse.documentCreator`)   
  
#### `contentwarehouse.documents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)   
  
#### `contentwarehouse.documents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)  [Content Warehouse Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentViewer) (`roles/contentwarehouse.documentViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.documents.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)  [Content Warehouse Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentViewer) (`roles/contentwarehouse.documentViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.documents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.documents.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)   
  
#### `contentwarehouse.documents.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)   
  
#### `contentwarehouse.links.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)   
  
#### `contentwarehouse.links.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)   
  
#### `contentwarehouse.links.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)  [Content Warehouse Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentViewer) (`roles/contentwarehouse.documentViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.links.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)   
  
#### `contentwarehouse.locations.getStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse document creator](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentCreator) (`roles/contentwarehouse.documentCreator`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)  [Content Warehouse document schema viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentSchemaViewer) (`roles/contentwarehouse.documentSchemaViewer`)  [Content Warehouse Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentViewer) (`roles/contentwarehouse.documentViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.locations.initialize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.rawDocuments.download`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)  [Content Warehouse Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentViewer) (`roles/contentwarehouse.documentViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.rawDocuments.upload`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Content Warehouse Document Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentAdmin) (`roles/contentwarehouse.documentAdmin`)  [Content Warehouse Document Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.documentEditor) (`roles/contentwarehouse.documentEditor`)   
  
#### `contentwarehouse.ruleSets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.ruleSets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.ruleSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.ruleSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.ruleSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.synonymSets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.synonymSets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
#### `contentwarehouse.synonymSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.synonymSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contentwarehouse.synonymSets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Content Warehouse Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.admin) (`roles/contentwarehouse.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
