---
url: https://docs.cloud.google.com/architecture/configure-networks-fedramp-dod-google-cloud/
title: Configure networks for FedRAMP and DoD in Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:01.466674+00:00
---

# Configure networks for FedRAMP and DoD in Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/configure-networks-fedramp-dod-google-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Configure networks for FedRAMP and DoD in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-20 UTC

This document provides configuration guidance to help you to securely deploy Google Cloud networking policies in the United States (US) that comply with the design requirements for FedRAMP High and Department of Defense (DoD) [Impact Level 2 (IL2), Impact Level 4 (IL4), and Impact Level 5 (IL5)](https://media.defense.gov/2020/May/18/2002302035/-1/-1/1/NAVY_TELEWORK_CAPABILITIES_V14.PDF). This document is intended for solution architects, network engineers, and security engineers who design and deploy networking solutions on Google Cloud. The following diagram shows a landing zone network design for highly regulated workloads.

![Landing zone network design for highly regulated workloads.](https://docs.cloud.google.com/static/architecture/images/compliance-architecture.svg)

## Architecture

The network design shown in the preceding diagram is aligned with the US compliance framework requirements for FedRAMP High, and DoD IL2, IL4, and IL5. This architecture includes the following components, which are described in greater detail later in this document:

  * **Virtual Private Cloud (VPC)** : These VPCs are global, however, you must only create [subnets](https://docs.cloud.google.com/vpc/docs/subnets) in US [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
  * **Regional load balancers** : These load balancers are regional, not global. They only support US deployments. Note that the use of external load balancers than can be directly accessed by the internet might need extra validation with DISA to assure DoD authorization for IL4 and IL5.
  * [**Google Cloud Armor**](https://docs.cloud.google.com/armor/docs/security-policy-overview) security policies: These policies can be used with supported [regional](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-2) load balancer security policies.
  * [**Private Service Connect**](https://docs.cloud.google.com/vpc/docs/private-service-connect), [**Private Google Access (PGA)**](https://docs.cloud.google.com/vpc/docs/private-google-access), and [**Private service access (PSA)**](https://docs.cloud.google.com/vpc/docs/private-services-access): These options enable private connectivity to Google managed services within the region. You must enable private access to Google managed services and APIs within the region through the relevant option for your use case.
  * **Third-party services** : For third-party producer-consumer services, you must ensure that both the producer service and the data that is in transit meet your compliance requirements.
  * **Non-prod** : Provision other environments such as non-prod, testing, and quality assurance (QA) in accordance with your organization's VPC strategy.



## Use case

[Assured Workloads](https://cloud.google.com/security/products/assured-workloads) is a compliance framework that can help to provide the security controls that you need to support regulatory requirements for FedRAMP High, and DoD IL2, IL4, and IL5. After you deploy with Assured Workloads, you are responsible for setting up compliant and secure networking policies. For other compliance use cases, see [Hosting FedRAMP Moderate and High Workloads on Google Cloud](https://cloud.google.com/security/compliance/fedramp#section-4) in the FedRAMP documentation.

The scope of this guidance is limited to networking components. You must configure workloads in accordance with the shared responsibility model, [FedRAMP Customer Responsibility Matrix](https://www.fedramp.gov/resources/templates/SSP-Appendix-J-CSO-CIS-and-CRM-Workbook.xlsx), [in-scope Google Cloud services](https://docs.cloud.google.com/assured-workloads/docs/supported-products), [FedRAMP](https://cloud.google.com/security/compliance/fedramp), and Assured Workloads guidelines. For more information about how to meet compliance requirements for other Google Cloud services, see the [Compliance resource center](https://cloud.google.com/security/compliance).

The services referenced in this document are for example purposes only. You must review the [services that are in scope for compliance programs](https://cloud.google.com/security/compliance/fedramp#section-6) to assure the correct compliance level requirements for your workload.

### Out of scope products

The following services don't meet FedRAMP High, or DoD IL2, IL4, and IL5 jurisdictional boundary compliance requirements:

  * Global External Application Load Balancer
  * Global Google Cloud Armor
  * Global External Proxy Load Balancer



We recommend that you discuss the risk of using these services in your network with your Google support team before you begin to make your network design.

## Design Considerations

This section describes design considerations for which the configurations that are described in this document are an appropriate choice.

### Use Assured Workloads

You must use Assured Workloads to meet compliance-based requirements on Google Cloud for regulations that have data sovereignty and residency requirements, such as FedRAMP High, and DoD IL4 and IL5. To understand if these principles apply to your compliance program on Google Cloud, we recommend that you review [Overview of Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview#when_to_use) in the early stages of your design phase. You are responsible for configuring your own network and IAM policies.

You must configure an Assured Workloads [folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder) and set the appropriate compliance program. In this case, either set the appropriate compliance program to `FedRAMP High` or `IL2, IL4, IL5`. This folder provides a regulatory boundary within an organization to identify regulated data types. By default, any project under this folder will inherit the security and compliance guardrails set at the Assured Workloads folder level. Assured Workloads restricts the regions that you can select for those resources based on the compliance program that you chose using the [resource restriction](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) Organization Policy Service.

### Regional alignment

You must use one or more of the US Google regions to support the compliance programs in scope for this guidance. Note that FedRAMP High and DoD IL4 and IL5 have a general requirement that data be kept within a US geographical boundary. To learn which regions you can add, see [Assured Workloads locations](https://docs.cloud.google.com/assured-workloads/docs/locations#us_regions).

### Product-level compliance

It's your responsibility to confirm that a product or service supports the appropriate data sovereignty and residency requirements for your use case. When you purchase or use your target [compliance](https://docs.cloud.google.com/assured-workloads/docs/supported-products) program, you must also follow these guidelines for each product that you use to meet applicable compliance requirements. Assured Workloads sets up a modifiable Organization Policy with a point in time [resource usage restriction policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) that reflects the services that are in compliance with the chosen compliance framework.

## Deployment

To help you to meet your compliance requirements, we recommend that you follow the guidelines in this section for individual networking services.

### Virtual Private Cloud network configurations

You must make the following Virtual Private Cloud configurations:

  * **Subnets** : Create subnets in the US regions referenced in Regional alignment. Assured Workloads applies policies to restrict the creation of subnets in other locations.
  * **Firewall rules** : You must configure [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) to allow or deny connections only to or from [virtual machine (VM) instances](https://docs.cloud.google.com/vpc/docs/vpc#vm-instances) in your VPC network.



### Private Service Connect configurations

[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) is a capability of Google Cloud networking that lets consumers access managed services privately from inside their VPC network.

Both [Private Service Connect types](https://docs.cloud.google.com/vpc/docs/private-service-connect#types) (Private Service Connect endpoints and Private Service Connect backends) support the controls that are described in this document when configured with regional load balancers. We recommend that you apply the configuration details described in the following table:

Private Service Connect Type | Supported load balancers | Compliance status  
---|---|---  
Private Service Connect endpoints for Google APIs | Not applicable | Not supported   
Private Service Connect backends for Google APIs | 

  * Global External Application Load Balancer


  * Regional External proxy Network Load Balancer or Internal Application Load Balancer


  * Regional External proxy Network Load Balancer

| Compliant when used with either of the following regional load balancers:  


  * Regional external or Internal Application Load Balancer


  * Regional External proxy Network Load Balancer

  
Private Service Connect endpoints for published services | 

  * Regional Internal Application Load Balancer


  * Regional Internal passthrough Network Load Balancer


  * Regional External proxy Network Load Balancer

| Compliant  
Private Service Connect backends for published services | 

  * Global External Application Load Balancer


  * Regional external or Internal Application Load Balancer


  * Regional External proxy Network Load Balancer


  * Regional Internal passthrough Network Load Balancer

| Compliant when used with the following regional load balancer:  


  * Regional external or Internal Application Load Balancer


  * Regional External proxy Network Load Balancer


  * Regional Internal passthrough Network Load Balancer

  
  
### Packet Mirroring

[Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) is a VPC feature that you can use to help you to maintain compliance. Packet Mirroring captures all your traffic and packet data, including payloads and headers, and forwards it to target collectors for analysis. Packet Mirroring inherits VPC compliance status.

### Cloud Load Balancing

Google Cloud offers different types of load balancers, as described in [Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer). For this architecture, you must use regional load balancers.

### Cloud DNS

You can use Cloud DNS to help you to meet your compliance requirements. Cloud DNS is a managed DNS service in Google Cloud which supports private [forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#fz-using), [peering zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones), [reverse lookup zones](https://docs.cloud.google.com/dns/docs/zones/managed-reverse-lookup-zones), and [DNS server policies](https://docs.cloud.google.com/dns/docs/policies-overview). Cloud DNS public zones don't comply with FedRAMP High, and DoD IL2, IL4, or IL5 controls.

### Cloud Router

[Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) is a regional product that you can configure for Cloud VPN, Cloud Interconnect, and Cloud NAT. You must only configure Cloud Router in US regions. When you create or edit a VPC network, you can set the [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes#change-network-modes) to be regional or global. If you enable global routing mode, you must configure custom advertised mode to only include US networks.

### Cloud NAT

[Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) is a regional managed NAT product that you can use to enable outbound access to the internet for private resources with no external IP addresses. You must only configure Cloud NAT gateway in US regions that have the associated Cloud Router component.

### Cloud VPN

You must use Cloud VPN endpoints located within the US. Ensure that your VPN gateway is configured only for use in the correct US region, as described in Regional alignment. We recommend that you use [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn) type for Cloud VPN. For encryption, you must only use FIPS 140-2 compliant ciphers to create certificates and to configure your IP address security. To learn more about supported ciphers in Cloud VPN, see [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers). For guidance about how to select a cipher that conforms to FIPS 140-2 standards, see [FIPS 140-2 Validated](https://cloud.google.com/security/compliance/fips-140-2-validated). After you make a configuration, there is no way to change an existing cipher in Google Cloud. Ensure that you configure the same cipher on your third-party appliance that you use with Cloud VPN.

### Cloud Armor

[Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) is a DDoS mitigation and application protection service. It helps to protect against DDoS attacks on Google Cloud customer deployments with workloads that are exposed to the internet. Cloud Armor for [Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#load-balancer-mode) is designed to provide the same protection and capabilities for regional load balanced workloads. Because Google Cloud Armor web-application firewalls (WAF) use a regional scope, your configurations and traffic reside in the region where the resources are created. You must create [regional backend security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types) and attach them to backend services which are regionally scoped. The new regional security policies can only be applied to regionally scoped backend services in the same region, and are stored, evaluated, and enforced in-region. Cloud Armor for Network Load Balancers and VMs extends Cloud Armor DDoS protection for workloads exposed to the internet through a Network Load Balancer (or protocol forwarding) forwarding rule, or through a VM that's directly exposed through a public IP. To enable this protection, you must configure [advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).

### Dedicated Interconnect

To use [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview), your network must physically connect to Google's network in a supported colocation facility. The facility provider supplies a 10G or 100G circuit between your network and a Google Edge point-of-presence. You must only use Cloud Interconnect in colocation facilities within the US that serve Google Cloud US regions.

When you use Partner Cloud Interconnect, you must consult with the service provider to confirm that their locations are within the US and connected to one of the Google Cloud US locations listed later in this section.

By default, the traffic sent over Cloud Interconnect is unencrypted. If you want to encrypt traffic sent over Cloud Interconnect then you can configure [VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) or [MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).

For the full list of supported regions and co-locations, see the following table:

Region | Location | Facility name | Facility  
---|---|---|---  
us-east4 (Virginia) | Ashburn | `iad-zone1-1` | [Equinix Ashburn (DC1-DC11)](https://www.peeringdb.com/fac/1)  
Ashburn | `iad-zone2-1` | [Equinix Ashburn (DC1-DC11)](https://www.peeringdb.com/fac/1)  
Ashburn | `iad-zone1-5467` | [CoreSite - Reston (VA3)](https://www.peeringdb.com/fac/5467)  
Ashburn | `iad-zone2-5467` | [CoreSite - Reston (VA3)](https://www.peeringdb.com/fac/5467)  
us-east5 (Columbus) | Columbus | `cmh-zone1-2377` | [Cologix COL1](https://www.peeringdb.com/fac/2377)  
Columbus | `cmh-zone2-2377` | [Cologix COL1](https://www.peeringdb.com/fac/2377)  
us-central1 (Iowa) | Council Bluffs | `cbf-zone1-575` | [Nebraska data centers (1623 Farnam)](https://www.peeringdb.com/fac/575)  
Council Bluffs | `cbf-zone2-575` | [Nebraska data centers (1623 Farnam)](https://www.peeringdb.com/fac/575)  
us-south1 (Dallas) | Dallas | `dfw-zone1-4` | [Equinix Dallas (DA1)](https://www.peeringdb.com/fac/4)  
Dallas | `dfw-zone2-4` | [Equinix Dallas (DA1)](https://www.peeringdb.com/fac/4)  
us-west1 (Oregon) | Portland | `pdx-zone1-1922` | [EdgeConneX Portland (EDCPOR01)](https://www.peeringdb.com/fac/1922)  
Portland | `pdx-zone2-1922` | [EdgeConneX Portland (EDCPOR01)](https://www.peeringdb.com/fac/1922)  
us-west2 (Los Angeles) | Los Angeles | `lax-zone1-8` | [Equinix Los Angeles (LA1)](https://www.peeringdb.com/fac/8)  
Los Angeles | `lax-zone2-8` | [Equinix Los Angeles (LA1)](https://www.peeringdb.com/fac/8)  
Los Angeles | `lax-zone1-19` | [CoreSite - LA1 - One Wilshire](https://www.peeringdb.com/fac/19)  
Los Angeles | `lax-zone2-19` | [CoreSite - LA1 - One Wilshire](https://www.peeringdb.com/fac/19)  
Los Angeles | `lax-zone1-403` | [Digital Realty LAX (600 West 7th)](https://www.peeringdb.com/fac/403)  
Los Angeles | `lax-zone2-403` | [Digital Realty LAX (600 West 7th)](https://www.peeringdb.com/fac/403)  
Los Angeles | `lax-zone1-333` | [Equinix LA3/LA4 - Los Angeles, El Segundo](https://www.peeringdb.com/fac/333)  
Los Angeles | `lax-zone2-333` | [Equinix LA3/LA4 - Los Angeles, El Segundo](https://www.peeringdb.com/fac/333)  
us-west3 (Salt Lake City) | Salt Lake City | `slc-zone1-99001` | [Aligned Salt Lake (SLC-01)](https://www.peeringdb.com/fac/7865)  
Salt Lake City | `slc-zone2-99001` | [Aligned Salt Lake (SLC-01)](https://www.peeringdb.com/fac/7865)  
us-west4 (Las Vegas) | Las Vegas | `las-zone1-770` | [Switch Las Vegas](https://www.peeringdb.com/fac/770)  
Las Vegas | `las-zone2-770` | [Switch Las Vegas](https://www.peeringdb.com/fac/770)  
  
## What's next

  * Learn more about the Google Cloud products used in this design guide: 
    * [Google Virtual Private Cloud](https://docs.cloud.google.com/vpc)
    * [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview)
    * [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview)
    * [Google Load Balancing](https://docs.cloud.google.com/load-balancing/docs)
    * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
    * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)
    * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
    * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Haider Witwit](https://www.linkedin.com/in/haider-witwit-8829951a) | Networking Specialist Architect
  * [Bhavin Desai](https://www.linkedin.com/in/bhavin-desai) | Product Manager



Other contributors: 

  * [Ashwin Gururaghavendran](https://www.linkedin.com/in/ashwinguru/) | Software Engineer
  * [Percy Wadia](https://www.linkedin.com/in/percywadia) | Group Product Manager
  * [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect
  * [Marquis Carroll](https://www.linkedin.com/in/mcarroll144) | Consultant
  * [Michele Chubirka](https://www.linkedin.com/in/mchubirka) | Cloud Security Advocate



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
