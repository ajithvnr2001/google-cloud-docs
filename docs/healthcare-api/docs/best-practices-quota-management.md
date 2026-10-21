---
url: https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management/
title: Quota management best practices \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:16.825015+00:00
---

# Quota management best practices  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Quota management best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for managing Cloud Healthcare API [quota](https://docs.cloud.google.com/docs/quotas/overview). Use this page if your Google Cloud project has, or might have, a large amount of traffic and you need more quota than what the Cloud Healthcare API provides by default.

## Cloud Healthcare API default quotas

The [default Cloud Healthcare API quotas](https://docs.cloud.google.com/healthcare-api/quotas) aren't designed for all use cases, particularly if your Google Cloud project has a large amount of traffic. The Cloud Healthcare API doesn't automatically grow quota. You must plan and monitor your quota usage.

## Best practices for monitoring and viewing quota

There are several methods for [viewing your quota usage](https://docs.cloud.google.com/docs/quotas/view-manage). When estimating and viewing quota for the Cloud Healthcare API, we recommend that you use the [Service Quota Model](https://docs.cloud.google.com/service-usage/docs/service-quota-model). The model lets you accurately assess the available quota you have based on the following criteria:

  * Whether an _admin override_ is present. A principal granted the [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaAdmin) role in an organization can apply an admin override to quota in Google Cloud projects within the organization. An admin override supersedes default limits and producer overrides.
  * Whether a _producer override_ is present. A service owner grants a producer override to a consumer of a service. Google Cloud is the service owner of the Cloud Healthcare API service. Any quota override that Google Cloud provides is a producer override.

**Important:** Admin overrides supersede producer overrides. If you have been granted additional quota using a producer override, but you have an existing admin override, the producer override might not take effect.
  * Whether a _consumer override_ is present. Someone who makes requests to the Cloud Healthcare API is a consumer of the Cloud Healthcare API service. You can apply consumer overrides for various situations, such as limiting quotas in your Google Cloud project as a cost-control measure to prevent going over your budget.




If you have any of these overrides in effect, you can [compute your consumer quota limit](https://docs.cloud.google.com/service-usage/docs/service-quota-model#computing_quota_limit) to get an accurate assessment of your available quota.

## Best practices for requesting additional quota

Google Cloud has procedures to [request a higher quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase). To learn how quota adjustment requests are processed, see [About quota adjustments](https://docs.cloud.google.com/docs/quotas/overview#about_increase_requests).

Before requesting additional quota, ensure that you've implemented both of the following:

  * [Exponential backoff](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#use-exponential)
  * [Client-side rate limiting](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#implement-client-side)



These implementations might reduce the amount of quota you require for the following reasons:

  * Both implementations spread load spikes out across several hours or minutes, rather than seconds.
  * Both implementations make efficient use of quota over a 24 hour period. If requests that significantly exceed the default quota are consistent over a 24 hour period, larger pools of resources can be allocated to the Cloud Healthcare API service. The additional allocation of resources is by request only and is determined on a case-by-case basis.
  * Consistent resource usage makes it simpler for Google Cloud to understand your quota requirements and provide you with the quota you need.



To manage your capacity and quota effectively, you need to know your organization's capacity requirements. If you're planning your capacity requirements and think that you'll need a large quota increase when your Google Cloud project is in production, request an increase from [Google Cloud Customer Care](https://docs.cloud.google.com/support). Customer Care can assist you with allocating and increasing quota during the testing and rollout phases of your Google Cloud project.

You don't need to have a paid Customer Care service to request a quota increase. Some quota increase requests are completed within 2-3 business days, but we recommend that you plan for longer. If your quota increase is large, it can take 10 business days or more for the quota increase request to be completed. Part of your planning must involve allocating time to respond to Customer Care to resolve any questions or open issues about the request. If you ensure that your initial quota increase request is sufficiently detailed, you might be able to reduce the time spent waiting for the request to be fulfilled.

## Best practices for anticipating quota needs

Before your Google Cloud project goes into production, anticipate and plan for how much quota you will need. Planning your quota requirements prevents unexpected limiting of your resource consumption later.

The following sections explain what to consider when planning for quota.

### Anticipate total usage for all data stores and clients

Understand your total usage across all Cloud Healthcare API [data stores](https://docs.cloud.google.com/healthcare-api/docs/concepts/projects-datasets-data-stores#datasets_and_data_stores), and understand the total usage of all clients that make requests to your Google Cloud project.

  * Some Google Cloud projects implement multiple Cloud Healthcare API use cases. For example, your Google Cloud project might use multiple Cloud Healthcare API datasets and data stores for different types of data, thus increasing your total quota usage.
  * Quotas are enforced on a per-Google Cloud-project and per-region basis. Ensure that you have accurate measurements of your required quota across multiple regions. If you have multiple Google Cloud projects, you might need more accurate measurements across the projects. For more information on planning for quota per-region, see Anticipate per-region usage.
  * The Cloud Healthcare API doesn't load balance quota across clients, datasets, or data stores. The client must determine whether to implement a prioritization scheme to ensure that the most critical traffic doesn't encounter `429 RESOURCE_EXHAUSTED` errors.



### Anticipate per-region usage

Cloud Healthcare API measures quotas at a per-Google Cloud-project and per-region basis. Quotas are typically measured per minute, which allows for small spikes of requests per second to balance out on a per-minute scale.

If your Google Cloud project uses multiple regions, you can set per-region quotas.

If your Cloud Healthcare API dataset is in the [`us`](https://docs.cloud.google.com/healthcare-api/docs/concepts/regions#multi-regional_locations) multi-regional location, and you want to request additional quota, state in your quota request that the quota is for the "US meta region". The `us` multi-regional location consists of the following subregions:

  * `us-central1`
  * `us-east1`
  * `us-west1`



If you already have Cloud Healthcare API traffic using quota in any of the `us-` subregions, ensure that you take the existing traffic in those subregions into account when making a quota increase request for the `us` multi-region. For example, if you have datasets in `us-central1` and `us`, and you request a quota increase in `us`, specify in your request that you have datasets in `us-central1`.

### Favor low-volume transactions on a consistent basis

The following scenario explains the importance of sending smaller amounts of traffic on a consistent basis instead of sending high-volume transactions with a longer interval between transactions.

Traffic _volume_ is calculated using the formula `request payload * time = traffic volume`. A _high-volume_ transaction is one or more requests to the Cloud Healthcare API in a short interval that contain a large payload. A series of requests can also be considered _high-volume_ if there are many requests sent over a short interval, regardless of the payload size.

Suppose that a client collects high-volume transactions and sends the transactions to the Cloud Healthcare API in a burst every five minutes. The following occurs:

  1. The initial burst of traffic consumes quota in the first minute (dependent on minute rollovers) until all quota is exhausted.
  2. Any remaining burst traffic receives `429 RESOURCE_EXHAUSTED` errors. If configured, all affected requests encounter exponential backoff.
  3. Some percentage of requests that encountered the initial exponential backoff are rescheduled to be tried again in the next minute. Some requests are attempted multiple times in a single minute, and then are retried the next minute.
  4. If the request volume is high enough, retried requests might encounter `429 RESOURCE_EXHAUSTED` errors and exponential backoff again. Certain bursts of traffic might encounter exponential backoff at different times, and the attempts to send traffic again might converge on the same minute in the future.
  5. If the request volume is still high, some traffic is retried when the next burst of traffic begins. The issue is exacerbated because more traffic is added to the existing backlog of requests. Your application might have difficulty maintaining the backlog of requests and sending them consistently to the Cloud Healthcare API.



This scenario shows the importance of knowing the volume of your traffic on a per-minute basis. Implement your traffic volume and backoffs to prevent network congestion and ensure that your application doesn't encounter many failures that require retries.

## Review DICOM and FHIR quotas

To view the Cloud Healthcare API quotas associated with FHIR and DICOM stores and operations, see [Quota limits](https://docs.cloud.google.com/healthcare-api/quotas#quota-limits).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
