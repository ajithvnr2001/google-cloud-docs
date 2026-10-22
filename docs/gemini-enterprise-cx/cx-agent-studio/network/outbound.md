---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/network/outbound/
title: Outbound networking \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:30.150240+00:00
---

# Outbound networking  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/network/outbound/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Outbound networking Stay organized with collections  Save and categorize content based on your preferences. 

Agents often require real-time API access to external, public-facing software-as-a-service (SaaS) platforms to retrieve interaction histories or trigger immediate operational workflows. This is accomplished by configuring [tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool#available_tools) and [callbacks](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback).

## Egress categories

To deliver context-aware, real-time interactions, CX Agent Studio must seamlessly interface with a diverse ecosystem of data sources and workflow automation platforms. This requires robust, secure egress routing mechanisms capable of traversing both public internet boundaries and highly restricted private networks. Integration architectures generally fall into two primary egress categories:

### Public and hybrid SaaS egress

By default, CX Agent Studio agents operate within a Google-managed tenant project that routes egress internet traffic through a shared, dynamic pool of public IP addresses. If your security architecture relies on firewall allow-listing and must accommodate this default path, you can retrieve the full list of public IP ranges allocated to Google APIs and services.

However, because Google manages these IP addresses globally, the published ranges are broad, shared across multiple Google Cloud customers, and subject to frequent changes. It is not possible to isolate specific IP blocks dedicated exclusively to your individual agent application instance using this method.

To track these dynamic changes and maintain firewall synchronization, you must implement an automated sync process:

Google publishes its [IP ranges for default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults) in a JSON payload. Because these ranges shift frequently without prior notification, you should configure a daily automated script (such as a cron job or Cloud Function) to fetch the payload, parse the CIDR blocks, and programmatically update your enterprise firewall rules.

### Private, multicCloud, and on-premises egress

For highly sensitive or proprietary data, agent applications can be configured to securely route traffic into isolated environments. This includes interfacing with privately hosted Model Context Protocol (MCP) tools, custom middleware, and core databases or public SaaS platforms that comply with strict ingress firewalls by leveraging a stable, static external IP address. Supported network topologies include:

  * [Cross-Cloud Interconnect (CCI)](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cross-cloud-interconnect) connects agent applications directly to private endpoints hosted on secondary cloud providers (such as AWS, Azure, or OCI) over a dedicated physical link, bypassing the public internet entirely to ensure low latency and high security.
  * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) and [High Availability VPN (HA-VPN)](https://docs.cloud.google.com/network-connectivity/docs/vpn) connects GECX agents to on-premises networks by bridging the Google-managed tenant project into your VPC, then routing traffic directly to your data center over a private, physical fiber connection.
  * **Public Saas:** To provide a stable, static external IP address for internet egress, you can deploy dedicated infrastructure inside your own self-managed VPC and expose it to your agent application using Service Directory. This architecture bridges the Google-managed tenant project to your private network, allowing GECX to route outbound internet traffic through your managed gateways (such as Cloud NAT, Network Virtual Appliance) where you can assign and control permanent, static external IP addresses.



## Service Directory and Private network access

CX Agent Studio integrates with Service Directory, a managed registry that allows organizations to register and resolve services for secure egress into their VPC. For CX Agent Studio, Service Directory acts as the foundational routing registry, mapping connections from the Google-managed tenant project directly to your private environment.

### Private network access

CX Agent Studio leverages [Private network access](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview) to establish a secure, isolated egress path for agent tools. When an agent tool invokes an API referencing Service Directory, the system bypasses normal public routing and secures the data path using the following:

  * CX Agent Studio facilitates direct traffic routing within your Virtual Private Cloud (VPC) by associating egress data with a designated private IP address from the Service Directory endpoint. This configuration creates a private gateway that efficiently transfers requests to the your internal network infrastructure.
  * Instead of routing traffic over the public internet—which introduces latency and security risks—CX Agent Studio establishes a secure, private, point-to-point tunnel. This traffic travels entirely over Google's internal network backbone, ensuring that sensitive data never touches public infrastructure.
  * By combining Private Networking Access with Service Directory, this architecture enables agents to securely reach private endpoints, legacy on-premises tools, and isolated multicloud resources. Organizations can seamlessly grant AI agents operational access to internal APIs, or securely route traffic to public APIs using predictable, static external IP addresses for strict firewall access control.



CX Agent Studio tools can be configured to use Service Directory for private network connectivity. Alternatively, they can use the default internet egress path from the tenant network.

The following table outlines the compatibility for each CX Agent Studio feature based on these connectivity options:

CX Agent Studio feature | Private | Public  
---|---|---  
OpenAPI | ✅ Private network access | ✅ Using Public Internet  
MCP Server | ✅ Private network access | ✅ Using Public Internet  
Salesforce tool | ✅ Private network access | ✅ Using Public Internet  
ServiceNow tool | ✅ Private network access | ✅ Using Public Internet  
Python code tool | ❌ | ✅ Using Public Internet  
Python callback | ❌ | ✅ Using Public Internet  
  
## Using Service Directory for private network access

Service Directory private network access enables CX Agent Studio to communicate with your Virtual Private Cloud (VPC) network resource once a Tool configured with Service Directory. The requests are sent over the private network while enforcing [Identity and Access Management(IAM)](https://docs.cloud.google.com/iam/docs/overview) and [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

The network resources supported as destinations are:

  * On-premises IP addresses, reached through Cloud Interconnect or Cloud VPN
  * Regional internal Application Load Balancers
  * Virtual machine (VM) instances
  * Internal passthrough Network Load Balancers



![inbound architecture](https://docs.cloud.google.com/static/gemini-enterprise-cx/cx-agent-studio/images/network-outbound-1.png)

For more information, see [Using Service Directory for private network access](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/vpc-service-controls#service-directory).

Service Directory limitations:

  * The Service Directory operates as a regional service.
  * Each CX Agent Studio agent application is limited to a single Service Directory configuration.
  * Service Directory does not support targeting a PSC Endpoint



## Outbound networking patterns

To optimize connectivity, configure a Service Directory entry to target an internal application load balancer (ALB). This approach provides centralized access to multiple egress endpoints, leveraging [URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) and Server Name Indication (SNI) routing to direct traffic across your backend services.

![inbound architecture](https://docs.cloud.google.com/static/gemini-enterprise-cx/cx-agent-studio/images/network-outbound-2.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
