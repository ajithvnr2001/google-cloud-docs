---
url: https://docs.cloud.google.com/vpc/docs/private-google-access/
title: Private Google Access \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:21.612969+00:00
---

# Private Google Access  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/private-google-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private Google Access

VM instances that only have internal IP addresses (no external IP addresses) can use Private Google Access. They can reach the external IP addresses of Google APIs and services. The source IP address of the packet can be the primary internal IP address of the network interface or an address in an alias IP range that is assigned to the interface. If you disable Private Google Access, the VM instances can no longer reach Google APIs and services; they can only send traffic within the VPC network.

Private Google Access has no effect on instances that have external IP addresses. Instances with external IP addresses can access the internet, according to the [internet access requirements](https://docs.cloud.google.com/vpc/docs/vpc#internet_access_reqs). They don't need any special configuration to send requests to the external IP addresses of Google APIs and services.

You enable Private Google Access on a subnet by subnet basis; it's a setting for subnets in a VPC network. To enable a subnet for Private Google Access and to view the requirements, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

## Supported services

Private Google Access lets you access [Google APIs and services](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options) that are hosted in Google's production infrastructure.

Private Google Access doesn't support [regional and multi-regional endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) (endpoints that end in `rep.googleapis.com`). To connect to these endpoints, see [Access regional Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints).

Other Google services are hosted in VPC networks and can be accessed by using the following methods:

  * To connect to services that are published using the [Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest), see [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).

  * To connect to services that are published using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer), see [Access managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services).




## Example

The following diagram shows an implementation of Private Google Access.

[ ![Implementation of Private Google Access.](https://docs.cloud.google.com/static/vpc/images/private-google-access.svg)](https://docs.cloud.google.com/static/vpc/images/private-google-access.svg) Implementation of Private Google Access (click to enlarge).

The VPC network has been configured to meet the [DNS, routing, and firewall network requirements](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config) for Google APIs and services. Private Google Access has been enabled on `subnet-a`, but not on `subnet-b`.

  * `VM A1` can access Google APIs and services, including Cloud Storage, because its network interface is located in `subnet-a`, which has Private Google Access enabled. Private Google Access applies to the instance because it only has an internal IP address.

  * `VM B1` **cannot** access Google APIs and services because it only has an internal IP address and Private Google Access is disabled for `subnet-b`.

  * `VM A2` and `VM B2` can both access Google APIs and services, including Cloud Storage, because they each have external IP addresses. Private Google Access has no effect on whether or not these instances can access Google APIs and services because both have external IP addresses.




## What's next

  * To configure Private Google Access, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
