---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork/
title: Distributed Cloud Edge Network roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:27:03.922501+00:00
---

# Distributed Cloud Edge Network roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Distributed Cloud Edge Network roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Distributed Cloud Edge Network. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Distributed Cloud Edge Network roles

Role | Permissions  
---|---  
  
#### Edge Network Admin 

(`roles/edgenetwork.admin`) Full access to Edge Network all resources.  |  `edgenetwork.*`

  * `edgenetwork.interconnectAttachments.create`
  * `edgenetwork.interconnectAttachments.delete`
  * `edgenetwork.interconnectAttachments.get`
  * `edgenetwork.interconnectAttachments.getIamPolicy`
  * `edgenetwork.interconnectAttachments.list`
  * `edgenetwork.interconnectAttachments.setIamPolicy`
  * `edgenetwork.interconnectAttachments.update`
  * `edgenetwork.interconnects.get`
  * `edgenetwork.interconnects.getDiagnostics`
  * `edgenetwork.interconnects.getIamPolicy`
  * `edgenetwork.interconnects.list`
  * `edgenetwork.interconnects.setIamPolicy`
  * `edgenetwork.locations.get`
  * `edgenetwork.locations.list`
  * `edgenetwork.networks.create`
  * `edgenetwork.networks.delete`
  * `edgenetwork.networks.get`
  * `edgenetwork.networks.getIamPolicy`
  * `edgenetwork.networks.getStatus`
  * `edgenetwork.networks.list`
  * `edgenetwork.networks.setIamPolicy`
  * `edgenetwork.networks.update`
  * `edgenetwork.operations.cancel`
  * `edgenetwork.operations.delete`
  * `edgenetwork.operations.get`
  * `edgenetwork.operations.list`
  * `edgenetwork.routers.create`
  * `edgenetwork.routers.delete`
  * `edgenetwork.routers.get`
  * `edgenetwork.routers.getIamPolicy`
  * `edgenetwork.routers.getRouterStatus`
  * `edgenetwork.routers.list`
  * `edgenetwork.routers.patch`
  * `edgenetwork.routers.setIamPolicy`
  * `edgenetwork.routers.update`
  * `edgenetwork.routes.create`
  * `edgenetwork.routes.delete`
  * `edgenetwork.routes.get`
  * `edgenetwork.routes.list`
  * `edgenetwork.subnetworks.create`
  * `edgenetwork.subnetworks.delete`
  * `edgenetwork.subnetworks.get`
  * `edgenetwork.subnetworks.getIamPolicy`
  * `edgenetwork.subnetworks.getStatus`
  * `edgenetwork.subnetworks.list`
  * `edgenetwork.subnetworks.setIamPolicy`
  * `edgenetwork.subnetworks.update`
  * `edgenetwork.zones.get`
  * `edgenetwork.zones.initialize`
  * `edgenetwork.zones.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Network Editor 

(`roles/edgenetwork.editor`) Editor role for Edge Network  |  `edgenetwork.interconnectAttachments.create` `edgenetwork.interconnectAttachments.delete` `edgenetwork.interconnectAttachments.get` `edgenetwork.interconnectAttachments.getIamPolicy` `edgenetwork.interconnectAttachments.list` `edgenetwork.interconnectAttachments.update` `edgenetwork.interconnects.get` `edgenetwork.interconnects.getDiagnostics` `edgenetwork.interconnects.getIamPolicy` `edgenetwork.interconnects.list` `edgenetwork.locations.*`

  * `edgenetwork.locations.get`
  * `edgenetwork.locations.list`

`edgenetwork.networks.create` `edgenetwork.networks.delete` `edgenetwork.networks.get` `edgenetwork.networks.getIamPolicy` `edgenetwork.networks.getStatus` `edgenetwork.networks.list` `edgenetwork.networks.update` `edgenetwork.operations.*`

  * `edgenetwork.operations.cancel`
  * `edgenetwork.operations.delete`
  * `edgenetwork.operations.get`
  * `edgenetwork.operations.list`

`edgenetwork.routers.create` `edgenetwork.routers.delete` `edgenetwork.routers.get` `edgenetwork.routers.getIamPolicy` `edgenetwork.routers.getRouterStatus` `edgenetwork.routers.list` `edgenetwork.routers.patch` `edgenetwork.routers.update` `edgenetwork.routes.*`

  * `edgenetwork.routes.create`
  * `edgenetwork.routes.delete`
  * `edgenetwork.routes.get`
  * `edgenetwork.routes.list`

`edgenetwork.subnetworks.create` `edgenetwork.subnetworks.delete` `edgenetwork.subnetworks.get` `edgenetwork.subnetworks.getIamPolicy` `edgenetwork.subnetworks.getStatus` `edgenetwork.subnetworks.list` `edgenetwork.subnetworks.update` `edgenetwork.zones.*`

  * `edgenetwork.zones.get`
  * `edgenetwork.zones.initialize`
  * `edgenetwork.zones.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Edge Network Viewer 

(`roles/edgenetwork.viewer`) Read-only access to Edge Network all resources.  |  `edgenetwork.interconnectAttachments.get` `edgenetwork.interconnectAttachments.getIamPolicy` `edgenetwork.interconnectAttachments.list` `edgenetwork.interconnects.get` `edgenetwork.interconnects.getDiagnostics` `edgenetwork.interconnects.getIamPolicy` `edgenetwork.interconnects.list` `edgenetwork.locations.*`

  * `edgenetwork.locations.get`
  * `edgenetwork.locations.list`

`edgenetwork.networks.get` `edgenetwork.networks.getIamPolicy` `edgenetwork.networks.getStatus` `edgenetwork.networks.list` `edgenetwork.operations.get` `edgenetwork.operations.list` `edgenetwork.routers.get` `edgenetwork.routers.getIamPolicy` `edgenetwork.routers.getRouterStatus` `edgenetwork.routers.list` `edgenetwork.routes.get` `edgenetwork.routes.list` `edgenetwork.subnetworks.get` `edgenetwork.subnetworks.getIamPolicy` `edgenetwork.subnetworks.getStatus` `edgenetwork.subnetworks.list` `edgenetwork.zones.get` `edgenetwork.zones.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Distributed Cloud Edge Network permissions

Permission | Included in roles  
---|---  
  
#### `edgenetwork.interconnectAttachments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.interconnectAttachments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.interconnectAttachments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.interconnectAttachments.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.interconnectAttachments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.interconnectAttachments.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgenetwork.interconnectAttachments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.interconnects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.interconnects.getDiagnostics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.interconnects.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.interconnects.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.interconnects.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgenetwork.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.networks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.networks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.networks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.networks.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.networks.getStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.networks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.networks.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgenetwork.networks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.routers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.routers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.routers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.routers.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.routers.getRouterStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.routers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.routers.patch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.routers.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgenetwork.routers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.routes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.routes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.routes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.routes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.subnetworks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.subnetworks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.subnetworks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.subnetworks.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.subnetworks.getStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.subnetworks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.subnetworks.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `edgenetwork.subnetworks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.zones.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `edgenetwork.zones.initialize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)   
  
#### `edgenetwork.zones.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Edge Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.admin) (`roles/edgenetwork.admin`)  [Edge Network Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.editor) (`roles/edgenetwork.editor`)  [Edge Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/edgenetwork#edgenetwork.viewer) (`roles/edgenetwork.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
