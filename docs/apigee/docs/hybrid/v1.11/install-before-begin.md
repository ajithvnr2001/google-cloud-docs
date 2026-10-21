---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-before-begin/
title: Part 2: Hybrid runtime setup \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:19:11.525931+00:00
---

# Part 2: Hybrid runtime setup  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-before-begin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Part 2: Hybrid runtime setup Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-before-begin.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-before-begin.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-before-begin.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-before-begin.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-before-begin.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-before-begin.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-before-begin.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-before-begin.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-before-begin.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-before-begin.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-before-begin.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-before-begin.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-before-begin.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-before-begin.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-before-begin.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-before-begin.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-before-begin.html)



##  Supported platforms 

You can install Apigee hybrid on a number of platforms, including Anthos on premises, AWS, Bare Metal, EKS, Google Kubernetes Engine (GKE), OpenShift, and others. For a list of supported platforms see [Apigee hybrid: supported platforms](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms). 

##  Permissions 

Each supported platform has its own permission requirements for creating a cluster. As cluster owner, you can proceed to install the Apigee-specific components (including cert-manager and the Apigee runtime) into the cluster. However, if you want to delegate to another user the installation of the runtime components into the cluster, you can manage the necessary permissions through Kubernetes [authn-authz](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

For a complete list of Kubernetes resources and custom resources that are used by Apigee installations, see [Kubernetes and custom resources used by Apigee](https://docs.cloud.google.com/apigee/docs/hybrid/kubernetes-resources). 

## Prerequisites

This section describes tasks you must accomplish before you begin the runtime plane quickstart install.

Complete the tasks in [Part 1: Project and org setup](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-overview) before you begin the runtime installation:  
---  
Meet the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/prerequisites) having a Google Cloud project, a billing account, and the `gcloud` CLI installed.  
Enable the APIs for Google Cloud services in [Step 1: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-enableapi).  
Create an Apigee organization in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-provision).  
Create an Apigee environment and environment group in [Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-add-environment).  
Select the installation and management tool you plan to use for Apigee hybrid, [Helm](https://helm.sh/docs/) or [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cli-reference).  
Apigee recommends Helm for new installations.  
**Note about VPC Service Controls:** If you plan to enable Google Cloud [ Virtual Private Cloud (VPC) Service Controls](https://cloud.google.com/vpc-service-controls) with your Apigee hybrid installation, see [Using VPC Service Controls with Apigee and Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) for instructions before you proceed.[Next step: Create a cluster with Helm](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-cluster) | [Next step: Create a cluster with apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-cluster)  
---|---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
