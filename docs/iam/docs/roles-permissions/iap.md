---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/iap/
title: Identity-Aware Proxy roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:28.000647+00:00
---

# Identity-Aware Proxy roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/iap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Identity-Aware Proxy roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Identity-Aware Proxy. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Identity-Aware Proxy roles

Role | Permissions  
---|---  
  
#### IAP Policy Admin 

(`roles/iap.admin`) Provides full access to Identity-Aware Proxy resources.  |  `iap.projects.*`

  * `iap.projects.getSettings`
  * `iap.projects.updateSettings`

`iap.tunnel.*`

  * `iap.tunnel.getIamPolicy`
  * `iap.tunnel.setIamPolicy`

`iap.tunnelDestGroups.create` `iap.tunnelDestGroups.delete` `iap.tunnelDestGroups.get` `iap.tunnelDestGroups.getIamPolicy` `iap.tunnelDestGroups.list` `iap.tunnelDestGroups.remediate` `iap.tunnelDestGroups.setIamPolicy` `iap.tunnelDestGroups.update` `iap.tunnelInstances.getIamPolicy` `iap.tunnelInstances.setIamPolicy` `iap.tunnelLocations.*`

  * `iap.tunnelLocations.getIamPolicy`
  * `iap.tunnelLocations.setIamPolicy`

`iap.tunnelZones.*`

  * `iap.tunnelZones.getIamPolicy`
  * `iap.tunnelZones.setIamPolicy`

`iap.tunnelinstances.remediate` `iap.web.*`

  * `iap.web.getIamPolicy`
  * `iap.web.getSettings`
  * `iap.web.setIamPolicy`
  * `iap.web.updateSettings`

`iap.webServiceVersions.getIamPolicy` `iap.webServiceVersions.getSettings` `iap.webServiceVersions.remediate` `iap.webServiceVersions.setIamPolicy` `iap.webServiceVersions.updateSettings` `iap.webServices.*`

  * `iap.webServices.getIamPolicy`
  * `iap.webServices.getSettings`
  * `iap.webServices.setIamPolicy`
  * `iap.webServices.updateSettings`

`iap.webTypes.*`

  * `iap.webTypes.getIamPolicy`
  * `iap.webTypes.getSettings`
  * `iap.webTypes.setIamPolicy`
  * `iap.webTypes.updateSettings`

  
  
#### IAP Policy Editor 

(`roles/iap.editor`) Editor role for IAP  |  `iap.projects.*`

  * `iap.projects.getSettings`
  * `iap.projects.updateSettings`

`iap.resources.egressViaIAP` `iap.tunnelDestGroups.create` `iap.tunnelDestGroups.delete` `iap.tunnelDestGroups.get` `iap.tunnelDestGroups.list` `iap.tunnelDestGroups.update` `iap.web.getSettings` `iap.web.updateSettings` `iap.webServiceVersions.getSettings` `iap.webServiceVersions.updateSettings` `iap.webServices.getSettings` `iap.webServices.updateSettings` `iap.webTypes.getSettings` `iap.webTypes.updateSettings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### IAP-secured Egressor Beta

(`roles/iap.egressor`) Egress to resources via Identity-Aware Proxy  |  `iap.webServiceVersions.egressViaIAP`  
  
#### IAP-secured Web App User 

(`roles/iap.httpsResourceAccessor`) Provides permission to access HTTPS resources which use Identity-Aware Proxy.  |  `iap.webServiceVersions.accessViaIAP`  
  
#### IAP-secured Tunnel User 

(`roles/iap.tunnelResourceAccessor`) Access Tunnel resources which use Identity-Aware Proxy  |  `iap.tunnelDestGroups.accessViaIAP` `iap.tunnelInstances.accessViaIAP`  
  
#### IAP Policy Viewer 

(`roles/iap.viewer`) Viewer role for IAP  |  `iap.projects.getSettings` `iap.resources.egressViaIAP` `iap.tunnelDestGroups.get` `iap.tunnelDestGroups.list` `iap.web.getSettings` `iap.webServiceVersions.getSettings` `iap.webServices.getSettings` `iap.webTypes.getSettings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### IAP-secured Resource Remediator User Beta

(`roles/iap.remediatorUser`) Remediate IAP resource  |  `iap.tunnelDestGroups.remediate` `iap.tunnelinstances.remediate` `iap.webServiceVersions.remediate`  
  
#### IAP Settings Admin 

(`roles/iap.settingsAdmin`) Administrator of IAP Settings.  |  `iap.projects.*`

  * `iap.projects.getSettings`
  * `iap.projects.updateSettings`

`iap.web.getSettings` `iap.web.updateSettings` `iap.webServiceVersions.getSettings` `iap.webServiceVersions.updateSettings` `iap.webServices.getSettings` `iap.webServices.updateSettings` `iap.webTypes.getSettings` `iap.webTypes.updateSettings`  
  
#### IAP-secured Tunnel Destination Group Editor 

(`roles/iap.tunnelDestGroupEditor`) Edit Tunnel Destination Group resources which use Identity-Aware Proxy  |  `iap.tunnelDestGroups.create` `iap.tunnelDestGroups.delete` `iap.tunnelDestGroups.get` `iap.tunnelDestGroups.list` `iap.tunnelDestGroups.update`  
  
#### IAP-secured Tunnel Destination Group Viewer 

(`roles/iap.tunnelDestGroupViewer`) View Tunnel Destination Group resources which use Identity-Aware Proxy  |  `iap.tunnelDestGroups.get` `iap.tunnelDestGroups.list`  
  
## Identity-Aware Proxy permissions

Permission | Included in roles  
---|---  
  
#### `iap.projects.getSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.viewer) (`roles/iap.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.projects.updateSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.resources.egressViaIAP`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.viewer) (`roles/iap.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iap.tunnel.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `iap.tunnel.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.tunnelDestGroups.accessViaIAP`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [IAP-secured Tunnel User](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`)   
  
#### `iap.tunnelDestGroups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP-secured Tunnel Destination Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelDestGroupEditor) (`roles/iap.tunnelDestGroupEditor`)   
  
#### `iap.tunnelDestGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP-secured Tunnel Destination Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelDestGroupEditor) (`roles/iap.tunnelDestGroupEditor`)   
  
#### `iap.tunnelDestGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.viewer) (`roles/iap.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAP-secured Tunnel Destination Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelDestGroupEditor) (`roles/iap.tunnelDestGroupEditor`)  [IAP-secured Tunnel Destination Group Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelDestGroupViewer) (`roles/iap.tunnelDestGroupViewer`)   
  
#### `iap.tunnelDestGroups.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `iap.tunnelDestGroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.viewer) (`roles/iap.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAP-secured Tunnel Destination Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelDestGroupEditor) (`roles/iap.tunnelDestGroupEditor`)  [IAP-secured Tunnel Destination Group Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelDestGroupViewer) (`roles/iap.tunnelDestGroupViewer`)   
  
#### `iap.tunnelDestGroups.remediate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP-secured Resource Remediator User](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.remediatorUser) (`roles/iap.remediatorUser`)   
  
#### `iap.tunnelDestGroups.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.tunnelDestGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP-secured Tunnel Destination Group Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelDestGroupEditor) (`roles/iap.tunnelDestGroupEditor`)   
  
#### `iap.tunnelInstances.accessViaIAP`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [IAP-secured Tunnel User](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`)   
  
#### `iap.tunnelInstances.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `iap.tunnelInstances.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.tunnelLocations.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `iap.tunnelLocations.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.tunnelZones.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `iap.tunnelZones.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.tunnelinstances.remediate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP-secured Resource Remediator User](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.remediatorUser) (`roles/iap.remediatorUser`)   
  
#### `iap.web.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `iap.web.getSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.viewer) (`roles/iap.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.web.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.web.updateSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.webServiceVersions.accessViaIAP`

|  [IAP-secured Web App User](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.httpsResourceAccessor) (`roles/iap.httpsResourceAccessor`)   
  
#### `iap.webServiceVersions.egressViaIAP`

|  [IAP-secured Egressor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.egressor) (`roles/iap.egressor`)   
  
#### `iap.webServiceVersions.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `iap.webServiceVersions.getSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.viewer) (`roles/iap.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.webServiceVersions.remediate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP-secured Resource Remediator User](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.remediatorUser) (`roles/iap.remediatorUser`)   
  
#### `iap.webServiceVersions.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.webServiceVersions.updateSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.webServices.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `iap.webServices.getSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.viewer) (`roles/iap.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.webServices.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.webServices.updateSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.webTypes.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `iap.webTypes.getSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Policy Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.viewer) (`roles/iap.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
#### `iap.webTypes.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)   
  
#### `iap.webTypes.updateSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [IAP Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)  [IAP Policy Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.editor) (`roles/iap.editor`)  [IAP Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.settingsAdmin) (`roles/iap.settingsAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
