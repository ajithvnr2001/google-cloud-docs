---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/api-permissions/
title: API roles and permissions \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:22.559138+00:00
---

# API roles and permissions  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/api-permissions/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/apis)



Send feedback 

#  API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS has specific Identity and Access Management (IAM) permissions. Those permissions are described in the following tables. For instructions on managing permissions, see [Granting, Changing, and Revoking Access to Resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## GKE on AWS API permissions

The GKE on AWS API includes the predefined `gkemulticloud.viewer`, and `gkemulticloud.admin` roles. These roles are described in the following table:

Role | Permissions  
---|---  
  
#### Anthos Multi-cloud Admin 

(`roles/gkemulticloud.admin`) Admin access to Anthos Multi-cloud resources.  |  `gkemulticloud.*`

  * `gkemulticloud.attachedClusters.create`
  * `gkemulticloud.attachedClusters.createTagBinding`
  * `gkemulticloud.attachedClusters.delete`
  * `gkemulticloud.attachedClusters.deleteTagBinding`
  * `gkemulticloud.attachedClusters.generateInstallManifest`
  * `gkemulticloud.attachedClusters.get`
  * `gkemulticloud.attachedClusters.import`
  * `gkemulticloud.attachedClusters.list`
  * `gkemulticloud.attachedClusters.listEffectiveTags`
  * `gkemulticloud.attachedClusters.listTagBindings`
  * `gkemulticloud.attachedClusters.update`
  * `gkemulticloud.attachedServerConfigs.get`
  * `gkemulticloud.awsClusters.create`
  * `gkemulticloud.awsClusters.delete`
  * `gkemulticloud.awsClusters.generateAccessToken`
  * `gkemulticloud.awsClusters.get`
  * `gkemulticloud.awsClusters.getAdminKubeconfig`
  * `gkemulticloud.awsClusters.list`
  * `gkemulticloud.awsClusters.update`
  * `gkemulticloud.awsNodePools.create`
  * `gkemulticloud.awsNodePools.delete`
  * `gkemulticloud.awsNodePools.get`
  * `gkemulticloud.awsNodePools.list`
  * `gkemulticloud.awsNodePools.update`
  * `gkemulticloud.awsServerConfigs.get`
  * `gkemulticloud.azureClients.create`
  * `gkemulticloud.azureClients.delete`
  * `gkemulticloud.azureClients.get`
  * `gkemulticloud.azureClients.list`
  * `gkemulticloud.azureClusters.create`
  * `gkemulticloud.azureClusters.delete`
  * `gkemulticloud.azureClusters.generateAccessToken`
  * `gkemulticloud.azureClusters.get`
  * `gkemulticloud.azureClusters.getAdminKubeconfig`
  * `gkemulticloud.azureClusters.list`
  * `gkemulticloud.azureClusters.update`
  * `gkemulticloud.azureNodePools.create`
  * `gkemulticloud.azureNodePools.delete`
  * `gkemulticloud.azureNodePools.get`
  * `gkemulticloud.azureNodePools.list`
  * `gkemulticloud.azureNodePools.update`
  * `gkemulticloud.azureServerConfigs.get`
  * `gkemulticloud.operations.cancel`
  * `gkemulticloud.operations.delete`
  * `gkemulticloud.operations.get`
  * `gkemulticloud.operations.list`
  * `gkemulticloud.operations.wait`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Anthos Multi-cloud Viewer 

(`roles/gkemulticloud.viewer`) Viewer access to Anthos Multi-cloud resources.  |  `gkemulticloud.attachedClusters.generateInstallManifest` `gkemulticloud.attachedClusters.get` `gkemulticloud.attachedClusters.list` `gkemulticloud.attachedClusters.listEffectiveTags` `gkemulticloud.attachedClusters.listTagBindings` `gkemulticloud.attachedServerConfigs.get` `gkemulticloud.awsClusters.generateAccessToken` `gkemulticloud.awsClusters.get` `gkemulticloud.awsClusters.list` `gkemulticloud.awsNodePools.get` `gkemulticloud.awsNodePools.list` `gkemulticloud.awsServerConfigs.get` `gkemulticloud.azureClients.get` `gkemulticloud.azureClients.list` `gkemulticloud.azureClusters.generateAccessToken` `gkemulticloud.azureClusters.get` `gkemulticloud.azureClusters.list` `gkemulticloud.azureNodePools.get` `gkemulticloud.azureNodePools.list` `gkemulticloud.azureServerConfigs.get` `gkemulticloud.operations.get` `gkemulticloud.operations.list` `gkemulticloud.operations.wait` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## What's next

Additional IAM roles, such as owner and editor, include GKE on AWS permissions. For more information, see the complete [IAM Permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference) list.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
