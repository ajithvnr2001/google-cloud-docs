---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/change-reliability-options/
title: Change Dedicated Interconnect reliability options \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:23.250545+00:00
---

# Change Dedicated Interconnect reliability options  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/change-reliability-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Change Dedicated Interconnect reliability options Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to change your connection groups' intended levels of reliability between critical production, non-critical production, and no SLA. For more information about connection groups, see [Cloud Interconnect groups](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#groups).

When you configure a Cloud Interconnect connection, you can do so at a specific level of reliability. You can choose between the following reliability options:

  * **Critical production**. Choose this option for critical production workloads that require maximum resiliency. This option provides a 99.99% uptime SLA.
  * **Non-critical production**. Choose this option for non-critical production and development workloads. This option provides a 99.9% uptime SLA.
  * **No SLA**. You can configure your connection group without specifying an intended level of reliability. We recommend that you avoid using this option for resources in which extended downtime is undesirable. This option doesn't provide an uptime SLA.



For more information about Cloud Interconnect SLAs, see [Dedicated Interconnect and Partner Interconnect SLA](https://cloud.google.com/network-connectivity/docs/interconnect/sla).

## Change reliability options for Cloud Interconnect connection groups

Use the following procedure to change the reliability options for a Cloud Interconnect connection group. When you update your connection group from non-critical production to critical production, you might need to modify your deployment to meet the new SLA requirements. For guidance on SLA blockers, see [Fix SLA eligibility problems](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/fix-sla).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.update`
  * `compute.interconnects.get`
  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`
  * `compute.interconnectGroups.get`
  * `compute.interconnectGroups.update`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

**Note:** You can't set the intended reliability for your Cloud Interconnect connection group to no SLA using the Google Cloud console. If you need to remove your SLA, use the Google Cloud CLI.

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the connection group that you want to edit.

  3. Click **Edit**.

  4. In the **Intended SLA** field, select **Critical production** or **Non-critical production**.

  5. Click **Save**.




###  gcloud 

You can declare a different reliability level for your Cloud Interconnect connection by using the following command.
    
    
    gcloud compute interconnects groups update GROUP_NAME \
        --intended-topology-capability SLA
    

Replace the following:

  * `GROUP_NAME`: the name of your connection group
  * `SLA`: the SLA to use; available values are `PRODUCTION_CRITICAL`, `PRODUCTION_NON_CRITICAL`, or `NO_SLA`



## Change reliability options for VLAN attachment groups

Use the procedures in the following sections to change reliability options for your VLAN attachment groups. When you update your connection group from non-critical production to critical production, your deployment might not meet the new SLA requirements. If so, the group reports SLA blockers to explain the changes you need to make to achieve the critical production SLA. For more information about SLA blockers, see [Fix SLA eligibility problems](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/fix-sla).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.update`
  * `compute.interconnects.get`
  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`
  * `compute.interconnectGroups.get`
  * `compute.interconnectGroups.update`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

**Note:** You can't set the intended reliability for your Cloud Interconnect VLAN attachment group to no SLA using the Google Cloud console. If you need to remove your SLA, use the Google Cloud CLI.

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment group that you want to edit.

  3. Click **Edit**.

  4. In the **Production SLA** field, select **Critical production** or **Non-critical production**.

  5. Click **Save**.




###  gcloud 

You can declare a different reliability level for your VLAN attachment group by using the following command. Replace `GROUP_NAME` with the name of your connection group, and replace `SLA` with either `PRODUCTION_CRITICAL`, `PRODUCTION_NON_CRITICAL`, or `NO_SLA`.
    
    
    gcloud compute interconnects attachments groups update GROUP_NAME \
        --intended-availability-sla SLA
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
