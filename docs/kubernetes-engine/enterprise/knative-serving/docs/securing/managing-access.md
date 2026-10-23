---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/managing-access/
title: Managing access \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:41.587889+00:00
---

# Managing access  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/managing-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Managing access Stay organized with collections  Save and categorize content based on your preferences. 

Knative serving manages access through [Identity and Access Management permissions](https://docs.cloud.google.com/kubernetes-engine/docs/reference/api-permissions) and [Kubernetes role based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

To manage access and privileges for your Knative serving services, you have the following options for managing permissions and authenticating your Knative serving services to Google Cloud APIs:

  * Use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/workload-identity) for your Knative serving services across your fleet.
  * Use [service accounts](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/service-accounts) for specific Knative serving services.
  * Use short lived OAuth2 [access tokens](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/service-identity) if required.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
