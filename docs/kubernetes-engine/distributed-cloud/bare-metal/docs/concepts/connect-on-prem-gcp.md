---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/connect-on-prem-gcp/
title: Connect to Google \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:29.710598+00:00
---

# Connect to Google  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/connect-on-prem-gcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Connect to Google Stay organized with collections  Save and categorize content based on your preferences. 

There are various ways that you can connect Google Distributed Cloud clusters, running in your on-premises data center, to the Google Cloud network. Possibilities include:

  * Regular internet connection
  * [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview)
  * [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview)



## Regular internet connection

In certain scenarios, you can use the internet as the connection between Google and your on-premises data center. For example:

  * Your Google Distributed Cloud deployment is self-contained on your premises, and your on-premises components seldom communicate with the Google Cloud network. You use the connection primarily for cluster management. The speed, reliability, and security of the connection are not critical.

  * Your on-premises cluster is self-contained, except for access to a Google service like Cloud SQL. Traffic between your on-premises cluster and the Google service uses public IP addresses. You configure firewall rules to provide security.




## HA VPN

With [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) and [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router), traffic between Google and your on-premises data center traverses the public internet, but is encrypted. on-premises components can communicate with cloud components using private IP addresses. Cloud Router dynamically exchanges routes between your Google Cloud networks and your on-premises network. Dynamic routing is especially beneficial as your network expands and changes, because it ensures that the correct routing state is propagated to your on-premises data center.

One way to set up an HA VPN between Google Cloud and an on-premises GKE Enterprise cluster is to configure [Network Connectivity Gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/network-connectivity-gateway) in the cluster. Network Connectivity Gateway is available for [Preview](https://cloud.google.com/products/#product-launch-stages).

## Partner Interconnect

[Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) provides connectivity between your on-premises network and the Google Cloud network through a supported service provider. Traffic between Google and your on-premises data center does not traverse the public internet. On-premises components can communicate with cloud components using private IP addresses. Your connection to Google is fast, secure, and reliable.

## Dedicated Interconnect

[Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) provides a direct physical connection between your on-premises network and the Google Cloud network. This type of connection can be cost-effective if you need high bandwidth. Traffic between Google and your on-premises data center does not traverse the public internet. On-premises components can communicate with cloud components using private IP addresses. Your connection to Google is secure and reliable, and is even faster than a connection using Partner Interconnect.

## Impact of a temporary disconnection

For information on what happens if you're disconnected, see [Impact of temporary disconnection from Google Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/connectivity).

## Choosing a connection type

For additional guidance on choosing a connection type, see:

  * [Choosing a VPN Routing Option](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-vpn)
  * [Choose an Interconnect Type](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect)



## Network monitoring

Regardless of how you establish a fundamental connection to Google, you can benefit from insights provided by network logging and monitoring. For more information, see [Logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring) for Google Distributed Cloud.

## Enhancing your fundamental connection

After your fundamental connection is in place, you can add features that enhance access, security, and visibility. For example, you could enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access), [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview), or [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs).

The remainder of the guidance in this topic assumes you're using one of the following options for your fundamental connection to Google:

  * [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview)
  * [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview)



### Private Google Access

[Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) enables VMs that have only private IP addresses to reach the IP addresses of [Google APIs and services](https://developers.google.com/apis-explorer/). This scenario includes the case where your Google Distributed Cloud cluster nodes have only private IP addresses. You enable Private Google Access at the subnet level.

With Private Google Access, requests from your on-premises data center to Google services traverse your Cloud Interconnect or Cloud VPN connection instead of traversing the public internet.

Use Private Google Access in these situations:

  * Your on-premises VMs without public IP addresses must connect to Google services like BigQuery, Pub/Sub, or Container Registry.

  * You want to connect to Google services without traversing the public internet.




For a list of services that support Google Private Access from on-premises VMs, see [Supported services](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid#supported-services-onprem). For information about using Private Google Access from on-premises VMs, see [Configuring Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

#### Services that don't require Google Private Access

Sometimes, you don't need Private Google Access to reach a service from a VM that has only a private IP address. For example:

  * You create a Cloud SQL instance that has both a public IP address and a private IP address. Then your on-premises components can access the Cloud SQL instance using its private IP address. You don't need Private Google Access in this case, because you don't need to reach the public IP address of a Google service. This approach works only if Cloud Router advertises the private IP address of the Cloud SQL instance to your on-premises network.

  * You have an Google Distributed Cloud cluster in Google Cloud, and the cluster nodes have private IP addresses. Your on-premises components can access a NodePort Service or an internal load balancer Service in the cloud Google Distributed Cloud cluster.




### VPC Service Controls

If you want added protection against exfiltration, you can use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). With VPC Service Controls, you can configure security perimeters around the resources of your Google-managed services and control the movement of data across the perimeter boundary. For more information, see [Use VPC Service Controls with Cloud Interconnect or Cloud VPN](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/hardening-your-cluster#vpc-sc). 

### Connect

[Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview) enables you to view and manage your on-premises user clusters from Google Cloud console.

**Note:** Connect is not the fundamental connection between your on-premises data center and Google. Your fundamental connection is formed with [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview). To provide a view of your on-premises clusters from Google Cloud console, Connect runs on top of your fundamental connection.

## What's next

  * [Logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring)
  * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview)
  * [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
