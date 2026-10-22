---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/resource-model/
title: Knative serving resource model \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:56.892795+00:00
---

# Knative serving resource model  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/resource-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Knative serving resource model Stay organized with collections  Save and categorize content based on your preferences. 

Use Knative serving to automatically manage the infrastructure needed to host software on Google Kubernetes Engine (GKE). To manage your applications, Knative serving uses an organizational structure called a _resource model_. This resource model consists of three main parts: _Services_ , _Revisions_ , and _Container Instances_.

The following diagram illustrates these components and their interactions: a Google Cloud project contains two Knative serving services, Service A and Service B, each with several revisions. Service A is processing requests with multiple running container instances, while Service B is idle.

![Knative serving services and revisions](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/images/resource-model.svg)

## Knative serving services

The service is the main resource of Knative serving. Each service is located in a specific [GKE cluster namespace](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-organizing-with-namespaces).

A given Google Cloud project can run many services in different regions or GKE clusters.

Each service exposes a unique endpoint and automatically scales the underlying infrastructure to handle incoming requests.

## Knative serving revisions

Each deployment to a service creates a revision. A revision consists of a specific container image, along with environment settings such as environment variables, memory limits, or concurrency value.

Revisions are immutable: once a revision has been created, it cannot be modified. For example, when you deploy a container image to a new Knative serving service, the first revision is created. If you then deploy a different container image to that same service, a second revision is created. If you subsequently set an environment variable, a third revision is created. Each subsequent configuration change creates a new revision.

Requests are automatically routed as soon as possible to the latest healthy service revision. You can [split traffic](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/rollouts-rollbacks-traffic-migration#split-traffic) between different revisions as needed.

## Knative serving container instances

Each revision receiving requests is automatically scaled to the number of container instances needed to handle all these requests. Note that a container instance can receive many requests at the same time. With the [concurrency setting](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/concurrency), you can set the maximum number of requests that can be sent in parallel to a given container instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
