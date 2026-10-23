---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/disabling-vlans/
title: Disable VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:16.996787+00:00
---

# Disable VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/disabling-vlans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Disable VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

You can temporarily disable a VLAN attachment so that it stops forwarding packets. Disabling an attachment can be useful if you want to test failover. To test that a redundant connection can successfully serve traffic, disable the primary Cross-Cloud Interconnect connection.

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select a VLAN attachment to disable.

  3. On the **VLAN attachment details** page, click **Disable**. The attachment stops forwarding packets within a minute or two. To re-enable the attachment, click **Enable**.




###  gcloud 

Use the [`gcloud compute interconnects attachments dedicated update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update) with the `--no-admin-enabled` flag:
    
    
    gcloud compute interconnects attachments dedicated update ATTACHMENT_NAME \
        --region REGION \
        --no-admin-enabled
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of your VLAN attachment
  * `REGION`: the region where the attachment is located



The attachment stops forwarding packets within a minute or two.

To enable the attachment, use the `--admin-enabled` flag.

## What's next

  * To learn more about Cross-Cloud Interconnect, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

  * To learn about common issues that you might encounter when using Cross-Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cci).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
