---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/workbench/workbench-api-overview/
title: Vertex AI Workbench API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:20.981850+00:00
---

# Vertex AI Workbench API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/workbench/workbench-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Vertex AI Workbench API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Vertex AI Workbench application programming interface (API) is a programmatic interface to the Vertex AI Workbench service. Google builds the control-plane APIs on top of Kubernetes, using the Kubernetes Resource Model (KRM). The control plane performs resource management for services such as Notebook creation and deletion.

## About Vertex AI Workbench API

Vertex AI Workbench service currently supports only the Kubernetes-based (KRM) API. Refer to the KRM page under Vertex AI Workbench section for the User Interface (UI) equivalent functionality.

**Note:** Currently, the Vertex AI Workbench KRM API doesn't support any functionality beyond the Vertex AI Workbench service provided in the UI. Therefore, if you choose to perform a KRM API action beyond the UI capability, there is no security guarantee or product support provided. If there is a need for supporting certain functionality on the UI, file a feature request to the Google Distributed Cloud (GDC) air-gapped product team.

## Service endpoint

The following URL is the API endpoint for the Vertex AI Workbench service KRM API:

  * https://ORG_ADMIN_CLUSTER_KUBERNETES_API_ENDPOINT/apis/aiplatform.gdc.goog/v1



Replace ORG_ADMIN_CLUSTER_KUBERNETES_API_ENDPOINT with the API endpoint of your organization admin Kubernetes cluster.

## Discovery document

Use the `kubectl proxy --port=8001` command to open a proxy to the API server on your local machine. From there, you can access the discovery document at the following URL:

  * http://127.0.0.1:8001/apis/aiplatform.gdc.goog/v1



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
