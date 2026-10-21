---
url: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-prerequisites/
title: Prerequisites and setup \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:35:58.888318+00:00
---

# Prerequisites and setup  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-prerequisites/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)



Send feedback 

#  Prerequisites and setup Stay organized with collections  Save and categorize content based on your preferences. 

To complete the lineage use case tutorials, perform the following setup steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. Enable the BigQuery, Data lineage, Dataform, BigQuery Data Transfer, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,datalineage.googleapis.com,dataform.googleapis.com,bigquerydatatransfer.googleapis.com,secretmanager.googleapis.com)

For new projects, the BigQuery API is automatically enabled.




## Required roles

To get the permissions that you need to perform the lineage use case tutorials, ask your administrator to grant you the following IAM roles on your projects:

  * **Data Lineage Viewer** (`roles/datalineage.viewer`): on the project where lineage is recorded and viewed.
  * **BigQuery Data Viewer** (`roles/bigquery.dataViewer`): on the table's storage project.
  * **BigQuery Resource Viewer** (`roles/bigquery.resourceViewer`): on the job's compute project.
  * **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`): on the project where catalog entries are stored.
  * **Dataform Editor** (`roles/dataform.editor`): on the project where your workspaces and repositories are located.



The following list describes the project types and services associated with the required roles:

  * Storage project stores the BigQuery datasets and tables.
  * Compute project processes your data and stores the lineage metadata. It is used to run BigQuery jobs and data transformations.
  * Catalog entries contain metadata that describes your tables, allowing you to find and organize them without accessing the underlying data.
  * Lineage project records and visualizes the history of your data and its transformations.
  * Dataform is a service used to build, version control, and run SQL-based data pipelines. It transforms raw data into clean, documented datasets.



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

## Get started

To complete the tutorials, use the [Data lineage use cases repository](https://github.com/GoogleCloudPlatform/dataplex-labs/tree/main/lineage-uses-cases-documentation). This repository contains predefined code to set up datasets and run data transformations.

### Datasets overview

Each tutorial uses a different real-world dataset, such as healthcare provider, employment, or business data, to demonstrate data lineage in realistic scenarios.

### Set up datasets

To track data changes with data lineage, perform this one-time setup:

  1. Create a personal access token and store it in Secret Manager.
  2. Link the repository to Dataform.



After setup, run the data transformations to process the data and generate lineage.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
