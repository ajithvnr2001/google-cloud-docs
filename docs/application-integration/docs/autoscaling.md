---
url: https://docs.cloud.google.com/application-integration/docs/autoscaling/
title: About autoscaling in Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:48.680359+00:00
---

# About autoscaling in Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About autoscaling in Application Integration

Application Integration, built on the same underlying infrastructure as some of Google Cloud's largest-scale services, offers autoscaling capabilities. Autoscaling enables integration workloads to adapt automatically to changing demands. This helps eliminate the need for manual intervention or complex tuning in most cases and provides reliable performance and seamless scaling.

## How Application Integration scales

Application Integration uses both horizontal and vertical scaling to manage varying workloads:

### Horizontal scaling

Scales out dynamically by provisioning or deprovisioning the Application Integration instances based on the workload or demand. When demand increases, horizontal autoscaling provisions additional instances to run concurrently and handle the increased load. Conversely, during periods of low activity, the unused instances are deprovisioned to optimize resource usage.

**Example:** A sudden surge in orders can trigger autoscaling, which provisions additional integration instances to handle the increased volume and process requests in parallel.

### Vertical scaling

Scales up by allocating additional resources (such as GCU and RAM) to each individual task or Application Integration instance on demand. Instead of provisioning more instances, vertical scaling enhances the performance of the existing instances.

**Example:** A complex data transformation task may require additional memory. Vertical scaling allocates additional memory to help complete the task more efficiently.

**Note:** The Application Integration platform automatically provisions additional resources as needed during scaling. This dynamic provisioning may introduce brief latency while the resources are being initialized. To ensure smooth and reliable performance during anticipated traffic surges (such as marketing campaigns or seasonal peaks), it's recommended to plan ahead and request resource scaling in advance. If you require assistance with proactive scaling, [contact support](https://docs.cloud.google.com/application-integration/docs/getting-support).

Application Integration adheres to defined quotas and limits, which can be increased upon request. For more information, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

To understand the autoscaling behavior of Integration Connectors, see [About autoscaling in Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/autoscaling).

## Benefits

The autoscaling features of Application Integration provide the following advantages:

  * **Performance at scale:** Automatically adjust to changes in traffic and usage. Planned scaling is still recommended for predictable, high-impact events like seasonal peaks.
  * **Reduced operational overhead:** Scaling is automated and doesn't require manual intervention in most cases. For extreme load spikes, advance planning may still be needed.
  * **Enhanced reliability:** Responds to traffic spikes while maintaining service availability.
  * **Simplified management:** Scaling is handled by Google Cloud's infrastructure, letting teams focus on building integrations instead of managing scaling infrastructure.



## Observability and monitoring

Application Integration automatically exports a rich set of metrics to Cloud Monitoring, providing deep insights into the usage, performance, and health of your integrations.

While a single, pre-built dashboard for all metrics across projects isn't directly available within the Application Integration platform, you can leverage Cloud Monitoring to create custom dashboards tailored to your specific needs.

### Key Application Integration metrics

Key metrics | Description  
---|---  
Integration execution latency | The time taken for individual integration executions to complete.  
Data processed by integration executions | The size of data processed by integrations, including input/output parameters and payloads.  
Integration execution count | The number of individual tasks or triggers executed within an integration workflow.  
Status | The execution status of the integration or integration step (task or trigger). For example, succeeded, failed, or cancelled.  
  
For a comprehensive list of all Application Integration metrics available for monitoring, refer to [Monitor Application Integration resources](https://docs.cloud.google.com/application-integration/docs/monitoring-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
