---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudquotas/
title: Cloud Quotas roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:59.119974+00:00
---

# Cloud Quotas roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudquotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Quotas roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Quotas. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Quotas roles

Role | Permissions  
---|---  
  
#### Cloud Quotas Admin 

(`roles/cloudquotas.admin`) Full access to Cloud Quotas resources.  |  `cloudquotas.*`

  * `cloudquotas.quotas.get`
  * `cloudquotas.quotas.update`

`monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Quotas Viewer 

(`roles/cloudquotas.viewer`) Readonly access to Cloud Quotas resources.  |  `cloudquotas.quotas.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Cloud Quotas permissions

Permission | Included in roles  
---|---  
  
#### `cloudquotas.quotas.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Capacityplanner Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.admin) (`roles/capacityplanner.admin`)  [Capacity Planner Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`)  [Cloud Quotas Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudquotas#cloudquotas.admin) (`roles/cloudquotas.admin`)  [Cloud Quotas Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudquotas#cloudquotas.viewer) (`roles/cloudquotas.viewer`)  [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Capacity Planner](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.planner) (`roles/capacityplanner.planner`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Cloud Infrastructure Manager Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.agent) (`roles/config.agent`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaAdmin) (`roles/servicemanagement.quotaAdmin`)  [Quota Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaViewer) (`roles/servicemanagement.quotaViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `cloudquotas.quotas.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Quotas Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudquotas#cloudquotas.admin) (`roles/cloudquotas.admin`)  [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaAdmin) (`roles/servicemanagement.quotaAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
