---
url: https://docs.cloud.google.com/memorystore/docs/redis/high-resource-utilization/
title: High resource utilization \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:36.035156+00:00
---

# High resource utilization  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/high-resource-utilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  High resource utilization Stay organized with collections  Save and categorize content based on your preferences. 

A Memorystore for Redis instance might experience the following conditions, which prevent it from performing optimally:

  * The instance has a high CPU or memory usage.
  * There are repeated cache flushes in the instance because of memory exhaustion.
  * You can't create backups for the instance because of high memory utilization or high write traffic.
  * Replicas can't synchronize data with the instance because of a high level of write traffic.



To resolve these issues, use the **High resource utilization** health issue. To access this health issue, use the [Database Center](https://docs.cloud.google.com/database-center/docs/overview). This is an AI-assisted dashboard that gives you a centralized view of health issues for instances.

## Before you begin

Before you begin to use the **High resource utilization** health issue, complete the prerequisites in this section.

### Assign roles and permissions

To use Database Center to view and work with health issues, you must be granted IAM permissions for Database Center. For more information about getting these permissions, see [Grant IAM permissions](https://docs.cloud.google.com/database-center/docs/set-up-database-center#grant-iam-permissions).

Also, for more information about IAM roles, see [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View the health issue

To view the **High resource utilization** health issue, do the following:

  1. In the Google Cloud console, go to the **All resources** page in Database Center.

[All resources](https://console.cloud.google.com/database-center/resources)

  2. Select the **Products** menu. In the **Products** dialog, do the following:

     1. Optional: If any products are selected, then clear them.

     2. In the **Memorystore** pane, select **Redis**.

     3. Click **Apply**.

  3. Select the **Issues** menu. In the **Issues** dialog, do the following:

     1. Clear all selected issues.

     2. In the **Performance and capacity** pane, select the **High resource utilization** health issue.

     3. Click **Apply**. Database Center displays any instances that have high resource utilization issues.

  4. Click the issue, which appears next to the name of an instance. The **High resource utilization** health issue opens in a separate pane.

If the issue doesn't appear next to the instance, then the resource utilization for the instance isn't high.

  5. To view detailed information about the health issue, click the expander arrow (_expand_more_) in the pane.




## Address the health issue

To address the **High resource utilization** health issue, increase the instance's capacity. This gives the instance more memory and processing power to handle a larger volume of data or traffic. The capacity is determined by the size of the instance.

By [scaling the instance](https://docs.cloud.google.com/memorystore/docs/redis/about-scaling-instances), your application can handle an increased demand without performance degradation. To scale the instance, [increase the size of the instance](https://docs.cloud.google.com/memorystore/docs/redis/scale-instances#instance_scaling_instructions).

## What's next

  * [About scaling instances](https://docs.cloud.google.com/memorystore/docs/redis/about-scaling-instances)
  * [Scale Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/scale-instances)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
