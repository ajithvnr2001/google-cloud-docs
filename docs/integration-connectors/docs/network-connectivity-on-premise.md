---
url: https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-on-premise/
title: Private connectivity for on-premise or other cloud providers \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:33.674599+00:00
---

# Private connectivity for on-premise or other cloud providers  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-on-premise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private connectivity for on-premise or other cloud providers

This page describes how to set up private connectivity from Integration Connectors to your backend service such as MySQL, Postgres, and SQL Server hosted in your on-premise data center or other cloud providers.

The following image shows the private network connectivity setup from Integration Connectors to your backend service hosted in your on-premise network.

![](https://docs.cloud.google.com/static/integration-connectors/images/on-prem.png)

This page assumes that you are familiar with the following concepts:

  * [Endpoint attachments](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private#endpoint-attachments)
  * [Managed zones](https://docs.cloud.google.com/dns/docs/zones)
  * [Private Service Connect (PSC)](https://docs.cloud.google.com/vpc/docs/private-service-connect)
  * [Google Cloud load balancer](https://docs.cloud.google.com/load-balancing)



## Considerations

When you create a PSC service attachment, consider the following key points:

  * As a service producer, you must configure a PSC service attachment that Integration Connectors can use to consume the service. After the service attachment is ready, you can configure the connection to consume the service attachment using an endpoint attachment.
  * The PSC service attachment and the load balancer must be in different subnets within the same VPC. And specifically, the service attachment must be in a NAT subnet.
  * Software running on your backend VMs must respond to both load balanced traffic and health check probes sent to each forwarding rule's IP address (the software must listen on `0.0.0.0:<port>` and not on a specific IP address assigned to a network interface). For more information, see [Health check](https://docs.cloud.google.com/load-balancing/docs/internal#health-checking).
  * Configure the firewall rules to facilitate the traffic flow. 

**Ingress rules**

    * Traffic from the PSC service attachment's subnet must reach the ILB's subnet. 
    * Within the ILB's subnet, ILB must be able to send traffic to your backend system.
    * The health check probe must be able to access your backend system. The Google Cloud health check probes have a fixed IP range (`35.191.0.0/16, 130.211.0.0/22`). So these IPs can be allowed to send traffic to your backend server.

**Egress rules**

Egress traffic is enabled by default in a Google Cloud project, unless specific deny rules are configured.

  * All your Google Cloud components such as the PSC service attachment and the load balancer must be in the same region.
  * Your backend system must not be open to the public network, as this can be a security concern. However, ensure that your backend system accepts traffic in the following scenario:

**Proxy-based/HTTP(s) load balancers (L4 proxy ILB, L7 ILB)** : All new requests originate from the load balancer. Therefore, your backend must accept requests from the proxy subnet of your VPC network. For more information, see [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).




## Configure private connectivity

This steps described in this section assume that private connectivity is already established between your Google Cloud project and your on-premise data center or other cloud providers, by using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)

To configure private connectivity, do the following tasks:

  1. Create a PSC service attachment.
  2. Create an endpoint attachment to consume the PSC service attachment.
  3. Configure your connection to use the endpoint attachment.



### Create a PSC service attachment

In order to establish private connectivity from Integration connectors, you must expose the service to Integration Connectors using a PSC service attachment. A service attachment always targets a load balancer. Therefore, if your service isn't behind a load balancer, a load balancer must be configured.

To create a PSC service attachment, do the following: 

  1. Create a [health check probe](https://docs.cloud.google.com/load-balancing/docs/internal#health-checking) and then create a load balancer. For information about setting up a regional internal proxy Network Load Balancer, see [Set up a regional internal proxy Network Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid).
  2. Create a service attachment in the same region as the service's load balancer. For information about creating a service attachment, see [Publish a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service).



### Create an endpoint attachment

**Endpoint attachment as an IP address**

For instructions on how to create an endpoint attachment as an IP address, see [Create an endpoint attachment as an IP address](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment#create-ep-ipaddr).

**Endpoint attachment as a hostname**

In certain cases such as TLS enabled backends, the destination requires you to use hostnames instead of private IPs to perform TLS validation. In those cases where a private DNS is used instead of an IP address for the host destination, in addition to creating an endpoint attachment as an IP address, you must also configure managed zones. For instructions on how to create an endpoint attachment as a hostname, see [Create an endpoint attachment as a hostname](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment#create-ep-hostname). 

Later, when you configure your connection to use the endpoint attachment, you can select this endpoint attachment.

### Configure a connection to use the endpoint attachment

Now that you have created an endpoint attachment, use the endpoint attachment in your connection. When you create a new connection or update an existing connection, in the Destinations section, select **Endpoint attachment** as the **Destination Type** and select the endpoint attachment that you created from the **Endpoint Attachment** list.

If you created a managed zone, select **Host Address** as the **Destination Type** and use the A-record that you created while creating the managed zone.

## Troubleshooting tips

If you are having issues with private connectivity, follow the guidelines listed in this section to avoid common issues.

  * To verify that the endpoint attachment is set up correctly and the PSC connection is established, check the connection status. For more information, see [Verify the endpoint attachment connection](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment#verify-ep-connection).
  * Ensure the following configuration for the firewall rules: 
    * Traffic from the PSC service attachment's subnet must be allowed to reach your backend service.
    * The load balancer must be able to send traffic to your backend system. Hybrid NEGs are supported on proxy load balancers only. Requests from a proxy load balancer originate from the proxy only subnet of the region. Therefore, your firewall rules need to be configured to allow requests from proxy only subnet ranges to reach your backend. 
  * The health check probe must be able to access your backend system. The Google Cloud health check probes have a fixed IP range (35.191.0.0/16, 130.211.0.0/22). So these IP addresses must be allowed to send traffic to your backend server.


* [Google Cloud Connectivity test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) can be used to identify any gaps in your network configuration. For more information, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests). 
* Ensure that firewall rules are updated in on-premises or other cloud environments to allow traffic from the Google Cloud region's [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
