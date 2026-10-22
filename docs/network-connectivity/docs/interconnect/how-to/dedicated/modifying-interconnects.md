---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-interconnects/
title: Modify connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:42.788275+00:00
---

# Modify connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-interconnects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Modify connections Stay organized with collections  Save and categorize content based on your preferences. 

For an existing Dedicated Interconnect connection, you can modify its description, technical contact email address, and the number of circuits (the capacity).

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

If you modify the description or email address, these changes are immediate. If you change the number of circuits, the existing Dedicated Interconnect connection and its VLAN attachments continue to operate as normal because the circuit bundle uses Link Aggregation Control Protocol (LACP). Traffic isn't disrupted.

  * If you increase the number of circuits, you follow a process similar to [creating a connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview). Google sends you an LOA-CFA with your requested changes. You send this document to your vendor to grant them authorization to complete the work. New circuits aren't usable until they are provisioned and [tested](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections).

  * If you decrease the number of circuits, Google removes the requested number of ports from the bundle and notifies you which circuits to remove. You then need to contact your vendor to remove those Dedicated Interconnect connections.




The following items can't be modified for existing Dedicated Interconnect connections:

  * The link type on a Dedicated Interconnect connection. For example, changing the circuit from 10 Gpbs to 100 Gbps. If you want to migrate to 100 Gbps, you must first provision a new 100‑Gbps Dedicated Interconnect connection alongside your existing 10‑Gbps connection, and then migrate the traffic onto the 100‑Gbps connection.

  * Requested features, such as MACsec. For more information, see [MACsec support on existing Cloud Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview#macsec-support-existing-connections).




#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.get`
  * `compute.interconnects.update`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. For the Dedicated Interconnect connection that you want to modify, select it.

  3. On the connection's detail page, click **Edit**.

  4. Modify your Dedicated Interconnect connection:

     * **Description** : Information about the connection.
     * **Capacity** : The total capacity of your connection, which is determined by the number and size of the circuits that you order.

**Note:** You can view the estimated cost of your choice in the upper-right corner of the Google Cloud console page.

Select _one_ of the following options:

       * 1 x 10‑Gbps circuit in 10‑Gbps increments up to 8 x 10‑Gbps (80 Gbps) circuits
       * 1 x 100‑Gbps (100 Gbps) circuit
       * 2 x 100‑Gbps (200 Gbps) circuits
     * **Technical contact** : An email address where notifications about this connection are sent. You don't need to enter your own address; you are included in all notifications. You can specify only one address.

  5. Click **Save**.

  6. To confirm your changes, click **Done**.




###  gcloud 

Modify an existing Dedicated Interconnect connection by running the following command:
    
    
    gcloud compute interconnects update INTERCONNECT_NAME \
        --description=UPDATED_DESCRIPTION \
        --noc-contact-email=UPDATED_EMAIL_CONTACT \
        --requested-link-count=UPDATED_COUNT
    

Replace `UPDATED_COUNT` with the total number of circuits of type `link-type`.

For example, if you have a 20‑Gbps Dedicated Interconnect connection and want to make it 40 Gbps, use `--requested-link-count=4`.

Billing for new circuits starts after they're ready to use (all [tests](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections) have passed) or 30 days after your order is received. You aren't charged before then. You can cancel your order by reverting to the original number of circuits. Billing for removed circuits stops when the LACP bundle is resized.

## What's next

  * To create a Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
