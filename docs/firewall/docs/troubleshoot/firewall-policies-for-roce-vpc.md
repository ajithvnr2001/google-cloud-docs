---
url: https://docs.cloud.google.com/firewall/docs/troubleshoot/firewall-policies-for-roce-vpc/
title: Troubleshoot Cloud NGFW policies for RoCE network profiles \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:01.766575+00:00
---

# Troubleshoot Cloud NGFW policies for RoCE network profiles  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/troubleshoot/firewall-policies-for-roce-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Troubleshoot Cloud NGFW policies for RoCE network profiles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot common issues that you might encounter when setting up Cloud Next Generation Firewall (Cloud NGFW) policies for Virtual Private Cloud (VPC) networks with the remote direct memory access (RDMA) over converged ethernet (RoCE) network profile.

### Default policy allows all connections

This issue occurs when you don't associate any firewall policy for a a VPC network with the RoCE network profile.

To resolve this issue, define a firewall policy for your VPC network with the RoCE network profile. If you don't define a policy, all virtual machine (VM) instances in the same VPC network connect to one another by default. For more information, see [Create a network with the RDMA network profile](https://docs.cloud.google.com/firewall/docs/create-manage-roce-vpcs#create_a_network_with_the_rdma_network_profile).

### Implied firewall rule allows ingress traffic

This issue occurs when a RoCE firewall policy attaches to a VPC network by using the RoCE network profile and no other matching rules.

To resolve this issue, understand that the implied firewall rule for a RoCE network firewall policy is `INGRESS ALLOW ALL`. This rule applies if no other rules match.

### Cannot enable logging on the implied rule

This issue occurs when you attempt to enable logging on the implied firewall rule for a RoCE firewall policy. You cannot enable logging on the implied rule. For more information, see [Implied firewall rules](https://docs.cloud.google.com/firewall/docs/firewall-for-roce#implied_firewall_rules).

To resolve this issue, create a separate `ALLOW` or `DENY` rule. Use the `--src-ip-range=0.0.0.0/0` and `--enable-logging` flags with this rule. Firewall action logs include the following connection information:

  * `ALLOW` logs are published once, at connection establishment, and provide 2-tuple (source IP address, destination IP address) information.
  * `DENY` logs provide 5-tuple information for the denied packet. These logs are repeated as long as traffic attempts continue, with a maximum rate of once every 5 seconds.



For more information about limits, see [Per firewall rule](https://docs.cloud.google.com/firewall/docs/quotas#per-firewall-rule).

## What's next

  * [Cloud NGFW for the RoCE network profile](https://docs.cloud.google.com/firewall/docs/firewall-for-roce)
  * [Create and manage firewall rules for RoCE](https://docs.cloud.google.com/firewall/docs/create-manage-roce-vpcs)
  * [Network profiles overview](https://docs.cloud.google.com/firewall/docs/network-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
