---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/egress-and-ingress/
title: Control ingress and egress traffic \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:55.421168+00:00
---

# Control ingress and egress traffic  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/egress-and-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Control ingress and egress traffic Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure ingress and egress traffic for a VPN tunnel.

Control egress and ingress traffic to a VPN tunnel on a per-project basis.

  * By default, all projects will deny incoming traffic from a VPN tunnel.
  * By default, projects with data exfiltration protection enabled will deny outgoing traffic to a VPN tunnel.



Use the following directions to change the default VPN traffic egress and ingress rules for a project.

## Before you begin

To configure ingress and egress traffic for a VPN tunnel, you must have the following:

  * An existing VPN tunnel. For more information, see [Create a VPN tunnel](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-tunnel).
  * The necessary identity and access roles:

    * VPN Admin: has read and write permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Admin (`vpn-admin`) role.
    * VPN Viewer: has read permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Viewer (`vpn-viewer`) role.
    * Project NetworkPolicy Admin: manages project network policies in project namespace. Ask your Organization IAM Admin to grant you the Project NetworkPolicy Admin (`project-networkpolicy-admin`) role.
    * For more information, see [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions).



## Configure ingress traffic

By default, all projects deny incoming traffic from a VPN tunnel. To enable a project to allow traffic from a VPN tunnel, use a `ProjectNetworkPolicy` object which targets the routes received over the Border Gateway Protocol (BGP) session used on the VPN tunnel:

To enable a project to allow traffic from a VPN tunnel, follow thse steps:

  1. Retrieve all received routes from the `VPNBGPPeer` status:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER get -n platform vpnbgppeer VPN_BGP_PEER_NAME -ojson | jq '.status.received'
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `VPN_BGP_PEER_NAME`: the name of your VPN BGP session.

For more information, see [Create a VPN BGP session](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-routing#create-vpn-bgp-session).

The output looks like the following example:
    
    [
      {
        "prefix": "192.168.100.0/24"
      },
      {
        "prefix": "192.168.101.0/24"
      }
    ]
    

  2. Add all of the received routes from the `VPNBGPPeer` status to a `ProjectNetworkPolicy` object in the namespace of the project:
         
         kubectl --kubeconfig GLOBAL_API_SERVER create -n PROJECT_NAME -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           name: allow-ingress-vpn-traffic
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
           ingress:
           - from:
             - ipBlocks:
               - cidr: 192.168.100.0/24
               - cidr: 192.168.101.0/24
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).
     * `PROJECT_NAME`: the name of your GDC project.



## Configure egress traffic

By default, a project with data exfiltration protection enabled will deny sending traffic to the VPN.

You can allow a project to send traffic to a VPN tunnel by disabling data exfiltration protection for the project. For more information, see [Prevent data exfiltration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration#prevent-data-exfiltration).

## What's next

  * [Access user VMs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/access-vm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
