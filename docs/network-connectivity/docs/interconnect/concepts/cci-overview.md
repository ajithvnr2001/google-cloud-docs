---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview/
title: Cross-Cloud Interconnect overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:56.685933+00:00
---

# Cross-Cloud Interconnect overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Cross-Cloud Interconnect overview Stay organized with collections  Save and categorize content based on your preferences. 

Provisioning Cross-Cloud Interconnect requires that Google creates a dedicated physical connection between the Google network and that of another service provider. Alternatively, you can connect to AWS and OCI by using partner Cross-Cloud Interconnect, which connects your network in another cloud and your VPC networks through a supported service provider. For more information, see the following pages: 

  * [Partner Cross-Cloud Interconnect for AWS overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview)
  * [Partner Cross-Cloud Interconnect for OCI overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-oci-overview)



Cross-Cloud Interconnect is a product that helps you establish high-bandwidth dedicated connectivity between Google Cloud and another cloud service provider.

When you buy Cross-Cloud Interconnect, Google provisions a dedicated physical connection between the Google network and that of another cloud service provider. You can use this connection to peer your Google Virtual Private Cloud (VPC) network with your network that's hosted by a supported cloud service provider.

[ ![Cross-Cloud Interconnect configuration.](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/99.9.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/99.9.svg) Cross-Cloud Interconnect configuration (click to enlarge).

Google supports the connection up to the point where it reaches the network of your other cloud service provider. Google does not guarantee uptime from the other cloud service provider and cannot create a support ticket on your behalf. With your permission [Cloud Customer Care](https://docs.cloud.google.com/support) can communicate directly with your other cloud provider's support team to expedite issue resolution. However, you must have a support ticket open with the other provider.

Cross-Cloud Interconnect helps you avoid some of the common pain points associated with multicloud configuration, as described in the following section.

## Benefits

This section describes the benefits of multicloud in general and of Cross-Cloud Interconnect in particular.

### Integrated multicloud strategy

Cross-Cloud Interconnect supports your adoption of an integrated multicloud strategy. Adopting a multicloud architecture lets you do the following:

  * Avoid being locked in with a single vendor.

  * Store data in one cloud while hosting business logic in another.

  * Avoid downtime if one cloud has an outage.

  * Use a second cloud for disaster recovery.

  * Maximize business insights by analyzing data in multiple clouds.




### Reduced complexity

Without Cross-Cloud Interconnect, the options for setting up connectivity are limited, and all are relatively complex.

One option is to deploy your own router in a colocation facility and then connect it to the networks of your cloud service providers. In general, this approach can be expensive and time consuming.

Another option is to contract with a third party to establish connectivity. However, it can be a hassle to select a vendor, or potentially multiple vendors, and then negotiate one or more contracts. When you use this approach, you also have to invest time learning about the systems that are specific to your vendors.

When you use Cross-Cloud Interconnect, you don't have to deploy your own hardware, and you eliminate the need to work with third parties.

### Site-to-site data transfer

You can use Cross-Cloud Interconnect as part of a site-to-site data transfer strategy. [Site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer) is a feature of Network Connectivity Center (NCC) that lets you use the Google network as a wide area network (WAN).

With this feature, you connect your external networks to Google Cloud by using [supported connectivity resources](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#supported-spoke-resources). You then associate each connectivity resource with a NCC spoke and enable the spokes for site-to-site data transfer. At that point, you can conduct data transfer between the sites.

You can use this feature to do the following:

  * **Connect your cloud networks:** Suppose you have a network hosted by Microsoft Azure and another hosted by Amazon Web Services (AWS). In this scenario, you can establish one pair of Cross-Cloud Interconnect connections to reach the Azure network and another to reach the AWS network. After configuring NCC spokes, you can use the Google network to transfer data between your Azure and AWS networks.

  * **Connect an on-premises network to other clouds:** Suppose you have the setup that's described in the preceding bullet point, but you also have offices in New York and Sydney. In this scenario, you can establish connectivity to your offices by using resources such as Dedicated Interconnect VLAN attachments or Cloud VPN (HA VPN) tunnels. After creating spokes, you can use the Google network to transfer data between either of your offices and your Azure and AWS networks.




Site-to-site data transfer is supported only in certain [locations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).

## Compare Cross-Cloud Interconnect to partner Cross-Cloud Interconnect

Use the information in the following sections to help decide whether Cross-Cloud Interconnect or partner Cross-Cloud Interconnect are the best fit for your application.

### Comparison to partner Cross-Cloud Interconnect for OCI

While Cross-Cloud Interconnect lets you turn up dedicated connectivity between Google Cloud and OCI, partner [Cross-Cloud Interconnect for OCI](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-oci-overview) lets you connect any Google Cloud and OCI resources privately in [available paired locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/paired-locations). Use the following table to choose the option that works best for your needs:

Feature | Cross-Cloud Interconnect | Partner Cross-Cloud Interconnect for OCI  
---|---|---  
**Tenancy** |  Connections are fully owned by you and can't be shared across organizations.  |  Google Cloud and OCI own ports; connections can be used by multiple customers.   
**Supported speeds** |  10 Gbps, 100 Gbps, 400 Gbps.  |  1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, 20 Gbps, 50 Gbps.   
**Cost** |  You pay for ports and attachments in both clouds and data transfer out for traffic leaving Google Cloud.  |  You pay for Google Cloud partner attachments and OCI virtual circuits. There is no data transfer fee.   
**Performance** |  Optimal latency.  |  Optimal latency.   
**Support** |  Google supports the connection all the way to the OCI demarcation.  |  Google Cloud and OCI partner on supporting the solution end to end.   
  
### Comparison to partner Cross-Cloud Interconnect for AWS

While Cross-Cloud Interconnect lets you turn up dedicated connectivity between Google Cloud and AWS, [partner Cross-Cloud Interconnect for AWS](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview) lets you connect any Google Cloud and AWS resources privately in [available paired locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/paired-locations). Use the following table to choose the option that works best for your needs:

Interconnect connection type | Cross-Cloud Interconnect | Partner Cross-Cloud Interconnect for AWS  
---|---|---  
**Description** | Provides dedicated connectivity between Google Cloud and providers like OCI, AWS, Azure, and Alibaba | Provides dedicated connectivity between Google Cloud and providers like AWS  
**Needs physical provisioning** | Yes | No  
**Needs physical attachments and ports** | Yes | No  
**Connection increments** | 10 Gbps or 100 Gbps | Granular pre approved speeds starting from 1 Gbps to 100 Gbps  
**Provisioning time** | 1-4 weeks | Minutes  
**Connection ordering** | Must be initiated from Google Cloud | Bidirectional; can be initiated from Google Cloud or Amazon Web Services  
**Resiliency** | Must be configured manually | Built into the product  
  
## Encryption

Cross-Cloud Interconnect supports MACsec for Cloud Interconnect encryption for additional security. You can use MACsec for Cloud Interconnect to help secure traffic in your Cross-Cloud Interconnect connections. For more information, see [MACsec for Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).

## Supported cloud service providers

Google supports the following cloud service providers for use with Cross-Cloud Interconnect:

  * Amazon Web Services (AWS)

  * Microsoft Azure

  * Oracle Cloud Infrastructure (OCI)

  * Alibaba Cloud




Cross-Cloud Interconnect and this documentation refer to such cloud service providers as your _remote cloud service provider_ or _remote cloud_.

## Google support for Cross-Cloud Interconnect

The following diagram shows the point of physical cabling that Google support is responsible for. For any other issues, contact the other cloud service provider that you are using.

[ ![Cross-Cloud Interconnect physical cabling support.](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/cci-support.png)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/cci-support.png) Cross-Cloud Interconnect physical cabling support (click to enlarge).

## Port capacity

Cross-Cloud Interconnect connections are available in the following sizes: Provider | Size  
---|---  
Amazon Web Services (AWS), Oracle Cloud Infrastructure (OCI) | 10 Gbps, 100 Gbps, and 400 Gbps  
Microsoft Azure, Alibaba Cloud | 10 Gbps, 100 Gbps  
  
## Cross-Cloud Interconnect MTU

Cross-Cloud Interconnect lets you configure jumbo [maximum transmission units (MTUs)](https://docs.cloud.google.com/vpc/docs/mtu) with any of the cloud providers. For information about support for larger MTUs, refer to the remote cloud provider's documentation as they may not be the same as Google's.

## Setup process

To start the setup process, you identify supported locations where you want Google to place your connections. Then you purchase primary and redundant Cross-Cloud Interconnect ports. You also buy primary and redundant ports from your remote cloud service provider.

Following your purchase from your remote cloud service provider, they provide you with documentation that authorizes you to connect to their router. You send this documentation to Google. At that point, Google can provision your connections. For each connection, Google physically connects one of your Cross-Cloud Interconnect ports to one of your remote cloud ports.

After Google provisions your connection, we notify you that the connection is ready to use. To begin using the connection, you configure your Google Cloud resources and your remote cloud resources.

For a more detailed overview, see one of the following:

  * [Connect to Amazon Web Services](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/connectivity-overview)

  * [Connect to Azure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/connectivity-overview)

  * [Connect to Oracle Cloud Infrastructure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/connectivity-overview)

  * [Connect to Alibaba Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/connectivity-overview)




### Fixed pricing

Cross-Cloud Interconnect offers fixed port pricing for outbound data transfers for VLAN attachments. You can choose fixed pricing for each Cross-Cloud Interconnect connection and choose which types of connections you want the fixed pricing to apply to. This lets you get a fixed monthly invoice for outbound data transfers.

Fixed port pricing considers the following types of connections:

  * **Local connection** : The VLAN attachment is in the same a metro location where the destination Google Cloud [region](https://docs.cloud.google.com/docs/geography-and-regions) is located.

For example, if you obtain a VLAN attachment in the Los Angeles, California metro location and the destination Google Cloud region is `us-west2`, then the VLAN attachment's location and destination Google Cloud region are the same. This is considered a local connection.

  * **Remote connection** : The VLAN attachment is in a different metro location where the destination Google Cloud region is located.

For example, if you create a VLAN attachment in the Los Angeles, California metro location and the destination Google Cloud region is `us-east4`, then the VLAN attachment's location and destination Google Cloud region are different. This is considered a remote connection.

Similarly, if you obtain a VLAN attachment in the Portland, Oregon metro location, then there isn't a local Google Cloud region available within that metro location. Because you can't connect to a local Google Cloud region, this is considered a remote connection.




The following Google Cloud regions only offer support for fixed pricing for remote connections on Cross-Cloud Interconnect:

  * us-west1
  * us-east1
  * europe-west4
  * europe-north1
  * asia-east1



To request a Cross-Cloud Interconnect connection with fixed port pricing, contact your account team.

## Custom IP address ranges

When you create a VLAN attachment for Cross-Cloud Interconnect, you can configure custom IP address ranges for the Cloud Router and customer router ends of the attachment. For information about how it works, including limitations and best practices, see the [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip) section in the Cloud Interconnect overview.

When you configure custom IP address ranges for VLAN attachments that you use with Cross-Cloud Interconnect and AWS, you must provide the IPv6 subnet that was allocated by AWS during attachment provisioning. When you configure custom IP address ranges for VLAN attachments with other cloud service providers, you can use your own IP addresses or use IP addresses that your service provider configures. To configure custom IP address ranges with Cross-Cloud Interconnect, see the following pages:

  * Alibaba Cloud: [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources#custom-ip)
  * Amazon Web Services (AWS): [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#custom-ip)
  * Microsoft Azure: [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources#custom-ip)
  * Oracle Cloud Infrastructure: [configure custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-google-resources#custom-ip)



## Service-level agreement

Cross-Cloud Interconnect uses the Cloud Interconnect service level agreement ([SLA](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#service-level-agreement)). Since Cross-Cloud Interconnect is a shared responsibility model between Google Cloud and another cloud service provider, the Cross-Cloud Interconnect SLA covers Google Cloud's infrastructure up until the point it's transferred to the other cloud service provider.

To qualify for the SLA, your Cross-Cloud Interconnect configuration must use one of the approaches described in the following sections.

Both of these approaches require redundancy. You incorporate redundancy by, at a minimum, locating connections in two edge availability domains. An _edge availability domain_ is a zone within a metropolitan area. Using multiple edge availability domains maximizes availability because two domains in the same metropolitan area are typically not down for maintenance at the same time.

### Production critical

To achieve 99.99% availability, you can use either a multi-region or a single-region topology.

#### Multi-region

For more critical applications, configure two pairs of connections. Each pair must be located in a different metropolitan area. Within each metropolitan area, you must use two different edge availability domains. This approach gives you 99.99% availability.

[ ![Figure 2. Set up Cross-Cloud Interconnect with 99.99% availability.](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/99.99.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/99.99.svg) **Figure 2.** Cross-Cloud Interconnect configuration that has 99.99% availability (click to enlarge).

#### Single-region

For workloads that require 99.99% availability within a single region, you can use the single-region topology. This configuration requires both Cloud Routers to be in the same region, connected to VLAN attachments in different edge availability domains.

For more information about supported locations for each cloud provider, see the following documents:

  * [Supported locations for AWS](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/choose-locations#supported-locations)

  * [Supported locations for Azure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/choose-locations#supported-locations)

  * [Supported locations for OCI](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/choose-locations#supported-locations)

  * [Supported locations for Alibaba Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations#supported-locations)




### Production non-critical

The Cloud Interconnect SLA requires you to have, minimally, two connections: a primary connection and a redundant connection, each in a different edge availability domain of a metropolitan area. This approach gives you 99.9% availability.

[ ![Figure 1. Set up Cross-Cloud Interconnect with 99.9% availability.](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/99.9.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/99.9.svg) **Figure 1.** Cross-Cloud Interconnect configuration that has 99.9% availability (click to enlarge).

## Limitations

Cross-Cloud Interconnect connections are supported only in certain locations. For details, see the following documents:

  * [Supported locations for AWS](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/choose-locations#supported-locations)

  * [Supported locations for Azure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/choose-locations#supported-locations)

  * [Supported locations for OCI](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/choose-locations#supported-locations)

  * [Supported locations for Alibaba Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations#supported-locations)




## What's next

  * [Connect to Amazon Web Services](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/connectivity-overview)

  * [Connect to Azure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/connectivity-overview)

  * [Connect to Oracle Cloud Infrastructure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/connectivity-overview)

  * [Connect to Alibaba Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/connectivity-overview)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
