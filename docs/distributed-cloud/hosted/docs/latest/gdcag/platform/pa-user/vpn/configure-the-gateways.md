---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-gateways/
title: Create a VPN gateway and peer gateway \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:22.699381+00:00
---

# Create a VPN gateway and peer gateway  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-gateways/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a VPN gateway and peer gateway Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a VPN gateway or a peer gateway resource.

VPN gateways provide secure connectivity between multiple sites, such as between on-premises data centers and cloud environments. There are two gateway components to configure for Google Distributed Cloud (GDC) air-gapped VPN:

  * A VPN gateway in GDC.
  * Your peer VPN gateway. This is a physical VPN gateway device or software application in the peer network to which the VPN gateway connects. The peer gateway can either be an on-premises VPN gateway or one hosted by another cloud provider.



## Before you begin

To manage or view VPN resources from the GDC console, you must have the necessary identity and access roles:

  * VPN Admin: has read and write permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Admin (`vpn-admin`) role.
  * VPN Viewer: has read permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Viewer (`vpn-viewer`) role.
  * For more information, see [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions).



## Create a VPN gateway

To create a VPN gateway, follow these steps:

  1. Specify an interface name on the gateway to represent the IP address. When the gateway is created an external IPv4 address is automatically allocated. Create the VPN gateway object in the platform namespace:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER create -n platform -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: VPNGateway
         metadata:
           name: VPN_GW_NAME
         spec:
           interfaces:
           - name: VPN_INTERFACE_NAME
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `VPN_GW_NAME`: the name of the VPN gateway object. For example, `vpngateway`.
     * `VPN_INTERFACE_NAME`: the name of the VPN interface. For example, `interface0`.
  2. Verify that the `VPN_GW_NAME` object was correctly reconciled by examining the `Status` field. Get the details for the VPN gateway object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER describe -n platform vpngateway VPN_GW_NAME
         

Examine the output, it must look similar to the following example:
         
         status:
           conditions:
           - lastTransitionTime: "2024-05-10T00:12:58Z"
             message: All interfaces are assigned an IP.
             observedGeneration: 1
             reason: Ready
             status: "True"
             type: IPsAssigned
           - lastTransitionTime: "2024-05-10T00:12:36Z"
             message: Condition "TunnelsAttached" is not ready.
             observedGeneration: 1
             reason: NotReady
             status: "False"
             type: Ready
           - lastTransitionTime: "2024-05-10T00:12:36Z"
             message: 'At least one interface is not attached to any VPNTunnel: ["interface0"]'
             observedGeneration: 1
             reason: NoTunnelAttached
             status: "False"
             type: TunnelsAttached
           interfaces:
           - ip: 10.252.218.240
             name: interface0
         




The `VPNGateway` object must be attached to a `VPNTunnel`. We handle this step in [Create a VPN Tunnel](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-tunnel#create-a-vpn-tunnel).

## Create a peer VPN gateway

Create a peer VPN gateway by creating a `PeerGateway` object in the Management API server. The `PeerGateway` object represents a remote VPN endpoint. An interface on a `PeerGateway` object is used by a VPN tunnel to establish an encrypted tunnel to the remote site. To create a peer VPN gateway, follow these steps:

  1. Specify an interface name and the static external IPv4 address of your peer VPN gateway. Create the `PeerGateway` object must be created in the platform namespace:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER create -n platform -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: PeerGateway
         metadata:
           name: PEER_GW_NAME
         spec:
           interfaces:
           - name: PEER_INTERFACE_NAME
             ip: PEER_INTERFACE_IP
         EOF
         

Replace the following:

     * `PEER_GW_NAME`: the name of the peer VPN gateway. For example, `peergateway`.
     * `PEER_INTERFACE_NAME`: the name of the peer interface. For example, `interface0`.
     * `PEER_INTERFACE_IP`: the static external IPv4 address of your peer VPN gateway.
  2. Verify that the `PEER_GW_NAME` object was correctly reconciled by examining the `Status` field.

Get the details for the peer VPN gateway object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER describe -n platform peergateway PEER_GW_NAME
         

Examine the output, it must look similar to the following example:
         
         Status:
           Conditions:
             Last Transition Time:  2024-05-10T00:15:25Z
             Message:               Condition "TunnelsAttached" is not ready.
             Observed Generation:   1
             Reason:                NotReady
             Status:                False
             Type:                  Ready
             Last Transition Time:  2024-05-10T00:20:45Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  ValidGatewayIPs
             Last Transition Time:  2024-05-10T00:15:25Z
             Message:               At least one interface is not attached to any VPNTunnel: ["interface0"]
             Observed Generation:   1
             Reason:                NoTunnelAttached
             Status:                False
             Type:                  TunnelsAttached
         

The `PeerGateway` object must be referenced by a `VPNTunnel`. We handle this step in [Create a VPN Tunnel](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-tunnel#create-a-vpn-tunnel).




## What's next

  * [Create a VPN BGP session](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-routing)
  * [Supported IKE ciphers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/supported-ike-ciphers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
