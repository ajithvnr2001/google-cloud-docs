---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets/
title: Manage context sets \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:57.301244+00:00
---

# Manage context sets  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage context sets Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Knowledge Studio gated preview**  
Knowledge Studio is currently available as a gated preview. To view the context graph, create context sets, and run enrichment workflows, you must first request allowance for your organization.   
  
[Request preview access](https://docs.google.com/forms/d/e/1FAIpQLScw1O38BmcLIvqL1ZvpybJsLGO_Dmuq0a5RrCJIqW11iljsKQ/viewform)

Context sets let you ground AI agents using bounded containers of semantic information and data asset references. For more information about how these containers operate, see [Context sets overview](https://docs.cloud.google.com/knowledge-catalog/docs/context-sets).

You must configure a context set before you run an enrichment task. Enrichment tasks are autonomous agents that continuously analyze your dataset schemas and documentation to generate proposed metadata for your data assets.

You can configure a context set either as a standalone container or as part of an enrichment job setup. For more information about creating a context set during a task setup, see [Create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks).

## Before you begin

Before you manage context sets, make sure that you have the required IAM roles.

### Required roles

To get the permissions that you need to manage context sets, ask your administrator to grant you the following IAM roles on the project:

  * To create context sets: **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`) or **Dataplex Entry Group Owner** (`roles/dataplex.entryGroupOwner`). These roles contain the `dataplex.entryGroups.setIamPolicy` permission, which is required to automatically grant you owner permissions during context set creation.
  * To edit or delete context sets: **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`) or **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`).



## Create a context set

To create an empty context set to store your enriched metadata, do the following:

### Knowledge Studio

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the left navigation pane, select **Context sets**.

  3. In the **Context sets** page, click **Create**.

  4. In the **Create context set** pane, enter a name in the **Display name** field and an ID in the **Context set ID** field.

  5. Optional: Enter a **Description** , select a **Location** , and add **Labels**.

  6. Click **Save**.




### Metadata types

  1. In the Google Cloud console, go to the **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog/entry-groups)

  2. Click **Entry groups** > **Context set**.

  3. In the **Metadata types** page, click **Create**.

  4. In the **Create context set** pane, enter a name in the **Display name** field and an ID in the **Context set ID** field.

  5. Optional: Enter a **Description** , select a **Location** , and add **Labels**.

  6. Click **Save**.




After you create the context set, you can select it as the target for your enrichment tasks. The enrichment run populates this container with the AI's proposed metadata concepts, semantic associations, and formulas.

For more information about enrichment tasks, see [About enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks).

## View context sets

To view existing context sets, do the following:

### Knowledge Studio

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the left navigation pane, select **Context sets**.

  3. To view the details of a specific context set, click its name in the list.




### Metadata types

  1. In the Google Cloud console, go to the **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog/entry-groups)

  2. Click **Entry groups** > **Context set**.

  3. To view the details of a specific context set, click its name in the list.




The details page displays the context set's properties, such as its description, location, and project ID. It also contains a **Sample entries** section that lists a preview of the enriched metadata entries stored within the context set, and provides a button to view all related entries in search.

## Edit a context set

Using the Google Cloud console, you can edit the container properties of a context set, which include its **Display name** , **Description** , and **Labels**.

To update the enriched metadata content inside a context set, you must run an enrichment task targeting that set and approve the generated change proposals. For more information about approving change proposals, see [Manage enrichment runs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs).

To edit the properties of a context set, do the following:

### Knowledge Studio

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the left navigation pane, select **Context sets**.

  3. Click the name of the context set that you want to edit.

  4. On the details page, click **Edit**.

  5. Modify the editable fields (**Display name** , **Description** , or **Labels**), and then click **Save**.




### Metadata types

  1. In the Google Cloud console, go to the **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog/entry-groups)

  2. Click **Entry groups** > **Context set**.

  3. In the **Metadata types** page, click the name of the context set that you want to edit.

  4. On the details page, click **Edit**.

  5. Modify the editable fields (**Display name** , **Description** , or **Labels**), and then click **Save**.




## Delete a context set

Deleting a context set removes its semantic associations from the data context graph. If you delete a context set while an enrichment run is active, the run fails to save its proposed metadata at completion because the target destination is no longer available. Subsequent runs of the enrichment task also fail until you update the task to output to a valid context set.

To delete a context set, do the following:

### Knowledge Studio

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the left navigation pane, select **Context sets**.

  3. In the list, click the name of the context set that you want to delete.

  4. On the details page, click **Delete**.

  5. Confirm the deletion.




### Metadata types

  1. In the Google Cloud console, go to the **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog/entry-groups)

  2. Click **Entry groups** > **Context set**.

  3. In the list, click the name of the context set that you want to delete.

  4. On the details page, click **Delete**.

  5. Confirm the deletion.




## Limitations

For information about limitations that apply during Preview, see [ Preview boundaries](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks#preview-boundaries).

## What's next

For more information, see the following:

  * [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites)
  * [Create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks)
  * [Manage enrichment runs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
