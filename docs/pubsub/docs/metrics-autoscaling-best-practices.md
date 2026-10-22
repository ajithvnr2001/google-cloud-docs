---
url: https://docs.cloud.google.com/pubsub/docs/metrics-autoscaling-best-practices/
title: Best practices for using Pub/Sub metrics as a scaling signal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:37.794065+00:00
---

# Best practices for using Pub/Sub metrics as a scaling signal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/metrics-autoscaling-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Best practices for using Pub/Sub metrics as a scaling signal Stay organized with collections  Save and categorize content based on your preferences. 

If you use Pub/Sub metrics as a signal to autoscale your pipeline, here are some recommendations.

## Use more than one signal to autoscale your pipeline

Don't use only Pub/Sub metrics to autoscale your pipeline. It might lead to scenarios where you have a single point of failure for your autoscaling decisions. Instead, use a combination of signals to trigger autoscaling. An example of an additional signal is the client's CPU utilization level. This signal can indicate whether the client tasks are handling work and if scaling up can let the client tasks handle more work. Some examples of signals from other Cloud products that you can use for your pipeline are as follows:

  * Compute Engine supports autoscaling based on signals such as CPU utilization and Monitoring metrics. Compute Engine also supports multiple metrics and multiple signals for better reliability.

For more information about scaling with Monitoring metrics, see [Scale based on Monitoring metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics). For more information about scaling with CPU utilization, see [Scale based on CPU utilization](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu).

  * Google Kubernetes Engine Horizontal Pod autoscaling (HPA) supports autoscaling based on resource usage such as CPU and memory usage, custom Kubernetes metrics, and external metrics such as Monitoring metrics for Pub/Sub. It also supports multiple signals.

For more information, see [Horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).




## Use the regional version of the metrics instead of global versions

Pub/Sub offers two versions of each metric typically used with autoscaling. Make sure you use the versions with the `by_region` suffix:

  * [`subscription/num_unacked_messages_by_region`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/num_unacked_messages_by_region)
  * [`subscription/oldest_unacked_message_age_by_region`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/oldest_unacked_message_age_by_region)



Don't use the global versions of these metrics if you want your autoscaling to be resilient to single-region outages. The global version of these metrics requires the calculation of the backlog across all regions known to have messages, which means unavailability in a single region results in a data gap. In contrast, the `by_region` versions of the metrics calculate and report the backlog on a per-region basis. If the backlog cannot be computed for a single region, the metric still reports values for the other regions.

## Avoid using subscriber-side throughput metrics to autoscale subscribers

Avoid using subscriber-side throughput metrics like `subscription/ack_message_count` to autoscale subscriber clients. Instead, consider using metrics that directly reflect the backlog of messages waiting to be processed, such as the previously mentioned `subscription/num_unacked_messages` or `subscription/oldest_unacked_message_age`.

**Issues with using subscriber-side throughput metrics for autoscaling**

Using these metrics can cause problems because they represent the amount of traffic between Pub/Sub and subscribers. Scaling based on such metric can create a self-referential loop where a decrease in delivered or acknowledged messages leads to scaling down of clients. For example, this might occur if there is a temporary dip in traffic or there is an issue with one of your subscribers.

If your clients scale down to zero or near-zero, all on-going subscribe traffic can stop, and subscribers may not be able to process messages, even if new messages arrive. This can result in significant ingestion lag and lead to an unrecoverable state for your subscriber clients.

## Deal with metrics gaps when they occur

Don't assume that the absence of metrics means that there are no messages to process. For example, if in response to missing metrics, you scale down processing tasks to zero, messages already in the backlog or that get published during this time might not be consumed. This increases the end-to-end latency. To minimize latency, set a minimum task count greater than zero so that you are always prepared to handle published messages, even if recent Pub/Sub metrics indicate an empty queue.

Both Compute Engine autoscalers and Google Kubernetes Engine HPAs are designed to maintain the current replica count when metrics are unavailable. This provides a safety net if no metrics are available.

You can also implement [Pub/Sub flow control](https://docs.cloud.google.com/pubsub/docs/flow-control) mechanisms to help prevent tasks from being overwhelmed if they are unintentionally downscaled due to missing metrics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
