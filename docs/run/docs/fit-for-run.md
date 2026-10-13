---
url: https://docs.cloud.google.com/run/docs/fit-for-run/
title: Is my app a good fit for a Cloud Run service? \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:50.677593+00:00
---

# Is my app a good fit for a Cloud Run service?  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/fit-for-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Is my app a good fit for a Cloud Run service? Stay organized with collections  Save and categorize content based on your preferences. 

This page lays out a list of criteria to help you determine if your app is well-suited to be a Cloud Run service.

## Criteria

In order to be a good fit as a Cloud Run service, your app needs to meet _all_ of the following criteria. See the Cloud Run [container contract](https://docs.cloud.google.com/run/docs/reference/container-contract) for more information.

  * Serves requests, streams, or events delivered using HTTP, HTTP/2, WebSockets, or gRPC, or executes to completion.
  * Does not require a _local_ _persistent_ [file system](https://docs.cloud.google.com/run/docs/reference/container-contract#filesystem), but either a local _ephemeral_ file system or a _network_ file system.
  * Is built to handle [multiple instances of the app running simultaneously](https://docs.cloud.google.com/run/docs/about-instance-autoscaling).
  * Does not require more than [8 CPU and 32 GiB of memory per instance](https://docs.cloud.google.com/run/quotas#cloud_run_limits).



If your app meets those criteria, then it's good fit for Cloud Run! To get started, try one of the [Cloud Run quickstarts](https://docs.cloud.google.com/run/docs/quickstarts#build-and-deploy-a-web-service).

If your app doesn't meet all of the criteria, you might want to check out [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine) as a hosting option. For a comparison of Cloud Run and Google Kubernetes Engine, see the [comparison guide](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-and-cloud-run). To assess your application requirements for choosing between Cloud Run and Google Kubernetes Engine based on technical and organizational considerations, see the [Selection guide for managed container runtime environments](https://docs.cloud.google.com/architecture/select-managed-container-runtime-environment).

For automatic GitHub integration and optimized deployments with CDN for server-rendered [Next.js](https://docs.cloud.google.com/run/docs/quickstarts/frameworks/deploy-nextjs-service) or [Angular](https://docs.cloud.google.com/run/docs/quickstarts/frameworks/deploy-angular-ssr-service) apps, consider using [Firebase App Hosting](https://firebase.google.com/docs/app-hosting/product-comparison).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
