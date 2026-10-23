---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/permissions-reference/
title: Multicast permissions reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:56.330993+00:00
---

# Multicast permissions reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/permissions-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Multicast permissions reference

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes the Identity and Access Management (IAM) roles and permissions that are required to use multicast. For more information about granting roles and permissions, see the [IAM documentation](https://docs.cloud.google.com/iam/docs/overview).

## Multicast roles

The following predefined roles are available for multicast:

Role | Permissions  
---|---  
  
#### Multicast Admin 

(`roles/networkservices.multicastAdmin`) Multicast Admin is responsible for setting up and managing multicast configurations.  |  `compute.forwardingRules.get` `compute.forwardingRules.list` `compute.networks.get` `compute.networks.list` `networkconnectivity.internalRanges.*`

  * `networkconnectivity.internalRanges.create`
  * `networkconnectivity.internalRanges.delete`
  * `networkconnectivity.internalRanges.get`
  * `networkconnectivity.internalRanges.list`

`networkconnectivity.operations.get` `networkconnectivity.operations.list` `networkservices.locations.*`

  * `networkservices.locations.get`
  * `networkservices.locations.list`

`networkservices.multicastConsumerAssociations.*`

  * `networkservices.multicastConsumerAssociations.create`
  * `networkservices.multicastConsumerAssociations.delete`
  * `networkservices.multicastConsumerAssociations.get`
  * `networkservices.multicastConsumerAssociations.list`

`networkservices.multicastDomainActivations.*`

  * `networkservices.multicastDomainActivations.create`
  * `networkservices.multicastDomainActivations.delete`
  * `networkservices.multicastDomainActivations.get`
  * `networkservices.multicastDomainActivations.list`
  * `networkservices.multicastDomainActivations.update`

`networkservices.multicastDomainGroups.*`

  * `networkservices.multicastDomainGroups.create`
  * `networkservices.multicastDomainGroups.delete`
  * `networkservices.multicastDomainGroups.get`
  * `networkservices.multicastDomainGroups.list`

`networkservices.multicastDomains.*`

  * `networkservices.multicastDomains.create`
  * `networkservices.multicastDomains.delete`
  * `networkservices.multicastDomains.get`
  * `networkservices.multicastDomains.list`

`networkservices.multicastGroupConsumerActivations.*`

  * `networkservices.multicastGroupConsumerActivations.create`
  * `networkservices.multicastGroupConsumerActivations.delete`
  * `networkservices.multicastGroupConsumerActivations.get`
  * `networkservices.multicastGroupConsumerActivations.list`
  * `networkservices.multicastGroupConsumerActivations.update`

`networkservices.multicastGroupProducerActivations.*`

  * `networkservices.multicastGroupProducerActivations.create`
  * `networkservices.multicastGroupProducerActivations.delete`
  * `networkservices.multicastGroupProducerActivations.get`
  * `networkservices.multicastGroupProducerActivations.list`

`networkservices.multicastGroupRangeActivations.*`

  * `networkservices.multicastGroupRangeActivations.create`
  * `networkservices.multicastGroupRangeActivations.delete`
  * `networkservices.multicastGroupRangeActivations.get`
  * `networkservices.multicastGroupRangeActivations.list`
  * `networkservices.multicastGroupRangeActivations.update`

`networkservices.multicastGroupRanges.*`

  * `networkservices.multicastGroupRanges.create`
  * `networkservices.multicastGroupRanges.delete`
  * `networkservices.multicastGroupRanges.get`
  * `networkservices.multicastGroupRanges.list`
  * `networkservices.multicastGroupRanges.update`

`networkservices.multicastProducerAssociations.*`

  * `networkservices.multicastProducerAssociations.create`
  * `networkservices.multicastProducerAssociations.delete`
  * `networkservices.multicastProducerAssociations.get`
  * `networkservices.multicastProducerAssociations.list`

`networkservices.operations.get` `networkservices.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Multicast Viewer 

(`roles/networkservices.multicastViewer`) Read-only access to multicast configurations.  |  `networkservices.locations.*`

  * `networkservices.locations.get`
  * `networkservices.locations.list`

`networkservices.multicastConsumerAssociations.get` `networkservices.multicastConsumerAssociations.list` `networkservices.multicastDomainActivations.get` `networkservices.multicastDomainActivations.list` `networkservices.multicastDomainGroups.get` `networkservices.multicastDomainGroups.list` `networkservices.multicastDomains.get` `networkservices.multicastDomains.list` `networkservices.multicastGroupConsumerActivations.get` `networkservices.multicastGroupConsumerActivations.list` `networkservices.multicastGroupProducerActivations.get` `networkservices.multicastGroupProducerActivations.list` `networkservices.multicastGroupRangeActivations.get` `networkservices.multicastGroupRangeActivations.list` `networkservices.multicastGroupRanges.get` `networkservices.multicastGroupRanges.list` `networkservices.multicastProducerAssociations.get` `networkservices.multicastProducerAssociations.list` `networkservices.operations.get` `networkservices.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Multicast permissions

The following table lists the specific permissions required to use multicast resources.

Resource | Permissions  
---|---  
Multicast administrator resources  
Multicast domain group |  `networkservices.multicastDomainGroups.*`

  * `networkservices.multicastDomainGroups.create`
  * `networkservices.multicastDomainGroups.delete`
  * `networkservices.multicastDomainGroups.get`
  * `networkservices.multicastDomainGroups.list`

  
Multicast domain |  `networkservices.multicastDomains.*`

  * `networkservices.multicastDomains.create`
  * `networkservices.multicastDomains.delete`
  * `networkservices.multicastDomains.get`
  * `networkservices.multicastDomains.list`

  
Multicast domain activation |  `networkservices.multicastDomainActivations.*`

  * `networkservices.multicastDomainActivations.create`
  * `networkservices.multicastDomainActivations.delete`
  * `networkservices.multicastDomainActivations.update`
  * `networkservices.multicastDomainActivations.get`
  * `networkservices.multicastDomainActivations.list`

  
Multicast group range |  `networkservices.multicastGroupRanges.*`

  * `networkservices.multicastGroupRanges.create`
  * `networkservices.multicastGroupRanges.delete`
  * `networkservices.multicastGroupRanges.update`
  * `networkservices.multicastGroupRanges.get`
  * `networkservices.multicastGroupRanges.list`

  
Multicast group range activation |  `networkservices.multicastGroupRangeActivations.*`

  * `networkservices.multicastGroupRangeActivations.create`
  * `networkservices.multicastGroupRangeActivations.delete`
  * `networkservices.multicastGroupRangeActivations.update`
  * `networkservices.multicastGroupRangeActivations.get`
  * `networkservices.multicastGroupRangeActivations.list`

  
Multicast producer resources  
Multicast producer association |  `networkservices.multicastProducerAssociations.*`

  * `networkservices.multicastProducerAssociations.create`
  * `networkservices.multicastProducerAssociations.delete`
  * `networkservices.multicastProducerAssociations.get`
  * `networkservices.multicastProducerAssociations.list`

  
Multicast group producer activation |  `networkservices.multicastGroupProducerActivations.*`

  * `networkservices.multicastGroupProducerActivations.create`
  * `networkservices.multicastGroupProducerActivations.delete`
  * `networkservices.multicastGroupProducerActivations.get`
  * `networkservices.multicastGroupProducerActivations.list`

  
Multicast consumer resources  
Multicast consumer association |  `networkservices.multicastConsumerAssociations.*`

  * `networkservices.multicastConsumerAssociations.create`
  * `networkservices.multicastConsumerAssociations.delete`
  * `networkservices.multicastConsumerAssociations.get`
  * `networkservices.multicastConsumerAssociations.list`

  
Multicast group consumer activation |  `networkservices.multicastGroupConsumerActivations.*`

  * `networkservices.multicastGroupConsumerActivations.create`
  * `networkservices.multicastGroupConsumerActivations.delete`
  * `networkservices.multicastGroupConsumerActivations.update`
  * `networkservices.multicastGroupConsumerActivations.get`
  * `networkservices.multicastGroupConsumerActivations.list`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
