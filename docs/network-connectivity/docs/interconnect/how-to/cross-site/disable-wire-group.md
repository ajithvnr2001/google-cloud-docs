---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/disable-wire-group/
title: Disable a wire group \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:13.974520+00:00
---

# Disable a wire group  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/disable-wire-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Disable a wire group Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to disable a wire group in a cross-site network.

Disabling a wire group stops all traffic through the wire group. You can re-enable the wire group at any time.

###  Console 

To disable a wire group in a cross-site network, do the following:

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Cross-site networks** tab, click the name of the wire group that you want to disable.

  3. On the **Wire group details** page, click **Edit**.

  4. In the **Admin enabled state** field, deselect the **Active** checkbox.

  5. Click **Save**.




You can re-enable the wire group by updating the wire group with the **Active** checkbox selected.

###  gcloud 

To disable a wire group in a cross-site network, update the wire group and set the `--no-admin-enabled` flag.

Use the [`gcloud compute interconnects wire-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/update).
    
    
    gcloud compute interconnects wire-groups update WIRE_GROUP_NAME \
        --cross-site-network=NETWORK_NAME \
        --no-admin-enabled
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group
  * `NETWORK_NAME`: the name of the cross-site network that contains the wire group



You can re-enable the wire group by updating the wire group with the `--admin-enabled` flag.

## What's next

  * To learn more about Cross-Site Interconnect, see the [Cross-Site Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
