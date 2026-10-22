---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic/
title: Configure multiple network interfaces for Pods \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:55.510556+00:00
---

# Configure multiple network interfaces for Pods  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure multiple network interfaces for Pods Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Google Distributed Cloud (software only) for VMware to provide multiple network interfaces, multi-NIC, for your Pods. The multi-NIC for Pods feature can help separate control plane traffic from data plane traffic, creating isolation between planes. Additional network interfaces also enable multicast capability for your Pods. Multi-NIC for Pods is supported for user clusters, it is not allowed for admin clusters.

This page is for Networking specialists who install, configure, and support network equipment. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Network plane isolation is important for systems using network functions virtualizations (NFVs), such as software-defined networking in a wide area network (SD-WAN), a cloud access security broker (CASB), and next-generation firewalls (NG-FWs). These types of NFVs rely on access to multiple interfaces to keep the control and data planes separate.

The multiple network interface configuration supports associating network interfaces with node pools, which can provide performance benefits. For example, a cluster can contain a mix of node types. When you group high-performance machines into one node pool, you can create additional interfaces to the node pool to improve traffic flow.

## Set up multiple network interfaces

Generally, there are three steps to set up multiple network interfaces for your Pods:

  1. Enable multi-NIC for your user cluster by using the `multipleNetworkInterfaces` and `enableDataplaneV2` fields in the cluster configuration file.

  2. Specify network interfaces with the `additionalNodeInterfaces` section in the cluster configuration file, and create one or more `NetworkAttachmentDefinition` custom resources.

  3. Assign network interfaces to Pods with the `k8s.v1.cni.cncf.io/networks` annotation.




### Enable multi-NIC

Enable multi-NIC for your Pods by setting the `multipleNetworkInterfaces` and `enableDataplaneV2` fields in the user cluster configuration file to `true`.
    
    
    apiVersion: v1
    multipleNetworkInterfaces: true
    enableDataplaneV2: true
      ...
    

### Specify network interfaces

In the cluster configuration file, specify additional node network interfaces in the `additionalNodeInterfaces` section.

For example, here is a portion of a user cluster configuration file showing an additional node network interface:
    
    
    apiVersion: v1
    multipleNetworkInterfaces: true
    enableDataplaneV2: true
    network:
      serviceCIDR: "10.96.0.0/20"
      podCIDR: "192.168.0.0/16"
      vCenter:
        networkName: network-private310
      ...
      # New multiple network configs
      additionalNodeInterfaces:
      - networkName: "gke-network-1"
        ipBlockFilePath: "my-block-yaml"
        type: static
    

After creating a cluster with the preceding configuration, you have to create one or more `NetworkAttachmentDefinition` (NAD) custom resources in your user cluster where you specify additional network interfaces. The `NetworkAttachmentDefinitions` correspond to the networks that are available for your Pods. The following example shows a manifest for a `NetworkAttachmentDefinition`:
    
    
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: gke-network-1
      namespace: default
    spec:
      config: '{
      "cniVersion":"0.3.0",
      "type": "ipvlan",
      "master": "ens224", # defines the node interface that this Pod interface would map to
      "mode": "l2",
      "ipam": {
        "type": "whereabouts",
        "range": "172.16.0.0/24"
       }
    }'
    

Save the manifest as a YAML file, for example, `my-nad.yaml`, and create the `NetworkAttachmentDefinition`:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] apply -f my-nad.yaml

### Assign network interfaces to a Pod

Use the `k8s.v1.cni.cncf.io/networks` annotation to assign one or more network interfaces to a Pod. Each network interface is specified with a namespace and the name of a `NetworkAttachmentDefinition`, separated by a forward slash (`/`). Use a comma-separated list to specify multiple network interfaces.

In the following example, two network interfaces are assigned to the `samplepod` Pod. The network interfaces are specified by names of two `NetworkAttachmentDefinitions`, `gke-network-1` and `gke-network-2`, that were created in the `default` namespace.
    
    
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
    

### Restrict network interfaces to a set of nodes

If you do not want a `NetworkAttachmentDefinition` to be applicable to an entire cluster, you can limit its functionality to a set of nodes.

You can group cluster nodes either by using the standard label assigned to the node or your own custom label. You can then specify the node label in the `NetworkAttachmentDefinition` manifest using the `k8s.v1.cni.cncf.io/nodeSelector` annotation. Google Distributed Cloud forces any Pods that reference this custom resource to be deployed on those nodes that have this label.
    
    
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      annotations:
        k8s.v1.cni.cncf.io/nodeSelector: LABEL_KEY=LABEL_VALUE
      name: gke-network-1
    spec:
    ...
    

The following example shows the `my-label=multinicNP` label indicated on the `NetworkAttachmentDefinition`, and forces deployment of all Pods that are assigned the `gke-network-1` network to the nodes that have this label.
    
    
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      annotations:
        k8s.v1.cni.cncf.io/nodeSelector: my-label=multinicNP
      name: gke-network-1
    spec:
    ...
    

To apply a custom label to a node, use the `kubectl label nodes` command:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] label nodes NODE_NAME LABEL_KEY=LABEL_VALUE 

Replace the following:

  * `NODE_NAME`: the name of the Node you are labeling.
  * `LABEL_KEY`: the key to use for your label.
  * `LABEL_VALUE`: the label value.



In this example, the node `my-node` is given the `environment=production` label:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] label nodes my-node environment=production

### Security concerns

A `NetworkAttachmentDefinition` provides full access to a network, so cluster administrators must be cautious about providing create, update, or delete access to other users. If a given `NetworkAttachmentDefinition` has to be isolated, you can specify a non-default namespace when creating it, where only the Pods from that namespace can access it. 

In the following diagram, Pods from the `default` namespace can't access the network interface in the `privileged` namespace.

![Use of namespaces to isolate network traffic.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/nad-namespace-iso.svg)

### Supported CNI plugins

This section lists the [CNI plugins](https://github.com/containernetworking/plugins) supported by the multi-NIC feature for Google Distributed Cloud. Use only the following plugins when specifying a `NetworkAttachmentDefinition`.

Interface creation:

  * `ipvlan`
  * `macvlan`
  * `bridge`



Meta plugins:

  * `portmap`
  * `sbr`
  * `tuning`



IPAM plugins:

  * `host-local`
  * `static`
  * `whereabouts`



### Route configuration

A Pod with one or more assigned `NetworkAttachmentDefinitions` has multiple network interfaces. By default, the Pod's routing table in this situation is extended with the locally available additional interfaces from assigned `NetworkAttachmentDefinitions` only. Packets bound for the default gateway are still configured to use the default interface of the Pod, `eth0`. You can modify this behavior by using the following CNI plugins:

  * `sbr`
  * `static`
  * `whereabouts`



For example, you might want most traffic to go through the default gateway, which means the traffic will go over the default network interface. However, you want some specific traffic to go over one of the non-default interfaces. Traffic can be difficult to disambiguate based on destination IP (normal routing), because the same endpoint is available over both the interface types. In this case, source-based routing (SBR) can help.

### SBR plugin

The `sbr` plugin gives the application control over routing decisions. The application controls what is used as the source IP address of the connection it establishes. When the application chooses to use the `NetworkAttachmentDefinition`'s IP address for its source IP, packets land in the additional routing table `sbr` has set up. The `sbr` routing table sends traffic through its own default gateway, which will go over the `NetworkAttachmentDefinition`'s interface. The default gateway IP inside that table is controlled with the `gateway` field inside `whereabouts` or `static` plugins. The `sbr` plugin runs as a chained plugin. For more information about the `sbr` plugin, including usage information, see [Source-based routing plugin](https://www.cni.dev/plugins/current/meta/sbr/).

The following example shows `"gateway":"21.0.111.254"` set in `whereabouts`, and `sbr` set as chained plugin after `ipvlan`:
    
    
    # ip route
    default via 192.168.0.64 dev eth0  mtu 1500
    192.168.0.64 dev eth0 scope link
    # ip route list table 100
    default via 21.0.111.254 dev net1
    21.0.104.0/21 dev net1 proto kernel scope link src 21.0.111.1
    

#### Static and whereabouts plugins

The `whereabouts` plugin is basically an extension of the `static` plugin and these two share the routing configuration. For a configuration example, see [static IP address management plugin](https://www.cni.dev/plugins/current/ipam/static/). You can define a gateway and route to add to the Pod's routing table. You can't, however, modify the default gateway of the Pod in this way.

The following example shows the addition of `"routes": [{ "dst": "172.31.0.0/16" }]` in the `NetworkAttachmentDefinition`:
    
    
    # ip route
    default via 192.168.0.64 dev eth0  mtu 1500
    172.31.0.0/16 via 21.0.111.254 dev net1
    21.0.104.0/21 dev net1 proto kernel scope link src 21.0.111.1
    192.168.0.64 dev eth0 scope link
    

### Configuration examples

This section illustrates some of the common network configurations supported by the multi-NIC feature.

Single network attachment used by multiple Pods:

![Single network attachment used by multiple pods.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/single-nad-multi-pod.svg)

Multiple network attachments used by single Pod:

![Multiple network attachments used by single pod.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/multi-nad-single-pod.svg)

Multiple network attachments pointing to same interface used by single Pod:

![Multiple network attachments pointing to same interface used by single pod.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/multi-nad-same-intfc-single-pod.svg)

Same network attachment used multiple times by single Pod:

![Same network attachment used multiple times by single pod.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/same-nad-multi-use-single-pod.svg)

## Troubleshoot

If additional network interfaces are misconfigured, the Pods to which they are assigned don't start. This section highlights how to find information for troubleshooting issues with the multi-NIC feature.

### Check Pod events

[Multus](https://github.com/k8snetworkplumbingwg/multus-cni) reports failures through Kubernetes Pod events. Use the following `kubectl describe` command to view events for a given Pod:
    
    
    kubectl describe pod POD_NAME
    

### Check logs

For each node, you can find Whereabouts and Multus logs at the following locations:

  * `/var/log/whereabouts.log`
  * `/var/log/multus.log`



### Review Pod interfaces

Use the `kubectl exec` command to check your Pod interfaces. Once the `NetworkAttachmentDefinitions` are successfully applied, the Pod interfaces look like the following output:
    
    
    user@node1:~$ kubectl exec samplepod-5c6df74f66-5jgxs -- ip a
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
    

### Get Pod status

Use the `kubectl get` to retrieve the network status for a given Pod:
    
    
    kubectl get pods POD_NAME -oyaml
    

Here's a sample output that shows the status of a Pod with multiple networks:
    
    
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

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
