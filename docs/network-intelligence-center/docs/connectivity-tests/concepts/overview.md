---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview/
title: Connectivity Tests overview \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:36:06.033182+00:00
---

# Connectivity Tests overview  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Connectivity Tests overview Stay organized with collections  Save and categorize content based on your preferences. 

Connectivity Tests is a diagnostics tool that lets you check connectivity between network endpoints. It analyzes your configuration and, in some cases, performs live data plane analysis between the endpoints. An endpoint is a source or destination of network traffic, such as a VM, Google Kubernetes Engine (GKE) cluster, load balancer forwarding rule, or an IP address on the internet.

To analyze network configurations, Connectivity Tests simulates the expected forwarding path of a packet through your Virtual Private Cloud (VPC) network, Cloud VPN tunnels, or VLAN attachments. Connectivity Tests can also simulate the expected inbound forwarding path to resources in your VPC network.

For some connectivity scenarios, Connectivity Tests also performs live data plane analysis. This feature sends packets over the data plane to validate connectivity and provides baseline diagnostics of latency and packet loss. If the route is supported for the feature, each test that you run includes a live data plane analysis result.

To learn how to create and run tests for various scenarios, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

The API for Connectivity Tests is the Network Management API. For more information, see the [API documentation](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/apis).

## Why use Connectivity Tests?

Connectivity Tests can help you troubleshoot the following network connectivity issues:

  * Unintended inconsistent configurations
  * Obsolete configurations caused by network configuration changes or migrations
  * Configuration errors for a variety of network services and functions



When testing Google-managed services, Connectivity Tests can also help you determine whether there is an issue in your VPC network or in the Google-owned VPC network used for the service resources.

## How Connectivity Tests analyzes configurations

When analyzing network configurations, Connectivity Tests uses an [abstract state machine](https://wikipedia.org/wiki/Abstract_state_machine) to model how a VPC network should process packets. Google Cloud processes a packet in several logical steps.

### The analysis can take many possible paths

Because of the variety of VPC network services and features that the configuration analysis supports, a test packet traversing a VPC network configuration can take many possible paths.

The following diagram shows a model for how the configuration analysis simulates trace traffic between two Compute Engine instances—one on the left and another on the right.

### The analysis depends on your network infrastructure

Depending on your Google Cloud network and resource configurations, this traffic might go through a Cloud VPN tunnel, a VPC network, a Google Cloud load balancer, or a peered VPC network before reaching the destination Compute Engine instance.

[ ![The network abstract state machine.](https://docs.cloud.google.com/static/network-intelligence-center/docs/connectivity-tests/images/nam-concept.svg)](https://docs.cloud.google.com/static/network-intelligence-center/docs/connectivity-tests/images/nam-concept.svg) The network abstract state machine (click to enlarge).

### The analysis follows one of the many finite states

The bounded number of steps between discrete states until a packet has been delivered or dropped is modeled as a [finite state machine](https://wikipedia.org/wiki/Finite-state_machine). This finite state machine can be in exactly one of many finite states at any one time and might have multiple successor states.

For example, when Connectivity Tests matches several routes according to route precedence, Google Cloud can choose a route among several routes based on an unspecified hashing function in the data plane. If a policy-based route is configured, Connectivity Test routes the packet to the next hop, which is an internal load balancer.

In the previous case, the Connectivity Tests trace returns all of the possible routes but can't determine the method Google Cloud used to return the routes. This is because that method is internal to Google Cloud and is subject to change.

### Google-managed services

Google-managed services, such as Cloud SQL and Google Kubernetes Engine (GKE), allocate resources for customers in projects and VPC networks that Google owns and manages. Customers don't have permission to access these resources.

The Connectivity Tests configuration analysis can still run a test and provide an overall reachability result for Google-managed services, but it doesn't provide details for the tested resources in the project owned by Google.

The following diagram shows a model for how the configuration analysis simulates trace traffic from a Compute Engine instance in a customer VPC network to a Cloud SQL instance in the Google-owned VPC network. In this example, the networks are connected through VPC Network Peering.

Similar to a standard test between two Compute Engine instances, the logical steps include checking the relevant egress firewall rules and matching the route. When you run a test, Connectivity Tests configuration analysis provides details about these steps. However, for the final logical step of analyzing the configuration in the Google-owned VPC network, the analysis provides only an overall reachability result. Connectivity Tests doesn't provide details for the resources in the Google-owned project because you don't have permission to view them.

For more information, see the test examples in [Test connectivity to and from Google-managed services](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/test-google-managed-services).

[ ![The network abstract state machine for Google-managed services.](https://docs.cloud.google.com/static/network-intelligence-center/docs/connectivity-tests/images/managed-service-state-machine.svg)](https://docs.cloud.google.com/static/network-intelligence-center/docs/connectivity-tests/images/managed-service-state-machine.svg) The network abstract state machine for Google-managed services (click to enlarge).

### Supported configurations

The Connectivity Tests configuration analysis supports testing the network configurations described in the following sections.

#### Source endpoints

Connectivity Tests configuration analysis supports the following source endpoints:

  * Compute Engine instance
  * [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service
  * [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) job
  * [Cloud Run functions (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/concepts/overview)
  * [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard)
  * [Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/introduction)
  * [Database Migration Service private connection](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections)
  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) control plane
  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) Pod
  * Internet IP address
  * IP address from an on-premises network
  * IP address of a Compute Engine instance
  * IP address of a Cloud SQL instance
  * IP address of a GKE control plane
  * IP address of a GKE Pod
  * Unassigned IP address in a Virtual Private Cloud network



#### Destination endpoints

Connectivity Tests configuration analysis supports the following destination endpoints:

  * Compute Engine instance
  * [Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/introduction)
  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) control plane
  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) Pod
  * [External](https://docs.cloud.google.com/load-balancing/docs/https) and [internal](https://docs.cloud.google.com/load-balancing/docs/l7-internal) Application Load Balancer
  * [External](https://docs.cloud.google.com/load-balancing/docs/tcp) and [internal](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) Proxy Network Load Balancer
  * [External](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer#ext-pass-netlb) and [internal](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer#int-pass-netlb) Passthrough Network Load Balancer
  * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoint
  * [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)
  * [Memorystore for Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/instances)
  * Internet IP address
  * IP address from an on-premises network
  * IP address of a forwarding rule
  * IP address of a Compute Engine instance
  * IP address of a Cloud SQL instance
  * IP address of a GKE control plane
  * IP address of a GKE Pod
  * IP address of a Memorystore for Redis Cluster
  * IP address of a Memorystore for Redis instance



#### Google Cloud networking features

You can test connectivity between resources that use the following features (both IPv4 and IPv6 are supported whenever applicable):

  * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
  * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
  * [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options)
  * [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
  * [Alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip)
  * [Privately used public IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges)
  * Compute Engine instances with multiple network interfaces
  * [VPC routing](https://docs.cloud.google.com/vpc/docs/routes)
  * [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls)
  * [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies)
  * [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies) and [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies)
  * [Resource Manager tags for firewalls](https://docs.cloud.google.com/vpc/docs/tags-firewalls-overview), including when attached to [Compute Engine instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [Policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes)
  * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)
  * [Instances with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address), including [instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [VPC spokes and hybrid spokes for NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)
  * [Public NAT and Private NAT](https://docs.cloud.google.com/nat/docs/overview)
  * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
  * [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview), including dynamic routes that use BGP and static routes



#### Considerations for Cloud Load Balancing

For Cloud Load Balancing, Connectivity Tests configuration analysis supports the following features:

  * Testing connectivity to the load balancer's IP address, including analysis of its underlying resources (such as backend services, backend buckets, and target pools)
  * Verifying connectivity of Cloud Load Balancing health checks to backends
  * Analyzing static routes that use an [internal Passthrough Network Load Balancer as the next hop](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview) (specify an IP address from the static route IP address range as the destination endpoint)



For Cloud Load Balancing features that are unsupported, see the Unsupported configurations section.

For information about how Connectivity Tests analyzes backends of a load balancer, see [Number of traces in a test to a load balancer](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/test-load-balancers#number-of-traces).

#### Considerations for Google Kubernetes Engine

For GKE, Connectivity Tests configuration analysis supports the following features:

  * Connectivity to and between [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) nodes and the GKE control plane
  * Connectivity to and between [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) Pods, including evaluation of [GKE network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) and [IP masquerading](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent).



Testing connectivity to a [GKE service through Cloud Load Balancing](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer) is supported. However, to evaluate GKE network policies and IP masquerading, you must use Pods as your test endpoints.

#### Considerations for serverless endpoints

The source IP addresses of serverless endpoints are usually nondeterministic. For each test run, Connectivity Tests selects a random IP address from the pool of addresses that are available to the serverless endpoint. For general information about how IP addresses are allocated for serverless endpoints, see the following:

  * For external connectivity, see [IP addresses](https://docs.cloud.google.com/appengine/docs/standard/outbound-ip-addresses#outbound-ip-addresses).
  * For connectivity through a Serverless VPC Access connector, see [Send serverless traffic to a Virtual Private Cloud network](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access).
  * For connectivity through Direct VPC egress, see [IP address allocation](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-ip-allocation). This connectivity type is available only for Cloud Run.



In some cases, Direct VPC egress and Serverless VPC Access connectors are configured to route traffic from serverless endpoints through external connectivity instead of the Virtual Private Cloud network, depending on the egress settings.

For serverless features that are unsupported, see the Unsupported configurations section.

### Unsupported configurations

The Connectivity Tests configuration analysis doesn't support testing the following network configurations:

  * Firewall policy rules with [FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview) aren't supported. If such firewalls can potentially affect a specific traffic flow, Connectivity Tests returns a corresponding warning.
  * [Internet NEG](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) backends targeting FQDNs aren't supported. However, internet NEG backends targeting IP addresses are supported.
  * [Cloud Service Mesh load balancers](https://docs.cloud.google.com/service-mesh/docs/load-balancing) with the `INTERNAL_SELF_MANAGED` forwarding rules aren't supported.
  * [Google Cloud Armor](https://docs.cloud.google.com/armor/docs) policies aren't considered or used when tracing connectivity to an external Application Load Balancer IP address.
  * [HA VPN gateways connected to Compute Engine instances](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/connect-ha-vpn-vm) aren't supported.
  * [Cloud SQL external server replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external) defined by DNS names aren't supported. However, external server replicas defined by IP addresses are supported.
  * [Cloud Run functions](https://docs.cloud.google.com/functions) (2nd gen) aren't supported. However, you can test connectivity from a Cloud Run function (2nd gen) by creating a Connectivity Test for the underlying Cloud Run revision. A Cloud Run revision is created every time a Cloud Run function is deployed.
  * [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible) isn't supported.
  * [Cloud Run](https://docs.cloud.google.com/run) worker pools aren't supported. For more information, see [Services, jobs, and worker pools: three ways to run your code](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#services-and-jobs).



## How Connectivity Tests analyzes the live data plane

The live data plane analysis feature tests connectivity by sending multiple probe packets from the source endpoint to the destination. If the destination isn't a Google Cloud resource, connectivity is tested between the source endpoint and the [network edge location](https://docs.cloud.google.com/vpc/docs/edge-locations).

The live data plane analysis results show you the number of probes sent, the number of probes that successfully reached the destination, and a reachability status. This status is determined based on how many probes were successfully delivered, as described in the following table.

Status | Number of probes that reached their destination | Reachable | At least 95%  
---|---  
Unreachable | None  
Partially reachable | More than 0 and less than 95%  
  
In addition to showing how many packets were successfully delivered, live data plane analysis also shows median and 95th percentile one-way latency information. When the destination is an internet IP address, live data plane analysis sends probes and shows the results for each [Google network edge router](https://docs.cloud.google.com/vpc/docs/edge-locations) that traffic might be routed through.

### Limitations

Live data plane analysis might not cover all possible networking paths:

  * If the destination endpoint is a Google Cloud load balancer with multiple backends, each live data plane analysis probe is sent to a random backend. Some backends can be tested by many probes while other backends might not be tested at all.
  * In case of equal-cost multipath (ECMP) routing, each live data plane analysis probe is forwarded by a random route. Some routing paths can be tested by many probes while other routing paths might not be tested at all.
  * The number of live data plane analysis probes doesn't depend on the number of existing networking paths, and there might not be a sufficient number of live data plane analysis probes to test each possible path.



If you see apparent discrepancies between the configuration analysis and live data plane analysis results, see [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting).

### Supported configurations

Live data plane analysis supports a subset of the configurations that are tested by Connectivity Tests configuration analysis.

#### Source endpoints

Live data plane analysis supports the following source endpoints:

  * Compute Engine instance
  * Serverless endpoint configured with a Serverless VPC Access connector and associated with one of the following resources: 
    * [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service
    * [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) job
    * [Cloud Run functions (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/concepts/overview)
    * [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard)
  * GKE control plane
  * Cloud SQL instance
  * [Database Migration Service private connection](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections)



#### Destination endpoints

Live data plane analysis supports the following destination endpoints:

  * Compute Engine instance
  * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) with a producer internal passthrough Network Load Balancer
  * Internet IP address, tested to the [network edge location](https://docs.cloud.google.com/vpc/docs/edge-locations)
  * VLAN attachment for [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
  * Private endpoint associated with one of the following resources: 
    * Cloud SQL instance
    * [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)
    * [Memorystore for Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/instances)
    * GKE control plane



#### Protocols

Live data plane analysis supports TCP and UDP protocols.

#### Google Cloud networking features

Live data plane analysis supports the following features:

  * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
  * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
  * [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * VPC spokes and hybrid spokes in [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)
  * [Alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip)
  * [External IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses)
  * [Internal IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#networkaddresses), including [privately used public IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges)
  * Compute Engine instances with multiple network interfaces
  * [VPC routing](https://docs.cloud.google.com/vpc/docs/routes)
  * [Public NAT and Private NAT](https://docs.cloud.google.com/nat/docs/overview), except for [NAT64](https://docs.cloud.google.com/nat/docs/public-nat#nat64)
  * [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls)
  * [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies), [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies), and [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies)
  * [Secure tags for firewalls](https://docs.cloud.google.com/vpc/docs/tags-firewalls-overview), including when attached to [Compute Engine instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [Policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes)
  * [Instances with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address), including [instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)



### Unsupported configurations

Live data plane analysis doesn't support and isn't executed for the following network configurations:

  * Non-Google Cloud resources as source endpoints: 
    * Internet IP addresses
    * Inbound traffic to Google Cloud through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview), [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview), and [NCC hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#hybrid_spokes)
  * Unassigned IP addresses in a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) as source endpoints
  * Source and destination endpoints are the same Compute Engine instance
  * Non-running Compute Engine instances
  * GKE Pods
  * Google API and services
  * [External](https://docs.cloud.google.com/load-balancing/docs/https) and [internal](https://docs.cloud.google.com/load-balancing/docs/l7-internal) Application Load Balancer
  * [External](https://docs.cloud.google.com/load-balancing/docs/tcp) and [internal](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) Proxy Network Load Balancer
  * [External passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer#ext-pass-netlb)
  * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [NAT64](https://docs.cloud.google.com/nat/docs/public-nat#nat64)



## Considerations and constraints

Evaluate the following considerations when deciding whether to use Connectivity Tests.

  * The configuration analysis that Connectivity Tests performs is based entirely on configuration information for Google Cloud resources and might _not_ represent the actual condition or status of the data plane for a VPC network.
  * While Connectivity Tests does acquire some dynamic configuration information, such as the Cloud VPN tunnel state and dynamic routes that are on Cloud Router, it does _not_ access or maintain the health state of Google internal production infrastructure and data plane components.
  * A status of `Packet could be delivered` for a Connectivity Test does _not_ guarantee that traffic can pass through the data plane. The purpose of the test is to validate configuration issues that can cause traffic to drop.



For supported routes, the live data plane analysis results supplement the configuration analysis results by testing whether transmitted packets arrive at the destination.

### Connectivity Tests has no knowledge of networks outside of Google Cloud

Outside networks are defined as the following:

  * On-premises networks that reside in your data center or other facility where you operate your hardware devices and software applications.
  * Other cloud providers where you run resources.
  * A host on the internet that sends traffic to your VPC network.



### Connectivity Tests doesn't perform firewall connection tracking

Connection tracking for VPC firewalls stores information about new and established connections and enables allowing or restricting subsequent traffic based on that information.

The Connectivity Tests configuration analysis doesn't support firewall connection tracking because the firewall connection table is located in the data plane for a Compute Engine instance and is inaccessible. However, the configuration analysis can simulate connection tracking by allowing a return connection that would normally be denied by an ingress firewall rule, as long as Connectivity Tests initiates the outbound connection.

Live data plane analysis doesn't support testing firewall connection tracking.

### Connectivity Tests can't test Compute Engine instances configured to modify forwarding behavior

Connectivity Tests can't test Compute Engine instances that have been configured to act in the data plane as routers, firewalls, NAT gateways, or VPNs. This type of configuration makes it difficult to assess the environment running on the Compute Engine instance. Additionally, live data plane analysis doesn't support this type of testing scenario.

### Connectivity Tests result times can vary

Getting Connectivity Tests results can take from 30 seconds to up to 10 minutes. The time a test takes is based on the size of your VPC network configuration and the number of Google Cloud resources that you use.

The following table shows response times that you can expect for all users running a test against a sample configuration in a query. This configuration contains Compute Engine instances, a Cloud VPN tunnel, and Google Cloud load balancers.

Response times per query Project size | Number of Google Cloud resources | Response latency  
---|---|---  
Small project | Fewer than 50 | 60 seconds for 95% of queries from all users  
Medium project | Greater than 50 but fewer than 5000 | 120 seconds for 95% of queries from all users  
Large project | Greater than 5000 | 600 seconds for 95% of queries from all users  
  
### Live data plane analysis is not intended for continuous monitoring

Live data plane analysis performs one-time verification of network connectivity for diagnostic purposes. For continuous monitoring of connectivity and packet loss, use [Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard).

## VPC Service Controls support

VPC Service Controls can provide additional security for Connectivity Tests to help mitigate the risk of data exfiltration. Using VPC Service Controls, you can add projects to service perimeters that protect resources and services from requests that originate outside the perimeter.

To learn more about service perimeters, see the [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) page of the VPC Service Controls documentation.

## What's next

  * [Roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control)

  * [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)

  * [Common test scenarios](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/common-use-cases)

  * [Detect invalid or inconsistent configurations](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/detecting-configs)

  * [Identify and fix ICMP issues](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/tutorials/tutorial-troubleshooting-workflow) (tutorial)

  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
