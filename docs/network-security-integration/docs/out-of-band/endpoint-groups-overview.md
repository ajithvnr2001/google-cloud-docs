---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview/
title: Mirroring endpoint groups overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:04.102546+00:00
---

# Mirroring endpoint groups overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Mirroring endpoint groups overview Stay organized with collections  Save and categorize content based on your preferences. 

An endpoint group is a consumer resource that references a producer deployment group. This page provides a detailed overview of mirroring endpoint groups and their capabilities.

## Mirroring endpoint groups

We recommend that you create the mirroring endpoint group in a project owned by your security administrator. To create the mirroring endpoint group associations, the security administrator must assign the Mirroring Endpoint Admin (`roles/networksecurity.mirroringAdmin`) and Mirroring Endpoint Network Admin (`roles/networksecurity.mirroringEndpointNetworkAdmin`) roles to the project or to the network administrator.

For more information about mirroring endpoint group association, see [Mirroring endpoint group association](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations).

## Specifications

  * A mirroring endpoint group is a project-level resource created at the global level.
  * Network Security Integration uses Packet Mirroring technology to mirror the traffic from the Google Cloud workloads in a Virtual Private Cloud (VPC) network to the mirroring endpoint groups.
  * The security profile redirects the workload traffic in a VPC network to the mirroring endpoint group only if the mirroring rules are configured to be applied to this flow and the network is associated with the mirroring endpoint group.
  * The mirroring rules add a VPC network identifier to each packet redirected to the mirroring endpoint groups for the deep packet inspection. If you have multiple VPC networks with overlapping IP address ranges, this network identifier helps to ensure that each redirected packet is correctly associated with its VPC network.
  * You can create a mirroring endpoint group globally and associate it with one or more VPC networks to monitor workloads. You use [mirroring endpoint group association](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations) to attach a mirroring endpoint group to a VPC network.
  * You can delete a mirroring endpoint group only when there are no VPC networks associated with it.



## Mirroring endpoints

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A mirroring endpoint is a Google-managed zonal resource that acts as the broker component to mirror traffic to multiple producer networks. The mirroring endpoint receives mirrored traffic from the consumer's network and replicates it to multiple producer networks. For more information about how to create and manage mirroring endpoints, see [Create and manage mirroring endpoints](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoints).

## Mirroring endpoint group associations

Mirroring endpoint group association is a project-level resource. Mirroring endpoint group association links mirroring endpoint groups to a VPC network to make their traffic eligible for inspection. After a mirroring endpoint group is associated, any traffic matching mirroring rules is replicated and sent to the attached mirroring deployment group. For more information about how to create and manage mirroring endpoint group associations, see [Create and manage mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations).

## Identity and Access Management roles

Identity and Access Management (IAM) roles govern the following actions for managing the mirroring endpoint groups:

  * Creating a mirroring endpoint group in a project
  * Modifying or deleting a mirroring endpoint group
  * Viewing details about a mirroring endpoint group
  * Viewing all the mirroring endpoint groups configured in a project



The following table describes the roles that are necessary for each step.

Ability | Necessary role  
---|---  
Create a new mirroring endpoint group  | Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`) on the project where the mirroring endpoint group is created.  
Modify an existing mirroring endpoint group  | Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`) on the project.  
View details about the mirroring endpoint group in a project  | Any of the following roles for the project: 

  * Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`)
  * Mirroring Endpoint Viewer role (`roles/networksecurity.mirroringEndpointViewer`)

  
View all the mirroring endpoint groups in a project  | Any of the following roles for the project: 

  * Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`)
  * Mirroring Endpoint Viewer role (`roles/networksecurity.mirroringEndpointViewer`)

  
  
IAM roles govern the following actions for the mirroring endpoint group associations:

  * Creating a mirroring endpoint group association in a project
  * Modifying or deleting a mirroring endpoint group association
  * Viewing details of a mirroring endpoint group association
  * Viewing all the mirroring endpoint group associations configured in a project



The following table describes the roles that are necessary for each step.

Ability | Necessary role  
---|---  
Create a mirroring endpoint group association  |  Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`) on the project where the mirroring endpoint group association is created.  Mirroring Endpoint User role (`roles/networksecurity.mirroringEndpointUser`) on the project, which represents permissions to associate the VPC (which the user is an administrator of) to the mirroring endpoint group (which is an organization-owned resource, not necessarily owned by the VPC owner).   
Modify (update or delete) the mirroring endpoint group associations  | Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`) on the project where the VPC network exists.   
View details about the mirroring endpoint group association in a project  |  Any of the following roles: 

  * Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`)
  * Mirroring Endpoint Viewer role (`roles/networksecurity.mirroringEndpointViewer`)

  
View all of the mirroring endpoint group associations in a project  | Any of the following roles: 

  * Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`)
  * Mirroring Endpoint Viewer role (`roles/networksecurity.mirroringEndpointViewer`)

  
  
## Quotas

To view quotas associated with mirroring endpoint groups, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## What's next

  * [Network Security Integration overview](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)
  * [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview)
  * [Monitor out-of-band integration](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/monitor-out-of-band-integration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
