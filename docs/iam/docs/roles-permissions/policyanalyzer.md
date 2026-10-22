---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer/
title: Policy Analyzer roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:41.264706+00:00
---

# Policy Analyzer roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Policy Analyzer roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Policy Analyzer. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Policy Analyzer roles

Role | Permissions  
---|---  
  
#### Policyanalyzer Admin Beta

(`roles/policyanalyzer.admin`) Admin role for policyanalyzer  |  `policyanalyzer.*`

  * `policyanalyzer.resourceAuthorizationActivities.query`
  * `policyanalyzer.serviceAccountKeyLastAuthenticationActivities.query`
  * `policyanalyzer.serviceAccountLastAuthenticationActivities.query`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Policyanalyzer Viewer Beta

(`roles/policyanalyzer.viewer`) Viewer role for policyanalyzer  |  `policyanalyzer.*`

  * `policyanalyzer.resourceAuthorizationActivities.query`
  * `policyanalyzer.serviceAccountKeyLastAuthenticationActivities.query`
  * `policyanalyzer.serviceAccountLastAuthenticationActivities.query`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Activity Analysis Viewer Beta

(`roles/policyanalyzer.activityAnalysisViewer`) Viewer user that can read all activity analysis.  |  `policyanalyzer.*`

  * `policyanalyzer.resourceAuthorizationActivities.query`
  * `policyanalyzer.serviceAccountKeyLastAuthenticationActivities.query`
  * `policyanalyzer.serviceAccountLastAuthenticationActivities.query`

  
  
## Policy Analyzer permissions

Permission | Included in roles  
---|---  
  
#### `policyanalyzer.resourceAuthorizationActivities.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Policyanalyzer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.admin) (`roles/policyanalyzer.admin`)  [Policyanalyzer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.viewer) (`roles/policyanalyzer.viewer`)  [Deny Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.denyAdmin) (`roles/iam.denyAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Activity Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.activityAnalysisViewer) (`roles/policyanalyzer.activityAnalysisViewer`)   
  
#### `policyanalyzer.serviceAccountKeyLastAuthenticationActivities.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Policyanalyzer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.admin) (`roles/policyanalyzer.admin`)  [Policyanalyzer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.viewer) (`roles/policyanalyzer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Activity Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.activityAnalysisViewer) (`roles/policyanalyzer.activityAnalysisViewer`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `policyanalyzer.serviceAccountLastAuthenticationActivities.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Policyanalyzer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.admin) (`roles/policyanalyzer.admin`)  [Policyanalyzer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.viewer) (`roles/policyanalyzer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Activity Analysis Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyanalyzer#policyanalyzer.activityAnalysisViewer) (`roles/policyanalyzer.activityAnalysisViewer`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
