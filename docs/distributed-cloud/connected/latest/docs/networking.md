---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking/
title: Networking features of Distributed Cloud connected \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:20.915768+00:00
---

# Networking features of Distributed Cloud connected  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking/

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

#  Networking features of Distributed Cloud connected Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the networking features of Google Distributed Cloud connected, including subnetworks and load balancing.

## Enable the Distributed Cloud Edge Network API

Before you can configure networking on a connected deployment of Distributed Cloud, you must enable the Distributed Cloud Edge Network API. To do so, complete the steps in this section. By default, Distributed Cloud connected servers ship with the Distributed Cloud Edge Network API already enabled.

###  Console 

  1. In the Google Cloud console, go to the **Distributed Cloud Edge Network API** page.

[Enable the API](https://console.cloud.google.com/apis/api/edgenetwork.googleapis.com)

  2. Click **Enable**.




###  gcloud 

Use the following command:
    
    
    gcloud services enable edgenetwork.googleapis.com
    

## Configure networking on Distributed Cloud connected

This section describes how to configure the networking components on your Distributed Cloud connected deployment.

The following limitations apply to Distributed Cloud connected servers:

  * You can only configure subnetworks.
  * Subnetworks only support VLAN IDs. CIDR-based subnetworks are not supported.



A typical network configuration for Distributed Cloud connected consists of the following steps:

  1. Optional: Initialize the network configuration of the target zone, if necessary.

  2. Create a network.

  3. Create one or more subnetworks within the network.

  4. Test your configuration.

  5. Connect your pods to the network.




### Initialize the network configuration of the Distributed Cloud zone

You must initialize the network configuration of your Distributed Cloud connected zone immediately after your Distributed Cloud connected hardware has been installed on your premises. Initializing the network configuration of a zone is a one-time procedure.

Initializing the network configuration of a zone creates a default network named `default`. This configuration provides your Distributed Cloud connected deployment with basic uplink connectivity to your local network.

For instructions, see [Initialize the network configuration of a zone](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/zones#init).

### Create a network

To create a new network, follow the instructions in [Create a network](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networks#create). You must also create at least one subnetwork within the network to allow Distributed Cloud connected nodes to connect to the network.

### Create one or more subnetworks

To create a subnetwork, follow the instructions in [Create a subnetwork](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/subnetworks#create). You must create at least one subnetwork in your network to allow nodes to access the network. The VLAN corresponding to each subnetwork that you create is automatically available to all nodes in the zone.

### Test your configuration

To test your configuration of the network components that you created, do the following:

  1. [Check the operational status of the network](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networks#get-info).

  2. [Check the provisioning status of each subnetwork](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/subnetworks#get-info).




### Connect your pods to the network

To connect your pods to the network and configure advanced network functions, follow the instructions in [Network Function operator](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/network-function). This functionality is not available to virtual machine workloads.

## Optional: Configure cluster network isolation

Distributed Cloud connected supports cluster network isolation. Nodes assigned to a network-isolated cluster cannot communicate with any other nodes within the same Distributed Cloud connected zone. To enable cluster network isolation, use the `--enable-cluster-isolation` flag when creating or modifying a cluster. For more information, see [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters).

## Optional: Configure island mode

Distributed Cloud connected supports island mode for its virtual networking subsystem. Island mode lets you specify an isolated IP address range on a Pod's secondary network interface. This isolated address range is independent of the primary network interface VLAN's address range. Pods configured for island mode are assigned only addresses from this isolated "island" address range. For more information, see [Flat versus island mode network models](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/flat-vs-island-network).

The isolated IP address range you specify for island mode must not collide with the following IP address ranges:

  * The primary VLAN CIDR for any network configured in the cluster
  * The Load Balancer virtual IP address range specified in the `networking.gke.io/gdce-lb-service-vip-cidrs` annotation in the `Network` resource
  * The IP address ranges used for island mode for any other networks in the cluster



### Configure island mode

To configure island mode at Pod level, add the `networking.gke.io/gdce-pod-cidr` annotation to the corresponding `Network` custom resource. Set the annotation value to the target isolated IP address range and apply the modified `Network` resource to your cluster. For example:
    
    
    networking.gke.io/gdce-pod-cidr: 172.15.10.32/27
    

You must also set the following parameters:

  * **`type`** must be set to `L3`.
  * **`IPAMMode`** must be set to `Internal`.



For example:
    
    
    apiVersion: networking.gke.io/v1
    kind: Network
    metadata:
      name: my-network
      annotations:
        # Enable island mode and specify the isolated address range.
        networking.gke.io/gdce-pod-cidr: 172.15.10.32/27
        # Specify the VLAN ID for this secondary network.
        networking.gke.io/gdce-vlan-id: "561"
        # Specify the CIDR block for load balancer services on this network.
        networking.gke.io/gdce-lb-service-vip-cidrs: 172.20.5.180/30
    spec:
      # Network type must be L3 for island mode.
      type: L3
      # IPAMMode must be Internal for island mode.
      IPAMMode: Internal
      nodeInterfaceMatcher:
        interfaceName: gdcenet0.561 # The name for the target network interface.
      gateway4: 172.20.5.177 # Gateway IP address; must be unique in this CR.
      externalDHCP4: false
      dnsConfig:
        nameservers:
        - 8.8.8.8
    

To verify that island mode is enabled, do the following:

  1. Create a test Pod and apply it to your cluster. For example:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: island-pod-tester
           annotations:
             networking.gke.io/interfaces: '[{"interfaceName":"eth1","network":"test-network-vlan561"}]'
             networking.gke.io/default-interface: "eth1"
         spec:
           containers:
           - name: sample-container
             image: busybox
             command: ["/bin/sh", "-c", "sleep 3600"]
         

  2. Get the Pod's IP address:
         
         kubectl get pod island-pod-tester -o wide
         

The command returns the Pod's IP address, which is within the isolated address range you specified.




### Configure island mode with the `ClusterIP` service

To configure island mode with the `ClusterIP` service, complete the steps in the previous section, then add the `networking.gke.io/gke-gateway-clusterip-cidr` annotation to your `Network` resource and set its value according to your business needs. Address ranges specified in the `Network` resource must not overlap. For example:
    
    
    apiVersion: networking.gke.io/v1
    kind: Network
    metadata:
      annotations:
        networking.gke.io/gdce-lb-service-vip-cidrs: 172.20.5.180/30
        networking.gke.io/gdce-pod-cidr: 172.15.10.32/27
        networking.gke.io/gdce-vlan-id: "561"
        networking.gke.io/gke-gateway-clusterip-cidr: 10.20.1.0/28
      name: test-network-vlan561
    spec:
      IPAMMode: Internal
      dnsConfig:
        nameservers:
        - 8.8.8.8
      externalDHCP4: false
      gateway4: 172.20.5.177
      nodeInterfaceMatcher:
        interfaceName: gdcenet0.561
      type: L3
    

## Load balancing

Distributed Cloud ships with a bundled network load balancing solution based on [MetalLB in Layer 2 mode](https://metallb.universe.tf/concepts/layer2/). You can use this solution to expose services that run in your Distributed Cloud zone to the outside world by using virtual IP addresses (VIPs) as follows:

  1. Your network administrator plans the network topology and specifies the required virtual IPv4 address subnetwork when ordering Distributed Cloud. Your Google-certified systems integrator configures your Distributed Cloud hardware accordingly before delivery. Keep the following in mind: 
     * This VIP subnetwork is shared among all Kubernetes clusters that run within your Distributed Cloud zone.
     * The first (network ID), second (default gateway), and last (broadcast address) addresses in the subnetwork are reserved for core system functionality. Do not assign those addresses to your MetalLB configurations' address pools.
     * Each cluster must use a separate VIP range that falls within the configured VIP subnetwork.
  2. When you create a cluster in your Distributed Cloud zone, your cluster administrator specifies the pod and ClusterIP service address pools by using CIDR notation. Your network administrator provides the appropriate `LoadBalancer` VIP subnetwork to your cluster administrator.
  3. After the cluster is created, the cluster administrator configures the corresponding VIP pools. You must specify the VIP pools by using the `--external-lb-address-pools` flag when you create the cluster. The flag accepts a file with a YAML or JSON payload in the following format:
         
         addressPools:
          - name: foo
            addresses:
            - 10.2.0.212-10.2.0.221
            - fd12::4:101-fd12::4:110
            avoid_buggy_ips: true
            manual_assign: false
         
          - name: bar
            addresses:
            - 10.2.0.202-10.2.0.203
            - fd12::4:101-fd12::4:102
            avoid_buggy_ips: true
            manual_assign: false
         

To specify a VIP address pool, provide the following information in the payload:

     * `name`: a descriptive name that uniquely identifies this VIP address pool.
     * `addresses`: a list of IPv4 addresses, address ranges, and subnetworks to include in this address pool.
     * `avoid_buggy_ips`: Excludes IP addresses that end with `.0` or `.255`.
     * `manual_assign`: Lets you manually assign addresses from this pool in the target `LoadBalancer` service's configuration instead of having the MetalLB controller assign them automatically.

For more information on configuring VIP address pools, see [Specify address pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb#specify_address_pools) in the MetalLB documentation.

  4. The cluster administrator creates the appropriate [Kubernetes `LoadBalancer` services](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer).




Distributed Cloud nodes in a single node pool share a common Layer 2 domain and are therefore also MetalLB load balancer nodes. When you follow these steps, Layer 2 load balancing with MetalLB is configured automatically.

## `ClusterDNS` resource

Distributed Cloud connected supports the Google Distributed Cloud `ClusterDNS` resource for configuring upstream name servers for specific domains by using the `spec.domains` section. For more information about configuring this resource, see [`spec.domains`](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/cluster-dns#specdomains).

## What's next

  * [Pod and service network address allocation](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/address-allocation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
