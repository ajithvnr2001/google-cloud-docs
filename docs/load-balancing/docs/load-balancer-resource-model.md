---
url: https://docs.cloud.google.com/load-balancing/docs/load-balancer-resource-model/
title: Cloud Load Balancing resource model \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:34.526550+00:00
---

# Cloud Load Balancing resource model  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/load-balancer-resource-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Cloud Load Balancing resource model Stay organized with collections  Save and categorize content based on your preferences. 

A load balancer is a system composed of multiple interacting components. There isn't a single API resource that represents a load balancer. Instead, multiple components work together to distribute incoming traffic across multiple backends.

The following diagram shows the core components of an Application Load Balancer, a proxy Network Load Balancer, and a passthrough Network Load Balancer.

### Application load balancer

[ ![Components of an Application Load Balancer](https://docs.cloud.google.com/static/load-balancing/images/overview/components_application_load_balancer.svg)](https://docs.cloud.google.com/static/load-balancing/images/overview/components_application_load_balancer.svg) Components of an Application Load Balancer (click to enlarge).

### Proxy network load balancer

[ ![Components of a proxy Network Load Balancer](https://docs.cloud.google.com/static/load-balancing/images/overview/components_proxy_network_load_balancers.svg)](https://docs.cloud.google.com/static/load-balancing/images/overview/components_proxy_network_load_balancers.svg) Components of a proxy Network Load Balancer (click to enlarge).

### Passthrough network load balancer

[ ![Components of a passthrough Network Load Balancer](https://docs.cloud.google.com/static/load-balancing/images/overview/components_passthrough_network_load_balancers.svg)](https://docs.cloud.google.com/static/load-balancing/images/overview/components_passthrough_network_load_balancers.svg) Components of a passthrough Network Load Balancer (click to enlarge).

This section provides a high-level overview of the key components of a load balancer, starting from the point where traffic reaches the load balancer to the stage where it is routed to the backend resource. For a deeper understanding of each load balancer component, refer to the page linked in each section.

## Forwarding rule

A forwarding rule specifies an IP address, an IP protocol, and one or more ports on which the load balancer accepts traffic. The forwarding rule and its attached IP address represent the frontend of a Google Cloud load balancer.

For more information, see [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).

## Target proxy

Target proxies terminate incoming connections from clients and create new connections from the load balancer to the backends.

  * The first connection originates from the client and is terminated at the target proxy of the load balancer.

  * The second connection starts at the target proxy and ends at the backend instance, which handles the client request.




The first connection is terminated either in a Google Front End (GFE) or in a specially designated subnet known as the proxy-only subnet, which is reserved exclusively for Envoy proxies. To know whether a load balancer is GFE-based or Envoy-based, see [Underlying technologies of Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#tech-gclb).

Target proxies are used only by proxy-based load balancers such as Application Load Balancers and proxy Network Load Balancers. For these types of load balancers, responses from the backend instances are sent back to the target proxy rather than directly to the client.

To make routing decisions, a target HTTP(S) proxy uses a URL map. A target TCP proxy can optionally use one or more TLS routes to perform SNI-based routing.

For more information, see [Target proxies](https://docs.cloud.google.com/load-balancing/docs/target-proxies).

## Proxy-only subnet

A proxy-only subnet provides a pool of IP addresses that are reserved exclusively for Envoy proxies used by Google Cloud load balancers. The proxies terminate incoming connections and then create new connections to the backend.

For more information, see [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/https#proxy-only-subnet)

## SSL certificates

Also known as Transport Layer Security (TLS) certificates, SSL certificates facilitate secure communication between clients and load balancers. Proxy-based load balancers whose forwarding rules reference a target HTTPS proxy or a target SSL proxy require a private key and SSL certificate as part of the load balancer's target proxy configuration.

For more information, see [SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).

## URL map

Upon terminating the connection, the target HTTP(S) proxy uses the URL map to decide where to route the new request (the second connection as stated in the Target proxy section). The URL map routes the request to either the backend service or the backend bucket. URL maps are only used by Application Load Balancers. As Application Load Balancers operate at Layer 7 of the OSI model, they can make routing decisions based on HTTP attributes, such as domain name, request path, and query parameters.

For more information, see [URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

## TLS route

A TLS route (represented by the `TLSRoute` API resource) lets you route TCP traffic to backend services based on the Server Name Indication (SNI) hostnames provided in the client's TLS handshake.

TLS routes are optionally attached to a load balancer's target TCP proxy. Instead of routing all incoming traffic to a single default backend service, the target TCP proxy uses the TLS route configuration to dynamically inspect the `ClientHello` message of the TLS handshake and route the traffic to the appropriate backend service based on the matching SNI hostname.

TLS routes are used only by proxy Network Load Balancers (specifically regional external proxy Network Load Balancers, regional internal proxy Network Load Balancers, and cross-region internal proxy Network Load Balancers). Because they operate at the TLS layer, they enable _TLS passthrough_ , where the encrypted traffic is passed directly to the backend without being decrypted by the load balancer.

For more information, see [SNI-based routing with TLS routes](https://docs.cloud.google.com/load-balancing/docs/tcp#sni-based-routing).

## Backend service

A backend service defines how your load balancer distributes traffic. The backend service configuration contains a set of values, such as the protocol used to connect to backends, various distribution and session settings, health checks, and timeouts.

These settings provide fine-grained control over how your load balancer behaves and let you direct traffic to the correct backends, which can be either [VM instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) or [network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs).

For more information, see [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).

## Backend bucket

If your workload serves _static content_ using the HTTP(S) protocol, you can use a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets) to store static content, and then use a [backend bucket](https://docs.cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets) to route requests to it.

## Health checks

When you configure a load balancer's backend service, you need to specify one or more health checks for its backends. A health check, as the name suggests, determines whether the backend instances of the load balancer are healthy. This determination is based on the ability of the backend to respond to incoming traffic. The traffic that a backend needs to respond to depends on the type of the load balancer. You can create health checks using both [Layer 7 and Layer 4 protocols](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports) to monitor load balanced instances.

## Firewall rules

For health checks to work, you must create ingress `allow` firewall rules that allow health check probes to reach your backends.

Load balancers based on Google Front Ends require an ingress allow firewall rule that permits traffic from the [CIDRs of Google Front End](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges) to connect to your backends. Load balancers based on the open source Envoy proxy require an ingress `allow` firewall rule that permits traffic from the _proxy-only subnet_ to reach the backend instances.

For more information, see [Firewall rules](https://docs.cloud.google.com/load-balancing/docs/firewall-rules).

## Backends

Backends are the final destination of load-balanced traffic.

Different load balancers support different types of backends. When you add a backend to the backend service, you specify a _balancing mode_. This mode evaluates the backend's capacity to handle new requests and determines how traffic is distributed among the backends.

For more information, see [Backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#backends).

## What's next

  * To help you determine which Google Cloud load balancer best meets your needs, see [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer).
  * To see a comparative overview of the load-balancing features offered by Cloud Load Balancing, see [Load balancer feature comparison](https://docs.cloud.google.com/load-balancing/docs/features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
