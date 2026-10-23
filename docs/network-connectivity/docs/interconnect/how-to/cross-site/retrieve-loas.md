---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/retrieve-loas/
title: Retrieve LOA-CFAs \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:19.285641+00:00
---

# Retrieve LOA-CFAs  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/retrieve-loas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Retrieve LOA-CFAs Stay organized with collections  Save and categorize content based on your preferences. 

After you order a Cross-Site Interconnect connection, Google sends you and the NOC (technical contact) an email with your [Letter of Authorization and Connecting Facility Assignment (LOA-CFA)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#loa) (one PDF file per connection). You must send these LOA-CFAs to your vendor so that they can install your connections. If you don't, your connections won't get connected.

If you can't find the LOA-CFAs in your email, retrieve them from the Google Cloud console. You can also respond to your order confirmation email for additional assistance.

After the status of a Cross-Site Interconnect connection changes to `PROVISIONED`, the LOA-CFA is no longer valid, necessary, or available in the Google Cloud console.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.create`



**Roles**

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Physical connections** tab, for the Cross-Site Interconnect connection that contains the LOA-CFAs that you need, select the options button, and then select **Download LOA-CFA**.

  3. Submit your LOA-CFAs to your vendor so that they can provision your connections. For more information, contact the colocation facility that you're working with.




To help you solve common issues that you might encounter when using Cross-Site Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).

[ Previous arrow_back  Order connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/order-connections)

[ Next Test connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/test-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
