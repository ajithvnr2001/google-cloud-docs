---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/command-line/
title: Work with fleet clusters from the command line \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:26.222422+00:00
---

# Work with fleet clusters from the command line  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/command-line/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Work with fleet clusters from the command line Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud provides several options for authenticating to fleet clusters from the command line. These let developers and other cluster users connect to and run commands against registered clusters in a simple, consistent, and secured way, whether the clusters are on Google Cloud, other public clouds, or on premises.

For details of how to work with fleet clusters from the Google Cloud console, see [Logging in to a cluster from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console).

## Authenticate with Google Cloud

All GKE clusters on Google Cloud are configured to accept Google Cloud user and service account identities. If your fleet contains clusters in multiple environments, you can configure the [Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway) so that users and service accounts can also authenticate to any registered cluster using their Google Cloud ID.

Learn more in the following guides:

  * [Configuring cluster access for `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
  * [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway)
  * [Using the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using).



## Authenticate with third-party providers

If you want to use your existing third-party identity provider to authenticate to your fleet clusters, GKE Identity Service is an authentication service that lets you bring your existing identity solutions to multiple Anthos environments. It supports all [OpenID Connect (OIDC)](https://openid.net/connect/) providers such as Okta and Microsoft AD FS, as well as preview support for LDAP providers in some environments. If configured, you can also use some third-party providers with the [Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-third-party).

Learn more in the following guides:

  * [Introducing GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity)
  * [Accessing clusters with GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing)
  * [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway)
  * [Using the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
