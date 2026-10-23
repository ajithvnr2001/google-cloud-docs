---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology/
title: Key terms \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:18.777880+00:00
---

# Key terms  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Key terms Stay organized with collections  Save and categorize content based on your preferences. 

This page provides important terms that apply to Cloud Interconnect. Review these terms to better understand how Cloud Interconnect works.

For more information, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

## Cloud Interconnect terms

The following key terminology describes the concepts on which Cloud Interconnect is built. Each section indicates whether a term applies to Dedicated Interconnect, Partner Interconnect, Cross-Cloud Interconnect, Cross-Site Interconnect, or a combination thereof. 

### Cloud Interconnect elements

Interconnect connection
    

_Applies to Dedicated Interconnect, Cross-Cloud Interconnect, and Cross-Site Interconnect._

#### For Dedicated Interconnect and Cross-Site Interconnect

A specific physical connection between Google and your on-premises network. This connection exists in a colocation facility where your on-premises network and Google's network meet. 

A single connection can be a single link or a link bundle. If you have multiple connections to Google at different locations or to different devices, you must create separate Interconnect connections. For more information about connection capacities, see one of the following: 

  * Dedicated Interconnect: [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#port-capacity). 
  * Cross-Site Interconnect: [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#port-capacity). 



#### For Cross-Cloud Interconnect

A specific physical connection between Google and the network of another cloud service provider (the remote cloud service provider). This connection exists in a single colocation facility or in adjoining facilities, where the networks of Google and the remote cloud service provider meet. 

A single connection can be a single link, or a link bundle depending on what the remote cloud provider supports. For more information about capacity, see [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#port-capacity).

connection type
    The type of Cloud Interconnect connection falls into one of the following categories: 

  * Dedicated Interconnect 
  * Partner Interconnect
  * Cross-Cloud Interconnect
  * Partner Cross-Cloud Interconnect for OCI
  * Partner Cross-Cloud Interconnect for AWS
  * Cross-Site Interconnect


VLAN attachment
    

_Applies to Dedicated Interconnect, Partner Interconnect, Cross-Cloud Interconnect, partner Cross-Cloud Interconnect for OCI, and partner Cross-Cloud Interconnect for AWS._

A VLAN (virtual local area network) attachment is a logical connection between an external network and a single region in your Virtual Private Cloud (VPC) network. In the Compute Engine API, the VLAN attachment is known as an `interconnectAttachment` resource. 

When you create a VLAN attachment, you associate it with a project, a region, an existing or new Cloud Router, and an existing Cloud Interconnect connection. Then you configure a Border Gateway Protocol (BGP) session between the Cloud Router and your external router. 

  * For Dedicated Interconnect, the VLAN attachment uses a dedicated connection that you create to reach your on-premises router. 
  * For Partner Interconnect, the attachment uses a connection that your chosen partner sets up and manages. 
  * For Cross-Cloud Interconnect, the attachment uses a connection that Google creates on your behalf between the networks of Google Cloud and your remote cloud service provider. 



A VLAN attachment is not directly associated with a VPC network. However, it's indirectly tied to a single VPC network because a Cloud Router can be associated with only one network. Therefore, the VLAN attachment is tied to the network where the Cloud Router is located. 

To fully use the bandwidth of a given Cloud Interconnect connection, you might need to create multiple VLAN attachments. Creating VLAN attachments with a combined bandwidth greater than the Cloud Interconnect connection doesn't give you more than the stated bandwidth of the connection. For example, consider the following: 

  * To fully use the bandwidth of 2 x 10-Gbps Cloud Interconnect connections, you need a 20-Gbps VLAN attachment. 
  * To fully use the bandwidth of 5 x 10-Gbps Cloud Interconnect connections, you need a 50-Gbps VLAN attachment. 



#### For Dedicated Interconnect

A VLAN attachment for Dedicated Interconnect allocates a single 802.1Q VLAN on your Dedicated Interconnect connection and connects it to a specific VPC network. Because each connection for Dedicated Interconnect supports multiple VLAN attachments, you can access multiple VPC networks without creating multiple connections. 

Each attachment that you create is associated with a VPC network and a Google Cloud region: 

  * When you associate an attachment for Dedicated Interconnect with a VPC network, this network must be in a project in the same organization as the project that contains the Dedicated Interconnect connection. 
  * The set of valid regions for an attachment depends on the colocation facility used by the Cloud Interconnect. 



You can set the capacity of each attachment. For a list of capacities, see the [ Pricing](https://cloud.google.com/network-connectivity/pricing#dedicated-pricing-table) page. The default attachment capacity is 10 Gbps. 

The capacity setting limits the maximum bandwidth that an attachment can use. If you have multiple attachments on a single Dedicated Interconnect connection, the capacity limitation might be helpful in cases where you want to prevent network congestion on your connection. The maximum bandwidth is approximate, so it's possible for an attachment to use more bandwidth than the selected capacity. 

Because the capacity setting only limits the data transfer bandwidth from Google Cloud to the colocation facility for the Interconnect connection, we recommend that you configure a data transfer rate limiter on your router for your connection. Configuring this limiter enables you to cap the maximum inbound data transfer bandwidth to your VPC network for traffic using that connection. 

#### For Partner Interconnect

To request Partner Interconnect connectivity from a service provider, you create a VLAN attachment in your Google Cloud project. The VLAN attachment generates a unique pairing key that you share with your service provider. The service provider uses the pairing key, along with your requested connection location and capacity, to complete the configuration of your VLAN attachment. 

After your service provider configures the attachment, they allocate a specific 802.1q VLAN on your on-premises connection. 

#### For Cross-Cloud Interconnect

A VLAN attachment for Cross-Cloud Interconnect allocates a single 802.1Q VLAN on your Cross-Cloud Interconnect connection. The VLAN attachment and the associated Cloud Router link your connection to a specific VPC network. Because each Cross-Cloud Interconnect connection can support multiple VLAN attachments, you can access multiple VPC networks without creating multiple connections. 

The following requirements apply: 

  * When you associate a Cloud Router with your VLAN attachment, you associate the attachment with a VPC network. That network must be in the same project as the Cross-Cloud Interconnect connection. 
  * The set of valid regions for an attachment depends on the locations supported by Google Cloud and by your remote cloud service provider. 



You can select a capacity for each attachment. For a list of capacities, see the [Pricing](https://docs.cloud.google.com/network-connectivity/pricing) page. The default capacity is 10 Gbps. This setting affects the maximum bandwidth that the attachment can use. If you have multiple VLAN attachments, we recommend setting a capacity for each of them. Doing so can prevent any single attachment from using the entire bandwidth of the connection, which can cause packets to be dropped. The maximum bandwidth is approximate, so it's possible for an attachment to use more bandwidth than the selected capacity. 

The capacity setting limits only the outbound data transfer bandwidth from Google Cloud to the colocation facility for the Cross-Cloud Interconnect connection. For this reason, we recommend that you configure an outbound data transfer rate limiter on the virtual router in your remote cloud. Configuring this limiter enables you to cap the maximum inbound data transfer bandwidth to your VPC network for traffic using that connection. 

#### For partner Cross-Cloud Interconnect for OCI

A VLAN Attachment for partner Cross-Cloud Interconnect for OCI establishes cross-cloud connectivity with OCI on pre-built physical connectivity between Oracle and Google Cloud. You order a partner VLAN attachment in your project and input the `pairing key` when you get an Oracle Fast Connect virtual circuit, specifying requested capacity through Oracle's interface. This establishes BGP connectivity directly between your networks within the two clouds. 

Cloud Router
    

_Applies to Dedicated Interconnect, Partner Interconnect, and Cross-Cloud Interconnect._

Cloud Router uses Border Gateway Protocol (BGP) to dynamically exchange routes between your VPC network and your external network. Before you can create a VLAN attachment, you must create or select an existing Cloud Router in the VPC network that you want to connect to. You then use the Cloud Router to configure a BGP session with your external router. 

For detailed information about Cloud Router, see the [ Cloud Router overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview). 

The BGP configuration of the Cloud Router depends on whether you're using Layer 2 or Layer 3 connectivity. Dedicated Interconnect and Cross-Cloud Interconnect use only Layer 2 connectivity. Partner Interconnect can use Layer 2 or Layer 3 connectivity. 

  * For Layer 2, you establish a BGP session between your Cloud Router and your external router. 
  * For Layer 3, your service provider establishes a BGP session between your Cloud Router and their edge router. For more information, see [ Layer 2 versus Layer 3 connectivity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#connectivity-type). 



Cloud Router advertises subnets in its VPC network and propagates learned routes to those subnets. Unless you configure [ custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip), Cloud Router advertises the following routes: 

  * If your VPC network uses _regional dynamic routing mode_ , Cloud Router advertises [subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) in the region where it's located. 
  * If your VPC network uses _global dynamic routing mode_ , Cloud Router advertises subnet routes in all regions. 



Cloud Router also creates dynamic routes in your VPC network for destinations that it learns from your external router. If your VPC network uses regional dynamic routing mode, Cloud Router makes those routes available to only the region where it's located. If your network uses global dynamic routing mode, Cloud Router makes those routes available to all regions. 

on-premises router
    

_Applies to Dedicated Interconnect, Partner Interconnect, and Cross-Site Interconnect._

The on-premises router is an external router that establishes a BGP session with Cloud Router, or an Ethernet session with another on-premises router. This connection lets you exchange data between your on-premises network and your VPC network, or between your on-premises networks. 

For Dedicated Interconnect and Cross-Site Interconnect, you manage the on-premises router, which is often physically located in the colocation facility where your connection is provisioned. However, the device can be physically located in another facility, such as an office location where you manage networking equipment. You establish the BGP sessions between your on-premises router and Cloud Router, or Ethernet sessions between your on-premises routers. 

For Partner Interconnect, an on-premises router is a device that either you or the service provider uses to configure BGP sessions with Cloud Router. 

  * With Layer 2 Partner Interconnect connections, you configure the BGP session between your on-premises router and Cloud Router. 
  * With Layer 3 Partner Interconnect connections, your service provider manages the BGP session between their on-premises router and Cloud Router. 



For more information about different Partner Interconnect connections, see [ Layer 2 versus Layer 3 connectivity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#connectivity-type). 

For information about configuring on-premises routers, see the following documents: 

  * [ Configure on-premises routers (Dedicated Interconnect)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers)
  * [ Configure on-premises routers (Partner Interconnect)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers)
  * [ Configure on-premises routers (Cross-Site Interconnect)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/configure-onprem-routers)


external router
    

_Applies to Dedicated Interconnect, Partner Interconnect, Cross-Cloud Interconnect, and Cross-Site Interconnect._

An external router is a networking device that provides access to the network that you want to peer with. The external router can be one of the following: 

  * An on-premises router
  * A virtual router hosted by your  remote cloud service provider



### Cloud Interconnect locations

connection location or colocation facility
    

_Applies to Dedicated Interconnect and Cross-Site Interconnect, with notes for Partner Interconnect and Cross-Cloud Interconnect._

The colocation facility where a physical Cloud Interconnect connection is provisioned. This location is where your on-premises routing equipment meets Google's peering edge. 

A colocation facility is where Google has a point of presence (PoP), enabling you to connect your on-premises network with Google's network. In the colocation facility, you work with the facility provider to provision your routing equipment before using Dedicated Interconnect. 

For connections to Google Cloud through VLAN attachments, each connection location supports a subset of Google Cloud regions. For example, `lga-zone1-16` supports VLAN attachments in the regions `northamerica-northeast1`, `northamerica-northeast2`, `us-central1`, `us-east1`, `us-east4`, `us-east5`, `us-south1`, `us-west1`, `us-west2`, `us-west3`, and `us-west4`. 

For a list of all locations and their supported regions, see [ All colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities). 

For a list of locations that you can use to connect your sites to each other, see [ Colocation facilties for Cross-Site Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-locations). 

**Note:** 100-Gbps circuits are not available in all Cloud Interconnect locations. To find out if a location is supported, contact your sales representative. 

When using Partner Interconnect, partners have already set up connections to Google's network. The set of locations varies, depending on which partner you choose. When you set up your VLAN attachment, you can select from the partner's available locations. For a list of locations that each service provider supports, see the [ service providers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers#by-provider) page. 

When using Cross-Cloud Interconnect, you must choose a location that your remote cloud service provider supports: 

  * [ Locations for Amazon Web Services](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/choose-locations#list-of-supported-locations)
  * [ Locations for Microsoft Azure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/choose-locations#list-of-supported-locations)
  * [ Locations for Oracle Cloud Infrastructure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/choose-locations#list-of-supported-locations)
  * [ Locations for Alibaba Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations#list-of-supported-locations)



Each partner location supports a subset of Google Cloud regions. These supported regions are where you can connect to your Cloud Routers and associated VLAN attachments. For example, if you choose the `Ashburn` location, you can reach all the North American regions, such as `us-east1` and `us-west1`. For a list of Google Cloud regions, see the [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones) page. 

service provider
    

_Applies to Partner Interconnect._

A network service provider for Partner Interconnect. To use Partner Interconnect, you must connect to a supported [ service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers). The service provider provides connectivity between your on-premises network and your VPC network. 

metropolitan area (metro)
    

_Applies to Dedicated Interconnect, Partner Interconnect, Cross-Cloud Interconnect, and Cross-Site Interconnect._

The city where a colocation facility is located. 

The metro that you choose depends on the location of your on-premises network and the location of your Compute Engine VM instances (their Google Cloud region) if you are connecting to Google Cloud. Typically, you might want to pick a metro that's geographically close to your on-premises network to reduce latency. When configuring a redundant connection, you might choose an additional metro that is further away. 

For VLAN attachments, each metro supports a subset of Google Cloud regions. You can create VLAN attachments only in these supported regions. For example, if you pick a facility in `Ashburn`, you can only create VLAN attachments in the North American regions. Assuming that your VM instances are also located in these regions, you can create VLAN attachments in the same regions as your VMs to reduce latency and outbound data transfer costs. Otherwise, traffic would have to travel between regions to reach your VM instances or on-premises network. 

For more information for Dedicated Interconnect, see [ All colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities). 

For more information for Cross-Site Interconnect, see [ Colocation facilties for Cross-Site Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-locations). 

metro availability zone
    

_Applies to Dedicated Interconnect, Partner Interconnect, Cross-Cloud Interconnect, and Cross-Site Interconnect._

An older term for edge availability domain.

edge availability domain
    

_Applies to Dedicated Interconnect, Partner Interconnect, Cross-Cloud Interconnect, and Cross-Site Interconnect._

Each metropolitan area has two independent maintenance domains called _edge availability domains_. The two edge availability domains are named `zone1` and `zone2`. These domains provide isolation during scheduled maintenance, which means that two domains in the same metro are not down for maintenance at the same time. This isolation is important when you're building for redundancy. 

Edge availability domains span a whole metro, and do not cross metros. To maintain availability and an [SLA](https://cloud.google.com/network-connectivity/sla), you must build duplicate Cloud Interconnect connections by picking two connection locations in the same metro that are in different edge availability domains. Some metros offer more than two locations, but there are still only two edge availability domains in the metro. For example, building connections in locations `dfw-zone1-4` and `dfw-zone1-505` does not provide redundancy because both locations are in the `zone1` edge availability domain. Building them in `dfw-zone1-4` and `dfw-zone2-4` provides redundancy because the locations are in different edge availability domains. 

Maintenance windows are not coordinated across metros. For example, the edge availability domains `dfw-zone1-4` and `ord-zone1-7` could experience overlapping maintenance events. When connecting to multiple metros for redundancy, it is important to connect to different edge availability domains in each of those metros, as described in the [ production topology](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview). 

### Provisioning and configuration

Letter of Authorization and Connecting Facility Assignment (LOA-CFA)
    

_Applies to Dedicated Interconnect and Cross-Site Interconnect._

An [ LOA-CFA](https://en.everybodywiki.com/LOA-CFA) identifies the connection ports that Google has assigned for your Cloud Interconnect connection, and grants permission for a vendor in a colocation facility to connect to them. LOA-CFA documents are required when you order Dedicated Interconnect connections in a colocation facility. 

When you order Cloud Interconnect connections, Google allocates resources for your connections and then generates an LOA-CFA document for each one. The LOA-CFA lists the demarcation points that Google allocated for your connections. Submit this form to the facility vendor to provision connections between Google's equipment and your own. After the status of a connection changes to `PROVISIONED`, the LOA-CFA is no longer valid, necessary, or available in the Google Cloud console. 

For more information about the provisioning flow, see [ Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview) or [Cross-Site Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/provisioning-overview). 

pairing key
    

_Applies to Partner Interconnect._

A unique identifier that lets service providers identify particular VLAN attachments without anyone sharing potentially sensitive information about their VPC network or Google Cloud project. Pairing keys are used only for Partner Interconnect. 

Treat the pairing key as sensitive information until your VLAN attachment is configured. If it's discovered, it's possible for other parties to use it to connect to your network. The key is for one-time use and can't be modified. If you need a new pairing key, delete your VLAN attachment and create a new one. 

Pairing keys use the following format:  
`<random>/<vlan-attachment-region>/<edge-availability-domain>`. 

For example, `7e51371e-72a3-40b5-b844-2e3efefaee59/us-central1/2` is a pairing key for a VLAN attachment in the `us-central1` region and edge availability domain `2`. 

remote cloud service provider
    

_Applies to Cross-Cloud Interconnect._

Another cloud service provider, in addition to Google Cloud, where you might have networking resources. 

## Border Gateway Protocol (BGP) terms

The following terminology applies to the [Border Gateway Protocol (BGP)](https://wikipedia.org/wiki/Border_Gateway_Protocol), which Cloud VPN and Cloud Interconnect use for dynamic routing.

Border Gateway Protocol (BGP)
    An exterior gateway routing protocol standardized by the Internet Engineering Task Force (IETF) in [RFC 1722](https://tools.ietf.org/html/rfc1772). BGP automatically exchanges routing and reachability information among autonomous systems on the internet. Your device is BGP-capable if it can perform BGP routing, which means that you can enable the BGP protocol on it and assign it a BGP IP address and an autonomous system number. To determine if your device supports BGP, see the vendor information for your device or contact your device's vendor.
[autonomous system (AS)](https://wikipedia.org/wiki/Autonomous_system_\(Internet\))
    A collection of connected IP routing prefixes under the control of a single administrative entity or domain that presents a common routing policy to the internet, such as an internet service provider (ISP), a large company, or a university.
autonomous system number (ASN)
    A unique identifier allocated to each autonomous system that uses BGP routing. For more information, see [RFC 7300](https://tools.ietf.org/html/rfc7300).
MD5 authentication
    A method of BGP peer authentication that uses the MD5 message-digest algorithm. When you use this approach, BGP peers must use the same authentication key, or a connection cannot be established between them. Later, every segment routed between the peers is verified. For more information about MD5 authentication, see [RFC 2385](https://datatracker.ietf.org/doc/html/rfc2385). To find out whether your device supports MD5 authentication, see the vendor information for the device or contact the vendor. To get support with using Cloud Router MD5 authentication, see [Support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support).

## Google Cloud terms

The following terminology applies to Google Cloud and its features.

Google Cloud
    Google Cloud is a suite of public cloud computing services offered by Google. For more information, see [Google Cloud products](https://cloud.google.com/products/).
project ID
    The ID of your Google Cloud project. A project contains networking resources such as networks, subnets, and Cloud VPN gateways as described in the [VPC network overview](https://docs.cloud.google.com/vpc/docs/vpc#specifications). For a description of the difference between _project name_ , _project ID_ , and _project number_ , see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). You can view the project ID in the [Google Cloud console](https://console.cloud.google.com/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
