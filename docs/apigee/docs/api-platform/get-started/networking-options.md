---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options/
title: Apigee networking options \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:54:54.529132+00:00
---

# Apigee networking options  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee networking options Stay organized with collections  Save and categorize content based on your preferences. 

You can choose one of two distinct networking options when you provision a new Apigee organization: Non-VPC Peering or VPC peering. These two options are summarized below. 

  * The Non-VPC Peering option uses [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to route traffic from clients to Apigee (northbound traffic) and from Apigee to target services hosted in your Google Cloud projects (southbound traffic). In this model, you do not need to provide dedicated IP ranges in your network during Apigee provisioning. See also [Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints) and [Northbound networking with Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc).
  * The VPC-peering option uses [private service access](https://docs.cloud.google.com/vpc/docs/private-services-access) to create a private connection between your VPC network and a network owned by Apigee. This model employs [VPC network peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) to connect your network with Apigee's. The peering model requires you to allocate dedicated IP ranges in your network when you provision a new instance of Apigee. Additionally, you can also leverage [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to route traffic from clients to Apigee (northbound traffic) and from Apigee to target services hosted in your Google Cloud projects (southbound traffic) along with VPC peering.



## Non-VPC Peering option

**Note:** The non-VPC peering option is available using the CLI provisioning steps only. Non-VPC peering through the Cloud console is not available at this time. You can use the CLI to provision Apigee with non-VPC peering for [subscription](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered), [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo), and [eval](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval) organizations. 

We also support using [Terraform](https://www.terraform.io/) to provision Apigee. See [Terraform overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview).

This option does not require VPC peering. With this approach, you are not required to provide networks and IP ranges during the Apigee provisioning process. Instead, you use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) for routing northbound traffic (from clients to Apigee) and southbound traffic (from Apigee to to target services running in your Google Cloud projects). 

Private Service Connect enables private connection between a service producer (Apigee) and a service consumer (one or more other Cloud projects that you control). With non-VPC peering provisioning, requests pass through either a global external load balancer or a regional external load balancer to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments) (Figure 1) using Private Service Connect. 

The non-VPC provisioning steps are described in [Provision without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/non-vpc-peered-arch.png)**Figure 1.** Apigee architecture without VPC peering. See also [ Apigee architecture overview](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview).![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/non-vpc-peered-arch.png)

## VPC peering option

Traditionally, Apigee has employed [VPC network peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) to enable communication between a virtual private cloud (VPC) network managed by you and a VPC network managed by Apigee. This configuration allows bi-directional communication between the two VPC networks and allows Apigee API proxies to call target services deployed in your VPC. If target applications are in the peered network, Apigee can access their IP addresses and route API proxy traffic to them. See also [Apigee architecture overview](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview). 

To create an Apigee instance, you are required to allocate a pair of IP Address Ranges (a /22 and /28 CIDR range) to Apigee and perform the VPC peering between your network and Apigee's network. Each Apigee instance requires a non-overlapping CIDR range of /22 and /28. The Apigee runtime plane is assigned IP addresses from within this CIDR range. As a result, it's important that the range is reserved for Apigee and not used by other applications in your VPC network.

Apigee supports peering with only one network; however, many enterprises have multiple networks where applications and services are deployed. In these cases, you can use Private Service Connect to privately connect Apigee to target services running across VPC networks in addition to the peered network (Figure 2). See [ Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints) for more information. 

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vpc-peered-architecture.png)**Figure 2.** Apigee architecture with VPC peering. For details of this architecture, see [Apigee architecture overview](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview).![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/vpc-peered-architecture.png)

The steps for provisioning Apigee with VPC peering are covered in [Provision with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli). 

## How to choose a networking option

The following table describes the features/approaches available with each networking option: 

**Feature availability** | **VPC peering-based provisioning** | **Non-VPC peering-based provisioning**  
---|---|---  
**Network requirements** |  |   
Requires network information for Apigee organization creation  | Yes  | No   
Requires IP range allocation for Apigee instance creation  | Yes (/22 & /28 CIDR ranges for each region)  | No   
  
**Northbound routing** |  |   
Private Service Connect-based routing  | Yes  | Yes   
MIG-based routing  | Yes  | No   
Global load balancing  | Yes  | Yes   
Global load balancing (Classic)  | Yes  | No   
Regional load balancing  | Yes  | Yes   
Health check for multi-region failover routing  | Yes—active health check with [MIG-based routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#external-routing-mig). See [Active health check](https://docs.cloud.google.com/apigee/docs/api-platform/debug/health-check#active-health-check).  | Yes—opt in to [PSC health check](https://docs.cloud.google.com/apigee/docs/api-platform/debug/health-check#psc-health-check) for built-in regional failover with [Private Service Connect NEGs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered#external-routing-psc). Alternatively, you can use a [MIG-based pattern](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/psc-health-check-using-mig) to drive active health check yourself.   
  
**Southbound routing** |  |   
Southbound routing options  | Can use VPC peering or Private Service Connect  | Private Service Connect Only   
  
**Other features** |  |   
DNS peering  
(See [Connecting with private DNS peering zones](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#connecting-with-private-dns-peering-zones))  | Yes  | Yes   
VPC Service Controls  | Yes  | No   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
