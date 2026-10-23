---
url: https://docs.cloud.google.com/intrusion-detection-system/docs/best-practice/
title: Best practices for Cloud IDS \u00a0|\u00a0 Cloud Intrusion Detection System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:21.673919+00:00
---

# Best practices for Cloud IDS  |  Cloud Intrusion Detection System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/intrusion-detection-system/docs/best-practice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud IDS ](https://docs.cloud.google.com/intrusion-detection-system/docs)
  * [ Guides ](https://docs.cloud.google.com/intrusion-detection-system/docs/overview)



Send feedback 

#  Best practices for Cloud IDS Stay organized with collections  Save and categorize content based on your preferences. 

This page provides best practices for configuring Cloud Intrusion Detection System (Cloud IDS).

Cloud IDS is an intrusion detection service that provides threat detection for intrusions, malware, spyware, and command-and-control attacks on your network. Cloud IDS uses a resource known as an _IDS endpoint_ , a zonal resource that can inspect traffic from any zone in its region. Each IDS endpoint receives mirrored traffic and performs threat detection analysis.

## Deploy IDS endpoints

  * Create an IDS endpoint in each region that you want to monitor by using Cloud IDS. You can create multiple IDS endpoints for each region.
  * Allow up to 20 minutes for Cloud IDS to create and configure firewalls.
  * During IDS endpoint creation, you must choose an alert severity level. For maximum visibility, we recommend the `informational` level.
  * If you use the **Packet mirroring** page in the Google Cloud console to create a packet mirroring policy, ensure that you enable **Allow both ingress and egress traffic**. 

[Go to Packet mirroring](https://console.cloud.google.com/networking/packetmirroring)

  * If you use the **Cloud IDS** page to configure an IDS endpoint, you do not need to enable **Allow both ingress and egress traffic** because it is automatically enabled. 

[Go to the Cloud IDS dashboard](https://console.cloud.google.com/net-security/ids/dashboard)




You can use Cloud IDS to create an IDS endpoint in each region that you want to monitor. You can create multiple IDS endpoints for each region. Each IDS endpoint has a maximum inspection capacity of 5 Gbps. While each IDS endpoint can handle anomalous traffic spikes of up to 17 Gbps, we recommend that you configure one IDS endpoint for every 5 Gbps of throughput that your network experiences.

## Attach packet mirroring policies

  * We recommend that you attach more than one packet mirroring policy to an IDS endpoint when you want to mirror traffic from multiple types of sources, including subnets, instances, or network tags. You can only mirror traffic from subnets that exist in the same region as the IDS endpoint.
  * Choose only the subnets whose traffic you want to mirror to Cloud IDS.



## Cost optimization

Cloud IDS employs a fixed cost for each IDS endpoint and a variable cost based on the volume of inspected traffic. Without careful planning, all network traffic within a Virtual Private Cloud (VPC) can be mirrored and inspected, leading to unexpectedly high bills. To control expenses, we recommend that you do the following:

  * Understand the specific security and compliance requirements to judiciously select which VPCs, regions, subnets, and most critically, which traffic flows truly need inspection.
  * Start with minimal inspection of critical assets and gradually expand.
  * Use packet mirroring filters to precisely control the amount of traffic processed, thereby significantly reducing the variable cost.



The following example tunes Cloud IDS packet mirroring policy for cost optimization:

Suppose you need to inspect traffic in VPC-_x_ , subnet-_x_ , and only traffic to or from the internet needs to be inspected. You make this decision based on your security and compliance requirements. Also, suppose that only the internet-facing virtual machine (VM) instances in subnet-_x_ need to be inspected.

  1. Tag the internet-facing VMs with `tag-_x_`.
  2. Use the [Classless Inter-Domain Routing (CIDR)](https://docs.cloud.google.com/firewall/docs/key-terms#cidr-format) IP address ranges in the packet mirroring policy to inspect all traffic between VMs tagged with `tag-_x_` and the internet. Because negation isn't supported with packet mirroring, you need to construct it in a different way. Suppose this VPC uses the `10.0.0.0/8` CIDR; if so, then you need to construct a CIDR for everything except `10.0.0.0/8`, which is the following: 
     * `128.0.0.0/1`
     * `64.0.0.0/2`
     * `32.0.0.0/3`
     * `16.0.0.0/4`
     * `0.0.0.0/5`
     * `12.0.0.0/6`
     * `8.0.0.0/7`
     * `11.0.0.0/8`



To create the packet mirroring policy, run the following command: 
    
    
      gcloud compute packet-mirrorings create NAME
          --network=vpc-_x_
          --filter-cidr-ranges=[128.0.0.0/1, 64.0.0.0/2, 32.0.0.0/3, 16.0.0.0/4, 0.0.0.0/5, 12.0.0.0/6, 8.0.0.0/7, 11.0.0.0/8]
          --mirrored-subnets=[subnet-_x_]
          --mirrored-tags=[tag-_x_]
          --region=REGION
      

Replace the following:

  * `NAME`: the name of the packet mirroring to create
  * `REGION`: the region of the packet mirroring



## What's next

  * To review conceptual information, see the [Cloud IDS overview](https://docs.cloud.google.com/intrusion-detection-system/docs/overview).
  * To set up Cloud IDS, see [Configure Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
