---
url: https://docs.cloud.google.com/vpc/docs/private-access-options/
title: Private access options for services \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:21.453410+00:00
---

# Private access options for services  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/private-access-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private access options for services

This document provides an overview of the different options for private connectivity to Google and third-party APIs and services. By default, a virtual machine (VM) that doesn't have an external IP address can't reach anything outside of its VPC network, including Google APIs and services. Google Cloud provides several options to provide private connectivity to services through a VM's internal IP address. All Google Cloud APIs and services support at least one of the following private access options:

  * Private Service Connect
  * Private Google Access
  * Private services access
  * VPC Network Peering



You can configure one or more of these options—the options operate independently of each other.

## Types of Google Cloud services

Google Cloud offers two types of services:

  * Google APIs and services that run on Google's production infrastructure. Example services include the following:

    * Web applications such as Gmail, Google Docs and Google Maps.
    * Google APIs, including those that have `*.googleapis.com` API service endpoints.
    * Serverless resources served from `*.appspot.com`, `*.run.app`, or `*.cloudfunctions.net` URLs.
    * Files served from `*.gstatic.com` URLs.

Services in Google's production infrastructure might offer private connectivity through Private Service Connect, Private Google Access, or both.

  * VPC-hosted services that run on Compute Engine VMs in VPC networks. VPC-hosted services can be managed by Google or by third-party service producers. Example services include the following:

    * Cloud SQL
    * Filestore
    * Memorystore for Redis

VPC-hosted services might offer private connectivity through Private Service Connect, private services access, VPC Network Peering, or a combination of those options.




Additionally, if you have a serverless service, you can connect from the service to VPC networks.

## Connect to Google APIs

The following table describes the private access options for connecting to Google APIs and services that are hosted in Google's production infrastructure:

Option | Clients | Connection | Supported services  
---|---|---|---  
[ **Private Service Connect endpoints for Google APIs**](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) |   
| Google Cloud resources or on-premises systems, with or without external IP addresses. | Connect to an [ endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) in your VPC network, which forwards requests to Google APIs and services. | [ Supports all Google Cloud APIs and most other Google APIs and services](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis)1.  
[ **Private Service Connect backends for Google APIs**](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends)  
| Google Cloud resources or on-premises systems, with or without external IP addresses. | Connect to a [ load balancer](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#google-apis) in your VPC network, which forwards requests to Google APIs and services. | Supports selected [ locational](https://docs.cloud.google.com/vpc/docs/locational-service-endpoints) and [global](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-api-list) Google APIs and services.  
[**Private Google Access**](https://docs.cloud.google.com/vpc/docs/private-google-access) |   
| Google Cloud resources without external IP addresses. | Connect to the [standard external IP addresses or Private Google Access domains and VIPs](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config) for Google APIs and services through the VPC network's default internet gateway. | [Supports most Google APIs and services](https://docs.cloud.google.com/vpc/docs/private-google-access#pga-supported)1.  
[**Private Google Access for on-premises hosts**](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid) |   
| On-premises hosts with or without external IP addresses. | Connect to Google APIs and services from your on-premises network through a Cloud VPN tunnel or VLAN attachment by using one of the [Private Google Access-specific domains and VIPs](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid#private-vips). | The [Google services](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid#supported-services-onprem) that you can access depend on which Private Google Access-specific domain you use.  
  
1 Use private services access or Private Service Connect to connect to Google services that are not supported by Private Service Connect for Google APIs or Private Google Access. 

## Connect to services in VPC networks

The following table describes the private access options for connecting to VPC-hosted services:

Option | Clients | Connection | Supported services | Usage  
---|---|---|---|---  
**Connecting to services**  
[ **Private Service Connect endpoints for published services**](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) |  |   
| Google Cloud VM instances with or without external IP addresses. | Connect to services in another VPC network through an endpoint. | Supports services that are published using [Private Service Connect for service producers. ](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) | Use this option to connect to supported services in another VPC network without assigning external IP addresses to your Google Cloud resources.  
[ **Private Service Connect backends for published services**](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) |  |   
| Google Cloud VM instances with or without external IP addresses. | Connect to services in another VPC network through a load balancer. | Supports services that are published using [Private Service Connect for service producers. ](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) | Use this option to connect to supported services in another VPC network through a consumer-managed load balancer. You don't need to assign external IP addresses to your Google Cloud resources.  
[ **Service connection policies**](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) |  |   
| Google Cloud VM instances with or without external IP addresses. | Connect to services in another VPC network through an endpoint. | Supports specific Google and third-party services. To find out whether a service supports service connection policies, contact the service provider. | Use this option to deploy a managed service instance and configure connectivity through a service's administrative API or UI. The service instance is deployed in a producer VPC network that is connected to your VPC network through an endpoint. You don't need to assign external IP addresses to your Google Cloud resources.  
[**Private services access**](https://docs.cloud.google.com/vpc/docs/private-services-access) |  |   
| Google Cloud VM instances with or without external IP addresses. | Connect to a Google or third-party managed VPC network through a VPC Network Peering connection. | Supports [ Google services](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services)2 and third-party services that are made available using the [ Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest).  | Use this option to connect to specific Google and third-party services without assigning external IP addresses to your Google Cloud and Google or third-party resources.  
  
2 Use Private Service Connect for Google APIs or Private Google Access to connect to Google services that are not supported by private services access or Private Service Connect for published services. 

## Connect from serverless Google services to VPC networks

You can use [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) to let Cloud Run, App Engine standard, and Cloud Run functions environments send packets to the internal IPv4 addresses of resources in a VPC network. If Direct VPC egress isn't an option for you, you can configure a [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) connector instead. Both options also support sending packets to other networks connected to the selected VPC network.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
