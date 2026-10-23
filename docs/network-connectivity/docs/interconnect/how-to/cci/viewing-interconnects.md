---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/viewing-interconnects/
title: View connection details \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:24.931370+00:00
---

# View connection details  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/viewing-interconnects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  View connection details Stay organized with collections  Save and categorize content based on your preferences. 

You can view a list of all Cross-Cloud Interconnect connections in your project and see details about each one. For example, you can view the name of each connection, its location, and its capacity.

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

  2. Select the appropriate connection.




###  gcloud 

  1. To list all Cloud Interconnect connections that are in your project, use the [`gcloud compute interconnects list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/list):
         
         gcloud compute interconnects list
         

You should see output similar to the following: 
         
         NAME             LOCATION       OPERATIONAL_STATUS  ADMIN_ENABLED
         my-interconnect  sin-zone1-388  ACTIVE              True
         ...
         

  2. To view more information about a connection, use the [`gcloud compute interconnects describe my-interconnect` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/describe):
         
         gcloud compute interconnects describe my-interconnect CONNECTION_NAME
         

Replace `CONNECTION_NAME` with the name of your Cross-Cloud Interconnect connection.

You should see output similar to the following:
         
         adminEnabled: true
         circuitInfos:
         \\- customerDemarcId: 'COLGX: MMRC-COL3-CO17-RU35 Ports 121, 122'
           googleCircuitId: GCP-00067
           googleDemarcId: 'COLGX: MMRC-COL3-CO17-RU35 Ports 121, 122'
         creationTimestamp: '2023-02-08T22:52:54.425-08:00'
         googleReferenceId: '562358802'
         id: '9075210876797658793'
         interconnectType: IT_PRIVATE
         kind: compute#interconnect
         linkType: LINK_TYPE_ETHERNET_10G_LR
         location: https://www.googleapis.com/compute/....../cmh-zone1-2377
         name: my-interconnect
         nocContactEmail: my-name@gmail.com
         operationalStatus: OS_ACTIVE
         provisionedLinkCount: 1
         requestedLinkCount: 1
         selfLink: https://www.googleapis.com/compute/....../my-interconnect
         state: ACTIVE
         




## What's next

  * To learn more about Cross-Cloud Interconnect, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

  * To learn about common issues that you might encounter when using Cross-Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cci).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
