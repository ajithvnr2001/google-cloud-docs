---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/create-vlan-attachment/
title: Create a VLAN attachment \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:06.840285+00:00
---

# Create a VLAN attachment  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/create-vlan-attachment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a VLAN attachment Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on how to create or update a VLAN attachment in Google Distributed Cloud (GDC) air-gapped.

A VLAN attachment represents an attachment of a Virtual Local Area Network (VLAN) and its associated BGP session configuration to an interconnect link. The VLAN specifies which part of your network has access through this connection.

The VLAN attachment and its associated BGP session configuration are a required resource for setting up a secure air-gapped connection with high bandwidth and low latency.

This page is for developers within the application operator group who are looking to establish connectivity with interconnects. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create or update a VLAN attachment, you must have the following:

  * A submitted ticket in the GDC portal requesting an interconnect with your chosen specifications, such as 10 G of redundant connectivity.
  * The necessary resource information and IDs for the interconnect resources that the Infrastructure Operator (IO) configures. For more information, see [Interconnect creation process](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview#interconnect-creation).
  * The necessary identity and access roles. For more information, see [Prepare predefined roles and permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview#prepare-roles).



## Create or update a VLAN attachment

To create or update a VLAN attachment, follow these steps:

  1. Create a YAML file named `interconnectattachment.yaml`.
  2. Add the following content to the file:
         
         apiVersion: system.private.gdc.goog/v1alpha1
         kind: InterconnectAttachment
         metadata:
           name: UNIQUE_INTERCONNECT_NAME
           namespace: gpc-system
         spec:
           interconnectLinkRef:
             name: INTERCONNECT_LINK_NAME
             namespace: gpc-system
           parentInterconnectRef:
             name: INTERCONNECT_GROUP_NAME
             namespace: gpc-system
           parentInterconnectType: DirectConnect
           bgpSessionConfig:
             localIP: LOCAL_IP_SUBNET
             localASN: LOCAL_ASN
             peerASN: PEER_ASN
             peerIP: PEER_IP
           peerExternalSubnets:
             - PEER_EXTERNAL_SUBNET
           routePolicyRef:
             name: ROUTE_POLICY_NAME
             namespace: gpc-system
           attachmentGroup:
             name: ATTACHMENT_GROUP_NAME
             namespace: gpc-system
           vlanID: VLAN_ID
         status: {}
         
         

  3. Replace the following:

     * `UNIQUE_INTERCONNECT_NAME`: unique name for this `InterconnectAttachment` resource.
     * `INTERCONNECT_LINK_NAME`: the universal object reference to the interconnect link in the `gpc-system` namespace.
     * `INTERCONNECT_GROUP_NAME`: the universal object reference to the interconnect group in the `gpc-system` namespace containing `INTERCONNECT_LINK_NAME`.
     * `LOCAL_IP_SUBNET`: the local IP address of the `/31` peer on the GDC side.
     * `LOCAL_ASN`: the local autonomous system number (ASN) of the Border Gateway Protocol (BGP).
     * `PEER_ASN`: the peer autonomous system number (ASN) of the Border Gateway Protocol (BGP).
     * `PEER_IP`: the peer IP address of the `/31` peer on the side of the peer.
     * `PEER_EXTERNAL_SUBNET`: the peer external subnet that this interconnect allows. If there is more than one subnet, list all of them in the `peerExternalSubnets` field.
     * `ROUTE_POLICY_NAME`: the universal object reference to the route policy in the `gpc-system` namespace.
     * `ATTACHMENT_GROUP_NAME`: the universal object reference to the attachment group in the `gpc-system` namespace that this attachment is a part of.
     * `VLAN_ID`: the VLAN ID to use on this interconnect.

Keep `parentInterconnectType` set to `DirectConnect`. VLAN attachments that you create in your organization must use this type. The `CustomerPeering` type is on the deprecation path. For more information, see [Interconnect types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview#interconnect-types).

  4. Create the VLAN attachment:
         
         kubectl apply -f interconnectattachment.yaml -n gpc-system
         --kubeconfig=MANAGEMENT_API_SERVER
         

Replace `MANAGEMENT_API_SERVER` with the path to the kubeconfig file for the Management API server.

  5. Check that the creation of the VLAN attachment is successful:
         
         kubectl get interconnectattachment -n gpc-system
         --kubeconfig=MANAGEMENT_API_SERVER
         

  6. The output returns the VLAN attachment and shows `True` in the `Ready` column:
         
         NAME                                                   AGE    TYPE            MTU   VLAN-ID   INTERCONNECT GROUP                   INTERCONNECT LINK                           READY
         interconnect-attachment-zv-aa-blsw01-directconnect-1   3d2h   DirectConnect         3966      interconnect-group-directconnect-1   interconnect-zv-aa-blsw01-directconnect-1   True
         




## What's next

  * [Configure external probe targets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/external-targets-probe)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
