---
url: https://docs.cloud.google.com/compute/docs/oslogin/os-login-quotas/
title: OS Login Quotas \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:11.314189+00:00
---

# OS Login Quotas  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/os-login-quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  OS Login Quotas Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the quotas for OS Login, which define the maximum number of requests that your project can make to the [OS Login API](https://docs.cloud.google.com/compute/docs/oslogin/rest).

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

## Rate quotas

Any requests you make to the OS Login API count towards your OS Login quota. OS Login usage through the Google Cloud console or Google Cloud CLI also counts towards your quota because these services use the OS Login API. OS Login quotas apply to your entire project and are separate for each project.

Each quota group is counted separately, so you can achieve the maximum limit in each group simultaneously. Quotas are enforced at intervals of every 60 seconds. If you reach a group's enforced maximum anytime within 60 seconds, you need to wait for the next interval for your quota to refresh before you can make more requests in that group.

### Per user quotas

Quota group | Details | Default quota  
---|---|---  
Read requests | 

  * **Description** : Quota for `*.get`, and `*.getLoginProfile` methods.
  * **Metric** : `oslogin.googleapis.com/read_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=oslogin.googleapis.com%2Fread_requests)

| 60 requests per user per minute  
Write requests | 

  * **Description** : Limit for `*.create`, `*.patch`, `*.delete` and `*.importSshPublicKey` methods.
  * **Metric** : `oslogin.googleapis.com/write_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=oslogin.googleapis.com%2Fwrite_requests)

| 60 requests per user per minute  
Start session requests | 

  * **Description** : Limit for initiating OS Login two-factor authentication attempts.
  * **Metric** : `oslogin.googleapis.com/start_session_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=oslogin.googleapis.com%2Fstart_session_requests)

| 6 requests per user per minute  
Continue session requests | 

  * **Description** : Limit for completing OS Login two-factor authentication attempts.
  * **Metric** : `oslogin.googleapis.com/continue_session_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=oslogin.googleapis.com%2Fcontinue_session_requests)

| 6 requests per user per minute  
  
### Per region quotas

Quota group | Details | Default quota  
---|---|---  
Metadata server requests | 

  * **Description** : Limit for calls to the metadata server for OS Login connection authorization checks and user lookups. OS Login makes calls to the metadata server to retrieve OS Login users during the following operations:
    * When a VM is created. OS Login caches the result.
    * When a user attempts to connect to a VM.
    * When system processes search for a user that isn't in the cache.
  * **Metric** : `oslogin.googleapis.com/metadata_server_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=oslogin.googleapis.com%2Fmetadata_server_requests)

| 60,000 requests per region per minute  
Metadata server group requests | 

  * **Description** : Limit for calls to the metadata server for OS Login POSIX group lookups. If VMs don't have [OS Login groups](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#linux-groups) configured, metadata server groups quota might be consumed, but consumption has no impact on VM performance. OS Login makes calls to the metadata server to retrieve OS Login groups during the following operations:
    * When a VM is created. OS Login caches the result.
    * When system processes search for a group that isn't in the cache.
  * **Metric** : `oslogin.googleapis.com/metadata_server_groups_requests` View this quota in the Google Cloud console: [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?metric=oslogin.googleapis.com%2Fmetadata_server_groups_requests)

| 60 requests per region per minute  
  
## Manage quotas

To manage the quotas for your project, do the following:

  * Follow the best practices for [preserving API rate limits](https://docs.cloud.google.com/compute/docs/api/best-practices#preserve-API-rate-limits).
  * Use the Google Cloud console to view and edit quotas:

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?service=oslogin.googleapis.com)

    * If you want to quotas, see [Capping usage](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage).
    * If you need higher quotas than the default maximum, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). In your request, add information showing the consumption rate in your environment. These include [OS Login audit logs](https://docs.cloud.google.com/compute/docs/oslogin/view-audit-logs) or other error messages stating that the rate limit is exceeded.



## What's next?

  * Learn more about [working with Cloud Quotas](https://docs.cloud.google.com/docs/quotas/overview).
  * Learn more about [OS Login](https://docs.cloud.google.com/compute/docs/oslogin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
