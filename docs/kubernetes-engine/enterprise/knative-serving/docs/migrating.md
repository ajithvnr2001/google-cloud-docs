---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrating/
title: Migrating an Existing Service \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:00.793771+00:00
---

# Migrating an Existing Service  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Migrating an Existing Service Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows how to prepare a web service to run in a container on Knative serving. It does not cover data migration.

## Identify the port your code is listening on

Your service should listen for requests on a specific port. You must identify this port and [configure Knative serving to send request to the same port](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/containers#command-line).

This is the same port you would use when invoking your service on your local machine. For example, if to test your code you open `localhost:3000`, then [set the container port](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/containers#command-line) to `3000` in Knative serving.

Knative serving defaults to sending requests to `8080`. The value of the port to which requests are sent is always available in the `PORT` environment variable. It is a best practice for your code to listen on the value defined by the `PORT` environment variable if possible.

## Remove reliance on local filesystem for persistent storage

Check your application code for reliance on local filesystems, and replace it with file storage on [Cloud Storage](https://docs.cloud.google.com/storage) or data storage such as [Firestore](https://docs.cloud.google.com/firestore) or [Cloud SQL](https://docs.cloud.google.com/sql).

## Add a `Dockerfile`

In order to wrap your service in a container, you should use a Dockerfile to define the operating environment. Read more about customizing your `Dockerfile` on the [Developing your service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/developing#add-dockerfile) page.

## Tune for concurrency and memory limits

Learn about [concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/concurrency) in Knative serving and how to optimize your services in [development tips for tuning concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general#tuning-concurrency).

Make sure your [memory limit](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits) is high enough for your application to run, including capacity for any temporary file storage your service requires.

## Send logs to stdout or stderr

Knative serving automatically uses Google Cloud Observability to aggregate and review your logs, as described in the [logging page](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
