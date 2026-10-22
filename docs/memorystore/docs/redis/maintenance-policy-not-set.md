---
url: https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy-not-set/
title: The maintenance policy isn't set \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:54.715478+00:00
---

# The maintenance policy isn't set  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy-not-set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  The maintenance policy isn't set Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Redis updates instances routinely by performing maintenance on them to ensure that the service is reliable, performant, secure, up-to-date, and has a zero downtime impact. In addition to Memorystore for Redis performing maintenance on your instances, you can customize maintenance schedules to align with your application's needs and to minimize disruptions.

To customize your maintenance schedules, you can configure maintenance windows for your instances. _Maintenance windows_ are specific, user-defined time slots of when Memorystore for Redis can update instances. A _maintenance policy_ describes the metadata of this configuration, such as when it was created or last updated, often referring to the overall strategy of managing these maintenance windows.

To check if you set maintenance windows for instances, use the **Maintenance policy not set** health issue. The health issue provides you with an optimal time slot for your maintenance windows when you have low traffic.

To access the health issue, use the [Database Center](https://docs.cloud.google.com/database-center/docs/overview). This is an AI-assisted dashboard that gives you a centralized view of health issues for instances.

## Before you begin

Before you begin to use the **Maintenance policy not set** health issue, complete the prerequisites in this section.

### Assign roles and permissions

To use Database Center to view and work with health issues, you must be granted IAM permissions for Database Center. For more information about getting these permissions, see [Grant IAM permissions](https://docs.cloud.google.com/database-center/docs/set-up-database-center#grant-iam-permissions).

Also, for more information about IAM roles, see [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View the health issue

To view the **Maintenance policy not set** health issue, do the following:

  1. In the Google Cloud console, go to the **All resources** page in Database Center.

[All resources](https://console.cloud.google.com/database-center/resources)

  2. Select the **Products** menu. In the **Products** dialog, do the following:

     1. Optional: If any products are selected, then clear them.

     2. In the **Memorystore** pane, select **Redis**.

     3. Click **Apply**.

  3. Select the **Issues** menu. In the **Issues** dialog, do the following:

     1. Clear all selected issues.

     2. In the **Other** pane, select the **Maintenance policy not set** health issue.

     3. Click **Apply**. Database Center displays any instances that don't have custom maintenance windows set for them.

  4. Click the issue, which appears next to the name of an instance. The **Maintenance policy not set** health issue opens in a separate pane.

If the issue doesn't appear next to the instance, then you set a maintenance window for the instance.

  5. To view detailed information about the health issue, click the expander arrow (_expand_more_) in the pane.




## Address the health issue

To address the **Maintenance policy not set** health issue, [configure a maintenance window](https://docs.cloud.google.com/memorystore/docs/redis/find-and-set-maintenance-windows#set_a_preferred_window_for_maintenance_on_an_instance) so that when regular maintenance occurs, it's during a day and time that minimizes disruption.

## What's next

  * [About maintenance](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance)
  * [Find and set maintenance windows](https://docs.cloud.google.com/memorystore/docs/redis/find-and-set-maintenance-windows)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
