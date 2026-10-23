---
url: https://docs.cloud.google.com/knowledge-catalog/docs/add-metadata-quickstart/
title: Quickstart: Add metadata to a BigQuery table \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:02.967142+00:00
---

# Quickstart: Add metadata to a BigQuery table  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/add-metadata-quickstart/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add metadata to a BigQuery table

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you attach business and technical metadata to your data assets so that you can organize, discover, and govern your data. In Knowledge Catalog, each data asset is represented as an _entry_ , and you attach metadata by adding _aspects_ —sets of related metadata fields defined by a reusable template called an _aspect type_.

In this quickstart, you create a BigQuery dataset and table from a public BigQuery dataset, create an aspect type, and add an aspect to the table entry.

## Before you begin

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com)

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com)




### Required roles

To get the permissions that you need to add metadata to a BigQuery table, ask your administrator to grant you the following IAM roles on the project: 

  * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)
  * [BigQuery Data Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`)
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a dataset and a table

  1. In the Google Cloud console, go to the **BigQuery Studio** page.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

  2. Create a dataset:

     1. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

     2. In the **Explorer** pane, find your project. Click more_vert**View actions** , and then click **Create dataset**.

     3. In the **Dataset ID** field, enter `catalog_demo_dataset`.

Keep the default values for the other fields.

     4. Click **Create dataset**.

  3. Copy a public table to your dataset:

     1. In the **Explorer** pane, search for the table named `bigquery-public-data.new_york_citibike.citibike_stations`. You might need to set the search scope to include the `bigquery-public-data` project.

This table is part of the NYC Citi Bike Trips dataset, a public dataset that contains data about a bike share program.

     2. Select the `citibike_stations` table.

     3. Click **Copy**. Enter the following information:

        * **Project** : select your project.
        * **Dataset** : select `catalog_demo_dataset`.
        * **Table** : enter `bike_stations`.
     4. Click **Copy**.

  4. In the **Explorer** pane, locate the `catalog_demo_dataset` dataset, and confirm that the `bike_stations` table is listed in the dataset.




## Define a metadata template: create an aspect type

  1. In the Google Cloud console, go to the Knowledge Catalog **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog)

  2. Click the **Aspect types** tab, and then click the **Custom** tab.

  3. Click **Create aspect type**.

  4. In the **Aspect type ID** field, enter `data-governance-demo`.

  5. For **Location** , select `global`.

  6. In the **Template** section, click **Add field**. Use the information in the following table to add several fields to the aspect type:

Name | Type | Is required | Description  
---|---|---|---  
`source-of-data-asset` | Text | No | -  
`retention-date` | Date and time | No | -  
`data-classification` |  Enum Add the values `Public`, `Sensitive`, and `Confidential`. | Yes | -  
`has-pii` | Boolean | Yes | `Whether the data asset has personally identifiable information`  
  7. Click **Save**.




## Add metadata to the table: add an aspect to the entry

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the search box, enter `catalog_demo_dataset`.

  3. Select the **bike_stations** table.

  4. Add a custom aspect to the entry:

     1. In the **Aspects** section, next to **Optional aspects** , click add**Add**.

     2. Select the `data-governance-demo` aspect type.

This creates an aspect that uses your aspect type as a template.

     3. Enter the following values:

        * **Source of data asset** : `Copied from NYC Citi Bike Trips public dataset`
        * **Retention date** : enter a date.
        * **Data classification** : `Public`
        * **Has PII** : `False`
     4. Click **Save**.

  5. To see the metadata values that you added, in the **Aspects** section, select the **data-governance-demo** aspect.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the project

The easiest way to stop billing is to delete the project that you created for this quickstart.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

If you want to reuse your project, delete the resources that you created.

  1. Delete the dataset:

     1. In the Google Cloud console, go to the **BigQuery Studio** page.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

     2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

     3. In the **Explorer** pane, search for the `catalog_demo_dataset` dataset.

     4. Click more_vert**View actions** , and then click **Delete**. Confirm when prompted.

  2. Delete the aspect type:

     1. In the Google Cloud console, go to the Knowledge Catalog **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog)

     2. Click the **Aspect types** tab, and then click the **Custom** tab.

     3. Click the `data-governance-demo` aspect type.

     4. Click **Delete**. Confirm when prompted.




## What's next

  * Learn more about [metadata management](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).
  * Learn how to [search for resources](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  * Learn how to [work with aspects and aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata).
  * Try [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
