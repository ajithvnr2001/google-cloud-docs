---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement/
title: Service Consumer Management roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:58.350909+00:00
---

# Service Consumer Management roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Service Consumer Management roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Service Consumer Management. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Service Consumer Management roles

Role | Permissions  
---|---  
  
#### Service Consumer Management Admin Beta

(`roles/serviceconsumermanagement.admin`) Admin role for Service Consumer Management  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceconsumermanagement.*`

  * `serviceconsumermanagement.consumers.get`
  * `serviceconsumermanagement.quota.get`
  * `serviceconsumermanagement.quota.update`
  * `serviceconsumermanagement.tenancyu.addResource`
  * `serviceconsumermanagement.tenancyu.create`
  * `serviceconsumermanagement.tenancyu.delete`
  * `serviceconsumermanagement.tenancyu.list`
  * `serviceconsumermanagement.tenancyu.removeResource`

  
  
#### Service Consumer Management Viewer Beta

(`roles/serviceconsumermanagement.viewer`) Viewer role for Service Consumer Management  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceconsumermanagement.consumers.get` `serviceconsumermanagement.quota.get` `serviceconsumermanagement.tenancyu.list`  
  
#### Admin of Tenancy Units Beta

(`roles/serviceconsumermanagement.tenancyUnitsAdmin`) Administrate tenancy units  |  `serviceconsumermanagement.tenancyu.*`

  * `serviceconsumermanagement.tenancyu.addResource`
  * `serviceconsumermanagement.tenancyu.create`
  * `serviceconsumermanagement.tenancyu.delete`
  * `serviceconsumermanagement.tenancyu.list`
  * `serviceconsumermanagement.tenancyu.removeResource`

  
  
#### Viewer of Tenancy Units Beta

(`roles/serviceconsumermanagement.tenancyUnitsViewer`) View tenancy units  |  `serviceconsumermanagement.tenancyu.list`  
  
## Service Consumer Management permissions

Permission | Included in roles  
---|---  
  
#### `serviceconsumermanagement.consumers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Consumer Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.admin) (`roles/serviceconsumermanagement.admin`)  [Service Consumer Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.viewer) (`roles/serviceconsumermanagement.viewer`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `serviceconsumermanagement.quota.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Consumer Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.admin) (`roles/serviceconsumermanagement.admin`)  [Service Consumer Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.viewer) (`roles/serviceconsumermanagement.viewer`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `serviceconsumermanagement.quota.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Consumer Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.admin) (`roles/serviceconsumermanagement.admin`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)   
  
#### `serviceconsumermanagement.tenancyu.addResource`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Consumer Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.admin) (`roles/serviceconsumermanagement.admin`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Admin of Tenancy Units](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.tenancyUnitsAdmin) (`roles/serviceconsumermanagement.tenancyUnitsAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `serviceconsumermanagement.tenancyu.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Consumer Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.admin) (`roles/serviceconsumermanagement.admin`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Admin of Tenancy Units](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.tenancyUnitsAdmin) (`roles/serviceconsumermanagement.tenancyUnitsAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `serviceconsumermanagement.tenancyu.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Consumer Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.admin) (`roles/serviceconsumermanagement.admin`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Admin of Tenancy Units](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.tenancyUnitsAdmin) (`roles/serviceconsumermanagement.tenancyUnitsAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
#### `serviceconsumermanagement.tenancyu.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Consumer Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.admin) (`roles/serviceconsumermanagement.admin`)  [Service Consumer Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.viewer) (`roles/serviceconsumermanagement.viewer`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Admin of Tenancy Units](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.tenancyUnitsAdmin) (`roles/serviceconsumermanagement.tenancyUnitsAdmin`)  [Viewer of Tenancy Units](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.tenancyUnitsViewer) (`roles/serviceconsumermanagement.tenancyUnitsViewer`)   
  
#### `serviceconsumermanagement.tenancyu.removeResource`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Consumer Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.admin) (`roles/serviceconsumermanagement.admin`)  [Service Management Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`)  [Admin of Tenancy Units](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceconsumermanagement#serviceconsumermanagement.tenancyUnitsAdmin) (`roles/serviceconsumermanagement.tenancyUnitsAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Workload Certificate Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadcertificate#workloadcertificate.serviceAgent) (`roles/workloadcertificate.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
