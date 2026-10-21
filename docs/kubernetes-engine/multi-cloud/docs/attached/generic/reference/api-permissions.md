---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/reference/api-permissions/
title: Attached clusters API access control \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:56.247989+00:00
---

# Attached clusters API access control  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/reference/api-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/reference/api-permissions)



Send feedback 

#  Attached clusters API access control Stay organized with collections  Save and categorize content based on your preferences. 

To use the GKE attached clusters API, users must have specific Identity and Access Management (IAM) permissions on their Google Cloud account for access to GKE Multi-Cloud resources. GKE attached clusters includes two predefined roles that bundle together two commonly-used sets of permissions:

  * `gkemulticloud.viewer` (for read-only access) and
  * `gkemulticloud.admin`(to grant administrative control).



The permissions in these roles are:

### gkemulticloud.admin

  * gkemulticloud.*
  * resourcemanager.projects.get
  * resourcemanager.projects.list



### gkemulticloud.viewer

  * gkemulticloud.attachedClusters.get
  * gkemulticloud.attachedClusters.list
  * gkemulticloud.attachedServerConfigs.get
  * gkemulticloud.attachedClusters.generateInstallManifest
  * gkemulticloud.awsClusters.generateAccessToken
  * gkemulticloud.awsClusters.get
  * gkemulticloud.awsClusters.list
  * gkemulticloud.awsNodePools.get
  * gkemulticloud.awsNodePools.list
  * gkemulticloud.awsServerConfigs.get
  * gkemulticloud.azureClients.get
  * gkemulticloud.azureClients.list
  * gkemulticloud.azureClusters.generateAccessToken
  * gkemulticloud.azureClusters.get
  * gkemulticloud.azureClusters.list
  * gkemulticloud.azureNodePools.get
  * gkemulticloud.azureNodePools.list
  * gkemulticloud.azureServerConfigs.get
  * gkemulticloud.operations.get
  * gkemulticloud.operations.list
  * gkemulticloud.operations.wait
  * resourcemanager.projects.get
  * resourcemanager.projects.list



To learn about granting and revoking these permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
