---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/concurrency/
title: Concurrency \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:36.585158+00:00
---

# Concurrency  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/concurrency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Concurrency Stay organized with collections  Save and categorize content based on your preferences. 

In Knative serving, each [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/resource-model#revisions) is automatically scaled to the number of container instances needed to handle all incoming requests.

When more container instances are processing requests, more CPU and memory will be used, resulting in higher costs. When new container instances need to be started, requests might take more time to be processed, decreasing the performances of your service.

To give you more control, Knative serving provides a _concurrency_ setting that specifies the maximum number of requests that can be processed simultaneously by a given container instance.

## Concurrency values

By default Knative serving container instances can receive many requests at the same time (up to a maximum of 80). Note that in comparison, Functions-as-a-Service (FaaS) solutions like Cloud Run functions have a fixed concurrency of 1.

Although you should use the default concurrency value, if needed you can [lower the maximum concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/concurrency). For example, if your code cannot process parallel requests, set concurrency to `1`.

The specified concurrency value is a maximum and Knative serving might not send as many requests to a given container instance if the CPU of the instance is already highly utilized.

The following diagram shows how the concurrency setting affects the number of container instances needed to handle incoming concurrent requests:

![Concurrency diagram](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/concurrency-diagram.svg)

## When to limit concurrency to one request at a time

You can limit concurrency so that only one request at a time will be sent to each running container instance. You should consider doing this in cases where:

  * Each request uses most of the available CPU or memory.
  * Your container image is not designed for handling multiple requests at the same time, for example, if your container relies on global state that two requests cannot share.



Note that a concurrency of `1` is likely to negatively affect scaling performance, because many container instances will have to start up to handle a spike in incoming requests.

## Case study

The following metrics show a use case where 400 clients are making 3 requests per second to a Knative serving service that is set to a maximum concurrency of 1. The green top line shows the requests over time, the bottom blue line shows the number of container instances started to handle the requests.

![Concurrency set to one](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/concurrency-1.png)

The following metrics show 400 clients making 3 requests per second to a Knative serving service that is set to a maximum concurrency of 80. The green top line shows the requests over time, the bottom blue line shows the number of container instances started to handle the requests. Notice that far fewer instances are needed to handle the same request volume.

![Concurrency set to 80](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/concurrency-80.png)

## What's next

To manage the concurrency of your Knative serving services, see [Setting concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/concurrency).

To optimize your concurrency setting, see [development tips for tuning concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general#tuning-concurrency).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
