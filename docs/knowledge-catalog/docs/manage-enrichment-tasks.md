---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-tasks/
title: Manage enrichment tasks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:53.692436+00:00
---

# Manage enrichment tasks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-tasks/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage enrichment tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Knowledge Studio gated preview**  
Knowledge Studio is currently available as a gated preview. To view the context graph, create context sets, and run enrichment workflows, you must first request allowance for your organization.   
  
[Request preview access](https://docs.google.com/forms/d/e/1FAIpQLScw1O38BmcLIvqL1ZvpybJsLGO_Dmuq0a5RrCJIqW11iljsKQ/viewform)

This guide describes how to manage your existing enrichment tasks from the **Enrichment** page in Knowledge Studio. From this page, you can edit, view, delete, and manually run your tasks.

## View an enrichment task

To view the configuration and details of an enrichment task:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the left navigation pane, select **Enrichments**.

  3. In the **Knowledge Studio** page, click **Enrichments**.

  4. From the list of enrichment tasks, click the name of the task you want to view.




The task details page opens, displaying the following tabs:

  * **Overview** : Displays the task's configuration, including its goal, target resources, context set, and source datasets.
  * **Jobs** : Displays a list of all historical runs (jobs) for this task. > **Note:** For tasks with auto-publishing enabled, auto-approved metadata > changes are written directly to Knowledge Catalog and > don't have detailed change information tracked directly on the individual > run report. These changes are surfaced in the global change-events history > API instead.



## Edit an enrichment task

To modify an existing enrichment task:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.
  2. In the left navigation pane, select **Enrichments**.
  3. In the **Knowledge Studio** page, click **Enrichments**.
  4. From the list of enrichment tasks, click the name of the task you want to view.
  5. Click **Edit**.
  6. Modify the task configuration as needed. You can update the goal, scope, and evaluation configurations.
  7. Click **Save** to apply your changes.



## Run an enrichment task manually

While tasks can be scheduled to run automatically, you can also trigger them manually:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.
  2. In the left navigation pane, select **Enrichments**.
  3. In the **Knowledge Studio** page, click **Enrichments**.
  4. From the list of enrichment tasks, click the name of the task you want to trigger.
  5. Click **Run now**.



A new job run is initiated and will appear in the **Jobs** tab.

## Delete an enrichment task

If you no longer need an enrichment task, you can delete it:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.
  2. In the left navigation pane, select **Enrichments**.
  3. In the **Knowledge Studio** page, click **Enrichments**.
  4. From the list of enrichment tasks, click the name of the task you want to delete.
  5. Click **Delete**.
  6. In the confirmation dialog, confirm that you want to delete the task.



## What's next

  * [About enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks).
  * [Manage enrichment runs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
