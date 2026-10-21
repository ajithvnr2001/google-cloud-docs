---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/pnp-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:56.851517+00:00
---

# Overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/pnp-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of project network policies in Google Distributed Cloud (GDC) air-gapped appliance.

Project network policies define either ingress or egress rules. Unlike Kubernetes network policies, you can only specify one policy type for a policy.

For traffic within a project, GDC applies a predefined project network policy, the intra-project policy, to each project by default.

Services and workloads in a project are isolated from external services and workloads by default. However, services and workloads from different project namespaces can communicate with each other by applying cross-project traffic network policies.

Ingress and egress firewall rules are the main components of project network policies and determine which types of traffic are allowed in and out of your network. To set firewall rules for your project namespace in GDC, use the GDC console.

## Security and connectivity

By default, services and workloads in a project are isolated within that project. They cannot communicate with external services and workloads without configuring a network policy.

To set a network policy for your project namespace in GDC, use the `ProjectNetworkPolicy` resource. This resource lets you define policies, which allow communication within projects, between projects, to external IP addresses, and from external IP addresses. Also, you can transfer workloads out from a project only if you [disable data exfiltration protection for the project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/data-exfiltration#prevent-data-exfiltration).

GDC project network policies are additive. The resulting enforcement for a workload is an _any_ match for the traffic flow against the union of all policies applied to that workload. When multiple policies are present, the rules for each policy are additively combined, allowing traffic if it matches at least one of the rules.

Furthermore, after you apply a single policy, all traffic you don't specify is denied. Therefore, when you apply one or more policies that select a workload as the subject, only the traffic that a policy specifies is allowed.

When you use a well-known IP address you allocate for the project, it performs a source network address translation (NAT) on the outbound traffic from the organization.

## Workload-level network policies

You can create workload-level network policies to define fine-grained access control for individual VMs and pods within a project. These policies act like firewalls for your workloads, controlling traffic flow based on labels to enhance security and isolate applications. This granularity allows stricter control over which workloads can communicate with each other within and across projects.

## Prepare predefined roles and access

To configure project network policies, you must have the necessary identity and access roles:

  * Project NetworkPolicy Admin: manages project network policies in the project namespace. Ask your Organization IAM Admin to grant you the Project NetworkPolicy Admin (`project-networkpolicy-admin`) cluster role.



## What's next

  * [Create intra-project traffic network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/intra-project-traffic)
  * [Create cross-project traffic network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/cross-project-traffic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
