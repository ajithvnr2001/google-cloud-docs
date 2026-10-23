---
url: https://docs.cloud.google.com/looker/docs/looker-core-networking-options/
title: Looker (Google Cloud core) networking options \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:45:30.392964+00:00
---

# Looker (Google Cloud core) networking options  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-networking-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker (Google Cloud core) networking options Stay organized with collections  Save and categorize content based on your preferences. 

You can choose from several network configurations for a Looker (Google Cloud core) instance to meet your organization's security, architectural, and data access requirements. You must select a network configuration when you create an instance. Some network configurations can be modified after creation, while others cannot. Each configuration option has different implications for setup complexity, ongoing maintenance, and how your instance connects to external resources and data sources.

## Overview

The following network configuration options for Looker (Google Cloud core) are available:

  * **Use public secure connections**: An instance that uses an external internet accessible IP address.
  * **Use private connections**: Private connections use private networks for access to and from Looker (Google Cloud core) instances. There are two options for using private networks:

    * **Private Service Connect**: An instance enabled for Private Service Connect uses an internal, Google-hosted Virtual Private Cloud (VPC) IP address and uses [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to connect privately to Google and third-party services.
    * **private services access**: An instance enabled for private services access uses an internal, Google-hosted Virtual Private Cloud (VPC) IP address and uses [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) to connect privately to Google and third-party services.
  * **Use hybrid connections**: An instance that supports a public IP address for ingress and an internal, Google-hosted VPC IP address and [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) or [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) for egress.




When considering a network configuration for your Looker (Google Cloud core) instance, the following information may be helpful as you make your decision:

  * Network configuration must be set when the instance is created. An instance configured for public secure connections can't be changed after instance creation. An instance configured for [hybrid connections can by changed to private connections](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings), or an instance with private connections can be changed to a hybrid connections configuration after the instance is created.
  * Feature availability varies by network option. See the [Feature availability in Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_connection_type) documentation page for more information.
  * All connections to BigQuery are through Google's private network, regardless of the network configuration.
  * If a third-party identity provider is configured for single-sign on, the user's browser communicates to the identity provider and is then redirected to the Looker (Google Cloud core) instance. As long as the redirect URL is accessible over the user's network, third-party identity providers work for all networking configurations.



Also see the table in the How to choose a networking option section of this documentation page for more information about how to decide on the right networking configuration for your team.

## Public secure connections

Looker (Google Cloud core) deployed as a public secure connection instance is accessible from an external internet-accessible IP address. In this configuration, [inbound](https://docs.cloud.google.com/looker/docs/glossary#northbound-traffic) (northbound) traffic to Looker (Google Cloud core) is supported in addition to Looker (Google Cloud core) [outbound](https://docs.cloud.google.com/looker/docs/glossary#southbound-traffic) (southbound) access to internet endpoints. This configuration is similar to the configuration of a Looker (original) instance that is hosted by Looker.

![Traffic to and from a public secure connection instance moves over the public internet.](https://docs.cloud.google.com/static/looker/docs/images/public-network-connection.png)

Public secure connections allow only HTTPS traffic into Looker (Google Cloud core). Google auto-provisions an SSL certificate when the CNAME is updated and Google can locate the DIG records. This certificate is automatically rotated every four months. To securely connect to external databases from a public secure connection Looker (Google Cloud core) instance, you can set up an encrypted [SSL connection](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_2_ssl_encryption).

Public secure connections configurations are straightforward to set up and connect to and don't require advanced network configuration or expertise.

To create a Looker (Google Cloud core) public secure connection instance, see the [Create a public secure connection Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) documentation page.

After a public secure connection instance is created, the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) for the instance in the Google Cloud console will show the **Public IP enabled** field as **true** and the **Private IP Enabled** and **PSC Enabled** fields as **false**.

## Private connections

A Looker (Google Cloud core) instance configured to use private connections uses an internal, Google-hosted [VPC](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) IP address. You can use this address to communicate with other resources that can access the VPC. Private connections make services reachable without going through the public internet or using external IP addresses. Because they don't traverse the internet, private connections typically provide lower latency and limited attack vectors.

In a private connections configuration, internal certificates are completely managed by Google and aren't exposed to anyone. If you are provisioning a private connections instance with custom certificates, you don't need to manage the internal private certificates. Instead, use your own custom certificate, and ensure that the rotation of that certificate is maintained.

In a private connections configuration, Looker (Google Cloud core) doesn't have a public URL. You control all inbound (northbound) traffic, and all outbound (southbound) traffic will be routed through your VPC.

![](https://docs.cloud.google.com/static/looker/docs/images/private-network-connection.png)

If your instance uses only a private connection, additional configuration is necessary to set up a custom domain and user access to the instance; [use some Looker (Google Cloud core) features](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_connection_type); or connect to external resources, such as Git providers. In-house networking expertise is helpful to plan and execute this configuration.

Looker (Google Cloud core) supports the following two options for private connections:

  * Private services access
  * Private Service Connect



The use of private services access or Private Service Connect must be decided at the time of instance creation.

### Private Service Connect

**Action needed for Private Service Connect instances**

The backend infrastructure for Looker (Google Cloud core) private connections has been upgraded to support new features like global access and Google-managed certificates. If your instance uses Private Service Connect, you can update your Private Service Connect endpoint or backend configuration to point to a new service attachment URI. See the [Migrating Private Service Connect connections to the new service attachment URI](https://docs.cloud.google.com/looker/docs/looker-core-psc-migration) documentation page for detailed instructions.

The use of [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) with Looker (Google Cloud core) must be set at the time of instance creation.

To create a Looker (Google Cloud core) Private Service Connect instance, see the [Create a Looker (Google Cloud core) Private Service Connect instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc) documentation page.

After a Private Service Connect instance is created, the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) for the instance in the Google Cloud console will show **true** for the **PSC Enabled** field.

When used with Looker (Google Cloud core), Private Service Connect differs from private services access in the following ways:

  * Endpoints and backends support public or private access methods.
  * Looker (Google Cloud core) can connect to other Google services, such as Cloud SQL, that are accessible through Private Service Connect.
  * There is no need to allocate large IP blocks.
  * Direct connections allow for transitive communication.
  * There is no need to share a network with other services.
  * Supports [multi-tenancy](https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments#multi-tenant-services).
  * Supports [global access](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#using_global_access).
  * Supports [Google-managed certificates](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#using_google-managed_certificates_with_a_custom_domain) for custom domains.



In-house networking expertise is helpful for planning and executing Private Service Connect configurations.

To learn more about Private Service Connect instances, see the [Use Private Service Connect with Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview) documentation page.

#### Accessing a Looker (Google Cloud core) instance with Private Service Connect

Private Service Connect [backends](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#backends) can be used to [privately access Looker (Google Cloud core) Private Service Connect instances](https://docs.cloud.google.com/looker/docs/looker-core-psc-access) or to [access Looker (Google Cloud core) over the public internet](https://docs.cloud.google.com/looker/docs/looker-core-psc-access-public).

#### Controlled native egress

When you use the [**Global FQDN** setting](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#global-fqdn) or use the [**Enable connection to Looker Marketplace** setting](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#connect-to-marketplace), Looker (Google Cloud core) uses controlled native egress. This built-in, managed solution simplifies internet (HTTPS) egress connectivity for Private Service Connect-based deployments. Controlled native egress removes the need to create a producer service for internet egress in your Virtual Private Cloud (VPC). Controlled native egress routes internet traffic through the Google-managed Looker VPC, which provides several key benefits, primarily focusing on simplifying configuration and enhancing usability for customers with secure environments.

The following are the key benefits of controlled native egress:

  * **Eases configuration complexity** : Configuration is simplified by removing prerequisites such as deploying load balancers and NAT gateways, or allocating subnet space for a Private Service Connect producer service. Controlled native egress is managed by Looker (Google Cloud core) to facilitate HTTPS internet egress.
  * **Eliminates complicated workarounds** : Offers a simplified way to connect to services like Marketplace without deploying network infrastructure.
  * **Supports key external services** : Enables configurable native egress for customer-specified fully qualified domain names (FQDNs), such as Looker managed Marketplace, github.com, and gitlab.com.



When choosing controlled native egress, consider the following:

  * Controlled native egress supports HTTPS internet egress for public endpoints.
  * You can identify the IP addresses that Looker (Google Cloud core) uses for controlled native egress by navigating to the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) of the **Instances** page for your Looker (Google Cloud core) instance in the Google Cloud console. The IP addresses that are used for internet egress traffic appear in the **Egress IPs** field in the **Controlled Egress Configuration** section. The IP addresses are unique to your Looker (Google Cloud core) instance. These IP addresses are allocated using the Secure Web Proxy, and they are dynamic and may change without warning.

**Note:** We recommend using controlled native egress only with remote endpoints that allow all incoming network traffic without IP-based restrictions.
  * Traffic to Google APIs that are supported by [the restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services) is automatically routed through controlled native egress. For Google APIs that are not supported by the restricted VIP, you can add a [**Global FQDN** egress rule](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#global-fqdn) to allow traffic to that API using controlled native egress.

  * If your Looker (Google Cloud core) instance is in a VPC Service Controls perimeter, VPC Service Controls will block controlled native egress traffic to Google APIs [not supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#supported_products). Those services must be [published as producer services](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#set_up_for_external_services) and traffic can be allowed through Private Service Connect by adding the service to the [**Local FQDN**](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#update-local-fqdn-setting) allowlist. An example of such a service is the Google Maps API.

  * The [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub#the_looker_action_hub) isn't supported by controlled native egress.

  * Oubound connections to non-Google services can use controlled native egress by adding them to the [**Global FQDN** allowlist](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#global-fqdn).

  * If you encounter connection timeouts or authentication failures with external services when using controlled native egress, see [Troubleshooting Looker (Google Cloud core) networking issues](https://docs.cloud.google.com/looker/docs/looker-core-networking-troubleshooting).




For a comparison between outbound connections that use controlled native egress or Private Service Connect published services, see the Comparison of controlled native egress versus Private Service Connect connections section.

#### Connecting to external services using Private Service Connect

Looker (Google Cloud core) Private Service Connect instances can use endpoints to connect to Google Cloud or external resources. If a resource is external, a network endpoint group (NEG) and load balancer need to be set up as well. Additionally, each outbound connection to a unique service requires that the service be [published using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#set_up_for_external_services). On the Looker (Google Cloud core) end, each unique egress connection must be [created through the **Local FQDN** setting](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#update-local-fqdn-setting) and [maintained](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#include_all_connections_that_should_be_enabled) for each service that you want to connect to.

![An overview of inbound and outbound network topologies for Private Service Connect.](https://docs.cloud.google.com/static/looker/docs/images/psc-connections-042125.png)

For an example of connecting to an external service using Private Service Connect, see the [Looker PSC Southbound HTTPS Internet NEG codelab](https://codelabs.developers.google.com/looker-psc-internet-neg-https).

For a comparison of outbound connection types for Private Service Connect, see the Controlled native egress versus Private Service Connect connections section.

#### Controlled native egress versus Private Service Connect connections

The following table compares key features of connecting to external services with controlled native egress or through southbound Private Service Connect connections.

Feature | Controlled native egress | Southbound connections using Private Service Connect  
---|---|---  
**Primary goal** | Simplify configuration for accessing specific, common public external services (for example, Marketplace, GitHub). | Enables Looker (Google Cloud core) to act as a service consumer to establish communication with services in your VPC, your multi-cloud network, or the internet.  
**Management and complexity** | A managed, built-in Looker (Google Cloud core) Private Service Connect feature, designed to eliminate complex network knowledge requirements. | Requires manual, detailed configuration by the customer to set up southbound connections.  
**Targeted services** | Designed for HTTPS internet egress services (for example, Marketplace, github.com, gitlab.com) | Supports a wide variety of outbound services (both private and public), including Google-managed databases (for example, Cloud SQL), on-premises databases, and self-managed services.  
  
### Private services access

The use of [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) private connections with Looker (Google Cloud core) must be set at the time of instance creation. Looker (Google Cloud core) instances can optionally include a public secure connection with their private (private services access) connection. After creation of an instance that uses private services access, you can add or remove a private connection to that instance.

To create a private (private services access) connection, you must allocate a `/22` CIDR range in your VPC to Looker (Google Cloud core).

To set up user access to an instance that uses only a private (private services access) connection, you must set up a custom domain and configure access to the domain [depending on your organization's needs](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-private-ip-overview). To connect to external resources, you will need to [perform additional configuration](https://docs.cloud.google.com/looker/docs/looker-core-private-ip-config). In-house networking expertise is helpful to plan and execute this configuration.

To create a Looker (Google Cloud core) private services access instance, see the [Create a private connections instance](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip) documentation page.

After a private services access instance is created, the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) for the instance in the Google Cloud console will show the **Private IP Enabled** field as **true**.

## Hybrid connections configuration

Looker (Google Cloud core) instances that use private services access or Private Service Connect for their private connection support a hybrid connections configuration.

A Looker (Google Cloud core) instance that uses private services access and that has a hybrid connection has a public URL, and all incoming (northbound) traffic will go through the public connection using HTTPS. Outgoing (southbound) traffic is routed through your VPC, which can be configured to allow only private connection traffic, using HTTPS or encryption. All traffic in transit is encrypted.

A Looker (Google Cloud core) instance that is enabled for Private Service Connect uses a customer-defined IP address accessible in a VPC for ingress. Communication to the VPC and on-premises or multi-cloud workloads use service attachments that you deploy for egress traffic.

![In a hybrid connections configuration, inbound traffic goes through a public connection, and outbound traffic goes through a private connection.](https://docs.cloud.google.com/static/looker/docs/images/public-private-network-connection.svg)

After an instance using a hybrid connections configuration is created, the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) for the instance in the Google Cloud console will show **true** for the **Public IP enabled** field and **true** for either the **Private IP Enabled** or the **PSC Enabled** field.

## How to choose a networking option

The following table shows the feature availability for different networking options.

Network requirements  
---  
**Feature** | **Public secure connections** | **Hybrid connections (PSA)** | **Private connections (PSA)** | **Hybrid connections (PSC)** | **Private connections (PSC)**  
Requires IP range allocation for instance creation  | No  | Yes (`/22` per instance, per region)  | Yes (`/22` per instance, per region)  | No  | No   
Google Cloud Armor  | Yes. Looker (Google Cloud core) uses default Google Cloud Armor rules, which are managed by Google. These rules are not configurable.  | Yes. Looker (Google Cloud core) uses default Google Cloud Armor rules, which are managed by Google. These rules are not configurable.  | No  | Yes. Looker (Google Cloud core) uses default Google Cloud Armor rules, which are managed by Google. These rules are not configurable.  | Supported with customer-managed regional external Application Load Balancer, Private Service Connect backend, and customer-managed Google Cloud Armor   
Custom domain  | Yes  | Supported as a public URL  | Yes  | Supported as a public URL  | Yes   
Inbound access  
**Feature** | **Public secure connections** | **Hybrid connections (PSA)** | **Private connections (PSA)** | **Hybrid connections (PSC)** | **Private connections (PSC)**  
Public internet  | Yes  | Yes  | No  | Supported with Google-managed regional external Application Load Balancer | Supported with customer-managed regional external Application Load Balancer, Private Service Connect backend, and custom domain  
VPC peering (private services access)  | No  | Yes  | Yes  | No  | No   
PSC-based routing  | No  | No  | No  |  Supported with the following: 

  * Regional external Application Load Balancer and Private Service Connect backend
  * Regional internal Application Load Balancer and Private Service Connect backend

Global access is supported (with the [enhanced service attachment URI](https://docs.cloud.google.com/looker/docs/looker-core-psc-migration)), letting you access your instance from a different region than where the instance is located.  
Hybrid networking  | No  | Yes  | Yes  | Yes  | Yes   
Outbound access  
**Feature** | **Public secure connections** | **Hybrid connections (PSA)** | **Private connections (PSA)** | **Hybrid connections (PSC)** | **Private connections (PSC)**  
Internet  | Yes  | No  | No  | Supported with regional TCP proxy internal load balancer, internet NEG, and Cloud NAT gateway.   
VPC peering (private services access)  | No  | Yes  | Yes  | No  | No   
Private Service Connect-based routing  | No  | No  | No  | Supported with regional TCP proxy internal load balancer and hybrid NEG  
Hybrid networking (multi-cloud and on-premises)  | No  | Yes  | Yes  | Supported with regional TCP proxy internal load balancer, hybrid NEG, and [Google Cloud networking products](https://docs.cloud.google.com/network-connectivity/docs/concepts#connect-to-google-cloud)  
Application  
**Feature** | **Public secure connections** | **Hybrid connections (PSA)** | **Private connections (PSA)** | **Hybrid connections (PSC)** | **Private connections (PSC)**  
GitHub  | Yes  | Supported with TCP proxy internal load balancer and internet NEG  | Yes. For an example, see the [Looker PSC Southbound HTTPS Internet NEG codelab](https://codelabs.developers.google.com/looker-psc-internet-neg-https).   
GitHub Enterprise  | No  | Yes  | Yes  | Yes  | Yes   
Cloud SQL  | Yes  | Supported with Cloud SQL deployed in the same VPC as Looker (Google Cloud core)  | Yes  | Yes  | Yes   
BigQuery  | Yes  | Yes  | Yes  | Yes  | Yes   
Embed  | Yes  | Yes  | Yes  | Yes  | Yes   
Marketplace  | Yes  | No  | No  | Yes  | Yes   
Looker Action Hub  | Yes  | Yes  | No  | Yes  | No   
Looker-managed MCP server  | Yes  | Yes  | Yes  | Yes  | Yes   
Connected Sheets  | Yes  | Yes  | Yes  | Yes  | Yes   
SMTP  | Yes  | Yes  | Yes  | Yes. Requires outbound connectivity.   
Benefits  
**Feature** | **Public secure connections** | **Hybrid connections (PSA)** | **Private connections (PSA)** | **Hybrid connections (PSC)** | **Private connections (PSC)**  
Benefits  | 

  * A publicly accessible URL means that it is straightforward to connect to Looker (Google Cloud core) from other services that need to access the instance or redirect to Looker.
  * No need for advanced network configuration.

| 
* Access Looker (Google Cloud core) through a public URL
* Outbound access to multi-cloud environments is achieved based on IP reachability
| 

  * Private instance for inbound and outbound access
  * Outbound access to multi-cloud environments is achieved based on IP reachability

| 

  * No shared constraints and no IP coordination required between the consumer and producer
  * Subnet allocation for Looker (Google Cloud core) instantiation is not required
  * Explicit access to Looker (Google Cloud core) and endpoints
  * Supports Google-managed external load balancer.

| 

  * No shared constraints and no IP coordination required between the consumer and producer
  * Subnet allocation for Looker (Google Cloud core) instantiation is not required
  * Explicit access to Looker (Google Cloud core) and endpoints
  * Supports public and private access to Looker (Google Cloud core) with the use of Private Service Connect backends

  
Considerations  
**Feature** | **Public secure connections** | **Hybrid connections (PSA)** | **Private connections (PSA)** | **Hybrid connections (PSC)** | **Private connections (PSC)**  
Considerations  | If you want a custom URL, you have to configure a fully qualified domain name (for example, `looker.examplepetstore.com`). You cannot have a custom URL like `examplepetstore.looker.com`.  | 

  * Outbound access to on-premises and multi-cloud environment requires firewall updates
  * Deploying Looker (Google Cloud core) in a hub-and-spoke VPC architecture with VPC peering results in non-transitive routing to Looker if accessed over hybrid networking from on-premises or multi-cloud networks
  * Additional infrastructure to connect to public Git (proxy VM, internet NEG, and load balancer)

| 

  * Outbound access to on-premises and multi-cloud environment requires firewall updates
  * Deploying Looker (Google Cloud core) in a hub-and-spoke VPC architecture with VPC peering results in non-transitive routing to Looker if accessed over hybrid networking from on-premises or multi-cloud networks
  * Additional infrastructure to connect to public Git (proxy VM, internet NEG, and load balancer)

| 

  * Public access to Looker (Google Cloud core) is managed by Google.
  * Each outbound endpoint (IP address) requires a Private Service Connect published service.

| 

  * Public access to Looker (Google Cloud core) requires integration with an external Application Load Balancer and Private Service Connect backend
  * Each outbound endpoint (IP address) requires a Private Service Connect published service

  
  
## Changing networking configuration

After you create a Looker (Google Cloud core) instance, you might need to change its networking configuration to accommodate evolving security or infrastructure requirements. Depending on the current and target networking configurations, you can either update the settings directly on your existing instance or create a new instance with the updated configuration and migrate your data:

  * **Direct configuration change:** You can switch between private connections and hybrid connections by [editing the instance configuration](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings) in the Google Cloud console.
  * **Migration required:** You cannot directly switch an existing instance to or from public secure connections, or change the underlying private connectivity mechanism between private services access (PSA) and Private Service Connect (PSC). In these cases, you must create a new Looker (Google Cloud core) instance with the target networking setup and then [export data from the original instance and import it into the new instance](https://docs.cloud.google.com/looker/docs/looker-core-import-export).



The following table summarizes the requirements for switching between networking configurations:

Current network configuration | Target network configuration | How to change  
---|---|---  
Private connections | Hybrid connections | [Edit the instance configuration](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings) in the Google Cloud console.  
Hybrid connections | Private connections | [Edit the instance configuration](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings) in the Google Cloud console.  
Public secure connections | Private connections | Create a new instance with private connections, and then [export and import data](https://docs.cloud.google.com/looker/docs/looker-core-import-export).  
Public secure connections | Hybrid connections | Create a new instance with hybrid connections, and then [export and import data](https://docs.cloud.google.com/looker/docs/looker-core-import-export).  
Private connections | Public secure connections | Create a new instance with public secure connections, and then [export and import data](https://docs.cloud.google.com/looker/docs/looker-core-import-export).  
Hybrid connections | Public secure connections | Create a new instance with public secure connections, and then [export and import data](https://docs.cloud.google.com/looker/docs/looker-core-import-export).  
  
## What's next

  * [Understand the right network configuration for Looker Core](https://docs.cloud.google.com/looker/docs/best-practices/network-configuration-options)
  * [Create a public secure connections Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create)
  * [Use Private Service Connect with Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview)
  * [Create a Looker (Google Cloud core) private connections Private Service Connect instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc)
  * [Follow a tutorial on how to perform a outbound HTTPS connection to GitHub from a PSC.](https://codelabs.developers.google.com/looker-psc-internet-neg-https)
  * [Create a private connections (private services access) Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip)
  * [Troubleshoot Looker (Google Cloud core) networking issues](https://docs.cloud.google.com/looker/docs/looker-core-networking-troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
