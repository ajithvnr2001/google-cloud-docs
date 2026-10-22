---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices/
title: General best practices \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:30.756656+00:00
---

# General best practices  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  General best practices Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

When designing and onboarding cloud identities, resource hierarchy, and landing zone networks, consider the design recommendations in [Landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones) and the Google Cloud security best practices covered in the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). Validate your selected design against the following documents:

  * [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/architecture/best-practices-vpc-design)
  * [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design)
  * [Google Cloud Well-Architected Framework: Security, privacy, and compliance](https://docs.cloud.google.com/architecture/framework/security)



Also, consider the following general best practices:

  * When choosing a hybrid or multicloud network connectivity option, consider business and application requirements such as SLAs, performance, security, cost, reliability, and bandwidth. For more information, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product) and [Patterns for connecting other cloud service providers with Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-connecting-other-csps-with-gcp).

  * Use shared VPC networks on Google Cloud instead of multiple VPC networks when appropriate and aligned with your [resource hierarchy design](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy) requirements. For more information, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).

  * Follow the best practices for [planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning).

  * Where applicable, [establish a common identity](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities) between environments so that systems can authenticate securely across environment boundaries.

  * To securely expose applications to corporate users in a hybrid setup, and to choose the approach that best fits your requirements, you should follow the recommended ways to [integrate Google Cloud with your identity management system](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment).

    * Also, see [Patterns for authenticating workforce users in a hybrid environment](https://docs.cloud.google.com/architecture/patterns-for-authenticating-corporate-users-in-a-hybrid-environment).
  * When designing your on-premises and cloud environments, consider IPv6 addressing early on, and account for which services support it. For more information, see [An Introduction to IPv6 on Google Cloud](https://cloud.google.com/blog/products/networking/getting-started-with-ipv6-on-google-cloud). It summarizes the services that were supported when the blog was written.

  * When designing, deploying, and managing your VPC firewall rules, you can:

    * Use [service-account-based filtering over network-tag-based filtering](https://docs.cloud.google.com/vpc/docs/firewalls#service-accounts-vs-tags) if you need strict control over how firewall rules are applied to VMs.
    * Use [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) when you group several firewall rules, so that you can update them all at once. You can also make the policy hierarchical. For hierarchical firewall policy specifications and details, see [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies).
    * Use [geo-location objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview) in firewall policy when you need to filter external IPv4 and external IPv6 traffic based on specific geographic locations or regions.
    * Use [Threat Intelligence for firewall policy rules ](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview) if you need to secure your network by allowing or blocking traffic based on Threat Intelligence data, such as known malicious IP addresses or based on public cloud IP address ranges. For example, you can allow traffic from specific public cloud IP address ranges if your services need to communicate with that public cloud only. For more information, see [Best practices for firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#best_practices_for_firewall_rules).
  * You should always design your cloud and network security using a multilayer security approach by considering additional security layers, like the following:

    * [Google Cloud Armor](https://docs.cloud.google.com/armor)
    * [Cloud Intrusion Detection System](https://docs.cloud.google.com/intrusion-detection-system/docs/overview)
    * [Cloud Next Generation Firewall IPS](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention#how-ips-works)
    * [Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview)

These additional layers can help you filter, inspect, and monitor a wide variety of threats at the network and application layers for analysis and prevention.

  * When deciding where DNS resolution should be performed in a hybrid setup, we recommend using two authoritative DNS systems for your private Google Cloud environment and for your on-premises resources that are hosted by existing DNS servers in your on-premises environment. For more information see, [Choose where DNS resolution is performed](https://docs.cloud.google.com/dns/docs/best-practices#choose_where_dns_resolution_is_performed).

  * Where possible, always expose applications through APIs using an API gateway or load balancer. We recommend that you consider an API platform like Apigee. Apigee acts as an abstraction or facade for your backend service APIs, combined with security capabilities, rate limiting, quotas, and analytics.

  * An API platform (gateway or proxy) and [Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) aren't mutually exclusive. Sometimes, using both API gateways and load balancers together can provide a more robust and secure solution for managing and distributing API traffic at scale. Using [Cloud Load Balancing API gateways](https://docs.cloud.google.com/api-gateway/docs/gateway-serverless-neg) lets you accomplish the following:

    * Deliver high-performing APIs with Apigee and Cloud CDN, to:

      * Reduce latency
      * Host APIs globally
      * Increase availability for peak traffic seasons

For more information, watch [Delivering high-performing APIs with Apigee and Cloud CDN](https://www.youtube.com/watch?v=lwiJUaGPCK4) on YouTube.

    * Implement advanced traffic management.

    * Use Cloud Armor as DDoS protection, WAF, and network security service to protect your APIs.

    * Manage efficient load balancing across gateways in multiple [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). For more information, watch [Securing APIs and Implementing multi-region failover with PSC and Apigee](https://www.youtube.com/watch?v=AatzC4ct7co).

  * To determine which Cloud Load Balancing product to use, you must first determine what traffic type your load balancers must handle. For more information, see [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer).

  * When Cloud Load Balancing is used, you should use its [application capacity optimization abilities](https://docs.cloud.google.com/load-balancing/docs/tutorials/about-capacity-optimization-with-global-lb) where applicable. Doing so can help you address some of the capacity challenges that can occur in globally distributed applications.

    * For a deep dive on latency, see [Optimize application latency with load balancing](https://docs.cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency).
  * While Cloud VPN encrypts traffic between environments, with Cloud Interconnect you need to use either MACsec or HA VPN over Cloud Interconnect to [encrypt traffic in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit) at the connectivity layer. For more information, see [How can I encrypt my traffic over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq#encryption).

    * You can also consider service layer encryption using TLS. For more information, see [Decide how to meet compliance requirements for encryption in transit](https://docs.cloud.google.com/architecture/landing-zones/decide-security#encrypt-transit).
  * If you need more traffic volume over a VPN hybrid connectivity than a single VPN tunnel can support, you can consider using [active/active HA VPN routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#active) option.

    * For long-term hybrid or multicloud setups with high outbound data transfer volumes, consider Cloud Interconnect or Cross-Cloud Interconnect. Those connectivity options help to optimize connectivity performance and might reduce outbound data transfer charges for traffic that meets certain conditions. For more information, see [Cloud Interconnect pricing](https://cloud.google.com/network-connectivity/docs/interconnect/pricing).
  * When [connecting to Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#google-cloud) resources and trying to choose between Cloud Interconnect, Direct Peering, or Carrier Peering, we recommend using Cloud Interconnect, unless you need to access Google Workspace applications. For more information, you can compare the features of [Direct Peering with Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#dp-compare) and [Carrier Peering with Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cp-compare).

  * Allow enough IP address space from your existing RFC 1918 IP address space to accommodate your cloud-hosted systems.

  * If you have technical restrictions that require you to keep your IP address range, you can:

    * Use the same internal IP addresses for your on-premises workloads while migrating them to Google Cloud, using [hybrid subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets).

    * Provision and use your own public IPv4 addresses for Google Cloud resources using [bring your own IP (BYOIP)](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) to Google.

  * If the design of your solution requires exposing a Google Cloud-based application to the public internet, consider the design recommendations discussed in [Networking for internet-facing application delivery](https://docs.cloud.google.com/architecture/network-application-delivery).

  * Where applicable, use [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/private-service-connect) to allow workloads in Google Cloud, on-premises, or in another cloud environment with hybrid connectivity, to privately access Google APIs or published services, using internal IP addresses in a fine-grained fashion.

  * When using Private Service Connect, you must control the following:

    * Who can deploy Private Service Connect resources.
    * Whether connections can be established between consumers and producers.
    * Which network traffic is allowed to access those connections.

For more information, see [Private Service Connect security](https://docs.cloud.google.com/vpc/docs/private-service-connect-security).

  * To achieve a robust cloud setup in the context of hybrid and multicloud architecture:

    * Perform a comprehensive assessment of the required levels of reliability of the different applications across environments. Doing so can help you meet your objectives for availability and resilience.
    * Understand the reliability capabilities and [design principles](https://docs.cloud.google.com/architecture/framework/reliability#core_principles) of your cloud provider. For more information, see [Google Cloud infrastructure reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide).
  * Cloud network visibility and monitoring are essential to maintain reliable communications. [Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center/docs) provides a single console for managing network visibility, monitoring, and troubleshooting.




[ Previous arrow_back  Handover pattern  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/handover-pattern)

[ Next What's next  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/whats-next)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
