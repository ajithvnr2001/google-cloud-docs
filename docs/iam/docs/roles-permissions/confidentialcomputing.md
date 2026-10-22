---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing/
title: Confidential Computing roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:26.950336+00:00
---

# Confidential Computing roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Confidential Computing roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Confidential Computing. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Confidential Computing roles

Role | Permissions  
---|---  
  
#### Confidentialcomputing Admin 

(`roles/confidentialcomputing.admin`) Admin role for confidentialcomputing  |  `confidentialcomputing.*`

  * `confidentialcomputing.challenges.create`
  * `confidentialcomputing.challenges.verify`
  * `confidentialcomputing.challenges.verifygke`
  * `confidentialcomputing.locations.get`
  * `confidentialcomputing.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Confidentialcomputing Viewer 

(`roles/confidentialcomputing.viewer`) Viewer role for confidentialcomputing  |  `confidentialcomputing.locations.*`

  * `confidentialcomputing.locations.get`
  * `confidentialcomputing.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Confidential GKE Workload User 

(`roles/confidentialcomputing.gkeWorkloadUser`) Grants the ability to generate a GKE attestation token and run a workload in a GKE cluster.  |  `confidentialcomputing.challenges.create` `confidentialcomputing.challenges.verifygke` `confidentialcomputing.locations.*`

  * `confidentialcomputing.locations.get`
  * `confidentialcomputing.locations.list`

`logging.logEntries.create`  
  
#### Confidential Space Workload User 

(`roles/confidentialcomputing.workloadUser`) Grants the ability to generate an attestation token and run a workload in a VM. Intended for service accounts that run on Confidential Space VMs.  |  `confidentialcomputing.challenges.create` `confidentialcomputing.challenges.verify` `confidentialcomputing.locations.*`

  * `confidentialcomputing.locations.get`
  * `confidentialcomputing.locations.list`

`logging.logEntries.create`  
  
## Confidential Computing permissions

Permission | Included in roles  
---|---  
  
#### `confidentialcomputing.challenges.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Confidentialcomputing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.admin) (`roles/confidentialcomputing.admin`)  [Confidential GKE Workload User](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.gkeWorkloadUser) (`roles/confidentialcomputing.gkeWorkloadUser`)  [Confidential Space Workload User](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.workloadUser) (`roles/confidentialcomputing.workloadUser`)   
  
#### `confidentialcomputing.challenges.verify`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Confidentialcomputing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.admin) (`roles/confidentialcomputing.admin`)  [Confidential Space Workload User](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.workloadUser) (`roles/confidentialcomputing.workloadUser`)   
  
#### `confidentialcomputing.challenges.verifygke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Confidentialcomputing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.admin) (`roles/confidentialcomputing.admin`)  [Confidential GKE Workload User](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.gkeWorkloadUser) (`roles/confidentialcomputing.gkeWorkloadUser`)   
  
#### `confidentialcomputing.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Confidentialcomputing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.admin) (`roles/confidentialcomputing.admin`)  [Confidentialcomputing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.viewer) (`roles/confidentialcomputing.viewer`)  [Confidential GKE Workload User](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.gkeWorkloadUser) (`roles/confidentialcomputing.gkeWorkloadUser`)  [Confidential Space Workload User](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.workloadUser) (`roles/confidentialcomputing.workloadUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `confidentialcomputing.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Confidentialcomputing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.admin) (`roles/confidentialcomputing.admin`)  [Confidentialcomputing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.viewer) (`roles/confidentialcomputing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Confidential GKE Workload User](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.gkeWorkloadUser) (`roles/confidentialcomputing.gkeWorkloadUser`)  [Confidential Space Workload User](https://docs.cloud.google.com/iam/docs/roles-permissions/confidentialcomputing#confidentialcomputing.workloadUser) (`roles/confidentialcomputing.workloadUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
