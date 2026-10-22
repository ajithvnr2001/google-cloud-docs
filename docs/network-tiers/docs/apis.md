---
url: https://docs.cloud.google.com/network-tiers/docs/apis/
title: APIs and reference \u00a0|\u00a0 Network Service Tiers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:13.194387+00:00
---

# APIs and reference  |  Network Service Tiers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-tiers/docs/apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Service Tiers ](https://docs.cloud.google.com/network-tiers/docs)
  * [ Reference ](https://docs.cloud.google.com/network-tiers/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# APIs and reference

This page describes Google Cloud resources relevant to Network Service Tiers. For procedures and examples, see [Using Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/set-network-tier).

The Network Service Tiers APIs and `gcloud` commands are part of Compute Engine.

## gcloud CLI and API reference

### Addresses

Used to create, edit, and manage internal and external IP address resources that can be assigned to virtual machine (VM) instances and forwarding rules for load balancers. Internal IP addresses and global external IP addresses are always Premium Tier. Regional external IP addresses can use either Standard or Premium Tier.

  * [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses)
  * [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses)



### Forwarding rules

Used to create, edit, and manage forwarding rules in your Virtual Private Cloud (VPC) network. Forwarding rules with a load balancing scheme of `EXTERNAL` define paths for sending traffic from outside your VPC network to a load balancer or VM instances in your VPC network.

External forwarding rules can be either global or regional. Global external forwarding rules are always Premium Tier. Regional external forwarding rules can use either Standard or Premium Tier.

  * [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules)
  * [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules)



### Instances

Used to create and modify VM instances in your VPC network.

  * [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances)
  * [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances)



### Instance templates

Used to create and modify instance templates. Instance templates are used by managed instance groups. Instance groups are one type of backend for load balancers.

  * [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates)
  * [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates)



### Projects

Used to set the default network tier to apply to resources in a project. This default can be overridden on a resource-by-resource basis.

  * [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info)
  * [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
