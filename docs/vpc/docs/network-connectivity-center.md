---
url: https://docs.cloud.google.com/vpc/docs/network-connectivity-center/
title: Network Connectivity Center \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:47.363770+00:00
---

# Network Connectivity Center  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/network-connectivity-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Network Connectivity Center

This page provides a brief overview of Network Connectivity Center (NCC). You can use NCC to connect multiple VPC networks to each other.

NCC is an orchestration framework that lets you connect spoke resources to a central management resource called a hub.

When a hub uses VPC spokes, you can configure connectivity between VPC networks connected to the hub by exchanging [subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) between all or some of the VPC networks. VPC spokes attached to a single hub can reference VPC networks in the same project or a different project, including a project in a different organization.

An NCC hub can support up to [hundreds of VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-quotas).

For detailed information about NCC, see the [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

## What's next

  * To learn about VPC spokes, see [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview).
  * To create an NCC hub, see [Create a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub).
  * To create a VPC spoke, see [Create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
