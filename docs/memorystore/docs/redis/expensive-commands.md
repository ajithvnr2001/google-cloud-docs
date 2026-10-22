---
url: https://docs.cloud.google.com/memorystore/docs/redis/expensive-commands/
title: Expensive commands \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:56.973534+00:00
---

# Expensive commands  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/expensive-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Expensive commands Stay organized with collections  Save and categorize content based on your preferences. 

You might use Redis commands that are resource-intensive. As either your total data size or the size of a key increases, so does the cost of using these commands. Using the commands might result in the following performance issues:

  * High latency and client timeouts
  * Memory pressure caused by commands that increase memory usage
  * Data loss during node replication and synchronization because the Redis main thread is blocked
  * Starved health checks, observability, and replication



To resolve these performance issues, use the **Expensive commands** health issue. To access this health issue, use the [Database Center](https://docs.cloud.google.com/database-center/docs/overview). This is an AI-assisted dashboard that gives you a centralized view of health issues for instances.

## Before you begin

Before you begin to use the **Expensive commands** health issue, complete the prerequisites in this section.

### Assign roles and permissions

To use Database Center to view and work with health issues, you must be granted IAM permissions for Database Center. For more information about getting these permissions, see [Grant IAM permissions](https://docs.cloud.google.com/database-center/docs/set-up-database-center#grant-iam-permissions).

Also, for more information about IAM roles, see [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View the health issue

To view the **Expensive commands** health issue, do the following:

  1. In the Google Cloud console, go to the **All resources** page in Database Center.

[All resources](https://console.cloud.google.com/database-center/resources)

  2. Select the **Products** menu. In the **Products** dialog, do the following:

     1. Optional: If any products are selected, then clear them.

     2. In the **Memorystore** pane, select **Redis**.

     3. Click **Apply**.

  3. Select the **Issues** menu. In the **Issues** dialog, do the following:

     1. Clear all selected issues.

     2. In the **Performance and capacity** pane, select the **Expensive commands** health issue.

     3. Click **Apply**. Database Center displays any instances that have performance issues associated with expensive commands.

  4. Click the issue, which appears next to the name of an instance. The **Expensive commands** health issue opens in a separate pane.

If the issue doesn't appear next to the instance, then you aren't using expensive commands for the instance.

  5. To view detailed information about the health issue, click the expander arrow (_expand_more_) in the pane.




## Address the health issue

To address the **Expensive commands** health issue, instead of using expensive commands, use [resource-efficient](https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices#resource-intensive-commands) commands. For example, to remove files and links, an alternative to the expensive `DEL` command is the resource-efficient `UNLINK` command.

In addition, use Cloud Monitoring to view the [`/stats/cpu_utilization`](https://docs.cloud.google.com/memorystore/docs/redis/supported-monitoring-metrics#cloud-monitoring-metrics) metric and your client-side logs. Check whether periods of high CPU utilization coincide with the same periods when the expensive commands ran.

## What's next

  * [Resource-intensive commands](https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices#resource-intensive-commands)
  * [Supported monitoring metrics for Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/supported-monitoring-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
