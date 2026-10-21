---
url: https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/overview/
title: Hierarchical service activation overview \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:35.632072+00:00
---

# Hierarchical service activation overview  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Hierarchical service activation overview

**Preview — Hierarchical service activation**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Hierarchical service activation is a Service Usage feature that gives you more control over enabling and disabling services, including [public and private services](https://docs.cloud.google.com/service-usage/docs/public-vs-private), across your organization's [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). Hierarchical service activation supports a declarative policy model that helps you manage service dependencies and many services efficiently.

This document provides an overview of hierarchical service activation. To learn how to use the feature, see [Manage service enablement](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-enablement).

## Inheriting service enablement policies

Hierarchical service activation lets you set service enablement policies at different levels of the Google Cloud resource hierarchy. Policies set at a higher level are inherited by all child resources. You only need to enable a service at the highest common level.

This simplifies managing services across a large number of projects and supports consistent policy enforcement. For example, you can ensure that all projects under a folder or organization adhere to a baseline set of enabled services, and reduce the need for project-level configuration.

You can set service enablement policies at the following levels:

  * Policies set at the **organization** level apply to all folders and projects within the organization.
  * Policies set at the **folder** level apply to all sub-folders and projects within the folder.
  * Policies set at the **project** level inherit from parent folders and the organization.



  
![Policies set at a higher level are inherited by all child
             resources.](https://docs.cloud.google.com/static/service-usage/images/policy-hierarchy-converted.svg)

### Organization policy

While hierarchical service activation lets you enable or disable services, the [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) complements this by providing centralized control over how services can be used. Once a service is enabled, you can use organization policies to enforce constraints on its configuration, such as restricting the physical location of newly created resources or limiting which service accounts can be used. This lets you establish compliance guardrails, ensuring that even after a service is enabled, its usage adheres to your organization's governance requirements.

## Key concepts

To manage service enablement, you should understand these key concepts of the hierarchical service activation declarative policy model.

### Consumer policy

The [`ConsumerPolicy`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/consumerPolicies#resource:-consumerpolicy) is a Service Usage API resource found at each level of the Google Cloud resource hierarchy. This resource, always named `default`, contains the `enableRules` that define which services are enabled. Instead of enabling or disabling a specific service, you can modify the `ConsumerPolicy` resource. When a service name is in its list, the service is enabled at that hierarchy level. This declarative approach simplifies managing service states.

### Effective policy

The `EffectivePolicy` is a Service Usage API resource found at each level of the Google Cloud resource hierarchy. The effective policy shows which services are enabled for a resource. It combines the resource's `ConsumerPolicy` with the policies of all its ancestors. This gives you a complete view of all enabled services and where their enablement originated.

![Effective policy gives you a complete view of all enabled
             services and where their enablement originated.](https://docs.cloud.google.com/static/service-usage/images/effective-policy-converted.svg)

### Service dependencies

Many Google Cloud services need other services to function. When you enable a service using hierarchical service activation, its required dependencies are automatically added to the `ConsumerPolicy`. A _service dependency group_ contains these relied-on services, which you can inspect to better understand and manage them.

## Transitioning from a previous Service Usage version

Hierarchical service activation works with previous Service Usage versions. You can use hierarchical service activation features, like enabling services at the folder or organization level, without changing existing project-level settings. Services enabled at the project level will continue to work. The hierarchical model adds to these settings. A project's effective policy will be the result of policies set at the project level combined with policies inherited from folders and the organization.

For example, if `compute.googleapis.com` was enabled at the project level using a previous Service Usage version, the service remains enabled. It is unaffected by any subsequent enablements made at the folder or organization level using hierarchical service activation. Conversely, if you enable `compute.googleapis.com` at the folder level, the service is effectively enabled for all projects in that folder.

## What's next

  * To enable and disable services, see [Manage service enablement](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-enablement).
  * To manage policies, see [Manage consumer policies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/manage-consumer-policies).
  * To inspect service dependencies, see [List service dependencies](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/list-dependencies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
