---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/multi-nic/
title: Configure multiple network interfaces for pods \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:21.525276+00:00
---

# Configure multiple network interfaces for pods  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/multi-nic/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Configure multiple network interfaces for pods Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/multi-nic)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/multi-nic)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document describes how to configure Distributed Cloud to provide multiple network interfaces, multi-NIC, for your pods. The multi-NIC for pods feature can help separate control plane traffic from data plane traffic, creating isolation between planes. Additional network interfaces also enable multicast capability for your pods. Multi-NIC for pods is supported for user clusters, hybrid clusters, and standalone clusters. It is not allowed for admin type clusters.

Network plane isolation is important for systems using network functions virtualizations (NFVs), such as software-defined networking in a wide area network (SD-WAN), a cloud access security broker (CASB), and next-generation firewalls (NG-FWs). These types of NFVs rely on access to multiple interfaces to keep the management and data planes separate, while running as containers.

The multiple network interface configuration supports associating network interfaces with node pools, which can provide performance benefits. Clusters can contain a mix of node types. When you group high-performance machines into one node pool, you can add additional interfaces to the node pool to improve traffic flow.

## Set up multiple network interfaces

Generally, there are three steps to set up multiple network interfaces for your pods:

  1. Enable multi-NIC for your cluster with the `multipleNetworkInterfaces` field in the cluster custom resource.

  2. Specify network interfaces with `NetworkAttachmentDefinition` custom resources.

  3. Assign network interfaces to pods with the `k8s.v1.cni.cncf.io/networks` annotation.




Additional information is provided to help you configure and use the multi-NIC feature in a way that best suits your networking requirements.

### Enable multi-NIC

Enable multi-NIC for your pods by adding the `multipleNetworkInterfaces` field to the `clusterNetwork` section of the cluster custom resource and setting it to `true`.
    
    
      ...
      clusterNetwork:**    multipleNetworkInterfaces: true**
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20
      ...
    

### Specify network interfaces

Use `NetworkAttachmentDefinition` custom resources to specify additional network interfaces. The `NetworkAttachmentDefinition` custom resources correspond to the networks that are available for your pods. You can specify the custom resources within the cluster configuration, as shown in the following example, or you can create the `NetworkAttachmentDefinition` custom resources directly.
    
    
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: my-cluster
      namespace: cluster-my-cluster
    spec:
        type: user
        clusterNetwork:
          multipleNetworkInterfaces: true
    ...
    ---
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: gke-network-1
      namespace: cluster-my-cluster
    spec:
      config: '{
      "cniVersion":"0.3.0",
      "type": "ipvlan",
      "master": "enp2342",  # defines the node interface that this pod interface would
                             map to.
      "mode": "l2",
      "ipam": {
        "type": "whereabouts",
        "range": "172.120.0.0/24"
      }
    }'
    ---
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: gke-network-2
      namespace: cluster-my-cluster
    spec:
      config: '{
      "cniVersion":"0.3.0",
      "type": "macvlan",
      "mode": "bridge",
      "master": "vlan102",
      "ipam": {
        "type": "static",
        "addresses": [
          {
            "address": "10.10.0.1/24",
            "gateway": "10.10.0.254"
          }
        ],
        "routes": [
          { "dst": "192.168.0.0/16", "gw": "10.10.5.1" }
        ]
      }
    }'
    

When you specify the `NetworkAttachmentDefinition` custom resource in your cluster configuration file, Google Distributed Cloud uses this name to control the `NetworkAttachmentDefinition` custom resource after cluster creation. Google Distributed Cloud treats this custom resource inside the cluster namespace as the source of truth and reconciles it to the `default` namespace of the target cluster.

The following diagram illustrates how Google Distributed Cloud reconciles `NetworkAttachmentDefinition` custom resources from the cluster-specific namespace to the `default` namespace.

![NetworkAttachmentDefinition reconciliation](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/nad-reconcile.svg)

Although it is optional, we recommend that you specify `NetworkAttachmentDefinition` custom resources this way, during cluster creation. User clusters benefit the most when you specify the custom resources during cluster creation, because you can then control the `NetworkAttachmentDefinition` custom resources from the admin cluster.

If you choose not to specify `NetworkAttachmentDefinition` custom resources during cluster creation, you can add `NetworkAttachmentDefinition` custom resources directly to an existing target cluster. Google Distributed Cloud reconciles `NetworkAttachmentDefinition` custom resources defined in the cluster namespace. Reconciliation also happens upon deletion. When a `NetworkAttachmentDefinition` custom resource is removed from a cluster namespace, Google Distributed Cloud removes the custom resource from the target cluster.

### Assign network interfaces to a pod

Use the `k8s.v1.cni.cncf.io/networks` annotation to assign one or more network interfaces to a pod. Each network interface is specified with a namespace and the name of a `NetworkAttachmentDefinition` custom resource, separated by a forward slash (`/`).
    
    
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      name: samplepod
      annotations:
        k8s.v1.cni.cncf.io/networks: NAMESPACE/NAD_NAME
    spec:
      containers:
      ...
    

Replace the following:

  * `NAMESPACE`: the namespace. Use `default` for the default namespace, which is standard. See Security concerns for an exception.
  * `NAD_NAME`: the name of the `NetworkAttachmentDefinition` custom resource.



Use a comma-separated list to specify multiple network interfaces.

In the following example, two network interfaces are assigned to the `samplepod` Pod. The network interfaces are specified by names of two `NetworkAttachmentDefinition` custom resources, `gke-network-1` and `gke-network-2`, in the default namespace of the target cluster.
    
    
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      name: samplepod
      annotations:
        k8s.v1.cni.cncf.io/networks: default/gke-network-1,default/gke-network-2
    spec:
      containers:
      ...
    

### Restrict network interfaces to a NodePool

Use the `k8s.v1.cni.cncf.io/nodeSelector` annotation to specify the pool of nodes for which a `NetworkAttachmentDefinition` custom resource is valid. Google Distributed Cloud forces any pods that reference this custom resource to be deployed on those specific nodes. In the following example, Google Distributed Cloud forces deployment of all pods that are assigned the `gke-network-1` network interface to the `multinicNP` NodePool. Google Distributed Cloud labels a NodePool with the `baremetal.cluster.gke.io/node-pool` label accordingly.
    
    
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      annotations:
        k8s.v1.cni.cncf.io/nodeSelector: baremetal.cluster.gke.io/node-pool=multinicNP
      name: gke-network-1
    spec:
    ...
    

You are not limited to using the standard labels. You can create your own, custom pools from the cluster nodes by applying a custom label to those nodes. Use the `kubectl label nodes` command to apply a custom label:
    
    
    kubectl label nodes NODE_NAME LABEL_KEY=LABEL_VALUE
    

Replace the following:

  * `NODE_NAME`: the name of the Node you are labeling.
  * `LABEL_KEY`: the key to use for your label.
  * `LABEL_VALUE`: the label name.



Once the node is labeled, apply the `baremetal.cluster.gke.io/label-taint-no-sync` annotation on that node to prevent Google Distributed Cloud from reconciling the labels. Use the `kubectl get nodes --show-labels` command to verify if a node is labeled.

### Security concerns

A `NetworkAttachmentDefinition` custom resource provides full access to a network, so cluster administrators must be cautious about providing create, update, or delete access to other users. If a given `NetworkAttachmentDefinition` custom resource has to be isolated, it can be placed in a non-default namespace, where only the pods from that namespace can access it. To reconcile `NetworkAttachmentDefinition` custom resources specified in the cluster configuration file, they are always placed in the default namespace.

In the following diagram, pods from the `default` namespace can't access the network interface in the `privileged` namespace.

![Use of namespaces to isolate network traffic](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/nad-namespace-iso.svg)

### Supported CNI plugins

This section lists the [CNI plugins](https://github.com/containernetworking/plugins) supported by the multi-NIC feature for Google Distributed Cloud. Use only the following plugins when specifying a `NetworkAttachmentDefinition` custom resource.

Interface creation:

  * `ipvlan`
  * `macvlan`
  * `bridge`
  * `sriov`



Meta plugins:

  * `portmap`
  * `sbr`
  * `tuning`



IPAM plugins:

  * `host-local`
  * `static`
  * `whereabouts`



### Route configuration

A pod with one or more assigned `NetworkAttachmentDefinition` custom resources has multiple network interfaces. By default, the routing table in this situation is extended with the locally available additional interfaces from assigned `NetworkAttachmentDefinition` custom resources only. The default gateway is still configured to use the master/default interface of the pod, `eth0`.

You can modify this behavior by using the following CNI plugins:

  * `sbr`
  * `static`
  * `whereabouts`



For example, you might want _all_ traffic to go through the default gateway, the default interface. However, some specific traffic goes over one of the non-default interfaces. Traffic can be difficult to disambiguate based on destination IP (normal routing), because the same endpoint is available over both the interface types. In this case, source-based routing (SBR) can help.

#### SBR plugin

The `sbr` plugin gives the application control over routing decisions. The application controls what is used as the source IP address of the connection it establishes. When the application chooses to use the `NetworkAttachmentDefinition` custom resource's IP address for its source IP, packets land in the additional routing table `sbr` has set up. The `sbr` routing table establishes the `NetworkAttachmentDefinition` custom resource's interface as the default gateway. The default gateway IP inside that table is controlled with the `gateway` field inside `whereabouts` or `static` plugins. Provide the `sbr` plugin as a chained plugin. For more information about the `sbr` plugin, including usage information, see [Source-based routing plugin](https://www.cni.dev/plugins/current/meta/sbr/).

The following example shows `"gateway":"21.0.111.254"` set in `whereabouts`, and `sbr` set as chained plugin after `ipvlan`:
    
    
    # ip route
    default via 192.168.0.64 dev eth0  mtu 1500
    192.168.0.64 dev eth0 scope link
    # ip route list table 100
    default via 21.0.111.254 dev net1
    21.0.104.0/21 dev net1 proto kernel scope link src 21.0.111.1
    

#### Static and whereabouts plugins

The `whereabouts` plugin is basically an extension of the `static` plugin and these two share the routing configuration. For a configuration example, see [static IP address management plugin](https://www.cni.dev/plugins/current/ipam/static/). You can define a gateway and route to add to the pod's routing table. You can't, however, modify the default gateway of the pod in this way.

The following example shows the addition of `"routes": [{ "dst": "172.31.0.0/16" }]` in the `NetworkAttachmentDefinition` custom resource:
    
    
    # ip route
    default via 192.168.0.64 dev eth0  mtu 1500
    172.31.0.0/16 via 21.0.111.254 dev net1
    21.0.104.0/21 dev net1 proto kernel scope link src 21.0.111.1
    192.168.0.64 dev eth0 scope link
    

### Configuration examples

This section illustrates some of the common network configurations supported by the multi-NIC feature.

Single network attachment used by multiple pods

![Single network attachment used by multiple pods](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/single-nad-multi-pod.svg)

Multiple network attachments used by single pod

![Multiple network attachments used by single pod](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/multi-nad-single-pod.svg)

Multiple network attachments pointing to same interface used by single pod

![Multiple network attachments pointing to same interface used by single pod](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/multi-nad-same-intfc-single-pod.svg)

Same network attachment used multiple times by single pod

![Same network attachment used multiple times by single pod](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/same-nad-multi-use-single-pod.svg)

## Troubleshoot

If additional network interfaces are misconfigured, the pods to which they are assigned don't start. This section highlights how to find information for troubleshooting issues with the multi-NIC feature.

### Check pod events

[Multus](https://github.com/k8snetworkplumbingwg/multus-cni) reports failures through Kubernetes pod events. Use the following `kubectl describe` command to view events for a given pod:
    
    
    kubectl describe pod POD_NAME
    

### Check logs

For each node, you can find Whereabouts and Multus logs at the following locations:

  * `/var/log/whereabouts.log`
  * `/var/log/multus.log`



### Review pod interfaces

Use the `kubectl exec` command to check your pod interfaces. Once the `NetworkAttachmentDefinition` custom resources are successfully applied, the pod interfaces look like the following output:
    
    
    $ kubectl exec samplepod-5c6df74f66-5jgxs -- ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
    2: net1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default
        link/ether 00:50:56:82:3e:f0 brd ff:ff:ff:ff:ff:ff
        inet 21.0.103.112/21 scope global net1
           valid_lft forever preferred_lft forever
    38: eth0@if39: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
        link/ether 36:23:79:a9:26:b3 brd ff:ff:ff:ff:ff:ff link-netnsid 0
        inet 192.168.2.191/32 scope global eth0
           valid_lft forever preferred_lft forever
    

### Get pod status

Use the `kubectl get` to retrieve the network status for a given pod:
    
    
    kubectl get pods POD_NAME -oyaml
    

Here's a sample output that shows the status of a pod with multiple networks:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        k8s.v1.cni.cncf.io/network-status: |-
          [{
              "name": "",
              "interface": "eth0",
              "ips": [
                  "192.168.1.88"
              ],
              "mac": "36:0e:29:e7:42:ad",
              "default": true,
              "dns": {}
          },{
              "name": "default/gke-network-1",
              "interface": "net1",
              "ips": [
                  "21.0.111.1"
              ],
              "mac": "00:50:56:82:a7:ab",
              "dns": {}
          }]
        k8s.v1.cni.cncf.io/networks: gke-network-1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
