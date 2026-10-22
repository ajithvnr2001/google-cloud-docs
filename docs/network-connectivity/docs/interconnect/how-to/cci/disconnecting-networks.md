---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/disconnecting-networks/
title: Disconnect networks \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:53.278017+00:00
---

# Disconnect networks  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/disconnecting-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Disconnect networks Stay organized with collections  Save and categorize content based on your preferences. 

To remove a connection between a Virtual Private Cloud (VPC) network and a Cross-Cloud Interconnect connection, delete the related VLAN attachment (also known as an `interconnectAttachment`). After you delete the attachment, no traffic can travel between the VPC network and your remote cloud network. Also, Border Gateway Protocol (BGP) sessions that use the attachment go down.

Billing for the VLAN attachment stops when you delete it. However, you're still billed for the Cross-Cloud Interconnect connection, even if no traffic is passing through it.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectAttachments.delete`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. For the Cloud Interconnect connection that you want to configure, click **Configure**.

  3. In the **Router connections** section, select the VLAN attachment to delete.

  4. Select the options button, and then click **Delete**.

  5. Click **Delete** to confirm that you want to delete the VLAN attachment.




###  gcloud 

Use the [`gcloud compute interconnects attachments delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/delete):
    
    
    gcloud compute interconnects attachments delete ATTACHMENT_NAME
    

Replace `ATTACHMENT_NAME` with the name of your VLAN attachment.

## What's next

  * To learn more about Cross-Cloud Interconnect, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

  * To learn about common issues that you might encounter when using Cross-Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cci).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
