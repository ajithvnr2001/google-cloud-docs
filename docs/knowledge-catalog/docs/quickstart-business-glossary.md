---
url: https://docs.cloud.google.com/knowledge-catalog/docs/quickstart-business-glossary/
title: Create and use a business glossary \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:27.266919+00:00
---

# Create and use a business glossary  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/quickstart-business-glossary/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and use a business glossary

Knowledge Catalog lets you create a business glossary to establish a standardized vocabulary for your data assets, reduce ambiguity, and improve data discovery across your organization. In this quickstart, you use a retail industry scenario with sample data in BigQuery to build a category hierarchy for inventory management. You then define business terms like _Safety Stock Level_ , attach them to BigQuery columns, and search for data using business context.

## Before you begin

Set up your project: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Dataplex and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com&redirect=https%3A//console.cloud.google.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Dataplex and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to create and manage business glossaries, ask your administrator to grant you the following IAM roles: 

  * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) on the Knowledge Catalog (formerly Dataplex Universal Catalog) resource project
  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the project where you use BigQuery



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create the retail operations glossary

  1. In the Google Cloud console, go to the **Knowledge Catalog** > **Glossaries** page.

[Go to glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Click **Create business glossary**.

  3. In the **Display name** field, enter `Global Retail Operations Glossary`.

  4. In the **Location** list, select **us (multiple regions in United States)**.

Multi-regions offer higher availability and resilience, while single regions help meet strict data residency requirements. For more information, see [Knowledge Catalog locations](https://docs.cloud.google.com/knowledge-catalog/docs/locations).

  5. Click **Create**.




## Build the category hierarchy

Organize your terms into a hierarchy to help users navigate your business domains. You can nest categories up to 3 levels deep. For this quickstart, consider the following categories:

  * **Supply Chain & Logistics:** A parent category representing the overall supply chain operations.

  * **Inventory Levels:** A sub-category used to group specific metrics and parameters related to stock management.




### Create a parent category

In this section, create the category `Supply Chain & Logistics`.

  1. On the **Glossary details** page for `Global Retail Operations Glossary`, click **Create category**.
  2. In the **Display name** field, enter `Supply Chain & Logistics`.
  3. Click **Create**.



### Create a sub-category

In this section, create the category `Inventory Levels` as a subset to `Supply Chain & Logistics`.

  1. In the left pane, under `Global Retail Operations Glossary`, select the **Supply Chain & Logistics** category.

  2. In the main pane, click **Create category**.

  3. In the **Display name** field, enter `Inventory Levels`.

  4. Click **Create**.




## Define business terms

In retail, consistent terminology is crucial for managing inventory, sales, and logistics. Define terms to capture business logic and relate them through synonyms or related terms. For this quickstart, consider the following terms:

  * **Safety Stock Level:** Minimum inventory level kept on hand to protect against stockouts caused by unpredictable demand or supply chain disruptions. In this quickstart, this is also referred to as `Buffer Stock`.

  * **Lead Time:** The time it takes from placing an order with a supplier to receiving the inventory.




### Define "Safety Stock Level" as a business term

  1. Select the **Inventory Levels** category in the left pane and click **Add term**.
  2. In the **Display name** field, enter `Safety Stock Level` and click **Create**.
  3. In the **Terms details** page, click add **Add** for **Description** and enter `Minimum inventory maintained to mitigate risk of stockouts during supply chain volatility.`
  4. Click **Save**.



### Add "Buffer Stock" as a synonym

  1. Select the **Inventory Levels** category in the left pane and click **Add term**.
  2. In the **Display name** field, enter `Buffer Stock` and click **Create**.
  3. In the **Synonym terms** section, click edit **Edit synonyms**.
  4. Search for `Safety Stock Level`, select it, and click **Close**.



### Define "Lead Time" and relate it to "Buffer Stock"

  1. Select the **Inventory Levels** category in the left pane and click **Add term**.
  2. In the **Display name** field, enter `Lead Time` and click **Create**.
  3. Click add **Add** for **Description** and enter `The time it takes from placing an order with a supplier to receiving the inventory.`
  4. Click **Save**.
  5. In the **Related terms** section, click edit **Edit related terms**.
  6. Search for `Buffer Stock`, select it, and click **Close**.



## Create a sample table in BigQuery

To attach the business terms that you created to actual data assets, first create an asset with relevant columns.

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. If this is your first time using BigQuery, click **Done** to close the welcome window.

  3. In the query editor, paste the following query to create a sample dataset and table:
         
         CREATE SCHEMA omnichannel_prod OPTIONS(location="us");
         CREATE TABLE omnichannel_prod.daily_stock_summary (
           sku STRING,
           buffer_qty INT64,
           order_lead_time INT64
         );
         INSERT INTO omnichannel_prod.daily_stock_summary (sku, buffer_qty, order_lead_time)
         VALUES
           ('SH001', 50, 7),
           ('BT002', 20, 14),
           ('SH003', 60, 5),
           ('BT004', 30, 10),
           ('SH005', 70, 7),
           ('BT006', 40, 12),
           ('SH007', 80, 6);
         

  4. Click play_circle **Run**. After the query succeeds, you have a new table named `daily_stock_summary` in a dataset named `omnichannel_prod`.




## Attach terms to table columns

  1. In the Google Cloud console, return to the **Knowledge Catalog** > **Search** page.

[Go to search](https://console.cloud.google.com/dataplex/dp-search)

  2. Refresh the page if needed.

  3. In the **Search** bar, enter `omnichannel_prod.daily_stock_summary` and press **Try natural language search**.

  4. Click the **daily_stock_summary** table in the search results to view its details.

  5. Click the **Schema** tab.

  6. In the row for `buffer_qty`, select the checkbox, and then click add **Add business term**.

  7. In the **Add business terms** pane, search for and select `Safety Stock Level`.

  8. Select the row for `order_lead_time`, click add **Add business term**.

  9. In the **Add business terms** pane, search for and select `Lead Time`.




## Search for data using business context

Users can now find technical assets using business language.

  1. In the Google Cloud console, go to the **Knowledge Catalog** > **Search** page.

[Go to search](https://console.cloud.google.com/dataplex/dp-search)

  2. Try the following searches to return the `daily_stock_summary` table:

  3. In the search bar, enter `term: "Safety Stock Level"`.

  4. Click **Try natural language search**.

The **daily_stock_summary** table appears.

  5. In the search bar, enter `term: "Lead Time"` and press `Enter`.

The **daily_stock_summary** table appears.

  6. To find assets linked using synonym relationships, go to the **Glossary** page.

[Go to glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  7. Click **Global Retail Operations Glossary**.

  8. On the left navigation pane, click **Supply Chain & Logistics** > **Inventory Levels** > **Safety Stock Level**.

**Related entries** lists all linked data assets.




For large-scale glossaries, use the [Knowledge Catalog Bulk Import feature](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries#bulk-import) to manage terms programmatically using JSON or CSV files.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete project resources

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, delete the glossary and dataset that you created.

#### Delete the glossary

  1. In the Google Cloud console, go to the **Knowledge Catalog** > **Glossaries** page.

  2. Click **Global Retail Operations Glossary**.

  3. Delete the **Supply Chain & Logistics** category first.

  4. Delete the **Inventory Levels** category.

  5. Delete all the business terms.

  6. Click **Delete** for the glossary itself.

  7. Confirm your delete action.




#### Delete the BigQuery dataset

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, expand your project and locate the **omnichannel_prod** dataset.

  3. Click more_vert **View actions** next to the **omnichannel_prod** dataset and select **Delete**.

  4. In the dialog, enter `delete` to confirm deletion, and click **Delete**.




## What's next

  * Learn how to [search for resources](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) in Knowledge Catalog.
  * Learn more about [managing business glossaries](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).
  * Learn how to [enrich entries with aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata).
  * Try [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
