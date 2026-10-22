---
url: https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview/
title: Organizing your resources \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:47.310749+00:00
---

# Organizing your resources  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Organizing your resources

## Overview

Config Connector can create and manage Google Cloud resources at the project-level, folder-level, or organization-level scope. Config Connector needs to determine:

  * Whether to create the resource at the project-level, folder-level, or organization-level.
  * Which project, folder, or organization to use.



As a result, Config Connector first checks for a scope-defining field in your resource spec, if not found, then checks for a scope-defining annotation. Most Google Cloud resources can be created at only the project-level.

Once a resource is successfully created, regardless of how the scope is set, the field or annotation becomes immutable. To change the scope of a resource, you must delete the current resource and create a new resource in a different project, folder, or organization scope.

### Scope-defining field

A scope-defining resource spec field is part of the resource's spec and can be set only in the resource's configuration. It follows the naming convention of SCOPERef. Depending on the resource type, the schema of the spec may contain at least one of the following fields:

  * `projectRef`
  * `folderRef`
  * `organizationRef`



### Scope-defining annotation

You can define a scope-defining annotation in the resource's configuration or in the Kubernetes namespace which contains the resource. There are three types of scope-defining annotations depending on the resource type:

  * `cnrm.cloud.google.com/project-id`
  * `cnrm.cloud.google.com/folder-id`
  * `cnrm.cloud.google.com/organization-id`



Most Config Connector resources support scope-defining fields. We recommend fields over scope-defining annotations because a scope-defining field makes the resource spec more self-contained and enables the creation of a scope and its contained resources in one step. For resources that do not support scope-defining fields, you can either supply the scope-defining annotation in their configuration, or default the annotation for all resources in a particular namespace by annotating the namespace. The namespace annotation is ignored if the resource has the scope-defining annotation directly in its configuration.

**Warning:** Using the namespace annotation is a convenient way to specify default scope for all resources under the same namespace, but it may cause performance issues when managing a large number of resources under one Kubernetes namespace.

## Exceptions

If the scope concept does not apply to a Config Connector resource, you do not need to specify a project, folder, or organization scope. Specifically if a resource listed in the [resource reference page](https://docs.cloud.google.com/config-connector/docs/reference/overview) does not have a scope-defining field or a scope-defining annotation, you do not need to add a scope.

Some resources, like [BillingBudgetsBudget](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/billingbudgets/billingbudgetsbudget) are bound to a Google Cloud billing account, and requires you to specify the billing account information instead.

IAM resources, including [IAMPolicy](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampolicy), [IAMPartialPolicy](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampartialpolicy), [IAMPolicyMember](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampolicymember) and [IAMAuditConfig](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iamauditconfig) do not require you to provide a scope. Instead, these resources are attached to another Google Cloud resource through the `spec.resourceRef` field. This other Google Cloud resource can be a `PubSubTopic`, a `SpannerInstance` or even a "scope" like project, folder, organization, which are themselves modeled as a Google Cloud resource.

## What's next

See how to apply the following types of scopes:

  * [Project-scoped resources](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/project-scoped-resources)

  * [Folder-scoped resources](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/folder-scoped-resources)

  * [Organization-scoped resources](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/organization-scoped-resources)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
