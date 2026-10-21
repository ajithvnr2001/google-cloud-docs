---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/lustre/
title: Google Cloud Managed Lustre roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:29:56.345391+00:00
---

# Google Cloud Managed Lustre roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/lustre/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud Managed Lustre roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud Managed Lustre. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud Managed Lustre roles

Role | Permissions  
---|---  
  
#### Google Cloud Managed Lustre Admin 

(`roles/lustre.admin`) Full access to Google Cloud Managed Lustre resources.  |  `lustre.*`

  * `lustre.instances.create`
  * `lustre.instances.delete`
  * `lustre.instances.exportData`
  * `lustre.instances.get`
  * `lustre.instances.importData`
  * `lustre.instances.list`
  * `lustre.instances.rescheduleMaintenance`
  * `lustre.instances.update`
  * `lustre.locations.get`
  * `lustre.locations.list`
  * `lustre.operations.cancel`
  * `lustre.operations.delete`
  * `lustre.operations.get`
  * `lustre.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Cloud Managed Lustre Viewer 

(`roles/lustre.viewer`) Readonly access to Google Cloud Managed Lustre resources.  |  `lustre.instances.get` `lustre.instances.list` `lustre.locations.*`

  * `lustre.locations.get`
  * `lustre.locations.list`

`lustre.operations.get` `lustre.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Google Cloud Managed Lustre permissions

Permission | Included in roles  
---|---  
  
#### `lustre.instances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `lustre.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `lustre.instances.exportData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)   
  
#### `lustre.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  [Google Cloud Managed Lustre Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.viewer) (`roles/lustre.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `lustre.instances.importData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `lustre.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  [Google Cloud Managed Lustre Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.viewer) (`roles/lustre.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `lustre.instances.rescheduleMaintenance`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)   
  
#### `lustre.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `lustre.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  [Google Cloud Managed Lustre Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.viewer) (`roles/lustre.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `lustre.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  [Google Cloud Managed Lustre Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.viewer) (`roles/lustre.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `lustre.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `lustre.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `lustre.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  [Google Cloud Managed Lustre Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.viewer) (`roles/lustre.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
#### `lustre.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Google Cloud Managed Lustre Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`)  [Google Cloud Managed Lustre Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.viewer) (`roles/lustre.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [Cluster Director Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.serviceAgent) (`roles/hypercomputecluster.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
