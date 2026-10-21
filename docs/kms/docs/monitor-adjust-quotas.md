---
url: https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas/
title: Monitor and adjust Cloud KMS quotas \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:39.393837+00:00
---

# Monitor and adjust Cloud KMS quotas  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Monitor and adjust Cloud KMS quotas Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to manage your Cloud Key Management Service quotas. For information about the quotas associated with Cloud KMS, see [Quotas](https://docs.cloud.google.com/kms/quotas).

## Before you begin

The following permissions are required to view project quotas:

  * `resourcemanager.projects.get`
  * `monitoring.timeSeries.list`
  * `serviceusage.services.list`
  * `serviceusage.quotas.get`



The `serviceusage.quotas.update` permission is required to change project quotas.

For information about which IAM roles include these permissions, see [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference).

## Check your Cloud KMS quotas

  1. In the Google Cloud console, go to the **Cloud KMS API/Service Details** page.

[Go to Cloud KMS API/Service Details](https://console.cloud.google.com/apis/api/cloudkms.googleapis.com/quotas)

This page lets you view quota details for the Cloud KMS API.

  2. To view quotas for a different project, select the project in the Google Cloud console header.

  3. To filter by quota type, click in the **Filter** bar and select **Quota** from the properties list, then choose the quota.

  4. To filter by region, click in the **Filter** bar and select **Dimensions (e.g. location):** from the properties list, then enter the region name.




If you're nearing or exceeding your quotas, you can Request higher Cloud KMS quotas. You can also opt in to having the [quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster) system automatically adjust your Cloud KMS quotas based on your usage.

## Troubleshoot quota issues

If Cloud KMS denies a request because you have exceeded your quota and the system can't serve the request, it returns a `RESOURCE_EXHAUSTED` error. For requests made using the Cloud KMS REST API, the `RESOURCE_EXHAUSTED` error has an HTTP status code of `429`.

Recurring `RESOURCE_EXHAUSTED` errors indicate that your project regularly exceeds one or more of its quotas. To address this issue, you can try any or all of the following:

  * Reduce the rate at which your projects are making requests that use Cloud KMS resources.

  * Request higher Cloud KMS quotas or opt in to using the [quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster) system to automatically adjust your Cloud KMS quotas based on your usage.

  * Use separate key projects for your resources where appropriate so that multiple resources aren't sharing the same quotas.

**Note:** Creating additional projects as described here may create issues with other quotas, such as your **Projects per user** or **Projects per billing account** quotas. For more information about Google Cloud quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).
  * Add a backoff mechanism to your client to handle `RESOURCE_EXHAUSTED` errors.




## Request higher Cloud KMS quotas

  1. In the Google Cloud console, go to the **Cloud KMS API/Service Details** page.

[Go to Cloud KMS API/Service Details](https://console.cloud.google.com/apis/api/cloudkms.googleapis.com/quotas)

This page lets you view quota details for the Cloud KMS API.

  2. To request a quota increase for a different project, select the project in the Google Cloud console header.

  3. In the list of quotas, select the default or regional quota that you want to increase, then click **Edit Quotas**.

**Note:** Multiregional and global quotas don't appear in the console. To increase quota for multiregional locations or the global location, make the request for a different region and mention the multiregion in the **Request description**.
  4. In the **Quota changes** pane, enter the chosen limits for the selected quotas.

  5. In **Request description** , provide a description of the reason for your request.

  6. Click **Next** to continue.

  7. Provide your contact information including **Name** , **Email** , and **Phone**.

  8. To complete your request, click **Submit request**.

After your request is submitted, it's sent to approvers for evaluation. You're notified about the status of your request after it's reviewed.




## Cap Cloud KMS usage for a specific project

To impose a stricter usage quota for your Cloud KMS resources, set the quota for a given project to a lower limit than the default.

  1. In the Google Cloud console, go to the **Cloud KMS API/Service Details** page.

[Go to Cloud KMS API/Service Details](https://console.cloud.google.com/apis/api/cloudkms.googleapis.com/quotas)

This page lets you view quota details for the Cloud KMS API.

  2. To decrease a quota for a different project, select the project in the Google Cloud console header.

  3. In the list of quotas, select the default or regional quota that you want to decrease, then click **Edit Quotas**.

  4. In the **Quota changes** pane, enter the chosen limits for the selected quotas.

  5. Click **Next** to continue.

If you are reducing a quota by more than 10% of the current limit, a warning appears. To continue applying a lower quota than the default, click **Confirm**. Otherwise, you can click **Cancel** to go back and choose a new limit.

  6. To save your changes, click **Submit request**.

Your new limit is active immediately.




## What's next

  * Learn more about [Cloud Quotas](https://docs.cloud.google.com/docs/quotas/overview).
  * For information on how client libraries surface the `RESOURCE_EXHAUSTED` error, see [Client library mapping](https://docs.cloud.google.com/apis/design/errors#client_library_mapping).
  * View [details about Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
