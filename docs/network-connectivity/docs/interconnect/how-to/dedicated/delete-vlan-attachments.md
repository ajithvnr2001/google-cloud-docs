---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/delete-vlan-attachments/
title: Delete VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:08.079189+00:00
---

# Delete VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/delete-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Delete VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

To remove a connection between a Google Virtual Private Cloud (VPC) network and a Dedicated Interconnect connection, you delete the related VLAN attachment (also known as an `interconnectAttachment`). After you delete the attachment, no traffic can travel between the VPC network and your on-premises network through the connection, and BGP sessions that use the attachment go down.

Billing for the VLAN attachment stops when you delete it; however, you're still billed for the Dedicated Interconnect connection, even if no traffic is passing through it.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectAttachments.delete`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment to delete.

  3. On the **VLAN attachment details** page, click **Delete**.

  4. Click **Delete** to confirm.




###  gcloud 

Delete attachments by providing the name of the attachment to delete:
    
    
    gcloud compute interconnects attachments delete NAME
    

## What's next

  * To delete a Dedicated Interconnect connection, see [Delete connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/deleting-interconnects).

  * To create a Dedicated Interconnect, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
