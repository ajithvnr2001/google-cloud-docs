---
url: https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart/
title: Track data lineage for a BigQuery table \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:00.960598+00:00
---

# Track data lineage for a BigQuery table  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Track data lineage for a BigQuery table

Data lineage lets you track where data comes from, how it's transformed, and where it moves across BigQuery tables over time. Tracing these movements helps you maintain compliance, troubleshoot data issues, and perform root-cause analysis. In this quickstart, you use the Google Cloud console to copy two public `new_york_taxi_trips` tables, combine their ride counts into a new BigQuery table, and view the lineage visualization graph. To interact with data lineage programmatically instead, see [Knowledge Catalog and data lineage client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries).

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

  5. Enable the Dataplex, BigQuery, and Data Lineage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com,datalineage.googleapis.com&redirect=https%3A//console.cloud.google.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Dataplex, BigQuery, and Data Lineage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com,datalineage.googleapis.com&redirect=https%3A//console.cloud.google.com)


**Caution:** Data lineage is enabled on a per-project basis, not a per-service basis. After you enable the Data Lineage API, lineage information is automatically reported for multiple Google Cloud services in the project, depending on their product-level lineage control. For more details, see [Data lineage considerations and limitations](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-considerations). 

### Required roles

To get the permissions that you need to view lineage visualization graphs, ask your administrator to grant you the following IAM roles: 

  * [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the Knowledge Catalog (formerly Dataplex Universal Catalog) resource project
  * [Data Lineage Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`) on the project where you use BigQuery
  * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the project where you use BigQuery



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Add a public dataset to your project

  1. In the Google Cloud console, go to the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In the **Explorer** pane, click **Add data**.

  4. In the **Add data** pane, select **Public datasets**.

  5. In the **Marketplace** pane, search for `NYC TLC Trips` and click the **NYC TLC Trips** result.

  6. Click **View dataset**.




This adds the public dataset's project as a reference that you can view in the **Explorer** pane. The details pane shows **Dataset info** , including information such as **Dataset ID** , **Data location** , and **Last modified** date.

## Create a dataset in your project

  1. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

  2. In the **Explorer** pane, select the project where you want to create the dataset.

  3. Click more_vert**Actions** and click **Create dataset**.

  4. On the **Create dataset** page, in the **Dataset ID** field, enter: `data_lineage_demo`. Leave the other fields with their default values.

  5. Click **Create dataset**.

  6. In the **Explorer** pane, click **Datasets** , and then click the newly added `data_lineage_demo`.




The details pane shows its **Dataset info**.

## Copy two publicly accessible tables to your dataset

  1. Open a query editor: In the details pane, next to the tab called `data_lineage_demo`, click add_box **SQL query**. This step creates a tab called `Untitled`.

  2. In the query editor, copy the first table by entering the following query. Replace `PROJECT_ID` with your [project's identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
         
         CREATE TABLE `PROJECT_ID.data_lineage_demo.nyc_green_trips_2021`
         COPY `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2021`
         

  3. Click play_circle **Run**. This step creates the first table, called `nyc_green_trips_2021`.

  4. In the **Query results** pane, click **Go to table**. This step displays the contents of the first table.

  5. In the query editor, copy the second table by replacing the previous query with the following query. Replace `PROJECT_ID` with your [project's identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
         
         CREATE TABLE `PROJECT_ID.data_lineage_demo.nyc_green_trips_2022`
         COPY `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2022`
         

  6. Click play_circle **Run**. This step creates the second table, called `nyc_green_trips_2022`.

  7. In the **Query results** pane, click **Go to table**. This step displays the contents of the second table.




## Aggregate data into a new table

  1. In the query editor, enter the following query. Replace `PROJECT_ID` with your [project's identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
         
         CREATE TABLE `PROJECT_ID.data_lineage_demo.total_green_trips_22_21`
         AS SELECT vendor_id, COUNT(*) AS number_of_trips
         FROM (
              SELECT vendor_id FROM `PROJECT_ID.data_lineage_demo.nyc_green_trips_2022`
              UNION ALL
              SELECT vendor_id FROM `PROJECT_ID.data_lineage_demo.nyc_green_trips_2021`
         )
         GROUP BY vendor_id
         

  2. Click play_circle **Run**. This step creates a combined table, called `total_green_trips_22_21`.

  3. In the **Query results** pane, click **Go to table**. This step displays the combined table.




## View the lineage graph in Knowledge Catalog

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page. 

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the **Search** box, enter `total_green_trips_22_21` and click **Search**.

  3. From the results list, click `total_green_trips_22_21`. This step displays the BigQuery table **Details** tab.

  4. Click the **Lineage** tab.


**Note:** It might take some time for automatic lineage to pick up these changes. If you don't see the lineage graph yet, check again after several minutes.![The total_green_trips_22_21 table with details panel docked to the bottom.](https://docs.cloud.google.com/static/knowledge-catalog/images/lineage_total_end_screen.png)**Figure 1.** Data lineage with node details 

In the lineage graph, each rectangular node represents a table, either an original, copied, or combined table. You can do the following:

  * To show or hide the origin of a table, click **+** (Expand) or **-** (Collapse).

  * To show table information, click a node. This step displays a node **Details** pane.

  * To show process information, click ![view lineage process details](https://docs.cloud.google.com/static/knowledge-catalog/images/lineage_process_icon.png). This step displays a process **Details** pane showing the job that transformed a source table to a target table.


![The intermediary nyc_green_trips_2021 table with details panel docked to the bottom.](https://docs.cloud.google.com/static/knowledge-catalog/images/lineage_intermediary_table_screen.png)**Figure 2.** Data lineage with process details 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the dataset

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

  3. In the **Explorer** pane, search for the `data_lineage_demo` dataset that you created.

  4. Click the dataset, and then click **Delete**.

  5. Confirm your delete action.




## What's next

  * Learn more about [data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage).
  * Learn how to [run BigQuery queries](https://docs.cloud.google.com/bigquery/docs/running-queries).
  * Learn how to [use data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).
  * Learn how to use [Knowledge Catalog and Data Lineage client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries).
  * Learn about [Knowledge Catalog pricing](https://cloud.google.com/dataplex/pricing).
  * Try [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
