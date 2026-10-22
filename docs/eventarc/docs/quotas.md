---
url: https://docs.cloud.google.com/eventarc/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:26.622817+00:00
---

# Quotas and limits  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Resources ](https://docs.cloud.google.com/eventarc/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This document lists the quotas and system limits that apply to Eventarc.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Eventarc resources. System limits can't be changed. 

**Note:** Eventarc uses Pub/Sub push subscriptions that are subject to [throughput limits](https://docs.cloud.google.com/pubsub/quotas#resource_limits) per publish region.

## Quotas

If your project needs more of a particular resource than your quotas allow, you can [request an adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase) to most quotas in the Google Cloud console. For more information, see [About quota adjustments](https://docs.cloud.google.com/docs/quotas/overview#about_increase_requests).

### Eventarc Advanced

Quota | Description | Value | Can be increased | Scope  
---|---|---|---|---  
Bus throughput | Publishing throughput 1 | 384 MB per minute 2 | No | Per project per region per minute  
Enrollments | Number of enrollments | 100 | No | Per project per region  
Enrollments | Number of enrollments that can be attached to a bus | 100 | No | Per bus  
Pipelines | Number of pipelines | 100 | No | Per project per region  
Write requests | Number of management plane 3 writes | 1000 | No | Per project per region per minute  
  
**1** Throughput quota is measured in 64 kB increments. For example, a 1 kB message would use 64 kB of quota.

**2** The maximum pipeline throughput is also 384 MB per minute (or 6.4 MB per second average).

**3** Resource API operations.

### Eventarc Standard

Quota | Description | Value | Can be increased | Scope  
---|---|---|---|---  
Trigger read requests | Number of trigger API reads | 6000 | Yes | Per project per minute  
Trigger write requests | Number of trigger API writes | 600 | Yes. The [global location](https://docs.cloud.google.com/eventarc/docs/locations#global-region) has a write limit of 10 QPS. | Per project per minute  
  
## Limits

The number of Eventarc resources is limited for a given project. There is no direct limit on the size of the Eventarc API request.

### Eventarc Advanced

Resource | Description | Limit | Can be increased | Scope  
---|---|---|---|---  
Bus | Number of `MessageBus` resources | 1 | No | Per project per region  
Bus | Number of `MessageBus` resources | 5000 | No | Per organization  
Event | Event size | 1 MB | No | N/A  
Event message | Context attribute value size 1 | 1024 bytes | No | N/A  
Event message | Number of context attributes (including required attributes) | 80 | No | N/A  
Google API source | Number of `GoogleApiSource` resources | 1 | No | Per project per region  
Pipeline | Queries per second | 100 (1 KB payload) | No | Per pipeline  
Read requests | Number of management plane 2 reads | 6000 | No | Per project per region per minute  
Schema | Size of input or output data format schemas when [converting the format](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events) of an event | 8 KB | No | Per schema per pipeline  
  
**1** Applicable to non-Google events that are [ directly published](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format): if the size limit of an event [context attribute](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#context-attributes) value is exceeded, an error occurs, and publishing is prevented.

**2** Resource API operations.

### Eventarc Standard

Resource | Description | Limit | Can be increased | Scope  
---|---|---|---|---  
Event | Event size | 512 KB | No | N/A  
Event message | Context attribute value size 1 | 1024 bytes | No | N/A  
Published events (third-party and custom events) | Number of third-party and custom events that can be published per project across all channels | 300 | No. To request an exception, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support). | Per project  
Trigger | Number of `Trigger` resources | 500 | No | Per location per project  
Trigger | Number of triggers for [internal HTTP endpoints](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events) | 100 | No | Per project  
  
**1** Applicable only to Cloud Audit Logs events: if the size limit of an event [context attribute](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#context-attributes) value is exceeded, the value is truncated. Attribute names for any truncated values, delimited by semicolons, are listed in the extension attribute, `ce_xgoogletruncatedattributes`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
