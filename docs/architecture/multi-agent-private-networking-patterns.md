---
url: https://docs.cloud.google.com/architecture/multi-agent-private-networking-patterns/
title: Multi-agent private networking patterns in Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:01.667964+00:00
---

# Multi-agent private networking patterns in Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/multi-agent-private-networking-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Multi-agent private networking patterns in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-04-16 UTC

This document provides guidance to help you design private networking infrastructure that supports a publicly accessible, multi-agent, [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs) app with private connections between agents, subagents, and tools. The network design provides private connections for agents that are hosted in Agent Runtime on Gemini Enterprise Agent Platform, Cloud Run, Google Kubernetes Engine (GKE), on-premises data centers, or in other clouds. The design also supports connectivity to agents that run in internet locations.

Multi-agent AI systems often involve organizationally sensitive or proprietary data. Private networking lets you avoid exposing this traffic to the public internet. This design uses Google Cloud network infrastructure, Virtual Private Cloud (VPC) network resources, and private connectivity to on-premises environments or cross-cloud networks.

In the design that this document describes, agents communicate with other agents and with tools by using the Agent2Agent (A2A) protocol and the Model Context Protocol (MCP). Communications are made private by routing them through a VPC network. To move traffic into and out of the VPC network, this design uses a combination of Private Service Connect endpoints, Private Service Connect interfaces, and Cloud Run Direct VPC egress. Cloud Next Generation Firewall (Cloud NGFW) governs traffic that passes through the VPC network. Additional security layers provide controlled internet egress by using Secure Web Proxy and provide API service access policies by using a VPC Service Controls perimeter.

The intended audience for this document includes architects, developers, and administrators who build and manage cloud AI infrastructure and apps. This document assumes that you have a foundational understanding of AI agents and models and that you're familiar with Google Cloud networking concepts.

## Multi-agent design pattern

A multi-agent Gemini Enterprise app requires a custom agent to serve as an orchestrator or _root_ agent for connections to tools and subagents. To implement private connections to tools and subagents that are hosted in Google Cloud or on-premises, the design uses a VPC network with private IP addresses. The root agent is hosted within Google's infrastructure, using Agent Engine, Cloud Run, or GKE. The multi-agent design pattern highlights these interactions:

  1. **Gemini Enterprise app interacting with custom root agents**. [ Gemini Enterprise apps](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores) present a managed user interface with built-in security functions that expose custom agent functionality. Custom-built root agents are registered with Gemini Enterprise and they're made available in apps to end users. The custom root agent acts as a top-level workflow orchestrator and it delegates specialized tasks to subagents. This architecture uses custom root agents that are hosted on Agent Runtime on Gemini Enterprise Agent Platform, Cloud Run, or GKE.
  2. **Root agents interacting with subagents and tools**. The core of the AI system workflow and business logic resides in the root agent and in specialized subagents. The flexibility in the agent framework, runtime, and hosting platform allows for different options to connect root agents to subagents and tools through the VPC network. By using VPC networking for this part of the architecture, agents can use private networking paths that you define that expose other private endpoints, enterprise security controls, and broader network reachability.



![High-level overview of a multi-agent networking architecture.](https://docs.cloud.google.com/static/architecture/images/multi-agent-private-networking-patterns-overview.svg)![](https://docs.cloud.google.com/static/architecture/images/multi-agent-private-networking-patterns-overview.svg)

The architecture includes the following components:

  * **Gemini Enterprise app** : The frontend for users to access an in-app chat interface and interact with the multi-agent AI system. Users can access Gemini Enterprise apps through the public internet or privately through hybrid connections.
  * **Custom agents** : Root agents that are built and registered with Gemini Enterprise and that are hosted on Agent Runtime, Cloud Run, or GKE. These root agents function as orchestrators that delegate tasks to subagents.
  * **VPC network** : A resource that you control to provide agents with IP network connectivity to private endpoints and broader network reachability. The VPC network provides a platform to implement private connectivity and network security controls for agent requests to other agents and tools.
  * **Subagents** : Specialized agents that are triggered by the root agent workflow. Subagents communicate using the A2A protocol, which enables interoperability between agents regardless of programming language and runtime.
  * **Tools** : Remote systems that expose services such as APIs, data sources, and workflow functions. These tools fetch data and perform actions or transactions for agents. Tools are external to agents, and agents connect and interact with tools by using the MCP specification.



This high-level multi-agent design pattern highlights the networking components that are in a multi-agent AI system. It can support many different types of agent-to-agent routing patterns. For information about other AI system design patterns, see [Choose a design pattern for your agentic AI system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system).

### Shared VPC

The multi-agent design pattern uses Shared VPC to centralize networking and security authority and responsibility. This design provides developers with environments that help fulfill an organization's security needs. We recommend that you use Shared VPC to centralize to simplify your network and security configurations.

In a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) architecture, a _host project_ contains the shared network resources, including VPC networks, Cloud Routers, subnets, firewalls, and Cloud DNS. Administrators can grant _service projects_ access to use these resources. Service projects contain the agent runtime resources, including Agent Runtime, Cloud Run, GKE, Gemini Enterprise, and app-specific load balancers.

Shared VPC enforces a clear boundary between network and security administrator personas and AI app developer personas:

  * **Network and security administrators** control the core infrastructure, such as VPC routing, subnets, DNS peering, and firewall policies.
  * **AI app developers** build agents in attached service projects without having permissions to modify the underlying network infrastructure.



When you centralize network and security deployments within a host project, you create a single point of management for agent-to-agent and agent-to-service communication. This design simplifies the enforcement of security policies across many different service projects while ensuring consistent connectivity.

You can incorporate your Shared VPC network into a [ Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design) by using Network Connectivity Center (NCC) VPC spokes to add the Shared VPC network as a workload VPC network. This implementation provides the Shared VPC with full reachability to NCC hub routes and with connectivity to service access points from other spokes.

Requests that are initiated from custom root agents use a private, customer-managed VPC network to provide secure network paths to subagents, tools, and services. VPC network routing governs reachability to private endpoints. Cloud NGFW policies that are applied to the VPC network govern network access.

Agents gain secure access to private VPC network paths, including connectivity to the following:

  * Other VPC networks through VPC network peering, multi-NIC appliances, or NCC.
  * Private Service Connect endpoints for accessing producer services.
  * Managed services that have private IP addresses, such as Cloud SQL.
  * Internal load balancer front ends and Compute Engine resources.
  * Google APIs through Private Google Access or through Private Service Connect.
  * The internet, controlled through Secure Web Proxy.
  * Hybrid and cross-cloud destinations by using Cloud Interconnect, Cloud VPN, router appliance, or SD-WAN.
  * Any endpoint destination that's reachable through VPC network IP routing.
  * Other AI agents, tools, and supporting services.



For more information about Shared VPC, see these resources:

  * [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/architecture/best-practices-vpc-design)
  * [Google Cloud Setup guided flow](https://docs.cloud.google.com/docs/enterprise/cloud-setup)
  * [Cross-Cloud Network inter-VPC connectivity using NCC](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-ncc-vpn-ra)



## Gemini Enterprise networking

Gemini Enterprise apps are managed resources that operate in a hosted environment outside of the VPC network, but within Google's network. The following sections describe configuration for networking between the user and the Gemini Enterprise app and describe networking between the app and the agents.

### User chat to Gemini Enterprise apps

Users chat with the Gemini Enterprise app by using a browser-based app that sends requests to Google APIs and services. To enable private user connectivity, you can configure the Google API URLs to resolve to private IP address ranges that are routed over your VPC network. For more information, see [Configure private UI access](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access).

### Gemini Enterprise apps to custom agents

You register custom agents with the Gemini Enterprise discovery service. When you register an agent, Gemini Enterprise maps the name of the agent to a specific target, either the [ Agent Runtime resource URI](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent#register-an-adk-agent) or the [A2A agent URL](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent#register_a2a_agent-drest). Gemini Enterprise apps have a built-in chat interface that's called [the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat). When a user specifies an agent by using `@agent_name`, or when the assistant decides to delegate, the app looks up the agent in the registry to find the associated endpoint.

When you register a root agent with Gemini Enterprise, you can deploy that agent anywhere as a custom agent. Custom agents on Agent Runtime and on Cloud Run can use existing private network paths without configuring additional networking resources. In order to deploy a custom agent on GKE, you must expose the service with an [external Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#external-gateway). For information about how to configure the external Gateway to be more secure, see GKE networking later in this document.

To make requests to custom agents, Gemini Enterprise uses the Gemini Enterprise Agent Platform [Discovery Engine Service Account](https://docs.cloud.google.com/iam/docs/service-agents#discovery-engine-service-account) identity. The network path and authorization mechanisms differ based on the hosting platform that you use:

  * **Custom agents on Agent Runtime** : The Agent Platform Discovery Engine service agent includes the necessary Agent Platform Identity and Access Management (IAM) roles to invoke Agent Runtime resources as a built-in feature. The system routes requests that are made to the Agent Platform API service over the Google network as an internal API call.
  * **Custom agents on Cloud Run** : Gemini Enterprise apps use the Agent Platform Discovery Engine service agent identity to make calls to the stable `run.app` URL that's registered from the agent card. In order for the AI agent Cloud Run service to authorize these calls, you must grant the Cloud Run Invoker IAM role (`roles/run.invoker`) to the Discovery Engine Service Agent. Requests to Cloud Run are routed over the Google production network to the [Google Front End (GFE) for Cloud Run](https://docs.cloud.google.com/run/docs/securing/security) ingress.
  * **Custom agents on GKE** : Gemini Enterprise apps use the Agent Platform Discovery Engine service agent identity to make calls to the URL that's registered from the agent card. Public DNS must be able to resolve the hostname to an external IP address that's managed by the Gateway. We recommend that you use the `gke-l7-regional-external-managed` [load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities) or the `gke-l7-global-external-managed` load balancer. For added security, we recommend that Gemini Enterprise calls a GKE hosted A2A agent by using Identity-Aware Proxy (IAP). In order for IAP to authorize these calls, you must grant the IAP-secured Web App User IAM role (`roles/iap.httpsResourceAccessor`) to the Discovery Engine service agent. The Google production network routes requests to GKE to the GFE for external Application Load Balancer ingress.

To secure [GKE Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) from Gemini Enterprise, see the IAP and Google Cloud Armor sections later in this document.




## Private networking for agent hosting platforms

After a user initiates a request to the Gemini Enterprise app, requests are initiated from custom root agents to subagents and tools. The custom agent hosting platforms provide the interface between Gemini Enterprise and your VPC networks. The hosting platforms for your containerized agents and tools are Agent Runtime, Cloud Run, and GKE.

When you choose an agent hosting platform, you need to consider the private networking patterns, security controls, management control, level of customization, and security compliance of each platform. For more information about how to select an AI agent hosting platform, see [Choose models and infrastructure for your generative AI application](https://docs.cloud.google.com/docs/generative-ai/choose-models-infra-for-ai) and [Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components#agent_runtime).

You establish private VPC connectivity through different mechanisms based on the agent hosting platform that you use:

  * **Custom agents on Agent Runtime** : Private Service Connect interfaces connect the Agent Runtime runtimes to the VPC network. You [create a network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-network-attachments) in a subnet of your VPC network and give Agent Runtime permission to attach to it. Traffic that's sent from Agent Runtime appears in the VPC network as if it originated at the subnet IP address of the attachment. The VPC network then routes the traffic to the appropriate destination IP address.
  * **Custom agents on Cloud Run** : Cloud Run Direct VPC egress connects the Cloud Run service instances to the VPC network. The VPC network that's specified when a Cloud Run service is deployed can be from the Cloud Run service project or from its Shared VPC host project. Traffic that's sent from Cloud Run appears in the VPC network as if it originated at the subnet IP address of the Direct VPC egress. The VPC network then routes the traffic to the appropriate destination IP address.
  * **Custom agents on GKE** : GKE clusters reside directly in the VPC network and they use local subnet IP addresses. By default, GKE egress traffic uses the Pod IP address as the source IP address. If you configure masquerading, GKE egress traffic uses the node IP address as the source IP address. All GKE egress traffic is routed by the VPC network.



The following sections provide additional guidance for managing ingress and egress requests into and out of the VPC network for each agent hosting platform. The network considerations are applicable to both root agent and subagent functionality.

### Agent Runtime networking

This section describes private networking for root agents and subagents that are hosted on Agent Runtime. If you're using Agent Runtime to host your root agent, you must deploy Gemini Enterprise and Agent Runtime in the same project.

Agent Runtime hosts containers on Google infrastructure outside of your VPC network. To enable private connectivity to other agents, you can connect your agent to your VPC network by using the following methods:

  * To allow Agent Runtime agent traffic to egress to your VPC network, use [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces).
  * To allow agent traffic that's routed through your VPC network to ingress to your Agent Runtime agent, use [Private Service Connect endpoints for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).



To allow requests between your agents and other agents, set up both of the preceding connections.

#### Agent Runtime egress to the VPC network

Agent Runtime uses a Google-managed tenant project for network egress. The tenant network provides connectivity for agents to Google APIs and for public internet egress, but it isn't directly connected to customer VPC networks _by default_.

To connect agents to resources that are inside of your VPC network, Agent Runtime uses [ Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces). Agent Runtime deploys a network interface in the tenant project that connects to a [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments) resource in your project. This connection creates a secure data path between the Agent Runtime runtime and the VPC network. When you configure a Private Service Connect interface in your Agent Runtime project, the system routes all of the agent traffic that isn't destined for Google APIs to the VPC network.

**Note:** Agent Runtime resources can access agents that are hosted in Agent Runtime and in Cloud Run directly over the Google production network _without_ egressing to the VPC network. Agent Runtime has a private path to Google APIs and services that routes requests to the Agent Platform API for Agent Runtime and to `.run.app` URLs for Cloud Run. This traffic is subject to VPC Service Controls enforcement policies. For other security controls that are enforced by the VPC network, agent traffic must egress to the VPC network. To override default behavior and route Google API and Cloud Run service traffic to the VPC network, use [private DNS peering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#dns-peering).

To deploy Agent Runtime VPC network egress, see these resources:

  * [Using Private Service Connect interface with Agent Runtime](https://docs.cloud.google.com/agent-builder/agent-engine/private-service-connect-interface).
  * Deploy an agent: [Configure Private Service Connect interface](https://docs.cloud.google.com/agent-builder/agent-engine/deploy#psc-i).
  * Set up a Private Service Connect interface for Agent Platform resources: [Set up a private DNS peering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#dns-peering).
  * Deploy an agent: [Define environment variables](https://docs.cloud.google.com/agent-builder/agent-engine/deploy#environment-variables) for explicit proxy.



To further secure agents and the VPC network for Agent Runtime egress, see these sections later in this document:

  * Use Cloud NGFW policies and rules.
  * Configure VPC Service Controls protected resources.
  * Integrate Model Armor screening.
  * Deploy Secure Web Proxy for internet egress.



#### Agent Runtime ingress from the VPC network

Requests to agents that run on Agent Runtime are made by using the Agent Platform API endpoint (`aiplatform.googleapis.com`). To reach Google API endpoints by using private network paths from the VPC network, use Private Google Access or use [Private Service Connect endpoints for Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints).

Private users that make queries to agents need to resolve the Agent Platform API endpoint hostname to the private IP address range for [ Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain) or to the IP address of the [Private Service Connect endpoint for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#configure-dns-default). A private managed Cloud DNS [zone for `googleapis.com`](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#dns-config-google-apis) resolves requests for the Agent Platform API. The VPC network routes the request directly over the Google production network.

If you use Private Google Access or Private Service Connect for Google APIs, you can help protect traffic from your VPC network to Agent Runtime by using the following products and features:

  * [Agent Platform API authentication](https://docs.cloud.google.com/gemini/enterprise/docs/authentication)
  * VPC Service Controls
  * Model Armor



#### Additional Agent Runtime network considerations

Agent Runtime egress that uses Private Service Connect interfaces can only route to RFC 1918 IP address ranges in the VPC network. For specific destination ranges that aren't routable by Agent Runtime egress, see [Subnetwork IP range requirements](https://docs.cloud.google.com/agent-builder/agent-engine/private-service-connect-interface#subnetwork-ip-range-requirements). To reach non-routable IP address range destinations, use an explicit proxy configuration on the agents and deploy proxy resources that use a routable IP address in the VPC network.

When Agent Runtime is deployed _without_ a Private Service Connect interface, it has access to the internet by default. To protect against data exfiltration, disable the default access by enabling VPC Service Controls.

When Agent Runtime is deployed with a Private Service Connect interface, direct internet egress is disabled, regardless of VPC Service Controls. If you need your agent to access a destination that Agent Runtime can't normally reach, such as the internet, do the following:

  1. Configure Secure Web Proxy in an [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918#section-3) subnet of your VPC network. You must configure the proxy in [explicit proxy routing mode](https://docs.cloud.google.com/secure-web-proxy/docs/overview#explicit-proxy-routing).
  2. Create a Cloud DNS record for the Secure Web Proxy hostname.
  3. Configure [DNS peering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#dns-peering) for Agent Runtime to support agent DNS query resolution to the private address of the Secure Web Proxy in the VPC network.
  4. When you deploy agents do the following: 
     1. Define [environment variables](https://docs.cloud.google.com/agent-builder/agent-engine/deploy#environment-variables) to use the explicit proxy by specifying the Secure Web Proxy hostname and port.
     2. If you're accessing a private destination, configure a private DNS zone for that destination.



After traffic from Agent Runtime egress reaches the VPC network, it can reach any network destination that's routable by the VPC network. For information about how to limit the scope of egress network destinations that are available to Agent Runtime agents, see the Cloud NGFW section later in this document.

### Cloud Run networking

This section describes private networking for root agents and subagents that are hosted on Cloud Run. Cloud Run hosts containers on Google infrastructure outside of your VPC network. To enable private connectivity to other agents, you can connect your agent to your VPC network by using the following methods:

  * To allow Cloud Run agent traffic to egress to your VPC network, use [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).
  * To allow agent traffic that's routed through your VPC network to ingress to your Cloud Run agent, use [ Private Service Connect endpoints for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).



To allow requests between your agents and other agents, set up both of the preceding connections.

#### Cloud Run egress to the VPC network

To initiate Cloud Run connections into a VPC network, we recommend that you use [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc). With Direct VPC egress, Cloud Run instances connect directly to the shared VPC network by using an IP address from the subnet that you specify when you deploy Direct VPC egress.

When you configure Direct VPC egress, do the following:

  1. Configure the target subnet with [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) enabled.
  2. Configure [traffic routing to route all traffic to the VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#console).



This configuration sends all traffic through the VPC network for privacy and it sends requests from Cloud Run to other Google APIs over the Google internal network.

All of the [DNS queries from Cloud Run](https://docs.cloud.google.com/run/docs/securing/private-networking#to-vpc) use the Cloud DNS policy and zones that are associated with the VPC network. No additional DNS peering configuration is required. Agents that are hosted on Cloud Run resolve all of the Cloud DNS private zones and public hostnames.

For information about how to further secure agents and the VPC network for Cloud Run egress, see these sections later in this document:

  * Use Cloud NGFW policies and rules.
  * Configure VPC Service Controls protected resources.
  * Integrate Model Armor screening.
  * Deploy Secure Web Proxy for internet egress.



#### Cloud Run ingress from the VPC network

Cloud Run is a Google-managed platform that operates in an environment outside of the VPC network. This environment hosts the stable `*.run.app` URL endpoint for Cloud Run services that run AI agent or tool workloads. These endpoints are served by the same GFE entry point that serves `*.googleapis.com` API services. Cloud Run uses the same underlying network paths that enable private connectivity for Private Google Access and for Private Service Connect for Google APIs.

Private users on the VPC network that make queries to agents or tools need to resolve the `run.app` hostname to the private IP address range for [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain) or to the IP address of the [Private Service Connect endpoint for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#configure-dns-default). A private managed Cloud DNS [zone for the `run.app` URL](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#dns-config-other-domains) resolves requests for Cloud Run services. The VPC network routes the request directly over the Google production network.

Setting Cloud Run ingress to [Internal](https://docs.cloud.google.com/run/docs/securing/ingress#settings) restricts access to your service by permitting requests only from verified internal sources. Approved sources include the following:

  * VPC networks of the Cloud Run service project.
  * The Shared VPC network that hosts the Direct VPC egress endpoint.
  * Resources that are within the same VPC Service Controls perimeter.
  * Internal Application Load Balancers in the VPC network.
  * Google services like Cloud Scheduler and Pub/Sub that are within the service project or VPC Service Controls perimeter.



If you don't use a common VPC Service Controls perimeter to encompass both the calling and called services, traffic that's from outside the Cloud Run service project or the Shared VPC environment is treated as external. Such traffic includes traffic from other Google Cloud services like Agent Runtime and other Cloud Run services. To satisfy the Cloud Run Internal ingress check, this traffic must be routed in a way that it appears to originate from within the target service's VPC network.

To provide the necessary internal network attribution, you can do either of the following:

  * Use **Private Service Connect endpoints** to allow services in other VPCs or projects to connect to Google APIs and services, including your Cloud Run service, by using a private IP address within your VPC network.
  * Route traffic through an **internal Application Load Balancer** placed within your VPC network in front of your Cloud Run service. The load balancer funnels requests from other services through the VPC network so they meet the internal ingress criteria.



Internal Application Load Balancers with serverless network endpoint group (NEG) backends create a VPC resource that's mapped directly to a Cloud Run service. In this model, the load balancer terminates client TLS connections with a trusted certificate. Internal Application Load Balancers support additional security controls including Cloud Armor [backend security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview) and additional [authorization policies](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb).

By default, access to all Cloud Run services requires IAM authentication. We recommend that you use an identity on a per-service basis and grant the [principal](https://docs.cloud.google.com/iam/docs/overview#principals) the Cloud Run Invoker IAM role (`roles/run.invoker`).

For information about how to configure Cloud Run ingress controls, see these resources:

  * [Restrict network endpoint ingress for Cloud Run services](https://docs.cloud.google.com/run/docs/securing/ingress)
  * [Access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access)
  * [Receive requests from your private network](https://docs.cloud.google.com/run/docs/securing/private-networking#from-private-network)
  * [Set up a regional internal Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless)



If you use Private Google Access or [Private Service Connect endpoints for Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) to send traffic from your VPC network to Cloud Run, you can help protect that traffic by using the following products and features:

  * [Cloud Run ingress controls](https://docs.cloud.google.com/run/docs/securing/ingress)
  * [Cloud Run authentication](https://docs.cloud.google.com/run/docs/authenticating/overview)
  * VPC Service Controls
  * Model Armor



If you use an internal Application Load Balancer to send traffic from your VPC network to Cloud Run, you can help protect that traffic by using the following products and features:

  * [Cloud Run ingress controls](https://docs.cloud.google.com/run/docs/securing/ingress)
  * [Cloud Run authentication](https://docs.cloud.google.com/run/docs/authenticating/overview)
  * VPC Service Controls
  * Model Armor
  * [Load balancer certificate validation](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)
  * [Cloud Armor backend security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview)
  * [Load balancer authorization policies](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview)



### GKE networking

This section describes networking for agents that are based on GKE.

#### GKE and Gemini Enterprise

As a host for AI agents and tools, GKE offers a highly customizable platform for network and security controls. A multi-agent AI system that's deployed on GKE can provide operational efficiency at scale. It can tightly integrate with other Kubernetes apps and larger microservices architectures.

GKE clusters are Compute Engine VM nodes that run within a subnet of the VPC network. Gemini Enterprise apps are managed resources that operate in a hosted environment outside of the VPC network. To enable Gemini Enterprise apps to call custom agents that are hosted on GKE, you must securely expose an external Gateway with a public IP address and DNS name. Traffic flows from Gemini Enterprise egress to the Google edge network where it takes an optimized route to the GKE external load balancer.

It's important to secure the GKE endpoint by using strong authentication and authorization, Cloud Armor, and limited permissions. To provide a comprehensive defense-in-depth model to secure AI agents that run on GKE, consider the security controls that are described in the following sections.

##### GKE mode of operation

GKE offers these modes of operation to balance management and control:

  * **Autopilot** : Google automates the entire GKE cluster infrastructure, including the control plane, node provisioning, security hardening, and scaling.
  * **Standard** : Google manages the control plane. You retain full responsibility for node pool configurations, such as selecting machine types, managing OS images, and manual scaling.



##### Infrastructure and control plane hardening

  * **Private GKE clusters** : Provision nodes without public IP addresses, which ensures that the runtime environment is isolated from direct internet exposure.
  * **Master authorized networks** : Restrict administrative access to the Kubernetes API to specific, trusted IP address ranges, which hardens the control plane against unauthorized configuration changes. Secure the DNS Endpoint for Kubernetes API by using Google Cloud's IAM and VPC Service Controls.



##### Identity and access (zero trust)

  * **IAP** : Acts as a gatekeeper at the load balancer level. It ensures that only authenticated users with the correct IAM permissions can access the agent endpoint. This approach effectively shifts the security perimeter from the network to the individual user and their device context.



##### Edge protection and traffic management

  * **Cloud Armor** : Provides robust edge security, including Web Application Firewall (WAF) rules to help block malicious payloads, DDoS protection to help ensure uptime, and rate limiting to help prevent service exhaustion.
  * **Model Armor** : Specifically designed for LLM safety, Model Armor inspects and sanitizes prompts and responses in real-time to prevent prompt injection and data exfiltration.



##### Internal network isolation

  * **Kubernetes network policies** : Enforces granular, least-privilege communication between microservices. By default, policies deny all traffic unless you explicitly permit it, which prevents lateral movement within the cluster.



#### GKE egress to the VPC network

The VPC network routes outbound connections from agents that are hosted on GKE. The default GKE cluster network mode is [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips), which provides the following attributes:

  * The GKE cluster uses alias IP address ranges.
  * Pod IP addresses are reserved by specifying the Pod IP range.
  * Pod IP addresses are natively routable within the cluster VPC network and other connected VPC networks.



If an agent Pod is communicating with a subagent Pod in the same node, then the traffic is locally routed within the node network namespace. If the destination agent Pod is on a different node within the cluster, then traffic is routed by using the VPC network routing table. For an agent Pod to communicate with other VPC resources like load balancers or Private Service Connect endpoints, it can reach the destination by using the same standard VPC routing, subject to firewall rules.

You can help protect traffic that leaves your GKE cluster by using the following products and services:

  * Model Armor
  * [Cloud NGFW](https://docs.cloud.google.com/firewall/docs/about-firewalls)
  * [GKE network policies](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy)
  * [Private GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/legacy/network-isolation)



#### GKE ingress from the VPC network

Kubernetes [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) provide access to GKE resources. For a multi-agent AI system, we recommend that you use a [GKE Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways) or a [ GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway). The Gateway provides enhanced capabilities with traffic control, operational separation of resources, and security integrations. However, other [ingress service options](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-networking#choosing_the_method_to_expose_your_application) are available depending on your system requirements.

The Gateway resource creates an Application Load Balancer and it provisions all of the necessary load balancing components. The backend network endpoint groups of the service are wired to provide load balancing directly to containers. To expose a service internally for traffic that's sourced from the VPC network, use the Gateway classes for regional internal Application Load Balancer (`gke-l7-rilb`) or cross-region internal Application Load Balancer (`gke-l7-cross-regional-internal-managed-mc`).

Application Load Balancers provide additional security control points to protect AI agents and tools that are hosted on GKE clusters:

  * **Cloud Armor** : Protects services by attaching a Cloud Armor security policy to the backend services that are managed by the Gateway. It provides WAF screening, IP address and geo-based filtering, DDoS protection, and rate limiting before traffic reaches the GKE cluster or IAP.
  * **IAP** : Enabled on the backend service to control access to apps by using IAM credentials, IAP enforces zero-trust access policies. IAP authenticates and authorizes the AI agents that access the cluster resources, including Gemini Enterprise apps, custom agents, and external resources. It requires callers to have an identity that's authenticated by IAM and to have authorized permission to access the backend service.



If you send traffic from your VPC network to your GKE service through a Gateway, you can help protect that traffic by using the following products and features:

  * [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview)
  * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * VPC Service Controls
  * Model Armor



If you don't use a Gateway to send traffic from your VPC network to your GKE service, you can help protect that traffic by using the following products and services:

  * VPC Service Controls
  * Model Armor
  * [Cloud NGFW](https://docs.cloud.google.com/firewall/docs/about-firewalls)
  * [GKE network policies](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy)
  * [GKE network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)
  * [Private GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/legacy/network-isolation)



For more information about securing GKE, see [Network security best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking#network-security) and [Understand network security in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-in-networking).

## Agent network security

To protect the network of a multi-agent AI system, you must secure communications through both the VPC network and the API surface. The VPC network dataplane addresses how agents and tools securely connect. The API surface defines which identities and types of data exchanges are allowed. Layering access controls across both the VPC network and the API surface helps to enforce a highly controlled and resilient security posture.

### Cloud NGFW

Cloud NGFW acts as the network-level gatekeeper to secure A2A and MCP communications. The firewall ensures that only authorized traffic can reach the agent endpoints by verifying every incoming or outgoing connection to and from other agents and tools.

[Cloud NGFW](https://docs.cloud.google.com/firewall/docs/about-firewalls) is a distributed firewall service that's built into the VPC network fabric. It offers these feature tiers that operate at different layers of the network stack:

  * **Cloud Next Generation Firewall Essentials** : Provides stateful firewall packet filtering. Policy rules are defined based on IP addresses (L3), protocols, and ports (L4).
  * **Cloud Next Generation Firewall Standard** : Provides IP-based enforcement with Fully Qualified Domain Name (FQDN) objects, geolocation objects, and feeds from Google Threat Intelligence to block known malicious addresses.
  * **Cloud Next Generation Firewall Enterprise** : Provides true app (L7) inspection capabilities with TLS decryption and intrusion detection and prevention system (IDPS) capabilities to analyze payloads against advanced threat signatures.



Cloud NGFW can be applied on the VPC network to enforce firewall policy based on rules that are needed to target the agent hosting platform that you used.

  * **Agent Runtime** : Agents that run in Agent Runtime connect to the VPC network by using Private Service Connect network attachments. These attachments make the agent network interface appear within a subnet in the VPC network. Cloud NGFW network firewall policies are applied to the VPC network. The policies filter traffic based on the source IP addresses from the subnet that's dedicated to the Private Service Connect network attachment. For traffic matching, you can use source IP address and destination IP address ranges.
  * **Cloud Run** : Cloud Run services that use Direct VPC egress send traffic directly from instances that run within a subnet that's specified in the VPC network. Cloud NGFW network firewall policies apply to the subnet that's used by Cloud Run to filter traffic. For traffic matching, you can use source IP address and destination IP address ranges.
  * **GKE** : [VPC-native GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) give Pods IP addresses that are directly from the VPC network secondary IP address ranges. Network firewall policies can filter traffic based on IP address ranges for GKE nodes and Pods, and the policies can use [secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) and service accounts. Secure tags bind to the VM instances that act as GKE nodes. Firewall rules can then target or source traffic from nodes that have specific tags. Firewall rules can also target or source traffic from GKE nodes based on the service account identity that's associated with the node pool.



#### Default deny egress policy

Implementing a default deny strategy is a security best practice that adheres to the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). This strategy ensures that only network traffic that's explicitly allowed is permitted, while all other traffic is blocked by default. This implementation is achieved by structuring firewall rules with high-priority `ALLOW` rules for known, legitimate flows and a low-priority, catch-all `DENY` rule. All tiers of Cloud NGFW allow rules based on source and destination IP address ranges.

Firewall policy rules can effectively match source traffic from the Agent Runtime [network attachment](https://docs.cloud.google.com/vpc/docs/configure-security-network-attachments#producer-to-consumer-ingress) subnet and from the Cloud Run [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#restrict-access) subnet.

The following is an example default-deny egress policy:

  * **Create network firewall policy and rules** : Create a global or regional [firewall policy](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) and associate it with the VPC network. Create [firewall policy rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-egress-rule-target-vm) that target traffic in the egress direction (`--direction=EGRESS`) based on the source IP address ranges (`--src-ip-ranges=SRC_IP_RANGES`) and the destination IP address ranges (`--dest-ip-ranges=DEST_IP_RANGES`).
  * **Specific`ALLOW` rules**: Use lower priority numbers, for example 100-1000. These rules precisely allow the network traffic that's required for your AI agents to function. This traffic includes communication to other internal services, load balancers, required Google APIs, or legitimate external endpoints. Create a rule that matches source traffic from the Agent Runtime [network attachment](https://docs.cloud.google.com/vpc/docs/configure-security-network-attachments#producer-to-consumer-ingress) subnet or from the Cloud Run [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#restrict-access) subnet to the destinations that you want.
  * **General`DENY` rule**: To ensure that the rule is last in the evaluation order, use the highest priority number, for example 2147483647. This rule denies traffic to any destination (`--dest-ip-ranges=0.0.0.0/0`) that doesn't match any of the preceding `ALLOW` rules.



A default deny egress policy prevents AI agents from making any network connections that aren't explicitly authorized and it blocks potential data exfiltration or access to malicious sites. The policy confines the hosted agents to only communicate with approved endpoints, which is crucial for maintaining control over autonomous workloads.

#### Additional Cloud NGFW policy considerations

Beyond the default deny strategy that's available with all Cloud NGFW tiers, you can further harden your multi-agent AI network security by using paid-tier features:

  * **Cloud NGFW Standard features** : 
    * **FQDN Objects for dynamic endpoints** : AI agents often interact with external APIs, model endpoints, or data sources whose IP addresses might change. For consistent access to necessary services by domain name, use FQDN objects in `ALLOW` rules.
    * **Geolocation controls** : If AI agents have compliance requirements or if they shouldn't interact with services in specific geographic regions, use geolocation objects (`--src-region-codes=SRC_COUNTRY_CODES`) in your firewall rules to restrict traffic to or from those locations.
    * **Google Threat Intelligence** : Use Google Threat Intelligence in egress filters to automatically block agents from connecting to known malicious destinations, such as command and control (C2) servers, anonymizers like Tor, and malware distribution sites. The use of Google Threat Intelligence helps to contain the impact of a potentially compromised agent. We recommend that you include these destination filters in the higher priority number (lower evaluation order) `DENY` rules.
  * **Cloud NGFW Enterprise features** : 
    * **Layer 7 inspection** : For agents that handle sensitive data or that are exposed to higher risks, inspect packet payloads for threats like malware, spyware, and exploits that aren't analyzed by network layer firewall rules.
    * **TLS inspection** : To allow the inspection engine to analyze encrypted traffic, enable TLS inspection. The use of TLS inspection is crucial because most modern attacks and C2 communication are encrypted.



For additional implementation considerations or limitations that might be applicable to your environment, see these resources:

  * [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering#limitations)
  * [Intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention#ips-limitations)
  * [TLS inspection](https://docs.cloud.google.com/firewall/docs/about-tls-inspection#ips-limitations)



### IAP

[IAP](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto) secures ingress requests to GKE clusters by providing a central authentication and authorization layer for AI apps. IAP intercepts all of the HTTPS requests that are destined for the Gateway, and it checks the identity and permissions of the caller. IAP allows only authenticated and authorized requests to pass to the backend service workload. IAP on the Gateway load balancer only protects traffic that comes from outside the cluster. Communication within the cluster doesn't pass through IAP.

To access AI apps that are hosted on GKE and that are protected by IAP, principal user identities must be granted the IAP-secured Web App User IAM role (`roles/iap.httpsResourceAccessor`) on the IAP-protected backend service resource. We recommend that you configure a custom service account as the identity for deployed agents. Using a custom service account lets you assign permissions more precisely according to the principle of least privilege.

Only grant the IAP-secured Web App User IAM role directly to the service accounts of agents that are allowed to access other agents and tools that are hosted on the GKE [`BackendConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration) custom resource. To allow Gemini Enterprise apps access, grant permissions by binding the IAM role [Discovery Engine Service Account](https://docs.cloud.google.com/iam/docs/service-agents#discovery-engine-service-account) (`roles/discoveryengine.serviceAgent`) for your Gemini Enterprise project.

### VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) mitigates data exfiltration risks by strictly controlling access to Google APIs. We recommend that you deploy a single macro perimeter that includes all supported services. This approach provides the most robust defense against exfiltration. To ensure consistent policy enforcement for [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) architectures, it's crucial to include both the _host project_ and all of the associated _service projects_ within the same service perimeter.

**Note:** Implementation of a VPC Service Controls perimeter requires organizational planning, data gathering, and testing. This organizational effort includes documenting and interviewing workload teams to map specific access patterns and use cases. For information about how to implement a service perimeter on new or existing environments, see [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable).

To secure the interaction between Gemini Enterprise and Cloud Run across project boundaries, consider the following recommendations:

  * Deploy a single VPC Service Controls perimeter that encompasses both the Gemini Enterprise and Cloud Run projects.
  * Add all supported VPC Service Controls services to the list of restricted services. This approach helps to prevent unauthorized administrative changes.
  * Enforce internal [ingress](https://docs.cloud.google.com/run/docs/securing/ingress) and [authorization](https://docs.cloud.google.com/run/docs/securing/managing-access) settings to block all public internet access to your Cloud Run services.



Cloud Run services are secured by IAM. Callers must be authenticated and they must have the [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) IAM role (`roles/run.invoker`) on the target service. The role is checked by validating a token from the Authorization header. To successfully call the Cloud Run service, service accounts, such as those used by [ Gemini Enterprise](https://docs.cloud.google.com/iam/docs/service-agents#discovery-engine-service-account), must also be granted the Cloud Run Invoker role.

When Gemini Enterprise and Cloud Run are deployed in different projects, a VPC Service Controls perimeter is required in order to set Cloud Run ingress to Internal. Without this perimeter, cross-project calls from Gemini are treated as external traffic, which forces you to set Cloud Run ingress to All—which leaves the service exposed to the public internet.

  * Cloud Run ingress `all` is supported when both of these are _true_ : 
    * VPC Service Controls isn't enabled.
    * Cloud Run and Gemini Enterprise aren't in the same project.
  * Only Cloud Run ingress `internal` is supported for all other configurations.



#### Additional VPC Service Controls considerations

When Cloud Run is deployed inside a VPC Service Controls perimeter, we recommend that you implement the following policy guardrails to help ensure comprehensive protection:

  * [**Restrict allowed ingress settings**](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls#restrict-ingress): Prevent developers from accidentally deploying public-facing endpoints by setting the `run.allowedIngress` organization policy constraint. This constraint only applies to new deployments. Prior deployments might not be compliant. We recommend that you audit any existing Cloud Run services within the perimeter and re-deploy or update any that don't meet the required ingress and egress settings. 
    * To allow only internal requests, set the value to `internal`.
    * To allow requests through an external Application Load Balancer, set the value to `internal-and-cloud-load-balancing`.
  * [**Restrict allowed VPC egress settings**](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls#restrict-egress): To route all outbound requests through the VPC so that they can be inspected by perimeter firewall rules, set the `run.allowedVPCEgress` organization policy constraint value to `all-traffic`. This setting requires that every Cloud Run revision use Direct VPC egress or a Serverless VPC Access connector. This constraint only applies to new deployments. Prior deployments might not be compliant. We recommend that you audit any existing Cloud Run services within the perimeter and re-deploy or update any that don't meet the required ingress and egress settings.
  * **Colocate container images and services** : The Artifact Registry repository that contains your container images must reside within the same perimeter as the Cloud Run service. Cross-perimeter image pulling is automatically blocked unless you establish explicit ingress and egress rules.
  * **Manage access levels** : VPC Service Controls ingress policy rules and access levels that rely on IAM principal identities aren't supported for Cloud Run invocations. You must instead manage access with network-based criteria or device-based access levels.



### Model Armor

[Model Armor](https://docs.cloud.google.com/model-armor/overview) is an API-based service that provides enhanced security and safety for AI apps. AI agents interact with Model Armor by making calls to sanitize user prompts before they're sent to an LLM and to sanitize model responses before they're returned to the user. Model Armor actively screens LLM prompts and responses, which provides an important inspection point for detecting emerging risks and provides a control point for implementing responsible AI standards. We recommend that you use Model Armor to ensure compliance with data residency requirements and with data sovereignty legal regulations. To use Model Armor within a VPC Service Controls perimeter, you need to configure a Private Service Connect endpoint for the Model Armor regional endpoint within your VPC network.

Model Armor is a regional service that's accessed privately through regional [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints) in the VPC network. For example, the `us-central1` service is called by using the [regional endpoint](https://docs.cloud.google.com/storage/docs/regional-endpoints) `modelarmor.us-central1.rep.googleapis.com`. Regional endpoints [help to ensure data residency](https://docs.cloud.google.com/storage/docs/regional-endpoints#overview).

To enable access for agents, configure the following components in every region where the Model Armor service is required:

  1. Create or identify an [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918#section-3) subnet in the VPC network region where the Model Armor service resides.
  2. Create a [regional endpoint](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#create-regional-endpoint) in the RFC 1918 subnet.
  3. Create a [Cloud DNS private zone](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#configure-dns) and a record for the Model Armor regional endpoint hostname (for example, `modelarmor.us-central1.rep.googleapis.com`) that resolves to the IP address of the regional endpoint.
  4. For Agent Runtime interoperability, establish [DNS peering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#dns-peering) from Agent Runtime to the Cloud DNS private zone that's associated with your VPC network. When agents make requests to Model Armor, Cloud DNS resolves the hostname requests to the IP address of the Private Service Connect regional endpoint in the VPC network. This step isn't required for agents that are hosted in Cloud Run and GKE.



To integrate [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor) with Model Armor, create a Model Armor template in the same project as Gemini Enterprise. The location of the template and the Gemini Enterprise app must be the same.

For more information about enabling Model Armor, see these resources:

  * [Model Armor integration with Gemini Enterprise](https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration)
  * [Enable Model Armor in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor)
  * [Supported Google APIs in supported regions](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints)
  * [Model Armor integration with Google Cloud services](https://docs.cloud.google.com/model-armor/integrations)
  * [Data residency and endpoints](https://docs.cloud.google.com/model-armor/data-residency)



### Cloud Armor

[Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) is a distributed network security service that protects apps and services behind load balancers before requests reach backend service runtimes. AI agent workloads involve high volumes of inter-service communication that use A2A, MCP, and API calls. Cloud Armor protection provides additional layers of resilience in the security design with rate limiting, WAF screening, and custom rules that conform to expected agentic requests. By attaching Cloud Armor security policies to Application Load Balancer backend services, traffic can be filtered for malicious requests and policed with rate limits, and DDoS attacks can be mitigated.

Cloud Armor can be deployed in an agent network architecture in the following scenarios:

  * **Cloud Run with internal Application Load Balancer** : Protect agents and tools that run on Cloud Run by using an internal Application Load Balancer with serverless NEG backends. Apply [backend security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-2) to the serverless NEG to enforce WAF rules for internal traffic and rate limiting. To control agent communications, you can define additional custom rules based on IP addresses and headers.
  * **Gateway** : Protect agents and tools that run on GKE by using a Gateway resource definition for a global or regional external Application Load Balancer with zonal NEG backends. Use the [Kubernetes Gateway API](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor#armor-with-gke-gateway) to apply the `GCPBackendPolicy` resource with the defined Cloud Armor security policy. If you use a regional external Application Load Balancer, Cloud Armor supports [backend security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#backend-policies) with WAF rules, IP address and geo-based controls, and rate limiting. Global external Application Load Balancers support backend security policies and additional [edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#edge-policies) with [Google Cloud Armor Adaptive Protection](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview) and [ Google Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/detection).



### Secure Web Proxy

[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) is a regional managed service that's deployed within the VPC network to filter HTTP/S traffic that originates within the VPC network or within any connected networks. It acts as a centralized proxy and security enforcement point to provide granular control and visibility for outbound internet traffic. It also acts as an explicit proxy for internal service communications.

Secure Web Proxy supports three [deployment modes](https://docs.cloud.google.com/secure-web-proxy/docs/overview#deployment-modes): explicit proxy routing mode, Private Service Connect service attachment mode, and next hop mode. We recommend that you use Secure Web Proxy in [explicit proxy routing mode](https://docs.cloud.google.com/secure-web-proxy/docs/overview#explicit-proxy-routing), which is the focus of this document. In this mode, HTTP clients must be explicitly configured to point directly to the Secure Web Proxy IP address or hostname.

To deploy Secure Web Proxy in your VPC network, you must configure a frontend subnet and a [proxy-only subnet](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create_a_proxy_subnet). Secure Web Proxy is a fully managed service. When Secure Web Proxy is deployed, it automatically deploys and configures Cloud Router and Cloud NAT in your VPC network for specific integration with the proxy resource. This configuration mandates that any outbound requests must pass through Secure Web Proxy before they egress to the internet.

Using Secure Web Proxy as an explicit proxy supports agent requests that come from Agent Runtime Private Service Connect interfaces, Cloud Run Direct VPC egress, and VPC-native GKE clusters. When agents send requests to Secure Web Proxy by using the HTTP `CONNECT` method, TCP session traffic is tunneled to the proxy where security policy rules are applied. If the traffic is allowed, Secure Web Proxy sends the traffic to the controlled internet egress or to private network destinations that are routable by the VPC network.

#### Explicit proxy routing

Agent Runtime egress requires that you use an explicit proxy configuration in order for agents to reach internet destinations or [non-routable IP address ranges](https://docs.cloud.google.com/agent-builder/agent-engine/private-service-connect-interface#subnetwork-ip-range-requirements) in the VPC network. For Agent Runtime interoperability, we recommend that you configure the Secure Web Proxy resource with an RFC 1918 IP address from a frontend subnet in the VPC network. With this configuration, Secure Web Proxy becomes directly reachable from Agent Runtime. It can then proxy any connections to non-routable IP address destinations that are in the VPC network or in connected networks.

To support agent hosting platform use of Secure Web Proxy in explicit routing mode, configure these networking resources:

  1. Create or identify an [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918#section-3) subnet in the VPC network to host the Secure Web Proxy resource.
  2. Create a Cloud DNS record for the Secure Web Proxy hostname (for example, `swp.example.com`) that resolves to the IP address of the Secure Web Proxy resource.
  3. For Agent Runtime interoperability, establish [DNS peering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#dns-peering) from Agent Runtime to the Cloud DNS private zone that's associated with your VPC network. When agents make requests to Secure Web Proxy, Cloud DNS resolves the hostname requests to the IP address of the Secure Web Proxy resource in the VPC network. This step isn't required for agents that are hosted in Cloud Run and GKE.



#### Agent proxy settings

The standard way to configure agent apps to use an HTTP(S) proxy is by setting these environment variables:

  * `HTTP_PROXY`: The URL of the explicit proxy server for HTTP traffic (for example, [`http://swp.example.com:8888`](http://swp.example.com:8888)). This setup uses the HTTP `CONNECT` method from the client to the proxy. Even though HTTP is specified, TLS encryption is maintained end-to-end through the proxy from the agent runtime to the target endpoint.
  * `HTTPS_PROXY`: The URL of the explicit proxy server for HTTPS traffic (for example, [`https://swp.example.com:8888`](https://swp.example.com:8888)). Like the `HTTP_PROXY` setting, the `HTTPS_PROXY` setting uses TLS by default. However, you can provide an additional layer of encryption by enabling your own TLS encryption on top of the default TLS. For more information, see Certificate Authority Service.
  * `NO_PROXY`: A comma-separated list of hostnames or IP addresses that shouldn't go through the proxy. For example, if you add `metadata.google.internal` and `169.254.169.254` to the `NO_PROXY` list, then workloads can directly access the metadata service for authentication and authorization to Google APIs and services.



When you use the `env_vars` argument to set variables during deployment, they become available within the agent runtime environment (for example, when you use `os.environ` in Python). Most standard HTTP client libraries automatically discover and use these environment variables to route traffic through the specified proxy. This approach is common for Python apps and HTTP client libraries like [`requests`](https://requests.readthedocs.io/en/latest/user/advanced/#proxies). When you deploy agents, define environment variables for using Secure Web Proxy for any private domains that the agents need to reach. Ensure that any private domain destinations are also included in Cloud DNS.

The following example shows a Agent Runtime proxy deployment from an [agent object](https://docs.cloud.google.com/agent-builder/agent-engine/deploy#create-agent-engine):
    
    
    ## specify environment variables (dictionary)
    env_vars = {
        "OTHER_VARIABLE": "OTHER_VALUE",
        "HTTP_PROXY": "http://swp.example.com:8888",
        "HTTPS_PROXY": "http://swp.example.com:8888",
        "NO_PROXY": "localhost,127.0.0.1,metadata.google.internal,169.254.169.254,.googleapis.com,run.app,.gcr.io,.pkg.dev,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.internal"
    }
    
    remote_agent = aiplatform.agent_engines.create(
        agent=local_agent,
        config={
            "display_name": "Example agent using proxy",
            "env_vars": env_vars,
            ## ... other configs
        },
    )
    

Cloud Run supports setting environment variables at the service revision level. This approach overrides any environment variables with the same name that were set within the container image. This approach is useful for setting operational parameters like proxy variables when the service instances start.

The following example shows the command to set the environment variables when you [deploy](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables#setting) a Cloud Run service:
    
    
    gcloud run deploy SERVICE_NAME \
    --image=IMAGE_URL \
    --set-env-vars="HTTP_PROXY=http://swp.example.com:8888,HTTPS_PROXY=http://swp.example.com:8888,NO_PROXY=localhost,127.0.0.1,metadata.google.internal,169.254.169.254,.googleapis.com,run.app,.gcr.io,.pkg.dev,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.internal"
    

To implement an explicit proxy configuration in GKE pods, define a `ConfigMap` resource that specifies the proxy variables:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: agent-proxy-config
      namespace: ai-apps
    data:
      HTTP_PROXY: "http://swp.example.com:8888"
      HTTPS_PROXY: "http://swp.example.com:8888"
    
      NO_PROXY: "localhost,127.0.0.1,metadata.google.internal,169.254.169.254,.googleapis.com,run.app,.gcr.io,.pkg.dev,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.internal"
    

To apply the `ConfigMap` keys to the Pods, use the `envFrom` field in the container manifest. This specification injects the environment variables into the container at runtime.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: subagent-app
    spec:
      template:
        spec:
          containers:
          -   name: my-container
            image: my-agent-app:latest
            envFrom:
            -   configMapRef:
                name: agent-proxy-config
    

### CA Service

[CA Service (CA Service)](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) is required when Secure Web Proxy or Cloud NGFW is configured for TLS inspection. When TLS inspection is enabled and a workload's destination uses TLS, CA Service creates and signs a certificate for that destination. When the encrypted traffic for the real destination arrives at Secure Web Proxy or Cloud NGFW, it decrypts the packet, inspects it, and then enforces policies. If the policies allow the packet, the service re-encrypts the packet for the final destination. You can also use CA Service to provide certificates to other Google managed services.

CA Service is a managed service. After CA Service is configured, it handles leaf certificate signing until the root CA certificate expires. Root CA certificates must be updated to ensure that they don't expire.

CA Service supports these capabilities to enable traffic inspection and certificate management at scale in a multi-agent AI architecture:

  * **TLS inspection** : Use of a private CA is required for full TLS inspection. To fully decrypt and analyze HTTPS payloads, the intermediary proxy device (Secure Web Proxy or Cloud NGFW) needs to terminate the TLS session with the client. The proxy must present a valid certificate that the client accepts as trusted for the domain that's requested.

CA Service can dynamically generate and sign a site-specific impersonation certificate for the site that's requested. When the client has the private root CA certificate installed in its trust store, it accepts this dynamically created certificate as valid. The client trusts the certificate that's sent by the proxy, so it sends the request. The proxy terminates the TLS session, decrypts the packet, inspects the contents, and then enforces policies.

  * **Certificate distribution** : Internal client resources like AI agents that run on Agent Runtime, Cloud Run, or GKE need the private root CA certificate added to their local trust stores. By storing the root CA certificate public key in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), AI agents can pull the certificate on startup and add it to their system trust store.

Internal server resources like internal Application Load Balancers need certificates that are issued by the private CA to act as trusted server endpoints and terminate client TLS sessions. Application Load Balancers integrate with Certificate Manager [issuance configurations](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs) to automate the CA Service signing the certificate request and deploying it to the load balancer.




For more information about certificate operations, see these resources:

  * Cloud Run: [Configure secrets for services](https://docs.cloud.google.com/run/docs/configuring/services/secrets)
  * GKE: [Access private registries with private CA certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates)
  * Secure Web Proxy: [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection)
  * Cloud NGFW: [TLS inspection overview](https://docs.cloud.google.com/firewall/docs/about-tls-inspection)



### A2A connection security

Root agents communicate with a diverse array of subagents and MCP servers that are deployed across various runtime hosting platforms. Each environment introduces unique networking and security requirements that must be abstracted by the A2A or MCP layer.

The following diagram shows the components and possible connection paths that are supported by this design guide:

![Agent2Agent \(A2A\) connectivity patterns between different hosting platforms including GKE, Cloud Run, and Agent Runtime, and connections to MCP servers and the internet.](https://docs.cloud.google.com/static/architecture/images/multi-agent-private-networking-patterns-a2a-connectivity.svg)![](https://docs.cloud.google.com/static/architecture/images/multi-agent-private-networking-patterns-a2a-connectivity.svg)

The preceding diagram summarizes these connection possibilities:

  * Users interact with the agentic system through a Gemini Enterprise app.
  * The Gemini Enterprise app uses Google infrastructure to connect to a root agent that runs in GKE, Cloud Run, or Agent Runtime.
  * The Gemini Enterprise app and the root agents use Google infrastructure to connect to Model Armor and the Gemini LLM on Agent Platform.
  * The root agents can use Google infrastructure to connect to subagents that run in Cloud Run or Agent Runtime.
  * The root agents can use private IP addresses to connect to subagents that run in Agent Runtime, Cloud Run, and GKE. These connections must be routed through a VPC network.
  * Both root agents and subagents can connect to MCP servers that run on Cloud Run or GKE. Agents that connect to the MCP servers can use either Google infrastructure or a VPC network. The MCP servers provide access to tools that are hosted in Google Cloud, on-premises, in another cloud, or on the internet.
  * Services that are hosted on the internet can be reached directly through Secure Web Proxy.



The following sections provide resources for the runtime data paths and security controls that are required for secure A2A interactions. This information serves as the architectural standard for establishing private connectivity and implementing the multi-layered defenses that are necessary to protect the end-to-end data path between agents.

#### GKE source agent

The following table provides resources to help you protect traffic when GKE is the source agent. This traffic travels through the VPC network that hosts the GKE cluster.

Destination agent (data path) | Security control  
---|---  
Agent Runtime (internal) | 

  * VPC Service Controls
  * Model Armor

  
Cloud Run (internal) | 

  * VPC Service Controls
  * Model Armor

  
Cloud Run (Private Service Connect for Google APIs) | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW

  
Cloud Run access (serverless NEG) | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Internal Application Load Balancer certificate authorization](https://docs.cloud.google.com/load-balancing/docs/l7-internal#ssl_certificates)
  * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)

  
GKE | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Internal Application Load Balancer certificate authorization](https://docs.cloud.google.com/load-balancing/docs/l7-internal#ssl_certificates)
  * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)

  
Internet through VPC network | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview)

  
  
#### Agent Runtime (internal) source agent

The following table provides resources to help you protect traffic when Agent Runtime is the source agent and the traffic travels directly over Google infrastructure. In these paths, no VPC network is involved.

Destination agent (data path) | Security control  
---|---  
Agent Runtime (internal) | 

  * VPC Service Controls

  
Cloud Run (internal) | 

  * VPC Service Controls

  
  
#### Agent Runtime (Private Service Connect interface) source agent

The following table provides resources to help you protect traffic when Agent Runtime is the source agent and the traffic uses a Private Service Connect interface to travel through a VPC network.

Destination agent (data path) | Security control  
---|---  
Cloud Run (Private Service Connect GoogleAPIs) | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW

  
Cloud Run access (serverless NEG) | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Internal Application Load Balancer certificate authorization](https://docs.cloud.google.com/load-balancing/docs/l7-internal#ssl_certificates)
  * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)

  
GKE | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Internal Application Load Balancer certificate authorization](https://docs.cloud.google.com/load-balancing/docs/l7-internal#ssl_certificates)
  * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)

  
Internet through VPC network | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview)

  
  
#### Cloud Run (internal) source agent

The following table provides resources to help you protect traffic when Cloud Run is the source agent and the traffic travels directly over Google infrastructure. In these paths, no VPC network is involved.

Destination agent (data path) | Security control  
---|---  
Agent Runtime (internal) | 

  * VPC Service Controls

  
Cloud Run (internal) | 

  * VPC Service Controls

  
  
#### Cloud Run (Direct VPC egress) source agent

The following table provides resources to help you protect traffic when Cloud Run is the source agent and the traffic uses Direct VPC egress to travel through a VPC network.

Destination agent (data path) | Security control  
---|---  
Cloud Run (Private Service Connect for Google APIs) | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW

  
Cloud Run access (serverless NEG) | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Internal Application Load Balancer certificate authorization](https://docs.cloud.google.com/load-balancing/docs/l7-internal#ssl_certificates)
  * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)

  
GKE | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Internal Application Load Balancer certificate authorization](https://docs.cloud.google.com/load-balancing/docs/l7-internal#ssl_certificates)
  * [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)

  
Internet through VPC network | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW
  * [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview)

  
Agent Runtime Private Service Connect for Google APIs  | 

  * VPC Service Controls
  * Model Armor
  * Cloud NGFW

  
  
### MCP connection security

The following list outlines the hosting platforms and defense-in-depth controls that are involved in securing the data path between agent runtimes and MCP servers. For source agents in Agent Runtime, in Cloud Run, or in GKE, use the following security controls depending on the destination MCP server:

  * **Internet** : 
    * VPC Service Controls
    * Model Armor
    * Cloud NGFW
    * Secure Web Proxy
  * **Google MCP** : 
    * VPC Service Controls
    * Model Armor



## What's next

  * Read about how to build your agentic system: 
    * [Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components). 
      * [Choose a design pattern for your agentic AI system](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system).
      * [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * Deepak Michael | Networking Specialist Customer Engineer
  * [Michael Larson](https://www.linkedin.com/in/michaellarson) | Customer Engineer, Networking Specialist
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking



Other contributors: 

  * [Christine Sizemore](https://www.linkedin.com/in/christine-sizemore) | Cloud Security Architect
  * [Aspen Sherrill](https://www.linkedin.com/in/aspensherrill/) | Cloud Security Architect
  * [Assaf Namer](https://www.linkedin.com/in/assaf-namer-0677644) | Principal Cloud Security Architect
  * [David Tu](https://www.linkedin.com/in/davidatu) | Customer Engineer
  * [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
