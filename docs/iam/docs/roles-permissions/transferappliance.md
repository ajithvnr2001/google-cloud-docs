---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance/
title: Transfer Appliance roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:10.342214+00:00
---

# Transfer Appliance roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Transfer Appliance roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Transfer Appliance. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Transfer Appliance roles

Role | Permissions  
---|---  
  
#### Transfer Appliance Admin Beta

(`roles/transferappliance.admin`) Full access to Transfer Appliance all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `transferappliance.*`

  * `transferappliance.appliances.create`
  * `transferappliance.appliances.delete`
  * `transferappliance.appliances.get`
  * `transferappliance.appliances.list`
  * `transferappliance.appliances.update`
  * `transferappliance.credentials.get`
  * `transferappliance.locations.get`
  * `transferappliance.locations.list`
  * `transferappliance.operations.cancel`
  * `transferappliance.operations.delete`
  * `transferappliance.operations.get`
  * `transferappliance.operations.list`
  * `transferappliance.orders.create`
  * `transferappliance.orders.delete`
  * `transferappliance.orders.get`
  * `transferappliance.orders.list`
  * `transferappliance.orders.update`
  * `transferappliance.savedAddresses.create`
  * `transferappliance.savedAddresses.delete`
  * `transferappliance.savedAddresses.get`
  * `transferappliance.savedAddresses.list`
  * `transferappliance.savedAddresses.update`

  
  
#### Transfer Appliance Viewer Beta

(`roles/transferappliance.viewer`) Read-only access to Transfer Appliance all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `transferappliance.appliances.get` `transferappliance.appliances.list` `transferappliance.locations.*`

  * `transferappliance.locations.get`
  * `transferappliance.locations.list`

`transferappliance.operations.get` `transferappliance.operations.list` `transferappliance.orders.get` `transferappliance.orders.list` `transferappliance.savedAddresses.get` `transferappliance.savedAddresses.list`  
  
## Transfer Appliance permissions

Permission | Included in roles  
---|---  
  
#### `transferappliance.appliances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.appliances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.appliances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.appliances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.appliances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.credentials.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.orders.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.orders.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.orders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.orders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.orders.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.savedAddresses.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.savedAddresses.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
#### `transferappliance.savedAddresses.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.savedAddresses.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)  [Transfer Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transferappliance.savedAddresses.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transfer Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
