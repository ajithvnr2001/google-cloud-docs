---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/fix-sla/
title: Fix SLA eligibility problems \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:18.869091+00:00
---

# Fix SLA eligibility problems  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/fix-sla/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Fix SLA eligibility problems Stay organized with collections  Save and categorize content based on your preferences. 

This document describes common problems that you might encounter with the SLA eligibility of your Cloud Interconnect connection groups or VLAN attachment groups, and provides troubleshooting steps to help you resolve those problems.

## Topology capability blockers

The following sections describe problems with the topology of your interconnect groups or VLAN attachment groups. For Cloud Interconnect connection groups, the `configured.topologyCapability.intendedCapabilityBlockers` field returns blockers that map to each of these sections. For VLAN Attachment groups, the same information is returned by the `configured.availabilitySla.intendedSlaBlockers` field. The solutions generally involve modifying your interconnect connection group resource.

### No interconnects

If you receive this blocker, then your connection group doesn't contain any Cloud Interconnect connections. To resolve this blocker, see [Create Cloud Interconnect connections within a connection group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups#create-connections) or [Add existing Cloud Interconnect connections to a group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups#add-connections).

### No attachments

If you receive this blocker, then your VLAN attachment group doesn't contain any VLAN attachments. To resolve this blocker, see [Add VLAN attachments to a VLAN attachment group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#add-to-group).

### Incompatible metros

If you receive this blocker, then your connections or VLAN attachments need to be configured in additional metropolitan areas (metros). Check the `configured.topologyCapability.intendedCapabilityBlockers.metros` field (for connection groups) or `configured.availabilitySla.intendedSlaBlockers` field (for VLAN attachment groups) to identify the metro or metros in which you have already deployed resources, then create or add a connection or VLAN attachment to the group within a new metro. To resolve this blocker, see the following pages:

  * Connection groups: 
    * [Create Cloud Interconnect connections within a connection group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups#create-connections)
    * [Add existing Cloud Interconnect connections to a group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups#add-connections).
  * VLAN attachment groups: 
    * [Add VLAN attachments to a VLAN attachment group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#add-to-group).



### Incompatible regions

If you receive this blocker, then your VLAN attachments need to be configured in additional regions. Check the `configured.availabilitySla.intendedSlaBlockers.regions` field to identify the region or regions in which you have already deployed resources, then create or add a VLAN attachment to the group within a new region. To resolve this blocker, see [Add VLAN attachments to a VLAN attachment group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#add-to-group).

### No interconnects in metro and zone

If you receive this blocker, then your connections within the same metro need to be configured in different edge availability domains. Check the `configured.topologyCapability.intendedCapabilityBlockers.zones` field to identify the zone in which you are missing an interconnect connection, then see [Create Cloud Interconnect connections within a connection group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups#create-connections) or [Add existing Cloud Interconnect connections to a group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups#add-connections) to resolve this blocker.

### No attachments in metro and zone

If you receive this blocker, then your VLAN attachments within the same metro need to be configured in different edge availability domains. Check the `configured.availabilitySla.intendedSlaBlockers.zones` field to identify the zone in which you are missing a VLAN attachment, then see [Add VLAN attachments to a VLAN attachment group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#add-to-group) to resolve this blocker.

### Missing global routing

If you receive this blocker, then your VPC network's dynamic routing mode isn't set to **Global**. To resolve this blocker, [change your VPC network's dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes#change-network-modes) to **Global**.

### Not available

If you receive this blocker, then you have chosen a level of reliability that isn't generally available with your configured connection group or VLAN attachment group. To resolve this blocker, [contact support](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/getting-support).

## Other

If you receive this blocker, then there is an issue with your deployment that doesn't fall under the other categories. To resolve this blocker, [contact support](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
