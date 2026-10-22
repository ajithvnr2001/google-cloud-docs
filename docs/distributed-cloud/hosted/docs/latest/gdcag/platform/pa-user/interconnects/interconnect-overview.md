---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:50.745380+00:00
---

# Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the workflow for setting up a direct connection between your on-premises network and Google's network. It explains the steps involved in configuring an interconnect in Google Distributed Cloud (GDC) air-gapped.

This page is for developers within the application operator group who want to establish a secure air-gapped connection where they need to increase bandwidth with low latency. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

You must coordinate with the infrastructure operator group to successfully configure an interconnect. Submit a ticket in the GDC portal requesting an interconnect with your chosen specifications, such as 10 G of redundant connectivity.

## Interconnect creation process

To create an interconnect or VLAN attachment, you and the IO must create all of the following custom resources in the specified order:

  1. `InterconnectLink`: a representation of the physical cable that connects you to a GDC instance. The IO configures this resource.
  2. `InterconnectGroup`: a logical grouping of interconnect links that share a common purpose. The IO configures this resource.
  3. `AttachmentGroup`: a collection of VLAN attachments that share access to a set of organizations. You configure this resource.
  4. `RoutePolicy`: specifies what subnets are allowed to be advertised across the VLAN attachment. You must ask the IO to configure this resource.
  5. `InterconnectAttachment`: the VLAN attachment. This resource links your network's VLAN to a GDC instance with BGP for routing, enabling private and controlled access. You configure this resource.



## Interconnect types

The `InterconnectGroup` resource has an `interconnectType` field, and the `InterconnectAttachment` resource has a matching `parentInterconnectType` field. VLAN attachments that you create in your organization must use the `DirectConnect` type. With `DirectConnect`, the `AttachmentGroup` resource can use any unique identifier.

**Warning:** The `CustomerPeering` type is on the deprecation path. Don't use it for new interconnects. Use `DirectConnect` instead.

## Interconnection creation for a multi-zone universe

If you are configuring interconnects for a multi-zone universe, you must follow the requirement for zonal symmetry. To access services and resources in a particular zone, you must create an interconnect that connects your network to that zone. In the case of a [multi-zone universe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview#deployment-hierarchy-overview), you must create an interconnect for each zone in that universe. One interconnect does not work across zones. For the multi-zone configuration, each interconnect must be identical to one another for each zone in the multi-zone universe.

## Prepare predefined roles and permissions

To interact with interconnect resources, you must have access to the following identity and access roles:

  * Ask your IAM Org Admin to grant you the Interconnect Admin (`interconnect-admin`) cluster role. For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).



## Create or update interconnects

The instructions in this section specify creation operations. However, you can also use these instructions to update existing interconnect resources. Update the YAML files and apply the updated file using the command `kubectl apply -f`.

## What's next

  * [Create an attachment group](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/create-attachment-group)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
