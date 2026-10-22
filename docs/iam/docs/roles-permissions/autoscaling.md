---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling/
title: Cloud Autoscaling roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:52.449805+00:00
---

# Cloud Autoscaling roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Autoscaling roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Autoscaling. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Autoscaling roles

Role | Permissions  
---|---  
  
#### Autoscaling Admin Beta

(`roles/autoscaling.admin`) Admin role for autoscaling  |  `autoscaling.*`

  * `autoscaling.sites.getIamPolicy`
  * `autoscaling.sites.readRecommendations`
  * `autoscaling.sites.setIamPolicy`
  * `autoscaling.sites.writeMetrics`
  * `autoscaling.sites.writeState`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Autoscaling Editor Beta

(`roles/autoscaling.editor`) Editor role for autoscaling  |  `autoscaling.sites.getIamPolicy` `autoscaling.sites.readRecommendations` `autoscaling.sites.writeMetrics` `autoscaling.sites.writeState` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Autoscaling Viewer Beta

(`roles/autoscaling.viewer`) Viewer role for autoscaling  |  `autoscaling.sites.getIamPolicy` `autoscaling.sites.readRecommendations` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Autoscaling Metrics Writer Beta

(`roles/autoscaling.metricsWriter`) Access to write metrics for autoscaling site  |  `autoscaling.sites.writeMetrics`  
  
#### Autoscaling Recommendations Reader Beta

(`roles/autoscaling.recommendationsReader`) Access to read recommendations from autoscaling site  |  `autoscaling.sites.readRecommendations`  
  
#### Autoscaling Site Admin Beta

(`roles/autoscaling.sitesAdmin`) Full access to all autoscaling site features  |  `autoscaling.*`

  * `autoscaling.sites.getIamPolicy`
  * `autoscaling.sites.readRecommendations`
  * `autoscaling.sites.setIamPolicy`
  * `autoscaling.sites.writeMetrics`
  * `autoscaling.sites.writeState`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Autoscaling State Writer Beta

(`roles/autoscaling.stateWriter`) Access to write state for autoscaling site  |  `autoscaling.sites.writeState`  
  
## Cloud Autoscaling permissions

Permission | Included in roles  
---|---  
  
#### `autoscaling.sites.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Autoscaling Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.admin) (`roles/autoscaling.admin`)  [Autoscaling Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.editor) (`roles/autoscaling.editor`)  [Autoscaling Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.viewer) (`roles/autoscaling.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Autoscaling Site Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.sitesAdmin) (`roles/autoscaling.sitesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `autoscaling.sites.readRecommendations`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Autoscaling Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.admin) (`roles/autoscaling.admin`)  [Autoscaling Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.editor) (`roles/autoscaling.editor`)  [Autoscaling Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.viewer) (`roles/autoscaling.viewer`)  [Autoscaling Recommendations Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.recommendationsReader) (`roles/autoscaling.recommendationsReader`)  [Autoscaling Site Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.sitesAdmin) (`roles/autoscaling.sitesAdmin`)  [Dataflow Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker) (`roles/dataflow.worker`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
#### `autoscaling.sites.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Autoscaling Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.admin) (`roles/autoscaling.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Autoscaling Site Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.sitesAdmin) (`roles/autoscaling.sitesAdmin`)   
  
#### `autoscaling.sites.writeMetrics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Autoscaling Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.admin) (`roles/autoscaling.admin`)  [Autoscaling Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.editor) (`roles/autoscaling.editor`)  [Autoscaling Metrics Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.metricsWriter) (`roles/autoscaling.metricsWriter`)  [Autoscaling Site Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.sitesAdmin) (`roles/autoscaling.sitesAdmin`)  [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`)  [Dataflow Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker) (`roles/dataflow.worker`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Default Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent) (`roles/container.defaultNodeServiceAgent`) 
  * [[Deprecated] Kubernetes Engine Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.nodeServiceAgent) (`roles/container.nodeServiceAgent`) 
  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 
  * [RMA Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rapidmigrationassessment.serviceAgent) (`roles/rapidmigrationassessment.serviceAgent`) 

  
  
#### `autoscaling.sites.writeState`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Autoscaling Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.admin) (`roles/autoscaling.admin`)  [Autoscaling Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.editor) (`roles/autoscaling.editor`)  [Autoscaling Site Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.sitesAdmin) (`roles/autoscaling.sitesAdmin`)  [Autoscaling State Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/autoscaling#autoscaling.stateWriter) (`roles/autoscaling.stateWriter`)  [Dataflow Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker) (`roles/dataflow.worker`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Kubernetes Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.serviceAgent) (`roles/container.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
