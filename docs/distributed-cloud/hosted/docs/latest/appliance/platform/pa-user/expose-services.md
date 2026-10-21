---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/expose-services/
title: Manage load balancers \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:12.278419+00:00
---

# Manage load balancers  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/expose-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage load balancers Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance provides load balancers that enable applications to expose services to one another. Load balancers allocate a stable virtual IP (VIP) address that balances traffic over a set of backend workloads. Load balancers in GDC perform layer four (L4) load balancing, which means they map a set of configured frontend TCP or UDP ports to corresponding backend ports. Load balancers are configured at the project level.

Load balancers are configured for the following workload types:

  * Workloads running on VMs.
  * Containerized workloads inside the Kubernetes cluster.



There are three ways to configure load balancers in GDC:

  * Use the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/networking/networking-api-overview). You can use this API to create load balancers.
  * Use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). You can use this API to create load balancers.
  * Use the Kubernetes Service directly from the Kubernetes cluster. This method only creates zonal load balancers.



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
    * One cluster backend resource per cluster. This cannot be mixed with the project backends.
  * **Backends** : a zonal object that specifies the endpoints that serve as the backends for the created backend services. Backend resources must be scoped to a zone. Select endpoints using labels. Scope the selector to a project or cluster:

    * A project backend is is a backend that does not have the `ClusterName` field specified. In this case the specified labels apply to all of the workloads in the specific project, in the specific VPC of a zone. The labels are applied to VM and pod workloads across multiple clusters. When a backend service uses a project backend, you can't reference another backend for that zone in that backend service.

    * A cluster backend is a backend that has the `ClusterName` field specified. In this case, the specified labels apply to all the workloads in the named cluster in the specified project. You can specify, at most, one backend per zone per cluster in a single backend service.

  * **Health checks** : specify the probes to determine whether a given workload endpoint in the backend is healthy. The unhealthy endpoint is taken out from the load balancer, until it becomes healthy again. Health checks are only applicable to VM workloads. Pod workloads can use the built-in Kubernetes probe mechanism to determine if a specific endpoint is healthy.




When using the Kubernetes Service directly, you use the `Service` object instead of the previously listed components. You can only target workloads in the cluster where the `Service` object is created.

## External and internal load balancing

GDC applications have access to the following networking service types:

  * **Internal Load Balancer (ILB)** : lets you expose a service to other clusters within the organization.
  * **External Load Balancer (ELB)** : allocates a VIP address from a range that is routable from external workloads and exposes services outside of the GDC organization, such as other organizations inside or outside of the GDC instance.



## Service virtual IP addresses

ILBs allocate VIP addresses that are internal only to the organization. These VIP addresses are not reachable from outside the organization; therefore, you can only use them to expose services to other applications within an organization. These IP addresses may overlap between organizations in the same instance.

On the other hand, ELBs allocate VIP addresses that are externally reachable from outside the organization. For this reason, ELB VIP addresses must be unique among all organizations. Typically, fewer ELB VIP addresses will be available for use by the organization.

## What's next

  * [Configure internal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/ilb-service)
  * [Configure external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/elb-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
