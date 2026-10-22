---
url: https://docs.cloud.google.com/docs/security/gcmvsp/network-security/
title: Network security guidelines \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:48.865399+00:00
---

# Network security guidelines  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/gcmvsp/network-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Network security guidelines Stay organized with collections  Save and categorize content based on your preferences. 

The following guidelines for the minimum viable security platform align with the network security pillar.

## Basic level guidelines

Implement the following network security guidelines first.

Item | 

### Block default network creation  
  
---|---  
Description | The `compute.skipDefaultNetworkCreation` boolean constraint skips the creation of the default network and related resources when creating Google Cloud projects.The default network is an auto-mode Virtual Private Cloud (VPC) network with pre-populated IPv4 firewall rules to allow internal communication paths. Generally, this setup isn't a recommended security posture for production environments.  
Related information | 

  * [Organization policy constraints](https://docs.cloud.google.com/vpc/docs/vpc#org-policies)

  
Item ID | MVSP-CO-1-47  
Mapping |  Related NIST-800-53 controls:

  * SC-7
  * SC-8

Related CRI profile controls:

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

Compliance Manager control:

  * [Restrict Default Network Creation for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-default-network-creation-for-compute-engine)

  
Item | 

### Enable Private Google Access  
  
---|---  
Description | Enable Private Google Access on all subnets.Enabling Private Google Access lets services access Google Cloud services that don't have external IP addresses. By default, Private Google Access isn't enabled on new resources and requires additional steps to explicitly enable it.  
Related information | 

  * [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access)

  
Item ID | MVSP-CO-1.52  
Mapping |  Related NIST-800-53 controls:

  * SC-7
  * SC-8
  * SC-13

Related CRI profile controls:

  * PR.AC-3.1

Compliance Manager control:

  * [Enable Private Google Access on an instance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-private-google-access)

  
  
## Intermediate level guidelines

After you implemented the basic guidelines, implement the following network security guidelines.

Item | 

### Use Cloud Armor policies  
  
---|---  
Description | For applications that are exposed behind Cloud Load Balancing, use Google Cloud Armor default policies or configure your own policies to add Layer 3 to Layer 7 network protection for externally-facing applications or services. Cloud Armor security policies help protect your application by providing Layer 7 filtering. These policies also review incoming requests for common web attacks or other Layer 7 attributes to potentially block traffic before the traffic reaches your load-balanced backend services or backend buckets. Each security policy is made up of a set of rules that include attributes from Layer 3 through Layer 7.  
Related information | 

  * [Cloud Armor overview](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)

  
Item ID | MVSP-CO-1.49  
Mapping |  Related NIST-800-53 controls:

  * SC-7

Related CRI profile controls:

  * PR.AC-3.1

Compliance Manager control:

  * [Define a Security Policy to Mitigate for DDoS Events](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#define-security-policy-mitigate-ddos-events)

  
Item | 

### Restrict outbound traffic  
  
---|---  
Description | Limit access to external sources because by default, all access is allowed out. Set specific firewall rules for intended patterns of traffic needing to egress.By default, systems are often allowed to make outbound connections to the internet, which can be deemed a security risk. A deny-by-default policy blocks outbound traffic and requires specific rules to be created for only the known, necessary destinations.  
Related information | 

  * [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls)

  
Item ID | MVSP-CO-1.50  
Mapping |  Related NIST-800-53 controls:

  * SC-7

Related CRI profile controls:

  * PR.AC-3.1

Compliance Manager control:

  * [Enforce Deny All Egress Firewall Rule](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enforce-deny-all-egress-firewall-policy)

  
Item | 

### Limit inbound access to SSH and RDP ports  
  
---|---  
Description | Where possible, restrict inbound access to specific resources and resource ranges only. If Identity-Aware Proxy (IAP) is configured, set inbound SSH and Remote Desktop Protocol (RDP) firewall rules to IAP IP ranges as sources.Permissive SSH and RDP firewall rules allow for brute force attacks. Instead, use Google Cloud identity-aware proxies (such as IAP) for SSH and RDP.  
Related information | 

  * [Using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding)

  
Item ID | MVSP-CO-1.51  
Mapping |  Related NIST-800-53 controls:

  * SC-7

Related CRI profile controls:

  * PR.AC-3.1

Compliance Manager control:

  * [Block Access to SSH Port](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-access-to-ssh-port)
  * [Block Access to RDP Port](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-access-to-rdp-port)

  
  
## Advanced level guidelines

After you implemented the intermediate guidelines, implement the following network security guidelines.

Item | 

### Enable VPC Service Controls  
  
---|---  
Description | Enable VPC Service Controls as an additional layer of protection to prevent potential data loss.VPC Service Controls can help prevent data exfiltration by creating isolation perimeters around your cloud resources, sensitive data, and networks.  
Related information | 

  * [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)
  * [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products)

  
Item ID | MVSP-CO-1.48  
Mapping |  Related NIST-800-53 controls:

  * SC-7
  * SC-8

Related CRI profile controls:

  * PR.AC-3.1

Compliance Manager control:

  * [Define Service Perimeters in VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#define-service-perimeter)

  
  
## What's next

  * [Monitoring, logging, and alerting guidelines](https://docs.cloud.google.com/docs/security/gcmvsp/monitoring-logging-alerting)
  * [Overview of minimum viable secure platform](https://docs.cloud.google.com/docs/security/gcmvsp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
