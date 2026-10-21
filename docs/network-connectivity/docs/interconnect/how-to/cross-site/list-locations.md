---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/list-locations/
title: List locations for Cross-Site Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:14.090070+00:00
---

# List locations for Cross-Site Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/list-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  List locations for Cross-Site Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

When you order a Cross-Site Interconnect connection, you must specify a colocation facility where your network meets Google's network. In most cases, select a facility that's geographically close to your on-premises network.

To view a list of these facilities in the documentation, see [Colocation facilities for Cross-Site Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-locations).

To use the Google Cloud console or Google Cloud CLI to view a list of facilities, see the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectLocations.list`
  * `compute.interconnectLocations.get`



**Roles**

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

You can view a list of the colocation facilities when you order a Cross-Site Interconnect connection. You can filter the locations by city or facility name.

For more information, see [Order Cross-Site Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/order-connections).

###  gcloud 

To list all colocation facilities that support Cross-Site Interconnect, run the following command:
    
    
    gcloud compute interconnects locations list \
        --filter "availableFeatures: (IF_CROSS_SITE_NETWORK)"
    

To view the details of a facility, such as its physical address, run the following command.

The command output includes a `CrossSiteInterconnectInfos` field, which lists the metros that the location can connect to through a cross-site network.
    
    
     gcloud compute interconnects locations describe LOCATION
     

Replace `LOCATION` with the name of the Cross-Site Interconnect location.

## What's next

  * To create a Cross-Site Interconnect connection, see the [Cross-Site Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/provisioning-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
