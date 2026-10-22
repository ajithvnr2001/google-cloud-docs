---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/cluster-security/
title: Security overview \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:21.714070+00:00
---

# Security overview  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/cluster-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/overview)



Send feedback 

#  Security overview Stay organized with collections  Save and categorize content based on your preferences. 

When an application sends a request to an attached cluster through Connect, it must pass through three security checkpoints.

  1. The request first goes to the Google Cloud API _connectgateway.googleapis.com_ API, which verifies that the caller is authorized to use that API.

  2. If authorized, the request is then passed to the connect gateway for Google Cloud IAM authorization.

  3. If this succeeds, the request is passed to the connect gateway to the cluster's kube-api server for RBAC authorization.




If all of these checks are successful, then the cluster's kube-apiserver will serve the request.

See [Grant IAM roles to users](https://docs.cloud.google.com/anthos/multicluster-management/gateway/setup#grant_iam_roles_to_users) for instructions on granting IAM roles to cluster users with the Connect Gateway.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
