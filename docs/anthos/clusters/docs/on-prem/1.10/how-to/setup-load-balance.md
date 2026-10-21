---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/setup-load-balance/
title: Setting up your load balancer for Google Distributed Cloud \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:58.185283+00:00
---

# Setting up your load balancer for Google Distributed Cloud  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/setup-load-balance/

**Version 1.10**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.10 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/overview)



Send feedback 

#  Setting up your load balancer for Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.10 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/setup-load-balance)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/setup-load-balance)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud clusters can run load balancers in one of three ways: integrated, bundled, or manual. With the integrated option, an Google Distributed Cloud cluster uses the F5 BIG-IP load balancer.

With the bundled option, Google Distributed Cloud provides and manages the load balancer. You do not have to get a license for a load balancer, and the amount of setup that you have to do is minimal.

### Advantages of bundled load balancing

Bundled load balancing provides these advantages compared to manual load balancing:

  * A single team can be in charge of both cluster creation and load balancer configuration. For example, a cluster administration team would not have to rely on a separate networking team to acquire, run, and configure the load balancer ahead of time.

  * Google Distributed Cloud automatically configures virtual IP addresses (VIPs) on the load balancer. At cluster creation time, Google Distributed Cloud configures the load balancer with VIPs for the Kubernetes API server, the ingress service, and the cluster add-ons. As clients create Services of type LoadBalancer, Google Distributed Cloud automatically configures the Service VIPs on the load balancer.

  * Dependencies among organizations, groups, and administrators are reduced. In particular, the group that manages a cluster is less dependent on the group that manages the network.




With the manual option, Google Distributed Cloud uses a different load balancer of your choice. Manual load balancing requires that you do more configuration than with the integrated option.

If you choose to use the F5 BIG-IP load balancer, you need to have a [user role](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-user-account-administration-11-6-0/3.html) that has sufficient permissions to set up and manage the load balancer. Either the Administrator role or the Resource Administrator role is sufficient.

This topic describes setting aside IP addresses and `nodePort` values for later use. The idea is that you choose the IP addresses and `nodePort` values that you want to use for load balancing and for your cluster nodes. But you don't do anything with the addresses and `nodePort` values at this point. Later, when you are ready to install Google Distributed Cloud, you will need the addresses and `nodePort` values to fill in your cluster configuration file.

## Setting aside virtual IP addresses

Regardless of which load balancing method you use, you must set aside several virtual IP addresses (VIPs) that you intend to use for load balancing. With integrated and bundled load balancing, you specify these VIPs in your cluster configuration file, and Google Distributed Cloud automatically configures the F5 BIG-IP, MetalLB, or Seesaw load balancer to use the VIPs. With manual load balancing, you must manually configure your load balancer to use the VIPs.

For your admin cluster, you must set aside this VIP:

  * VIP for Kubernetes API server



For each user cluster you intend to create, you must set aside these VIPs:

  * VIP for the Kubernetes API server
  * VIP for the ingress service



If you intend to use add-ons in your admin cluster, you must set aside a VIP for the addon service in the admin cluster.

For example, suppose you intend to have two user clusters, and you intend to use addons. Then you would need two VIPs for your admin cluster and two VIPs for each of your user clusters. So you would need to set aside six VIPs.

## Setting aside node IP addresses

With integrated or bundled load balancing, you can use an existing Dynamic Host Configuration Protocol (DHCP) server to provide IP addresses for your cluster nodes, or you can specify static IP addresses for nodes. With manual load balancing, you cannot use DHCP. You must specify static IP addresses for your nodes.

If you choose to use static IP addresses, you must set aside enough addresses for the nodes in the admin cluster and the nodes in all the user clusters you intend to create. For details about how many node IP addresses to set aside, see [Creating an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/create-admin-cluster).

## Setting aside `nodePort` values

In Google Distributed Cloud clusters, the Kubernetes API server, the ingress service, and the addon service are implemented as [Kubernetes Services of type `NodePort`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#service_of_type_nodeport). With integrated or bundled load balancing, Google Distributed Cloud chooses the `nodePort` values for these Services automatically. With manual load balancing, you must specify the `nodePort` values to be used for these Services. For more information, see [Setting aside `nodePort` values](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/manual-load-balance#set_aside_nodeports).

## Configuring the load balancer

With integrated or bundled load balancing, Google Distributed Cloud automatically configures the load balancer with the VIPs that you specify in the cluster configuration file. With manual load balancing, you must configure your load balancer with the VIPs you have chosen. How you configure your load balancer depends on which load balancer you are using. For more information, see [Enabling manual load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/manual-load-balance).

## Summary of preparing for load balancing

The following table summarizes what you must do to prepare for integrated and manual load balancing:

| Integrated/Bundled| Manual  
---|---|---  
Choose VIPs before you create your clusters.| Yes| Yes  
Choose node IP addresses before you create your clusters.| No, if using DHCP.  
Yes, if using static IP addresses.| Yes  
Choose `nodePort` values before you create your clusters.| No| Yes  
Manually configure your load balancer| No| Yes  
  
## Creating Services in your cluster

After your user cluster is running, you might want to create [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) and expose them to external clients.

Regardless of whether you are using integrated, bundled or manual load balancing, you can expose Services to external clients by using [Ingress objects](https://kubernetes.io/docs/concepts/services-networking/ingress/).

With integrated or bundled load balancing, you can create a Service of type `LoadBalancer` and specify a VIP for the Service. Google Distributed Cloud automatically configures the VIP on the load balancer.

With manual load balancing, you cannot expose a Service of type `LoadBalancer` to external clients. Instead, you can use these steps to expose a Service to external clients:

  * Create a Service of type NodePort.

  * Choose a VIP for your Service.

  * Manually configure your load balancer so that traffic sent to the VIP is forwarded to your Service.




The following table summarizes the kinds of Services you can expose with the different load balancing options:

| Integrated/Bundled| Manual  
---|---|---  
Expose Services to external clients by using Ingress objects.| Yes| Yes  
Expose Services of type `ClusterIP` to internal clients.| Yes| Yes  
Expose Services of type `NodePort` to external clients.| Yes| Yes  
Expose Services of type `LoadBalancer` to external clients.| Yes| No  
  
## What's next

  * [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance-metallb)
  * [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/bundled-load-balance)
  * [Enabling manual load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/manual-load-balance)
  * [Load balancing with Citrix](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/citrix-load-balance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
