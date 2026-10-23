---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-interconnects/
title: View connection details \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:03.477402+00:00
---

# View connection details  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-interconnects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  View connection details Stay organized with collections  Save and categorize content based on your preferences. 

You can view a list of all the Dedicated Interconnect connections in your project and details about each one. For example, you can view the name of each Dedicated Interconnect connection, the colocation facility in which it's located, and the capacity of the connection.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.list`
  * `compute.interconnects.get`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the Dedicated Interconnect connection to view its details.




###  gcloud 

  1. List all Dedicated Interconnect connections that are in your project:
         
         gcloud compute interconnects list
         

Output: 
         
         NAME             LOCATION       OPERATIONAL_STATUS  ADMIN_ENABLED
         my-interconnect  sin-zone1-388  ACTIVE              True
         ...
         

  2. Describe a connection to view more information about it by passing the name of the connection:
         
         gcloud compute interconnects describe my-interconnect
         

Output:
         
         adminEnabled: true
         availableFeatures:
         ‐ IF_MACSEC
         creationTimestamp: '2017-08-13T20:26:05.783-07:00'
         description: test interconnect
         googleIpAddress: 169.254.123.122/29
         googleReferenceId: '12345678'
         id: '1234567890123456789'
         interconnectType: DEDICATED
         kind: compute#interconnect
         linkType: ETHERNET_10G_LR
         location:
         https://www.googleapis.com/compute/....../sin-zone1-388
         name: my-interconnect
         operationalStatus: ACTIVE
         peerIpAddress: 169.254.123.123/29
         provisionedLinkCount: 1
         requestedLinkCount: 1
         requestedFeatures:
         ‐ IF_MACSEC
         selfLink:
         https://www.googleapis.com/compute/....../my-interconnect
         




## What's next

  * To create a Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
