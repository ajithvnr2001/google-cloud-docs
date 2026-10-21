---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise/
title: Google Cloud Fraud Defense roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:32:52.639569+00:00
---

# Google Cloud Fraud Defense roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud Fraud Defense roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud Fraud Defense. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud Fraud Defense roles

Role | Permissions  
---|---  
  
#### reCAPTCHA Enterprise Admin 

(`roles/recaptchaenterprise.admin`) Access to view and modify reCAPTCHA Enterprise keys  |  `monitoring.timeSeries.list` `recaptchaenterprise.*`

  * `recaptchaenterprise.assessments.annotate`
  * `recaptchaenterprise.assessments.create`
  * `recaptchaenterprise.firewallpolicies.create`
  * `recaptchaenterprise.firewallpolicies.delete`
  * `recaptchaenterprise.firewallpolicies.get`
  * `recaptchaenterprise.firewallpolicies.list`
  * `recaptchaenterprise.firewallpolicies.update`
  * `recaptchaenterprise.keys.create`
  * `recaptchaenterprise.keys.createTagBinding`
  * `recaptchaenterprise.keys.delete`
  * `recaptchaenterprise.keys.deleteTagBinding`
  * `recaptchaenterprise.keys.get`
  * `recaptchaenterprise.keys.list`
  * `recaptchaenterprise.keys.listEffectiveTags`
  * `recaptchaenterprise.keys.listTagBindings`
  * `recaptchaenterprise.keys.retrievelegacysecretkey`
  * `recaptchaenterprise.keys.update`
  * `recaptchaenterprise.metrics.get`
  * `recaptchaenterprise.policies.get`
  * `recaptchaenterprise.policies.update`
  * `recaptchaenterprise.projectmetadata.get`
  * `recaptchaenterprise.projectmetadata.update`
  * `recaptchaenterprise.relatedaccountgroupmemberships.list`
  * `recaptchaenterprise.relatedaccountgroups.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### reCAPTCHA Enterprise Editor 

(`roles/recaptchaenterprise.editor`) Editor role for reCAPTCHA Enterprise  |  `monitoring.timeSeries.list` `recaptchaenterprise.assessments.*`

  * `recaptchaenterprise.assessments.annotate`
  * `recaptchaenterprise.assessments.create`

`recaptchaenterprise.firewallpolicies.*`

  * `recaptchaenterprise.firewallpolicies.create`
  * `recaptchaenterprise.firewallpolicies.delete`
  * `recaptchaenterprise.firewallpolicies.get`
  * `recaptchaenterprise.firewallpolicies.list`
  * `recaptchaenterprise.firewallpolicies.update`

`recaptchaenterprise.keys.create` `recaptchaenterprise.keys.delete` `recaptchaenterprise.keys.get` `recaptchaenterprise.keys.list` `recaptchaenterprise.keys.listEffectiveTags` `recaptchaenterprise.keys.listTagBindings` `recaptchaenterprise.keys.retrievelegacysecretkey` `recaptchaenterprise.keys.update` `recaptchaenterprise.metrics.get` `recaptchaenterprise.policies.*`

  * `recaptchaenterprise.policies.get`
  * `recaptchaenterprise.policies.update`

`recaptchaenterprise.projectmetadata.*`

  * `recaptchaenterprise.projectmetadata.get`
  * `recaptchaenterprise.projectmetadata.update`

`recaptchaenterprise.relatedaccountgroupmemberships.list` `recaptchaenterprise.relatedaccountgroups.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### reCAPTCHA Enterprise Viewer 

(`roles/recaptchaenterprise.viewer`) Access to view reCAPTCHA Enterprise keys and metrics  |  `monitoring.timeSeries.list` `recaptchaenterprise.firewallpolicies.get` `recaptchaenterprise.firewallpolicies.list` `recaptchaenterprise.keys.get` `recaptchaenterprise.keys.list` `recaptchaenterprise.keys.listEffectiveTags` `recaptchaenterprise.keys.listTagBindings` `recaptchaenterprise.metrics.get` `recaptchaenterprise.policies.get` `recaptchaenterprise.projectmetadata.get` `recaptchaenterprise.relatedaccountgroupmemberships.list` `recaptchaenterprise.relatedaccountgroups.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### reCAPTCHA Enterprise Agent 

(`roles/recaptchaenterprise.agent`) Access to create and annotate reCAPTCHA Enterprise assessments  |  `recaptchaenterprise.assessments.*`

  * `recaptchaenterprise.assessments.annotate`
  * `recaptchaenterprise.assessments.create`

`recaptchaenterprise.firewallpolicies.list` `recaptchaenterprise.relatedaccountgroupmemberships.list` `recaptchaenterprise.relatedaccountgroups.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Google Cloud Fraud Defense permissions

Permission | Included in roles  
---|---  
  
#### `recaptchaenterprise.assessments.annotate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.agent) (`roles/recaptchaenterprise.agent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase App Check Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappcheck#firebaseappcheck.serviceAgent) (`roles/firebaseappcheck.serviceAgent`) 

  
  
#### `recaptchaenterprise.assessments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.agent) (`roles/recaptchaenterprise.agent`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase App Check Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappcheck#firebaseappcheck.serviceAgent) (`roles/firebaseappcheck.serviceAgent`) 
  * [Identity Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.serviceAgent) (`roles/identitytoolkit.serviceAgent`) 

  
  
#### `recaptchaenterprise.firewallpolicies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)   
  
#### `recaptchaenterprise.firewallpolicies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)   
  
#### `recaptchaenterprise.firewallpolicies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `recaptchaenterprise.firewallpolicies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [reCAPTCHA Enterprise Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.agent) (`roles/recaptchaenterprise.agent`)   
  
#### `recaptchaenterprise.firewallpolicies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)   
  
#### `recaptchaenterprise.keys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Identity Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.serviceAgent) (`roles/identitytoolkit.serviceAgent`) 

  
  
#### `recaptchaenterprise.keys.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `recaptchaenterprise.keys.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Identity Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.serviceAgent) (`roles/identitytoolkit.serviceAgent`) 

  
  
#### `recaptchaenterprise.keys.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `recaptchaenterprise.keys.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Identity Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.serviceAgent) (`roles/identitytoolkit.serviceAgent`) 

  
  
#### `recaptchaenterprise.keys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 

  
  
#### `recaptchaenterprise.keys.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `recaptchaenterprise.keys.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `recaptchaenterprise.keys.retrievelegacysecretkey`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)   
  
#### `recaptchaenterprise.keys.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 

  
  
#### `recaptchaenterprise.metrics.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `recaptchaenterprise.policies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `recaptchaenterprise.policies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)   
  
#### `recaptchaenterprise.projectmetadata.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `recaptchaenterprise.projectmetadata.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)   
  
#### `recaptchaenterprise.relatedaccountgroupmemberships.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [reCAPTCHA Enterprise Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.agent) (`roles/recaptchaenterprise.agent`)   
  
#### `recaptchaenterprise.relatedaccountgroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [reCAPTCHA Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)  [reCAPTCHA Enterprise Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.editor) (`roles/recaptchaenterprise.editor`)  [reCAPTCHA Enterprise Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.viewer) (`roles/recaptchaenterprise.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [reCAPTCHA Enterprise Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.agent) (`roles/recaptchaenterprise.agent`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
