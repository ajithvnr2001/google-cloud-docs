---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform/
title: Google Cloud Contact Center as a Service roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:19.916798+00:00
---

# Google Cloud Contact Center as a Service roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud Contact Center as a Service roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud Contact Center as a Service. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud Contact Center as a Service roles

Role | Permissions  
---|---  
  
#### Contact Center AI Platform Admin 

(`roles/contactcenteraiplatform.admin`) Full access to Contact Center AI Platform resources.  |  `contactcenteraiplatform.*`

  * `contactcenteraiplatform.contactCenters.create`
  * `contactcenteraiplatform.contactCenters.delete`
  * `contactcenteraiplatform.contactCenters.get`
  * `contactcenteraiplatform.contactCenters.list`
  * `contactcenteraiplatform.contactCenters.program`
  * `contactcenteraiplatform.contactCenters.queryQuota`
  * `contactcenteraiplatform.contactCenters.update`
  * `contactcenteraiplatform.locations.generateShifts`
  * `contactcenteraiplatform.locations.get`
  * `contactcenteraiplatform.locations.list`
  * `contactcenteraiplatform.operations.cancel`
  * `contactcenteraiplatform.operations.delete`
  * `contactcenteraiplatform.operations.get`
  * `contactcenteraiplatform.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Contact Center AI Platform Viewer 

(`roles/contactcenteraiplatform.viewer`) Read-only access to Contact Center AI Platform resources.  |  `contactcenteraiplatform.contactCenters.get` `contactcenteraiplatform.contactCenters.list` `contactcenteraiplatform.contactCenters.queryQuota` `contactcenteraiplatform.locations.get` `contactcenteraiplatform.locations.list` `contactcenteraiplatform.operations.get` `contactcenteraiplatform.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Workforce Scheduling Shift Generator Beta

(`roles/contactcenteraiplatform.workforceSchedulingShiftGenerator`) Access to generating shifts using Workforce Scheduling.  |  `contactcenteraiplatform.locations.generateShifts`  
  
## Google Cloud Contact Center as a Service permissions

Permission | Included in roles  
---|---  
  
#### `contactcenteraiplatform.contactCenters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)   
  
#### `contactcenteraiplatform.contactCenters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)   
  
#### `contactcenteraiplatform.contactCenters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)  [Contact Center AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.viewer) (`roles/contactcenteraiplatform.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contactcenteraiplatform.contactCenters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)  [Contact Center AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.viewer) (`roles/contactcenteraiplatform.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contactcenteraiplatform.contactCenters.program`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)   
  
#### `contactcenteraiplatform.contactCenters.queryQuota`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)  [Contact Center AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.viewer) (`roles/contactcenteraiplatform.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contactcenteraiplatform.contactCenters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)   
  
#### `contactcenteraiplatform.locations.generateShifts`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)  [Workforce Scheduling Shift Generator](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.workforceSchedulingShiftGenerator) (`roles/contactcenteraiplatform.workforceSchedulingShiftGenerator`)   
  
#### `contactcenteraiplatform.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)  [Contact Center AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.viewer) (`roles/contactcenteraiplatform.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contactcenteraiplatform.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)  [Contact Center AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.viewer) (`roles/contactcenteraiplatform.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contactcenteraiplatform.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)   
  
#### `contactcenteraiplatform.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)   
  
#### `contactcenteraiplatform.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)  [Contact Center AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.viewer) (`roles/contactcenteraiplatform.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `contactcenteraiplatform.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Contact Center AI Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`)  [Contact Center AI Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.viewer) (`roles/contactcenteraiplatform.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
