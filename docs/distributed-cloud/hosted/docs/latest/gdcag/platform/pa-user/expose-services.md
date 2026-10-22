---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services/
title: Manage load balancers \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:26.037975+00:00
---

# Manage load balancers  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage load balancers Stay organized with collections  Save and categorize content based on your preferences. 

This overview page explains how you can configure internal and external load balancers in Google Distributed Cloud (GDC) air-gapped for both zonal and global network configurations.

Load balancing for GDC ensures efficient traffic distribution across backend workloads, enhancing application availability and performance. The algorithm used to distribute the traffic is Maglev; for more details, see Load balancing algorithm.

This page is for network administrators within the platform administrator group, or developers within the application operator group, who are responsible for managing network traffic for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Load balancing architecture

GDC provides load balancers that enable applications to expose services to one another. Load balancers allocate a stable virtual IP (VIP) address that balances traffic over a set of backend workloads. Load balancers in GDC perform layer four (L4) load balancing, which means they map a set of configured frontend TCP or UDP ports to corresponding backend ports. Load balancers are configured at the project level.

Load balancers are configured for the following workload types:

  * Workloads running on VMs.
  * Containerized workloads inside the Kubernetes cluster.



There are three ways to configure load balancers in GDC:

  * Use the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview). You can use this API to create global or zonal load balancers.
  * Use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). You can use this API to create global or zonal load balancers.
  * Use the Kubernetes Service directly from the Kubernetes cluster. This method only creates zonal load balancers.

**Note:** The Kubernetes Service is the only supported way to configure load balancers for [standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

## Load balancer components

When you use the KRM API or gdcloud CLI to configure the load balancer, you use an L4 passthrough load balancer:

  * L4 means the protocol is either TCP or UDP.
  * Passthrough means there is no proxy between workload and client.



The load balancer consists of the following configurable components:

  * **Forwarding rules** : specify what traffic is forwarded, and to which backend service. Forwarding rules have the following specifications:

    * Consists of three tuples, CIDR, port and protocol, for the client to access.
    * Supports TCP and UDP protocols.
    * Offers internal and external forwarding rules. Clients can access internal forwarding rules from within the Virtual Private Cloud (VPC). Clients can access external forwarding rules from outside the GDC platform or from within by workloads that have `EgressNAT` value defined.
    * Forwarding rules connect to a backend service. You can point multiple forwarding rules to point to the same backend service.
  * **Backend services** : are the load balancing hub that link forwarding rules, health checks and backends together. A backend service references a backend object, that identifies the workloads the load balancer forwards the traffic to. There are limitations on what backends a single backend service can reference:

    * One zonal backend resource per zone.
    * One cluster backend resource per cluster. This can't be mixed with the project backends.
  * **Backends** : a zonal object that specifies the endpoints that serve as the backends for the created backend services. Backend resources must be scoped to a zone. Select endpoints using labels. Scope the selector to a project or cluster:

    * A project backend is a backend that doesn't have the `ClusterName` field specified. In this case the specified labels apply to all of the workloads in the specific project, in the specific VPC of a zone. The labels are applied to VM and pod workloads across multiple clusters. When a backend service uses a project backend, you can't reference another backend for that zone in that backend service.

    * A cluster backend is a backend that has the `ClusterName` field specified. In this case, the specified labels apply to all the workloads in the named cluster in the specified project. You can specify, at most, one backend per zone per cluster in a single backend service.

  * **Health checks** : specify the probes to determine whether a given workload endpoint in the backend is healthy. The unhealthy endpoint is taken out from the load balancer, until it becomes healthy again. Health checks are only applicable to VM workloads. Pod workloads can use the built-in Kubernetes probe mechanism to determine if a specific endpoint is healthy. Refer to the [health checks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/health-checks) for more information.




When using the Kubernetes Service directly from the Kubernetes user cluster, you use the `Service` object instead of the previously listed components. You can only target workloads in the cluster where the `Service` object is created.

## External and internal load balancing

GDC applications have access to the following networking service types:

  * **Internal Load Balancer (ILB)** : lets you expose a service to other clusters within the organization.
  * **External Load Balancer (ELB)** : allocates a Virtual IP (VIP) address from a range that is routable from external workloads and exposes services outside of the GDC organization, such as other organizations inside or outside of the GDC instance. Use session affinity for ELBs to ensure that requests from a client are consistently routed to the same backend.



## Global and zonal load balancers

You can create global or zonal load balancers. The scope of global load balancers spans across a GDC universe. Each GDC universe can consist of multiple GDC zones organized into regions that are interconnected and share a control plane. For example, a universe consisting of two regions with three zones each might look like: `us-virginia1-a`, `us-virginia1-b`, `us-virginia1-c` and `eu-ams1-a`, `eu-ams1-b`, `eu-ams1-c`.

The scope of zonal load balancers is limited to the zones specified at the time of creation. Each zone is an independent disaster domain. A zone manages infrastructure, services, APIs, and tooling that use a local control plane.

For more information about global and zonal resources in a GDC universe, see [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).

You can create global load balancers using the following methods:

  * Use the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview). Use the API version `networking.global.gdc.goog` to create global resources.
  * Use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). Use the `--global` flag when using the gdcloud CLI commands to specify a global scope.



You can create zonal load balancers using the following methods:

  * Use the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview). Use the API version `networking.gdc.goog` to create zonal resources.
  * Use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). Use the `--zone` flag when using the gdcloud CLI commands to specify which zones to create load balancers for.
  * Use the Kubernetes `Service` directly from the Kubernetes cluster.



## Service virtual IP addresses

ILBs allocate VIP addresses that are internal only to the organization. These VIP addresses are not reachable from outside the organization; therefore, you can only use them to expose services to other applications within an organization. These IP addresses might overlap between organizations in the same instance.

On the other hand, ELBs allocate VIP addresses that are externally reachable from outside the organization. For this reason, ELB VIP addresses must be unique among all organizations. Typically, fewer ELB VIP addresses are available for use by the organization.

## Load balancing algorithm

Our Load Balancer uses _Maglev_ , a consistent hashing algorithm, to distribute incoming traffic to backend targets. This algorithm is designed for high performance and resiliency, ensuring that traffic is spread evenly and predictably, while maximizing data locality in the backends.

### How Maglev works: the hashing mechanism

Maglev makes forwarding decisions by hashing the properties of each incoming packet. This ensures that all packets for a given connection are consistently sent to the same backend to maximize data locality.

  * **Hashing Input (5-tuple)** : The algorithm uses a standard 5-tuple from the packet's header to generate a hash. This tuple consists of: 
    1. **Source IP Address**
    2. **Source Port**
    3. **Destination IP Address**
    4. **Destination Port**
    5. **Protocol** (e.g., TCP, UDP)
  * **Forwarding Decision** : The result of this hash deterministically maps the connection to one of the healthy backends in the load balancing pool. For the lifetime of that connection, all its packets will be forwarded to the same backend.
  * **Entropy for Balancing** : By using all five elements of the tuple, Maglev generates sufficient entropy to ensure that different connections are spread evenly across all available backends.



### Handling backend health and failures

Maglev is designed to be resilient and minimize disruption when the set of available backends changes.

  * **Backend Failure** : When a backend fails its health checks, it is removed from the list of available targets. The connections that were previously routed to the failed backend are terminated. New connections will be automatically redistributed among the remaining healthy backends based on the hashing algorithm. Importantly, connections to other healthy backends are not impacted or re-routed.
  * **Backend Recovery** : When the unhealthy backend becomes healthy again and is added back to the pool, the consistent nature of the hash ensures this backend is added to the pool with minimal disruption, and the LB will re-balance the load taking this newly healthy backend. This "minimal disruption" approach prevents a massive reshuffling of all existing connections, which could otherwise overwhelm application caches or state.



### Behavior in multi-zone deployments

It is critical to understand that Maglev is _topology-unaware_. It distributes traffic based purely on the mathematical outcome of the hash, without considering the physical location or network path to the backends.

  * **Equal Distribution Regardless of Location** : Maglev treats all backends in its pool as equal targets. If you have backends spread across different zones, traffic will be distributed evenly among all of them. The algorithm **does not** prefer backends in a "local" zone or account for network latency between zones.
  * **Ensure MultiZone Interconnect capacity** :As backends can span across Multiple Zones, It is essential for the network administrator to ensure that the MultiZone interconnect has sufficient network capacity to handle the Cross Zone traffic between the Load Balancer nodes and the backends.



## Limitations

  * The `BackendService` resource must not be configured with a `HealthCheck` resource for pod workloads. The `HealthCheckName` in the `BackendService` specification is optional and must be omitted when configuring a load balancer with pods.

  * A load balancer configuration can't target mixed workloads involving pods and VMs. Therefore, mixed backends involving pods and VMs in one `BackendService` resource is not allowed.

  * A global load balancer custom resource, such as `ForwardingRuleExternal`, `ForwardingRuleInternal`, `BackendService`, or `HealthCheck`, must not have the same name as these zonal load balancer custom resources.

  * An organization can define a maximum of 500 forwarding rules per zone in which it resides. Global forwarding rules count toward this limit for all zones.




### Limitations for standard clusters

The following limitations apply to load balancing for standard clusters:

#### Single cluster scope

  * **Single cluster scope:** Any Load Balancer (ILB or ELB) provisioned for a standard cluster using a `Service type=LoadBalancer` resource must target backend endpoints that are pods located exclusively within that single standard cluster. A single Load Balancer definition that attempts to distribute traffic to pods running across multiple different standard clusters, or across a mix of standard clusters and shared clusters, is not supported.

  * **The[gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) and the [Networking Kubernetes Resource Model API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview) are not supported for standard clusters.** Use the standard Kubernetes `Service` resource with `type=LoadBalancer` and associated annotations to manage load balancing for standard clusters.

  * **Project-scoped load balancers will ignore standard clusters.** If a project-scoped load balancer configuration is created using the [ gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) command or the [Networking Kubernetes Resource Model API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview), it will ignore any standard clusters in the project.

  * **Global load balancing not supported.** The ILB and ELB resources provisioned for standard clusters are zonal resources scoped to a single zone. Global load balancing is not supported for standard cluster load balancers.

  * **Cross-zone ILB connectivity not supported.** Connectivity from a standard cluster pod to a global ILB or a zonal ILB in a different zone is not supported.




## What's next

  * [Configure internal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service)
  * [Configure external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
