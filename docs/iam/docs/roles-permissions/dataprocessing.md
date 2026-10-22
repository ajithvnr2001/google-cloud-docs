---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing/
title: Customer Usage Data Processing roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:06.214335+00:00
---

# Customer Usage Data Processing roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Customer Usage Data Processing roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Customer Usage Data Processing. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Customer Usage Data Processing roles

Role | Permissions  
---|---  
  
#### Data Processing Controls Resource Admin 

(`roles/dataprocessing.admin`) Data processing controls admin who can fully manage data processing controls settings and view all datasource data.  |  `billing.accounts.get` `billing.accounts.list` `dataprocessing.*`

  * `dataprocessing.datasources.get`
  * `dataprocessing.datasources.list`
  * `dataprocessing.datasources.update`
  * `dataprocessing.featurecontrols.list`
  * `dataprocessing.featurecontrols.update`
  * `dataprocessing.groupcontrols.get`
  * `dataprocessing.groupcontrols.list`
  * `dataprocessing.groupcontrols.update`

  
  
#### Dataprocessing Editor 

(`roles/dataprocessing.editor`) Editor role for dataprocessing  |  `dataprocessing.datasources.*`

  * `dataprocessing.datasources.get`
  * `dataprocessing.datasources.list`
  * `dataprocessing.datasources.update`

`dataprocessing.featurecontrols.list` `dataprocessing.groupcontrols.get` `dataprocessing.groupcontrols.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataprocessing Viewer 

(`roles/dataprocessing.viewer`) Viewer role for dataprocessing  |  `dataprocessing.datasources.get` `dataprocessing.datasources.list` `dataprocessing.featurecontrols.list` `dataprocessing.groupcontrols.get` `dataprocessing.groupcontrols.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Processing Controls Data Source Manager 

(`roles/dataprocessing.dataSourceManager`) Data processing controls data source manager who can get, list, and update the underlying data.  |  `dataprocessing.datasources.list` `dataprocessing.datasources.update`  
  
## Customer Usage Data Processing permissions

Permission | Included in roles  
---|---  
  
#### `dataprocessing.datasources.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Data Processing Controls Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`)  [Dataprocessing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.editor) (`roles/dataprocessing.editor`)  [Dataprocessing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.viewer) (`roles/dataprocessing.viewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataprocessing.datasources.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Data Processing Controls Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`)  [Dataprocessing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.editor) (`roles/dataprocessing.editor`)  [Dataprocessing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.viewer) (`roles/dataprocessing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Data Processing Controls Data Source Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.dataSourceManager) (`roles/dataprocessing.dataSourceManager`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataprocessing.datasources.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Processing Controls Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`)  [Dataprocessing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.editor) (`roles/dataprocessing.editor`)  [Data Processing Controls Data Source Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.dataSourceManager) (`roles/dataprocessing.dataSourceManager`)   
  
#### `dataprocessing.featurecontrols.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Processing Controls Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`)  [Dataprocessing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.editor) (`roles/dataprocessing.editor`)  [Dataprocessing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.viewer) (`roles/dataprocessing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataprocessing.featurecontrols.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Processing Controls Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`)   
  
#### `dataprocessing.groupcontrols.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Data Processing Controls Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`)  [Dataprocessing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.editor) (`roles/dataprocessing.editor`)  [Dataprocessing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.viewer) (`roles/dataprocessing.viewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataprocessing.groupcontrols.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Data Processing Controls Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`)  [Dataprocessing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.editor) (`roles/dataprocessing.editor`)  [Dataprocessing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.viewer) (`roles/dataprocessing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataprocessing.groupcontrols.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Processing Controls Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
