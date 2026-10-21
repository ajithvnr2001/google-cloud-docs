---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/setup-load-balance/
title: Overview of load balancing for Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:51.193848+00:00
---

# Overview of load balancing for Google Distributed Cloud  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/setup-load-balance/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Overview of load balancing for Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/setup-load-balance)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/setup-load-balance)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document explains the load balancing options supported by Google Distributed Cloud.

There are several load balancing options available to you. Choose the option that seems most suited to your environment and your needs. For example, you might choose an option that requires minimal configuration. Or you might choose an option that aligns with the load balancers you already have in your network.

These are the available options:

  * MetalLB bundled

  * Seesaw bundled (Not supported for user clusters using Controlplane V2.)

  * F5 BIG-IP integrated (Not supported for user clusters using Controlplane V2.)

  * F5 BIG-IP set up manually

  * Citrix set up manually

  * Any load balancer that you set up manually




## MetalLB

The MetalLB load balancer is bundled with Google Distributed Cloud and is especially easy to configure. The MetalLB components run on your cluster nodes, so you don't have to create separate VMs for your load balancer.

You can configure MetalLB to perform IP address management. This means that when a developer creates a Service of type `LoadBalancer`, they don't have to specify a VIP for the Service. Instead, MetalLB automatically chooses a VIP from an address pool that you provide ahead of time.

For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb).

## Seesaw

The Seesaw load balancer is bundled with Google Distributed Cloud and requires a bit more manual configuration than is required by MetalLB. The Seesaw load balancer runs on VMs that are separate from your cluster nodes. The Seesaw load balancer isn't supported for user clusters using Controlplane V2. We recommend that you use MetalLB instead.

For more information, see [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance).

## F5 BIG-IP

The F5 BIG-IP load balancer is not bundled with Google Distributed Cloud, so you must get a license and set up the load balancer separately from installing Google Distributed Cloud.

You can configure Google Distributed Cloud to be integrated with F5 BIG-IP in the following sense: when a developer creates a Service of type `LoadBalancer` and specifies a VIP for the service, Google Distributed Cloud will automatically configure the VIP on the load balancer.

The F5 BIG-IP integration isn't supported for user clusters using Controlplane V2. Instead, you can use F5 BIG-IP as a manually configured load balancer. In this case, Google Distributed Cloud does not automatically configure Service VIPs.

**Note:** These Service VIPs can share a subnet that is used by other clusters or applications.

## Citrix

We document how to set up the Citrix load balancer as an example of setting up a load balancer manually. With any load balancer that you set up manually, you must configure mappings between VIPs, node addresses, and `nodePort` values. For information, on how to do this for the Citrix load balancer, see [Manual load balancing with Citrix](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/citrix-load-balance).

## Manual load balancing in general

You can use any load balancer of your choice as long as you set it up manually. With any load balancer that you set up manually, you must configure mappings between VIPs, node addresses, and `nodePort` values. For general information on how to do this, see [Manual load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manual-load-balance).

## Setting aside virtual IP addresses

Regardless of which load balancer you use, you must set aside several virtual IP addresses (VIPs) that you intend to use for load balancing.

For your admin cluster, you must set aside these VIPs:

  * VIP for Kubernetes API server
  * VIP for add-ons



For each user cluster you intend to create, you must set aside these VIPs:

  * VIP for the Kubernetes API server
  * VIP for the ingress service



For example, suppose you intend to have two user clusters. Then you would need two VIPs for your admin cluster and two VIPs for each of your user clusters. So you would need to set aside six VIPs.

## Node IP addresses

If you choose one of the following load-balancing options, then you can either use static IP addresses for your cluster nodes, or you can have your cluster nodes get their IP addresses from a DHCP server:

  * MetalLB
  * Seesaw
  * F5 BIG-IP integrated



If you choose a manual load-balancing option, then you must use static IP addresses for your cluster nodes.

If you choose to use static IP addresses, you must set aside enough addresses for the nodes in the admin cluster and the nodes in all the user clusters you intend to create. For details about how many node IP addresses to set aside, see [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses).

## Creating Services in your cluster

After your user cluster is running, application developers might want to create [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) and expose them to external clients.

For Services of type `LoadBalancer`, VIPs must be configured on the load balancer. How those VIPs get configured depends on your choice of load balancer.

### MetalLB

In the user cluster configuration file, you specify address pools that the MetalLB controller uses to assign VIPs to Services. When a developer creates a Service of type `LoadBalancer`, the MetalLB controller chooses an address from a pool and assigns the address to the Service. The developer does not have to specify a value for `loadBalancerIP` in the Service manifest.

### Seesaw

When a developer creates a Service of type `LoadBalancer`, they specify an external IP address. For example:
    
    
    spec:
      type: LoadBalancer
      loadBalancerIP: 192.168.100.1
    

Google Distributed Cloud automatically configures the specified address on a network interface of a Seesaw VM.

### F5 BIG-IP integrated

When a developer creates a Service of type `LoadBalancer`, they specify an external IP address. For example:
    
    
    spec:
      type: LoadBalancer
      loadBalancerIP: 192.168.100.2
    

Google Distributed Cloud automatically configures the specified address on a network interface of the F5 BIG-IP load balancer.

### Manually configured load balancer

If you have chosen a manual load balancing option, developers can follow these steps to expose a Service to external clients:

  * Create a Service of type NodePort.

  * Choose a VIP for the Service.

  * Manually configure the load balancer so that traffic sent to the VIP is forwarded to the Service.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
