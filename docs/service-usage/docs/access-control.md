---
url: https://docs.cloud.google.com/service-usage/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:11.524436+00:00
---

# Access control with IAM  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access control with IAM

Service Usage uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) to control access to services. This page explains the IAM roles and permissions related to Service Usage and how to use them to control access.

## Resource model

For Service Usage, there are three relevant resources:

  1. The service you are using.

  2. The project from which you are using the service.

  3. The operation or long-running operation returned by certain methods.




Each Service Usage method requires a permission on one or more of these resources.

## IAM permissions

The following table shows the required permissions for each Service Usage API method. You can also find this information in the [API reference](https://docs.cloud.google.com/service-usage/docs/reference/rest).

Method | Required permissions  
---|---  
` [ services.batchEnable ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/batchEnable) ` |  On the project: `serviceusage.services.enable`  
On the services: `servicemanagement.services.bind`  
` [ services.enable ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable) ` |  On the project: `serviceusage.services.enable`  
On the service: `servicemanagement.services.bind`  
` [ services.disable ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/disable) ` |  On the project: `serviceusage.services.disable`  
` [ services.get ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/get) ` |  On the project: `serviceusage.services.get`  
` [ services.list ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/list) ` |  On the project: `serviceusage.services.list`  
` [ services.consumerQuotaMetrics.list ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/list)  
[ services.consumerQuotaMetrics.get ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/get)  
[ services.consumerQuotaMetrics.limits.get ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits/get)  
[ services.consumerQuotaMetrics.limits.consumerOverrides.list ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides/list)  
[ services.consumerQuotaMetrics.limits.adminOverrides.list ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides/list) ` |  On the project: `serviceusage.quota.get`  
On the service: `servicemanagement.services.bind`  
` [ services.consumerQuotaMetrics.limits.consumerOverrides.create ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides/create)  
[ services.consumerQuotaMetrics.limits.consumerOverrides.patch ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides/patch)  
[ services.consumerQuotaMetrics.limits.consumerOverrides.delete ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides/delete)  
[ services.consumerQuotaMetrics.limits.adminOverrides.create ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides/create)  
[ services.consumerQuotaMetrics.limits.adminOverrides.patch ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides/patch)  
[ services.consumerQuotaMetrics.limits.adminOverrides.delete ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.adminOverrides/delete) ` |  On the project: `serviceusage.quota.update`  
On the service: `servicemanagement.services.bind`  
To use a project for quota and billing purposes. For more information, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters).  |  On the project: `serviceusage.services.use`  
  
## IAM roles

With IAM, you give users permission by granting them a role. The following tables list IAM basic and predefined roles, and the permissions related to Service Usage that those roles include.

For more information about roles, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview).

### Basic roles

Name | Title | Permissions  
---|---|---  
`roles/viewer` | Viewer |  serviceusage.services.get  
serviceusage.services.list  
serviceusage.quotas.get  
  
`roles/editor` `roles/owner` |  Editor Owner |  serviceusage.services.get  
serviceusage.services.list  
serviceusage.services.disable  
serviceusage.services.enable  
serviceusage.services.use  
serviceusage.quotas.get  
serviceusage.quotas.update  
  
  
### Predefined roles

Role | Permissions  
---|---  
  
#### API Keys Admin 

(`roles/serviceusage.apiKeysAdmin`) Ability to create, delete, update, get and list API keys for a project.  |  `apikeys.*`

  * `apikeys.keys.create`
  * `apikeys.keys.delete`
  * `apikeys.keys.get`
  * `apikeys.keys.getKeyString`
  * `apikeys.keys.list`
  * `apikeys.keys.lookup`
  * `apikeys.keys.undelete`
  * `apikeys.keys.update`

`orgpolicy.policy.get` `serviceusage.apiKeys.*`

  * `serviceusage.apiKeys.regenerate`
  * `serviceusage.apiKeys.revert`

`serviceusage.operations.get`  
  
#### Service Usage Admin 

(`roles/serviceusage.serviceUsageAdmin`) Ability to enable, disable, and inspect service states, inspect operations, and consume quota and billing for a consumer project.  |  `cloudquotas.*`

  * `cloudquotas.quotas.get`
  * `cloudquotas.quotas.update`

`monitoring.timeSeries.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.contentsecuritypolicy.*`

  * `serviceusage.contentsecuritypolicy.get`
  * `serviceusage.contentsecuritypolicy.update`

`serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.*`

  * `serviceusage.mcppolicy.get`
  * `serviceusage.mcppolicy.update`

`serviceusage.operations.get` `serviceusage.quotas.*`

  * `serviceusage.quotas.get`
  * `serviceusage.quotas.update`

`serviceusage.services.*`

  * `serviceusage.services.disable`
  * `serviceusage.services.enable`
  * `serviceusage.services.get`
  * `serviceusage.services.list`
  * `serviceusage.services.listApis`
  * `serviceusage.services.listDependentServices`
  * `serviceusage.services.use`

`serviceusage.values.test`  
  
#### Service Usage Consumer 

(`roles/serviceusage.serviceUsageConsumer`) Ability to inspect service states and operations, and consume quota and billing for a consumer project.  |  `monitoring.timeSeries.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test`  
  
#### Service Usage Viewer 

(`roles/serviceusage.serviceUsageViewer`) Ability to inspect service states and operations for a consumer project.  |  `monitoring.timeSeries.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### API Keys Viewer 

(`roles/serviceusage.apiKeysViewer`) Ability to get and list API keys for a project.  |  `apikeys.keys.get` `apikeys.keys.getKeyString` `apikeys.keys.list` `apikeys.keys.lookup`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
