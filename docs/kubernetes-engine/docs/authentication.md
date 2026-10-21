---
url: https://docs.cloud.google.com/kubernetes-engine/docs/authentication/
title: Authenticate to GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:43:46.322245+00:00
---

# Authenticate to GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  Authenticate to GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to authenticate to Google Kubernetes Engine programmatically. How you authenticate to Google Kubernetes Engine depends on the interface you use to access the API and the environment where your code is running. 

The GKE API lets you interact with the Google Cloud infrastructure that runs Kubernetes, like your GKE clusters and nodes. 

To interact with _Kubernetes objects_ like Pods and Services, you must authenticate to the Kubernetes API, which is separate to the GKE API and is served by the Kubernetes API server in each cluster. For instructions, see [Authenticate to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).

To access other Google Cloud resources like Cloud Storage buckets from workloads running in GKE, use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). 

For more information about Google Cloud authentication, see the [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

## API access

GKE supports programmatic access. You can access the API in the following ways: 

  * Client libraries
  * Google Cloud CLI
  * REST



### Client libraries

The [GKE client libraries](https://docs.cloud.google.com/kubernetes-engine/docs/reference/libraries) provide high-level language support for authenticating to GKE programmatically. To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

### Google Cloud CLI

When you use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters) to access GKE, you authenticate to Google Cloud as a principal, which provides the credentials used by the gcloud CLI commands. 

If your organization's security policies prevent user accounts from having the required permissions, you can use service account impersonation. 

For more information, see [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate). For more information about using the gcloud CLI with GKE, see [the gcloud CLI reference pages](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters). 

### REST

You can authenticate to [the GKE API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest) by using your [gcloud CLI credentials](https://docs.cloud.google.com/sdk/docs/authenticate) or by using [ Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials). For more information about authentication for REST requests, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest). 

## What's next

  * [Authenticate to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).
  * [Use external identity providers to authenticate to GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc).
  * [Authenticate to Google Cloud APIs from GKE using Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).
  * [Learn about access control in GKE and Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control).
  * [Learn about the GKE API and the Kubernetes API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/api-organization).
  * Learn about [Google Cloud authentication methods](https://docs.cloud.google.com/docs/authentication#auth-decision-tree). 
  * See a list of [authentication use cases](https://docs.cloud.google.com/docs/authentication/use-cases). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
