---
url: https://docs.cloud.google.com/app-lifecycle-manager/glossary/
title: App Lifecycle Manager glossary \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:32.512886+00:00
---

# App Lifecycle Manager glossary  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/glossary/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  App Lifecycle Manager glossary Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## App offering

An _app offering_ represents a specific software as a service (SaaS) product offering, including details, configurations, and deployment regions that may be shared across multiple instances or deployments of that product within a company's larger SaaS portfolio.

## Unit

A _unit_ is an instantiation of a unit kind. For example, if you have a unit kind for the infrastructure of your SaaS application, then the related unit is the infrastructure wherein the application runs. 

## Unit kind

A _unit kind_ defines a type of managed component within your service (for example, a Kubernetes cluster, or an application instance). All units of a given unit kind are typically updated together (via a rollout). Unit kinds enable you to define separate rollout content and cadences for distinct groupings within your App offering.

## Release

A _release_ represents a specific, deployable snapshot of a unit kind. Releases contain the artifacts and configurations to create or update a unit. Releases include a pointer to an artifact encapsulating the actual deployment details (including the Terraform configuration). When you want to update a unit, you target a specific release in a rollout.

## Rollout

A _rollout_ is the process of updating units with a new release. A rollout process follows the rules defined in the rollout kind.

## Rollout kind

A _rollout kind_ functions as a description of how to deploy new releases to units. For example, you can set the rollout to progress by specific increments in the regions where the units are available.

## Tenant

A _tenant_ represents a dedicated instance of the App offering. It acts as a container for all the units (containing applications, databases, and infrastructure components) that you provision and manage.

## Feature flag

_Feature flags_ toggle the state or other binary behaviors of a feature. Feature flags allow you to change feature availability or feature behavior without redeploying or restarting the application.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
