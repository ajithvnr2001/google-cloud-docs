---
url: https://docs.cloud.google.com/anthos/run/docs/console/
title: Knative serving in the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:05.445513+00:00
---

# Knative serving in the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/run/docs/console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Knative serving in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

Knative serving is Google's managed and fully supported [Knative](https://knative.dev/) offering. Knative serving abstracts away the complexity of Kubernetes, making it easy to build and deploy your serverless workloads across hybrid and multi-cloud environments.

## Accessing Knative serving

The Knative serving button is located under **Kubernetes Engine** > **Applications**. All of your Knative serving services are listed on this page.

In the Google Cloud console, go to the **Knative serving** page.

[Go to Knative serving](https://console.cloud.google.com/projectselector2/kubernetes/run)

## What's new and changed

### Product specific support

Knative serving is now available as a separate experience from the managed [Cloud Run](https://cloud.google.com/run/) product. The new Knative serving page supports only your Knative serving services. Any of your services for the managed Cloud Run product continue to be available from the [Cloud Run page](https://docs.cloud.google.com/run/docs/managing/services) in the Google Cloud console.

### Cluster requirements

The prerequisites for Knative serving have changed to require that you must first create and configure your GKE clusters. You are no longer able to create clusters from within the Knative serving page in the Google Cloud console.

For more information about supported clusters and configuration requirements, see [GKE clusters](https://docs.cloud.google.com/anthos/clusters/docs).

Note that [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh) will be the recommended and fully supported service mesh for your Knative serving services. Cloud Service Mesh requires that your clusters use a machine type that has at least 4 vCPUs, such as `e2-standard-4`. If you need to change your cluster's machine type, see [Migrating workloads to different machine types](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrating-node-pool).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
