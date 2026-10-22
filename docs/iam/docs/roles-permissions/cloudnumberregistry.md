---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry/
title: Cloud Number Registry roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:59.474627+00:00
---

# Cloud Number Registry roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Number Registry roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Number Registry. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Number Registry roles

Role | Permissions  
---|---  
  
#### Cloud Number Registry IPAM Admin Beta

(`roles/cloudnumberregistry.ipamAdmin`) Full access to Cloud Number Registry resources.  |  `cloudnumberregistry.*`

  * `cloudnumberregistry.customRanges.create`
  * `cloudnumberregistry.customRanges.delete`
  * `cloudnumberregistry.customRanges.get`
  * `cloudnumberregistry.customRanges.list`
  * `cloudnumberregistry.customRanges.update`
  * `cloudnumberregistry.discoveredRanges.get`
  * `cloudnumberregistry.discoveredRanges.list`
  * `cloudnumberregistry.ipamAdminScopes.create`
  * `cloudnumberregistry.ipamAdminScopes.delete`
  * `cloudnumberregistry.ipamAdminScopes.get`
  * `cloudnumberregistry.ipamAdminScopes.list`
  * `cloudnumberregistry.ipamAdminScopes.update`
  * `cloudnumberregistry.locations.get`
  * `cloudnumberregistry.locations.list`
  * `cloudnumberregistry.operations.cancel`
  * `cloudnumberregistry.operations.delete`
  * `cloudnumberregistry.operations.get`
  * `cloudnumberregistry.operations.list`
  * `cloudnumberregistry.realms.create`
  * `cloudnumberregistry.realms.delete`
  * `cloudnumberregistry.realms.get`
  * `cloudnumberregistry.realms.list`
  * `cloudnumberregistry.realms.update`
  * `cloudnumberregistry.registryBooks.create`
  * `cloudnumberregistry.registryBooks.delete`
  * `cloudnumberregistry.registryBooks.get`
  * `cloudnumberregistry.registryBooks.list`
  * `cloudnumberregistry.registryBooks.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Number Registry IPAM Viewer Beta

(`roles/cloudnumberregistry.ipamViewer`) Readonly access to Cloud Number Registry resources.  |  `cloudnumberregistry.customRanges.get` `cloudnumberregistry.customRanges.list` `cloudnumberregistry.discoveredRanges.*`

  * `cloudnumberregistry.discoveredRanges.get`
  * `cloudnumberregistry.discoveredRanges.list`

`cloudnumberregistry.ipamAdminScopes.get` `cloudnumberregistry.ipamAdminScopes.list` `cloudnumberregistry.locations.*`

  * `cloudnumberregistry.locations.get`
  * `cloudnumberregistry.locations.list`

`cloudnumberregistry.operations.get` `cloudnumberregistry.operations.list` `cloudnumberregistry.realms.get` `cloudnumberregistry.realms.list` `cloudnumberregistry.registryBooks.get` `cloudnumberregistry.registryBooks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Cloud Number Registry permissions

Permission | Included in roles  
---|---  
  
#### `cloudnumberregistry.customRanges.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.customRanges.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.customRanges.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.customRanges.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.customRanges.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.discoveredRanges.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.discoveredRanges.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.ipamAdminScopes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.ipamAdminScopes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.ipamAdminScopes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.ipamAdminScopes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.ipamAdminScopes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.realms.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.realms.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.realms.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.realms.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.realms.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.registryBooks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.registryBooks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
#### `cloudnumberregistry.registryBooks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.registryBooks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)  [Cloud Number Registry IPAM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudnumberregistry.registryBooks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Number Registry IPAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
