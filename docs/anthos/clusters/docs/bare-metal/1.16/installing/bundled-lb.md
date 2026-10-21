---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb/
title: Configure bundled load balancing with MetalLB \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:17.381199+00:00
---

# Configure bundled load balancing with MetalLB  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Configure bundled load balancing with MetalLB Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/bundled-lb)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page describes how to configure bundled load balancing with MetalLB for Distributed Cloud. MetalLB load balancers run on either a dedicated pool of worker nodes or on the same nodes as the control plane.

See [Overview of load balancers](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/load-balance) for examples of load-balancing topologies available in Distributed Cloud.

## Requirements

  * All load balancer nodes must be in the same Layer 2 subnet.
  * All VIPs must be in the load balancer nodes subnet and be routable through the subnet's gateway.
  * The gateway of the load balancer subnet must listen to gratuitous ARP messages and forward ARP packets to the load balancer nodes.



## Configuration fields

Edit the `cluster.spec.loadBalancer` section of the cluster configuration file to configure bundled load balancing. For information about cluster configuration files and examples of valid configurations, see one of the following pages:

  * [Create admin clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/admin-cluster-creation)
  * [Create user clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/user-cluster-creation)
  * [Create hybrid clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/hybrid-cluster-creation)
  * [Create standalone clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/standalone-cluster-creation)



### loadBalancer.mode

This value must be `bundled` to enable bundled load balancing.

### loadBalancer.ports.controlPlaneLBPort

This value specifies the destination port to be used for traffic sent to the Kubernetes control plane (the Kubernetes API servers).

### loadBalancer.vips.controlPlaneVIP

This value specifies the destination IP address to be used for traffic sent to the Kubernetes control plane (the Kubernetes API servers). This IP address must be in the same Layer 2 subnet as the nodes in the cluster. **Don't** list this address in the `address pools` section of the configuration file.

### loadBalancer.vips.ingressVIP

This value specifies the IP address to be used for Services behind the load balancer for ingress traffic. This field is not allowed in [admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/admin-cluster-creation) configuration files. This address must be listed in the address pools section of the configuration.

### loadBalancer.addressPools

This section of the configuration contains one or more address pools. Each address pool specifies a list of IP address ranges. When you create a [Service of type `LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer), the external IP addresses for the Service are chosen from these ranges.

**Note:** Starting with Google Distributed Cloud version 1.16.0, you can update an existing load balancer address pool at any time to change the following two fields: `avoidBuggyIPs` and `manualAssign`.

Address pools are specified in the following format:
    
    
    - name: POOL_NAME
      avoidBuggyIPs: BOOLEAN
      manualAssign: BOOLEAN
      addresses:
      - IP_RANGE
      - IP_RANGE2
    

  * **`name`** : The name of the address pool, **pool-name** , for your own organizational purposes. This field is immutable.
  * **`avoidBuggyIPs`** : (Optional) `true` or `false`. If `true`, the pool omits IP addresses ending in `.0` and `.255`. Some network hardware drops traffic to these special addresses. You can omit this field, its default value is `false`. This field is mutable.
  * **`manualAssign`** : (Optional) `true` or `false`. If `true`, addresses in this pool are not automatically assigned to Kubernetes Services. If `true`, an IP address in this pool is used only when it is specified explicitly by a service. You can omit this field, its default value is `false`. This field is mutable.
  * **`addresses`** A list of one or more nonoverlapping IP address ranges. ip-range can be specified in either CIDR notation (like `198.51.100.0/24`) or range notation (like `198.51.100.0-198.51.100.10`, with no spaces around the dash). This field is immutable.



The IP address ranges in the `addresses` list must not overlap and must be in the same subnet as the nodes running load balancers.

### loadBalancer.nodePoolSpec

This section of the configuration specifies a list of nodes to run load balancers on. Load balancer nodes can run regular workloads by default; there is no special taint on those nodes. The example below shows a node pool with two nodes. The first node, `1.2.3.4`, uses the `k8sIP` field to specify the node's IP address in the cluster. The `1.2.3.4` address is only used for SSH access.
    
    
    nodePoolSpec:
      nodes:
      - address: 1.2.3.4
        k8sIP: 10.0.0.32
      - address: 10.0.0.33
    

All nodes in the load balancer node pool must be in the same Layer 2 subnet as the load balancer VIPs configured in the `loadBalancer.addressPools` section of the configuration file. If a node has a `k8sIP` configured, only that address needs to be in the same Layer 2 subnet as the other load balancer VIPs.

If `nodePoolSpec` is not set, the bundled load balancers run on the control plane nodes. We recommend you run load balancers on separate node pools if possible.

## Control plane load balancing

The control plane load balancer serves the control plane virtual IP address (VIP). Distributed Cloud runs Keepalived and HAProxy as Kubernetes static pods on the load-balancer nodes to announce the control plane VIP. Keepalived uses the Virtual Router Redundancy Protocol (VRRP) on the load balancer nodes for high availability.

## Data plane load balancing

**Note:** MetalLB in BGP mode isn't supported. For load balancing in BGP mode, see [Configure bundled load balancers with BGP](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-bundled-bgp).

The data plane load balancer is for all Kubernetes Services of type [`LoadBalancer`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_loadbalancer). Distributed Cloud uses [MetalLB](https://metallb.universe.tf/) running in Layer 2 mode for data plane load balancing. Data plane load balancing can only be configured through Distributed Cloud, don't modify the MetalLB ConfigMap directly. You can use all MetalLB features including [IP address sharing across Services](https://metallb.universe.tf/usage/#ip-address-sharing). See the MetalLB documentation for feature information.

MetalLB runs a speaker Pod on each node using a daemonset, using [memberlist](https://github.com/hashicorp/memberlist/blob/master/README.md) for high availability. There is a MetalLB dedicated load balancer node for each Kubernetes Service, rather than one for the entire cluster. This way traffic is distributed across load balancer nodes if there are multiple Services.

The data plane load balancers can run on either the control plane nodes or on a subset of worker nodes. Bundling data plane load balancers on the control plane nodes increases utilization of the control plane nodes. However, bundling on the control plane nodes also increases the risk of overloading the control plane and increases the risk profile of confidential information on the control plane, such as SSH keys.

## Preserving client source IP address

The `LoadBalancer` Service created with the bundled Layer 2 load balancing solution uses the default `Cluster` setting for the external traffic policy. This setting, `spec.externalTrafficPolicy: Cluster`, routes external traffic to cluster-wide endpoints, but it also obscures the client source IP address.

The following sections describe how to configure your cluster to [preserve the client source IP address](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip).

### `NodePort` Services

Kubernetes does source network address translation (NAT) for `NodePort` Services. To retain the client source IP addresses, set `service.spec.externalTrafficPolicy` to `Local`. Kubernetes won't perform source NAT anymore, but you must make sure there are pods running exactly on the node IP you picked.

### `LoadBalancer` Services

When using `externalTrafficPolicy: Local` in your `LoadBalancer` Services, set your application pods to run exactly on the load balancer nodes. Add the following `nodeSelector` to your application pods to make this change:
    
    
    apiVersion: v1
    kind: Pod
    ...
    spec:**  nodeSelector:
          baremetal.cluster.gke.io/lbnode: "true"**
    ...
    

### Ingress

If your applications are HTTP services, you can achieve client IP visibility by configuring ingress components:

  1. Open the `istio-ingress` Service for editing:
         
         kubectl edit service -n gke-system istio-ingress

  2. Add `externalTrafficPolicy: Local` to the `spec`, save and exit the editor.
         
         apiVersion: v1
         kind: Service
         ...
         spec:
         ...**  externalTrafficPolicy: Local**
         

  3. Open the `istio-ingress` Deployment for editing:
         
         kubectl edit deployment -n gke-system istio-ingress

  4. Add the following `nodeSelector` to the Deployment, save and exit the editor.
         
         apiVersion: apps/v1
         kind: Deployment
         ...
         spec:
           ...
           template:
             ...
             spec:
               ...**      nodeSelector:
                   baremetal.cluster.gke.io/lbnode: "true"**
         ...
         




Now, all of your services behind Ingress see a `X-Forwarded-For` header with the client IP, like the following example:
    
    
    X-Forwarded-For: 21.0.104.4
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
