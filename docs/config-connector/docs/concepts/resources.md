---
url: https://docs.cloud.google.com/config-connector/docs/concepts/resources/
title: About Config Connector CRDs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:16.742647+00:00
---

# About Config Connector CRDs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/concepts/resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About Config Connector CRDs 

Config Connector includes a collection of [Custom Resource Definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (CRDs). Each CRD lets you configure a Google Cloud resource from Kubernetes. Config Connector also lets you use a number of Kubernetes features for managing Google Cloud resources.

This page introduces you to how Config Connector uses Kubernetes objects and their metadata.

## Kubernetes objects and Config Connector resources

For example, when you create a [Kubernetes Object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) of `kind: SQLInstance`, Config Connector creates a Cloud SQL Instance. This section describes how Config Connector extends object types.

### Spec and Status

Each Config Connector resource is a [Kubernetes object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) with a [`Spec` and a `Status`](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/#object-spec-and-status).

Spec
    The `spec` field contains all the fields that define an object's desired state. The subfields of a `spec` refer to the associated Google Cloud resource. When you change a subfield, the Google Cloud resource's value is eventually consistent with your intended value.
    An example of a writable field is `databaseVersion` in a SQLInstance resource.
    For Config Connector resources with `spec.labels`, labels configured in the `spec.labels` field of the Config Connector resource will be applied to the associated Google Cloud resource. For details, see Managing labels.
Status
    The `status` field is read-only and contains the current state of your object. Config Connector periodically reads information on your Google Cloud resource and updates the `status`. You can check a resource's error messages or readiness by looking at the `Status.Condition`.
    An example read-only `status` field is the `connectionName` of a SQLInstance resource.

## Object metadata

Each Config Connector resource includes a [metadata](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#attaching-metadata-to-objects) field. This section describes how Config Connector uses subfields within metadata.

Name
    The name of a Config Connector resource. It should follow the [naming convention](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) of a Kubernetes object name. It is used by default as the name of the corresponding Google Cloud resource. If the `resourceID` field is supported in the Config Connector resource, you can specify a different name, which follows the naming convention of the Google Cloud resource, for the corresponding Google Cloud resource in the `spec.resourceID` field. For more information, see [Managing resources with the `resourceID` field](https://docs.cloud.google.com/config-connector/docs/how-to/managing-resources-with-resource-ids).
Namespace
    The namespace you create a Config Connector resource in determines the project that contains the Google Cloud resource. For more on namespaces, see [Kubernetes Namespaces and Google Cloud Projects](https://docs.cloud.google.com/config-connector/docs/concepts/namespaces-and-projects).
Labels
    Depending on the resource, labels in the `metadata.labels` field of a Config Connector resource can apply to the associated Google Cloud resource. For details, see Managing labels.
    Config Connector adds a system label named `managed-by-cnrm` with a value of `true` to Google Cloud resources that support labels.
Annotations
    Config Connector can take additional actions on your resources that are not defined in the `spec`. These actions are defined in subfields of `metadata.annotations`. Annotation values _must_ be a string. The types of annotations Config Connector supports are described in [annotations](https://docs.cloud.google.com/config-connector/docs/reference/annotations).

## Managing labels

For Google Cloud resources that support labels, where you define the labels depends on whether the Config Connector resource has a `spec.labels` field:

  * **Resources with a`spec.labels` field**: You must manage labels in `spec.labels`. User-specified labels in this field are applied to the Google Cloud resource.
  * **Resources without a`spec.labels` field**: _All_ labels in `metadata.labels`, including both user-specified labels and system labels, are applied to the Google Cloud resource.



## Folders and hierarchical resources

In addition to managing resources in Google Cloud products, Config Connector supports creating and managing resources within Google Cloud [Folders and Organizations](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders). For more information, see [Namespaces and projects](https://docs.cloud.google.com/config-connector/docs/concepts/namespaces-and-projects).

## Using RBAC for Access Control

Kubernetes [Role Based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) (RBAC) secures your resources. You can control creation of Google Cloud resources by assigning RBAC permissions. For more information, see [Securing access to resources](https://docs.cloud.google.com/config-connector/docs/how-to/securing-access-to-resources).

## Status Condition

Config Connector uses a ready condition in [`status.condition`](https://dev.to/maelvls/what-the-heck-are-kubernetes-conditions-for-4je7) for two purposes:

  * indicating when a resource is ready. When a resource is reconciled and ready, its `status.condition.status` will be set to `True`. To check when a resource is ready, see [Waiting for resources to be ready](https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-your-resources#waiting_for_resources_to_be_ready)
  * displaying additional error or information. The ready condition has `Message` and `Reason` fields which provide additional information on the resource's status.



## Events

Important status changes for Config Connector resources are visible as Kubernetes events. For more information, see [Viewing events](https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-your-resources#viewing_events_for_a_single_resource).

## Declarative configuration and eventual consistency

See [Reconciliation](https://docs.cloud.google.com/config-connector/docs/concepts/reconciliation).

## What's next

  * [Get started with Config Connector](https://docs.cloud.google.com/config-connector/docs/how-to/getting-started)
  * Learn about the [Resources](https://docs.cloud.google.com/config-connector/docs/reference/resources) that Config Connector configures.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
