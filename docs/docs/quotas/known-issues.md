---
url: https://docs.cloud.google.com/docs/quotas/known-issues/
title: Known issues \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:32.514725+00:00
---

# Known issues  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

The following are known issues within Cloud Quotas.

## Quota values during rollouts

Google Cloud sometimes increases the default quota values for resources and APIs. These changes take place gradually, which means that during the rollout, the quota value that appears in the Google Cloud console or Cloud Quotas API won't reflect the new, increased quota value until the rollout completes.

If a quota rollout is in progress, an informational message appears at the top of the Cloud Quotas page and the rolling update indicator appears next to the quota values impacted by ongoing rollouts. For details, see [View ongoing rollouts](https://docs.cloud.google.com/docs/quotas/view-ongoing-rollouts).

For troubleshooting steps, see [Exceeding quota values during a service rollout](https://docs.cloud.google.com/docs/quotas/troubleshoot#exceeding_quota_values_during_a_service_rollout).

## Quota preference `contactEmail` field is required

To update the `QuotaPreference` value through the Cloud Quotas API, the `contactEmail` field is required. This email address cannot be a group email.

For examples of using `QuotaPreference` in the API, see [Implement common use cases](https://docs.cloud.google.com/docs/quotas/implement-common-use-cases).

## Cloud Quotas limitations in the Google Cloud console

The following limitations apply when you use Cloud Quotas in the Google Cloud console.

### Requests for adjustments on quotas that have no usage

The Google Cloud console doesn't support quota adjustment requests for quotas that have no prior usage. However, you can still request a quota adjustment through the REST API or Google Cloud CLI:

### gcloud

Request a quota adjustment by [using the gcloud CLI](https://docs.cloud.google.com/docs/quotas/gcloud-cli-examples#request_a_quota_increase_adjustment_using_a_dimension)

### REST

Request a quota adjustment by [using the REST API](https://docs.cloud.google.com/docs/quotas/implement-common-use-cases#request_adjustments_on_quotas_that_have_no_usage)

For example, you might clone a project and know ahead of time that you need to increase the value for `compute.googleapis.com/local_ssd_total_storage_per_vm_family`. Although you won't see that quota available in the Google Cloud console, you can still use the API or gcloud CLI to request a quota adjustment. For more information, see [View ongoing rollouts](https://docs.cloud.google.com/docs/quotas/view-ongoing-rollouts).

### Per-user quota usage doesn't appear

The Google Cloud console doesn't display per-user quota usage on the Cloud Quotas page. If an application or service account exceeds a per-user rate limit, then API requests return an HTTP `429 Too Many Requests` status code, even when aggregate project-level metrics on the Cloud Quotas page show that quota remains available.

To diagnose which user or service account is exhausting a per-user rate limit, complete the following steps:

  1. In the Google Cloud console, select the project that initiates the API requests, and then go to the [**Metrics Explorer**](https://console.cloud.google.com/monitoring/metrics-explorer) page.
  2. Click **Select a metric** , and then enter `serviceruntime.googleapis.com/api/request_count` in the filter bar. In the submenus, select **Consumed API > Api > Request count**, and then click **Apply**.
  3. In the **Filter** element, add filters for the response code and the target service or API method: 
     1. Click **Add filter** , and then select `response_code`. In the filter dialog, leave **Comparator** set to **= (equals)** , enter `429` in the **Value** field, and then click **Apply**.
     2. Click **Add filter** again, and then select either `service` (for example, enter `sqladmin.googleapis.com` in the **Value** field for Cloud SQL Admin API) or `method` (for example, enter `google.cloud.sql.v1.SqlInstancesService.Get` in the **Value** field), and then click **Apply**.
  4. In the **Aggregation** element, verify that the first menu is set to **Sum** , and then in the second menu (next to **by**), select `credential_id` to group requests by individual credential.
  5. In the results, find the credential ID (`credential_id`) with the highest number of `429` response codes. This value is the OAuth 2.0 client ID of the service account or user credential that is exhausting the per-user rate limit.
  6. To find which service account corresponds to that client ID, go to the [**Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts) page in the Google Cloud console and search for the OAuth 2.0 client ID matching the credential ID. The matching entry is the service account that is exhausting the per-user rate limit.



To resolve the error after you identify the service account, implement client-side caching or exponential backoff in the client application, distribute workloads across distinct service accounts, or [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## What's next

  * [Troubleshoot quota errors](https://docs.cloud.google.com/docs/quotas/troubleshoot)
  * [Billing questions](https://docs.cloud.google.com/docs/quotas/billing-questions)
  * [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
