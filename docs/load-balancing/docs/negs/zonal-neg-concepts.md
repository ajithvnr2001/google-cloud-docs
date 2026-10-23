---
url: https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts/
title: Zonal network endpoint groups overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:45.909330+00:00
---

# Zonal network endpoint groups overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Zonal network endpoint groups overview Stay organized with collections  Save and categorize content based on your preferences. 

A network endpoint group (NEG) is a collection of network endpoints. Every endpoint in a NEG must point to a unique IP address of a VM's network interface. A network endpoint belongs to exactly one network endpoint group. A single IP address _cannot_ be referenced by more than one endpoint in a NEG. However, a single IP address can be referenced by endpoints in different NEGs. The following diagram presents a stylized representation of this concept. In the diagram, "IP address - 2" and "IP address - 3" are referenced by network endpoints that are located in different network endpoint groups.

[ ![A network endpoint group is a collection of network endpoints.](https://docs.cloud.google.com/static/load-balancing/images/zonal-negs.svg)](https://docs.cloud.google.com/static/load-balancing/images/zonal-negs.svg) Network endpoint group (click to enlarge).

Zonal NEGs are [zonal](https://docs.cloud.google.com/compute/docs/regions-zones) resources that represent collections of either IP addresses or IP address and port combinations for Google Cloud resources within a single VPC subnet. Zonal NEGs let you do the following:

  * Route packets to any network interface of a VM instance, including interfaces other than `nic0`. This lets you create logical groupings of IP addresses and ports representing software services instead of entire VMs.

  * Create a flexible set of IP addresses where an IP address can be attached to multiple NEGs, where each NEG can have different but possibly overlapping set of IP addresses.




There are two types of zonal NEGs, depending on the type of network endpoints that make up the NEG. The two types of zonal NEGs support different use cases and load balancer types.

  * Zonal NEGs with `GCE_VM_IP` endpoints are supported as backends for the following load balancers:

    * [Global external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture)
    * [Regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
    * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)
  * Zonal NEGs with `GCE_VM_IP_PORT` endpoints are supported as backends for the following proxy-based load balancers:

    * [External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)
    * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
    * [External proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)
    * [Internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)



## NEGs with `GCE_VM_IP` endpoints

These zonal NEGs contain one or more `GCE_VM_IP` endpoints with each endpoint having one of the following IP addresses:

  * The primary internal IPv4 address of a Compute Engine VM's network interface.
  * The first IPv6 address (`/128`) from a `/96` range assigned to a Compute Engine VM's network interface.



With a `GCE_VM_IP` endpoint, you select the primary internal IPv4 address or the first IPv6 address of a network interface, which provides a level of granularity similar to selecting a network interface directly.

A `GCE_VM_IP` endpoint can't point to an IP address from an [alias IPv4 range](https://docs.cloud.google.com/vpc/docs/alias-ip). The network interface referenced by the `GCE_VM_IP` endpoint must be in the same subnet as the NEG.

As depicted in the following table, `GCE_VM_IP` endpoints can reference a [VM's network interface whose stack type can be IPv4-only, IPv6-only, or dual-stack](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types). You _cannot_ add an endpoint that is simultaneously IPv4 and IPv6 (a dual-stack endpoint) to a `GCE_VM_IP` zonal NEG. In other words, you can only use a single IP address when creating a `GCE_VM_IP` endpoint.

Network endpoint | Compatible VM network interface  
---|---  
IPv4 endpoint (primary) | IPv4-only interface  
IPv4 endpoint (primary) | Dual-stack interface  
IPv6 endpoint (first in range) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | IPv6-only interface  
IPv6 endpoint (first in range) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | Dual-stack interface  
  
Because a `GCE_VM_IP` endpoint identifies a network interface, you _cannot_ specify a port with a `GCE_VM_IP` endpoint.

These types of endpoints can only be used as backends in [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) for internal passthrough Network Load Balancers and regional external passthrough Network Load Balancers.

## NEGs with `GCE_VM_IP_PORT` endpoints

These zonal NEGs contain one or more `GCE_VM_IP_PORT` endpoints with each endpoint having one of the following IP address combinations along with the destination port:

  * **Primary IPv4 address + port** : the primary internal IPv4 address of a VM network interface plus a destination port number

  * **Alias IPv4 address + port** : an internal IPv4 address from the alias IP address range assigned to a VM network interface plus a destination port number

  * **Primary IPv4 address + any IPv6 address + port** : the primary internal IPv4 address of a VM network interface and any IPv6 address (`/128`) from a `/96` range assigned to a VM network interface plus a destination port number

  * **Alias IPv4 address + any IPv6 address + port** : an internal IPv4 address from the alias IP address range assigned to a VM network interface and any IPv6 address (`/128`) from a `/96` range assigned to a VM network interface plus a destination port number

  * **IPv6 address + port** : any IPv6 address (`/128`) from a `/96` range assigned to a VM network interface plus a destination port number




Compared to a `GCE_VM_IP` endpoint, with a `GCE_VM_IP_PORT` endpoint you can select not only the primary IP address of a network interface but any IP address, so the level of granularity that a `GCE_VM_IP_PORT` endpoint provides is greater than just selecting a network interface.

The network interface referenced by the `GCE_VM_IP_PORT` endpoint must be in the same subnet as the NEG. When you omit a port number from a `GCE_VM_IP_PORT` endpoint, Google Cloud uses the NEG's default port number for the endpoint.

As depicted in the following table, `GCE_VM_IP_PORT` endpoints can reference a [VM's network interface whose stack type can be IPv4-only, IPv6-only, or dual-stack](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types).

Network endpoint | Compatible VM network interface  
---|---  
IPv4 endpoint (primary or alias) | IPv4-only interface  
IPv4 endpoint (primary or alias) | Dual-stack interface  
IPv6 endpoint (any from a `/96` range) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | IPv6-only interface  
IPv6 endpoint (any from a `/96` range) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | Dual-stack interface  
IPv4 (primary or alias) and IPv6 (any from a `/96` range) endpoint Also referred to as a dual-stack endpoint | Dual-stack interface  
  
Because these zonal NEG backends let you specify IP addresses and ports, you can distribute traffic in a granular fashion among applications or containers running _within_ VM instances—container-native load balancing. GKE uses `GCE_VM_IP_PORT` endpoints for:

  * [GKE Ingress for Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress)
  * [Kubernetes Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)



You can create self-managed load balancers that use zonal NEGs whose `GCE_VM_IP_PORT` endpoints are managed by GKE. For more information, see [Container-native load balancing through standalone zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).

Application Load Balancers and proxy Network Load Balancers support zonal NEGs with `GCE_VM_IP_PORT` endpoints.

## Endpoint specifications

When you [create a NEG](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs), you select a zone, a network, and a subnet.

If the network you select is an [auto mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges), you can omit specifying the subnet. However, _a subnet is still associated with the zonal NEG._ If you specify an auto mode VPC network but don't specify a subnet when creating a zonal NEG, the subnet it uses is the automatically created subnet in the region that contains the zone that you selected for the zonal NEG.

When you add an endpoint to a NEG, the corresponding instance network interface must reside in the NEG's subnet. If you specify only the instance name, the system automatically selects the instance's interface in that subnet. If you also specify an IP address, it must belong to that specific interface. For multi-NIC instances, you must use a NEG associated with the subnet of the interface through which you want to receive traffic. In all cases, the attachment succeeds only if the interface in the NEG's subnet is a [load balancer target interface](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#load-balancers).

The type of zonal NEG you create is specified when you create the NEG (either `GCE_VM_IP` or `GCE_VM_IP_PORT`). This determines what types of endpoints the NEG supports.

### `GCE_VM_IP` zonal NEGs

Within a given NEG, each `GCE_VM_IP` endpoint actually represents a network interface.

The following must be true for `GCE_VM_IP` zonal NEGs:

  * You must specify the VM name for each endpoint.

  * Each endpoint VM must be located in the same zone as the NEG.

  * Every endpoint in a `GCE_VM_IP` NEG must be a unique IP address. A unique endpoint IP address can be referenced by more than one NEG.

  * Each `GCE_VM_IP` NEG is always associated with a network and a subnetwork. The IP address from any network interface of a multi-NIC VM instance can be added to a NEG as long as it is in the same subnet as the NEG.

  * Each NEG supports up to the [maximum number of endpoints per NEG](https://docs.cloud.google.com/load-balancing/docs/quotas#endpoints_per_neg). The endpoints must be distributed among all unique VMs. Multiple endpoints can't be located on a single VM because a VM can't have more than one network interface associated with the same subnet.




When adding an endpoint for a `GCE_VM_IP` NEG, you can choose whether to specify the IP address or not:

  * If the IP address is specified, it must be set to the primary internal IPv4 address or the first IPv6 address (`/128`) of the VM's network interface.

  * If you omit the IP address, the IP address is selected based on the network interface that is in the NEG's subnet. If the endpoint references an IPv4-only or a dual-stack network interface, the primary internal IPv4 address of the VM's network interface is selected as the endpoint IP address. If the endpoint references an IPv6-only network interface, the first IPv6 address (`/128`) of the VM's network interface is selected as the endpoint IP address.

Note that specifying an IP address is redundant because there can only be a single network interface that is in the subnet associated with the NEG.




### `GCE_VM_IP_PORT` zonal NEGs

Within a given NEG, each `GCE_VM_IP_PORT` endpoint can represent not only the primary IP address of a network interface but any IP address of a network interface.

The following must be true for `GCE_VM_IP_PORT` zonal NEGs:

  * You must specify the VM name for each endpoint.

  * Each endpoint VM must be located in the same zone as the NEG.

  * Every endpoint in the NEG must be a unique IP address and port combination. A unique endpoint IP address and port combination can be referenced by more than one NEG.

  * Each endpoint VM must have a network interface in the same VPC network as the NEG. Endpoint IP addresses must be associated with the same subnet specified as the NEG.

  * Each NEG supports up to the [maximum number of endpoints per NEG](https://docs.cloud.google.com/load-balancing/docs/quotas#endpoints_per_neg). The endpoints can be distributed among that many unique VMs or all located on one VM.




When adding an endpoint for a `GCE_VM_IP_PORT` NEG, you can choose to specify an IP address and port, just an IP address, or neither:

  * If you specify an IP address and port, the IP address can be an IPv4 address, an IPv6 address, or both an IPv4 and IPv6 address. The port used is of your choice. The different combinations of IP addresses and ports are outlined in the NEGs with `GCE_VM_IP_PORT` endpoints section of this document.

The IPv4 address can be the primary internal or an internal IPv4 address from the alias IP address range on the network interface. The IPv6 address can be any IPv6 address (`/128`) from a `/96` range assigned to a VM network interface. The port used is of your choice.

  * If you specify just an IP address, the IP address can be an IPv4 address, an IPv6 address, or both an IPv4 and IPv6 address. The port used is the NEG's default port number for the endpoint.

The IPv4 address can be the primary internal or an internal IPv4 address from the alias IP address range on the network interface. The IPv6 address can be any IPv6 address (`/128`) address from a `/96` range assigned to a VM network interface. The port used is the NEG's default port number for the endpoint.

  * If you omit both the IP address and port, the IP address is selected based on the network interface that is in the NEG's subnet. If the endpoint references an IPv4-only or a dual-stack network interface, the primary internal IPv4 address of the VM's network interface is selected as the endpoint IP address. If the endpoint references an IPv6-only network interface, the first IPv6 address (`/128`) of the VM's network interface is selected as the endpoint IP address.

For the port, Google Cloud uses the NEG's default port number for the endpoint.




## Load balancing with zonal NEGs

Zonal NEGs can be used as backends for [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) in a load balancer. When you use a zonal NEG as a backend for a backend service, all other backends in that backend service must also be zonal NEGs of the same type (either all `GCE_VM_IP` or `GCE_VM_IP_PORT`). You cannot use instance groups and zonal NEGs as backends in the same backend service.

You can add the same network endpoint to more than one zonal NEG. You can also use the same zonal NEG as a backend for more than one backend service.

Zonal NEGs with `GCE_VM_IP_PORT` endpoints are used by proxy-based load balancers with the balancing modes as defined in [Balancing modes for Application Load Balancers and Cloud Service Mesh](https://docs.cloud.google.com/load-balancing/docs/backend-service#applb-csm) and [Balancing modes for Proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/backend-service#proxy-net-lb).

Zonal NEGs with `GCE_VM_IP` endpoints are used by passthrough load balancers, with the balancing modes as defined in [Balancing modes for passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/backend-service#pass-net-lb).

### Passthrough Network Load Balancers

See the following sections for the primary use-cases for NEGs with `GCE_VM_IP` endpoints.

#### Flexible endpoint grouping

Like instance groups, you can use the same NEG as a backend for multiple passthrough Network Load Balancers. Unlike instance groups, a NEG endpoint can be a member of multiple NEGs, and each of those NEGs can be used as a backend for one or more passthrough Network Load Balancers. Compared to instance groups, you aren't constrained by the fact that a VM instance can only be a part of a single instance group.

The following figure shows a sample internal passthrough Network Load Balancer architecture with a shared VM.

[ ![Internal passthrough Network Load Balancers with overlapping `GCE_VM_IP` zonal NEGs.](https://docs.cloud.google.com/static/load-balancing/images/l4ilb-zonal-neg-overlap.svg)](https://docs.cloud.google.com/static/load-balancing/images/l4ilb-zonal-neg-overlap.svg) Internal passthrough Network Load Balancers with overlapping zonal NEGs (click to enlarge).

#### Non-`nic0` interfaces as backend endpoints

Zonal NEGs allow load balancing to non-`nic0` network interfaces of VMs. This can be useful when integrating with third-party appliance VMs that typically reserve `nic0` for management operations. Non-`nic0` network interfaces can also be attached to a NEG backend of a passthrough Network Load Balancer. However, for multi-NIC instances, only [load balancer target interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#load-balancers) can be attached to a NEG backend.

For more information, see the following documents:

  * [Zonal NEG backends and network interfaces for global external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#neg-nic-net)

  * [Zonal NEG backends and network interfaces for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#neg-nic-net)

  * [Zonal NEG backends and network interfaces for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal#neg-nic-net)




#### GKE subsetting

GKE uses `GCE_VM_IP` zonal NEGs and _subsetting_ to improve the scalability of internal passthrough Network Load Balancers in the following way:

Without subsetting, GKE creates one unmanaged instance group per zone, consisting of the cluster's nodes from all node pools in that zone. These zonal instance groups are used as backends for one or more internal LoadBalancer Services (and for external Ingresses that don't use NEGs themselves).

With subsetting, GKE creates `GCE_VM_IP` zonal NEGs for each internal LoadBalancer Service. The same endpoint can be a member of more than one zonal NEG. Unlike instance groups, Google Cloud can load balance to more multiple zonal NEGs that contain the same endpoint.

Subsetting more efficiently distributes traffic to internal LoadBalancer Services in clusters with more than 250 nodes. For example, a 300-node GKE cluster might have one internal LoadBalancer Service with 25 nodes in a NEG because there are 25 serving Pods for that Service. Not all 300 nodes need to be added to an instance group backend for this Service.

Note that quotas for NEGs, forwarding rules, backend services, and other [Google Cloud networking resources](https://docs.cloud.google.com/load-balancing/docs/quotas) still apply.

For more details, see [Using internal passthrough Network Load Balancer subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#subsetting).

### Application Load Balancers and proxy Network Load Balancers

The following illustrations show configuration components for load balancers where zonal NEGs with `GCE_VM_IP_PORT` endpoints are the backends:

[ ![Zonal network endpoint groups in load balancing.](https://docs.cloud.google.com/static/load-balancing/images/neg-lb-over.svg)](https://docs.cloud.google.com/static/load-balancing/images/neg-lb-over.svg) Zonal network endpoint groups in load balancing (click to enlarge).

To learn more about the architectural requirements of these load balancers, see:

  * [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp)
  * [Internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)



The primary use case for `GCE_VM_IP_PORT` zonal NEGs is container-native load balancing so that you can distribute traffic directly to containers running on VMs—for example, to Pod IP addresses in GKE clusters.

[Container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing) enables load balancers to target Pods directly and to make load distribution decisions at the Pod-level instead of at the VM-level.

The following example demonstrates how load balancers distribute traffic among microservices running in containers on your VMs. The VMs are configured to use alias IP ranges from their subnets, and those ranges are the addresses used by the containers.

[ ![Load balancing zonal network endpoint groups with containers.](https://docs.cloud.google.com/static/load-balancing/images/neg-container.svg)](https://docs.cloud.google.com/static/load-balancing/images/neg-container.svg) Load balancing zonal network endpoint groups with containers (click to enlarge).

There are two ways to configure container-native load balancing: either use NEGs managed by GKE Ingress, or use standalone NEGs.

  * **Kubernetes Ingress with NEGs (Recommended)**

When NEGs are used with Ingress, the Ingress controller facilitates the creation of all aspects of an HTTP(S) load balancer. This includes creating the virtual IP address, forwarding rules, health checks, firewall rules, and more. To learn how to configure this, see [Container-native load balancing through Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing).

Ingress is the recommended way to use NEGs for container-native load balancing as it has many features that simplify the management of NEGs. Alternatively, you can create a proxy load balancer manually but still have GKE manage NEG endpoint membership, as described in the next point (Standalone NEGs).

For instructions about how to set up a load balancer through Ingress, see [Container-native load balancing through Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing).

  * **Standalone NEGs**

Standalone NEGs provide a way for your GKE cluster to create zonal NEGs with `GCE_VM_IP_PORT` endpoints representing Pod IP addresses and container ports, while giving you the flexibility to configure the load balancer components outside of GKE.

For examples on using standalone zonal NEGs with GKE, see:

    * [Attach an external Application Load Balancer to standalone zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg#attaching-ext-https-lb)
    * [Attach an internal Application Load Balancer to standalone zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg#attaching-int-https-lb)



## Limitations

  * You cannot use zonal NEGs with legacy networks.
  * A backend service that uses NEGs as backends cannot also use instance groups as backends.
  * An instance with multiple network interfaces attached to the same VPC network can be added as an endpoint to a zonal NEG. However, from the set of network interfaces that are attached to the same VPC network, only the network interface that meets [the conditions for receiving load-balanced traffic](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#load-balancers) can be referenced by the endpoint.
  * The [`default-port` property](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create) is not supported for `GCE_VM_IP` zonal NEGs.



## Quotas

  * For information about NEG quotas—such as NEGs per project, NEGs per backend service, and endpoints per NEG—see the [load balancing quotas page](https://docs.cloud.google.com/load-balancing/docs/quotas).



## What's next

  * For information about configuring zonal NEGs, see [Set up zonal network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs).
  * For information about using zonal NEGs in Google Kubernetes Engine, see [Container-native load balancing through Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
