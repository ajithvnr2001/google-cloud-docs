---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters/
title: LoadBalancer Service parameters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:10.031082+00:00
---

# LoadBalancer Service parameters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  LoadBalancer Service parameters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes parameters for the Service manifests which control LoadBalancer Service behavior and configuration. Before reading this page, ensure that you're familiar with [Google Kubernetes Engine (GKE) LoadBalancer Service concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).

**Important:** LoadBalancer Services rely on specific finalizers (prefixed with `networking.gke.io`) and debug annotations (prefixed with `service.kubernetes.io`). Don't manually edit or remove these finalizers or annotations. Modifying or removing these objects can cause unexpected behavior or disruptions.

## Service parameters

GKE supports the following parameters for LoadBalancer Services.

Parameter | Service field and description | Internal | External | Version Support  
---|---|---|---|---  
Internal passthrough Network Load Balancer | 

  * `spec.loadBalancerClass: networking.gke.io/l4-regional-internal`
  * `networking.gke.io/load-balancer-type: "Internal"`

Instructs GKE to create an internal passthrough Network Load Balancer. The load balancer uses `GCE_VM_IP` NEG backends if either of the following is true:

  * The Service manifest is applied to a cluster that has [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting) enabled.
  * The Service manifest is applied to a cluster that runs GKE version 1.36 or later. GKE subsetting is automatically enabled in GKE version 1.36 and later.

In all other situations, the load balancer uses instance group backends. For more information, see [ Node grouping](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#endpoint-grouping). |  |  | 

  * `spec.loadBalancerClass: networking.gke.io/l4-regional-internal`: requires GKE version 1.33.1-gke.1779000 and later _and_ GKE subsetting enabled.
  * `networking.gke.io/load-balancer-type: "Internal"`: all supported versions.

We recommend `spec.loadBalancerClass` if your cluster uses GKE version 1.33.1-gke.1779000 or later, and has GKE subsetting enabled. This attribute is immutable and can't be changed after the Service manifest has been applied to a cluster.  
Backend service-based regional external passthrough Network Load Balancer | 

  * Default behavior in GKE 1.37 and later
  * `spec.loadBalancerClass: networking.gke.io/l4-regional-external`
  * `cloud.google.com/l4-rbs: "enabled"`

Instructs GKE to create a regional external passthrough Network Load Balancer. The load balancer uses `GCE_VM_IP` NEG backends if any of the following is true:

  * The Service is created in a cluster that runs GKE version 1.37 or later. No annotations or classes are required.
  * The Service manifest includes `spec.loadBalancerClass: networking.gke.io/l4-regional-external` and is applied to a cluster that runs GKE version 1.33.1-gke.1779000 to 1.36.
  * The Service manifest includes the `cloud.google.com/l4-rbs: "enabled"` annotation and is applied to a cluster that runs GKE version 1.32.2-gke.1652000 to 1.36.

In all other situations, the load balancer uses instance group backends. For more information, see [ Node grouping](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#endpoint-grouping). |  |  | 

  * `spec.loadBalancerClass: networking.gke.io/l4-regional-external`: requires GKE version 1.33.1-gke.1779000 and later.
  * `cloud.google.com/l4-rbs: "enabled"`: all supported versions.

We recommend `spec.loadBalancerClass` if your cluster uses GKE version 1.33.1-gke.1779000 to 1.36. This attribute is immutable and can't be changed after the Service manifest has been applied to a cluster. In GKE 1.37 and later, no fields are needed for this load balancer type.  
Weighted Load Balancing | `networking.gke.io/weighted-load-balancing: "pods-per-node"` Allows nodes that have more serving Pods to receive a larger proportion of new connections compared to nodes that have fewer serving Pods. |  |  | GKE 1.31.0+  
Internal Traffic Policy | `spec.internalTrafficPolicy` When set to the `Local` value, GKE only routes packets from client Pods on a node to serving Pods on the same node. When set to the `Cluster` value, GKE routes packets from client Pods on a node to serving Pods on any node. For more details, see [ Service Internal Traffic Policy](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/). This parameter is not supported in clusters running GKE Dataplane V2. |  |  | GKE 1.22+  
External Traffic Policy | `spec.externalTrafficPolicy` Controls which node VMs pass load balancer health checks and how packets are routed to ready and serving Pods in the cluster. Also controls how nodes are grouped into `GCE_VM_IP` NEGs when _GKE subsetting_ is enabled. For details, see [ LoadBalancer Service concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer). |  |  | GKE 1.14+ (1.23.4-gke.400+ for Windows node pool).  
Zonal affinity | `spec.trafficDistribution: PreferSameZone` Enables zonal affinity for internal LoadBalancer Services. Zonal affinity controls the zone to which the internal passthrough Network Load Balancer routes incoming traffic for compatible clients when a zonal match is possible. To use zonal affinity, you must enable GKE subsetting (enabled by default from GKE version 1.36 and later). For more information, see [ Zonal affinity and traffic distribution](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#zonal-affinity). |  |  | Preview in GKE 1.33.3-gke.1392000 and later. Generally available in GKE version 1.36 and later.   
Health check port | `spec.healthCheckNodePort` Deploys a load balancer health check for LoadBalancer Services. This parameter is only valid if `spec.externalTrafficPolicy` is set to `Local`. |  |  | All supported versions.  
Firewall rules and source IP address allowlist | `spec.loadBalancerSourceRanges` Configures optional firewall rules in GKE and in the VPC network to only allow certain source ranges. `kube-proxy` also configures `iptables` rules to match the specified source ranges. |  |  | All supported versions.  
Static IP addresses | 

  * `spec.loadBalancerIP` (IPv4 only)
  * `networking.gke.io/load-balancer-ip-addresses`

Specifies a static IPv4 address, static IPv6 address range, or both, that are assigned to the forwarding rules of the load balancer. See Considerations for sharing a common IP address for important configuration requirements and implementation details. |  |  | 

  * `spec.loadBalancerIP`: All supported versions.
  * `networking.gke.io/load-balancer-ip-addresses`: GKE 1.29 and later. See Static IP address parameters for additional cluster configuration or annotation requirements.

  
Network Service Tiers | `cloud.google.com/network-tier` Specifies which [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview) GKE uses for the external forwarding rule and IP address. The annotation valid values are `Standard` and `Premium` (default). |  |  | GKE 1.19 and later.  
Custom subnet | 

  * `networking.gke.io/internal-load-balancer-subnet`
  * `networking.gke.io/load-balancer-subnet`

|  |   
(only applies to IPv6) | 

  * `networking.gke.io/internal-load-balancer-subnet`: All supported versions
  * `networking.gke.io/load-balancer-subnet`: GKE 1.29 and later. See Custom subnet annotations for additional requirements.

  
Global access | `networking.gke.io/internal-load-balancer-allow-global-access: "true"` Enables the IP address of the forwarding rule to be accessible by clients in any region of the VPC network or a connected network. |  |  | Preview in GKE 1.16+. Generally available in GKE 1.17.9-gke.600+.  
All ports | GKE automatically configures the forwarding rule to use all ports if more than five (up to 100) unique ports are specified in `spec.ports[].port`. |  |  | GKE version 1.18.19-gke.1400 or later  
ipFamilyPolicy | `spec.ipFamilyPolicy` Defines how GKE allocates IP addresses to a Service. You can define the `spec.ipFamilyPolicy` as `SingleStack`, `PreferDualStack`, or `RequireDualStack`. To learn more, see [ IPv4/IPv6 dual-stack Services](https://kubernetes.io/docs/concepts/services-networking/dual-stack/#services). |  |  | GKE clusters in version 1.29 or later support dual-stack network for LoadBalancer Services.  
ipFamilies (Optional) | `spec.ipFamilies` Defines the IP address family to allocate either single-stack or dual-stack Services. Use any of the following values:

  * `IPv4` for single-stack IPv4 Service only.
  * `IPv6` for IPv6 Service only.
  * `IPv4,IPv6` for dual-stack Service where the primary IP address of the Service is IPv4.
  * `IPv6,IPv4` for dual-stack Service where the primary IP address of the Service is IPv6.

|  |  | GKE clusters in version 1.29 or later support dual-stack network for LoadBalancer Services.  
  
### Health check port

As described in [Load balancer health checks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#health_check), GKE always deploys a load balancer health check when it creates a regional external passthrough Network Load Balancer or internal passthrough Network Load Balancer.

Whether you can set up `healthCheckNodePort` parameter or not depends on the following `externalTrafficPolicy` configuration:

`externalTrafficPolicy` | Health check port  
---|---  
`Cluster` |  You cannot use `spec.healthCheckNodePort`.   
`Local` |  You can select a custom port by using the `spec.healthCheckNodePort`. If unspecified, the Kubernetes control plane assigns a health check port from the node port range.  **Note: Either the**`kube-proxy` software (on clusters that don't use GKE Dataplane V2) or `cilium-agent` (GKE Dataplane V2) responds to packets sent to the health check node port. Health checks for LoadBalancer Services cannot be answered by serving Pods.  
**Warning:** Don't customize the regional external passthrough Network Load Balancer or internal passthrough Network Load Balancer by modifying its health check resource outside of GKE. GKE does not offer any other customization parameters for load balancer health checks created for LoadBalancer Services.

### Firewall rules and source IP address allowlist

Unless you've configured a cluster to [skip creating VPC firewall rules for LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules), GKE creates an ingress allow [VPC firewall rule for each Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws).

Each automatically created firewall rule has the following characteristics:

  * The firewall rule's direction is ingress, and its action is allow. The [implied deny ingress firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) in Google Cloud mean that GKE uses an allowlist model when creating ingress firewall rules.
  * GKE sets the firewall rule's protocol and destination port to those specified in the Service's `spec.ports[]` list.
  * GKE configures firewall rules for LoadBalancer Services by explicitly setting the [destination parameter](https://docs.cloud.google.com/firewall/docs/firewalls#destination_parameter_ingress_rule) to the virtual IP address of the LoadBalancer (the load balancer's forwarding rule).
  * GKE sets the [target parameter](https://docs.cloud.google.com/firewall/docs/firewalls#rule_assignment) of the firewall rule to include all nodes of the cluster.
  * If the Service includes `spec.loadBalancerSourceRanges[]`, GKE sets the firewall rule's [source parameter](https://docs.cloud.google.com/firewall/docs/firewalls#source_parameter_ingress_rule) to the IP addresses in that list. Additionally, GKE configures routes and rules within the node operating system to limit the source IP addresses for load-balanced traffic, using `kube-proxy` and `iptables` (on clusters that don't use GKE Dataplane V2) or `cilium-agent` and eBPF rules (on clusters with GKE Dataplane V2). If the Service does not include `loadBalancerSourceRanges[]`, GKE sets the firewall rule's source parameter to all IP addresses `(0.0.0.0/0)`.



### Static IP addresses

You can [create a static IP address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) and configure GKE to assign that static address to the load balancer's forwarding rule. Using a static IP address ensures that the load balancer's IP address remains the same even if you make changes to the LoadBalancer Service. Without a static IP address, GKE might assign a different IP address to the load balancer forwarding rule when you update a LoadBalancer Service. The forwarding rule IP address is _not_ the same as the Service's `spec.clusterIP` address. The ClusterIP address for a Service never changes when you update a LoadBalancer Service.

#### Static IP address parameters

To instruct a LoadBalancer Service to use a static IP address, use either the `spec.loadBalancerIP` parameter or the `networking.gke.io/load-balancer-ip-addresses` annotation. In GKE version 1.29 and later, the annotation takes precedence over `spec.loadBalancerIP` if the Service manifest contains both the parameter and the annotation.

Parameter or annotation and value | Requirements and capabilities  
---|---  
`spec.loadBalancerIP:`  
`IPv4_ADDRESS` | You can specify a static internal IPv4 address for an IPv4-only Internal LoadBalancer Service. You can specify a static external IPv4 address for an IPv4-only External LoadBalancer Service. The parameter works with all supported GKE versions.  
`networking.gke.io/load-balancer-ip-addresses:`  
`IP_ADDRESS_RESOURCE_NAME`

  * For single-stack LoadBalancer Services, set the value of the annotation to the IPv4 or IPv6 address resource _name_ , not the IP address itself.
  * For dual-stack LoadBalancer Services, set the value of the annotation to the static IPv4 address resource name and the static IPv6 address range resource name separated by a comma.

| You can specify static IPv4 address, static IPv6 address range, or both for IPv4-only, IPv6-only, and dual-stack Internal and External LoadBalancer Services. The annotation requires GKE 1.29 or later and the following additional requirements:

  * To use this annotation with an Internal LoadBalancer Service, your cluster must have [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting) enabled. GKE subsetting is enabled by default in GKE version 1.36 and later.
  * To use this annotation with an External LoadBalancer Service, you must set the `spec.loadBalancerClass` field to the `networking.gke.io/l4-regional-external` value in the Service manifest when you create the External LoadBalancer Service.

  
  
#### Considerations for sharing a common IP address

Two or more LoadBalancer Services can reference the same static IP address if the forwarding rule for each load balancer uses a unique combination of IP address, protocol, port specification, and Network Service Tiers specification, as indicated in the table in this section. Additionally:

  * Static IPv6 addresses are actually `/96` IPv6 address ranges, but GKE only configures nodes to accept packets on the first IPv6 address (`/128`) in the `/96` range.

  * For two or more Internal LoadBalancer Services to use the same internal IPv4 address or internal IPv6 address range, the static IP address must be created with the `SHARED_LOADBALANCER_VIP` purpose.


| Internal LoadBalancer Service | External LoadBalancer Service  
---|---|---  
Port specification | Forwarding rules for internal passthrough Network Load Balancers support up to five individual port numbers, or they can be configured to use all ports. When an Internal LoadBalancer Service has more than five `spec.ports[]` specified, GKE configures the forwarding rule for the internal passthrough Network Load Balancer to use all ports. Forwarding rules with the same IP address and protocol cannot have overlapping ports. This means you cannot create multiple Internal LoadBalancer Services that share the same IP address, protocol, and port(s). For example:

  * If you create an Internal LoadBalancer Service using TCP port 80, you cannot create another Service using TCP ports 80, 81, and 90 because port 80 overlaps.
  * If an Internal LoadBalancer Service uses TCP ports 80, 8080, and 90, you cannot create another Service using TCP on all ports, as this would also result in overlapping ports

For more information, see: [ internal passthrough Network Load Balancer forwarding rules that use a common IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip#two-int-passthrough-network-lbs). | For clusters running GKE versions earlier than 1.37, GKE creates a target pool based regional external passthrough Network Load Balancer if the LoadBalancer Service manifest _doesn't_ have the `spec.loadBalancerClass` field set to the `networking.gke.io/l4-regional-external` value, or doesn't include the `cloud.google.com/l4-rbs: "enabled"` annotation. For clusters running GKE 1.37 or later, you must explicitly set `spec.loadBalancerClass: "networking.gke.io/l4-regional-external-legacy"` to create a target pool based regional external passthrough Network Load Balancer. Forwarding rules for target pool based regional external passthrough Network Load Balancers must use _contiguous_ port ranges. The contiguous port range includes all ports the Service needs, but the range might also include additional ports not used by the Service. For example, an External LoadBalancer Service powered by a target pool based regional external passthrough Network Load Balancer which specifies ports 80 and 443 in its Service manifest uses a load balancer forwarding rule with a _port range_ of 80-443. This port range prevents other External LoadBalancer Services from using any of the ports 80, 443, and any of the numbers between 80 and 443. GKE creates a backend service-based regional external passthrough Network Load Balancer by default in versions 1.37 or later. In earlier versions, GKE creates the load balancer if the LoadBalancer Service manifest _includes_ the `spec.loadBalancerClass` field set to the `networking.gke.io/l4-regional-external` value. Forwarding rules for backend service-based regional external passthrough Network Load Balancers support up to five discrete port numbers or a _contiguous_ port range.  
Network Service Tiers | Not configurable—internal addresses are always Premium tier. | Configurable for static regional external IPv4 addresses. Static regional external IPv6 address ranges can only be created in the Premium tier. The Network Service Tiers specification of the static external IP address must match either:

  * The tier specified in the LoadBalancer Service manifest's `cloud.google.com/network-tier` annotation, if that annotation is present in the manifest, or
  * The project's default tier, if the `cloud.google.com/network-tier` annotation is absent from the LoadBalancer Service manifest.

The project's default tier is Premium, unless you have configured it differently.  
  
#### IP address reservation

GKE doesn't reserve the static IP addresses configured using `spec.loadBalancerIP` or `networking.gke.io/load-balancer-ip-addresses` annotation. This means that the IP address you assign to your Service can be released when the Service is deleted.

To keep the IP address reserved, you must manually create an address resource in your project. The static IP address must have the following attributes:

  * Be regional only.
  * Be in the same region as the cluster.
  * Be in the same Network Service Tiers as the LoadBalancer Service.
  * Have a name which does doesn't use the LoadBalancer name, prefixes like `k8s-`, or the service's UUID.



If you don't reserve the address yourself, the project logs can contain entries about address resources created and shortly removed. This is a part of normal service provisioning and should be expected.

### LoadBalancer subnet

You can configure an Internal LoadBalancer Service to use an ephemeral or static IPv4 address, IPv6 address range, or both, in a custom subnet located in the same region and VPC network as the cluster. Use a custom subnet for an Internal LoadBalancer Service to:

  * Group internal passthrough Network Load Balancers created by Internal LoadBalancer Services from two or more GKE clusters in the same VPC network and region.
  * Create Internal LoadBalancer Services whose internal passthrough Network Load Balancers have IPv4 addresses separate from the cluster's node IPv4 addresses.
  * In a dual-stack cluster, create Internal LoadBalancer Services whose internal passthrough Network Load Balancers have IPv6 address ranges separate from the cluster's node and Pod IPv6 addresses. A custom LoadBalancer subnet is mandatory to support Internal LoadBalancer Services if the cluster's subnet has an _external_ IPv6 address range.



You can configure an External LoadBalancer Service to use an ephemeral or static IPv6 address range in a custom subnet located in the same region and VPC network as the cluster. Use a custom subnet to create External LoadBalancer Services whose regional external passthrough Network Load Balancers have IPv6 address ranges separate from the cluster's node and Pod IPv6 addresses. A custom LoadBalancer subnet is mandatory to support External LoadBalancer Services in a dual-stack cluster because the cluster's subnet has an _internal_ IPv6 address range.

**Note:** The custom subnet annotation has no effect on the selection of the external IPv4 address for an External LoadBalancer Service because IPv4 addresses for regional external passthrough Network Load Balancers are not sourced from subnet ranges of a VPC network.

#### Custom subnet annotations

Use one of the following annotations to instruct a LoadBalancer Service to use an ephemeral or static IP address in a custom subnet. If a LoadBalancer Service manifest includes both annotations, the `networking.gke.io/load-balancer-subnet` annotation takes precedence provided that its annotation requirements are met.

Annotation and value | Requirements and capabilities  
---|---  
`networking.gke.io/internal-load-balancer-subnet:`  
`SUBNET_RESOURCE_NAME` | You can only use the annotation to specify a custom subnet for an IPv4-only Internal LoadBalancer Service. The annotation works with all supported GKE versions.  
`networking.gke.io/load-balancer-subnet:`  
`SUBNET_RESOURCE_NAME` | You can specify a custom subnet for an IPv4-only, IPv6-only, or dual-stack Internal LoadBalancer Service. You can specify a custom subnet for an IPv6-only or dual-stack External LoadBalancer Service. The annotation requires GKE 1.29 or later and the following additional requirements:

  * To use this annotation to specify a custom subnet for an Internal LoadBalancer Service, your cluster must have [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting) enabled. GKE subsetting is enabled by default in versions 1.36 and later.
  * To use this annotation to specify a custom subnet for an External LoadBalancer Service, you must configure a backend service-based load balancer. In GKE 1.37 and later, this configuration is the default behavior. In earlier versions, you must include the `spec.loadBalancerClass` field set to the `networking.gke.io/l4-regional-external` value in the Service manifest when you create the External LoadBalancer Service.

  
  
#### Subnet and IPv4 address for an Internal LoadBalancer Service

The following table describes valid subnet specification and IPv4 address combinations for an IPv4-only or dual-stack Internal LoadBalancer Service.

| Static IPv4 address 

  * For IPv4-only, can be specified using either Static IP address parameter. 
  * For dual-stack, must be specified using the  `networking.gke.io/load-balancer-ip-addresses` annotation. 

| Ephemeral IPv4 address  
---|---|---  
Custom subnet  


  * Must be in the same VPC network and region as the cluster.
  * For IPv4-only, can be specified using either of the Custom subnet annotations.
  * For dual-stack, must be specified using the  `networking.gke.io/load-balancer-subnet` annotation.

| **Custom subnet and static IPv4 address** : The static internal IPv4 address must have been created in the custom subnet's primary IPv4 address range.  | **Custom subnet and ephemeral IPv4 address** : GKE uses an unallocated internal IPv4 address in the custom subnet primary IPv4 address range.   
Cluster subnet | **Cluster subnet and static IPv4 address** : The static internal IPv4 address must have been created in the cluster subnet's primary IPv4 address range.  | **Cluster subnet and ephemeral IPv4 address** : GKE uses an unallocated internal IPv4 address in the cluster subnet primary IPv4 address range.   
  
#### Subnet and IPv6 address range for an Internal LoadBalancer Service

The following table describes valid subnet specification and IPv6 address range combinations for an IPv6-only or dual-stack Internal LoadBalancer Service. Even though the internal passthrough Network Load Balancer IPv6 forwarding rule uses an internal `/96` IPv6 address range, GKE only configures nodes to accept packets whose destinations match the first IPv6 address (`/128`) of the forwarding rule's `/96` range.

| Static IPv6 address range 

  * Must be specified using the `networking.gke.io/load-balancer-ip-addresses` annotation

| Ephemeral IPv6 address range  
---|---|---  
Custom dual-stack subnet  


  * Must be in the same VPC network and region as the cluster.
  * Must have an internal IPv6 address range (access type `INTERNAL`).
  * Must be specified using the  `networking.gke.io/load-balancer-subnet` annotation.

| **Custom subnet and static IPv6 address range** : The static internal `/96` IPv6 address range must have been created in the custom subnet's internal `/64` IPv6 address range.  | **Custom subnet and ephemeral IPv6 address range** : GKE uses an unallocated internal `/96` IPv6 address range from the custom subnet's internal `/64` IPv6 address range.   
Cluster dual-stack subnet 

  * Must have an internal IPv6 address range (access type `INTERNAL`).

| **Cluster subnet and static IPv6 address range** : The static internal `/96` IPv6 address range must have been created in the cluster subnet's internal `/64` IPv6 address range.  | **Cluster subnet and ephemeral IPv6 address range** : GKE uses an unallocated internal `/96` IPv6 address range from the cluster subnet's internal `/64` IPv6 address range.   
  
#### Subnet and IPv4 address for an External LoadBalancer Service

For IPv4-only and dual-stack External LoadBalancer Services, the external IPv4 address—whether a static external IPv4 address or an ephemeral external IPv4 address—doesn't come from a subnet.

#### Subnet and IPv6 address range for an External LoadBalancer Service

The following table describes valid subnet specification and IPv6 address range combinations for an IPv6-only or dual-stack External LoadBalancer Service. Even though the regional external passthrough Network Load Balancer IPv6 forwarding rule uses an external `/96` IPv6 address range, GKE only configures nodes to accept packets whose destinations match the first IPv6 address (`/128`) of the forwarding rule's `/96` range.

| Static IPv6 address range 

  * Must be specified using the `networking.gke.io/load-balancer-ip-addresses` annotation

| Ephemeral IPv6 address range  
---|---|---  
Custom dual-stack subnet  


  * Must be in the same VPC network and region as the cluster.
  * Must have an external IPv6 address range (access type `EXTERNAL`).
  * Must be specified using the  `networking.gke.io/load-balancer-subnet` annotation.

| **Custom subnet and static IPv6 address range** : The static external `/96` IPv6 address range must have been created in the custom subnet's external `/64` IPv6 address range. Static external IPv6 address ranges can only be created in Premium tier.  | **Custom subnet and ephemeral IPv6 address range** : GKE uses an unallocated external `/96` IPv6 address range from the custom subnet's external `/64` IPv6 address range.   
Cluster dual-stack subnet 

  * Must have an external IPv6 address range (access type `EXTERNAL`).

| **Cluster subnet and static IPv6 address range** : The static external `/96` IPv6 address range must have been created in the cluster subnet's external `/64` IPv6 address range. Static external IPv6 address ranges can only be created in Premium tier.  | **Cluster subnet and ephemeral IPv6 address range** : GKE uses an unallocated external `/96` IPv6 address range from the cluster subnet's external `/64` IPv6 address range.   
  
### Global access

When the `networking.gke.io/internal-load-balancer-allow-global-access` annotation is `false` or unspecified for an Internal LoadBalancer Service, GKE creates an internal passthrough Network Load Balancer whose forwarding rule has global access disabled. When global access is disabled, clients that need to access the load balancer must be located in the same region and VPC network, or a network connected to the cluster's VPC network.

When the `networking.gke.io/internal-load-balancer-allow-global-access` annotation is `true` for an Internal LoadBalancer Service, GKE enables the global access option on the internal passthrough Network Load Balancer's forwarding rule. Clients located in any region of the VPC network or a network connected to the cluster's VPC network can access the load balancer.

**Note:** If you use an [internal load balancer with Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net#ilb_psc), you might face an error when you enable global access on the Service. To mitigate this issue, follow the steps outlined in [Error enabling global access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net#global-access).

For more information about how global access applies to clients in a connected network, see:

  * [Client access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access) in the internal passthrough Network Load Balancer documentation
  * [Internal passthrough Network Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks)



### All ports forwarding rules

Forwarding rules for internal passthrough Network Load Balancers support five unique port numbers or all ports.

In GKE, an Internal LoadBalancer Service can only support up to 100 ports in the Service's `spec.ports[].port`. If an Internal LoadBalancer Service defines up to five ports, the forwarding rule will include those specific ports. However, if the Service specifies more than five ports, the forwarding rule will automatically be configured to match all ports. When configuring a forwarding rule to use all ports, GKE only creates ingress allow firewall rules for the specific ports configured in `spec.ports[].port` on the Service.

For more information about internal passthrough Network Load Balancer forwarding rules and valid port specifications, see [Forwarding rules and port specifications](https://docs.cloud.google.com/load-balancing/docs/internal#all_ports).

### IPv4/IPv6 dual-stack LoadBalancer Service

You can create an Internal or External LoadBalancer Service that can be single-stack (IPv4 only or IPv6 only) or dual-stack. Single-stack LoadBalancer Services create a single forwarding rule with either an IPv4 address or an IPv6 address. Dual-stack LoadBalancer Services create two forwarding rules: one with an IPv4 address, and another with an IPv6 address. To create a IPv4/IPv6 dual-stack LoadBalancer Service, deploy it on a [IPv4/IPv6 dual-stack cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#dual-stack) and complete any of the following depending on the type of load balancer you use:

  * For Internal LoadBalancer Services, you must have GKE subsetting enabled. GKE subsetting is enabled by default for dual-stack clusters. For more information see, enabling [Internal load balancer subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#enabling_internal_load_balancer_subsetting_in_a_new_cluster).
  * For External LoadBalancer Services, you must use a backend service-based regional external passthrough Network Load Balancer. For more information, see [backend service-based external Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer#backend_service-based_external).



For each Service, you can define `ipFamilyPolicy` and `ipFamilies` specs. To learn more, see [IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/#services).

#### Restrictions of dual-stack LoadBalancer Services

  * LoadBalancer Services with IPv6 addresses are only supported on clusters with stack type `ipv4-ipv6`. For more information, learn how to [Use a dual-stack IP address for a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#dual-stack).
  * LoadBalancer Services created with a single-stack address cannot be upgraded to dual-stack Services.

  * LoadBalancer Services created with a dual-stack addresses can be changed to single stack according to the following conditions:

    * A Service with ipFamilies `["IPv4","IPv6"]` can be changed to a Service with ipFamilies `IPv4` but not `IPv6`.
    * A Service with ipFamilies `["IPv6","IPv4"]` can be changed to a Service with ipFamilies `IPv6` but not `IPv4`.



## What's next

  * Learn about [LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).
  * Learn how to set up an [internal load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).
  * Read an overview of [Ingress for Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress).
  * Learn how to use [standalone NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).
  * Learn more about [VPC firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
