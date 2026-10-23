---
url: https://docs.cloud.google.com/run/docs/configuring/connecting-vpc/
title: Compare Direct VPC egress and VPC connectors \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:56:03.126198+00:00
---

# Compare Direct VPC egress and VPC connectors  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/connecting-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Compare Direct VPC egress and VPC connectors Stay organized with collections  Save and categorize content based on your preferences. 

This page is for networking specialists who want to compare the following methods for sending egress (outbound) traffic from a Cloud Run service or job to a VPC network: 

  * [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) (recommended)
  * [Serverless VPC Access connectors](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors)



Both of these methods allow access to Compute Engine VM instances, Memorystore instances, and any other resources with an internal IP address.

## Inbound and outbound requests

When using Direct VPC egress or Serverless VPC Access connectors, outbound connections initiated by Cloud Run services and jobs route directly to and from their destination.

Inbound requests sent from your VPC network to Cloud Run route through a custom load balancer, not through Direct VPC egress or Serverless VPC Access connectors.

To learn more about sending requests from your VPC network to Cloud Run, see [Receive requests from VPC networks](https://docs.cloud.google.com/run/docs/securing/private-networking#from-vpc).

## Direct VPC egress (recommended)

Direct VPC egress brings enhanced infrastructure and simpler VPC egress configuration to Cloud Run, including the following advantages:

  * **Setup** : Cloud Run services and jobs can send traffic to a VPC network without the overhead of managing a Serverless VPC Access connector.
  * **Cost** : You only pay for network traffic charges, which scale to zero just like the service itself.
  * **Security** : You can use network tags directly on service revisions for more granular network security.
  * **Performance** : Lower latency, higher throughput.



## Serverless VPC Access connectors

Serverless VPC Access connectors also let you send requests to your VPC network and receive the corresponding responses without using the public internet. Setup requires additional maintenance and cost with lower performance than Direct VPC egress offers.

See the comparison table for details.

## Comparison table

Feature | Direct VPC egress | Serverless VPC Access connector  
---|---|---  
Spend caps support | Supported | Not supported  
Latency | Lower | Higher  
Throughput | Higher | Lower  
IP allocation | Uses more IP addresses in most cases | Uses fewer IP addresses  
Cost | No additional VM charges | Incurs additional VM charges  
Scaling speed | [Instance autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) is slower, including starting from zero, while creating new VPC network interfaces. | Network latency occurs during VPC network traffic surges while more connector instances are created.  
Network tags | Finer granularity. Each service or job can have its own unique sets of tags; firewall rules applied separately. | Less granularity. Shared across services and jobs that use the same connectors; firewall rules applied at the connector level.  
Firewall Rules Logging | Firewall Rules Logging for Cloud Run egress traffic doesn't include the Cloud Run resource name. | Firewall Rules Logging for Cloud Run egress traffic includes the connector instance name, not the name of the Cloud Run resource.  
Cloud Next Generation Firewall Enterprise layer 7 inspection | Not supported | Not supported  
Google Cloud console | Supported | Supported  
Google Cloud CLI | Supported | Supported  
Launch stage | GA | GA  
  
## Pricing

For pricing information, see [Cloud Run pricing](https://cloud.google.com/run/pricing).

With Serverless VPC Access connectors, you pay for two types of charges: Compute (billed as Compute Engine VMs) and network egress (billed as traffic from VMs). With Direct VPC egress, you pay only for network egress (at the same rate as connectors). You do not pay any compute charges.

If you use Serverless VPC Access connectors, you can view your associated costs as follows:

  1. Go to the [Cloud Billing Reports page](https://console.cloud.google.com/billing/reports) in the Google Cloud console.
  2. If prompted, select the billing account associated with your Google Cloud project.
  3. In the **Filters** panel, under **Labels** , [add a label filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) with the key `serverless-vpc-access`.
  4. In the **Value** field, select the names of the connectors that you want to filter for.



## Next steps

  * Learn how to [configure your service](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-service) with Direct VPC egress.
  * Learn how to [configure your job](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-job) with Direct VPC egress.
  * See information about [Direct VPC egress with a Shared VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-shared-vpc).
  * Learn how to [configure your service](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#configuring-service) with Serverless VPC Access connectors.
  * Learn how to [configure your job](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#configuring-job) with Serverless VPC Access connectors. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
