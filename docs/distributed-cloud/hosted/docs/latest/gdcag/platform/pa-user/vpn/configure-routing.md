---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-routing/
title: Create a VPN BGP session \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:54.513626+00:00
---

# Create a VPN BGP session  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a VPN BGP session Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the specifications a VPN Border Gateway Protocol (BGP) session must adhere to and how to create a VPN BGP session.

Google Distributed Cloud (GDC) air-gapped VPN supports dynamic routing using an IPv4 BGP session for each VPN tunnel. The BGP session lets the BGP peers in the remote network and in the GDC organization advertise routes to each other.

## Before you begin

To create a VPN BGP session, you must have the necessary identity and access roles:

  * VPN Admin: has read and write permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Admin (`vpn-admin`) role.
  * VPN Viewer: has read permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Viewer (`vpn-viewer`) role.
  * For more information, see [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions).



## VPN BGP session specifications

The BGP peer in the organization supports a BGP keepalive interval of 30 seconds, with a hold timer of 90 seconds.For each BGP session, the IPv4 addresses must meet the following requirements:

  * Each BGP IPv4 address must belong to the same `/30` subnet that fits within the `169.254.0.0/16` range.
  * Each BGP IPv4 address is the first or second host of the `/30` subnet. The first and the last IP addresses of the subnet are reserved for network and broadcast addresses.
  * Each BGP address range for each BGP session must be unique among all VPN BGP sessions for the organization.



MD5 authentication is not supported. This is a method of verifying the integrity and authenticity of data using the MD5 hashing algorithm.

## Create a VPN BGP session

To create a BGP session for the VPN tunnel, follow these steps:

  1. Create a `VPNBGPPeer` object in the org admin cluster in the platform namespace:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER create -n platform -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: VPNBGPPeer
         metadata:
           name: VPN_BGP_PEER_NAME
         spec:
           remote:
             name: REMOTE_PEER_NAME
             ip: REMOTE_PEER_IP
             asn: REMOTE_PEER_ASN
           local:
             name: LOCAL_PEER_NAME
             ip: LOCAL_PEER_IP
             asn: LOCAL_PEER_ASN
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `VPN_BGP_PEER_NAME`: the name of the VPN BGP peer.
     * `REMOTE_PEER_NAME`: the name for the BGP peer in the remote network.
     * `REMOTE_PEER_IP`: the BGP IPv4 address from the `/30` subnet of the BGP peer in the remote network.
     * `REMOTE_PEER_ASN`: the Autonomous System Number (ASN) configured for the remote network.
     * `LOCAL_PEER_NAME`: a name for the BGP peer in the GDC organization.
     * `LOCAL_PEER_IP`: the BGP IPv4 address from the `/30` subnet of the BGP peer in the GDC organization.
     * `LOCAL_PEER_ASN`: the ASN configured for the GDC organization.
  2. Verify that the `VPN_BGP_PEER_NAME` object was correctly reconciled by examining the `Status` field. Get the details of the `VPNBGPPeer` object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER describe -n platform vpnbgppeer VPN_BGP_PEER_NAME
         

Examine the output, it must look similar to the following example:
         
         Status:
             Conditions:
               Last Transition Time:  2024-05-10T00:26:13Z
               Message:               Ready
               Observed Generation:   1
               Reason:                Ready
               Status:                True
               Type:                  ValidIPs
               Last Transition Time:  2024-05-10T00:26:00Z
               Message:               Used by 0 VPNTunnels, must be used by a single VPNTunnel
               Observed Generation:   1
               Reason:                GetResourceFailed
               Status:                False
               Type:                  TunnelsAttached
               Last Transition Time:  2024-05-10T00:26:00Z
               Message:               TunnelsAttached or ValidIPs Condition not Ready.
               Observed Generation:   1
               Reason:                Unknown
               Status:                False
               Type:                  Reconciled
               Last Transition Time:  2024-05-10T00:26:01Z
               Message:               ValidIPs or Reconciled Condition not Ready.
               Observed Generation:   1
               Reason:                Unknown
               Status:                False
               Type:                  AdvertisedRoutesReady
               Last Transition Time:  2024-05-10T00:26:13Z
               Message:               Ready
               Observed Generation:   1
               Reason:                Ready
               Status:                True
               Type:                  ReceivedRoutesValid
               Last Transition Time:  2024-05-10T00:26:01Z
               Message:               TunnelsAttached Condition not Ready.
               Observed Generation:   1
               Reason:                Unknown
               Status:                False
               Type:                  ReceivedRoutesReady
               Last Transition Time:  2024-05-10T00:26:01Z
               Message:               Condition "TunnelsAttached" is not ready.
               Observed Generation:   1
               Reason:                NotReady
               Status:                False
               Type:                  Ready
           ```
         




The `VPNBGPPeer` must be attached to a `VPNTunnel`. We handle this step in [Create a VPN Tunnel](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-tunnel#create-a-vpn-tunnel).

## What's next

  * [Create the secret with a PSK](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/create-secret)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
