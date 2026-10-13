---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/internet-negs/
title: Cloud Service Mesh with internet network endpoint groups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:05:02.984251+00:00
---

# Cloud Service Mesh with internet network endpoint groups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/internet-negs/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh with internet network endpoint groups

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

You can configure Cloud Service Mesh to use [internet network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) of the type `INTERNET_FQDN_PORT`. The external service is represented by its fully qualified domain name (FQDN) and port number in the NEG. The NEG can contain only one `FQDN:Port` pair, and the backend service can contain only one NEG of this type. The FQDN is resolved by using the underlying Virtual Private Cloud (VPC) network's [name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order).

## Expand the Cloud Service Mesh service mesh using FQDN backends

The Cloud Service Mesh service mesh can route traffic to private services that are reachable by using hybrid connectivity, including named on-premises, multi-cloud, and internet services. The remote service is referenced by its FQDN.

[ ![Extending the Cloud Service Mesh service mesh to on-premises or multi-cloud locations using FQDN backends over hybrid connectivity.](https://docs.cloud.google.com/static/service-mesh/docs/images/internet-neg-example-setup.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/internet-neg-example-setup.svg) Extending the Cloud Service Mesh service mesh to on-premises or multi-cloud locations using FQDN backends over hybrid connectivity (click to enlarge)

You can also route traffic to services that are reachable over the public internet.

[ ![Extending the Cloud Service Mesh service mesh to an internet service using FQDN backends.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-internet-service.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-internet-service.svg) Extending the Cloud Service Mesh service mesh to an internet service using FQDN backends (click to enlarge)

## Google Cloud resources and architecture

This section describes the resources and architecture for configuring Cloud Service Mesh with an internet NEG.

## `INTERNET_FQDN_PORT` network endpoint group

To route traffic to an external service referenced by its FQDN, use the global internet NEG of the type `INTERNET_FQDN_PORT`. The NEG contains the FQDN of your service and its port number. Cloud Service Mesh programs the FQDN into Envoy proxies by using xDS configuration.

Cloud Service Mesh itself does not guarantee name resolution and reachability of the remote endpoints. The FQDN must be resolvable by the name resolution order of the VPC network to which the Envoy proxies are attached, and the resolved endpoints must be reachable from the Envoy proxies.

## Health checks

Health checking behavior for network endpoints of the type `INTERNET_FQDN_PORT` differs from health checking behavior for other types of network endpoints used with Cloud Load Balancing and Cloud Service Mesh. While most other network endpoint types use Google Cloud's centralized health checking system, the NEGs used for endpoints in multi-cloud environments (`INTERNET_FQDN_PORT` and `NON_GCP_PRIVATE_IP_PORT`) use Envoy's distributed health checking mechanism.

Envoy supports the following protocols for health checking:

  * HTTP
  * HTTPS
  * HTTP/2
  * TCP



You configure health checks by using the Compute Engine APIs.

## DNS considerations

There are two distinct considerations regarding DNS:

  * The DNS server that hosts the resource records of your external service.
  * The mode with which the Envoy proxy is configured to use DNS for connection management.



### Cloud DNS server

You can create a Cloud DNS [managed private zone](https://docs.cloud.google.com/dns/docs/zones#create-private-zone) to host the DNS records in your Google Cloud project. You can also use other features of Cloud DNS, such as [forwarding zones](https://docs.cloud.google.com/dns/docs/zones#creating-forwarding-zones), to fetch records from an on-premises DNS server.

### Envoy DNS mode

Envoy DNS mode, which is also called _service discovery_ , specifies how the Envoy proxy uses DNS records for managing outbound connections. Cloud Service Mesh configures Envoy to use [strict DNS mode](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/service_discovery#strict-dns). Strict DNS mode enables load balancing to all resolved endpoints. It honors health check status and drains connections to endpoints that are unhealthy or no longer resolved by using DNS. You cannot change this mode.

For more information about service discovery, see the Envoy documentation.

## Connectivity and routing

If you are routing traffic to a private service, the following are the requirements for the underlying network connectivity:

  * Hybrid connectivity between the VPC network and the on-premises data center or third-party public cloud is established by using Cloud VPN or Cloud Interconnect.
  * VPC firewall rules and routes are correctly configured to establish bi-directional reachability from Envoy to your private service endpoints and, if applicable, to the on-premises DNS server.
  * For successful regional high-availability failover, global dynamic routing must be enabled. For more details, see [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes).



If you are routing traffic to an external service that is reachable on the internet, the following are the requirements:

  * The client virtual machine (VM) instances in the VPC network must have an external IP address or Cloud NAT.
  * The [default route](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet) must be present to egress traffic to the internet.



In both of the preceding cases, traffic uses the VPC network's routing.

## Security

FQDN backends are compatible with [Cloud Service Mesh's security features](https://docs.cloud.google.com/service-mesh/docs/service-routing/security-overview#securing_service-to-service_communications) and APIs. On the outbound connections to your external service, you can configure FQDN in the SNI header by using [client TLS policies](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-internet-neg#unauth-https).

## Limitations and considerations

  * Internet NEGs of the type `INTERNET_IP_PORT` are not supported with Cloud Service Mesh.
  * Envoy version 1.15.0 or later is required with FQDN backends.
  * Use the Google Cloud CLI or REST APIs to configure Cloud Service Mesh. End-to-end configuration using the Google Cloud console is not supported.
  * FQDN backends are only supported with Envoy. Proxyless gRPC is not supported.
  * When you use the NEG type `INTERNET_FQDN_PORT` with Cloud Service Mesh, health checks of the remote endpoints are done using Envoy's distributed health checking mechanism. Whenever a new remote endpoint is added, all Envoy proxies start health checking it independently.

Similarly, when a new Envoy proxy is added to the mesh, it starts checking all the remote endpoints. Therefore, depending on the number of Envoy proxies and remote endpoints in your deployment, the resulting health check mesh might cause significant network traffic and an undue load on the remote endpoints. You can choose not to configure health checks.

  * Health check status is not visible in the Google Cloud console for FQDN backends.

  * Health checking that uses the UDP, SSL, and gRPC protocols is not supported.

  * The following health check options are not supported:

    * HTTP/HTTP2/HTTPS health check 
      * `--proxy-header`
      * `--response`
    * TCP health check 
      * `--proxy-header`
      * `--request`
      * `--response`



## What's next

  * To set up Cloud Service Mesh with internet NEGS, see [Set up external backends](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-internet-neg).
  * To learn about hybrid connectivity NEGs, see [Cloud Service Mesh with hybrid connectivity NEGs](https://docs.cloud.google.com/service-mesh/docs/service-routing/multi-environment-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
