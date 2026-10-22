---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/instance-autoscaling/
title: Container instance autoscaling \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:56.138219+00:00
---

# Container instance autoscaling  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/instance-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Container instance autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

In Knative serving, each [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/resource-model#revisions) is automatically scaled to the number of container instances needed to handle all incoming requests. When a revision does not receive any traffic, by default it is scaled to zero container instances. However, if desired, you can change this default to specify an instance to be kept idle or "warm" using the [minimum instances](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/min-instances) setting.

The number of instances scheduled is impacted by:

  * The amount of CPU needed to process a request
  * The [concurrency setting](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/concurrency)
  * The [maximum number of container instances setting](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/max-instances)
  * The [minimum number of container instances setting](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/min-instances)



In some cases you may want to limit the total number of container instances that can be started, for cost control reasons, or for better compatibility with other resources used by your service. For example, your Knative serving service might interact with a database that can only handle a certain number of concurrent open connections.

## About maximum container instances

You can use the maximum container instances setting to limit the total number of instances that can be started in parallel, as documented in [Setting a maximum number of container instances](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/max-instances).

### Exceeding maximum instances

Under normal circumstances, your revision scales out by creating new instances to handle incoming traffic load. But when you set a maximum instances limit, in some scenarios there will be insufficient instances to meet that traffic load. In that case, incoming requests queue for up to 60 seconds. During this 60 second window, if an instance finishes processing requests, it becomes available to process queued requests. If no instances become available during the 60 second window, the request fails with a `429` error code on Cloud Run.

### Scaling guarantees

The maximum instances limit is an upper limit. Setting a high limit does not mean that your revision will scale out to the specified number of container instances. It only means that the number of container instances at any point in time should not exceed the limit.

### Traffic spikes

In some cases, such as rapid traffic surges, Knative serving may, for a short period of time, create slightly _more_ container instances than the specified max instances value. If your service cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower max instances value.

## Deployments

When you deploy a new revision, Knative serving gradually migrates traffic from the old revision to the new one. Because maximum instances limits are set for each revision, you may temporarily exceed the specified limit during the period after deployment.

## Idle instances and minimizing cold starts

Kubernetes resources are only consumed when an instance is handling a request, but this does not mean that Knative serving immediately shuts down instances once they have handled all requests. To minimize the impact of cold starts, Knative serving may keep some instances idle. These instances are ready to handle requests in case of a sudden traffic spike.

For example, when a container instance has finished handling requests, it may remain idle for a period of time in case another request needs to be handled. An idle container instance may persist resources, such as open database connections. However, for Cloud Run, the [CPU will not be available](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/reference/container-contract#cpu)

To keep idle instances _permanently_ available, use the [`min-instance`](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/min-instances) setting.

## What's next

  * To manage the maximum number of instances of your Knative serving services, see [Setting a maximum number of container instances](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/max-instances).
  * To manage the maximum number of simultaneous requests handled by each container instance, see [Setting concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/concurrency).
  * To optimize your concurrency setting, see [development tips for tuning concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general#tuning-concurrency).
  * To specify an idle instance to keep running to minimize latency or cold starts on first requests, see [Using `min-instance` to enable idle instances](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/min-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
