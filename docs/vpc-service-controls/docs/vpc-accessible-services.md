---
url: https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services/
title: VPC accessible services \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:52.400235+00:00
---

# VPC accessible services  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  VPC accessible services Stay organized with collections  Save and categorize content based on your preferences. 

To define the services that can be accessed from a network inside your service perimeter, use the _VPC accessible services_ feature. The VPC accessible services feature limits the set of services that are accessible from network endpoints inside your service perimeter.

The VPC accessible services feature applies only to traffic from your VPC network endpoints to Google APIs. Unlike service perimeters, the VPC accessible services feature doesn't apply to communication between Google APIs or to [tenancy units](https://cloud.google.com/service-infrastructure/docs/glossary#tenancy) networks, which are used to implement certain Google Cloud services.

When configuring VPC accessible services for a perimeter, you can specify a list of individual services. You can also include the `RESTRICTED-SERVICES` value, which automatically includes all services protected by the perimeter.

To ensure that access to the expected services is limited, you must do the following:

  * Configure the perimeter to protect the same set of services that you want to make accessible.
  * Restrict network access depending on whether you need to use unsupported services: 
    * To restrict access to supported services, configure VPC networks to use the [restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).
    * To restrict access to unsupported Google APIs, configure VPC networks to use the [private VIP](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-options) and configure service patterns.
  * Use VPC firewall rules to restrict traffic based on destination IP addresses.



## VPC network with Cloud Storage only

Assume you have a service perimeter, `my-authorized-perimeter`, that includes two projects: `my-authorized-compute-project` and `my-authorized-gcs-project`. The perimeter protects the Cloud Storage service.

`my-authorized-gcs-project` uses a number of services, including Cloud Storage, Bigtable, and others. `my-authorized-compute-project` hosts a VPC network.

Because the two projects share a perimeter, the VPC network in `my-authorized-compute-project` has access to the resources of services in `my-authorized-gcs-project`, regardless of whether the perimeter protects those services. However, you want your VPC network to only have access to Cloud Storage resources in `my-authorized-gcs-project`.

You are concerned that if the credentials for a VM in your VPC network are stolen, an adversary could leverage that VM to exfiltrate data from any available service in `my-authorized-gcs-project`.

You have already configured your VPC network to use the restricted VIP, which limits access from your VPC network only to APIs that are supported by VPC Service Controls. However, this setting doesn't prevent your VPC network from accessing supported services, such as the Bigtable resources in `my-authorized-gcs-project`.

To limit the VPC network's access to only the storage service, you enable VPC accessible services and set `storage.googleapis.com` as an allowed service:
    
    
    gcloud access-context-manager perimeters update my-authorized-perimeter \
      --enable-vpc-accessible-services \
      --add-vpc-allowed-services=storage.googleapis.com
    

Success! After running this command, the VPC network in `my-authorized-compute-project` can only access Cloud Storage resources. This restriction also applies to any projects and VPC networks that you add to the perimeter later.

## VPC Service Controls service patterns

VPC Service Controls service patterns let you configure which Google APIs can be accessed from VPC networks in a service perimeter when using the private VIP. You can specify Google API URL patterns for unsupported services that you want to allow access to and deny access to all other unsupported API requests on the private VIP path.

You can use service patterns to attach HTTP headers (such as `X-Goog-Allowed-Resources`) to API requests for unsupported services without deploying a proxy. Doing so helps mitigate exfiltration risks by enforcing tenant-based or domain-based restrictions.

To configure service patterns, see [Limit access to Google APIs by using service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#service-patterns-cfg).

## What's next?

  * [Use VPC accessible services.](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#accessible-services)
  * [Optimize perimeters with recommender](https://docs.cloud.google.com/vpc-service-controls/docs/recommender) ([Preview](https://cloud.google.com/products/#product-launch-stages)).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
