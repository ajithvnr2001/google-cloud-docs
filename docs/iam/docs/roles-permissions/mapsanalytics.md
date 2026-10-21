---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/mapsanalytics/
title: Maps Analytics roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:05.714806+00:00
---

# Maps Analytics roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/mapsanalytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Maps Analytics roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Maps Analytics. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Maps Analytics roles

Role | Permissions  
---|---  
  
#### Mapsanalytics Admin Beta

(`roles/mapsanalytics.admin`) Admin role for mapsanalytics  |  `mapsanalytics.*`

  * `mapsanalytics.metricData.query`
  * `mapsanalytics.metricData.queryMobilitySolutionsOverageData`
  * `mapsanalytics.metricMetadata.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Maps Analytics Viewer Beta

(`roles/mapsanalytics.viewer`) Grants read-only access to all of the Maps Analytics resources.  |  `mapsanalytics.metricData.query` `mapsanalytics.metricMetadata.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.list` `serviceusage.groups.listMembers` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.values.test`  
  
#### Mobility Solutions Overages Viewer Beta

(`roles/mapsanalytics.mobilitySolutionsOverageViewer`) Grants read-only access to Mobility Solutions Overages metric data.  |  `mapsanalytics.metricData.queryMobilitySolutionsOverageData` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.list` `serviceusage.groups.listMembers` `serviceusage.services.list` `serviceusage.values.test`  
  
## Maps Analytics permissions

Permission | Included in roles  
---|---  
  
#### `mapsanalytics.metricData.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Mapsanalytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsanalytics#mapsanalytics.admin) (`roles/mapsanalytics.admin`)  [Maps Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsanalytics#mapsanalytics.viewer) (`roles/mapsanalytics.viewer`)   
  
#### `mapsanalytics.metricData.queryMobilitySolutionsOverageData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Mapsanalytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsanalytics#mapsanalytics.admin) (`roles/mapsanalytics.admin`)  [Mobility Solutions Overages Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsanalytics#mapsanalytics.mobilitySolutionsOverageViewer) (`roles/mapsanalytics.mobilitySolutionsOverageViewer`)   
  
#### `mapsanalytics.metricMetadata.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Mapsanalytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsanalytics#mapsanalytics.admin) (`roles/mapsanalytics.admin`)  [Maps Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsanalytics#mapsanalytics.viewer) (`roles/mapsanalytics.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
