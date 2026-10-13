---
url: https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/Overview/
title: Kubernetes API Connector Overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:36.473641+00:00
---

# Kubernetes API Connector Overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/Overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Kubernetes API Connector Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Workflows connector defines the built-in functions that can be used to access other APIs within a workflow.

This page provides an overview of the individual connector. There is no need to import or load connector libraries in a workflow—connectors work out of the box when used in a call step.

**Note:** The Kubernetes API is distinct from the Kubernetes Engine API, which is used to deploy and manage GKE clusters. To call the Kubernetes Engine API in a workflow, use the [Kubernetes Engine API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/Overview).

## Kubernetes API

The Kubernetes API server runs on the control plane of a Google Kubernetes Engine (GKE) cluster, allowing you to interact with objects in the cluster. This connector uses a provided `cluster_id` field and optional `project` and `location` fields to make a request to a cluster's control plane endpoint, even if the cluster is private. Learn more about [using the Kubernetes API connector](https://docs.cloud.google.com/workflows/docs/access-kubernetes-api).

**Note:** If not specified, the `project` and `location` default to that of the workflow. If the GKE cluster is in a different project or region, you must specify it.

For more information about the control plane, see [ GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). For more information about API methods, see [ Kubernetes API reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#delete-job-v1-batch).

Functions  
---  
`[await_job](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/await_job)` | Wait for a Kubernetes Job to complete.  
`[create_job](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/create_job)` | Run a Kubernetes Job in a GKE cluster.  
`[delete_job](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/delete_job)` | Delete a Kubernetes Job.  
`[request](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/request)` | Send an HTTP request to a GKE cluster's control plane.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
