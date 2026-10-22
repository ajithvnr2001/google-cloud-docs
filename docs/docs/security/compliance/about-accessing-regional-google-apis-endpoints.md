---
url: https://docs.cloud.google.com/docs/security/compliance/about-accessing-regional-google-apis-endpoints/
title: About accessing regional and multi-regional Google APIs through private endpoints \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:47.686368+00:00
---

# About accessing regional and multi-regional Google APIs through private endpoints  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/about-accessing-regional-google-apis-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  About accessing regional and multi-regional Google APIs through private endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of using [Private Service Connect endpoints to access regional endpoints and multi-regional endpoints](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints) for [supported Google APIs](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

Consider using regional endpoints or multi-regional endpoints if you want to ensure that in-transit data remains in a particular region or multi-region. For more information, see [Google Cloud API endpoint overview](https://docs.cloud.google.com/docs/security/compliance/endpoints).

For information about other Private Service Connect configurations, see [Private Service Connect overview](https://docs.cloud.google.com/vpc/docs/private-service-connect).

## Features and compatibility

This table summarizes the features that are supported by endpoints that are used to access regional endpoints for Google APIs.

Configuration | Details | **Consumer configuration (endpoint)**  
---  
Global reachability |  If [ global access](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints#global-access) is enabled  
[Cloud Interconnect traffic](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#hybrid-access) |   
[Cloud VPN traffic](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#hybrid-access) |   
[Access through VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) |   
[Connection propagation through NCC](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) |   
DNS configuration | [Manual DNS configuration](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#configure-dns)  
IP version | IPv4 or IPv6  
**Producer******  
Supported services | [Supported regional Google APIs](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints)  
  
## Specifications

  * Public hostnames for regional endpoints have the following formats: `SERVICE.REGION.rep.DOMAIN`.
  * Public hostnames for multi-regional endpoints have the following format: `SERVICE.MULTI_REGION.rep.DOMAIN`.

We recommend using the public hostnames to specify the target service in your Private Service Connect endpoint configuration.

**Note:** For regional endpoints only, the private hostname formats are also supported, ending with `p.rep.DOMAIN`. Multi-regional endpoints don't support private hostname formats.
  * The subnet that you specify when you create an endpoint is a [regular subnet](https://docs.cloud.google.com/vpc/docs/subnets#purpose). The IP address assigned to the endpoint is a regional internal IP address.

  * By default, endpoints can be accessed only by clients that are in the same region and the same VPC network (or Shared VPC network) as the endpoint. For information about making endpoints available in other regions, see Global access.

  * For information about creating this configuration in a Shared VPC network, see Shared VPC.




## Architecture

Private Service Connect endpoints that have a regional endpoint or multi-regional endpoint target point to a service attachment that has been created by Google to direct traffic to the service.

  * **Regional endpoints:** Traffic is routed to the regional service endpoint in the same region as the Private Service Connect endpoint.
  * **Multi-regional endpoints:** The Private Service Connect endpoint is regional (created in a specific region, such as `us-central1`), but the target is multi-regional (such as `us`). Traffic from the regional Private Service Connect endpoint is load balanced to a regional frontend. The regional frontend can be located in any of the regions associated with the multi-regional destination.



Clients in the same region as the endpoint can send traffic to the endpoint. You can also access the endpoint from [connected networks](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#hybrid-access) in the same region. If you want to access the endpoint from other regions, configure global access.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-endpoint-service-rep.svg)](https://docs.cloud.google.com/static/vpc/images/psc-endpoint-service-rep.svg)

**Figure 1.** An endpoint lets service consumers send traffic from the consumer's VPC network to regional service endpoints for supported Google APIs through a service attachment that is managed by Google (click to enlarge).

## Global access

When you create an endpoint, you can configure global access. Global access lets clients in other regions access the endpoint. The endpoint is also accessible from [connected networks](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#hybrid-access).

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-multi-region-rep.svg)](https://docs.cloud.google.com/static/vpc/images/psc-multi-region-rep.svg)

**Figure 2.** An endpoint with global access enabled can be accessed by clients in another region, including by clients in connected networks (click to enlarge). 

## Supported regions and services

For a list of supported regions and services, see [Regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

## DNS configuration and resolution

When you create a Private Service Connect endpoint that targets a regional or multi-regional endpoint, you must [create a DNS record in a private DNS zone](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#configure-dns) to send requests to it. For example, if you create a Private Service Connect endpoint that targets `storage.us-east1.rep.googleapis.com`, you must create a private DNS record for the hostname `storage.us-east1.rep.googleapis.com` that points to the IP address of your Private Service Connect endpoint.

If a client looks up `storage.us-east1.rep.googleapis.com` and that hostname doesn't exist in a private DNS zone, the query is forwarded to Google's public DNS servers. The public DNS servers respond with the [public IP address of the regional or multi-regional endpoint](https://docs.cloud.google.com/docs/security/compliance/about-regional-endpoints#public-access), _not_ the internal IP address of the Private Service Connect endpoint IP address.

If you're accessing the Private Service Connect endpoint from clients in hybrid networks, additional configuration is needed so that the hybrid clients can correctly resolve the hostname of the Private Service Connect endpoint. For more information, see [Access endpoints from hybrid networks](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#hybrid-access).

## Shared VPC

[Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) can create Private Service Connect endpoints in Shared VPC service projects that use IP addresses from [Shared VPC networks](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks).

In general, we recommend that you create forwarding rules and their corresponding address resources in the same Google Cloud project. Using the same project helps to avoid issues when a project is deleted.

If you're creating an endpoint in a service project and using a reserved static IP address in the configuration, use or create an address resource in the service project. The address resource can reference an IP address from a subnet in the host project, or from the service project, if it contains subnets.

We _don't_ recommend using an address resource from a host project to create an endpoint in a service project.

You must use the gcloud CLI or the API to create an endpoint in a service project, and this configuration requires [additional permissions](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#roles-shared-vpc).

For more information, see [Create a regional Private Service Connect endpoint in a Shared VPC service project](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#shared-vpc).

## Pricing

For pricing information, see [Virtual Private Cloud pricing](https://cloud.google.com/vpc/pricing#psc-forwarding-rule-regional-end-apis).

## Quotas

See the **Number of Regional Endpoints per project per region** quota in [Quotas and limits](https://docs.cloud.google.com/vpc/docs/quota#regional-per-project-regional-endpoints).

  * Create a Private Service Connect endpoint to [access regional or multi-regional Google APIs](https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints).
  * Learn more about [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
