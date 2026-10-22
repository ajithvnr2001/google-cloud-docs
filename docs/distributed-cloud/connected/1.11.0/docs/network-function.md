---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/network-function/
title: Network Function operator \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:53.680087+00:00
---

# Network Function operator  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/network-function/

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
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/overview)



Send feedback 

#  Network Function operator Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the specialized Network Function Kubernetes operator that Google Distributed Cloud connected ships with. This operator implements a set of CustomResourceDefinitions (CRDs) that allow Distributed Cloud connected to execute high-performance workloads.

The Network Function operator lets you do the following:

  * Poll for existing network devices on a node.
  * Query the IP address and physical link state for each network device on a node.
  * Provision additional network interfaces on a node.
  * Configure low-level system features on the node's physical machine required to support high-performance workloads.
  * Use single-root input/output virtualization (SR-IOV) on PCI Express network interfaces to virtualize them into multiple virtual interfaces. You can then configure your Distributed Cloud connected workloads to use those virtual network interfaces.



Distributed Cloud connected support for SR-IOV is based on the following open source projects:

  * [Kubernetes SR-IOV Network Operator](https://github.com/k8snetworkplumbingwg/sriov-network-operator)
  * [Multus-CNI plugin](https://github.com/k8snetworkplumbingwg/multus-cni)
  * [SRIOV-CNI plugin](https://github.com/k8snetworkplumbingwg/sriov-cni)



## Network Function operator profiles

Distributed Cloud connected provides the following Network Function operator functionality profiles on each Distributed Cloud connected form factor:

  * **Distributed Cloud connected racks** support the full Network Function operator functionality profile with the following features:

    * **Network automation** functions let you automate the configuration of your workload Pod networking. For example, configuring BGP peering and secondary network interfaces.

    * **State export** functions let you export host network states to the user, including network interface configuration and status.

    * **Node configuration** functions let you fine-tune a node's performance to fit your business needs, including CPU isolation, huge page, realtime kernel, `kubelet` parameters, and `sysctl`.

    * **Power management** functions let you manage power consumption on a node, including P-states and C-states of isolated CPUs.

    * **Webhook** functions let you validate user inputs.

    * **Miscellaneous** functions include the SR-IOV automator that automatically configures the SR-IOV operator.

  * **Distributed Cloud connected servers** support the performance-optimized Network Function operator functionality profile with the following features:

    * **Network automation** functions let you automate the configuration of your workload Pod networking. For example, configuring BGP peering and secondary network interfaces.

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

  * `Network`. Defines a virtual network that pods can use to communicate with internal and external resources. You must create the corresponding VLAN using the Distributed Cloud Edge Network API before specifying it in this resource. For instructions, see [Create a subnetwork](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networking#create_one_or_more_subnetworks).
  * `NetworkInterfaceState`. Enables the discovery of network interface states and querying a network interface for link state and IP address.
  * `NodeSystemConfigUpdate`. Enables the configuration of low-level system features such as kernel options and `Kubelet` flags.
  * `SriovNetworkNodePolicy`. Selects a group of SR-IOV virtualized network interfaces and instantiates the group as a Kubernetes resource. You can use this resource in a `NetworkAttachmentDefinition` resource.
  * `SriovNetworkNodeState`. Lets you query the provisioning state of the `SriovNetworkNodePolicy` resource on a Distributed Cloud node.
  * `NetworkAttachmentDefinition`. Lets you attach Distributed Cloud pods to one or more logical or physical networks on your Distributed Cloud connected node. You must create the corresponding VLAN using the Distributed Cloud Edge Network API before specifying it in this resource. For instructions, see [Create a subnetwork](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networking#create_one_or_more_subnetworks).



The Network Function operator also lets you define secondary network interfaces that do not use SR-IOV virtual functions.

### `Network` resource

The `Network` resource defines a virtual network within the Distributed Cloud connected rack that pods within your Distributed Cloud connected cluster can use to communicate with internal and external resources.

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

The default configuration of Distributed Cloud connected machines includes a bonded network interface on the Rack Select Network Daughter Card (rNDC) named `gdcenet0`. This interface bonds the `eno1np0` and `eno2np1` network interfaces. Each of those is connected to one Distributed Cloud ToR switch, respectively.

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
    

### `NodeSystemConfigUpdate` resource

The `NodeSystemConfigUpdate` resource lets you make changes to the node's operating system configuration as well as modify `Kubelet` flags. Changes other than `sysctl` changes require a node reboot. This resource is not available on Distributed Cloud connected servers deployments.

When instantiating this resource, you must specify the target nodes in the `nodeSelector` field. You must include all key-value pairs for each target node in the `nodeSelector` field. When you specify more than one target node in this field, the target nodes are updated one node at a time.

CAUTION: The `nodeName` field has been deprecated. Using it immediately reboots the target nodes, including local control plane nodes, which can halt critical workloads.

The `NodeSystemConfigUpdate` resource provides the following configuration fields specific to Distributed Cloud connected:

  * `spec.containerRuntimeDNSConfig.ip`: specifies a list of IP addresses for private image registries.
  * `spec.containerRuntimeDNSConfig`: specifies a list of custom DNS entries used by the Container Runtime Environment on each Distributed Cloud connected node. Each entry consists of the following fields:

    * `ip`: specifies the target IPv4 address,
    * `domain`: specifies the corresponding domain,
    * `interface`: specifies the network egress interface through which the IP address specified in the `ip` field is reachable. You can specify an interface defined through the following resources: `CustomNetworkInterfaceConfig`, `Network` (by annotation), `NetworkAttachmentDefinition`, (by annotation).
  * `spec.kubeletConfig.cpuManagerPolicy`: specifies the Kubernetes CPUManager policy. Valid values are `None` and `Static`.

  * `spec.kubeletConfig.topologyManagerPolicy`: specifies the Kubernetes `TopologyManager` policy. Valid values are `None`, `BestEffort`, `Restricted`, and `SingleNumaMode`.

  * `spec.osConfig.cgroupConfig.noKernelMemory`: excludes kernel-space memory from Pod memory usage calculation. Valid values are `true` and `false`.

  * `spec.osConfig.hugePagesConfig`: specifies the huge page configuration per NUMA node. Valid values are `2MB` and `1GB`. The number of huge pages requested is evenly distributed across both NUMA nodes in the system. For example, if you allocate 16 huge pages at 1 GB each, then each node receives a pre-allocation of 8 GB.

  * `spec.osConfig.isolatedCpusPerSocket`: specifies the number of isolated CPUs per socket. Required if `cpuManagerPolicy` is set to `Static`. The maximum number of isolated CPUs must be fewer than 80% of the total CPUs in the node.

  * `spec.osConfig.cpuIsolationPolicy`: specifies the CPU isolation policy. The `Default` policy only isolates `systemd` tasks from CPUs reserved for workloads. The `Kernel` policy marks the CPUs as `isolcpus` and sets the `rcu_nocb`, `nohz_full`, and `rcu_nocb_poll` flags on each CPU. The `KernelOptimized` policy marks the CPUs as `isolcpus` and sets the `rcu_nocb` and `rcu_nocb_poll` flags on each CPU, but not the `nohz_full` flag.

  * `spec.sysctls.NodeLevel`: specifies the `sysctls` parameters that you can configure globally on a node by using the Network Function operator. The configurable parameters are as follows:

    * `fs.inotify.max_user_instances`
    * `fs.inotify.max_user_watches`
    * `kernel.sched_rt_runtime_us`
    * `kernel.core_pattern`
    * `net.ipv4.tcp_wmem`
    * `net.ipv4.tcp_rmem`
    * `net.ipv4.tcp_slow_start_after_idle`
    * `net.ipv4.udp_rmem_min`
    * `net.ipv4.udp_wmem_min`
    * `net.ipv4.tcp_rmem`
    * `net.ipv4.tcp_wmem`
    * `net.core.rmem_max`
    * `net.core.wmem_max`
    * `net.core.rmem_default`
    * `net.core.wmem_default`
    * `net.netfilter.nf_conntrack_tcp_timeout_unacknowledged`
    * `net.netfilter.nf_conntrack_tcp_timeout_max_retrans`
    * `net.sctp.auth_enable`
    * `net.sctp.sctp_mem`
    * `net.ipv4.udp_mem`
    * `net.ipv4.tcp_mem`
    * `net.ipv4.tcp_slow_start_after_idle`
    * `net.sctp.auth_enable`
    * `vm.max_map_count`

You can also scope both safe and unsafe `sysctls` parameters to a specific pod or namespace by using the [`tuning` Container Networking Interface (CNI) plug-in](https://www.cni.dev/plugins/current/meta/tuning/).




The `NodeSystemConfigUpdate` resource provides the following read-only general status fields:

  * `status.lastReportTime`: the most recent time that status was reported for the target interface.
  * `status.conditions.lastTransitionTime`: the most recent time that the condition of the interface has changed.
  * `status.conditions.observedGeneration`: denotes the `.metadata.generation` value on which the initial condition was based.
  * `status.conditions.message`: an informative message describing the change of the interface's condition.
  * `status.conditions.reason`: a programmatic identifier denoting the reason for the last change of the interface's condition.
  * `status.conditions.status`: the status descriptor of the condition. Valid values are `True`, `False`, and `Unknown`.
  * `status.conditions.type`: the condition type in camelCase.



The following example illustrates the structure of the resource:
    
    
    apiVersion: networking.gke.io/v1
    kind: NodeSystemConfigUpdate
    metadata:
      name: node-pool-1-config
      namespace: default
    spec:
      nodeSelector:
        baremetal.cluster.gke.io/node-pool: node-pool-1
        networking.gke.io/worker-network-sriov.capable: true
      sysctls:
        nodeLevel:
          "net.ipv4.udp_mem" : "12348035 16464042 24696060"
      kubeletConfig:
        topologyManagerPolicy: BestEffort
        cpuManagerPolicy: Static
      osConfig:
        hugePagesConfig:
          "TWO_MB": 0
          "ONE_GB": 16
        isolatedCpusPerSocket:
          "0": 10
          "1": 10
    

### `SriovNetworkNodePolicy` resource

The `SriovNetworkNodePolicy` resource lets you allocate a group of SR-IOV virtual functions (VFs) on a Distributed Cloud connected physical machine and instantiate that group as a Kubernetes resource. You can then use this resource in a `NetworkAttachmentDefinition` resource. This resource is not available on Distributed Cloud connected servers deployments

You can select each target VF by its PCIe vendor and device ID, its PCIe device addresses, or by its Linux enumerated device name. The SR-IOV Network Operator configures each physical network interface to provision the target VFs. This includes updating the network interface firmware, configuring the Linux kernel driver, and rebooting the Distributed Cloud connected machine, if necessary.

To discover the network interfaces available on your node, you can look up the `NetworkInterfaceState` resources on that node in the `nf-operator` namespace.

The following example illustrates the structure of the resource:
    
    
    apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: mlnx6-p2-sriov-en2
      namespace: sriov-network-operator
    spec:
      deviceType: netdevice
      isRdma: true
      mtu: 9000
      nicSelector:
        pfNames:
        - enp134s0f1np1
      nodeSelector:
        edgecontainer.googleapis.com/network-sriov.capable: "true"
      numVfs: 31
      priority: 99
      resourceName: mlnx6_p2_sriov_en2
    

The preceding example creates a maximum of 31 VFs from the second port on the network interface named `enp134s0f1np1` with an MTU value of `9000` (the maximum allowed value). Use the node selector label `edgecontainer.googleapis.com/network-sriov.capable`, which is present on all Distributed Cloud connected nodes capable of SR-IOV.

For information about using this resource, see [`SriovNetworkNodeState`](https://github.com/k8snetworkplumbingwg/sriov-network-operator#sriovnetworknodepolicy).

### `SriovNetworkNodeState` resource

The `SriovNetworkNodeState` read-only resource lets you query the provisioning state of the `SriovNetworkNodePolicy` resource on a Distributed Cloud connected node. It returns the complete configuration of the `SriovNetworkNodePolicy` resource on the node as well as a list of active VFs on the node. The `status.syncStatus` field indicates whether all `SriovNetworkNodePolicy` resources defined for the node have been properly applied. This resource is not available on Distributed Cloud connected servers deployments

The following example illustrates the structure of the resource:
    
    
    apiVersion: sriovnetwork.k8s.cni.cncf.io/v1
    kind: SriovNetworkNodeState
    metadata:
      name: MyNode1
      namespace: sriov-network-operator
    spec:
      dpConfigVersion: "1969684"
      interfaces:
      - mtu: 9000
        name: enp134s0f1np1
        numVfs: 31
        pciAddress: 0000:86:00.1
        vfGroups:
        - deviceType: netdevice
          mtu: 9000
          policyName: mlnx6-p2-sriov-en2
          resourceName: mlnx6_p2_sriov_en2
          vfRange: 0-30
    status:
    
    Status:
      Interfaces:
        Device ID:    1015
        Driver:       mlx5_core
        Link Speed:   25000 Mb/s
        Link Type:    ETH
        Mac:          ba:16:03:9e:9c:87
        Mtu:          9000
        Name:         eno1np0
        Pci Address:  0000:1a:00.0
        Vendor:       15b3
        Device ID:    1015
        Driver:       mlx5_core
        Link Speed:   25000 Mb/s
        Link Type:    ETH
        Mac:          ba:16:03:9e:9c:87
        Mtu:          9000
        Name:         eno2np1
        Pci Address:  0000:1a:00.1
        Vendor:       15b3
        Vfs:
      - Vfs:
        - deviceID: 101e
          driver: mlx5_core
          mac: c2:80:29:b5:63:55
          mtu: 9000
          name: enp134s0f1v0
          pciAddress: 0000:86:04.1
          vendor: 15b3
          vfID: 0
        - deviceID: 101e
          driver: mlx5_core
          mac: 7e:36:0c:82:d4:20
          mtu: 9000
          name: enp134s0f1v1
          pciAddress: 0000:86:04.2
          vendor: 15b3
          vfID: 1
          .. <omitted 29 other VFs here>
      syncStatus: Succeeded
    

For information about using this resource, see [`SriovNetworkNodeState`](https://github.com/k8snetworkplumbingwg/sriov-network-operator#sriovnetworknodestate).

### `NetworkAttachmentDefinition` resource

The `NetworkAttachmentDefinition` resource lets you attach Distributed Cloud pods to one or more logical or physical networks on your Distributed Cloud connected node. It leverages the [Multus-CNI](https://github.com/k8snetworkplumbingwg/multus-cni) framework and the following plugins:

  * [`ipvlan`](https://www.cni.dev/plugins/current/main/ipvlan/)
  * [`macvlan`](https://www.cni.dev/plugins/current/main/macvlan/)
  * [`sriov-cni`](https://github.com/k8snetworkplumbingwg/sriov-cni)



Use an annotation to reference the name of the appropriate `SriovNetworkNodePolicy` resource. When you create this annotation, do the following:

  * Use the key `k8s.v1.cni.cncf.io/resourceName`.
  * Use the prefix `gke.io/` in its value, followed by the name of the target `SriovNetworkNodePolicy` resource.



Use the `networking.gke.io/gdce-vlan-id` annotation to specify the VLAN ID for the target network. This annotation is mandatory.

The following examples illustrate the structure of the resource. For IPv4 networking.
    
    
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: sriov-net1
      namespace: mynamespace
      annotations:
        k8s.v1.cni.cncf.io/resourceName: gke.io/mlnx6_p2_sriov_en2
        networking.gke.io/gdce-vlan-id: 225
    
    spec:
      config: '{
      "type": "sriov",
      "cniVersion": "0.3.1",
      "name": "sriov-network",
      "ipam": {
        "type": "host-local",
        "subnet": "10.56.217.0/24",
        "routes": [{
          "dst": "0.0.0.0/0"
        }],
        "gateway": "10.56.217.1"
      }
    }'
    

For IPv6 networking:
    
    
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: sriov-210-den102
      annotations:
        k8s.v1.cni.cncf.io/resourceName: gke.io/mlnx6_p0_sriov_en
        networking.gke.io/gdce-vlan-id: 225
    spec:
      config: '{
      "type": "sriov",
      "cniVersion": "0.3.1",
      "name": "sriov-210-den102",
      "vlan": 210,
      
      "ipam": {
        "type": "host-local",
        "rangeStart": "2001:4860:1025:102:ffff:0220::2",
        "rangeEnd": "2001:4860:1025:102:ffff:0220::F",
        "subnet": "2001:4860:1025:102:ffff:0220::/96",
        "routes": [{
          "dst": "::/0"
        }],
        "gateway": "2001:4860:1025:102:ffff:0220::1"
      }
    }'
    

## Configure a secondary interface on a pod using SR-IOV VFs

After you configure a `SriovNetworkNodePolicy` resource and a corresponding `NetworkAttachmentDefinition` resource, you can configure a secondary network interface on a Distributed Cloud pod by using SR-IOV virtual functions.

To do so, add an annotation to your Distributed Cloud pod definition as follows:

  * Key: `k8s.v1.cni.cncf.io/networks`
  * Value: `nameSpace/<NetworkAttachmentDefinition1,nameSpace/NetworkAttachmentDefinition2...`



The following example illustrates this annotation:
    
    
    apiVersion: v1
    kind: pod
    metadata:
      name: sriovpod
      annotations:
        k8s.v1.cni.cncf.io/networks: mynamespace/sriov-net1
    spec:
      containers:
      - name: sleeppodsriov
        command: ["sh", "-c", "trap : TERM INT; sleep infinity & wait"]
        image: alpine
        securityContext:
          capabilities:
            add:
              - NET_ADMIN
    

## Configure a secondary interface on a pod using the MacVLAN driver

Distributed Cloud connected also supports creating a secondary network interface on a pod by using the MacVLAN driver. Only the `gdcenet0` interface supports this configuration and only on pods that run containerized workloads.

To configure an interface to use the MacVLAN driver:

  1. Configure a `NetworkAttachmentDefinition` resource as shown in the following examples. For IPv4 networking:
         
         apiVersion: "k8s.cni.cncf.io/v1"
          kind: NetworkAttachmentDefinition
          metadata:
            name: macvlan-b400-1
            annotations:
              networking.gke.io/gdce-vlan-id: 400
          spec:
            config: '{
            "type": "macvlan",
            "master": "gdcenet0.400",
            "ipam": {
              "type": "static",
              "addresses": [
                {
                  "address": "192.168.100.20/27",
                  "gateway": "192.168.100.1"
                }
              ]
            ...
            }
          }'
         

For IPv6 networking:
         
         apiVersion: "k8s.cni.cncf.io/v1"
          kind: NetworkAttachmentDefinition
          metadata:
            name: macvlan-bond0-210-den402
            annotations:
                networking.gke.io/gdce-vlan-id
          spec:
            config: '{
            "type": "macvlan",
            "cniVersion": "0.3.1",
            "name": "bond0-210",
            "master": "bond0.210",
         
            "ipam": {
              "type": "host-local",
              "rangeStart": "2001:4860:1025:102:0001:0210::2",
              "rangeEnd": "2001:4860:1025:102:0001:0210::F",
              "subnet": "2001:4860:1025:102:0001:0210::/96",
              "routes": [{
                "dst": "::/0"
              }],
              "gateway": "2001:4860:1025:102:0001:0210::1"
            }
          }'
         

  2. Add an annotation to your Distributed Cloud pod definition as follows. For IPv4 networking:
         
         apiVersion: v1
          kind: pod
          metadata:
            name: macvlan-testpod1
            annotations:
              k8s.v1.cni.cncf.io/networks: macvlan-b400-1
         

For IPv6 networking:
         
         apiVersion: v1
          kind: Pod
          metadata:
            name: vlan210-1
            namespace: default
            annotations:
              k8s.v1.cni.cncf.io/networks: default/macvlan-bond0-210-den402
         




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
         

The `networking.gke.io/gdce-lb-service-vip-cidrs` annotation specifies one or more IP address pools for this virtual network. The first half of the CIDR you specify here must include Service Virtual IP (SVIP) addresses. Distributed Cloud connected enforces this requirement through webhook checks as follows:

     * The SVIP address range must be within the corresponding VLAN CIDR range, and
     * The SVIP address range can only span up to the first half of the VLAN CIDR range.
  2. Add an annotation to your Distributed Cloud pod definition as follows:
         
         apiVersion: v1
         kind: pod
         metadata:
           name: myPod
           annotations:
             networking.gke.io/interfaces: '[{"interfaceName":"eth0","network":"pod-network"}, {"interfaceName":"eth1","network":"my-network-410"}]'
             networking.gke.io/default-interface: eth1
         

This annotation configures the `eth0` interface as primary and the `eth1` interface as secondary with Layer2 load balancing with MetalLB.




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

  * [Installation requirements](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/requirements)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
