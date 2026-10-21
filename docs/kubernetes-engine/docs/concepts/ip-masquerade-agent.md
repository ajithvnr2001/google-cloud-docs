---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent/
title: IP masquerade agent \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:25:16.816622+00:00
---

# IP masquerade agent  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  IP masquerade agent Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how IP masquerading works in Google Kubernetes Engine (GKE) and provides configuration options for different scenarios.

This page assumes that you know about [IP masquerading in Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/ip-masq-agent/#ip-masquerade-agent-user-guide).

## GKE IP masquerading

GKE can use IP masquerading to change the source IP addresses of packets sent from Pods. When IP masquerading applies to a packet emitted by a Pod, GKE changes the packet's source IP address from the Pod IP address to the underlying node's IP address. Masquerading a packet's source IP address is useful when a recipient is configured to receive packets only from the cluster's node IP addresses.

On Linux nodes, GKE configures `iptables` rules. GKE uses the `ip-masq-agent` [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) to configure the appropriate dataplane.

The `ip-masq-agent` is not supported on Windows Server node pools. However, Windows nodes perform IP masquerading (Source Network Address Translation or SNAT) for packets sent to destinations that are external to the cluster by rewriting the source Pod IP address to the node's IP address. SNAT is skipped for packets sent to Pod or node IP addresses within the same cluster. This behavior on Windows nodes is not user-configurable.

### IP masquerading for Standard clusters

In Standard clusters, the cluster's IP masquerade behavior is governed by three factors:

  * Whether you have deployed or GKE has automatically deployed the [`ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#check-ip-masq-agent) in the cluster. To learn about the scenarios in which GKE automatically deploys the `ip-masq-agent` DaemonSet, see When the `ip-masq-agent` is deployed automatically.
  * Whether you have created a [custom `nonMasqueradeCIDRs` list in the `ip-masq-agent` configMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent).
  * In cases where no `ip-masq-agent` DaemonSet is deployed in the cluster, whether you created the cluster with the `--disable-default-snat` flag. To learn more about this flag, see Effect of the `--disable-default-snat` flag.



The following table summarizes IP masquerade configurations for Standard GKE clusters:

Cluster configuration | Resulting SNAT behavior  
---|---  
The `ip-masq-agent` DaemonSet is present in the cluster, **and** a custom `nonMasqueradeCIDRs` list exists in the `ip-masq-agent` ConfigMap. |  GKE preserves the source Pod IP addresses for packets sent to destinations specified in the `nonMasqueradeCIDRs` list. GKE changes source Pod IP addresses to source node IP addresses for packets sent to destinations not specified in the `nonMasqueradeCIDRs` list.  
The `ip-masq-agent` DaemonSet is present in the cluster, **but** a custom `nonMasqueradeCIDRs` list **does not exist** in the `ip-masq-agent` ConfigMap _or_ the `ip-masq-agent` ConfigMap is not present at all.  |  GKE preserves the source Pod IP addresses for packets sent to a set of default non-masquerade destinations. GKE changes source Pod IP addresses to source node IP addresses for packets sent to destinations outside of the default non-masquerade destinations.  
The `ip-masq-agent` DaemonSet is **not** present in the cluster, **and** you have created the cluster **without** the `--disable-default-snat` flag. |  GKE preserves the source Pod IP addresses for packets sent to a set of default non-masquerade destinations. GKE changes source Pod IP addresses to source node IP addresses for packets sent to destinations outside of the default non-masquerade destinations.  
The `ip-masq-agent` DaemonSet is **not** present in the cluster, **and** you have created the cluster **with** the `--disable-default-snat` flag. |  GKE preserves the source Pod IP addresses for packets sent to all destinations. Review Preserving Pod IPv4 address sources to internet destinations for important routing considerations when you preserve Pod IPv4 source addresses and need to route packets to the internet.  
  
### IP masquerading for Autopilot clusters

In Autopilot clusters, GKE always deploys an `ip-masq-agent` DaemonSet. Except for packets sent by Pods to the cluster's node, Pod, or Services ranges, you can control the IP masquerade behavior using an `EgressNATPolicy`. To use an `EgressNATPolicy`, your Autopilot cluster must meet both of these requirements:

  * The cluster must use GKE version 1.23.4-gke.1600 or later, or 1.22.7-gke.1500 or later.
  * The cluster must have been created with [GKE Dataplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#create-cluster).



The following table summarizes IP masquerade configurations for Autopilot GKE clusters:

Autopilot cluster configuration | Resulting SNAT behavior  
---|---  
The cluster includes a custom `EgressNATPolicy` whose `spec.action` is `NoSNAT` containing non-masquerade destinations specified in `spec.destinations[]`.  |  GKE preserves the source Pod IP addresses for packets sent to destinations specified in `spec.destinations[]` of the `EgressNATPolicy`. GKE accomplishes this by translating `spec.destinations[]` into a `nonMasqueradeCIDRs` list in an `ip-masq-agent` configMap. GKE changes source Pod IP addresses to source node IP addresses for packets sent to destinations not specified in `spec.destinations[]` of the `EgressNATPolicy`.   
The cluster **does not include** a custom `EgressNATPolicy`.  |  The default `EgressNATPolicy` and Managed by GKE policy both apply, resulting in the following behavior:

  * GKE preserves the source Pod IP addresses for packets sent to a set of default non-masquerade destinations.
  * GKE changes source Pod IP addresses to source node IP addresses for packets sent to destinations outside of the default non-masquerade destinations.

  
**Note:** Autopilot clusters never perform IP masquerading (SNAT) when sending packets to the cluster's own node, Pod, or Services IP addresses because of the Managed by GKE `EgressNATPolicy`.

## Configuration examples

Expand the following sections to see IP masquerading and configuration examples based on cluster type.

#### Standard cluster IP masquerading configuration examples

To achieve this SNAT behavior | Implement the following configuration  
---|---  
  
  * Preserve source Pod IP addresses in packets that Pods1 send to destinations `198.15.5.92/24` and `10.0.0.0/8`.
  * Masquerade source Pod IP addresses in packets that Pods1 send to all other destinations by changing the packet source to the underlying node IP address.

| 

  1. [ Create an `ip-masq-agent` ConfigMap whose `nonMasqueradeCIDRs` contains only `198.15.5.92/24` and `10.0.0.0/8`.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#creating_the_ip-masq-agent_configmap)
  2. [ Deploy the `ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#deploy-ip-masq-agent-deamonset). 

  
  
  * Preserve source Pod IP addresses in packets that Pods1 send to default non-masquerade destinations.
  * Masquerade source Pod IP addresses in packets that Pods1 send to all other destinations by changing the packet source to the underlying node IP address.

|  Use one of the following techniques: |  **Technique 1**

  1. Create or update the cluster so that the `--disable-default-snat` flag is _not_ set, and 
  2. Ensure that `nonMasqueradeCIDRs` is _not_ specified in the `ip-masq-agent` ConfigMap or that the `ip-masq-agent` ConfigMap is absent. 

With this configuration, even if GKE automatically deploys an `ip-masq-agent` DaemonSet, the `ip-masq-agent` ConfigMap instructs it to use the default non-masquerade destinations.   
---  
**Technique 2**

  1. Ensure that `nonMasqueradeCIDRs` is _not_ specified in the `ip-masq-agent` ConfigMap or that the `ip-masq-agent` ConfigMap is _not_ present in the cluster, and 
  2. [ Deploy the `ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#deploy-ip-masq-agent-deamonset) in the cluster. 

With this configuration, the  effect of the `--disable-default-snat` flag is nullified by deploying an `ip-masq-agent` DaemonSet.   
  
  * Preserve source Pod IP addresses in packets that Pods1 send to all destinations.
  * Disable IP masquerading completely.

| 

  1. Review Preserving Pod IPv4 address sources to internet destinations for important routing considerations when you preserve Pod IPv4 source addresses and need to route packets to the internet.
  2. Use one of the following cluster configuration techniques:
|  **Technique 1**
     1. Create or update the cluster so that the `--disable-default-snat` flag is set, and 
     2. Ensure that the `ip-masq-agent` DaemonSet is _not_ deployed in the cluster. 
You can [ delete the `ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#deleting_the_ip-masq-agent_daemonset) to ensure that setting the `--disable-default-snat` flag has an effect. Because the `ip-masq-agent` DaemonSet must be absent in this technique, it doesn't matter if the cluster has an `ip-masq-agent` ConfigMap or what the contents of the `ip-masq-agent` ConfigMap might be.   
---  

  
**Technique 2**

  1. [ Create an `ip-masq-agent` ConfigMap whose `nonMasqueradeCIDRs` is `[0.0.0.0/0]`.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#creating_the_ip-masq-agent_configmap)
  2. [ Deploy the `ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#deploy-ip-masq-agent-deamonset). 

With this configuration, the  effect of the `--disable-default-snat` flag is nullified because you have purposefully deployed an `ip-masq-agent` DaemonSet.   
  
1Except for diagnostic containers and Pods with `hostNetwork: true`.

#### Autopilot cluster IP masquerading configuration examples

To achieve this SNAT behavior | Implement the following configuration  
---|---  
  
  * Preserve source Pod IP addresses in packets that Pods send to destinations `198.15.5.92/24` and `10.0.0.0/8`.
  * Masquerade source Pod IP addresses in packets that Pods send to all other destinations by changing the packet source to the underlying node IP address.

|  [ Edit the default EgressNATPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot#edit-default-egress-nat-policy) such that: 

  * The `spec.action` is `NoSNAT`, and
  * The `spec.destinations` contains only: 
    * `Cidr: 198.15.5.92/24`
    * `Cidr: 10.0.0.0/8`

  
  
  * Preserve source Pod IP addresses in packets that Pods send to default non-masquerade destinations.
  * Masquerade source Pod IP addresses in packets that Pods send to all other destinations by changing the packet source to the underlying node IP address.

|  [ Edit the default EgressNATPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot#edit-default-egress-nat-policy) such that: 

  * The `spec.action` is `NoSNAT`, and
  * The `spec.destinations` contains a `Cidr` entry for each of the default non-masquerade destinations
. 
  
  
  * Preserve source Pod IP addresses in packets that Pods send to all destinations.
  * Disable IP masquerading completely.

| 

  1. Review Preserving Pod IPv4 address sources to internet destinations for important routing considerations when you preserve Pod IPv4 source addresses and need to route packets to the internet.
  2. [Edit the default EgressNATPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot#edit-default-egress-nat-policy) such that:
     * The `spec.action` is `NoSNAT`, and
     * The `spec.destinations` contains `Cidr: 0.0.0.0/0`
. 
  
  
## Advanced configuration reference

### When the `ip-masq-agent` is deployed automatically

In Autopilot mode clusters, GKE always deploys an `ip-masq-agent` DaemonSet.

In Standard clusters, GKE deploys an `ip-masq-agent` DaemonSet when the `--disable-default-snat` flag is _not_ set and the cluster uses one of the following configuration combinations:

  * The cluster does not use GKE Dataplane V2, and [network policy enforcement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) is enabled.

  * The cluster uses a Pod IP address range that does not fit within `10.0.0.0/8`.




For the `ip-masq-agent` DaemonSet to be effective, you must also [specify the `nonMasqueradeCIDRs` list](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) in the `ip-masq-agent` ConfigMap. For more information, see [how to configure an IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).

When a `ip-masq-agent` DaemonSet is present in a cluster, GKE updates and reconciles a serving Pod on each node of the cluster.

### Default non-masquerade destinations

The default non-masquerade destination are:

  * `10.0.0.0/8`
  * `172.16.0.0/12`
  * `192.168.0.0/16`
  * `100.64.0.0/10`
  * `192.0.0.0/24`
  * `192.0.2.0/24`
  * `192.88.99.0/24`
  * `198.18.0.0/15`
  * `198.51.100.0/24`
  * `203.0.113.0/24`
  * `240.0.0.0/4`



The default non-masquerade destinations are applicable to clusters with the following configurations:

  * Your cluster has an [`ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#check-ip-masq-agent-daemonset), but no [`nonMasqueradeCIDRs` list](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) specified in its `ip-masq-agent` ConfigMap. This includes the case where your cluster has an `ip-masq-agent` DaemonSet, but does not have an `ip-masq-agent` ConfigMap at all.

  * Your cluster _does not_ have an [`ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#check-ip-masq-agent-daemonset), _and_ the [`--disable-default-snat` flag](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-default-snat) is not set.




The default non-masquerade destinations are _not_ applicable to clusters with the following configurations:

  * Your cluster has an [`ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#check-ip-masq-agent-daemonset), and you have a custom [`nonMasqueradeCIDRs` list](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) specified in the `ip-masq-agent` ConfigMap. A custom `nonMasqueradeCIDRs` list always overrides the default non-masquerade destinations when the cluster has an `ip-masq-agent` DaemonSet.

  * Your cluster _does not_ have an [`ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#check-ip-masq-agent-daemonset), _and_ the [`--disable-default-snat` flag](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-default-snat) is set. See Effect of the `--disable-default-snat` flag for more details about this configuration.




### Effect of the `--disable-default-snat` flag

The [`--disable-default-snat`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-default-snat) flag changes the _default_ GKE SNAT behavior so that source Pod IP addresses are preserved for packets sent to all destinations. GKE implements the default SNAT behavior by not deploying any `ip-masq-agent` DaemonSet in the cluster.

The `--disable-default-snat` flag has no effect when a cluster includes an `ip-masq-agent` DaemonSet:

  * Because Autopilot clusters always include an `ip-masq-agent` DaemonSet, the `--disable-default-snat` flag has no effect on Autopilot clusters.

  * For Standard clusters: If you [deploy an `ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#deploy-ip-masq-agent-deamonset) or if GKE automatically deploys an `ip-masq-agent` DaemonSet, the `--disable-default-snat` flag has no meaning for the cluster, even if `--disable-default-snat` is set. When an `ip-masq-agent` DaemonSet is present in the cluster, non-masquerade destinations are either explicitly specified in a `nonMasqueradeCIDRs` list of the `ip-masq-agent` ConfigMap or from the default non-masquerade destinations when no `nonMasqueradeCIDRs` list is defined.




You can set the `--disable-default-snat` flag by updating a cluster after it has been created. Provided that the cluster has no `ip-masq-agent` DaemonSet deployed, disabling default SNAT takes effect after the cluster has replaced all of its nodes—sometimes hours later. This is because GKE respects your configured [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) when it replaces nodes in the cluster. If you haven't configured any maintenance window, you need to manually cycle the nodes in the cluster before the `--disable-default-snat` flag has any effect.

### Link-local masquerading

The `169.254.0.0/16` range is used for _link-local IP addresses_. Link-local masquerading refers to changing a source Pod IP address to a source node IP address for packets sent to the `169.254.0.0/16` destinations.

Autopilot clusters always preserve source Pod IP addresses for packets sent to `169.254.0.0/16` destinations.

By default, Standard clusters also preserve the source Pod IP addresses for packets sent to `169.254.0.0/16` destinations.

You can enable link-local IP masquerading in a Standard cluster by doing both of the following:

  * Ensure that the `masqLinkLocal` parameter exists and is set to `True` in the `ip-masq-agent` configMap. When the `masqLinkLocal` parameter is not present in the `ip-masq-agent` configMap, the default is `False`. For guidance, see [Checking the `ip-masq-agent` ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#checking_the_ip-masq-agent_configmap), [Creating the `ip-masq-agent` ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#creating_the_ip-masq-agent_configmap), and [Editing an existing `ip-masq-agent` ConfigMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#edit-ip-masq-agent-configmap).
  * Ensure that your cluster has the `ip-masq-agent` DaemonSet deployed. For guidance, see [Checking the `ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#check-ip-masq-agent-daemonset) and [Deploying the `ip-masq-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#deploy-ip-masq-agent-deamonset).

**Important:** In Standard clusters, after you enabled link-local IP masquerading, you cannot override link-local IP masquerading by adding `169.254.0.0/16` (or any CIDR that fits within `169.254.0.0/16`) to the `nonMasqueradeCIDRs` list in the `ip-masq-agent` ConfigMap. You also cannot override link-local IP masquerading with the `--disable-default-snat` flag because enabling link-local IP masquerading requires deploying the `ip-masq-agent` DaemonSet, and the `--disable-default-snat` flag has no effect when an `ip-masq-agent` DaemonSet exists in the cluster.

### Diagnostic containers and Pods with `hostNetwork: true`

Unless you specify a custom source IP address for packets, Pods running with `hostNetwork: true` and diagnostic containers send packets with sources matching the node's IP address. For Pods running with `hostNetwork: true`, GKE assigns the Pod the node's IP address. GKE does not manage IP addresses for diagnostic containers, including containers for [debugging node issues using toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox).

Autopilot clusters do not support running Pods with `spec.hostNetwork: true`. Because the nodes of an Autopilot cluster are not accessible using SSH, you cannot run diagnostic containers on them.

### Preserving Pod IPv4 address sources to internet destinations

If your cluster's IP masquerade configuration is one of the following, GKE preserves Pod IP address sources for packets sent to all destinations, including internet destinations:

  * In Standard clusters with an `ip-masq-agent` DaemonSet, if you've set the `nonMasqueradeCIDRs` to `0.0.0.0` in the `ip-masq-agent` ConfigMap.
  * In Standard clusters without an `ip-masq-agent` DaemonSet, if you've set the `--disable-default-snat` flag.
  * In Autopilot clusters, if you [edit the default EgressNATPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot#edit-default-egress-nat-policy) such that the `spec.action` is `NoSNAT`, and the `spec.destinations` contains `Cidr: 0.0.0.0/0`.



Pod IPv4 sources are internal IPv4 addresses, which means that they aren't routable on the internet. Consequently, when you preserve source Pod IPv4 addresses for packets sent to the internet, you need to use a technique like one of the following in order to route packets after they leave the nodes of the cluster:

  * Make sure your VPC network has a default route with the default internet gateway next hop, and configure a Cloud NAT gateway to provide public NAT services to at least the subnet secondary IPv4 address ranges used by Pods in your cluster. For more details, see [GKE interaction](https://docs.cloud.google.com/nat/docs/nat-product-interactions#NATwithGKE) in the Cloud NAT overview.
  * Configure your VPC network to use a custom default route whose next hop is a VM instance or internal passthrough Network Load Balancer, where the VM or backends of the load balancer have been configured to route packets to the internet on behalf of the Pods.



### Restoring to the default SNAT behavior

To restore to the default SNAT behavior when an `ip-masq-agent` DaemonSet is present in a cluster, delete the associated `ip-masq-agent` ConfigMap. The `ip-masq-agent` DaemonSet restores the default IP masquerading behavior on the nodes it manages.

**Note:** Deleting both the `ip-masq-agent` DaemonSet and ConfigMap won't restore the default SNAT behavior.

To restore to the default SNAT behavior when an `ip-masq-agent` DaemonSet is not present in a cluster, you will need to [upgrade the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#upgrading_a_node_pool) (make sure `--disable-default-snat` is not set on the cluster).

## Effect of the Egress NAT policy in Autopilot clusters

The GKE _Egress NAT policy_ lets you configure IP masquerading on Autopilot clusters. You can use the GKE Egress NAT policy custom resource definition (CRD) to change the source IP addresses of packets sent from the Pods.

For security or IP address exhaustion reasons, you can masquerade IP addresses from Pod to Node IP address range for outbound traffic to on-premises networks. For example, you can use a non-RFC-1918 range for Autopilot clusters and use a RFC-1918 range for the nodes. However, if Pods must communicate with on-premises networks that also use non-RFC-1918 range, IP addresses can overlap. To avoid traffic loss, you can [configure an Egress NAT Policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot#deploy-new-policy) to not advertise the Pods' non-RFC-1918 ranges to on-premises networks. The Egress NAT Policy masquerades the Pods' non RFC-1918 range to use the Node's RFC-1918 range instead. Ensure that a Node range is not overlapping with any on-premises range or it can cause a traffic loop.

**Note:** For clusters in Autopilot mode in versions earlier than 1.23.4-gke.1600 or 1.22.7-gke.1500, [RFC-1918 and all reserved addresses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#default-non-masq-dests) as destinations are not masqueraded. Changes to the masquerading behavior require special `kube-system` configurations that are not available in Autopilot mode.

GKE enforces the IP masquerading behavior for Autopilot clusters through the following process:

  1. GKE deploys the Egress NAT controller and the `ip-masq-agent`.
  2. You create the Egress NAT policy.
  3. The GKE controller translates the policy into the `ip-masq-agent` ConfigMap.
  4. The `ip-masq-agent` DaemonSet reads the ConfigMap and then GKE enforces the IP masquerading behavior.



### Automatically generated policies

GKE supports the following two automatically generated Egress NAT policies:

  * Default: These policies are editable.
  * Managed by GKE: These policies are fixed and are not editable.



#### Default policy

GKE predefines a set of default IP address ranges. When packets are sent to these destinations, your cluster does not masquerade IP address sources and preserves source Pod IP addresses. To change these default IP address ranges, see [Edit and deploy the Egress NAT policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot#edit-default-egress-nat-policy).

The following manifest describes a default Egress NAT policy:
    
    
        Name:         default
        Namespace:
        Labels:       <none>
        Annotations:  <none>
        API Version:  networking.gke.io/v1
        Kind:         EgressNATPolicy
        Metadata:
          Creation Timestamp:  2022-03-16T21:05:45Z
          Generation:          2
          Managed Fields:
            API Version:  networking.gke.io/v1
            Fields Type:  FieldsV1
            fieldsV1:
              f:spec:
                .:
                f:action:
              f:status:
            Manager:      egress-nat-controller
            Operation:    Update
            Time:         2022-03-16T21:05:45Z
            API Version:  networking.gke.io/v1
            Fields Type:  FieldsV1
            fieldsV1:
              f:spec:
                f:destinations:
            Manager:         kubectl
            Operation:       Update
            Time:            2022-03-17T01:58:13Z
          Resource Version:  189346
          UID:               06acbb5a-23ba-4c2a-bb34-9b6ed8c4a87f
        Spec:
          Action:  NoSNAT
          Destinations:
            Cidr:  10.0.0.0/8
            Cidr:  172.16.0.0/12
            Cidr:  192.168.0.0/16
            Cidr:  240.0.0.0/4
            Cidr:  192.0.2.0/24
            Cidr:  198.51.100.0/24
            Cidr:  203.0.113.0/24
            Cidr:  100.64.0.0/10
            Cidr:  198.18.0.0/15
            Cidr:  192.0.0.0/24
            Cidr:  192.88.99.0/24
        Status:
        Events:  <none>
    

The CIDR ranges are the same as the default non-masquerade destination ranges.

#### Managed by GKE policy

GKE Egress NAT policy reserves a static range of IP addresses required to preserve cluster's operation. This static range contains the Pod, Service, and Node IP address ranges of the cluster, and might overlap with the default policy.

You can identify this policy by a dynamic 8-byte hash (`gke-{CLUSTER_SHORT_HASH}`) that GKE assigns. You cannot edit this policy.

The following manifest describes a managed by GKE policy named `gke-bbfa6c0e-1`:
    
    
        Name:         gke-bbfa6c0e-1
        Namespace:
        Labels:       <none>
        Annotations:  <none>
        API Version:  networking.gke.io/v1
        Kind:         EgressNATPolicy
        Metadata:
          Creation Timestamp:  2022-03-16T21:05:46Z
          Generation:          1
          Managed Fields:
            API Version:  networking.gke.io/v1
            Fields Type:  FieldsV1
            fieldsV1:
              f:spec:
                .:
                f:action:
                f:destinations:
              f:status:
            Manager:         egress-nat-controller
            Operation:       Update
            Time:            2022-03-16T21:05:46Z
          Resource Version:  11699
          UID:               0201b5de-a6f6-4926-822b-31ed7cdee2c6
        Spec:
          Action:  NoSNAT
          Destinations:
            Cidr:  10.119.128.0/17
            Cidr:  10.120.0.0/22
            Cidr:  10.128.0.0/20
        Status:
        Events:  <none>
    

## What's next

  * [Learn how to use Egress NAT Policy to configure IP masquerade in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot).
  * [Learn how to configure an IP masquerade agent in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).
  * [Read the GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * [Learn about configuring authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
