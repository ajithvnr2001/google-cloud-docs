---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/best-practices/
title: Security best practices in Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:41.014562+00:00
---

# Security best practices in Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Security best practices in Knative serving Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Knative serving and its major components following security best practices.

## Securing Knative serving

Knative serving is based on the open source [Knative](https://knative.dev/) project, and inherits its security posture.

Workloads running on Knative serving share the same network and compute nodes. You should create separate clusters for workloads that don't have mutual trust. Knative serving clusters should not run unrelated workloads like CI/CD infrastructure or databases.

Reasons to create multiple clusters for Knative serving workloads include:

  * Separating development from production environments.
  * Isolating applications owned by different teams.
  * Isolating highly privileged workloads.



Once you've designed your clusters, take the following actions to help secure them:

  * [Restrict access to your cluster](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/managing-access).
  * [Understand the Knative threat model](https://github.com/knative/community/blob/main/working-groups/security/threat-model.md).
  * [Read the Knative security reference if you plan to use community supported tooling](https://knative.dev/docs/reference/security/).



## Securing components

You are responsible for securing components that aren't [part of Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview#components_in_the_default_installation).

### Cloud Service Mesh

Knative serving relies on [Cloud Service Mesh for routing traffic](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview#components_in_the_default_installation).

Use the following guides to help you secure Cloud Service Mesh:

  * [Cloud Service Mesh security overview and features](https://docs.cloud.google.com/service-mesh/docs/security/security-overview).
  * [Cloud Service Mesh security best practices](https://docs.cloud.google.com/service-mesh/docs/security/best-practices).



### Google Kubernetes Engine

Knative serving uses Google Kubernetes Engine (GKE) to schedule workloads. Take the following actions to help you secure your clusters:

  * [Follow the GKE Enterprise security tutorial](https://docs.cloud.google.com/anthos/docs/tutorials/security).
  * [Understand the Google Kubernetes Engine multi-tenancy model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview).
  * [Follow the Google Kubernetes Engine cluster hardening guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).
  * [Understand the Google Kubernetes Engine shared responsibility model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).



## Known vulnerabilities

You should subscribe to the security bulletins for Knative serving dependencies so you can keep up-to-date with known vulnerabilities:

  * [Cloud Service Mesh security bulletins](https://docs.cloud.google.com/service-mesh/docs/security-bulletins).
  * [GKE Enterprise security bulletins](https://docs.cloud.google.com/kubernetes-engine/security-bulletins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
