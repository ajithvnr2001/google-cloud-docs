---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/view-connections/
title: View connection details \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:28.242585+00:00
---

# View connection details  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/view-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  View connection details Stay organized with collections  Save and categorize content based on your preferences. 

You can view a list of all the Cross-Site Interconnect connections in your project and details about each one. For example, you can view the name of each Cross-Site Interconnect connection, the colocation facility in which it's located, and the capacity of the connection.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.list`
  * `compute.interconnects.get`



**Roles**

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Physical connections** tab, select the Cross-Site Interconnect connection to view its details.




###  gcloud 

  1. List all Cross-Site Interconnect connections that are in your project:
         
         gcloud compute interconnects list \
             --filter "requestedFeatures: (IF_CROSS_SITE_NETWORK) OR availableFeatures: (IF_CROSS_SITE_NETWORK)"
         

  2. Describe a connection to view more information about it:
         
         gcloud compute interconnects describe CONNECTION_NAME
         

Replace `CONNECTION_NAME` with the name of the Cross-Site Interconnect connection that you want to view.




## What's next

  * To create a Cross-Site Interconnect connection, see the [Cross-Site Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/provisioning-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
