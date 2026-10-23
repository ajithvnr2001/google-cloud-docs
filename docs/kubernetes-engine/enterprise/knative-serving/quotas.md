---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/quotas/
title: Quotas and Limits \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:17.855608+00:00
---

# Quotas and Limits  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/resources)



Send feedback 

#  Quotas and Limits Stay organized with collections  Save and categorize content based on your preferences. 

This page contains usage quota and limits that apply when using Knative serving.

Knative serving is subject to the [Google Kubernetes Engine quotas and limits](https://docs.cloud.google.com/kubernetes-engine/quotas).

The number of Knative serving resources is limited by the configuration of the cluster as well as other dependencies. The following limits are recommended limits for a properly scaled Kubernetes Engine cluster.

Resource | Description | Limit | Can be increased | Scope  
---|---|---|---|---  
Services | Maximum number of services | 150 | No | per cluster  
Revisions | Maximum number of revisions | 300 | No | per cluster  
Timeout | Maximum time before timeout for [0.16.0-gke.1 and later](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/cluster-versions) | 24 hours | No | per request  
| Maximum time before timeout for [0.15.0-gke.3 and earlier](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/cluster-versions) | 900 seconds | No | per request  
  
Other resource limitations are imposed by the configuration of the Kubernetes Engine cluster that the services are running in. For example, you cannot request more memory than is available in the nodes in the cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
