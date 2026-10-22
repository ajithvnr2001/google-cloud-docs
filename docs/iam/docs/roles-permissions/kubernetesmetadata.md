---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata/
title: Kubernetes Metadata API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:22.879850+00:00
---

# Kubernetes Metadata API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Kubernetes Metadata API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Kubernetes Metadata API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Kubernetes Metadata API roles

Role | Permissions  
---|---  
  
#### Kubernetesmetadata Admin 

(`roles/kubernetesmetadata.admin`) Admin role for kubernetesmetadata  |  `kubernetesmetadata.*`

  * `kubernetesmetadata.metadata.config`
  * `kubernetesmetadata.metadata.publish`
  * `kubernetesmetadata.metadata.snapshot`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Kubernetesmetadata Viewer 

(`roles/kubernetesmetadata.viewer`) Viewer role for kubernetesmetadata  |  `kubernetesmetadata.metadata.config` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Metadata Publisher 

(`roles/kubernetesmetadata.publisher`) Publisher of Kubernetes clusters metadata  |  `kubernetesmetadata.*`

  * `kubernetesmetadata.metadata.config`
  * `kubernetesmetadata.metadata.publish`
  * `kubernetesmetadata.metadata.snapshot`

  
  
## Kubernetes Metadata API permissions

Permission | Included in roles  
---|---  
  
#### `kubernetesmetadata.metadata.config`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Kubernetesmetadata Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata#kubernetesmetadata.admin) (`roles/kubernetesmetadata.admin`)  [Kubernetesmetadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata#kubernetesmetadata.viewer) (`roles/kubernetesmetadata.viewer`)  [Anthos Multi-cloud Telemetry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.telemetryWriter) (`roles/gkemulticloud.telemetryWriter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Metadata Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata#kubernetesmetadata.publisher) (`roles/kubernetesmetadata.publisher`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Anthos Multi-Cloud Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent) (`roles/gkemulticloud.containerServiceAgent`) 

  
  
#### `kubernetesmetadata.metadata.publish`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Kubernetesmetadata Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata#kubernetesmetadata.admin) (`roles/kubernetesmetadata.admin`)  [Anthos Multi-cloud Telemetry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.telemetryWriter) (`roles/gkemulticloud.telemetryWriter`)  [Metadata Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata#kubernetesmetadata.publisher) (`roles/kubernetesmetadata.publisher`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Anthos Multi-Cloud Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent) (`roles/gkemulticloud.containerServiceAgent`) 

  
  
#### `kubernetesmetadata.metadata.snapshot`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Kubernetesmetadata Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata#kubernetesmetadata.admin) (`roles/kubernetesmetadata.admin`)  [Anthos Multi-cloud Telemetry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.telemetryWriter) (`roles/gkemulticloud.telemetryWriter`)  [Metadata Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/kubernetesmetadata#kubernetesmetadata.publisher) (`roles/kubernetesmetadata.publisher`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Edge Container Cluster Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.clusterServiceAgent) (`roles/edgecontainer.clusterServiceAgent`) 
  * [Anthos Multi-Cloud Container Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.containerServiceAgent) (`roles/gkemulticloud.containerServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
