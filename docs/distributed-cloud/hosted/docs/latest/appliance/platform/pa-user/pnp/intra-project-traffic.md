---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/intra-project-traffic/
title: Intra-project traffic network policies \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:56.662893+00:00
---

# Intra-project traffic network policies  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/intra-project-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Intra-project traffic network policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to configure intra-project traffic network policies in Google Distributed Cloud (GDC) air-gapped appliance.

Project network policies define either ingress or egress rules. You can define policies that allow communication within projects, between projects, and to external IP addresses.

## Before you begin

To configure intra-project traffic network policies, you must have the following:

  * The necessary identity and access roles. For more information, see [Prepare predefined roles and access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/pnp-overview#prepare-predefined-roles-and-access).
  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project).



## Create an intra-project traffic policy

For traffic within a project, GDC applies a predefined project network policy, the intra-project policy, to each project by default. By default, workloads in a project namespace have the ability to communicate with each other without exposing anything to external resources.

By default, there is no egress policy, so outbound traffic is allowed for all intra-project traffic. However, when you set a single egress policy, only the traffic that the policy specifies is allowed.

### Ingress intra-project traffic network policy

When you create a project, you implicitly create a default base `ProjectNetworkPolicy` that allows intra-project communication. This policy allows inbound traffic from other services in the same project.

You can remove the default policy, but be aware that this removal results in denying intra-project communication for all services and workloads within the project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
