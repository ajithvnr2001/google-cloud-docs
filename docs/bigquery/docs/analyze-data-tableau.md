---
url: https://docs.cloud.google.com/bigquery/docs/analyze-data-tableau/
title: Analyze BigQuery data with BI Engine and Tableau Desktop \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:19.364889+00:00
---

# Analyze BigQuery data with BI Engine and Tableau Desktop  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/analyze-data-tableau/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Analyze data with BI Engine and Tableau Desktop

BigQuery BI Engine lets you perform fast, low-latency analysis services and interactive analytics with reports and dashboards backed by BigQuery.

This introductory tutorial is intended for data analysts and business analysts who use the business intelligence (BI) tool Tableau Desktop to build reports and dashboards.

## Objectives

In this tutorial, you complete the following tasks:

  * Create a dataset and copy data.
  * Create a BI reservation and add capacity using the Google Cloud console.
  * Use Tableau Desktop to connect to a BigQuery table that's managed by BI Engine.
  * Create dashboards using Tableau Desktop.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ BigQuery](https://docs.cloud.google.com/bigquery/pricing)
  * [ BI Engine](https://docs.cloud.google.com/bigquery/pricing#bi-engine-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Before you begin, ensure that you have a project to use, that you have enabled billing for that project, and that you have enabled the BigQuery API.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  6. Enable the BigQuery API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery)

For new projects, the BigQuery API is automatically enabled.




### Required roles

To get the permissions that you need to create a dataset, create a table, copy data, query data, and create a BI Engine reservation, ask your administrator to grant you the following IAM roles on the project: 

  * Run copy jobs and query jobs: [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) 
  * Create a dataset, create a table, copy data into a table, and query a table: [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) 
  * Create a BI Engine reservation: [BigQuery Resource Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.resourceAdmin) (`roles/bigquery.resourceAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Additional permissions might be needed if you have are using a custom OAuth client in Tableau Desktop to connect to BigQuery. For more information, see Troubleshooting Errors.

## Create a BigQuery dataset

The first step is to create a BigQuery dataset to store your BI Engine-managed table. To create your dataset, follow these steps:

  1. In the Google Cloud console, go to the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In the **Explorer** pane, click your project.

  4. In the details pane, click more_vert **View actions** , and then click **Create dataset**.

  5. On the **Create dataset** page, do the following:

     * For **Dataset ID** , enter `biengine_tutorial`.
     * For **Data location** , choose **us (multiple regions in United States)** , the [multi-region location](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) where public datasets are stored.

     * For this tutorial, you can select **Enable table expiration** , and then specify the number of days before the table expires.

![Create dataset page](https://docs.cloud.google.com/static/bigquery/images/create-dataset-biengine.png)

  6. Leave all of the other default settings in place and click **Create dataset**.




## Create a table by copying data from a public dataset

This tutorial uses a dataset available through the [Google Cloud Public Dataset Program](https://docs.cloud.google.com/bigquery/public-data). Public datasets are datasets that BigQuery hosts for you to access and integrate into your applications.

In this section, you create a table by copying data from the [San Francisco 311 service requests](https://console.cloud.google.com/marketplace/details/san-francisco-public-data/sf-311?filter=solution-type:dataset) dataset. You can explore the dataset by using the [Google Cloud console](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=san_francisco_311&page=dataset).

### Create your table

To create your table, follow these steps:

  1. In the Google Cloud console, go to the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

  3. In the **Explorer** pane, search for the `san_francisco_311` dataset.

  4. Click the dataset, and then click **Overview > Tables**.

  5. Click the `311_service_requests` table.

  6. In the toolbar, click **Copy**.

![Highlight of the copy option.](https://docs.cloud.google.com/static/bigquery/images/looker-311-table-copy.png)

  7. In the **Copy table** dialog, in the **Destination** section, do the following:

     * For **Project** , click **Browse** , and then select your project.
     * For **Dataset** , select **biengine_tutorial**.
     * For **Table** , enter `311_service_requests_copy`.

![The copy table window with destination options](https://docs.cloud.google.com/static/bigquery/images/copy-311-table.png)

  8. Click **Copy**.

  9. Optional: After the copy job is complete, verify the table contents by expanding **`PROJECT_NAME` > biengine_tutorial** and clicking **311_service_requests_copy > Preview**. Replace **`PROJECT_NAME`** with name of your Google Cloud project for this tutorial.




## Create your BI Engine reservation

  1. In the Google Cloud console, under **Administration** go to the **BI Engine** page.

[Go to the BI Engine page](https://console.cloud.google.com/bigquery/admin/bi-engine)

**Note:** If prompted to enable **BigQuery Reservation API** , click **Enable**.
  2. Click add **Create reservation**.

  3. On the **Create Reservation** page, configure your BI Engine reservation:

     * In the **Project** list, verify your Google Cloud project.
     * In the **Location** list, select a location. The location should match the [location of the datasets](https://docs.cloud.google.com/bigquery/docs/locations) that you're querying.
     * Adjust the **GiB of Capacity** slider to the amount of memory capacity that you're reserving. The following example sets the capacity to 2 GiB. The maximum is 250 GiB.

![BI Engine capacity location](https://docs.cloud.google.com/static/bigquery/images/step-1.png)

  4. Click **Next**.

  5. In the **Preferred Tables** section, optionally specify tables for acceleration with BI Engine. To find table names, do the following:

     1. In the **Table Id** field, type part of the name of the table that you want accelerated by BI Engine—for example, `311`.
     2. From the list of suggested names, select your table names.

Only specified tables are eligible for acceleration. If no preferred tables are specified, all project queries are eligible for acceleration. 

  6. Click **Next**.

  7. In the **Confirm and submit** section, review the agreement.

  8. If you accept the terms of agreement, click **Create**.




After you confirm your reservation, the details are displayed on the **Reservations** page.

![Confirmed reservation](https://docs.cloud.google.com/static/bigquery/images/reservation.png)

## Connect to a dataset from Tableau Desktop

To connect to a dataset from Tableau Desktop, you need to take some steps in Tableau Desktop and then some steps in BI Engine.

### Steps to take in Tableau

  1. Start [Tableau Desktop](https://www.tableau.com/products/desktop).
  2. Under **Connect** , select **Google BigQuery**.
  3. In the tab that opens, select the account that has the BigQuery data that you want to access.
  4. If you're not already signed in, enter your email or phone, select **Next** , and enter your password.
  5. Select **Accept**.



Tableau can now access your BigQuery data.

In [Tableau Desktop](https://www.tableau.com/products/desktop), on the **Data Source** page:

  1. From the **Billing Project** drop-down, select the billing project where you created the reservation.
  2. From the **Project** drop-down, select your project.
  3. From the **Dataset** drop-down, select the dataset `biengine_tutorial`.
  4. Under **Table** , select the table `311_service_requests_copy`.



## Creating a chart

Once you have added the data source to the report, the next step is to create a visualization.

Create a chart that displays the top complaints by neighborhood:

  1. In the Google Cloud console, click **New worksheet**.
  2. Set the **Dimension** to **Complaint Type**.
  3. Filter based on the dimension called `neighborhood`.
  4. Under **Measures** , select **Number of Records**.
  5. Right-click on the **Neighborhood** filter and click **Edit Filter**.
  6. Add a filter to exclude null: select **Null**.
  7. Click **OK**.



For more information, see the [Tableau documentation](https://help.tableau.com/current/pro/desktop/en-us/examples_googlebigquery.htm).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, you can delete the project, delete the BI Engine reservation, or both.

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Deleting the reservation

Alternatively, if you intend to keep the project, then you can avoid additional BI Engine costs by deleting your capacity reservation.

To delete your reservation, follow these steps:

  1. In the Google Cloud console, under **Administration** go to the **BI Engine** page.

[Go to the BI Engine page](https://console.cloud.google.com/bigquery/admin/bi-engine)

**Note:** If prompted to enable **BigQuery Reservation API** , click **Enable**.
  2. In the **Reservations** section, locate your reservation.

  3. In the **Actions** column, click the more_vert icon to the right of your reservation and choose **Delete**.

  4. In the **Delete reservation?** dialog, enter **Delete** and then click **DELETE**.




## Troubleshooting errors

If you are using a custom OAuth configuration in Tableau Desktop to connect to BigQuery, some users might experience issues connecting to a Tableau server and encounter the following error message:
    
    
    the app is blocked
    

To resolve this error, verify that the user is assigned to a role that has all the required permissions to connect Tableau to BigQuery. If the problem persists, add the user to the [OAuth Config Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.viewer) (`roles/oauthconfig.viewer`).

## What's next

  * For an overview of the BI Engine, see [Introduction to BI Engine](https://docs.cloud.google.com/bigquery/docs/bi-engine-intro).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
