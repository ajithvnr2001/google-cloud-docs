---
url: https://docs.cloud.google.com/config-connector/docs/how-to/configure-iam-permissions/
title: Access control with IAM \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:18.527321+00:00
---

# Access control with IAM  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/configure-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access control with IAM

This document describes how to use Identity and Access Management to control how Config Connector can create and manage Google Cloud resources.

To install Config Connector, you authenticate by creating an IAM service account and then using Workload Identity Federation for GKE for GKE to bind the IAM service accounts with the Kubernetes service accounts. IAM lets Config Connector take action on specific resources. By limiting the permissions assigned to your service accounts, you have greater control over what kinds of resources Config Connector can create.

You can choose to manage resources with a single service account or multiple service accounts.

**Note:** Your organization administrator might [disable the creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts) of service accounts. If this setting is applied, coordinate with your organization administrator before installing Config Connector.

## Single service account

When you install Config Connector with the GKE add-on or manual installation, you can set cluster mode in your `ConfigConnector` [CustomResource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). With cluster mode, you can use a single IAM service account to create and manage resources, even if you are using Config Connector to manage multiple projects.

The following diagram shows you how this mode works, where the same service account, which is called `my-service-account`, manages two projects:

![Config Connector using one service account to manage multiple projects](https://docs.cloud.google.com/static/config-connector/docs/images/cc-project-types.svg)

## Multiple service accounts

You can use multiple service accounts by setting namespaced mode in your `ConfigConnector` [CustomResource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). Namespaced mode lets you divide permissions based on the respective concerns of different IAM service accounts and isolate permissions among different Kubernetes namespaces since you can associate a different service account for each namespace.

Choose namespaced mode if you:

  * Want to isolate IAM permissions at Kubernetes namespace level.
  * Expect to manage a large number of Google Cloud resources from multiple Google Cloud projects on a single cluster.



As an example, you create one IAM service account for each project, organize resources from each project in the same Kubernetes namespace, and then bind the corresponding IAM service account to the Kubernetes namespace. This lets you separate IAM permissions for each project so that each project has a distinct, unrelated set of permissions.

The following diagram shows you an overview of how namespaced mode works, where each of project is managed by a different service account. Project 1 is managed by `my-service-account`, and Project 2 is managed by `another-service-account`:

![Config Connector using two different service accounts to manage multiple projects ](https://docs.cloud.google.com/static/config-connector/docs/images/cc-project-types-namespaced.svg)

In namespaced mode, each IAM service account is bound to a namespace by default. When you create resources within that namespace, Config Connector uses this service account to create Google Cloud resources. There is a dedicated Config Connector `cnrm-controller-manager` pod for each namespace which impersonates the IAM service account associated with the namespace.

To learn how to configure namespaced mode, see [Installing Config Connector using a namespaced mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced).

## What's next

  * Learn how to [organize your resources by folder, project, or organization](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
