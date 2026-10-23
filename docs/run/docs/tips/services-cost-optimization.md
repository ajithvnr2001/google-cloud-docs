---
url: https://docs.cloud.google.com/run/docs/tips/services-cost-optimization/
title: Best practices for cost-optimized Cloud Run services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:39.131212+00:00
---

# Best practices for cost-optimized Cloud Run services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tips/services-cost-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Best practices for cost-optimized Cloud Run services Stay organized with collections  Save and categorize content based on your preferences. 

Optimizing your Cloud Run services reduces expenses by aligning resource allocation with actual demand. Implementing cost-effective configurations prevents overprovisioning while maintaining service reliability and performance. There is no one-size-fits-all solution for cost optimization. It is important to monitor your needs, budget, and resources to determine what works best for you.

The best practices outlined in this document are specific to Cloud Run. These are not inclusive of other Google Cloud products.

## Resource configurations

Optimizing your services for cost involves consideration of many different configurations. Tailor these configurations to your needs to create services that are reliable and cost efficient.

### Select the appropriate region

Your service's deployment location impacts your total cost. Cloud Run uses a [two tier regional](https://docs.cloud.google.com/run/docs/locations) pricing model. Tier 1 regions offer a lower cost per vCPU and memory compared to Tier 2 regions, so consider deploying to a Tier 1 region.

### Require authentication

When configuring a Cloud Run service, you can choose from one of the two authentication options:

  * **Allow public access** : Authentication checks are not required.
  * **Require authentication** : Only authenticated users can access your Cloud Run service.



We recommend requiring authentication, unless you have a specific need to allow public access. This will prevent unwanted requests that could incur costs.

If you manage users with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/enabling-cloud-run), IAP might have its own associated costs.

### Compare instance-based versus request-based billing

Cloud Run services have [two billing settings](https://docs.cloud.google.com/run/docs/configuring/billing-settings):

  * **Request-based billing (default)** : You are charged per request, plus a higher per-second rate for vCPU and memory consumed during request processing.
  * **Instance-based billing** : You are charged for the entire lifetime of an instance. There is no per-request fee, and the per-second rates for vCPU and memory are lower.



For services with steady, slowly varying traffic, consider using instance-based billing. The savings from lower compute rates and no per-request fee outweigh the cost of paying for idle time between requests. For services with sporadic, bursty, or spiky traffic, consider using request-based billing. If you are still unsure about which billing setting to use, see [Recommender](https://docs.cloud.google.com/run/docs/recommender). The Recommender looks at the traffic received by your Cloud Run service over the past month and provides recommendations for switching from request-based billing to instance-based billing, if it is cheaper to do so.

### Configure service scaling at the service level

To establish a cost-safety baseline, configure [maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances-limits) for your service. Setting a higher maximum number prioritizes availability, but introduces potential billing risks from unexpected traffic spikes or misconfigurations. You should configure this setting at the service-level when you initially deploy your service to establish a cost baseline. For additional cost control tools, see [resource allocation quotas](https://docs.cloud.google.com/run/quotas#cloud_run_limits) or [billing budgets and alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).

### Optimize CPU and memory utilization

The cost of your Cloud Run service is impacted by its CPU/memory configuration and how long your service is active, among other factors. Overprovisioning your resources can increase your costs. To determine which configuration might be best for your service:

  1. Establish a baseline configuration.
  2. Monitor your metrics while testing the CPU and memory utilization metrics in Cloud Monitoring.
  3. Adjust your configuration as necessary.



If CPU utilization is consistently low under peak load, consider reducing vCPU allocation. If latency is high, consider increasing vCPU allocation.

If memory utilization is consistently low, consider reducing the allocated memory. If latency is high and memory utilization is near 100%, consider increasing the allocated memory. If you are experiencing Out of Memory (OOM) errors, you should increase the allocated memory or modify your application to prevent memory leaks or use less memory. See the [Cloud Monitoring dashboard](https://docs.cloud.google.com/monitoring/dashboards) to better understand your memory utilization.

### Configure GPU

All Cloud Run services using GPUs must have [instance-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings) configured. This means that Cloud Run instances are charged for the entire lifecycle of instances, even when there are no incoming requests. The minimum CPU and memory configurations required for GPUs also impact the cost of your Cloud Run service. By default, GPU zonal redundancy is turned on. Turning off GPU zonal redundancy results in a lower cost per GPU second, but does not guarantee reserved capacity for failover scenarios.

## Optimize networking costs

When configuring networking options for your service, consider the following:

  * **Co-locate your resources** : Try to deploy your Cloud Run services in the same region as your backend databases (like Cloud SQL or Firestore) and Cloud Storage buckets. Data transfer between Google Cloud resources within the same region is free.
  * **Switch to Direct VPC egress** : If you are securely routing traffic to internal VPC network resources, consider switching to [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) from Serverless VPC Access connectors. Direct VPC egress scales to zero, eliminating the baseline compute overhead and idle costs associated with connector instances. 
  * **Use Cloud CDN** : Offload static assets and highly cacheable content by placing [Cloud CDN](https://docs.cloud.google.com/cdn/docs) in front of your Cloud Run services. Serving data from the edge is significantly cheaper than paying for standard internet egress directly from Cloud Run. 
  * **Monitor internet egress** : Inbound traffic (ingress) is always free, and you receive 1 GiB of free outbound internet data transfer per month within North America. Focus your monitoring efforts on outbound traffic that crosses region boundaries or exceeds the free tier.



## Configure concurrency settings

When more instances process requests, Cloud Run allocates more CPU and memory at higher costs. A higher concurrency setting lets fewer instances handle the same request volume, which can reduce costs. However, the application code must be able to handle parallel requests efficiently. For more information, see [Tuning concurrency for autoscaling and resource utilization](https://docs.cloud.google.com/run/docs/about-concurrency#tuning-concurrency). 

## Committed use discounts

Committed use discounts (CUDs) provide discounted prices in exchange for committing to continuously using Cloud Run for a specified period of time. CUDs apply at a Cloud Billing-account level. You can purchase Compute flexible CUDs for Cloud Run resources. Compute flexible CUDs don't apply to GPUs or networking. See [Compute flexible committed use discount](https://docs.cloud.google.com/run/cud) for more details.

## Helpful tools

You can use the following tools to better understand your costs and to help avoid cost overruns.

### Cloud Run overview: Billing panel

The [Cloud Run overview page](https://console.cloud.google.com/run/overview) shows costs per resource name in the Billing panel. The numbers reflect the gross costs for selected time ranges per resource. This tool helps you better understand how much your resources cost.

### Budget alerts

Create [budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) in Cloud Billing to track your actual costs against your planned costs. A budget alert is an alerting mechanism that triggers notifications when spending thresholds are crossed, not a hard spending cap. There is a billing data delay that might impact when you receive alerts.

### Budget spend caps

When you configure Cloud Billing Budget [spend caps](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps) in the Cloud Billing console or programmatically using the [Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap), those caps automatically apply to all Cloud Run resource types in your project.

You can monitor your spend cap progress directly from the [Cloud Run console](https://console.cloud.google.com/run/) overview page. When you hit a spend cap, Google Cloud pauses all Cloud Run workloads to prevent further costs to the following Cloud Run resources:

  * Services: any existing service will fail to serve traffic and return `5xx` errors.
  * Jobs: new task executions fail to start, and in-progress tasks fail to complete.
  * Worker pools: any existing instances stop processing tasks.
  * [Instances](https://docs.cloud.google.com/run/docs/instances/create-and-manage-instances): any running instances shut down, new instances or restarts fail to start, and requests to instance URLs return `5xx` errors.



If you exceed your spend cap, you'll receive an alert notification and see an enforcement banner in the [Cloud Run console](https://console.cloud.google.com/run/). Enforced spend caps reset at the start of each month on the first day of the next billing cycle, unblocking your workloads and setting the spend amount to zero. If you exceed your spend cap and want to resume operations before the monthly reset, manually adjust or lift the cap in the Cloud Run console overview page.

**Note:** Compute Engine bills VPC connector VMs, so Cloud Run spend caps ignore them. If you want spend caps to fully cover egress networking, use [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).

### Cloud Billing

[Cloud Billing](https://docs.cloud.google.com/billing/docs/concepts) is a collection of tools that help you track and understand your Google Cloud spending. These tools help you monitor your usage costs, forecast your spending, and identify opportunities to save on costs.

### Cost Explorer

The [Cost Explorer](https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs) lets you understand the cost and utilization of your resources. Use Cost Explorer to:

  * Filter your resources by cost to see which resources are the most costly.
  * Understand what proportion of costs are driven by configurations such as vCPU, GPU, networking, and more.
  * Track impacts of changes to your resource configuration on your monthly bill.



### Google Cloud pricing calculator

The [Google Cloud pricing overview](https://cloud.google.com/pricing) contains information for better understanding the Google Cloud pricing model. This is also where you can find the [Detailed price list](https://cloud.google.com/pricing/list). You can estimate your costs by adding and configuring products by using the [pricing calculator](https://cloud.google.com/products/calculator).

### Recommender

[Recommender](https://docs.cloud.google.com/run/docs/recommender) is a tool that provides usage recommendations and insights for Cloud products.

Recommender automatically looks at traffic received by your Cloud Run service over the past month, and will recommend switching from request-based billing to instance-based billing, if this is cheaper. 

### Cloud Hub Optimization

You can view summary cost data, utilization data, and cost optimization recommendations for Google Cloud services on Cloud Hub's [Optimization page](https://docs.cloud.google.com/hub/docs/optimize).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
