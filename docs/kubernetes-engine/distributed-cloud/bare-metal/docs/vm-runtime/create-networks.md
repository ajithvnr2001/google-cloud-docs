---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-networks/
title: Create and use virtual networks for VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:31:17.959189+00:00
---

# Create and use virtual networks for VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create and use virtual networks for VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for IT administrators, Operators, and Networking specialists who run Google Distributed Cloud. This document shows you how to create and use virtual networks to support VM workloads that use VM Runtime on GDC. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

To complete this document, you need access to the following resources:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Google Distributed Cloud on Compute Engine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart#install_the_virtctl_client_tool).



## Virtual networks overview

Networks are created using custom resources. A network can be created at any time after your cluster is created. Network settings for the host interface and VLAN ID assignment, if defined, can't be changed after you create a network.

The deletion of networks is subject to some conditions. For example, the network controller rejects the deletion of a network when it's in use by any resources, such as VMs or network interfaces.

The network definition can include the gateway, routes, and DNS information. You can also enable the use of an external DHCP server. These network settings are statically or dynamically assigned depending on how certain network configurations options are defined.

### Default pod-network

Each cluster has a `pod-network` created by default for you. This network can't be changed. Routes for the pod CIDR and service CIDR, and DNS configuration are automatically populated. The DNS configuration uses the same values as the cluster.

The `pod-network` can be used by workloads that need an interface to access the pod network of the cluster and don't need any specific configuration options. The routes of the `pod-network` are always configured to ensure the cluster and service access for the workloads, even though the default gateway is not on the `pod-network` interface.

This default `pod-network` lets you test VM Runtime on GDC without additional steps to create your own virtual networks. Many of our docs use this default `pod-network` to reduce the complexity of the examples. The needs of your VM workloads determine if this default `pod-network` is sufficient, or if you need to create and use your own virtual networks.

**Note:** You typically wouldn't use this default `pod-network` for production traffic. Instead, you would create and use your own virtual networks, as shown in the rest of this document. You define IP address ranges, routes, and VLANs in your own networks, which aren't possible in the default `pod-network`.

The following YAML manifest shows a sample configuration for the `pod-network`. Values for routes, DNS, and the interface name have been populated by the cluster:
    
    
      ​​apiVersion: networking.gke.io/v1
      kind: Network
      metadata:
        name: pod-network
      spec:
        routes:
        - to: 192.168.0.0/16
        - to: 10.96.0.0/12
        dnsConfig:
          nameservers:
          - 10.96.0.10
    

## Create and use virtual networks

To support production workloads, create networks that support the features you need, such as the use of an external DHCP server or the use of a VLAN ID. These networks provide layer 2 (L2) connectivity for your VMs.

### Use an external DHCP server

VM Runtime on GDC doesn't provide DHCP servers. You must manually specify IP addresses for VMs or configure the use of external DHCP servers. When you enable the use of an external DHCP server, you can skip configuration of DNS and gateway settings if they're provided by DHCP.

To create a network that uses an external DHCP server, complete the following steps:

  1. Create a `Network` manifest, such as `use-dhcp-network.yaml`, in the editor of your choice:
         
         nano use-dhcp-network.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: NETWORK_NAME
         spec:
           type: L2
           nodeInterfaceMatcher:
             interfaceName: INTERFACE_NAME
           externalDHCP4: true
         

Replace the following values:

     * `NETWORK_NAME`: the name for your network.
     * `INTERFACE_NAME`: the interface name on your Google Distributed Cloud node to attach the network to. Specify the name of the physical interface on your node to use. All nodes in your cluster should have the same interface name.

In this `Network` manifest, the following values are set:

     * `type` is set to `L2`. With this setting, workloads can only have a Layer 2 attachment to this network. This is the only network `type` that you can create in VM Runtime on GDC.
     * `externalDHCP4` is set to `true`. This setting enables external DHCP for the network. The external DHCP server is responsible for IPv4 address allocation, routes, gateway, and DNS configuration for workloads connected to this network.
  3. Save and close the `Network` manifest in your editor.

  4. Create the network using `kubectl`:
         
         kubectl apply -f use-dhcp-network.yaml
         




### Manually define network settings

VM Runtime on GDC doesn't provide DHCP servers. You must manually specify IP addresses for VMs or configure the use of external DHCP servers. If you manually specify IP addresses, you must define network settings for DNS, routes, and default gateway.

To create a network with manually-specified networking settings for VMs, complete the following steps:

  1. Create a `Network` manifest, such as `manual-network.yaml`, in the editor of your choice:
         
         nano manual-network.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: NETWORK_NAME
         spec:
           type: L2
           nodeInterfaceMatcher:
             interfaceName: INTERFACE_NAME
           routes:
           - to: "ROUTE_ADDRESS"
           gateway4: GATEWAY_ADDRESS
           dnsConfig:
             nameservers:
             - NAMESERVER_ADDRESS
         

Replace the following values:

     * `NETWORK_NAME`: the name for your network.
     * `INTERFACE_NAME`: the interface name on your Google Distributed Cloud node to attach the network to. Specify the name of the physical interface on your node to use. All nodes in your cluster should have the same interface name.
     * `ROUTE_ADDRESS`: optional routes in CIDR notation to configure on every VM that connects to this network.
     * `GATEWAY_ADDRESS`: the gateway IP address for your VMs to use.
     * `NAMESERVER_ADDRESS`: one or more DNS nameserver IP addresses for your VMs to use.
  3. Save and close the `Network` manifest in your editor.

  4. Create the network using `kubectl`:
         
         kubectl apply -f manual-network.yaml
         




### Use a VLAN ID

When you create virtual networks, you can define tagged VLANs. These VLAN assignments help you isolate network traffic based on your workload requirements and isolation needs. In an `AnthosManaged` network, the cluster has permission to create and delete the VLAN interface on every node.

To create a network that defines a VLAN assignment, complete the following steps:

  1. Create a `Network` manifest, such as `vlan-network.yaml`, in the editor of your choice:
         
         nano vlan-network.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: NETWORK_NAME
         spec:
           type: L2
           networkLifecycle: AnthosManaged
           l2NetworkConfig:
             vlanID: VLAN_ID
           nodeInterfaceMatcher:
             interfaceName: INTERFACE_NAME
           externalDHCP4: true
         

Replace the following values:

     * `NETWORK_NAME`: the name for your network.
     * `INTERFACE_NAME`: the interface name on your Google Distributed Cloud node to attach the network to. Specify the name of the physical interface on your node to use. All nodes in your cluster should have the same interface name.
     * `VLAN_ID`: the VLAN ID you want to tag traffic for.

In this `Network` manifest, the following values are set:

     * Workloads can have only an `L2` attachment to this network.
     * The network is `AnthosManaged`. This setting is the default lifecycle if not specified. 
       * In this mode, the cluster has permission to create and delete the VLAN interface on every node, such as `INTERFACE_NAME.VLAN_ID`.
       * If you want to create, or have already created, the VLAN interfaces on the nodes, set the `networkLifecycle` value to `UserManaged` as shown in the next section.
     * The network has external DHCP enabled. The external DHCP server is responsible for IPv4 address allocation, routes, gateway, and DNS configuration for workloads connected to this network.
  3. Save and close the `Network` manifest in your editor.

  4. Create the network using `kubectl`:
         
         kubectl apply -f vlan-network.yaml
         




### Create a user-managed network

In the following example virtual network, the network is _user-managed_ , as opposed to _Anthos-managed_ in a previous example. In user-managed networks, you're responsible for creating or deleting the VLAN interface on the host.

To create a network in a user-managed mode and manually define the VLAN interface configuration, complete the following steps:

  1. Create a `Network` manifest, such as `user-managed-network.yaml`, in the editor of your choice:
         
         nano user-managed-network.yaml
         

  2. Copy and paste the following YAML definition:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: NETWORK_NAME
         spec:
           type: L2
           networkLifecycle: UserManaged
           l2NetworkConfig:
             vlanID: VLAN_ID
           nodeInterfaceMatcher:
             interfaceName: INTERFACE_NAME
           externalDHCP4: true
         

Replace the following values:

     * `NETWORK_NAME`: the name for your network.
     * `INTERFACE_NAME`: the host interface to attach the network to.
     * `VLAN_ID`: the VLAN ID you want to tag traffic for.

In this `Network` manifest, the following values are set:

     * Workloads can have only an `L2` attachment to this network.
     * The network is `UserManaged`. You must create or delete the VLAN `VLAN_ID` interface on every node before the network is created, or after the network is deleted.
     * The network has external DHCP enabled. The external DHCP server is responsible for IPv4 address allocation, routes, gateway, and DNS configuration for workloads connected to this network.
  3. Save and close the `Network` manifest in your editor.

  4. Create the network using `kubectl`:
         
         kubectl apply -f user-managed-network.yaml
         




## Connect a VM to a network

Network settings for your VM such as DNS and DHCP are statically or dynamically assigned depending on how certain network configurations options are defined:

  * If you configure a static IP address on the VM, no query is sent to a DHCP server. Additional information to configure the gateway and route must come from the network resource.
  * If you don't configure a static IP address on the VM, a query is sent to the DHCP server. The VM gets all information from the DHCP server and ignores any configuration you define in the network resource.
  * If external DHCP isn't set to `true` in the network resource, you must configure a static IP address for the VM. All other information comes from the configuration you define in network resource.



To create a VM that connects to a network, complete the following steps:

###  CLI 

  * To create a VM using `kubectl`, complete the following steps:
        
        kubectl virt create vm VM_NAME \
          --image ubuntu20.04 \
          --network NETWORK_NAME
        

Replace the following values:

    * `VM_NAME`: the name for your VM.
    * `NETWORK_NAME`: the name of your network to connect to. 
      * If the network is configured to allow the use of external DHCP servers, the VM gets an IP address assignment automatically. If you need to define a static IP address, add the optional `--ip IP_ADDRESS` parameter and value.
**Note:** In the `~/google-virtctl` directory, a `VM_NAME.yaml` file is created. You can view the content of this file to see the definition of the Kubernetes resources that were created by the VM Runtime on GDC.



###  Manifest 

To create a VM using a YAML manifest, complete the following steps:

  1. Create a `VirtualMachine` manifest, such as `my-vm.yaml`, in the editor of your choice:
         
         nano my-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           interfaces:
             - name: eth0
               networkName: NETWORK_NAME
               ipAddresses:
                 - IP_ADDRESS
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
         

In this YAML manifest, define the following settings:

     * `VM_NAME`: the name for your VM.
     * `NETWORK_NAME`: the name of your network to connect to.
     * `IP_ADDRESS`: the IP address in CIDR notation to assign to your VM, such as `192.0.2.10/24`. 
       * If your network is configured to allow the use of external DHCP servers, remove this field from the `VirtualMachine` manifest.

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create a VM boot disk](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks#create-a-vm-with-an-attached-disk).

  3. Save and close the `VirtualMachine` manifest in your editor.

  4. Create the VM using `kubectl`:
         
         kubectl apply -f my-vm.yaml
         




## What's next

  * [Edit a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/edit-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
