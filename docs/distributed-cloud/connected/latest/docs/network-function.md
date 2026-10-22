---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/network-function/
title: Network Function operator \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:34.232531+00:00
---

# Network Function operator  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/network-function/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Network Function operator Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the specialized Network Function Kubernetes operator that Google Distributed Cloud connected ships with. This operator implements a set of CustomResourceDefinitions (CRDs) that allow Distributed Cloud connected to execute high-performance workloads.

The Network Function operator lets you do the following:

  * Poll for existing network devices on a node.
  * Query the IP address and physical link state for each network device on a node.
  * Provision additional network interfaces on a node.
  * Configure low-level system features on the node's physical machine required to support high-performance workloads.



## Network Function operator profiles

Distributed Cloud connected provides the following Network Function operator functionality:

  * **Network automation** functions let you automate the configuration of your workload Pod networking.

  * **State export** functions let you export host network states to the user, including network interface configuration and status.

  * **Webhook** functions let you validate user inputs.




## Prerequisites

The Network Function operator fetches network configuration from the Distributed Cloud Edge Network API. To allow this, you must grant the Network Function operator service account the Edge Network Viewer role (`roles/edgenetwork.viewer`) using the following command:
    
    
    gcloud projects add-iam-policy-binding ZONE_PROJECT_ID \
      --role roles/edgenetwork.viewer \
      --member "serviceAccount:CLUSTER_PROJECT_ID.svc.id.goog[nf-operator/nf-angautomator-sa]"
    

Replace the following:

  * `ZONE_PROJECT_ID` with the ID of the Google Cloud project that holds the Distributed Cloud Edge Network API resources.
  * `CLUSTER_PROJECT_ID` with the ID of the Google Cloud project that holds the target Distributed Cloud connected cluster.



## Network Function operator resources

The Distributed Cloud connected Network Function operator implements the following Kubernetes CRDs:

  * `Network`. Defines a virtual network that pods can use to communicate with internal and external resources. You must create the corresponding VLAN using the Distributed Cloud Edge Network API before specifying it in this resource. For instructions, see [Create a subnetwork](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking#create_one_or_more_subnetworks).
  * `NetworkInterfaceState`. Enables the discovery of network interface states and querying a network interface for link state and IP address.
  * `NodeSystemConfigUpdate`. Enables the configuration of low-level system features such as kernel options and `Kubelet` flags.
  * `NetworkAttachmentDefinition`. Lets you attach Distributed Cloud pods to one or more logical or physical networks on your Distributed Cloud connected node. You must create the corresponding VLAN using the Distributed Cloud Edge Network API before specifying it in this resource. For instructions, see [Create a subnetwork](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking#create_one_or_more_subnetworks).



The Network Function operator also lets you define secondary network interfaces.

### `Network` resource

The `Network` resource defines a virtual network within your Distributed Cloud connected deployment that pods within your Distributed Cloud connected cluster can use to communicate with internal and external resources.

The `Network` resource provides the following configurable parameters for the network interface exposed as writable fields:

  * `spec.type`: specifies the network transport layer for this network. The only valid value is `L2`. You must also specify a `nodeInterfaceMatcher.interfaceName` value.
  * `spec.nodeInterfaceMatcher.interfaceName`: the name of the physical network interface on the target Distributed Cloud connected node to use with this network.
  * `spec.gateway4`: the IP address of the network gateway for this network.
  * `spec.l2NetworkConfig.prefixLength4`: specifies the CIDR range for this network.
  * `annotations.networking.gke.io/gdce-per-node-ipam-size`: specifies the subnet mask size for an individual node. If this is omitted, the subnet mask size is set to the value of the `cluster-cidr-config-per-node-mask-size` field in the `nf-operator-defaults` ConfigMap in the `nf-operator` namespace.
  * `annotations.networking.gke.io/gke-gateway-clusterip-cidr`: specifies a CIDR block for accessing clusters through Connect gateway. This is used by `CoreDNS` on secondary network interfaces.
  * `annotations.networking.gke.io/gke-gateway-pod-cidr`: specifies a CIDR block for a Pod that can be allocated on secondary network interfaces.
  * `annotations.networking.gke.io/gdce-vlan-id`: specifies the VLAN ID for this network.
  * `annotations.networking.gke.io/gdce-vlan-mtu`: (optional) specifies the MTU value for this network. If omitted, inherits the MTU value from the parent interface.
  * `annotations.networking.gke.io/gdce-lb-service-vip-cidr`: specifies the virtual IP address range for the load balancing service. The value can be a CIDR block or an explicit address range value. This annotation is mandatory for Layer 3 and optional for Layer 2 load balancing.



The following example illustrates the structure of the resource:
    
    
    apiVersion: networking.gke.io/v1
    kind: Network
    metadata:
      name: vlan200-network
      annotations:
        networking.gke.io/gdce-vlan-id: 200
        networking.gke.io/gdce-vlan-mtu: 1500
        networking.gke.io/gdce-lb-service-vip-cidrs: "10.1.1.0/24"
    spec:
      type: L2
      nodeInterfaceMatcher:
        interfaceName: gdcenet0.200
      gateway4: 10.53.0.1
    

To specify multiple virtual IP address ranges for the load balancing service, use the `networking.gke.io/gdce-lb-service-vip-cidrs` annotation. You can provide the values for this annotation as either a comma-separated list or as a JSON payload. For example:
    
    
    [
      {
        "name": "test-oam-3",
        "addresses": ["10.235.128.133-10.235.128.133"],
        "autoAssign": false
      }
      ,
      {
        "name": "test-oam-4",
        "addresses": ["10.235.128.134-10.235.128.134"],
        "autoAssign": false
      },
      {
        "name": "test-oam-5",
        "addresses": ["10.235.128.135-10.235.128.135"],
        "autoAssign": false
      }
    ]
    

If you choose to use a JSON payload, we recommend that you use the condensed JSON format. For example:
    
    
    apiVersion: networking.gke.io/v1
      kind: Network
      metadata:
        annotations:
          networking.gke.io/gdce-lb-service-vip-cidrs: '[{"name":"test-oam-3","addresses":["10.235.128.133-10.235.128.133"],"autoAssign":false},{"name":"test-oam-4","addresses":["10.235.128.134-10.235.128.134"],"autoAssign":false},{"name":"test-oam-5","addresses":["10.235.128.135-10.235.128.135"],"autoAssign":false}]'
          networking.gke.io/gdce-vlan-id: "81"
        name: test-network-vlan81
      spec:
        IPAMMode: Internal
        dnsConfig:
          nameservers:
          - 8.8.8.8
        gateway4: 192.168.81.1
        l2NetworkConfig:
          prefixLength4: 24
        nodeInterfaceMatcher:
          interfaceName: gdcenet0.81
        type: L2
    

Keep in mind that the `autoAssign` field defaults to `false` if omitted. 

### `NetworkInterfaceState` resource

The `NetworkInterfaceState` resource is a read-only resource that lets you discover physical network interfaces on the node and collect runtime statistics on the network traffic flowing through those interfaces. Distributed Cloud creates a `NetworkInterfaceState` resource for each node in a cluster.

The default configuration of Distributed Cloud connected machines includes a bonded network interface named `uplink0`. This interface bonds the `eno1np0` and `eno2np1` network interfaces. Each of those is connected to one Distributed Cloud ToR switch, respectively.

The `NetworkInterfaceState` resource provides the following categories of network interface information exposed as read-only status fields.

General information:

  * `status.interfaces.ifname`: the name of the target network interface.
  * `status.lastReportTime`: the time and date of the last status report for the target interface.



IP address configuration information:

  * `status.interfaces.interfaceinfo.address`: the IP address assigned to the target interface.
  * `status.interfaces.interfaceinfo.dns`: the IP address of the DNS server assigned to the target interface.
  * `status.interfaces.interfaceinfo.gateway`: the IP address of the network gateway serving the target interface.
  * `status.interfaces.interfaceinfo.prefixlen`: the length of the IP prefix.



Hardware information:

  * `status.interfaces.linkinfo.broadcast`: the broadcast MAC address of the target interface.
  * `status.interfaces.linkinfo.businfo`: the PCIe device path in `bus:slot.function` format.
  * `status.interfaces.linkinfo.flags`: the interface flags—for example, `BROADCAST`.
  * `status.interfaces.linkinfo.macAddress`: the Unicast MAC address of the target interface.
  * `status.interfaces.linkinfo.mtu`: the MTU value for the target interface.



Reception statistics:

  * `status.interfaces.statistics.rx.bytes`: the total bytes received by the target interface.
  * `status.interfaces.statistics.rx.dropped`: the total packets dropped by the target interface.
  * `status.interfaces.statistics.rx.errors`: the total packet receive errors for the target interface.
  * `status.interfaces.statistics.rx.multicast`: the total multicast packets received by the target interface.
  * `status.interfaces.statistics.rx.overErrors`: the total packet receive over errors for the target interface.
  * `status.interfaces.statistics.rx.packets`: the total packets received by the target interface.



Transmission statistics:

  * `status.interfaces.statistics.tx.bytes`: the total bytes transmitted by the target interface.
  * `status.interfaces.statistics.tx.carrierErrors`: the total carrier errors encountered by the target interface.
  * `status.interfaces.statistics.tx.collisions`: the total packet collisions encountered by the target interface.
  * `status.interfaces.statistics.tx.dropped`: the total packets dropped by the target interface.
  * `status.interfaces.statistics.tx.errors`: the total transmission errors for the target interface.
  * `status.interfaces.statistics.tx.packets`: the total packets transmitted by the target interface.



The following example illustrates the structure of the resource:
    
    
    apiVersion: networking.gke.io/v1
    kind: NetworkInterfaceState
    metadata:
      name: MyNode1
    nodeName: MyNode1
    status:
      interfaces:
      - ifname: eno1np0
        linkinfo:
          businfo: 0000:1a:00.0
          flags: up|broadcast|multicast
          macAddress: ba:16:03:9e:9c:87
          mtu: 9000
        statistics:
          rx:
            bytes: 1098522811
            errors: 2
            multicast: 190926
            packets: 4988200
          tx:
            bytes: 62157709961
            packets: 169847139
      - ifname: eno2np1
        linkinfo:
          businfo: 0000:1a:00.1
          flags: up|broadcast|multicast
          macAddress: ba:16:03:9e:9c:87
          mtu: 9000
        statistics:
          rx:
            bytes: 33061895405
            multicast: 110203
            packets: 110447356
          tx:
            bytes: 2370516278
            packets: 11324730
      - ifname: enp95s0f0np0
        interfaceinfo:
        - address: fe80::63f:72ff:fec4:2bf4
          prefixlen: 64
        linkinfo:
          businfo: 0000:5f:00.0
          flags: up|broadcast|multicast
          macAddress: 04:3f:72:c4:2b:f4
          mtu: 9000
        statistics:
          rx:
            bytes: 37858381
            multicast: 205645
            packets: 205645
          tx:
            bytes: 1207334
            packets: 6542
      - ifname: enp95s0f1np1
        interfaceinfo:
        - address: fe80::63f:72ff:fec4:2bf5
          prefixlen: 64
        linkinfo:
          businfo: 0000:5f:00.1
          flags: up|broadcast|multicast
          macAddress: 04:3f:72:c4:2b:f5
          mtu: 9000
        statistics:
          rx:
            bytes: 37852406
            multicast: 205607
            packets: 205607
          tx:
            bytes: 1207872
            packets: 6545
      - ifname: enp134s0f0np0
        interfaceinfo:
        - address: fe80::63f:72ff:fec4:2b6c
          prefixlen: 64
        linkinfo:
          businfo: 0000:86:00.0
          flags: up|broadcast|multicast
          macAddress: 04:3f:72:c4:2b:6c
          mtu: 9000
        statistics:
          rx:
            bytes: 37988773
            multicast: 205584
            packets: 205584
          tx:
            bytes: 1212385
            packets: 6546
      - ifname: enp134s0f1np1
        interfaceinfo:
        - address: fe80::63f:72ff:fec4:2b6d
          prefixlen: 64
        linkinfo:
          businfo: 0000:86:00.1
          flags: up|broadcast|multicast
          macAddress: 04:3f:72:c4:2b:6d
          mtu: 9000
        statistics:
          rx:
            bytes: 37980702
            multicast: 205548
            packets: 205548
          tx:
            bytes: 1212297
            packets: 6548
      - ifname: gdcenet0
        interfaceinfo:
        - address: 208.117.254.36
          prefixlen: 28
        - address: fe80::b816:3ff:fe9e:9c87
          prefixlen: 64
        linkinfo:
          flags: up|broadcast|multicast
          macAddress: ba:16:03:9e:9c:87
          mtu: 9000
        statistics:
          rx:
            bytes: 34160422968
            errors: 2
            multicast: 301129
            packets: 115435591
          tx:
            bytes: 64528301111
            packets: 181171964
         .. <remaining interfaces omitted>
       lastReportTime: "2022-03-30T07:35:44Z"
    

## Configure a secondary interface on a pod using Distributed Cloud multi-networking

Distributed Cloud connected supports creating a secondary network interface on a pod by using its multi-network feature. To do so, complete the following steps:

  1. Configure a `Network` resource. For example:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: my-network-410
           annotations:
               networking.gke.io/gdce-vlan-id: "410"
               networking.gke.io/gdce-lb-service-vip-cidrs: '[{"name":"myPool","addresses":["10.100.63.130-10.100.63.135"],"avoidBuggyIPs":false,"autoAssign":true}]'
         spec:
           type: L2
           nodeInterfaceMatcher:
             interfaceName: gdcenet0.410
           gateway4: 10.100.63.129
           l2NetworkConfig:
             prefixLength4: 27
         

The `networking.gke.io/gdce-lb-service-vip-cidrs` annotation specifies one or more IP address pools for this virtual network. The CIDR that you specify here must be a subset of the first half of the VLAN CIDR for the network. Distributed Cloud connected enforces this requirement through webhook checks as follows:

     * The Service Virtual IP (SVIP) address range must be within the corresponding VLAN CIDR range.
     * The SVIP address range can only span up to the first half of the VLAN CIDR range.
  2. Add an annotation to your Distributed Cloud pod definition as follows:
         
         apiVersion: v1
         kind: pod
         metadata:
           name: myPod
           annotations:
             networking.gke.io/interfaces: '[{"interfaceName":"eth0","network":"pod-network"}, {"interfaceName":"eth1","network":"my-network-410"}]'
             networking.gke.io/default-interface: eth1
         

When you provide this annotation to the `Network` resource, Layer 2 load balancing with MetalLB is automatically configured. This annotation configures the `eth0` interface as primary and the `eth1` interface as secondary with Layer 2 load balancing with MetalLB.




Configuring your secondary interface as described in this section results in the automatic creation of the following custom resources:

  * An `IPAddressPool` resource, which enables automatic SVIP address assignment to Pods. For example:


    
    
    apiVersion: metallb.io/v1beta1
    kind: IPAddressPool
    metadata:
      name: test-410-pool
      namespace: kube-system
      annotations:
        networking.gke.io/network:my-network-410
        …
      spec:
      addresses:
      - 10.100.63.130-10.100.63.135
      autoAssign: true
    

  * An `L2Advertisement` resource, which enables advertising of the specified SVIP addresses. For example:


    
    
    apiVersion: metallb.io/v1beta1
    kind: L2Advertisement
    metadata:
      name: l2advertise-410
      namespace: kube-system
    spec:
      ipAddressPools:
      - test-410-pool
      interfaces:
      - gdcenet0.410
    

## What's next

  * [Installation requirements](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/requirements)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
