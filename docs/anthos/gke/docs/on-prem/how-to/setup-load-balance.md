---
url: https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/setup-load-balance/
title: Overview of load balancing for Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:45.676632+00:00
---

# Overview of load balancing for Google Distributed Cloud  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/setup-load-balance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Overview of load balancing for Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the load balancing options supported by Google Distributed Cloud for new clusters.

There are two load balancing options available to you. Choose the option that seems most suited to your environment and your needs. For example, you might choose an option that requires minimal configuration. Or you might choose an option that aligns with the load balancers you already have in your network.

These are the available options:

  * MetalLB bundled

  * Manual load balancing for any third-party load balancer, such as F5 BIG-IP Citrix




When you create user clusters using the Google Cloud console, the gcloud CLI, or Terraform, the kind of load balancer for the admin cluster and its user clusters must be the same. The only exception is if the admin cluster uses Seesaw, then the user clusters can use MetalLB. If you want your admin and user clusters to use different kinds of load balancers, you must create user clusters using the `gkectl` command-line tool.

## MetalLB

The MetalLB load balancer is bundled with Google Distributed Cloud and is especially easy to configure. The MetalLB components run on your cluster nodes, so you don't have to create separate VMs for your load balancer.

You can configure MetalLB to perform IP address management. This means that when a developer creates a Service of type `LoadBalancer`, they don't have to specify a VIP for the Service. Instead, MetalLB automatically chooses a VIP from an address pool that you provide ahead of time.

For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

## Citrix

We document how to set up the Citrix load balancer as an example of setting up a load balancer manually. With any load balancer that you set up manually, you must configure mappings between VIPs, node addresses, and `nodePort` values. For information, on how to do this for the Citrix load balancer, see [Manual load balancing with Citrix](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/citrix-load-balance).

## Manual load balancing in general

You can use any load balancer of your choice as long as you set it up manually. With any load balancer that you set up manually, you must configure mappings between VIPs, node addresses, and `nodePort` values. For general information on how to do this, see [Manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).

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

If you choose MetalLB as your load balancer, then you can either use static IP addresses for your cluster nodes, or you can have your cluster nodes get their IP addresses from a DHCP server

If you choose a manual load-balancing option, then you must use static IP addresses for your cluster nodes.

If you choose to use static IP addresses, you must set aside enough addresses for the nodes in the admin cluster and the nodes in all the user clusters you intend to create. For details about how many node IP addresses to set aside, see [Plan your IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses).

## Creating Services in your cluster

After your user cluster is running, application developers might want to create [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) and expose them to external clients.

For Services of type `LoadBalancer`, VIPs must be configured on the load balancer. How those VIPs get configured depends on your choice of load balancer.

### MetalLB

In the user cluster configuration file, you specify address pools that the MetalLB controller uses to assign VIPs to Services. When a developer creates a Service of type `LoadBalancer`, the MetalLB controller chooses an address from a pool and assigns the address to the Service. The developer does not have to specify a value for `loadBalancerIP` in the Service manifest.

### Manually configured load balancer

If you have chosen a manual load balancing option, developers can follow these steps to expose a Service to external clients:

  * Create a Service of type NodePort.

  * Choose a VIP for the Service.

  * Manually configure the load balancer so that traffic sent to the VIP is forwarded to the Service.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
