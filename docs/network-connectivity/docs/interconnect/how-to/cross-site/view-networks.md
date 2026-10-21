---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/view-networks/
title: View cross-site networks \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:13.737690+00:00
---

# View cross-site networks  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/view-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  View cross-site networks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to list cross-site networks and view the details of a cross-site network, including its wire groups.

For information about monitoring Cross-Site Interconnect, including cross-site networks and wire groups, see [Monitor connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/monitoring).

###  Console 

To list and view cross-site networks and wire groups, do the following:

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Cross-site networks** tab, click the name of the network.

The **Wire groups** section lists the wire groups in the network.

  3. To view the details of a wire group, click the name of the wire group.




###  gcloud 

See the following commands for listing and viewing cross-site networks and wire groups:

  * To list all cross-site networks in a project, use the [`gcloud compute interconnects cross-site-networks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/cross-site-networks/list).
        
        gcloud compute interconnects cross-site-networks list \
            --project PROJECT_ID
        

Replace `PROJECT_ID` with the ID of the project that contains the cross-site networks.

  * To view the details of a cross-site network, use the [`gcloud compute interconnects cross-site-networks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/cross-site-networks/describe).
        
        gcloud compute interconnects cross-site-networks describe NETWORK_NAME
        

Replace the following:

    * `NETWORK_NAME`: the name of the cross-site network.
  * To list all wire groups in a cross-site network, use the [`gcloud compute interconnects wire-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/list).
        
        gcloud compute interconnects wire-groups list \
            --cross-site-network=NETWORK_NAME
        

Replace `NETWORK_NAME` with the name of the cross-site network.

  * To view the details of a wire group, use the [`gcloud compute interconnects wire-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/describe).
        
        gcloud compute interconnects wire-groups describe WIRE_GROUP_NAME \
            --cross-site-network=NETWORK_NAME
        

Replace the following:

    * `WIRE_GROUP_NAME`: the name of the wire group
    * `NETWORK_NAME`: the name of the cross-site network



## What's next

  * To learn more about Cross-Site Interconnect, see the [Cross-Site Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
