---
url: https://docs.cloud.google.com/saas-runtime/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:56:16.091808+00:00
---

# Access control with IAM  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/saas-runtime/docs/access-control/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes App Lifecycle Manager roles and permissions.

To use App Lifecycle Manager, you need to ensure you have the required service accounts. For these service accounts, you need to grant the required permissions. For more details about service accounts and App Lifecycle Manager, see [App Lifecycle Manager service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#saas-service-accounts). For details about service accounts, see [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview).

To deploy or view the Google Cloud resources defined in the Terraform configuration, you need to grant the service account permissions that are specific to these resources. These permissions are in addition to the permissions required to use App Lifecycle Manager. For a list of all roles and the permissions they contain, see [Identity and Access Management basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

A service account is not required to view App Lifecycle Manager deployments, revisions, and IAM policies.

## Predefined App Lifecycle Manager roles

IAM provides [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) that grant access to specific Google Cloud resources and prevent unauthorized access to other resources.

The following table lists the App Lifecycle Manager IAM roles and the permissions that they include:

Role | Description | Permissions  
---|---|---  
App Lifecycle Manager Admin (`roles/saasservicemgmt.admin`) | Full access to all App Lifecycle Manager resources. | `saasservicemgmt.rollouts.create`  
`saasservicemgmt.rollouts.update`  
`saasservicemgmt.rollouts.delete`  
`saasservicemgmt.rolloutKinds.create`  
`saasservicemgmt.rolloutKinds.update`  
`saasservicemgmt.rolloutKinds.delete`  
`saasservicemgmt.releases.create`  
`saasservicemgmt.releases.update`  
`saasservicemgmt.releases.delete`  
`saasservicemgmt.units.create`  
`saasservicemgmt.units.update`  
`saasservicemgmt.units.delete`  
`saasservicemgmt.unitKinds.create`  
`saasservicemgmt.unitKinds.update`  
`saasservicemgmt.unitKinds.delete`  
`saasservicemgmt.unitOperations.create`  
`saasservicemgmt.unitOperations.update`  
`saasservicemgmt.unitOperations.delete`  
`saasservicemgmt.tenants.create`  
`saasservicemgmt.tenants.update`  
`saasservicemgmt.tenants.delete`  
`saasservicemgmt.saas.create`  
`saasservicemgmt.saas.update`  
`saasservicemgmt.saas.delete`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`saasservicemgmt.locations.list`  
`saasservicemgmt.locations.get`  
`saasservicemgmt.rollouts.list`  
`saasservicemgmt.rollouts.get`  
`saasservicemgmt.rolloutKinds.list`  
`saasservicemgmt.rolloutKinds.get`  
`saasservicemgmt.releases.list`  
`saasservicemgmt.releases.get`  
`saasservicemgmt.units.list`  
`saasservicemgmt.units.get`  
`saasservicemgmt.unitKinds.list`  
`saasservicemgmt.unitKinds.get`  
`saasservicemgmt.unitOperations.list`  
`saasservicemgmt.unitOperations.get`  
`saasservicemgmt.tenants.list`  
`saasservicemgmt.tenants.get`  
`saasservicemgmt.saas.list`  
`saasservicemgmt.saas.get`  
App Lifecycle Manager Viewer (`roles/saasservicemgmt.viewer`) | Read App Lifecycle Manager resources: releases, rollouts, rolloutKinds, units, unitKinds, unitOperations, saas, and tenants. | `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`saasservicemgmt.locations.list`  
`saasservicemgmt.locations.get`  
`saasservicemgmt.rollouts.list`  
`saasservicemgmt.rollouts.get`  
`saasservicemgmt.rolloutKinds.list`  
`saasservicemgmt.rolloutKinds.get`  
`saasservicemgmt.releases.list`  
`saasservicemgmt.releases.get`  
`saasservicemgmt.units.list`  
`saasservicemgmt.units.get`  
`saasservicemgmt.unitKinds.list`  
`saasservicemgmt.unitKinds.get`  
`saasservicemgmt.unitOperations.list`  
`saasservicemgmt.unitOperations.get`  
`saasservicemgmt.tenants.list`  
`saasservicemgmt.tenants.get`  
`saasservicemgmt.saas.list`  
`saasservicemgmt.saas.get`  
  
## Permissions

Permissions that the caller must have to call each method is listed in the [REST API reference](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest).

## What's next

  * Learn about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [using conditions in IAM](https://docs.cloud.google.com/deploy/docs/securing/iam#about_iam_conditions)
  * Find out more about [App Lifecycle Manager service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#saas-service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
