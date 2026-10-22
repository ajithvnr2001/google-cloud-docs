---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota/
title: Check bandwidth quotas and limits \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:43.474489+00:00
---

# Check bandwidth quotas and limits  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Check bandwidth quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to check and request increases for the following before provisioning Cross-Site Interconnect:

  * Your quota for _Wire groups unmetered bandwidth per Cloud Interconnect metro pair_
  * The limit for _Maximum bandwidth per wire_

**Note:** The 10 Gbps limit for _Maximum bandwidth per traffic flow on a wire_ can't be increased.

For more information, see the [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas) page for Cloud Interconnect.

## Before you begin

Before completing the procedures on this page, review [Colocation facilities for Cross-Site Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-locations) and determine the metros where you want to create your Cross-Site Interconnect connections.

## Determine your required bandwidth

You need quota that is equal to the bandwidth setting for the wire group. For example, if you want both wires in a group to have 1 Gbps bandwidth each, you need a quota of 1 Gbps.

If the wire group is in port mode you can only use one wire group with each set of ports. If the wire group is in VLAN mode, you can optionally create a second wire group on some or all of the same ports if you have remaining connection capacity and quota. Keep in mind that creating a second wire group increases the quota required between metros.

## Check your quota for bandwidth per Cloud Interconnect metro pair

To check your quota, follow these steps:

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. View the quota for [**Wire groups unmetered bandwidth per Interconnect metro pair**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/wire_groups_gold_unmetered_bandwidth_gbps). There is a separate quota for each pair of metros.

  3. In the **Dimensions** column, identify the pair of metros that you want to connect, for example `Ashburn|Chicago`, and check the **Value** column.

  4. If the bandwidth between metros in your planned configuration exceeds your current quota, follow the instructions to [Request additional quota](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#requesting-additional-quota).




## Review the limit for bandwidth per wire

You can view the _Maximum bandwidth per wire_ limit on the [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#limits) page.

If your bandwidth per wire in your planned configuration exceeds the limit, [file a support case](https://cloud.google.com/support-hub) to request an increase.

[ Previous arrow_back  Provisioning overview  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/provisioning-overview)

[ Next Order connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/order-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
