---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/artifactregistry/overview/
title: Artifact Registry API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:16.495762+00:00
---

# Artifact Registry API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/artifactregistry/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Artifact Registry API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Artifact Registry API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM). This API is used to view and manage Harbor container registry instances.

## Service endpoint and discovery document

The API endpoint for the Artifact Registry API is: `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/artifactregistry.gdc.goog/v1` where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.

Using the `kubectl proxy` command, you can access that URL in your browser or with a tool such as `curl` to get the discovery document for the Artifact Registry API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. After that command is running, you can access the document at the following URL: `http://127.0.0.1:8001/apis/artifactregistry.gdc.goog/v1`.

## Example Harbor container registry instance

The following is an example of a Harbor container registry instance:
    
    
    apiVersion: artifactregistry.gdc.goog/v1
    kind: HarborInstance
    metadata:
      name: myinstance
      namespace: tenant-project-namespace
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
