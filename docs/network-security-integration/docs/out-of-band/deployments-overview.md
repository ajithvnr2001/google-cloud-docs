---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployments-overview/
title: Mirroring deployments overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:03.301922+00:00
---

# Mirroring deployments overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployments-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Mirroring deployments overview Stay organized with collections  Save and categorize content based on your preferences. 

A _mirroring deployment_ is a zonal deployment of a producer's third-party appliances. Mirroring deployment acts as a backend to an internal passthrough Network Load Balancer, providing network services on the traffic mirrored from the consumer networks.

The mirroring deployments are grouped in mirroring deployment groups across different locations within a project for easier consumption and management.

This document provides a detailed overview of mirroring deployments and their capabilities.

## Specifications

  * A mirroring deployment is a project-level resource created at the zonal-level.

  * You can deploy only one mirroring deployment per zone and group.

  * Each mirroring deployment is associated with a mirroring deployment group. You can associate a mirroring deployment with exactly one deployment group.

  * A mirroring deployment references the forwarding rule that points to the backend services where the third-party appliances are deployed to provide mirroring services. This forwarding rule handles the traffic sent to the mirroring deployment. The forwarding rule must use the network specified in the mirroring deployment group.

  * Each mirroring deployment is uniquely identified by a URL with the following elements:

    * **Project ID** : ID of the project.
    * **Location** : scope of the mirroring deployment. Location is always set to the zone it resides in.
    * **Name** : mirroring deployment name in the following format: 
      * A string 1-63 characters long
      * Includes only lowercase alphanumeric characters or hyphens (-)
      * Must start with a letter

To construct a unique URL identifier for a mirroring deployment, use the following format:
    
    projects/PROJECT_ID/locations/ZONE/mirroringDeployments/DEPLOYMENT
    

Replace the following:

    * `PROJECT_ID`: ID of the project

    * `ZONE`: zone of the mirroring deployment

    * `DEPLOYMENT`: name of the mirroring deployment

For example, project `2345678432` in zone `us-east1-a` with mirroring deployment `example-mirroring-deployments` has the following unique identifier:
    
    projects/2345678432/locations/us-east1-a/mirroringDeployments/example-mirroring-deployments
    




## Identity and Access Management roles

Identity and Access Management (IAM) roles govern the following actions for managing the mirroring deployments:

  * Creating a mirroring deployment in a project
  * Modifying or deleting a mirroring deployment
  * Viewing details about a mirroring deployment
  * Viewing all the mirroring deployments configured in your project



The following table describes the roles that are necessary for each step.

Ability | Necessary role  
---|---  
Create a new mirroring deployment  | Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`) on the project where the mirroring deployment is created.  
Modify an existing mirroring deployment  | Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`) on the project where the mirroring deployment is created.  
View details about the mirroring deployment in a project  | Any of the following roles for the project: 

  * Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`)
  * Mirroring Deployment Viewer role (`networksecurity.mirroringDeploymentViewer`)

  
View all the mirroring deployments in your project  | Any of the following roles for the project: 

  * Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`)
  * Mirroring Deployment Viewer role (`networksecurity.mirroringDeploymentViewer`)

  
Delete a mirroring deployment  | Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentAdmin`) on the project.   
  
## Quotas

To view quotas associated with mirroring deployments, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## What's next

  * [Create and manage mirroring deployments](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployments)
  * [Mirroring deployment groups overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview)
  * [Create and manage mirroring deployment groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
