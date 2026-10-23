---
url: https://docs.cloud.google.com/filestore/docs/requesting-quota-increases/
title: Request quota increases \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:27.102147+00:00
---

# Request quota increases  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/requesting-quota-increases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Request quota increases Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to make a quota increase request for Filestore instances and backups when you have reached or are approaching your quota limit in a particular region.

A Filestore project's storage capacity and instance quota are influenced by the [region](https://docs.cloud.google.com/filestore/docs/regions) and [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) that you choose. Quota for the zonal tier with a higher capacity range starts at `0`, so to create such instances, you must first submit a quota increase request. Once quota is granted, you can start creating instances.

To view and manage your available quota, follow these steps:

  1. In the Google Cloud console, go to the **IAM & Admin** page.
  2. In the navigation pane, click **Quotas & System Limits**.

[Go to the Quotas & System Limits page](https://console.cloud.google.com/iam-admin/quotas)

  3. In the **Service** column, select **Cloud Filestore API**.

  4. Select the checkbox next to the Filestore quota you want to increase.

  5. Click create**Edit** and the **Quota changes** dialog appears.

  6. In the **New value** field, enter the quota value that you want. In the adjacent list, select the unit.

  7. Click **Done** and then click **Submit request**.




Quota increase requests generally take two business days to process. Large requests may require more information and take a longer time. If you don't get a response within two business days, work with support or your sales partner.

For more information about quotas, see [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview).

## What's next

  * Learn how to set up alerts for [low disk space](https://docs.cloud.google.com/filestore/docs/monitoring-instances#low-disk-space) and [low backups quota](https://docs.cloud.google.com/filestore/docs/monitoring-instances#low-backups-quota).
  * [Understand capacity errors you might receive before reaching full provisioned capacity](https://docs.cloud.google.com/filestore/docs/known-issues#capacity_errors_before_reaching_full_provisioned_capacity).
  * [Optimize and test instance performance](https://docs.cloud.google.com/filestore/docs/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
