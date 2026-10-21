---
url: https://docs.cloud.google.com/run/docs/configuring/max-instances-limits/
title: About maximum instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:49.019879+00:00
---

# About maximum instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/max-instances-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  About maximum instances Stay organized with collections  Save and categorize content based on your preferences. 

By default, Cloud Run services have a maximum number of instances determined by the lowest of the following relevant quota limits. The maximum limit for each region is also impacted by the CPU and memory configuration for your Cloud Run service. Specifically, the maximum number of instances available for your service is the minimum of each of the following:

  * regional [CPU quota](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fcpu_allocation_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\)) divided by the CPU configuration for the service.
  * regional [memory quota](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fmem_allocation_5C_22_22_2C_22s_22_3Atrue%257D%255D%22\)\)) divided by the memory configuration for the service.
  * regional [GPU quota](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_l4_gpu_allocation_5C_22_22_2C_22i_22_3A_22metricName_22%257D_2C%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22OR_5C_22_22_2C_22o_22_3Atrue%257D_2C%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_l4_gpu_allocation_no_zonal_redundancy_5C_22_22_2C_22s_22_3Atrue%257D%255D%22\)\)), with or without zonal redundancy, divided by the GPU configuration for the service.



For example, a baseline quota of 1000 vCPU or 2000 GiB memory would allow a deployment using 2 GiB memory or 1 CPU to specify a maximum of 1000 instances for a single service.

These quotas are also accounted as a sum of all in-use resources in the region across of your Cloud Run resources. You may experience failures to scale up or start new job executions if your total usage reaches one of these limits.

You can see the baseline total CPU, Memory, and GPU limits per-region quota for your region in the [quotas page](https://console.cloud.google.com/iam-admin/quotas?service=run.googleapis.com&usage=ALL) in the console.

## How to increase baseline regional quota

If you need a greater total count of CPU, memory, or GPU for the region your Cloud Run service is deployed to, you can [request a quota increase](https://docs.cloud.google.com/run/quotas#increase).

## Best practices for setting maximum instances

The following section describes the best practices for configuring maximum instance limits for your services.

### Optimal maximum instance value for event-driven services

Event driven services, such as functions, can experience sporadic traffic spikes based on incoming events. To determine an optimal maximum instance value for these services, you need to consider factors such as, service invocation time, expected average invocation, peak invocation frequency, and fault tolerance for invocation failures.

A good rule of thumb is to start with a maximum instances value of 3, then monitor for invocation failures and adjust the maximum instances value upward as necessary.

### Handle requests when all instances are busy

Under normal circumstances, your service scales up by creating new instances to handle incoming traffic load. But when you have set a maximum instances limit, you might encounter a scenario where there are insufficient instances to meet incoming traffic load.

In that scenario, Cloud Run attempts to serve a new inbound request for up to 30 seconds:

  * If an instance finishes processing its request during this time period, it might start to process the new inbound request.
  * If no instance becomes available, the request will fail.



Cloud Run automatically saves events destined for event-driven services until capacity is available.

### Maximum instance limits that exceed Cloud Run's scaling ability

When you specify a maximum instances limit, you are specifying an upper limit. Setting a large limit does not mean that your service will scale up to the specified number of instances. It only means that the number of instances that co-exist at any point in time shouldn't exceed the limit.

Further, setting a maximum instances limit might affect the scaling strategies that Cloud Run uses to meet your traffic demand. In general, Cloud Run will prioritize honoring your specified limit rather than scaling up and potentially exceeding your limit.

### Handle traffic spikes

In some cases, such as rapid traffic surges, Cloud Run might, for a short period of time, create more instances than the specified maximum instances limit. If your service can't tolerate this temporary behavior, you might want to factor in a safety margin and set a lower maximum instances value than your service can tolerate.

### Deployments

When you deploy a new revision, Cloud Run migrates traffic from the earlier revision to the new one. Because maximum instance limits are set for each revision independently, you might temporarily exceed the specified limit during the period after deployment.

For example, a service might have a maximum instances limit of 5. Under normal circumstances, the service scales up to 5 instances as it handles requests. When you deploy a new revision, the new revision has its own max instances limit of 5.

Requests that are already being handled by the previous revision aren't interrupted when you deploy a new revision. Instead, these requests continue to make progress. New inbound requests will be handled by the newly-deployed revision of your service.

Thus, the service in the previous example might have up to 10 total instances (5 for each revision) during the period after deploying the new revision. The amount of time required for instances of the previous revision to terminate depends on the time required for those instances to finish handling any active requests. This is an additional factor to take into account when selecting an appropriate max instances limit.

### Cost considerations

The maximum instances setting lets you establish a cost-safety limit to manage cost. Setting a higher maximum number prioritizes availability, but it introduces potential billing risks from unexpected traffic spikes or misconfigurations. As a cost safeguard, configure this setting at the service level when you initially deploy your service. We suggest starting with a maximum instances value of 3 to protect your budget from unexpected spikes.

Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information. For additional cost control tools, see [resource allocation quotas](https://docs.cloud.google.com/run/quotas#cloud_run_limits) or [billing budgets and alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
