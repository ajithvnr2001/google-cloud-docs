---
url: https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-accounting-faq/
title: Sole-tenancy accounting FAQ \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:39.624633+00:00
---

# Sole-tenancy accounting FAQ  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-accounting-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Sole-tenancy accounting FAQ Stay organized with collections  Save and categorize content based on your preferences. 

This FAQ can help you evaluate whether you can classify your [sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) payments as capital expenditures (CAPEX) or operational expenditures (OPEX). Although Google provides this FAQ, Google recommends that you consult with your accountants about how to classify your payments for sole-tenant nodes.

## What are sole-tenant nodes?

Normally, VMs run on physical hosts that might be shared by many customers. With sole-tenant nodes, you have exclusive access to the VMs on the physical host. Each sole-tenant node is associated with one physical server. Within each node, a single customer can fully control which VMs are running on that node, without sharing the host hardware with other customers.

## Should I consider the purchase of a sole-tenant node as CAPEX or OPEX?

Google does not provide guidance about accounting. Please review the details about the sole-tenant node product before you make any accounting decisions regarding CAPEX or OPEX.

## Can I uniquely identify a sole-tenant node?

Yes, each sole-tenant node has a unique identifier: the `server_id`. The `server_id` is unique across all of Google Cloud hardware, and is available as soon as you create a sole-tenant node. Retrieve the `server_id` with the [`nodeGroups.listNodes`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/listNodes) REST request.

## What is the server_id?

The `server_id` is a unique identifier that is used to mark each physical server. When a sole-tenant node is allocated to your account, there is a one-to-one relationship between the `server_id` and the physical server.

## Will Google Cloud reuse the same server_id for different physical servers?

No, Google Cloud does not reuse the same `server_id` for different physical servers. If the physical host is retired due to maintenance-related events, you receive a replacement server along with its `server_id`, and your VMs are moved to the replacement server. Maintenance-related events are logged in the Cloud Audit Logs, and you can use these logs to help you trace the lineage of your physical server.

## In the event that my physical host is retired, can I trace the server_id lineage?

Yes, each time a host is retired and you are provided a replacement host, the new `server_id` is available in Cloud Audit Logs. Use these logs to trace the `server_id` history of your VM's hosts.

## How am I billed for a sole-tenant node?

You pay for the entire sole-tenant node on a per-second basis, regardless of how many VMs are running on the node. When you provision a sole-tenant node, you control the VMs on that host.

## Can I pay for a commitment of longer than one year?

You can purchase sole-tenant nodes with a 1- or 3-year [committed use discount](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts), or you can pay for them as you use them. For more information about pricing, see [sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing).

## What's next

  * Learn about [bringing images with existing licenses to Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license).
  * Learn more about [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
