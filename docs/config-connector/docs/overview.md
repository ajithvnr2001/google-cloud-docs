---
url: https://docs.cloud.google.com/config-connector/docs/overview/
title: Config Connector overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:22:16.295276+00:00
---

# Config Connector overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Config Connector overview

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Config Connector is an [open source](https://github.com/GoogleCloudPlatform/k8s-config-connector) Kubernetes add-on that lets you manage Google Cloud resources through Kubernetes.

Many cloud-native development teams work with a mix of configuration systems, APIs, and tools to manage their infrastructure. This mix is often difficult to understand, leading to reduced velocity and expensive mistakes. Config Connector provides a method to configure many [Google Cloud services and resources](https://docs.cloud.google.com/config-connector/docs/reference/resources) using Kubernetes tooling and APIs.

With Config Connector, your environments can use Kubernetes-managed [Resources](https://docs.cloud.google.com/config-connector/docs/concepts/resources#managing_resources_with_kubernetes_objects) including:

  * RBAC for access control.
  * Events for visibility.
  * Single source of configuration and desired state management for reduced complexity.
  * Eventual consistency through loosely-coupled dependencies.



You can manage your Google Cloud infrastructure the same way you manage your Kubernetes applications, reducing the complexity and cognitive load for developers.

## How Config Connector works

Config Connector provides a collection of Kubernetes [Custom Resource Definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (CRDs) and controllers. The Config Connector CRDs allow Kubernetes to create and manage Google Cloud resources when you configure and apply Objects to your cluster.

For Config Connector CRDs to function correctly, Config Connector deploys Pods to your nodes that have elevated RBAC permissions, such as the ability to create, delete, get, and list CustomResourceDefinitions (CRDs). These permissions are required for Config Connector to create and reconcile Kubernetes resources.

When you configure and apply objects to your cluster, Config Connector reconciles the configured state against Google Cloud APIs asynchronously. Reconciliation executes using the identity of the Config Connector IAM service account, _not_ the identity of the human user or service account that submitted the manifest to Kubernetes.

The ability to create Kubernetes resources in a Config Connector namespace (in namespaced mode) or cluster (in cluster mode) grants authorization to change cloud resources by using Config Connector's identity. This mechanism is similar to CI/CD pipelines, where the ability to merge code into a repository also allows that code to deploy by using the pipeline's identity. The security of the system depends on tightly controlling who can create those objects, such as by having a Kubernetes controller apply Config Connector resources from a trusted code repository.

This approach delegates authority for broad cloud access management to Config Connector, while restricting individual developer access through repository source control. This is more secure than granting every developer access to modify cloud resources directly.

To get started, [install Config Connector](https://docs.cloud.google.com/config-connector/docs/concepts/installation-types) and [create your first resource](https://docs.cloud.google.com/config-connector/docs/how-to/getting-started). Config Connector's [controllers](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-controllers) eventually reconcile your environment with your desired state.

### Customizing Config Connector's behavior

Config Connector provides additional features beyond creating resources. For example, you can manage [existing Google Cloud resources](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#acquiring_an_existing_resource), and use [Kubernetes Secrets](https://docs.cloud.google.com/config-connector/docs/how-to/secrets) to provide sensitive data, such as passwords, to your resources. For more information, see the list of [how-to guides](https://docs.cloud.google.com/config-connector/docs/how-to).

To learn more about how Config Connector uses custom resources, see [About Config Connector CRDs](https://docs.cloud.google.com/config-connector/docs/concepts/resources). For the full list of Google Cloud resources supported by Config Connector, see the [Config Connector reference documentation](https://docs.cloud.google.com/config-connector/docs/reference/resources).

## What's next

  * [Install Config Connector](https://docs.cloud.google.com/config-connector/docs/concepts/installation-types).
  * [Get started](https://docs.cloud.google.com/config-connector/docs/how-to/getting-started) by creating your first resource.
  * Explore Config Connector [source code](https://github.com/GoogleCloudPlatform/k8s-config-connector). Config Connector is fully open sourced on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
