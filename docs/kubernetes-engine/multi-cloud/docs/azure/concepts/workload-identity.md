---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/workload-identity/
title: Workload identity overview \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:56.342577+00:00
---

# Workload identity overview  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/workload-identity/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Workload identity overview

_Workload identity_ enables you to assign distinct, fine-grained identities and authorization for each application in your cluster. Workload identity is the recommended way for applications running within GKE on Azure to access Azure and Google Cloud services.

All GKE clusters have workload identity enabled.

## Kubernetes service accounts

Workload identity implements _identity federation_ , or delegating trust or roles to an external provider. Each cluster has a built-in OpenID Connect (OIDC) provider. When a Pod runs in the cluster, it runs using a [Kubernetes service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/). The Pod can be configured to obtain a token with short-lived credentials for its Kubernetes service account using a [Bound Service Account Token Volume](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume).

## OpenID Connect providers

Each cluster can act as an [OpenID Connect (OIDC)](https://openid.net/connect/) provider. With this provider, you can provide Kubernetes service account credentials to services that support identity federation using OIDC.

This provider's issuer URI also serves as an OIDC discovery endpoint. Services can use this discovery endpoint to obtain the JSON Web Key Set (JWKS), which provides public key information that allows them to verify Kubernetes service account credentials.

## Google Cloud IAM identity pools and providers

Google Cloud IAM supports [identity federation using OIDC](https://cloud.google.com/iam/docs/workload-identity-federation). All GKE clusters are configured as identity providers in the workload identity pool `PROJECT_ID.svc.id.goog`.

To get the name of your workload identity pool and providers, see [Use workload identity with Google Cloud](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-workload-identity-google#determine_the_workload_identity_pool_for_your_cluster).

## Alternatives to workload identity

There are alternative methods to access services from GKE on Azure. We don't recommended the following methods due to complications.

  1. Export credentials and store them as Kubernetes Secrets. In this case, you must rotate stored credentials manually in both Azure IAM and in your cluster. Additionally, if an attacker steals credentials, they can exploit them.

  2. Attach credentials to the node pools's underlying instances. In this case, all workloads running on the same node share the credentials, which can result in a greater set of permissions than workloads might need. To block access to an instance's permissions, GKE clusters blocks access from a Pod to the instance metadata service.




## What's next

  * [Using workload identity with Google Cloud services](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/use-workload-identity-google)
  * Learn more about [Workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
