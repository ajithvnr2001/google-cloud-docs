---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking/
title: Best practices for GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:18.721107+00:00
---

# Best practices for GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Best practices for GKE networking Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document outlines the best practices for configuring networking options for Google Kubernetes Engine (GKE) clusters. It's intended to be an architecture planning guide for cloud architects and network engineers with cluster configuration recommendations that are applicable to most GKE clusters. Before you create your GKE clusters, we recommend that you review all the sections on this page to understand the networking options that GKE supports and their implications.

The networking options that you choose impact the architecture of your GKE clusters. Some of these options can't be changed once configured without recreating the cluster.

Before reading this page, make sure that you're familiar with Kubernetes networking concepts and terminology, some level of general networking concepts, and Kubernetes networking. For more information, see the [ GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).

While reviewing these best practices, consider the following:

  * How you plan to expose workloads internally to your Virtual Private Cloud (VPC) network, other workloads in the cluster, other GKE clusters, or externally to the internet.
  * How you plan to scale your workloads.
  * What types of Google services you want to consume.



For a summarized checklist of all the best practices, see the Checklist summary.

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## VPC design best practices

When designing your VPC networks, follow [best practices for VPC design](https://docs.cloud.google.com/solutions/best-practices-vpc-design).

The following section provides some GKE-specific recommendations for VPC network design.

**Best practices** :

Use VPC-native clusters.  
Use Shared VPC networks.  


### Use VPC-native clusters

We recommend using [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips). VPC-native clusters use [alias IP address ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) on GKE nodes and are required for clusters based on VPC Network Peering, for clusters on [Shared VPCs](https://docs.cloud.google.com/vpc/docs/shared-vpc), and have many [other benefits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#benefits). For clusters created in the [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) mode, VPC-native mode is always on and can't be turned off.

VPC-native clusters scale more easily than routes-based clusters without consuming Google Cloud routes, so they are less susceptible to hitting routing limits.

The [advantages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#benefits) to using VPC-native clusters go hand-in-hand with [alias IP support](https://docs.cloud.google.com/vpc/docs/alias-ip#key_benefits_of_alias_ip_ranges). For example, [network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs) (NEGs) can only be used with secondary IP addresses, so they are only supported on VPC-native clusters.

### Use Shared VPC networks

GKE clusters require careful [IP address planning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#defaults_limits). Most organizations have a centralized management structure with a network administration team who can allocate IP address space for clusters and a platform administrator for operating the clusters. This type of organization structure works well with Google Cloud's Shared VPC network architecture. In the Shared VPC network architecture, a network administrator can create subnets and share them with VPCs. You can create GKE clusters in a [service project](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc) and use the subnets shared from the Shared VPC on the [host project](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc). The IP address component stays in the host project, and your other cluster components live in the service project.

In general, a Shared VPC network is a frequently used architecture that's suitable for most organizations with a centralized management team. We recommend using Shared VPC networks to create the subnets for your GKE clusters and to avoid IP address conflicts across your organization. You might also want to use Shared VPCs for governance of operational functions. For example, you can have a network team that works only on network components and reliability, and another team that works on GKE.

## IP address management strategies

All Kubernetes clusters, including GKE clusters, require a unique IP address for every Pod. To learn more, see the [GKE networking model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-compare-network-models#gke-networking-model).

In GKE, all these IP addresses are routable throughout the VPC network. Therefore, IP address planning is necessary because addresses can't overlap with internal IP address space used on-premises or in other connected environments. The following sections suggest strategies for IP address management with GKE.

**Best practices** :

Plan the required IP address allotment.  
Use non-RFC 1918 space if needed.  
Use custom subnet mode.  
Plan Pod density per node.  
Avoid overlaps with IP addresses used in other environments.  
Create a load balancer subnet.  
Reserve enough IP address space for cluster autoscaler.  
Share IP addresses across clusters.  
Share IP addresses for internal LoadBalancer Services.  


### Plan the required IP address allotment

We recommend using VPC-native clusters with [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#clusters-private-service-connect) (PSC). Clusters that use VPC Network Peering must be VPC-native clusters.

VPC-native clusters require the following IP address ranges:

  * Control plane IP address range: use a /28 subnet within the IP address private ranges included on the [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918). You must make sure that this subnet doesn't overlap any other classless inter-domain routing (CIDR) in the VPC network.
  * Node subnet: the subnet with the primary IP address range that you want to allocate for all the nodes in your cluster. Services with the type `LoadBalancer` that use the `cloud.google.com/load-balancer-type: "Internal"` annotation also use this subnet by default. You can also use a dedicated [subnet for internal load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).
  * Pod IP address range: the IP range that you allocate for all Pods in your cluster. GKE provisions this range as an alias of the subnet. For more information, see [IP address ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing)
  * Service IP address range: the IP address range that you allocate for all Services in your cluster. GKE provisions this range as an alias of the subnet.



When configuring cluster networking, you must define a node subnet, a Pod IP address range, and a Service IP address range.

If you want to use IP address space more efficiently, see [Reduce internal IP address usage in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies#reduce-private-ip-address-usage-in-gke).

The control plane IP address range is dedicated to the GKE-managed control plane that resides in a Google-managed tenant project peered with your VPC. This IP address range shouldn't overlap with any IP addresses in your VPC peering group because GKE imports this route into your project. This means that if you have any routes to the same CIDR in your project, you might experience routing issues.

When creating a cluster, the subnet has a primary range for the nodes of the cluster and it should exist before cluster creation. The subnet should accommodate the [maximum number of nodes that you expect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_primary_range) in the cluster and the internal load balancer IP addresses across the cluster using the subnet.

You can use the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to limit the maximum number of nodes.

The Pod and service IP address ranges are represented as distinct secondary ranges of your subnet, implemented as alias IP addresses in VPC-native clusters.

Choose wide enough IP address ranges so that you can [accommodate all nodes, Pods, and Services for the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#defaults_limits).

Consider the following limitations:

  * You can [expand primary IP address ranges](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet) but you can't shrink them. These IP address ranges can't be discontiguous.
  * You can [expand the Pod range](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr) by appending additional Pod ranges to the cluster or creating new node pools with other secondary Pod ranges.
  * The secondary IP address range for Services can't be expanded or changed over the life of the cluster.
  * Review the limitations for the [secondary IP address range for Pods and Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#node_limiters).



### Use more than private RFC 1918 IP addresses

For some environments, RFC 1918 space in large contiguous CIDR blocks might already be allocated in an organization. You can use [non-RFC 1918 space](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_reserved_ip_ranges) for additional CIDRs for GKE clusters, if they don't overlap with Google-owned public IP addresses. We recommend using the 100.64.0.0/10 part of the [RFC](https://tools.ietf.org/html/rfc6598) address space because [Class E](https://tools.ietf.org/html/rfc5735) address space can present interoperability issues with on-premises hardware. You can use privately reused public IPs ([PUPI](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_pupis)).

When using [privately used public IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/archive/configuring-privately-used-public-ips-for-GKE), use with caution and consider controlling route advertisements in on-premises networks to the internet when choosing this option.

You shouldn't use [source network address translation (SNAT)](https://cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create#--disable-default-snat) in a cluster with Pod-to-Pod and Pod-to-Service traffic. This breaks the [Kubernetes networking model](https://kubernetes.io/docs/concepts/services-networking/).

Kubernetes assumes that all non-RFC 1918 IP addresses are privately reused public IP addresses and uses SNAT for all traffic originating from these addresses.

If you're using a non-RFC 1918 IP address for your GKE cluster, for Standard clusters, you will need to either [explicitly disable SNAT](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create#--disable-default-snat) or [configure the IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#how_ipmasq_works) to exclude your cluster's Pod IP addresses and the secondary IP address ranges for Services from SNAT. For Autopilot clusters, this doesn't require any extra steps.

### Use custom subnet mode

When you set up the network, you also select the subnet mode: `auto` (default) or `custom` (recommended). The `auto` mode leaves the subnet allocation up to Google and is a good option to get started without IP address planning. However, we recommend selecting the `custom` mode because this mode lets you choose IP address ranges that don't overlap other ranges in your environment. If you're using a Shared VPC, either an organizational administrator or network administrator can select this mode.

The following example creates a network called `my-net-1` with custom subnet mode:
    
    
    gcloud compute networks create my-net-1 --subnet-mode custom
    

### Plan Pod density per node

By default, Standard clusters reserve a /24 range for every node out of the Pod address space in the subnet and allows for up to [110 Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_secondary_range_pods). However, you can configure a Standard cluster to support up to 512 Pods per node, with a /22 range reserved for every node. Depending on the size of your nodes and the application profile of your Pods, you might run considerably fewer Pods on each node.

If you don't expect to run more than 64 Pods per node, we recommend [adjusting the maximum Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr) to preserve IP address space in your Pod subnet.

If you expect to run more than the default 110 Pods per node, you can increase the maximum Pods per node up to 512, with /22 reserved for every node. With this type of high Pod density configuration, we recommend using instances with 16 or more CPU cores to ensure the scalability and performance of your cluster.

For [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters, the maximum number of Pods per node is dynamically set up to 256 (reserving up to a /23 range per node). You can't configure this setting in Autopilot clusters.

### Avoid overlaps with IP addresses used in other environments

You can connect your VPC network to an on-premises environment or other cloud service providers through [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect). These environments can share routes, making the on-premises IP address management scheme important in IP address planning for GKE. We recommend making sure that the IP addresses don't overlap with the IP addresses used in other environments.

### Create a load balancer subnet

Create a separate [load balancer subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing) to expose services with internal TCP/UDP load balancing. If a separate load balancer subnet isn't used, these services are exposed by using an IP address from the node subnet, which can lead to the use of all allocated space in that subnet earlier than expected and can stop you from scaling your GKE cluster to the expected number of nodes.

Using a separate load balancer subnet also means that you can filter traffic to and from the GKE nodes separately to services that are exposed by internal TCP/UDP load balancing, which lets you set stricter security boundaries.

### Reserve enough IP address space for cluster autoscaler

**Note:** For [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters, Google dynamically provisions resources based on your Pod specification. The recommendations in this section can still be applied to Autopilot clusters.

You can use the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to dynamically add and remove nodes in the cluster so that you can control costs and improve utilization. However, when you're using the cluster autoscaler, make sure that your IP address planning accounts for the maximum size of all node pools. Each new node requires its own node IP address as well as its own allocatable set of Pod IP addresses based on the configured Pods per node. The number of Pods per node can be configured differently than what is configured at the cluster level. You can't change the number of Pods per node after you create the cluster or node pool. You should consider your workload types and assign them to distinct node pools for optimal IP address allocation.

Consider using [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning), with the cluster autoscaler, particularly if you're using VPC-native clusters. For more information, see [Node limiting ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#node_limiters).

### Share IP addresses across clusters

You might need to share IP addresses across clusters if you have a centralized team that's managing the infrastructure for clusters. To share IP addresses across GKE clusters, see [Sharing IP address ranges across GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#sharing_ip_address). You can reduce IP exhaustion by creating three ranges, for Pods, Services and nodes, and reusing or sharing them, especially in a Shared VPC model. This setup can also make it easier for network administrators to manage IP addresses by not requiring them to create specific subnets for each cluster.

Consider the following:

  * As a best practice, use separate subnets and IP address ranges for all clusters.
  * You can share the secondary Pod IP address range, but it isn't recommended because one cluster might use all of the IP addresses.
  * You can share secondary Service IP address ranges, but this feature doesn't work with [VPC-scope Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#vpc_scope_dns).



If you run out of IP addresses, you can create additional Pod IP address ranges using [discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).

### Share IP addresses for internal LoadBalancer Services

You can share a single IP address with up to 50 backends using different ports. This lets you reduce the number of IP addresses you need for internal LoadBalancer Services.

For more information, see [Shared IP](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#shared_VIP).

## Network security best practices

A few key recommendations are outlined in this section for cluster isolation. Network security for GKE clusters is a shared responsibility between Google and your cluster administrator(s).

**Best practices** :

Use GKE Dataplane V2.  
Minimize node exposure.  
Minimize the cluster control plane exposure.  
Authorize access to the control plane.  
Allow control plane connectivity.  
Deploy proxies for control plane access from peered networks.  
Restrict cluster traffic using network policies.  
Enable Google Cloud Armor security policies for Ingress.  
Use Identity-Aware Proxy to provide authentication for applications with IAM users.  
Use organization policy constraints to further enhance security.  


### Use GKE Dataplane V2

[GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) is based on [eBPF](https://ebpf.io/) and provides an integrated network security and visibility experience. When you create a cluster using GKE Dataplane V2 you don't need to explicitly enable network policies because GKE Dataplane V2 manages service routing, network policy enforcement and logging. Enable the new dataplane with the Google Cloud CLI `--enable-dataplane-v2` option when creating a cluster. After network policies are configured, a default `NetworkLogging` CRD object can be [configured](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging#configuring_network_policy_logging) to log allowed and denied network connections. We recommend creating clusters with GKE Dataplane V2 to take full advantage of the built-in features such as [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging).

### Minimize the node exposure

In a cluster with private nodes only, Pods are isolated from inbound and outbound communication (the cluster perimeter). You can control these directional flows by exposing services by using load balancing and Cloud NAT, discussed in the cluster connectivity section in this document. The following diagram shows this kind of setup:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/bp_networking_privatecluster.svg)**Diagram 1:** Private nodes communication

This diagram shows how a cluster with private nodes can communicate. On-premises clients can connect to the cluster with the kubectl client. Access to Google Services is provided through Private Google Access, and communication to the internet is available only by using Cloud NAT.

### Minimize the cluster control plane exposure

The control plane has two types of endpoints for cluster access:

  * DNS-based endpoint
  * IP-based endpoints

**Best practice** : 

Use only the DNS-based endpoint to access your control plane for simplified configuration and a flexible and policy-based layer of security.

The DNS endpoint is accessible from any network reachable by Google Cloud APIs, including on-premises or other cloud networks. To enable the DNS-based endpoint, use the `--enable-dns-access` flag.

The GKE API server can also be exposed as a public or a private IP-based endpoint. You can decide which endpoint to use when you create the cluster. You can control access with [authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks), where both the public and private endpoints default to allowing all communication between the Pod and the node IP addresses in the cluster. To enable a private endpoint when you create a cluster, use the [`--enable-private-endpoint`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-private-endpoint) flag.

### Authorize access to the control plane

Authorized networks can help dictate which IP address subnets can access the GKE control plane nodes. After enabling these networks, you can restrict access to specific source IP address ranges. If the public endpoint is disabled, these source IP address ranges should be private. If a public endpoint is enabled, you can allow public or internal IP address ranges. Configure [custom route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) to allow the private endpoint of the cluster control plane to be reachable from an on-premises environment. You can make the private GKE API endpoint be globally reachable by using the [`--enable-master-global-access`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#create_cluster) option when you create a cluster.

**Important:** Even if you disable access to the public endpoint, Google can use the control plane's public endpoint for cluster management purposes, such as [scheduled maintenance](https://docs.cloud.google.com/kubernetes-engine/docs/scheduled-maintenance) and [automatic control plane upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades).

The following diagram shows typical control plane connectivity using authorized networks:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/bp_networking_controlplane_connectivity.svg)**Diagram 2:** Control plane connectivity using authorized networks

This diagram shows trusted users being able to communicate with the GKE control plane through the public endpoint as they are part of authorized networks, while access from untrusted actors is blocked. Communication to and from the GKE cluster happens through the private endpoint of the control plane.

### Allow control plane connectivity

Certain system Pods on every worker node will need to reach services such as the Kubernetes API server (`kube-apiserver`), Google APIs, or the metadata server. The `kube-apiserver`also needs to communicate with some system Pods, such as `event-exporter` specifically. This communication is allowed by default. If you deploy VPC firewall rules within the projects (more details in the Restrict cluster traffic section), make sure that those Pods can keep communicating to the `kube-apiserver` as well as to Google APIs.

### Deploy proxies for control plane access from peered networks

If your cluster uses [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), you can't access the cluster's control plane from another peered network.

If you want direct access from another peered network or from on-premises when using a hub-and-spoke architecture, deploy proxies for control plane traffic.

### Restrict cluster traffic using network policies

Multiple levels of network security are possible for cluster workloads that can be combined: VPC firewall rules, Hierarchical firewall policies, and Kubernetes network policies. VPC firewall rules and Hierarchical firewall policies apply at the virtual machine (VM) level, that is the worker nodes on which the Pods of the GKE cluster reside. Kubernetes network policies apply at the Pod-level to enforce Pod to Pod traffic paths.

If you implement VPC firewalls, it can break the default, required control plane communication—for example the kubelet communication with the control plane. GKE creates [required firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules) by default, but they can be overwritten. Some deployments might require the control plane to reach the cluster on the service. You can use VPC firewalls to configure an ingress policy that makes the service accessible.

GKE network policies are configured through the Kubernetes Network Policy API to enforce a cluster's Pod communication. You can enable network policies when you create a cluster by using the `gcloud container clusters create` option `--enable-network-policy`. To restrict traffic using network policies, you can follow the [Anthos restricting traffic blueprint implementation guide](https://github.com/GoogleCloudPlatform/anthos-security-blueprints/tree/master/restricting-traffic).

### Enable Google Cloud Armor security policies for Ingress

Using [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview), you can protect applications that use [external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https) from DDoS attacks and other web-based attacks by blocking such traffic at the network edge. In GKE, enable Google Cloud Armor security policies for applications by using [Ingress for external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb) and [adding a security policy to the BackendConfig](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#cloud_armor) attached to the Ingress object.

### Use Identity-Aware Proxy to provide authentication for applications with IAM users

If you want to deploy services that only users within your organization can access, without requiring them to be on the corporate network, you can use [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview) to create an authentication layer for these applications. To enable Identity-Aware Proxy for GKE, follow the [configuration steps](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto) to add Identity-Aware Proxy as part of the BackendConfig for your service Ingress. Identity-Aware Proxy can be combined with Google Cloud Armor.

### Use organization policy constraints to further enhance security

Using [organizational policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints), you can set policies to further enhance your security posture. For example, you can use constraints to [restrict Load Balancer creation to certain types](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints), such as internal load balancers only.

## Cluster connectivity scaling

This section covers scalable options for DNS and outbound connectivity from your clusters towards the internet and Google services.

**Best practices** :

Use Cloud DNS for GKE.  
Enable NodeLocal DNSCache.  
Use Cloud NAT for internet access from clusters.  
Use Private Google Access for access to Google services.  


### Use Cloud DNS for GKE

You can use [Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns) to provide Pod and Service DNS resolution with managed DNS without a cluster-hosted DNS provider. Cloud DNS removes the overhead of managing a cluster-hosted DNS server and requires no scaling, monitoring, or managing of DNS instances because it's a hosted Google service.

### Enable NodeLocal DNSCache

GKE uses `kube-dns` in order to provide the cluster's local DNS service as a default cluster add-on. `kube-dns` is replicated across the cluster as a function of the total number of cores and nodes in the cluster.

You can improve DNS performance with [NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache). NodeLocal DNSCache is an add-on that is deployed as a DaemonSet, and doesn't require any Pod configuration changes. DNS lookups to the local Pod service don't create open connections that need to be tracked on the node, which allows for greater scale. External hostname lookups are forwarded to Cloud DNS whereas all other DNS queries go to kube-dns.

[Enable NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache) for more consistent DNS query lookup times and improved cluster scale. For Autopilot clusters, NodeLocal DNSCache is enabled by default and cannot be overridden.

The following Google Cloud CLI option enables NodeLocal DNSCache when you create a cluster: `--addons NodeLocalDNS.`

If you have control over the name that applications are looking to resolve, there are ways to improve DNS scaling. For example, use an FQDN (end the hostname with a period) or disable search path expansion through the `Pod.dnsConfig` manifest option.

### Use Cloud NAT for internet access from clusters

By default, clusters with private nodes enabled don't have internet access. To allow Pods to reach the internet, enable [Cloud NAT](https://docs.cloud.google.com/nat/docs) for each region. At a minimum, enable Cloud NAT for the primary and secondary ranges in the GKE subnet. Make sure that you allocate enough [IP addresses for Cloud NAT and ports per VM](https://docs.cloud.google.com/nat/docs/ports-and-addresses#ports).

Use the following Cloud NAT Gateway configuration best practices when using Cloud NAT for clusters:

  * When you create your Cloud NAT gateway, enable it only for the subnet ranges used by your clusters. By counting all the nodes in all the clusters, you can determine how many NAT consumer VMs you have in the project.
  * [Use dynamic port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#dynamic-port) to allocate different numbers of ports per VM, based on the VM's usage. Start with minimum ports of 64 and maximum ports of 2048.

  * If you need to manage many simultaneous connections to the same destination 3-tuple, lower the TCP `TIME_WAIT` timeout from its default value of `120s` to `5s`. For more information, see [Modify NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#modify-nat-timeouts).

  * Enable [Cloud NAT error logging](https://docs.cloud.google.com/nat/docs/monitoring#configuring_logging) to check related logs.

  * Check the Cloud NAT Gateway logs after configuring the gateway. To decrease allocation status dropped problems, you might need to increase the maximum number of ports per VM.




You should avoid double SNAT for Pods traffic (SNAT first at the GKE node and then again with Cloud NAT). Unless you require SNAT to hide the Pod IP addresses towards on-premises networks connected by Cloud VPN or Cloud Interconnect, [`disable-default-snat`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-default-snat) and offload the SNAT tracking to Cloud NAT for scalability. This solution works for all primary and secondary subnet IP ranges. Use network policies to restrict external traffic after enabling Cloud NAT. Cloud NAT is not required to access Google services.

### Use Private Google Access for access to Google services

In clusters with private nodes, Pods don't have public IP addresses to reach public services, including Google APIs and services. [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) lets private Google Cloud resources reach Google services.

[Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) is enabled by default in clusters with private nodes, except for Shared VPC clusters.

## Application scaling best practices

When creating applications that are reachable either externally or internal to your organization, make sure you use the right load balancer type and options. This section provides recommendations on exposing and scaling applications with Cloud Load Balancing.

**Best practices** :

Use container-native load balancing.  
Choose the correct GKE resource to expose your application.  
Create health checks based on BackendConfig.  
Use local traffic policy to preserve original IP addresses.  
Use Private Service Connect.  


### Use container-native load balancing

Use [container-native load balancing ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing) when exposing services by using HTTP(S) externally. Container-native load balancing reduces network hops, lowers latency, and provides more exact traffic distribution. It also increases round-trip time visibility and lets you use load-balancing features such as Google Cloud Armor.

### Choose the correct GKE resource to expose your application

Depending on the scope of your clients (internal, external, or even cluster-internal), the regionality of your application, and the protocols that you use, there are different GKE resources that you can choose to use to expose your application. The [Service networking overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-networking) explains these options and can help you choose the best resource to expose each part of your application by using Google Cloud load balancing options.

### Create health checks based on BackendConfig

If you use an Ingress to expose services, use a [health check configuration in a BackendConfig CRD](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#direct_health) to use the health check functionality of the external Application Load Balancer. You can direct the health check to the appropriate endpoint and set your own thresholds. Without a BackendConfig CRD, health checks are inferred from readiness probe parameters or use default parameters.

### Use local traffic policy to preserve original IP addresses

When you use an [internal passthrough Network Load Balancer with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing), set the [`externalTrafficPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters) option to `Local` to preserve the source IP address of the requests. Use this option if your application requires the original source IP address. However, the `externalTrafficPolicy` `local` option can lead to less optimal load spreading, so only use this feature when required. For HTTP(S) services, you can use Ingress controllers and get the original IP address by reading the [`X-Forwarded-For`](https://docs.cloud.google.com/load-balancing/docs/https#target-proxies) header in the HTTP request.

### Use Private Service Connect

You can use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to share internal passthrough Network Load Balancer Services across other VPC networks. This is useful for Services that are hosted on GKE clusters but serve customers that run in different projects and different VPCs.

You can use Private Service Connect to reduce IP address consumption by providing connectivity between VPCs with overlapping IP addresses.

## Operational best practices

**Best practices** :

Use IAM for GKE permissions to control policies in Shared VPC networks.  
Use regional clusters and distribute your workloads for high availability.  
Use Cloud Logging and Cloud Monitoring and enable network policy logging.  


The following sections contain operational best practices that help you ensure granular authorization options for your workloads. To avoid creating manual firewall rules, follow the operational best practices in this section. It also includes recommendations for distributing your workloads and for monitoring and logging in GKE.

### Use IAM for GKE permissions to control policies in Shared VPC networks

When using [Shared VPC networks](https://docs.cloud.google.com/vpc/docs/shared-vpc), firewall rules for load balancers are automatically created in the host project.

To avoid having to manually create firewall rules, assign a least-privilege custom role to the GKE service account in the host project named `service-HOST_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com`.

Replace `HOST_PROJECT_NUMBER` with the project number of the host project for the Shared VPC.

The custom role that you create should have the following permissions:

  * `compute.firewalls.create`
  * `compute.firewalls.get`
  * `compute.firewalls.list`
  * `compute.firewalls.delete`



In addition, firewall rules created by GKE always have the default priority of 1000, so you can disallow specific traffic from flowing by creating firewall rules at a higher priority.

If you want to restrict creation of certain load balancer types, use [organizational policies to restrict load balancer creation](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints).

### Use regional clusters and distribute your workloads for high availability

[Regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters) can increase the availability of applications in a cluster because the cluster control plane and nodes are spread across multiple zones.

However, to have the best possible user experience in case of a zone failure, use the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to make sure that your cluster can handle the required load at any time.

You can also use [Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) to make sure that Pods of a given service are scheduled in multiple zones.

For more information about how to configure these settings for high availability and cost optimizations, see the [Best practices for highly-available GKE clusters](https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-creating-a-highly-available-gke-cluster).

**Note:** There are costs involved for cross-zone data transfers. Refer to the Intra-zone/Inter-zone data transfer section on the [VPC pricing page](https://cloud.google.com/vpc/network-pricing#virtual-private-cloud) for more information.

### Use Cloud Logging and Cloud Monitoring and enable network policy logging

While each organization has different requirements for visibility and auditing, we recommend [enabling network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging). This feature is only available with [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2). Network policy logging provides visibility into policy enforcement and Pod traffic patterns. Be aware that there are costs involved for [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging#pricing).

For GKE clusters using version 1.14 or later, [ Logging and Monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/gke) are both enabled by default. Monitoring provides a dashboard for your GKE clusters. Logging also enables GKE annotations for [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs). By default, Logging collects logs for all workloads deployed to the cluster but [a system-only logs option](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#what_logs) also exists. Use the [GKE dashboard](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/observing) to observe and set alerts. For clusters created in the Autopilot mode, monitoring and logging are automatically enabled and can't be configured.

Be aware that there are costs involved for the [Google Cloud Observability](https://cloud.google.com/stackdriver/pricing).

## Even traffic distribution best practices

This section provides recommended practices for even traffic distribution. Before implementing these, make sure that you have appropriate monitoring in place (for example, using Prometheus, Cloud Monitoring, or your cloud provider's monitoring services) to identify and confirm uneven distribution patterns.

### Disable or carefully configure session affinity

To resolve this issue, disable session affinity unless absolutely necessary. Set `sessionAffinity: None` in your Service manifest. If you must use session affinity, carefully consider the implications and monitor Pod load. Session affinity makes sure that a user stays connected to the same backend for the duration of a session.

### Use weighted load balancing

To implement this practice, configure your Service to use weighted load balancing. Weighted load balancing distributes traffic based on the number of healthy Pods per node. The load balancer sends new connections to a GKE node in proportion to the number of healthy Pods in that node. For an external passthrough Network Load Balancer in GKE, weighted load balancing allows nodes with more serving Pods to receive a larger proportion of new connections.

To enable weighted load balancing, you must meet the following requirements and configure your Service with specific annotations:

  * **GKE cluster version** : your GKE cluster must use version 1.31.0-gke.1506000 or later.
  * **HTTP Load Balancing add-on** : the `HttpLoadBalancing` add-on must be enabled for your cluster (this is enabled by default). If your cluster is on version 1.36 and later, this add-on is not a prerequisite for backend services.
  * **Backend service-based load balancer** : set the `spec.loadBalancerClass` field to `networking.gke.io/l4-regional-external` in your Service manifest to make sure that GKE creates a backend service-based external passthrough Network Load Balancer. This field requires GKE version 1.33.1-gke.1779000 or later. Target pool-based load balancers don't support weighted load balancing.
  * **Weighted load balancing annotation** : include the `networking.gke.io/weighted-load-balancing: pods-per-node` annotation in your Service manifest.
  * **External traffic policy** : the Service manifest must use `externalTrafficPolicy: Local`. While `externalTrafficPolicy: Cluster` is allowed, it effectively disables weighted load balancing as packets might be routed to a different node after the initial load balancer distribution.


  1. Save the following sample manifest as `weighted-lb-service.yaml`:


    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-weighted-service
      annotations:
        networking.gke.io/weighted-load-balancing: pods-per-node
    spec:
      type: LoadBalancer
      loadBalancerClass: networking.gke.io/l4-regional-external
      externalTrafficPolicy: Local
      selector:
        app: my-app
      ports:
        -   protocol: TCP
          port: 80
          targetPort: 8080
    

  1. Apply the manifest to your cluster:
         
         kubectl apply -f weighted-lb-service.yaml
         




This configuration avoids overloading backend instances by distributing new connections proportionally to the number of Pods on each node. It also preserves client IP address affinity and the original source IP address of the client for the application due to `externalTrafficPolicy: Local`.

### Ensure even Pod distribution across nodes

Use Pod anti-affinity to prevent Pods from the same Service from being scheduled on the same node. Define Pod anti-affinity rules in your deployment manifests.

The following example shows a Deployment manifest with Pod anti-affinity:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 6
      template:
        metadata:
          labels:
            app: my-app
        spec:
          affinity:
            podAntiAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
              -   labelSelector:
                  matchExpressions:
                  -   key: app
                    operator: In
                    values:
                    -   my-app
                topologyKey: "kubernetes.io/hostname"
    

### Review external traffic policy

Use `Cluster` as the `externalTrafficPolicy` to allow the load balancer to distribute traffic to any node in the cluster. Set `externalTrafficPolicy: Cluster` in your Service manifest. Use this setting if you need to distribute traffic evenly across all nodes.

If you use `Local`, make sure that you evenly distribute your Pods across nodes.

### Disable node affinity

Remove affinity configurations from your deployments if you experience hotspots.

### Use readiness probes

Configure readiness probes on your Pods. Define readiness probes in your Pod manifests. This makes sure that the load balancer only sends traffic to Pods that are ready to handle requests.

The following example shows a Pod manifest with a readiness probe:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-pod
    spec:
      containers:
      -   name: my-container
        image: my-image
        readinessProbe:
          httpGet:
            path: /healthz
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
    

### Use container-native load balancing

Use container-native load balancing if possible. The load balancer distributes traffic directly to Pods, rather than to nodes. This improves traffic distribution and reduces latency. For more information, see [About load balancing in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-load-balancing).

### Consider topology aware routing

Consider using topology aware routing. This feature aims to keep traffic within its originating zone, improving performance and reducing costs. This feature works best when incoming traffic is evenly distributed, and the Kubernetes Services have three or more endpoints per zone. For more information, see [Traffic distribution troubleshooting](https://kubernetes.io/docs/concepts/services-networking/service/#traffic-distribution).

### Cloud Service Mesh

For more granular control over traffic distribution, advanced routing policies, and observability, consider implementing a Cloud Service Mesh like Istio. Cloud Service Mesh operates at the application layer and provides sophisticated traffic management capabilities.

## Checklist summary

Area | Practice  
---|---  
VPC design | 

  * Use VPC-native clusters
  * Use Shared VPC networks

  
IP address management strategies | 

  * Plan the required IP address allotment
  * Use non-RFC 1918 space if needed
  * Use custom subnet mode
  * Plan Pod density per node
  * Avoid overlaps with IP addresses used in other environments
  * Create a load balancer subnet
  * Reserve enough IP address space for cluster autoscaler
  * Share IP addresses across clusters
  * Share IP addresses for internal LoadBalancer Services

  
Network security options | 

  * Use GKE Dataplane V2
  * Minimize the cluster control plane exposure
  * Authorize access to the control plane
  * Allow control plane connectivity
  * Deploy proxies for control plane access from peered networks
  * Restrict cluster traffic using network policies
  * Enable Google Cloud Armor security policies for Ingress
  * Use Identity-Aware Proxy to provide authentication for applications with IAM users
  * Use organization policy constraints to further enhance security

  
Scaling | 

  * Use Cloud DNS for GKE
  * Enable NodeLocal DNSCache
  * Use Cloud NAT for internet access from clusters

  
Serving applications | 

  * Use container-native load balancing
  * Choose the correct GKE resource to expose your application
  * Create health checks based on BackendConfig
  * Use local traffic policy to preserve original IP addresses

  
Operations and administration | 

  * Use IAM for GKE permissions to control policies in Shared VPC networks
  * Use regional clusters and distribute your workloads for high availability
  * Use Cloud Logging and Cloud Monitoring and enable network policy logging

  
Even traffic distribution | 

  * Disable or carefully configure session affinity
  * Use weighted load balancing
  * Ensure even Pod distribution across nodes
  * Review external traffic policy
  * Disable node affinity
  * Use readiness probes
  * Use container-native load balancing
  * Consider topology aware routing
  * Cloud Service Mesh

  
  
## What's next

  * [GKE best practices insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-best-practices)
  * [Best practices for enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy)


  * [Exposing GKE applications through Ingress and Services](https://cloud.google.com/blog/products/containers-kubernetes/exposing-services-on-gke)


  * [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/solutions/best-practices-vpc-design)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
