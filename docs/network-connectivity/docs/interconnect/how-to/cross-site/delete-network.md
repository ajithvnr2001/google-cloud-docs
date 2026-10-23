---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/delete-network/
title: Delete a cross-site network \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:57.816567+00:00
---

# Delete a cross-site network  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/delete-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Delete a cross-site network Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a cross-site network.

To delete a cross-site network, you must first delete all of the wire groups that are associated with the network.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.crossSiteNetworks.delete`
  * `compute.wireGroups.delete`



**Roles**

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Compute Network Admin (`roles/compute.networkAdmin`)



## Delete a wire group

This section describes how to delete a wire group.

###  Console 

To delete a wire group in a cross-site network, do the following:

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Cross-site networks** tab, click the name of the cross-site network that contains the wire group that you want to delete.

  3. In the **Wire groups** section, click the name of the wire group that you want to delete.

  4. On the **Wire group details** page, click **Delete**.

  5. If you want to delete a cross-site network, repeat these steps for each wire group that is associated with the network.




###  gcloud 

To delete a wire group, use the [`gcloud compute interconnects wire-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/delete).
    
    
      gcloud compute interconnects wire-groups delete WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network that contains the wire group



If you want to delete a cross-site network, repeat this command for each wire group that is associated with the network.

## Delete a cross-site network

This section describes how to delete a cross-site network that doesn't contain any wire groups.

###  Console 

To delete a cross-site network, do the following:

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Cross-site networks** tab, click the name of the cross-site network that you want to delete.

  3. On the **Cross-site network details** page, click **Delete**.




###  gcloud 

To delete a cross-site network, use the [`gcloud compute interconnects cross-site-networks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/cross-site-networks/delete).
    
    
      gcloud compute interconnects cross-site-networks delete CROSS_SITE_NETWORK_NAME
    

Replace the following:

  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network



## What's next

  * To learn more about Cross-Site Interconnect, see the [Cross-Site Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
