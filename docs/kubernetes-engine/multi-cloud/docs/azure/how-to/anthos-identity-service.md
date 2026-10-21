---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/anthos-identity-service/
title: Manage identity with GKE Identity Service \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:53.204031+00:00
---

# Manage identity with GKE Identity Service  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/anthos-identity-service/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage identity with GKE Identity Service

GKE on Azure supports [OpenID Connect (OIDC)](https://openid.net/connect/) as an authentication mechanism for interacting with a cluster's Kubernetes API server, using GKE Identity Service. GKE Identity Service is an authentication service that lets you bring your existing identity solutions for authentication to multiple environments. Users can log in to and use your GKE clusters from the command line or from the Google Cloud console, all using your existing identity provider.

For an overview of how GKE Identity Service works, see [Introducing GKE Identity Service](https://docs.cloud.google.com/anthos/identity).

If you already use or want to use Google identities to log in to your GKE clusters, we recommend using the `gcloud containers azure clusters get-credentials` command for authentication. Find out more in [Connect and authenticate to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster#google-identity).

## OpenID Connect authentication

### Before you begin

  1. To use OIDC authentication, users must be able to connect to the cluster's control plane. See [Connect to your cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster#connect-to-vpn).

  2. To authenticate through the Google Cloud console, you must [register each cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) that you want to configure with your project fleet. For GKE on Azure, this is automatic once you have created a node pool.

  3. To allow users to authenticate through the Google Cloud console, ensure that all clusters you want to configure are [registered with your project fleet](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster). For GKE on Azure, this is automatic once you have created a node pool.




### Setup process and options

  1. Register GKE Identity Service as a client with your OIDC provider following the instructions in [Configuring providers for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/provider).

  2. Choose from the following cluster configuration options:

     * Configure your clusters at the fleet-level following the instructions in [Configuring clusters for fleet-level GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/fleet-cluster). With this option, your authentication configuration is centrally managed by Google Cloud.

     * Configure your clusters individually following the instructions in [Configuring clusters for GKE Identity Service with OIDC](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

  3. Set up user access to your clusters, including role-based access control (RBAC), following the instructions in [Setting up user access for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/user-access).




### Accessing clusters

After GKE Identity Service has been set up on a cluster, users can log in to clusters using either the command line or the Google Cloud console.

  * Learn how to log in to registered clusters with your OIDC ID in [Accessing clusters using GKE Identity Service](https://docs.cloud.google.com/anthos/identity/accessing).
  * Learn how to log in to clusters from the Google Cloud console in [Logging in to a cluster from the Google Cloud console](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
