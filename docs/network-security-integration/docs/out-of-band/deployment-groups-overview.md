---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview/
title: Mirroring deployment groups overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:56.862494+00:00
---

# Mirroring deployment groups overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Mirroring deployment groups overview Stay organized with collections  Save and categorize content based on your preferences. 

A _mirroring deployment group_ is a collection of [mirroring deployments](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployments-overview) that are set up across multiple zones. This collection represents a producer's mirroring service that the consumers can connect to.

A mirroring deployment group is identified by a unique URL identifier. This URL is used in the [mirroring endpoint group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview) to identify the producer mirroring service where the mirrored packets are sent for deep packet inspection.

This document provides a detailed overview of the mirroring deployment groups and their capabilities.

## Specifications

  * A mirroring deployment group is a global project-level resource.

  * Each mirroring deployment group is uniquely identified by a URL with the following elements:

    * **Project ID** : ID of the project.
    * **Location** : scope of the mirroring deployment group. Location is always set to `global`.
    * **Name** : mirroring deployment group name in the following format: 
      * A string 1-63 characters long
      * Includes only lowercase alphanumeric characters or hyphens (-)
      * Must start with a letter

To construct a unique URL identifier for a mirroring deployment group, use the following format:
    
    projects/PROJECT_ID/locations/global/mirroringDeploymentGroups/DEPLOYMENT_GROUP_ID
    

Replace the following:

    * `PROJECT_ID`: ID of the project

    * `DEPLOYMENT_GROUP_ID`: ID of the mirroring deployment group

For example, project `2345678432` in a `global` mirroring deployment `example-mirroring-deployment-group` has the following unique identifier:
    
    projects/2345678432/locations/global/mirroringDeploymentGroups/example-mirroring-deployment-group
    



  * You can use a single mirroring deployment group to inspect the mirrored traffic from multiple Virtual Private Cloud (VPC) instances across different projects and accounts.

  * If the deployment group doesn't have a deployment in a specific zone, then, on the consumer side, the packets in that zone are not mirrored.

  * To delete a deployment group, you must delete all the deployments in that deployment group.




## Identity and Access Management roles

Identity and Access Management (IAM) roles govern the following actions for managing the mirroring deployment groups:

  * Creating a mirroring deployment group in a project
  * Modifying or deleting a mirroring deployment group
  * Viewing details about a mirroring deployment group
  * Viewing all the mirroring deployment groups configured in your project



The following table describes the roles that are necessary for each step.

Ability | Necessary role  
---|---  
Create a new mirroring deployment group  | Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`) on the project where the mirroring deployment group is created.  
Modify an existing mirroring deployment group  | Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`) on the project where the mirroring deployment group is created.  
View details about the mirroring deployment group in a project  | Any of the following roles for the project: 

  * Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`)
  * Mirroring Deployment Viewer role (`networksecurity.mirroringDeploymentViewer`)

  
View all the mirroring deployment groups in your project  | Any of the following roles for the project: 

  * Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`)
  * Mirroring Deployment Viewer role (`networksecurity.mirroringDeploymentViewer`)

  
Delete a mirroring deployment group  | Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`) on the project.   
  
## Quotas

To view quotas associated with mirroring deployment groups, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## What's next

  * [Create and manage mirroring deployments](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployments)
  * [Create and manage mirroring deployment groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups)
  * [Network Security Integration overview](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)
  * [Monitor out-of-band integration](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/monitor-out-of-band-integration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
