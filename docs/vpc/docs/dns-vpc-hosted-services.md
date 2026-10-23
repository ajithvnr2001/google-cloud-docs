---
url: https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services/
title: DNS configuration for published services \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:12.244578+00:00
---

# DNS configuration for published services  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DNS configuration for published services

Service producers can [publish services by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer). The service producer can optionally configure a DNS domain name to associate with the service. If a domain name is configured, and a [service consumer creates an endpoint that targets that service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services), Private Service Connect and Service Directory automatically create DNS entries for the service in a private DNS zone in the service consumer's VPC network.

## DNS configuration for service producers

When you publish a service (create a service attachment), you can optionally configure a DNS domain name.

If you configure a domain name for a service, when a Private Service Connect endpoint is created that connects to that service, the following configurations are made in the service consumer's VPC network:

  * A [Service Directory DNS zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone) is created for the specified domain.

  * A DNS entry for each endpoint is created in the zone.




The recommended format for the domain name is `REGION.p.DOMAIN`. Because this domain name is used to create DNS entries in the service consumer's VPC network, it's important to use a name that doesn't conflict with any existing DNS domain names. Using this format reduces the risk of conflicts.

For example, if the service is configured with the domain name `us-west1.p.example.com`, and the service consumer creates an endpoint with the name `analytics`, a DNS record for `analytics.us-west1.p.example.com` is automatically created.

The load balancer that is hosting the service must be able to accept requests directed to this domain name. If you are using an internal Application Load Balancer, you might need to update the load balancer configuration to reflect the domain names that you want service consumers to use. For example, update [certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) or [URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

The same IAM principal that [publishes the service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) must confirm that they have Owner permissions for the domain in the Google Search Console. For more information, see [Before you begin](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#before) in _Publish services by using Private Service Connect_.

## Automatic DNS configuration for service consumers

If the following configurations are present, DNS entries are automatically created for endpoints:

  * The service producer has configured a domain name for the service.

  * The endpoint is configured with an IPv4 address.

  * The endpoint is registered with a Service Directory namespace.

All new endpoints are automatically registered with Service Directory, but older endpoints might not be registered.




If both configurations are present, when the endpoint is created, a [Service Directory DNS zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone) is created with the name `NAMESPACE--REGION`. This private zone stores DNS entries for services found in the Service Directory namespace `NAMESPACE` in the region `REGION`. The character limit for `NAMESPACE--REGION` is 63 characters or fewer.

[ ![](https://docs.cloud.google.com/static/vpc/images/private-service-connect-services-autodns.svg)](https://docs.cloud.google.com/static/vpc/images/private-service-connect-services-autodns.svg)

**Figure 1.** Automatic DNS configuration for endpoints using Service Directory (click to enlarge).

After you create the endpoint, you can verify if a Service Directory DNS zone is created. If the Service Directory DNS zone is not created, you can manually create a similar configuration. For more information, see [View Service Directory DNS zones](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#view-private-zones).

If you don't want these DNS entries to be created, do one of the following:

  * If you're not using Cloud DNS for another purpose, disable the Cloud DNS API, or remove the permissions that are required for Cloud DNS.

  * Wait for the DNS zone to be created, then [Delete the DNS zone](https://docs.cloud.google.com/dns/docs/zones#deleting_a_managed_zone) manually.

If you want to manually configure DNS, see [Configure DNS manually](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#configure-dns-manual).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
