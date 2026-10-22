---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/network-connectivity-gateway/
title: Configure Network Connectivity Gateway \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:08.985804+00:00
---

# Configure Network Connectivity Gateway  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/network-connectivity-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure Network Connectivity Gateway Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to configure Network Connectivity Gateway for a cluster in Google Distributed Cloud.

Sometimes you have Pods running in a cluster that must communicate with workloads running in a [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview). This communication must be secure. And perhaps you need this communication to occur over a flat network without using a proxy server. Network Connectivity Gateway enables this kind of communication.

Network Connectivity Gateway runs as a Pod in your cluster. As shown in the following diagram, this solution provides [IPsec](https://en.wikipedia.org/wiki/IPsec) tunnels for traffic from Pods in your cluster to VMs in a VPC. When the gateway Pod receives prefixes for VPC subnets over a Border Gateway Protocol (BGP) session, it sets up forwarding by using [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2). When other Pods send traffic to an address with one of those prefixes, the traffic is steered to the gateway Pod. Then the gateway Pod routes the traffic over an IPsec tunnel toward Google Cloud.

**Note:** Google Distributed Cloud running on Ubuntu 18.04 isn't supported for Network Connectivity Gateway, but all other OSes supported by Google Distributed Cloud are supported. For the list of the Linux distributions and versions that are supported by Google Distributed Cloud, see [Select your operating system](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs).

![Network Connectivity Gateway diagram for Google Distributed Cloud](https://docs.cloud.google.com/static/anthos/clusters/docs/images/network-connectivity-gateway-on-prem.svg)

Network Connectivity Gateway doesn't support the following features and capabilities:

  * IPv6 for HA VPN (and BGP)
  * MD5 for BGP
  * Bidirectional Forwarding Detection (BFD) for BGP



## Create Google Cloud resources

Before you enable Network Connectivity Gateway in a cluster, you must have the following Google Cloud resources:

  * A Cloud Router

  * An HA VPN gateway

  * A peer VPN gateway: one interface

  * Two VPN tunnels

  * Two BGP sessions: one for each of your VPN tunnels




For information on how to create and configure these resources, see [Creating an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn).

As you create these resources, gather the following information, and have it available for later:

  * The two external IP addresses that Google Cloud assigned to your HA VPN gateway.

  * The public IP address for IPsec/VPN traffic that leaves your organization. This address might be the result of a network address translation (NAT).

  * Your pre-shared key.

  * The autonomous system number (ASN) that you assigned to your Cloud Router for BGP sessions.

  * The ASN you've chosen to use in your on-premises cluster for BGP sessions.

  * For each BGP session, the [link-local address](https://en.wikipedia.org/wiki/Link-local_address), such as `169.254.1.1`, to be used by your Cloud Router and the link-local address to be used in your on-premises cluster.




For information on how to find the details for your BGP session configuration, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

## Cluster requirements

The Network Connectivity Gateway command-line tool download, `ncgctl-v1.12.0-linux-amd64.tar.gz` is compatible with version 1.12 of Google Distributed Cloud only. If you are creating a new version 1.12.0 cluster, you enable Network Connectivity Gateway with an annotation in the cluster configuration file.

**Note:** If you have an existing version 1.12.0 or higher cluster, you can use an `ncgctl` command to enable Network Connectivity Gateway. For more information, see Install.

To enable Network Connectivity Gateway during cluster creation:

  1. In the cluster configuration file, add the `baremetal.cluster.gke.io/enable-gng: "true"` annotation.
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:**  annotations:
             baremetal.cluster.gke.io/enable-gng: "true"**
           name: my-cluster
           namespace: cluster-my-cluster
         spec:
         ...
           anthosBareMetalVersion: 1.12.0
           ...
         

  2. Use `bmctl create` to create the cluster:
         
         bmctl create cluster -c CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name you that specified when you created the cluster configuration file. For more information about creating clusters, see [Cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs).




## Download

To download `ncgctl`, the Network Connectivity Gateway command-line tool, follow these steps:

  1. Download the Network Connectivity Gateway components and custom resource definitions:
         
         gcloud storage cp gs://ncg-release/anthos-baremetal/ncgctl-v1.12.0-linux-amd64.tar.gz .
         

  2. Extract the archive:
         
         tar -xvzf ncgctl-v1.12.0-linux-amd64.tar.gz
         




## Install

To install `ncgctl`, follow these steps:

  1. Run preflight checks to make sure the cluster satisfies the prerequisites. For example, make sure that Dataplane V2 is enabled.
         
         ./bin/ncgctl --verify --kubeconfig CLUSTER_KUBECONFIG
         

Replace `CLUSTER_KUBECONFIG` with the path of your cluster kubeconfig file.

  2. Install Network Connectivity Gateway.
         
         ./bin/ncgctl --install --kubeconfig CLUSTER_KUBECONFIG
         

**Note:** If you are creating a new version 1.12.0 cluster, you can skip the following steps. When you create clusters, we recommend that you add the `baremetal.cluster.gke.io/enable-gng: "true"` annotation to your cluster configuration file to enable Network Connectivity Gateway. For more information, see Cluster requirements.
  3. If you have an existing version 1.12.0 cluster, you can use the following `ncgctl` command to enable Network Connectivity Gateway:
         
         ./bin/ncgctl --enable-ncg-on-existing-cluster
         

The `ncgctl` command accepts `-e` as a shortened version of the enable flag.

  4. To see additional shortcuts and other command help, use the following command:
         
         ./bin/ncgctl --help
         




## Create a Secret for your pre-shared key

The gateways at either end of the IPsec tunnels use a Secret containing your pre-shared key for authentication.

To create the Secret, follow these steps:

  1. Create a file named `psk-secret.yaml` with the following Secret manifest details:
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: "ike-key"
           namespace: "kube-system"
         data:
           psk: PRE_SHARED_KEY
         

Replace `PRE_SHARED_KEY` with a [base64-encoded pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key). If you have a key in plaintext, encode the key to base64 format before you create this Secret. For example, if the Google Cloud console generated a key for you, it is in plaintext, and you must encode it. To base64 encode a key:
         
         echo -n PLAINTEXT_KEY | base64
         

  2. Create the Secret:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f psk-secret.yaml
         




## Create two `OverlayVPNTunnel` custom resources

To start two IPsec sessions, create two `OverlayVPNTunnel` custom resources.

  1. Create a file named `overlay-vpn-tunnels.yaml` with the following `OverlayVPNTunnel` manifest details:
         
         apiVersion: networking.gke.io/v1alpha1
         kind: OverlayVPNTunnel
         metadata:
           namespace: "kube-system"
           name: TUNNEL_1_NAME
         spec:
           ikeKey:
             name: "ike-key"
             namespace: "kube-system"
           peer:
             publicIP: PEER_PUBLIC_IP_1
           self:
             publicIP: SELF_PUBLIC_IP
           localTunnelIP: SELF_LOCAL_TUNNEL_IP_1
         ---
         apiVersion: networking.gke.io/v1alpha1
         kind: OverlayVPNTunnel
         metadata:
           namespace: "kube-system"
           name: TUNNEL_2_NAME
         spec:
           ikeKey:
             name: "ike-key"
             namespace: "kube-system"
           peer:
             publicIP: PEER_PUBLIC_IP_2
           self:
             publicIP: SELF_PUBLIC_IP
           localTunnelIP: SELF_LOCAL_TUNNEL_IP_2
         

Replace the following:

     * `TUNNEL_NAME_1`: a name of your choice for the first `OverlayVPNTunnel`.

     * `TUNNEL_NAME_2`: a name of your choice for the second `OverlayVPNTunnel`.

     * `PEER_PUBLIC_IP_1`: the public IP address of one interface on your HA VPN gateway. You specified this interface when you created your first VPN tunnel.

     * `PEER_PUBLIC_IP_2`: the public IP address of the other interface on your HA VPN gateway. You specified this interface when you created your second VPN tunnel.

     * `SELF_LOCAL_TUNNEL_IP_1`: the link-local address to be used in your cluster for BGP sessions over the first tunnel.

     * `SELF_LOCAL_TUNNEL_IP_2`: the link-local address to be used in your cluster for BGP sessions over the second tunnel. 

     * `SELF_PUBLIC_IP`: the public IP address for IPsec/VPN traffic that leaves your organization. This address might be the result of a network address translation (NAT).

  2. Create the two `OverlayVPNTunnels`:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f overlay-vpn-tunnels.yaml
         

  3. Check the status of the tunnels:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get OverlayVPNTunnel \
             --namespace kube-system --output yaml
         




## Create two `OverlayBGPPeer` custom resources

To start a BGP session over each of the tunnels, create two `OverlayBGPPeer` custom resources.

  1. Create a file named `overlay-bgp-peers.yaml` with the following `OverlayBGPPeer` manifest details.
         
         apiVersion: networking.gke.io/v1alpha1
         kind: OverlayBGPPeer
         metadata:
           namespace: "kube-system"
           name: BGP_PEER_1_NAME
         spec:
           localASN: LOCAL_ASN
           localIP: LOCAL_IP
           peerIP: PEER_IP_1
           peerASN: PEER_ASN
           vpnTunnel: TUNNEL_1_NAME
         ---
         apiVersion: networking.gke.io/v1alpha1
         kind: OverlayBGPPeer
         metadata:
           namespace: "kube-system"
           name: BGP_PEER_2_NAME
         spec:
           localASN: LOCAL_ASN
           localIP: LOCAL_IP
           peerIP: PEER_IP_2
           peerASN: PEER_ASN
           vpnTunnel: TUNNEL_2_NAME
         

Replace the following:

     * `BGP_PEER_1_NAME`: a name of your choice for the first `OverlayBGPPeer`.

     * `BGP_PEER_2_NAME`: a name of your choice for the second `OverlayBGPPeer`.

     * `LOCAL_ASN`: the ASN to be used in your cluster for BGP sessions.

     * `LOCAL_IP`: the public IP address for IPsec/VPN traffic that leaves your organization. This address might be the result of a network address translation (NAT).

     * `PEER_IP_1`: the public IP address of one interface on your HA VPN gateway. You specified this interface when you created your first VPN tunnel.

     * `PEER_IP_2`: the public IP address of the other interface on your HA VPN gateway. You specified this interface when you created your second VPN tunnel.

     * `PEER_ASN`: the ASN assigned to your Cloud Router for BGP sessions.

     * `TUNNEL_1_NAME`: the name of the first OverlayVPNTunnel that you created previously.

     * `TUNNEL_2_NAME`: the name of the second OverlayVPNTunnel that you created previously.

  2. Create the `OverlayBGPPeer` custom resources:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG apply -f overlay-bgp-peers.yaml
         

  3. Check the status of the BGP sessions:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get OverlayBGPPeer --namespace kube-system \
             --output yaml
         




## Check the status of Network Connectivity Gateway

The installation created a `NetworkConnectivityGateway` custom resource.

  * View the `NetworkConnectivityGateway` custom resource:
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG get NetworkConnectivityGateway --namespace kube-system \
            --output yaml
        

The output is similar to the following. Verify that you see `Status: Healthy`:
        
        apiVersion: networking.gke.io/v1alpha1
        kind: NetworkConnectivityGateway
        metadata:
          namespace: kube-system
          name: default
        spec:
        status:
            CurrNode: worker1-node
            CreatedTime: 2021-09-07T03:18:15Z
            LastReportTime: 2021-09-21T23:57:54Z
            Status:  Healthy
        




## Check the Network Connectivity Gateway logs

The gateway Pod belongs to a DaemonSet named `ncgd`, so the Pod name begins with `ncgd`.

To view the Network Connectivity Gateway logs, follow these steps:

  1. Find the name of the gateway Pod:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG pods --namespace kube-system | grep ncgd
         

  2. View the logs from the gateway Pod:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG logs GATEWAY_POD --namespace kube-system \
             --output yaml
         

Replace `GATEWAY_POD` with the name of the gateway Pod.




## Uninstall

To uninstall Network Connectivity Gateway from a cluster:
    
    
    ./bin/ncgctl –-uninstall --kubeconfig CLUSTER_KUBECONFIG
    

## Troubleshooting

For troubleshooting tips related to Network Connectivity Gateway, see [Troubleshooting Network Connectivity Gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/connect-google#network-connectivity-gateway-section). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
