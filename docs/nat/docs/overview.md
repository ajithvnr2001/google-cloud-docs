---
url: https://docs.cloud.google.com/nat/docs/overview/
title: Cloud NAT overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:59.549772+00:00
---

# Cloud NAT overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud NAT overview

Cloud NAT provides [network address translation](https://www.wikipedia.org/wiki/Network_address_translation) (NAT) for outbound traffic to the internet, Virtual Private Cloud (VPC) networks, on-premises networks, and other cloud provider networks.

Cloud NAT translates addresses for the following resources:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs/overview) virtual machine (VM) instances
  * [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) clusters

  * [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) instances 

  * [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) instances 

  * [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard) instances 

  * Regional [internet network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#nat-support)




NAT is automatically applied to the resources that match your Cloud NAT configuration after you create a Cloud NAT gateway and configure it to serve the subnets where those resources run.

Cloud NAT supports address translation for established inbound response packets only. It doesn't allow unsolicited inbound connections.

## Types of Cloud NAT

You configure Cloud NAT by creating a Cloud NAT gateway in the region of the subnets that require NAT. The gateway then serves each subnet that you specify in its configuration.

Cloud NAT supports two types of NAT:

  * Public NAT
  * Private NAT



A single Cloud NAT gateway provides either Public NAT or Private NAT. By creating two separate gateways, you can use both NAT types to serve the same subnet.

Both Public NAT and Private NAT can translate addresses from IPv4 to IPv4 and from IPv6 to IPv4.

### Public NAT

Public NAT lets Google Cloud resources that don't have external IPv4 addresses communicate with IPv4 destinations on the internet. These VMs use a set of shared external IP addresses to connect to the internet. Cloud NAT doesn't rely on proxy VMs. Instead, a Cloud NAT gateway allocates a set of external IP addresses and source ports to each VM that uses the gateway to create outbound connections to the internet.

Consider a scenario in which you have `VM-1` in `subnet-1` whose network interface doesn't have an external IP address. However, `VM-1` needs to connect to the internet to download updates. To enable connectivity to the internet, you can create a Cloud NAT gateway that is configured to apply to the IP address range of `subnet-1`. Now, `VM-1` can send traffic to the internet by using the internal IP address of `subnet-1`.

For more information, see [Public NAT](https://docs.cloud.google.com/nat/docs/public-nat).

**Note:** Traffic sent to Google APIs and services are routed through [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) even if the VM instance initiating the connections uses Public NAT. For more information, see [Private Google Access interaction](https://docs.cloud.google.com/nat/docs/nat-product-interactions#interaction-pga). 

### Private NAT

Private NAT enables private-to-private address translation for the following destinations.

Destination | Description  
---|---  
Another VPC network | Private NAT supports NAT for VPC networks attached to a Network Connectivity Center hub. For more information, see:

  * [Private NAT for NCC spokes](https://docs.cloud.google.com/nat/docs/about-private-nat-for-ncc) (NAT44)
  * [NAT64 in Private NAT](https://docs.cloud.google.com/nat/docs/private-nat#nat64)

  
Same VPC network | Private NAT supports NAT for IPv6 traffic within the same VPC network. For more information, see [NAT64 in Private NAT](https://docs.cloud.google.com/nat/docs/private-nat#nat64).  
On-premises or another cloud provider network | Private NAT supports the following options for traffic between VPC networks and on-premises or other cloud provider networks:

  * NAT for networks connected through NCC hybrid spokes. For more information, see: 
    * [Private NAT for NCC spokes](https://docs.cloud.google.com/nat/docs/about-private-nat-for-ncc) (NAT44)
    * [NAT64 in Private NAT](https://docs.cloud.google.com/nat/docs/private-nat#nat64)
  * NAT for networks connected through Cloud Interconnect or Cloud VPN. For more information, see: 
    * [Hybrid NAT](https://docs.cloud.google.com/nat/docs/about-hybrid-nat) (NAT44)
    * [NAT64 in Private NAT](https://docs.cloud.google.com/nat/docs/private-nat#nat64)

  
  
If your VPC network has IPv4 subnets that overlap with the destination network, you can use Private NAT to enable communication between the networks. The NAT gateway translates source traffic to unique IP addresses, which lets your Google Cloud resources connect to any non-overlapping subnets of the destination network.

For more information, see [Private NAT](https://docs.cloud.google.com/nat/docs/private-nat).

### Supported resources

The following table lists the Google Cloud resources that are supported by each type of Cloud NAT. The checkmark indicates that the resource is supported.

Resource | Public NAT | Private NAT  
---|---|---  
Compute Engine VM instances |  |   
GKE clusters |  |   
Cloud Run, Cloud Run functions, and App Engine1 |  |   
Regional internet NEGs |  | Not applicable  
  
1 The following serverless endpoints are supported: 

  * Cloud Run instances (services and jobs) and Cloud Run functions instances through Direct VPC egress (recommended) or Serverless VPC Access
  * App Engine standard environment instances through Serverless VPC Access



## Architecture

Cloud NAT is a distributed, software-defined managed service. It's not based on proxy VMs or appliances. Cloud NAT configures the [Andromeda software](https://cloudplatform.googleblog.com/2014/04/enter-andromeda-zone-google-cloud-platforms-latest-networking-stack.html) that powers your Virtual Private Cloud (VPC) network so that it provides _source network address translation (source NAT or SNAT)_ for resources. Cloud NAT also provides _destination network address translation (destination NAT or DNAT)_ for established inbound response packets.

[ ![Traditional NAT versus Cloud NAT.](https://docs.cloud.google.com/static/nat/images/07.svg)](https://docs.cloud.google.com/static/nat/images/07.svg) Traditional NAT versus Cloud NAT (click to enlarge).

## Benefits

Cloud NAT provides the following benefits:

  * **Security**

When using a Cloud NAT gateway for Public NAT, you can reduce the need for individual VMs to each have external IP addresses. Subject to egress [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls), VMs without external IP addresses can access destinations on the internet. For example, you might have VMs that only need internet access to download updates or to complete provisioning.

If you use [manual NAT IP address assignment](https://docs.cloud.google.com/nat/docs/ports-and-addresses#addresses) to configure a Cloud NAT gateway for Public NAT, you can confidently share a set of common external source IP addresses with a destination party. For example, a destination service might only allow connections from known external IP addresses.

Private NAT enables private-to-private NAT between VPC networks or between VPC and on-premises or other cloud provider networks. When Private NAT is configured, the Cloud NAT gateway performs NAT by using IP addresses from the Private NAT subnet range.

  * **Availability**

Cloud NAT is a distributed, software-defined managed service. It doesn't depend on any VMs in your project or a single physical gateway device. You configure a NAT gateway on a Cloud Router, which provides the control plane for NAT, holding configuration parameters that you specify. Google Cloud runs and maintains processes on the physical machines that run your Google Cloud VMs.

  * **Scalability**

Cloud NAT can be configured to automatically scale the number of NAT IP addresses that it uses, and it supports VMs that belong to managed instance groups, including the groups with [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) enabled.

  * **Performance**

Cloud NAT does not reduce the network bandwidth per VM. Cloud NAT is implemented by Google's Andromeda software-defined networking. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth) in the Compute Engine documentation.

  * **Logging**

For Cloud NAT traffic, you can trace the connections and bandwidth for compliance, debugging, analytics, and accounting purposes.

  * **Monitoring**

Cloud NAT exposes key metrics to Cloud Monitoring that give you insight into your fleet's use of NAT gateways. Metrics are sent automatically to Cloud Monitoring. There, you can create custom dashboards, set up alerts, and query metrics.

Additionally, Network Analyzer publishes [Cloud NAT insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/network-services/cloud-nat). Network Analyzer automatically monitors your Cloud NAT configuration to detect and generate these insights. 




## Product interactions

For more information about the important interactions between Cloud NAT and other Google Cloud products, see [Cloud NAT product interactions](https://docs.cloud.google.com/nat/docs/nat-product-interactions).

## What's next

  * Learn about [Cloud NAT product interactions](https://docs.cloud.google.com/nat/docs/nat-product-interactions)
  * Learn about [IP addresses and ports](https://docs.cloud.google.com/nat/docs/ports-and-addresses)
  * [Set up and manage network address translation with Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation)
  * Learn about [Cloud NAT rules](https://docs.cloud.google.com/nat/docs/nat-rules-overview)
  * [Set up and manage network address translation with Private NAT](https://docs.cloud.google.com/nat/docs/set-up-private-nat)
  * [Troubleshoot configuration](https://docs.cloud.google.com/nat/docs/troubleshooting)
  * Learn about [Cloud NAT pricing](https://cloud.google.com/nat/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
