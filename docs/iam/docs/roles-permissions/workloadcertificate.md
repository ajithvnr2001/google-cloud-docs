---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate/
title: Workload Certificate roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:12.398724+00:00
---

# Workload Certificate roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Workload Certificate roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Workload Certificate. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Workload Certificate roles

Role | Permissions  
---|---  
  
#### Workload Certificate Admin Beta

(`roles/workloadcertificate.admin`) Full access to all Workload Certificate API resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadcertificate.*`

  * `workloadcertificate.locations.get`
  * `workloadcertificate.locations.list`
  * `workloadcertificate.operations.cancel`
  * `workloadcertificate.operations.delete`
  * `workloadcertificate.operations.get`
  * `workloadcertificate.operations.list`
  * `workloadcertificate.workloadCertificateFeature.get`
  * `workloadcertificate.workloadCertificateFeature.update`
  * `workloadcertificate.workloadRegistrations.create`
  * `workloadcertificate.workloadRegistrations.delete`
  * `workloadcertificate.workloadRegistrations.get`
  * `workloadcertificate.workloadRegistrations.list`
  * `workloadcertificate.workloadRegistrations.update`

  
  
#### Workload Certificate Viewer Beta

(`roles/workloadcertificate.viewer`) Read-only access to Workload Certificate all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadcertificate.locations.*`

  * `workloadcertificate.locations.get`
  * `workloadcertificate.locations.list`

`workloadcertificate.operations.get` `workloadcertificate.operations.list` `workloadcertificate.workloadCertificateFeature.get` `workloadcertificate.workloadRegistrations.get` `workloadcertificate.workloadRegistrations.list`  
  
#### Workload Certificate Registration Admin Beta

(`roles/workloadcertificate.registrationAdmin`) Full access to WorkloadRegistration resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadcertificate.locations.*`

  * `workloadcertificate.locations.get`
  * `workloadcertificate.locations.list`

`workloadcertificate.operations.*`

  * `workloadcertificate.operations.cancel`
  * `workloadcertificate.operations.delete`
  * `workloadcertificate.operations.get`
  * `workloadcertificate.operations.list`

`workloadcertificate.workloadRegistrations.*`

  * `workloadcertificate.workloadRegistrations.create`
  * `workloadcertificate.workloadRegistrations.delete`
  * `workloadcertificate.workloadRegistrations.get`
  * `workloadcertificate.workloadRegistrations.list`
  * `workloadcertificate.workloadRegistrations.update`

  
  
#### Workload Certificate Registration Viewer Beta

(`roles/workloadcertificate.registrationViewer`) Read-only access to WorkloadRegistration resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `workloadcertificate.locations.*`

  * `workloadcertificate.locations.get`
  * `workloadcertificate.locations.list`

`workloadcertificate.operations.get` `workloadcertificate.operations.list` `workloadcertificate.workloadRegistrations.get` `workloadcertificate.workloadRegistrations.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Workload Certificate Service Agent 

(`roles/workloadcertificate.serviceAgent`) Gives the Workload Certificate service agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `container.clusterRoleBindings.get` `container.clusterRoleBindings.list` `container.clusters.get` `container.clusters.update` `container.customResourceDefinitions.create` `container.customResourceDefinitions.get` `container.customResourceDefinitions.list` `container.operations.get` `container.thirdPartyObjects.update` `gkehub.features.get` `gkehub.fleet.create` `gkehub.fleet.get` `gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.memberships.get` `gkehub.memberships.list` `gkehub.operations.get` `serviceconsumermanagement.tenancyu.addResource` `serviceconsumermanagement.tenancyu.create` `serviceconsumermanagement.tenancyu.delete` `serviceconsumermanagement.tenancyu.removeResource` `serviceusage.services.use` `workloadcertificate.workloadCertificateFeature.get` `workloadcertificate.workloadRegistrations.list`  
  
## Workload Certificate permissions

Permission | Included in roles  
---|---  
  
#### `workloadcertificate.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.viewer) (`roles/workloadcertificate.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)  [Workload Certificate Registration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationViewer) (`roles/workloadcertificate.registrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 

  
  
#### `workloadcertificate.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.viewer) (`roles/workloadcertificate.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)  [Workload Certificate Registration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationViewer) (`roles/workloadcertificate.registrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 

  
  
#### `workloadcertificate.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)   
  
#### `workloadcertificate.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)   
  
#### `workloadcertificate.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.viewer) (`roles/workloadcertificate.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)  [Workload Certificate Registration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationViewer) (`roles/workloadcertificate.registrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 

  
  
#### `workloadcertificate.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.viewer) (`roles/workloadcertificate.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)  [Workload Certificate Registration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationViewer) (`roles/workloadcertificate.registrationViewer`)   
  
#### `workloadcertificate.workloadCertificateFeature.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.viewer) (`roles/workloadcertificate.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `workloadcertificate.workloadCertificateFeature.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)   
  
#### `workloadcertificate.workloadRegistrations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 

  
  
#### `workloadcertificate.workloadRegistrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)   
  
#### `workloadcertificate.workloadRegistrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.viewer) (`roles/workloadcertificate.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)  [Workload Certificate Registration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationViewer) (`roles/workloadcertificate.registrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 

  
  
#### `workloadcertificate.workloadRegistrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.viewer) (`roles/workloadcertificate.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)  [Workload Certificate Registration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationViewer) (`roles/workloadcertificate.registrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Service Mesh Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#anthosservicemesh.serviceAgent) (`roles/anthosservicemesh.serviceAgent`) 
  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `workloadcertificate.workloadRegistrations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Workload Certificate Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.admin) (`roles/workloadcertificate.admin`)  [Workload Certificate Registration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.registrationAdmin) (`roles/workloadcertificate.registrationAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
