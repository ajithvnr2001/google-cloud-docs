---
url: https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints/
title: Firewall endpoint overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:37.649695+00:00
---

# Firewall endpoint overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Firewall endpoint overview Stay organized with collections  Save and categorize content based on your preferences. 

A firewall endpoint is a Cloud Next Generation Firewall (Cloud NGFW) resource that enables Layer 7 advanced protection capabilities, such as the [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention), [Advanced malware sandbox (WildFire)](https://docs.cloud.google.com/firewall/docs/about-wildfire) ([Preview](https://cloud.google.com/products#product-launch-stages)), and [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering) in your network.

This page provides a detailed overview of firewall endpoints and their capabilities.

## Specifications

This section provides a summary of firewall endpoint properties. For detailed implementation requirements and capabilities, see the corresponding sections on this page.

  * A firewall endpoint is a zonal resource that you can configure at the organization level or the project level.

    * **Organization-level firewall endpoint** : organization administrators create and manage these endpoints to centralize security across your organization or at the folder level.

    * **Project-level firewall endpoints** : project administrators create and manage these endpoints within a project. You can associate any VPC network in the organization with a project-level endpoint. Create project-level firewall endpoints if you can't obtain organization-level permissions to create organization-level firewall endpoints.

  * Firewall endpoints perform Layer 7 firewall inspection on the intercepted traffic. For more information, see How firewall endpoints work.

  * The endpoint and the workloads for which you want to enable Layer 7 inspection must be in the same zone. For more information, see Deployment considerations.

  * You can create a firewall endpoint in a zone and attach it to one or more VPC networks to monitor workloads in the same zone. If your VPC network spans multiple zones, you can attach one firewall endpoint in each zone. If you don't attach a firewall endpoint to a VPC network in a specific zone, no Layer 7 inspection is performed on the workload traffic for that zone.

You use [firewall endpoint association](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoint-associations#create-endpoint-association) to attach a firewall endpoint to a VPC network.

  * The endpoint and the workloads for which you want to enable Layer 7 inspection must be in the same zone. For more information, see Deployment considerations.

  * Firewall endpoints can process up to 2 Gbps of traffic with Transport Layer Security (TLS) inspection, and 10 Gbps of traffic without TLS inspection. Excessive traffic can overload the endpoint and cause packet losses. To monitor the firewall endpoint's capacity utilization, see [`firewall_endpoint` network security metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-networksecurity).

**Note:** To avoid endpoint overloading due to excessive traffic, gradually scale up the endpoint while monitoring its capacity utilization.
  * When a firewall endpoint inspects traffic targeting a cross-region internal Application Load Balancer ([Preview](https://cloud.google.com/products#product-launch-stages)), the maximum throughput is 1.6 Gbps.

  * Because the endpoint does not forward unapproved messages, an overloaded endpoint might drop legitimate traffic if it cannot inspect the traffic.

  * Firewall endpoints can have a per-connection throughput maximum of 250 Mbps of traffic with TLS inspection and 1.25 Gbps of traffic without TLS inspection.

  * You can create a firewall endpoint that processes jumbo frames up to 8,588 bytes in size. Alternatively, you can create an endpoint without jumbo frame support. For more information, see Supported packet size.

  * You can delete a firewall endpoint only when there are no VPC networks associated with it. For more information, see Firewall endpoint associations.




## How firewall endpoints work

Cloud NGFW uses Google Cloud's packet intercept technology to redirect traffic from the Google Cloud workloads in a Virtual Private Cloud (VPC) network to the firewall endpoints. Packet intercept is a Google Cloud capability that inserts network appliances in the path of selected network traffic without modifying the existing routing policies of the traffic.

Cloud NGFW redirects the workload traffic in a VPC network to the firewall endpoint only if you configure Layer 7 inspection for this flow. Cloud NGFW then adds a VPC network identifier to each packet redirected to the firewall endpoint for Layer 7 inspection. If you have multiple VPC networks with overlapping IP address ranges, this network identifier helps ensure that each redirected packet is correctly associated with its VPC network.

## Capacity and performance

Firewall endpoints can have a per-connection throughput maximum of 250 Mbps of traffic with TLS inspection and 1.25 Gbps of traffic without TLS inspection. Excessive traffic can overload the endpoint and cause packet losses. Because the endpoint does not forward unapproved messages, an overloaded endpoint might drop legitimate traffic if it cannot inspect the traffic.

To monitor the capacity utilization of a firewall endpoint, see [`firewall_endpoint` network security metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-networksecurity).

**Caution:** To avoid endpoint overloading due to excessive traffic, gradually scale up the endpoint while monitoring its capacity utilization.

## Supported packet size

A firewall endpoint either supports or doesn't support jumbo frames.

  * A firewall endpoint with jumbo frame support can accept packets up to 8,588 bytes.

Cloud NGFW reserves an additional 308 bytes for [GENEVE encapsulation](https://docs.cloud.google.com/network-security-integration/docs/understand-geneve) (needed for data inspection) and for other extensions. Therefore, the total packet size of 8,896 bytes matches the highest possible maximum transmission unit (MTU) that Google Cloud supports.

  * A firewall endpoint without jumbo frame support can accept packets up to 1,460 bytes.

To perform Layer 7 inspection successfully, [configure the VPC networks](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network) associated with the endpoint to follow these MTU limits:

    * For an endpoint with jumbo frame support, make sure the VPC networks use an MTU of 8,588 bytes or less.

    * For an endpoint without jumbo frame support, make sure the VPC networks use an MTU of 1,460 bytes or less.




**Caution:** A firewall endpoint doesn't perform URL filtering service, Advanced malware sandbox, or intrusion detection and prevention service for a VPC network if the network is configured with an MTU that's greater than the firewall endpoint's limit.

You can create a firewall endpoint with or without jumbo frame support. However, you cannot reconfigure an existing endpoint to either add or remove jumbo frame support. To add or remove jumbo frame support, delete the endpoint and recreate it. For more information, see [Create a firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#create-firewall-endpoint).

## Deployment considerations

You use [firewall endpoint association](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#create-endpoint-association) to attach a firewall endpoint to a VPC network. To monitor workloads, you can create a firewall endpoint in a zone and attach it to one or more VPC networks in the same zone. If your VPC network spans multiple zones, you can attach one firewall endpoint in each zone.

Creating the firewall endpoint in the same zone as workloads provides the following benefits:

  * Lower latency. Because firewall endpoints can intercept, inspect, and reinject the traffic back into the network, latency is lower than that of firewall endpoints in different zones.
  * No cross-zonal traffic. Keeping traffic within the same zone ensures lower costs.
  * More reliable traffic. Keeping traffic within the same zone removes the risk of cross-zonal outages.



If you don't attach a firewall endpoint to a VPC network in a specific zone, Cloud NGFW does not perform Layer 7 inspection on the workload traffic for that zone.

## Infrastructure and reliability

When you create a firewall endpoint, Google provides a set of dedicated virtual machine (VM) instances. This architecture ensures reliability, performance, and security isolation for your traffic, along with certificate management.

Google provides high availability by using proper failover mechanisms for the firewall endpoints. These mechanisms ensure reliable firewall protection for all VM instances in the associated VPC network.

## Firewall endpoint associations

Firewall endpoint association links a firewall endpoint to a VPC network in the same zone. After you define this association, Cloud NGFW forwards the zonal workload traffic in your VPC network that requires Layer 7 inspection to the attached firewall endpoint.

You can associate a VPC network with an organization-level or a project-level firewall endpoint. To associate a VPC network, consider the following:

  * **Cross-project association** : if the endpoint and VPC network are in different projects, both projects must belong to the same organization.

  * **Zonal limit** : associate a VPC network with only one firewall endpoint per zone. This limit includes both organization-level and project-level endpoints.




## Traffic interception by project-level firewall endpoints

To intercept and inspect traffic by using a project-level firewall endpoint, ensure that the following requirements are met:

  * A VPC network in the VM instance's zone is associated with the target firewall endpoint.
  * The traffic matches a firewall policy rule with the `apply_security_profile_group` action.
  * The security profile group exists in the same project as the firewall endpoint.

**Warning:** If the firewall endpoint and the security profile group exist in different projects, then Cloud NGFW might still intercept the traffic. However, because the firewall endpoint is not associated with that security profile group, Cloud NGFW applies a default profile to the intercepted traffic.

## Firewall endpoint for Advanced malware sandbox

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can create a firewall endpoint with Advanced malware sandbox enabled to extend your network protection beyond basic signature matching. While the intrusion detection and prevention service can only block malware with known signatures, Advanced malware sandbox adds near real-time updates to recognize and block novel, file-based threats.

When you enable Advanced malware sandbox while creating or editing a firewall endpoint, you can configure additional settings under the **Advanced configuration** section. These additional configurations include the following:

  * **Region** : specifies the geographical region where the firewall endpoint submits unknown or suspicious files for threat analysis. If you don't specify a region, the endpoint automatically defaults to the nearest available regional Advanced malware sandbox cloud based on its location to minimize latency.

  * **Content cloud region** : specifies the content cloud region that the endpoint will use. This defaults to the nearest available region.

  * **Signature lookup timeout** : the maximum amount of time (in milliseconds) the firewall holds a file while the Advanced malware sandbox cloud performs a real-time signature lookup.

  * **Signature lookup timeout action** : defines the firewall's response if the real-time signature lookup exceeds the configured timeout threshold. You can choose to `Allow` or `Deny` the file. The default action is `Allow`.

  * **Block HTTP partial responses** : lets you block the resuming of blocked malicious HTTP file downloads. Selecting this option provides maximum security.

  * **Inline cloud analysis max duration** : the maximum timeout (in seconds or milliseconds, depending on the interface) the firewall holds a file while the inline cloud analysis evaluates it.

  * **Inline cloud analysis timeout action** : defines the action to take if the inline cloud analysis process times out. You can configure this to `Allow` or `Deny` the file transfer. The default action is `Allow`.

  * **Enable submission timeout logging** : lets you enable log generation for files that time out during inline cloud analysis.




To learn about Advanced malware sandbox, see [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire).

To create a firewall endpoint with Advanced malware sandbox, see [Create firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints).

## IAM roles

Identity and Access Management (IAM) roles govern the following firewall endpoint actions:

  * Creating a firewall endpoint in an organization or a project
  * Modifying or deleting a firewall endpoint in an organization or a project
  * Viewing details of a firewall endpoint in an organization or a project
  * Viewing all the firewall endpoints configured in an organization or a project



The following table describes the roles that are necessary for each step.

Ability | Necessary role  
---|---  
Create a firewall endpoint | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 

  
Modify a firewall endpoint | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 

  
Delete a firewall endpoint | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 

  
View details about the firewall endpoint | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)

  
View all the firewall endpoints | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)

  
  
IAM roles govern the following firewall endpoint association actions:

  * Creating a firewall endpoint association in a project
  * Modifying or deleting a firewall endpoint association
  * Viewing details of a firewall endpoint association
  * Viewing all the firewall endpoint associations configured in a project



The following table describes the roles that are necessary for each step.

Ability | Necessary role  
---|---  
Create a firewall endpoint association | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoint associations, and at either the project level or the organization level for project-level firewall endpoint associations 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)

  
Modify a firewall endpoint association | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoint associations, and at either the project level or the organization level for project-level firewall endpoint associations 

  
Delete a firewall endpoint association | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoint associations, and at either the project level or the organization level for project-level firewall endpoint associations 

  
View details about the firewall endpoint association in a project | Any of the following roles:  


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoint associations, and at either the project level or the organization level for project-level firewall endpoint associations 
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)

  
View all of the firewall endpoint associations in a project. | Any of the following roles:   


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)
  * [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) at the organization level for organization-level firewall endpoints, and at either the project or organization level for firewall endpoints. 

  
  
## Quotas

To view quotas associated with firewall endpoints, see [Quotas and limits](https://docs.cloud.google.com/firewall/docs/quotas).

## What's next

  * [Configure the URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering)
  * [Configure intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention)
  * [Configure Advanced malware sandbox service](https://docs.cloud.google.com/firewall/docs/configure-wildfire)
  * [Create firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
