---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/access-control/
title: Runtime Configurator Access Control Options \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:59.679673+00:00
---

# Runtime Configurator Access Control Options  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/access-control/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Runtime Configurator Access Control Options Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to set access control on your Runtime Configurator resources using [Google Identity and Access Management](https://docs.cloud.google.com/iam). For information about Runtime Configurator, read the [Runtime Configurator Fundamentals](https://docs.cloud.google.com/deployment-manager/runtime-configurator).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand [Google Cloud console](https://support.google.com/cloud/answer/6158853?hl=en&ref_topic=6158848) projects.
  * Understand [Google Identity and Access Management](https://docs.cloud.google.com/iam).



## IAM Roles

Runtime Configurator supports [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for its resources. That means you can grant either the owner, editor, or viewer role to give other users the right amount of access to Runtime Configurator resources. You must grant these permissions on the project level or on the [Config resource level](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/setIamPolicy).

There are no predefined roles for Runtime Configurator.

## Permissions

With IAM, Each API method requires a specific permission in order to be called. Use the table below to determine which permissions are necessary for the desired API method.

Method | Required Permission(s) | Roles that allow you to call this method | [`projects.configs.create`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/create) | `runtimeconfig.configs.create` | 

  * `roles/owner`
  * `roles/editor`

  
---|---|---  
[`projects.configs.delete`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/delete) | `runtimeconfig.configs.delete` | 

  * `roles/owner`
  * `roles/editor`

  
[`projects.configs.get`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/get) | `runtimeconfig.configs.get` | 

  * `roles/owner`
  * `roles/editor`
  * `roles/viewer`

  
[`projects.configs.list`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/list) | `runtimeconfig.configs.list` | 

  * `roles/owner`
  * `roles/editor`
  * `roles/viewer`

  
[`projects.configs.update`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/update) | `runtimeconfig.configs.update` | 

  * `roles/owner`
  * `roles/editor`

  
[`projects.configs.operations.get`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.operations/get) | `runtimeconfig.configs.operations.get` | 

  * `roles/owner`
  * `roles/editor`
  * `roles/viewer`

  
[`projects.configs.variables.create`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/create) | `runtimeconfig.variables.create` | 

  * `roles/owner`
  * `roles/editor`

  
[`projects.configs.variables.delete`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/delete) | `runtimeconfig.variables.delete` | 

  * `roles/owner`
  * `roles/editor`

  
[`projects.configs.variables.get`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/get) | `runtimeconfig.variables.get` | 

  * `roles/owner`
  * `roles/editor`
  * `roles/viewer`

  
[`projects.configs.variables.list`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list) | `runtimeconfig.variables.list` | 

  * `roles/owner`
  * `roles/editor`
  * `roles/viewer`

  
[`projects.configs.variables.update`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/update) | `runtimeconfig.variables.update` | 

  * `roles/owner`
  * `roles/editor`

  
[`projects.configs.variables.watch`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/watch) | `runtimeconfig.variables.watch` | 

  * `roles/owner`
  * `roles/editor`
  * `roles/viewer`

  
[`projects.configs.waiters.create`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/create) | `runtimeconfig.waiters.create` | 

  * `roles/owner`
  * `roles/editor`

  
[`projects.configs.waiters.delete`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/delete) | `runtimeconfig.waiters.delete` | 

  * `roles/owner`
  * `roles/editor`

  
[`projects.configs.waiters.get`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/get) | `runtimeconfig.waiters.get` | 

  * `roles/owner`
  * `roles/editor`
  * `roles/viewer`

  
[`projects.configs.waiters.list`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/list) | `runtimeconfig.waiters.list` | 

  * `roles/owner`
  * `roles/editor`
  * `roles/viewer`

  
  
## What's next

  * Learn about [IAM](https://docs.cloud.google.com/iam).
  * Learn about [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
