---
url: https://docs.cloud.google.com/appengine/docs/standard/compare-direct-vpc-egress-connectors/
title: Compare Direct VPC egress and Serverless VPC Access connectors \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:41.087567+00:00
---

# Compare Direct VPC egress and Serverless VPC Access connectors  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/compare-direct-vpc-egress-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Compare Direct VPC egress and Serverless VPC Access connectors Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Direct VPC egress for App Engine**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can send egress (outbound) traffic from an App Engine service to a VPC network using either of the following methods:

  * [Direct VPC egress (recommended) (Preview)](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc)
  * [Serverless VPC Access connectors](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc)



This document helps networking specialists compare these methods to determine which solution best meets their requirements for performance, cost, and management.

Both Direct VPC egress and Serverless VPC Access connectors allow access to resources with an internal IP address, such as Compute Engine VM instances and Memorystore instances.

We recommend using Direct VPC egress since it brings enhanced infrastructure and simpler VPC egress configuration to App Engine. For key benefits, see [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc#key_benefits).

Serverless VPC Access connectors also let you send requests to your VPC network and receive the corresponding responses without using the public internet. Compared to Direct VPC egress, the setup requires additional maintenance and cost with lower throughput, but connectors are still a suitable option if your application requires lower cold start latency when scaling from zero or has limited IP address availability.

## Inbound and outbound requests

When using Direct VPC egress or Serverless VPC Access connectors, outbound connections initiated by App Engine services route directly to and from their destination.

Inbound requests sent from your VPC network to App Engine route through a custom load balancer, not through Direct VPC egress or Serverless VPC Access connectors.

## Key differences

The following table compares the key capabilities, performance characteristics, and costs for Direct VPC egress and Serverless VPC Access connectors.

Feature | Direct VPC egress | Serverless VPC Access connector  
---|---|---  
Latency | Lower | Higher  
Throughput | Higher | Lower  
IP allocation | Uses more IP addresses in most cases | Uses fewer IP addresses  
Cost | No additional VM charges | Incurs additional VM charges  
Scaling speed | [Instance autoscaling](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed) is slower, including starting from zero (cold start latency), while creating new VPC network interfaces. | Network latency occurs during VPC network traffic surges while more connector instances are created.  
Network tags | Finer granularity. Each service can have its own unique sets of tags; firewall rules applied separately. | Less granularity. Shared across App Engine services that use the same connectors; firewall rules applied at the connector level.  
Firewall Rules Logging | Firewall Rules Logging for App Engine egress traffic doesn't include the resource name. | Firewall Rules Logging for App Engine egress traffic includes the connector instance name, not the name of the App Engine service.  
Google Cloud console | Not supported | Supported  
Google Cloud CLI | Supported | Supported  
Launch stage | Preview | GA  
  
## Pricing

For pricing information, see [App Engine pricing](https://docs.cloud.google.com/appengine/pricing).

With Serverless VPC Access connectors, you pay for two types of charges: Compute (billed as Compute Engine VMs) and network egress (billed as traffic from VMs). With Direct VPC egress, you pay only for network egress (at the same rate as connectors). You don't pay any compute charges.

If you use Serverless VPC Access connectors, you can view your associated costs as follows:

  1. Go to the [Cloud Billing Reports page](https://console.cloud.google.com/billing/reports) in the Google Cloud console.
  2. If prompted, select the billing account associated with your Google Cloud project project.
  3. In the **Filters** panel, under **Labels** , [add a label filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) with the key `serverless-vpc-access`.
  4. In the **Value** field, select the names of the connectors that you want to filter for.



## What's next

  * [Configure Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc)
  * [Configure Serverless VPC Access connectors](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc)
  * [Compare Direct VPC egress between App Engine and Cloud Run](https://docs.cloud.google.com/appengine/docs/standard/compare-direct-vpc-app-engine-cloud-run)
  * [Connect to a Shared VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-shared-vpc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
