---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-tunnel/
title: Create a VPN tunnel \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:54.936294+00:00
---

# Create a VPN tunnel  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a VPN tunnel Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add a VPN tunnel from one VPN gateway to another.

A VPN tunnel is an encrypted IPsec tunnel between an organization network and a remote network. It connects a `VPNGateway` interface to a `PeerGateway` interface, and uses `VPNBGPPeer` resource to exchange routing information over the tunnel.

## Before you begin

To create a VPN tunnel, you must have the following:

  * An existing VPN gateway and VPN peer gateway resource. For more information, see [Create a VPN gateway and peer gateway](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-gateways).
  * An existing VPN BGP peer object. For more information, see [Create a VPN BGP session](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-routing).
  * An existing secret. For more information, see [Create the secret with a PSK](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/create-secret).
  * The necessary identity and access roles:

    * VPN Admin: has read and write permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Admin (`vpn-admin`) role.
    * VPN Viewer: has read permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Viewer (`vpn-viewer`) role.
    * For more information, see [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions).



## Create a VPN tunnel

Reference the `VPNGateway`, `PeerGateway`, `VPNBGPPeer`, and `Secret` resources created in the previous steps to create the tunnel.

To create a VPN tunnel, follow these steps:

  1. Create the `VPNTunnel` object:

**Note:** The `VPNTunnel` object must be created in the platform namespace.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER create -n platform -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: VPNTunnel
         metadata:
           name: VPN_TUNNEL_NAME
         spec:
           vpnInterface:
             name: VPN_GW_NAME
             namespace: platform
             interface: VPN_INTERFACE_NAME
           peerInterface:
             name: PEER_GW_NAME
             namespace: platform
             interface: PEER_INTERFACE_NAME
           vpnBGPPeer:
             name: VPN_BGP_PEER_NAME
             namespace: platform
           ikeKey:
             name: PSK_NAME
             namespace: platform
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `VPN_TUNNEL_NAME`: the name of the VPN tunnel being used.
     * `VPN_GW_NAME`: the name of the VPN gateway.
     * `VPN_INTERFACE_NAME`: the name of the VPN interface.
     * `PEER_GW_NAME`: the name of the peer VPN gateway.
     * `PEER_INTERFACE_NAME`: the name of the peer VPN gateway interface.
     * `VPN_BGP_PEER_NAME`: the name of the VPN BGP peer. For more information, see [Create a VPN BGP session](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-routing#create-vpn-bgp-session).
     * `PSK_NAME`: the name of the PSK you created in [Create the secret with a PSK](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/create-secret).
  2. Verify that the `VPN_TUNNEL_NAME` object was correctly reconciled by examining the `Status` field. Get the details of the VPN tunnel:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER describe -n platform vpntunnel VPN_TUNNEL_NAME
         

Examine the output, it must look similar to the following example:
         
         Status:
           Conditions:
             Last Transition Time:  2024-05-10T00:33:31Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  Reconciled
             Last Transition Time:  2024-05-10T00:33:31Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  Ready
             Last Transition Time:  2024-05-10T00:33:31Z
             Message:               Tunnel is established.
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  TunnelEstablished
           State:                   Established
         

  3. The `VPNGateway`, `PeerGateway`, and `VPNBGPPeer` objects must have updated statuses after being referenced by a `VPNTunnel`. For example, if you verify that the `VPNBGPPeer` was correctly reconciled, you see updated status values. Get the details of the `VPNBGPPeer` object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER describe -n platform vpnbgppeer VPN_BGP_PEER_NAME
         

Examine the output, the status values are now updated:
         
         Status:
           Advertised:
             Prefix:  10.0.0.16/28
             Prefix:  10.0.1.32/27
             Prefix:  172.16.0.0/14
             Prefix:  172.20.0.0/17
             Prefix:  172.20.128.0/17
             Prefix:  2002:4860:100e:fa00::/58
           Conditions:
             Last Transition Time:  2024-05-10T00:36:38Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  ValidIPs
             Last Transition Time:  2024-05-10T00:36:38Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  TunnelsAttached
             Last Transition Time:  2024-05-10T00:36:38Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  Reconciled
             Last Transition Time:  2024-05-10T00:36:38Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  AdvertisedRoutesReady
             Last Transition Time:  2024-05-10T00:36:38Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  ReceivedRoutesValid
             Last Transition Time:  2024-05-10T00:36:38Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  ReceivedRoutesReady
             Last Transition Time:  2024-05-10T00:36:38Z
             Message:               Ready
             Observed Generation:   1
             Reason:                Ready
             Status:                True
             Type:                  Ready
           Received:
             Prefix:  192.168.100.0/24
             Prefix:  193.188.200.0/24
           State:     Established
         




## What's next

  * [Control egress and ingress traffic](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/egress-and-ingress)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
