---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises/
title: Connecting from an on-premises network to VMware Engine standard or stretched private cloud \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:48.037746+00:00
---

# Connecting from an on-premises network to VMware Engine standard or stretched private cloud  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connecting from an on-premises network to VMware Engine standard or stretched private cloud

Google Cloud VMware Engine enables key use cases such as data center lift and shift, data center extension, and disaster recovery. These use cases require that you establish connectivity from your on-premises network to Google Cloud and your VMware Engine network.

## Connecting from your on-premises network to VPC network

Google Cloud offers multiple hybrid connectivity options such as [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) and [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect). Follow the links to learn how to set up Cloud VPN or Cloud Interconnect (Dedicated and Partner Interconnect) connections with your Virtual Private Cloud (VPC) network. If you have already connected your on-premises network to a VPC network, you can use this connection for this step.

**Warning:** Use of HCX requires either Cloud VPN or Cloud Interconnect-based connectivity between your on-premises network and your VMware Engine network.

## Connect from your VPC network to VMware Engine

The connection from your VPC network to a VMware Engine differs based on whether you use standard or legacy networks.

### Standard VMware Engine networks

The connection from your VPC network to a Standard VMware Engine network uses [VPC Network Peering](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network).

### Legacy VMware Engine networks

The connection from your VPC network to a Legacy VMware Engine network uses [private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). To access your workload virtual machines (VMs) from an on-premises network or from your VPC network, [set up private services access from your VPC network to your VMware Engine network](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access).

## End-to-end connectivity and routing considerations

To allow a VMware Engine regional network to reach on-premises networks, you must enable **Import/export custom routes** on the VPC network peering connection associated with the private services access. This enables routes that are advertised from on-premises to the VPC network to be propagated to the VMware Engine region.

When you use Cloud VPN for on-premises connection to the VPC network, you must add VMware Engine networks to the [Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing).

When you use Cloud Interconnect for on-premises connection to the VPC network, you can [add custom routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) to the Cloud Router that terminates the Cloud Interconnect attachment.

## Migrating VMs from on-premises to stretched private clouds

You can continue to use the same migration tools for on-premises to Google Cloud VMware Engine VM migrations for both standard private clouds and stretched private cloud destinations. VMware HCX is the default tool for VM migrations and comes bundled with the service.

HCX Cloud Manager is deployed automatically to the primary zone when a stretched private cloud is created. When an HCX service mesh is created, you can use affinity rules to ensure that the HCX service appliances are created in the primary zone.

After a site-level failover (in the case of a complete zone failure), the HCX Manager and service appliances are started on the surviving zone.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
