---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networking/
title: Networking features of Distributed Cloud connected \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:54.052301+00:00
---

# Networking features of Distributed Cloud connected  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networking/

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

#  Networking features of Distributed Cloud connected Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the networking features of Google Distributed Cloud connected, including subnetworks, BGP peering sessions, and load balancing.

The procedures on this page only apply to Distributed Cloud connected racks, except load balancing, which applies to both Distributed Cloud connected racks and Distributed Cloud connected servers.

## IPv4/IPv6 dual-stack networking

Distributed Cloud connected allows you to create clusters that use IPv4/IPv6 dual-stack networking. To take advantage of this functionality, you must order Distributed Cloud connected with dual-stack IPv4/IPv6 networking enabled. You cannot reconfigure and existing IPv4-only deployment of Distributed Cloud connected to IPv4/IPv6 dual-stack networking. To check whether your deployment supports IPv4/IPv6 dual-stack networking, follow the instructions in [Get information about a machine](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/machines#machine-info) and check the returned value of the `dualstack_capable` label.

In a dual-stack cluster, the IPv4 stack uses island mode, while the IPv6 stack uses flat mode. Because of this, you must specify individual, discrete node, and pod IPv6 addresses that belong to the same subnetwork. For more information, see [Flat vs island mode network models](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/flat-vs-island-network).

For example, if your Distributed Cloud connected nodes and other local machines reside in the same Layer 2 domain, you could specify your IPv6 CIDR blocks for the cluster as follows:

Block purpose | Block range | Block size  
---|---|---  
IPv6 subnetwork | fd12::/56 | 2^72  
Pods | fd12::1:0/59 | 2^69  
Services | fd12::2:0/59 | 2^69  
  
This example assumes the following:

  * The node, pod, and service CIDR blocks belong to the fd:12::/56 supernetwork.
  * The node, pod, and service IP addresses are subnetworks of the specified CIDR block.
  * None of the subnetworks overlap.



IPv4/IPv6 dual-stack networking requires Layer 2 load balancing for IPv4 BGP peering and Layer 3 load balancing for IPv6 peering. For more information, see Load balancing.

For more information about deploying workloads on IPv4/IPv6 dual-stack clusters, see the following:

  * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/dual-stack-networking#view_cluster_nodes_and_pods)
  * [IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/)



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

  * You can only configure subnetworks, and
  * Subnetworks only support VLAN IDs; CIDR-based subnetworks are not supported.



A typical network configuration for Distributed Cloud connected consists of the following steps:

  1. Optional: Initialize the network configuration of the target zone, if necessary.

  2. Create a network.

  3. Create one or more subnetworks within the network.

  4. Establish northbound BGP peering sessions with your PE routers by using the corresponding interconnect attachments.

  5. Establish southbound BGP peering sessions with the pods that run your workloads by using the corresponding subnetworks.

  6. Optional: Establish loopback BGP peering sessions for high availability.

  7. Test your configuration.

  8. Connect your pods to the network.




### Initialize the network configuration of the Distributed Cloud zone

You must initialize the network configuration of your Distributed Cloud connected zone immediately after your Distributed Cloud connected hardware has been installed on your premises. Initializing the network configuration of a zone is a one-time procedure.

Initializing the network configuration of a zone creates a default router named `default` and a default network named `default`. It also configures the `default` router to peer with all of the interconnects that you requested when you ordered the Distributed Cloud connected hardware by creating corresponding interconnect attachments. This configuration provides your Distributed Cloud connected deployment with basic uplink connectivity to your local network.

For instructions, see [Initialize the network configuration of a zone](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/zones#init).

### Create a network

To create a new network, follow the instructions in [Create a network](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networks#create). You must also create at least one subnetwork within the network to allow Distributed Cloud connected nodes to connect to the network.

### Create one or more subnetworks

To create a subnetwork, follow the instructions in [Create a subnetwork](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/subnetworks#create). You must create at least one subnetwork in your network to allow nodes to access the network. The VLAN corresponding to each subnetwork that you create is automatically available to all nodes in the zone.

For Distributed Cloud connected servers, you can only configure subnetworks using VLAN IDs. CIDR-based subnetworks are not supported.

### Establish northbound BGP peering sessions

When you create a network and its corresponding subnetworks, they are local to their Distributed Cloud connected zone. To enable outbound connectivity, you must establish at least one northbound BGP peering session between the network and your peering edge routers.

To establish a northbound BGP peering session, do the following:

  1. [List the interconnects available in your zone](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/interconnects#list) and then select the target interconnect for this peering session.

  2. [Create one or more interconnect attachments](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/attachments#create) on the selected interconnect. Interconnect attachments link the router that you create in the next step with the selected interconnect.

  3. [Create a router](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#create). This router routes traffic between the interconnect and your network by using the interconnect attachments that you created in the previous step.

  4. Add an interface to the router for each interconnect attachment that you created earlier in this procedure. For each interface, use the IP address of the corresponding top-of-rack (ToR) switch in your Distributed Cloud connected rack. For instructions, see [Establish a northbound peering session](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#northbound).

  5. [Add a peer](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#add-peer) for each interface that you created on the router in the previous step.




### Establish southbound BGP peering sessions

To enable inbound connectivity to your workloads from your local network, you must establish one or more southbound BGP peering sessions between your peering edge routers and the subnetwork to which your pods belong. The gateway IP address for each subnetwork is the IP address of the corresponding ToR switch in your Distributed Cloud connected rack.

To establish a southbound BGP peering session, do the following:

  1. Add an interface to the router in the target network for each subnetwork that you want to provision with inbound connectivity. For instructions, see [Establish a southbound peering session](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#southbound).

  2. [Add a peer](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#add-peer) for each interface that you created on the router in the previous step.




### Optional: Establish loopback BGP peering sessions

To enable high-availability connectivity between your workloads and your local network, you can establish a loopback BGP peering session between the target pod and both ToR switches in your Distributed Cloud connected rack. A loopback peering session establishes two independent peering sessions for the pod, one with each ToR switch.

To establish a loopback BGP peering session, do the following:

  1. Add a loopback interface to the router in the target network. For instructions, see [Establish a loopback peering session](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#loopback).

  2. [Add a peer](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#add-peer) for the loopback interface.




### Test your configuration

To test your configuration of the network components that you created, do the following:

  1. [Check the operational status of the network](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networks#get-info).

  2. [Check the provisioning status of each subnetwork](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/subnetworks#get-info).

  3. [Check the operational status of the interconnects](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/interconnects#get-info).

  4. [Check the operational status of the interconnect attachments](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/attachments#get-info).

  5. [Check the operational status of the router](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#get-info).




### Connect your pods to the network

To connect your pods to the network and configure advanced network functions, follow the instructions in [Network Function operator](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/network-function). This functionality is not available to virtual machine workloads.

## (Optional) Configure cluster network isolation

Distributed Cloud connected supports cluster network isolation. Nodes assigned to a network-isolated cluster cannot communicate with any other nodes within the same Distributed Cloud connected zone. To enable cluster network isolation, use the `--enable-cluster-isolation` flag when creating or modifying a cluster. For more information, see [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/clusters).

## (Optional) Configure island mode

Distributed Cloud connected supports island mode for its virtual networking subsystem. Island mode lets you specify an isolated IP address range on a Pod's secondary network interface. This isolated address range is independent of the primary network interface VLAN's address range. Pods configured for island mode are assigned only addresses from this isolated "island" address range. For more information, see [Flat vs island mode network models](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network).

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

Distributed Cloud connected ships with the following load balancing solutions:

  * Layer 2 load balancing with MetalLB
  * Layer 3 load balancing with Google Distributed Cloud load balancers



The load balancing solutions built into Distributed Cloud connected cannot use overlapping Kubernetes service virtual IP prefixes. If you have an existing Distributed Cloud connected deployment that uses Layer 2 MetalLB load balancing, and you want to switch to Layer 3 load balancing with Google Distributed Cloud load balancers, you must use a service virtual IP prefix that does not overlap with the prefix used by your Layer 2 MetalLB load balancing configuration.

### Layer 2 load balancing with MetalLB

Distributed Cloud ships with a bundled network load balancing solution based on [MetalLB in Layer 2 mode](https://metallb.universe.tf/concepts/layer2/). You can use this solution to expose services that run in your Distributed Cloud zone to the outside world by using virtual IP addresses (VIPs) as follows:

  1. Your network administrator plans the network topology and specifies the required virtual IPv4 and IPv6 address subnetwork when ordering Distributed Cloud. Google configures your Distributed Cloud hardware accordingly before delivery. Keep the following in mind: 
     * This VIP subnetwork is shared among all Kubernetes clusters that run within your Distributed Cloud zone.
     * A route for the requested VIP subnetwork is advertised through the BGP sessions between the Distributed Cloud zone and your local network.
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
     * `addresses`: a list of IPv4 and IPv6 addresses, address ranges, and subnetworks to include in this address pool.
     * `avoid_buggy_ips`: Excludes IP addresses that end with `.0` or `.255`.
     * `manual_assign`: Lets you manually assign addresses from this pool in the target `LoadBalancer` service's configuration instead of having the MetalLB controller assign them automatically.

For more information on configuring VIP address pools, see [Specify address pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb#specify_address_pools) in the MetalLB documentation.

  4. The cluster administrator creates the appropriate [Kubernetes `LoadBalancer` services](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer).




Distributed Cloud nodes in a single node pool share a common Layer 2 domain and are therefore also MetalLB load balancer nodes.

### Layer 3 load balancing with Google Distributed Cloud load balancers

Distributed Cloud connected ships with a bundled network load balancing solution based on the [Google Distributed Cloud bundled load balancers](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/lb-bundled-bgp) in Layer 3 mode configured as BGP speakers. You can use this solution to expose services that run in your Distributed Cloud connected zone to the outside world by using VIPs.

You can specify the VIP ranges for the corresponding `LoadBalancer` services by using the `metallb-config` ConfigMap. For example:
    
    
    kind: ConfigMap
    apiVersion: v1
    data:
      config: |
        address-pools:
        - name: default
          protocol: bgp
          addresses:
          - 10.100.10.66/27
    metadata:
      name: metallb-config
      namespace: metallb-system
    

In the preceding example, each `LoadBalancer` service that you configure is automatically assigned a virtual IP address from the `10.100.10.66/27` range specified in the ConfigMap. These VIPs are then advertised northbound by the Distributed Cloud BGP speakers configured on the ToR switches through the `BGPPeer` resources.

When you create a Distributed Cloud cluster, the following resources are automatically created on that cluster:

  * A `BGPLoadBalancer` resource that instantiates the BGP load balancer.
  * A `NetworkGatewayGroup` resource that specifies the local floating IP addresses to use for the BGP speakers. These IP addresses are automatically set to the last two IP addresses of the Kubernetes node subnetwork assigned to the cluster.



With those resources in place, you can set up BGP sessions to the Distributed Cloud ToR switches by configuring corresponding `BGPPeer` resources. To do so, you must have the necessary autonomous system numbers (ASNs) and the loopback peer IP addresses for the ToR switches. These IP addresses serve as the ToR switch BGP session endpoints on the default network resource. Keep in mind that the value of the `network` parameter must be `pod-network`. 

Following is an example of the two `BGPPeer` resources:
    
    
    kind: BGPPeer
    apiVersion: networking.gke.io/v1
    metadata:
      name: bgppeertor1
      labels:
        cluster.baremetal.gke.io/default-peer: "true"
      namespace: kube-system
    spec:
      network: pod-network
      localASN: 64777
      peerASN: 64956
      peerIP: 10.112.0.10
      sessions: 1
    
    
    
    kind: BGPPeer
    apiVersion: networking.gke.io/v1
    metadata:
      name: bgppeertor2
      labels:
        cluster.baremetal.gke.io/default-peer: "true"
      namespace: kube-system
    spec:
      network: pod-network
      localASN: 64777
      peerASN: 64956
      peerIP: 10.112.0.11
      sessions: 1
    

### Configure Layer 3 BGP load balancing automation for IPv6 peering

Before you can begin using IPv6 peering on your IPv4/IPv6 dual-stack networking cluster, you must work with Google Support to enable Google Distributed Cloud load balancer automation on your Distributed Cloud connected deployment.

### Create Layer 3 `LoadBalancer` service

After you have enabled enable Google Distributed Cloud load balancer automation on your Distributed Cloud connected deployment, instantiate the Layer 3 `LoadBalancer` service. For example:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
      labels:
        app.kubernetes.io/name: MyApp
    spec:
      ipFamilyPolicy: PreferDualStack
      ipFamilies:
      - IPv6
      - IPv4
      selector:
        app.kubernetes.io/name: MyApp
      type: LoadBalancer
      ports:
        - protocol: TCP
          port: 80
    

### Check the state of the BGP session and load balancing services

To check the state of your BGP session, use the following command:
    
    
    kubectl get bgpsessions.networking.gke.io -A
    

The command returns output similar to the following example:
    
    
    NAMESPACE     NAME                                                 LOCAL ASN   PEER ASN   LOCAL IP        PEER IP         STATE            LAST REPORT
    kube-system   bgppeertor1-np-den6-120demo-den6-04-6ad5b6f4         64777       64956      10.100.10.61    10.112.0.10     Established      2s
    kube-system   bgppeertor2-np-den6-120demo-den6-04-6ad5b6f4         64777       64956      10.100.10.61    10.112.0.11     Established      2s
    

To verify that your `LoadBalancer` services are being advertised by the BGP speakers, use the following command:
    
    
    kubectl get bgpadvertisedroutes.networking.gke.io -A
    

The command returns output similar to the following example:
    
    
    NAMESPACE      NAME                           PREFIX            METRIC
    kube-system    bgplb-default-service-tcp      10.100.10.68/32
    kube-system    bgplb-default-service-udp      10.100.10.77/32
    

## Distributed Cloud ingress

In addition to load balancing, Distributed Cloud connected also supports Kubernetes `Ingress` resources. A Kubernetes `Ingress` resource controls the flow of HTTP(S) traffic to Kubernetes services that run on your Distributed Cloud connected clusters. The following example illustrates a typical `Ingress` resource:
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: my-ingress
    spec:
      rules:
      - http:
          paths:
          - backend:
              service:
                name: my-service
                port:
                  number: 80
            path: /foo
            pathType: Prefix
    

When configured, network traffic flows through the `istio-ingress` service, which by default is assigned a random IP address from the VIP pools specified in your MetalLB configuration. You can select a specific IP address or a virtual IP address from the MetalLB configuration by using the `loadBalancerIP` field in the `istio-ingress` service definition. For example:
    
    
    apiVersion: v1
    kind: service
    metadata:
      labels:
        istio: ingress-gke-system
        release: istio
      name: istio-ingress
      namespace: gke-system
    spec:
      loadBalancerIP: <targetLoadBalancerIPaddress>
    

This functionality is not available on Distributed Cloud connected servers.

### Disable the default Distributed Cloud `Ingress` resource

By default, when you create a Distributed Cloud connected cluster, Distributed Cloud automatically configures the `istio-ingress` service for the cluster. You have the option to create a Distributed Cloud connected cluster without the `istio-ingress` service. To do so, complete the following steps:

###  gcloud 

  1. Create a YAML configuration file named `SystemsAddonConfig.yaml` with the following contents:
         
         systemAddonsConfig:
          ingress:
            disabled: true
         

  2. Pass the `SystemsAddonConfig.yaml` file by using the `--system-addons-config` flag in your cluster creation command. You must use the `gcloud alpha` version to use this feature. For example:
         
         gcloud alpha edge-cloud container clusters create MyGDCECluster1 --location us-west1 \
             --system-addons-config=SystemsAddonConfig.yaml
         

For more information about creating a Distributed Cloud cluster, see [Create a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/clusters#create).




###  API 

  1. Add the following JSON content to the JSON payload in your cluster creation request:
         
         "systemAddonConfig" {
            "ingress" {
                    "disabled": true
            }
         }
         

  2. Submit the cluster creation request as described in [Create a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/clusters#create).




## NodePort service

Distributed Cloud connected supports the Kubernetes `NodePort` service that listens for connections on a Distributed Cloud node at a port number of your choice. The `NodePort` service supports the TCP, UDP, and SCTP protocols. For example:
    
    
    apiVersion: v1
    kind: pod
    metadata:
      name: socat-nodeport-sctp
      labels:
        app.kubernetes.io/name: socat-nodeport-sctp
    spec:
      containers:
      - name: socat-nodeport-sctp
        ...
        ports:
          - containerPort: 31333
            protocol: SCTP
            name: server-sctp
    
    ---
    
    apiVersion: v1
    kind: service
    metadata:
      name: socat-nodeport-sctp-svc
    spec:
      type: NodePort
      selector:
        app.kubernetes.io/name: socat-nodeport-sctp
      ports:
        - port: 31333
          protocol: SCTP
          targetPort: server-sctp
          nodePort: 31333
    

## SCTP support

Distributed Cloud connected supports the Stream Control Transmission Protocol (SCTP) on the primary network interface for both internal and external networking. SCTP support includes the `NodePort`, `LoadBalancer`, and `ClusterIP` service types. pods can use SCTP to communicate with other pods and external resources. The following example illustrates how to configure IPERF as a `ClusterIP` service by using SCTP:
    
    
    apiVersion: v1
    kind: pod
    metadata:
      name: iperf3-sctp-server-client
      labels:
        app.kubernetes.io/name: iperf3-sctp-server-client
    spec:
      containers:
      - name: iperf3-sctp-server
        args: ['-s', '-p 31390']
        ports:
          - containerPort: 31390
            protocol: SCTP
            name: server-sctp
      - name: iperf3-sctp-client
        ...
    
    ---
    
    apiVersion: v1
    kind: service
    metadata:
      name: iperf3-sctp-svc
    spec:
      selector:
        app.kubernetes.io/name: iperf3-sctp-server-client
      ports:
        - port: 31390
          protocol: SCTP
          targetPort: server-sctp
    

This functionality is not available on Distributed Cloud connected servers.

### SCTP kernel modules

Starting with version 1.5.0, Distributed Cloud connected configures the `sctp` Edge OS kernel module as loadable. This allows you to load your own SCTP protocol stacks in the kernel user space.

Additionally, Distributed Cloud connected loads the following modules into the kernel by default:

Module name | Config name  
---|---  
`fou` | `CONFIG_NET_FOU`  
`nf_conntrack_proto_gre` | `CONFIG_NF_CT_PROTO_GRE`  
`nf_conntrack_proto_sctp` | `CONFIG_NF_CT_PROTO_SCTP`  
`inotify` | `CONFIG_INOTIFY_USER`  
`xt_redirect` | `CONFIG_NETFILTER_XT_TARGET_REDIRECT`  
`xt_u32` | `CONFIG_NETFILTER_XT_MATCH_U32`  
`xt_multiport` | `CONFIG_NETFILTER_XT_MATCH_MULTIPORT`  
`xt_statistic` | `CONFIG_NETFILTER_XT_MATCH_STATISTIC`  
`xt_owner` | `CONFIG_NETFILTER_XT_MATCH_OWNER`  
`xt_conntrack` | `CONFIG_NETFILTER_XT_MATCH_CONNTRACK`  
`xt_mark` | `CONFIG_NETFILTER_XT_MARK`  
`ip6table_mangle` | `CONFIG_IP6_NF_MANGLE`  
`ip6_tables` | `CONFIG_IP6_NF_IPTABLES`  
`ip6table_filter` | `CONFIG_IP6_NF_FILTER`  
`ip6t_reject` | `CONFIG_IP6_NF_TARGET_REJECT`  
`iptable_mangle` | `CONFIG_IP_NF_MANGLE`  
`ip_tables` | `CONFIG_IP_NF_IPTABLES`  
`iptable_filter` | `CONFIG_IP_NF_FILTER`  
  
## `ClusterDNS` resource

Distributed Cloud connected supports the Google Distributed Cloud `ClusterDNS` resource for configuring upstream name servers for specific domains by using the `spec.domains` section. For more information about configuring this resource, see [`spec.domains`](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.12/how-to/cluster-dns#specdomains).

This functionality is not available on Distributed Cloud connected servers.

## What's next

  * [pod and service network address allocation](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/address-allocation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
