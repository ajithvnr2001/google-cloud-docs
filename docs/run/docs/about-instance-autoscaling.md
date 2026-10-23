---
url: https://docs.cloud.google.com/run/docs/about-instance-autoscaling/
title: About instance autoscaling in Cloud Run services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:15.952964+00:00
---

# About instance autoscaling in Cloud Run services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/about-instance-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  About instance autoscaling in Cloud Run services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Cloud Run default autoscaling behavior. For an alternate scaling option where you can configure a specific instance count, see [Manual scaling](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling).

By default, each Cloud Run [revision](https://docs.cloud.google.com/run/docs/resource-model#revisions) is automatically scaled to the number of instances needed to handle incoming requests, events, or CPU utilization. You can also fine-tune this scaling behavior by [configuring custom CPU and concurrency utilization targets](https://docs.cloud.google.com/run/docs/configuring/scaling-controls).

When a revision does not receive any traffic, by default, it is scaled to zero instances. You can change this default to specify an instance to be kept idle or "warm" using the [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instance) setting. If your service is using CPU even when it's not processing requests, you should set minimum instances to `1`.

Cloud Run autoscaler evaluates the following metrics periodically to determine the number of instances needed to serve traffic:

  * **CPU and concurrency utilization** : Cloud Run adjusts instance counts to keep average CPU and concurrency within target thresholds.

  * **Instance limits** : Cloud Run bounds the number of instances between the [maximum](https://docs.cloud.google.com/run/docs/configuring/max-instances) and [minimum](https://docs.cloud.google.com/run/docs/configuring/min-instances) limits you configure.




## Horizontal service autoscaling behavior

Cloud Run has two autoscaling mechanisms, metrics-based scaling and on-demand scaling to determine the number of instances needed to serve traffic.

### Metrics-based scaling

Metrics-based scaling automatically adjusts the number of instances based on the average CPU utilization and the average request concurrency scaling drivers to provide stable serving capacity for your Cloud Run service.

The autoscaler determines a recommended number of instances based on the maximum number of instances it calculates for each of the following scaling drivers independently:

  * **CPU utilization** : calculates the number of instances by averaging the CPU usage per second over a 1-minute period and divides this by the number of CPUs per instance. This result is further divided by the CPU target. The following equation defines this calculation:



\\[ \text{Instances} = \left\lceil \dfrac{\left( \frac{\text{Average CPU usage per second over the past minute}}{\text{Number of CPUs per instance}} \right)}{\text{CPU target}} \right\rceil \\]

  * **Request concurrency** : calculates the number of instances by averaging the request concurrency per second over a 1-minute and 10-minute period and divides this by the maximum concurrency. This result is further divided by the request concurrency target. The following equation defines this calculation:



\\[ \text{Instances} = \left\lceil \dfrac{\left( \frac{\max(\text{average concurrent requests over 1 minute, 10 minutes})}{\text{Maximum concurrency}} \right)}{\text{Concurrency target}} \right\rceil \\]

  * **Adaptive concurrency tuning (ACT)** : calculates the recommended number of instances for 1-minute average request concurrency. This method uses each instance's ACT value as the instance's request concurrency capacity instead of the configured maximum concurrent requests. ACT dynamically reduces concurrency by 1 at 1-second intervals when CPU utilization exceeds 90%. For more information, see Adaptive concurrency tuning (ACT).



For each service revision, you can configure the number of CPUs per instance and maximum concurrency.

Cloud Run doesn't support scaling based on memory utilization.

By default, metrics-based scaling sets a 60% threshold for CPU utilization and request concurrency targets. You can use [scaling controls](https://docs.cloud.google.com/run/docs/configuring/scaling-controls#custom-targets) to specify custom CPU or concurrency targets.

When Cloud Run scales based on CPU utilization, it considers the average CPU utilization across all CPUs allocated to an instance. If your application is single-threaded but deployed on a multi-CPU instance, this can lead to a low average utilization reading, potentially impacting how CPU-based scaling decisions are made. For more details on optimizing CPU configuration for your application's architecture, see [Configure CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu) and [Set maximum concurrent requests per instance](https://docs.cloud.google.com/run/docs/configuring/concurrency).

#### Scale up

Cloud Run increases the number of instances based on whichever scaling driver requires more instances. At low instance counts, metrics-based scaling responds closely to your utilization targets.

Metrics-based scaling keeps the current instance count while utilization stays within a 10% tolerance of your target, relative to the target. For example, with the default 60% target, the instance count doesn't change while utilization stays between 54% and 66%.

When utilization moves outside that range, metrics-based scaling recalculates the instance count from the measured usage and your target, not from the number of running instances, and rounds the result up to the next whole instance. Because of this rounding, your service can scale up while utilization is still below your target. For example, a service that needs 4.1 instances to meet the target runs 5 instances.

#### Scale down

Cloud Run's autoscaling reduces the number of running instances when they are no longer needed to serve incoming traffic. Metrics-based scaling continuously adjusts the number of instances it recommends based on utilization. Cloud Run reduces the recommended instance count only when utilization drops more than 10% below the target, and then uses the same rounded-up calculation to determine the new count.

When the average CPU usage or average active requests decrease, the scaling algorithm reduces the recommended number of instances. The Cloud Run request load balancer considers these recommendations by preferentially routing incoming requests to the recommended instances first. This keeps recommended instances busier and lets other instances go idle. Cloud Run reduces the count of these unrecommended instances by deprioritizing them so they only receive traffic if all recommended instances are busy. To maintain stability, Cloud Run shuts down the deprioritized instances in the following order:

  1. Cloud Run shuts down a group of instances when their utilization over a 1-minute window is less than 10%.
  2. A second group of instances remains running until a 15-minute idle timeout occurs, ensuring capacity is available in case of a sudden traffic spike.



If your service performs other tasks even when it isn't processing requests, such as running background threads, or processing asynchronous tasks, you should set minimum instances to at least 1 to ensure that the CPU remains allocated for background processing.

### On-demand scaling

Cloud Run uses on-demand scaling when it can't find an available instance to serve the incoming request. On-demand scaling responds in real time to changes in the incoming traffic on a Cloud Run revision, or changes in the revision's latency. This scaling attempts to ensure that every incoming request gets routed to an instance in a short amount of time. On-demand scaling is the only driver for scaling from zero. However, when scaling from N instances, either metrics-based or on-demand scaling handles the traffic, depending on which triggers first.

Since on-demand scaling responds in real time to sudden traffic changes, Cloud Run manages the trade-off between cold start latency (the time to start a new instance) and pending queue latency (the time a request waits for a slot to open on an existing instance). For each request, the system determines if queuing for an upcoming instance or an existing instance is faster (in that order) before trying to start a new on-demand instance. A request remains in the pending queue for a maximum of 10 seconds or 3.5 times the predicted cold start time (whichever is higher) before the system triggers a new on-demand instance.

### Adaptive concurrency tuning (ACT)

Cloud Run uses Adaptive concurrency tuning (ACT) to prevent CPU throttling from causing high request latency. This approach measures the CPU utilization for each instance at a given number of requests and adjusts the instance's maximum concurrent requests value dynamically to keep CPU utilization below 90%. ACT tunes concurrency based on the following scenarios:

  * Each time the CPU utilization over the past 1 second exceeds 90%, ACT lowers the instance's maximum concurrent requests by 1.

  * If the instance hits its maximum concurrent requests limit, and CPU utilization stays under 70% for 1 second, ACT increases the maximum concurrent requests for the instance by 1.

  * If your scaling metrics show that concurrency never reaches your configured maximum, it might be because ACT dynamically lowered the actual maximum to protect instance performance.




Cloud Run calculates ACT values for each deployment. These metrics don't persist across deployments. If ACT reduces concurrency below the preferred level, increase the CPU allocated per maximum concurrent request. Background tasks that cause periodic CPU spikes can also interfere with this scaling approach.

You can monitor when ACT is actively driving your autoscaling by viewing the `scaling_driver` field in the Google Cloud console. For details on how to view this metric, see [Configure custom scaling controls for services](https://docs.cloud.google.com/run/docs/configuring/scaling-controls#best-practices).

## Instance-based billing and autoscaling

If you configure [instance-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings) for your Cloud Run service, you should be aware of scaling _to_ and _from_ zero behavior.

**Scaling from zero.** Scaling from zero can only be triggered by a request, so a service that is not processing requests cannot scale from zero. For these workloads, you can either set minimum instances > 0, or include a "wake-up request" in your design to restart processing after scaling to zero.

**Scaling to zero.** Given that no instance is ever at 0% CPU, looking at all CPU usage would result in never scaling to zero. This means the decision to scale from one to zero can only be made by checking to see if the instance is processing a request.

## About maximum instances for services

In some cases you may want to limit the total number of instances that can be started, for cost control reasons, or for better compatibility with other resources used by your service. For example, your Cloud Run service might interact with a database that can only handle a certain number of concurrent open connections.

All services are assigned a maximum instances limit by default, even if you don't specify your own limit. Set and monitor this limit to determine the scaling behavior and the costs associated with your service. For more information, see [Maximum instances limits](https://docs.cloud.google.com/run/docs/configuring/max-instances-limits).

You can use the maximum instances setting to limit the total number of instances that can be started in parallel, as documented in [Setting a maximum number of instances](https://docs.cloud.google.com/run/docs/configuring/max-instances).

### Exceeding maximum instances

Under normal circumstances, your revision scales out by creating new instances to handle incoming traffic load. But when you set a maximum instances limit, in some scenarios there will be insufficient instances to meet that traffic load. In that case, incoming requests are queued (pending) as follows:

Requests will pend for up to 3.5 times average startup time of container instances of this service, or 10 seconds, whichever is greater.

During this time window, if an instance finishes processing requests, it becomes available to process the queued pending requests. If no instances become available during the window, the request fails with a `429` error code.

### Scaling guarantees

The maximum instances limit is an upper limit per revision and it means that the number of instances for this revision shouldn't exceed the maximum.

Under normal circumstances, Cloud Run is able to scale out to the maximum instances limit very fast to handle all incoming requests or events. However, setting a high limit does not mean that your revision will be able scale out to the specified number of instances at any given moment. In exceptional circumstances, Cloud Run can throttle scaling to ensure good service for all customers.

### Exceeding maximum instances due to traffic spikes

In some cases, such as rapid traffic surges or system maintenance, Cloud Run might, for a short period of time, create more instances than are specified in the maximum instances setting. New instances can be started in excess of the maximum instances setting to replace existing instances and to provide a grace period for inflight requests to finish processing.

The maximum instance limit can be exceeded under normal operation a few times per week. The grace period usually lasts up to 15 minutes, or up to the value specified in the [request timeout](https://docs.cloud.google.com/run/docs/configuring/request-timeout) setting. These extra instances are destroyed within 15 minutes after they become idle.

If many replacements are needed, the updates are usually spread out over many minutes or hours, but each replacement has an excess instance for just the grace period. Instances in excess of the maximum instance value are normally less than twice the configured maximum instances limit, but can be much larger for sudden large traffic spikes.

Load tests experience _more_ instances exceeding the maximum instances setting because the system may change where traffic spikes are served to preserve capacity for existing workloads that have sustained load patterns.

If your service cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower maximum instances value.

### Traffic splits

Because the maximum instances limit is a limit for each revision, if the service [splits traffic across multiple revisions](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#split-traffic), the total number of instances for the service can exceed the maximum instances per revision. This can be observed in the [Instance Count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run) metrics.

### Deployments

When you deploy a new revision to serve 100% of the traffic, Cloud Run starts enough instances of the new revision before directing traffic to it. This reduces the impact of new revision deployments on request latencies, notably when serving high levels of traffic. Because the maximum instances limit is a limit for each revision, during a deployment, the total number of instances for the service can exceed the maximum instances per revision. This can be observed in the [Instance Count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run) metrics.

## Idle instances and minimizing cold starts

To minimize cold starts, Cloud Run might keep instances idle for a a period of time after they finish handling requests (up to 15 minutes, or 10 minutes for GPUs).

An idle instance might persist resources, such as open database connections. Note that the default billing setting is request-based billing unless you explicitly configure your service to have [instance-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings).

To keep idle instances _permanently_ available, use the [`min-instance`](https://docs.cloud.google.com/run/docs/configuring/min-instance) setting. Note that using this feature will [incur cost](https://cloud.google.com/run/pricing) even when the service is not actively serving requests.

## Autoscaling and pending requests

Requests will pend for up to 3.5 times average startup time of container instances of this service, or 10 seconds, whichever is greater.

## Autoscaling impact on backing services

As the number of instances automatically increases, your Cloud Run service might encounter limits with its backing services. For example, Cloud SQL has an [API quota limit](https://docs.cloud.google.com/sql/docs/mysql/connect-run#api-quota-limits). Make sure these backing services have enough quota and can handle connections from all instances of your Cloud Run service. Consider setting a [maximum number of instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) to avoid overloading backing services.

## Autoscaling and Pub/Sub

Google recommends using push subscriptions to consume messages from a Pub/Sub topic on Cloud Run. Pushed messages are received like HTTP requests by the container, thus triggering the same autoscaling behavior.

## Autoscaling and multiple containers (sidecars)

Cloud Run considers the CPU utilization of _instances_ for autoscaling, where the CPU utilization of an instance is the percentage of allocated CPU in use.

Note that you allocate CPU when you set [CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu) at the container level. If you use [multiple containers per instance](https://docs.cloud.google.com/run/docs/deploying#sidecars), the actual CPU allocation for that instance is the sum of the CPU limits you set on each container.

## What's next

  * To configure custom utilization targets or disable scaling drivers, see [Configure custom scaling controls](https://docs.cloud.google.com/run/docs/configuring/scaling-controls).
  * To learn about other scaling options, see [manual scaling](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling).
  * To manage the maximum number of instances of your Cloud Run services, see [Setting a maximum number of instances](https://docs.cloud.google.com/run/docs/configuring/max-instances).
  * To manage the maximum number of simultaneous requests handled by each instance, see [Setting concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency).
  * To optimize your concurrency setting, see [development tips for tuning concurrency](https://docs.cloud.google.com/run/docs/tips#tuning-concurrency).
  * To specify an idle instance to keep running to minimize latency or cold starts on first requests, see [Using `min-instance` to enable idle instances](https://docs.cloud.google.com/run/docs/configuring/min-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
