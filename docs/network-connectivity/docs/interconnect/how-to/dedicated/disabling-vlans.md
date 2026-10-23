---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/disabling-vlans/
title: Disable or enable VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:31.920268+00:00
---

# Disable or enable VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/disabling-vlans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Disable or enable VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

You can temporarily disable a VLAN attachment so that it stops forwarding packets. This can be useful, for example, for testing failover. Disable one Dedicated Interconnect connection to test that the redundant connection can successfully serve traffic.

You can enable VLAN attachments, typically after testing for failover.

## Drain traffic from a VLAN attachment

### Shut down BGP

We recommend that you disable a VLAN attachment by disabling its Border Gateway Protocol (BGP) session. Disabling only the BGP session instead of disabling the entire VLAN attachment avoids packet loss. After making this configuration change, it can take a few minutes for traffic to completely move away. For more information, see [Disable a BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#disable_a_bgp_session).

### Disable a VLAN attachment

If you need to disable your VLAN attachment more rapidly, or if you need to ensure that zero packets are sent over your VLAN attachment, you can disable the entire VLAN attachment. This process can incur packet loss. To disable a VLAN attachment, do the following:

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. On the **VLAN attachments** tab, select a VLAN attachment to disable.

  3. On the **VLAN attachment details** page, click **Disable**. The attachment stops forwarding packets within a minute or two. To re-enable the attachment, click **Enable**.




###  gcloud 

To disable an existing active attachment, use the `--no-admin-enabled` flag:
    
    
     gcloud compute interconnects attachments dedicated update my-attachment
         --region us-central1
         --no-admin-enabled
     

The attachment stops forwarding packets within a minute or two.

To enable the attachment, use the `--admin-enabled` flag.

## Restore traffic to a VLAN attachment

To restore traffic to your VLAN attachment, you must either enable its BGP session or enable the VLAN attachment, depending on how you drained traffic from your VLAN attachment.

### Enable BGP

If you disabled your VLAN attachment by disabling its BGP session, then you must re-enable BGP to make your attachment work again.

Enabling BGP takes a few minutes to take effect. For more information, see [Enable a BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#enable_a_bgp_session).

### Enable a VLAN attachment

If you shut down your VLAN attachment by disabling your VLAN attachment, then you must enable your VLAN attachment to restore traffic to your attachment.

Do the following:

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. On the **VLAN attachments** tab, select a VLAN attachment to enable.

  3. On the **VLAN attachment details** page, click **Enable**. The attachment starts forwarding packets within a minute or two.




###  gcloud 

To enable an existing active attachment, use the `--admin-enabled` flag:
    
    
     gcloud compute interconnects attachments dedicated update my-attachment
         --region us-central1
         --admin-enabled
     

The attachment starts forwarding packets within a minute or two.

## What's next

  * To create an Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
