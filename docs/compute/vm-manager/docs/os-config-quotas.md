---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas/
title: OS Config quotas \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:49.225340+00:00
---

# OS Config quotas  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/vm-manager/docs/resources)



Send feedback 

#  OS Config quotas Stay organized with collections  Save and categorize content based on your preferences. 

## Rate quotas

When you use the [Google Cloud CLI](https://docs.cloud.google.com/sdk) or the [Google Cloud console](https://console.cloud.google.com/), you're also making requests to the API, and these requests count towards your rate quota. If you use service accounts to access the API, that also counts towards your quota.

Quotas are enforced at intervals of every **60 seconds**. That means that if you reach a specific limit anytime within 60 seconds, you need to wait for your quota bucket to refresh to make more requests.

### Per user quotas

**Quota group** | **Detail** | **Default quota**  
---|---|---  
Read requests | 

  * **Description** : Quota for `*.get`, `*.describe`, and `*.list` methods.
  * **Metric** : `osconfig.googleapis.com/read_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Fread_requests)

| 60 requests per user per minute  
Write requests | 

  * **Description** : Quota for `*.create`, `*.update`, `*.exec`, `*.cancel`, and `*.delete` methods.
  * **Metric** : `osconfig.googleapis.com/write_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Fwrite_requests)

| 60 requests per user per minute  
Lookup requests [**(Legacy beta)**](https://docs.cloud.google.com/compute/docs/os-config-management) | 

  * **Description** : Quota for `*.lookupEffectiveGuestPolicy` method.
  * **Metric** : `osconfig.googleapis.com/lookup_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Flookup_requests)

| 600 requests per user per minute  
  
### Per region quotas

**Quota group** | **Detail** | **Default quota**  
---|---|---  
Read requests | 

  * **Description** : Quota for `*.get`, `*.describe`, and `*.list` methods.
  * **Metric** : `osconfig.googleapis.com/regional_zonal_read_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Fregional_zonal_read_requests)

| 100 requests per region per minute  
Write requests | 

  * **Description** : Quota for `*.create`, `*.update`, `*.patch`, `*.cancel`, and `*.delete` methods.
  * **Metric** : `osconfig.googleapis.com/regional_zonal_write_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Fregional_zonal_write_requests)

| 60 requests per region per minute  
  
## Allocation quotas

Allocation quotas are the maximum number of resources you can create of that resource type. OS Config resources include the following: patch deployments, OS policy assignments, and guest policies.

The following quotas don't reset over time and instead are released when you release the resource.

**Resource** | **Detail** | **Default quota**  
---|---|---  
Patch jobs | 

  * **Description** : Quota for the number of patch jobs that can be created in a project.
  * **Metric** : `osconfig.googleapis.com/patch_deployment_count` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Fpatch_deployment_count)

| 100 patch jobs per project  
OS policy assignments | 

  * **Description** : Quota for the number of OS policy assignments that can be created for each zone in a project.
  * **Metric** : `osconfig.googleapis.com/os_policy_assignment_count` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Fos_policy_assignment_count)

| 20 OS policy assignments per zone per project  
policy orchestrators | 

  * **Description** : Quota for the number of OS policy orchestrators that can be created for each project.
  * **Metric** : `osconfig.googleapis.com/policy_orchestrator_count_per_project` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Fpolicy_orchestrator_count_per_project)

| 20 policy orchestrators per project  
Folder and org policy orchestrators | 

  * **Description** : Quota for the number of OS policy orchestrators that can be created in a folder for each organization.
  * **Metric** : `osconfig.googleapis.com/folder_and_org_policy_orchestrator_count` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Ffolder_and_org_policy_orchestrator_count)

| 50 policy orchestrators per organization  
Guest policies [**(Legacy beta)**](https://docs.cloud.google.com/compute/docs/os-config-management) | 

  * **Description** : Quota for the number of guest policies that can be created in a project.
  * **Metric** : `osconfig.googleapis.com/guest_policy_count` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=osconfig.googleapis.com%2Fguest_policy_count)

| 100 guest policies per project  
  
## Manage request and allocation quotas

To manage the request and allocation quotas for your project, do the following:

  * Follow the best practices for [preserving API rate limits](https://docs.cloud.google.com/compute/docs/api/best-practices#preserve-API-rate-limits).
  * Use the Google Cloud console to view and edit rate quotas:

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?service=osconfig.googleapis.com)

    * If you want to lower rate quotas, see [Capping usage](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage).
    * If you need higher rate quotas than the default maximum, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). In your request, add information showing the consumption rate in your environment. These include [VM Manager audit logs](https://docs.cloud.google.com/compute/docs/osconfig/audit-logging) or other error messages stating that the rate limit is exceeded. It's also useful to include information such as future growth plans, region or zone spread, and any additional requirements or dependencies.



## What's next?

  * Learn more about [VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs)
  * Learn more about [Service Quota Model](https://docs.cloud.google.com/service-usage/docs/service-quota-model).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
