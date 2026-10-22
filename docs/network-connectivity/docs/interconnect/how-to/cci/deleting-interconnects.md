---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/deleting-interconnects/
title: Delete connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:57.829366+00:00
---

# Delete connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/deleting-interconnects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Delete connections Stay organized with collections  Save and categorize content based on your preferences. 

When you delete a Cross-Cloud Interconnect connection, Google shuts down your ports, and billing stops immediately.

You must also notify your remote cloud service provider to discontinue your port in their network and avoid further billing.

Before you can delete a connection, you must delete all of its attachments.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.delete`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the connection that you want to delete.

  3. On the **Interconnect details** page, click delete**Delete**.

  4. In the confirmation box, type the name of the connection that you want to delete.

  5. Click **Delete this Interconnect**.




###  gcloud 

Use the [`gcloud compute interconnects delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/delete):
    
    
    gcloud compute interconnects delete NAME
    

Replace `NAME` with the name of your Cross-Cloud Interconnect connection.

## What's next

  * To learn more about Cross-Cloud Interconnect, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

  * To learn about common issues that you might encounter when using Cross-Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cci).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
