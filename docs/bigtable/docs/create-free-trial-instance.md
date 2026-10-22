---
url: https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance/
title: Create a free trial instance and import sample data \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:16.369798+00:00
---

# Create a free trial instance and import sample data  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a free trial instance and import sample data

This Bigtable free trial instance quickstart guides you through the initial steps of setting up your Bigtable free trial instance and exploring Bigtable capabilities.

Your Bigtable free trial instance lets you learn and explore Bigtable features and capabilities at no cost for 90 days. For more information about Bigtable free trial and Bigtable free trial instances, see [Free trial overview](https://docs.cloud.google.com/bigtable/docs/free-trial-instance).

In this quickstart, you perform the following actions:

  * Create a Bigtable free trial instance in Google Cloud console.
  * Run a query on the example data using Bigtable Studio.
  * Import 100 GB of sample data for performance testing.
  * Import your own data into your Bigtable free trial instance using Cloud Shell.



## Before you begin

  * A 10-day trial period is available to any user with a Google Account. 
  * The 10-day trial period can be extended to 90 days if Cloud Billing is enabled in the project with the Bigtable free trial instance. You aren't charged unless you choose to upgrade your Bigtable free trial instance to a paid instance. 
  * If you delete the Bigtable free trial instance, it **won't be possible to create another instance again** , even if the 90-day trial period is still active. 
  * Enable the APIs and assign IAM roles: 

    1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
    2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

       * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
       * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

    3. Enable the Cloud Bigtable and Cloud Bigtable Admin APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigtable.googleapis.com,bigtableadmin.googleapis.com)

    4. Make sure that you have the following role or roles on the project: roles/bigtable.admin 

#### Check for the roles

       1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
       2. Select the project. 
       3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

       4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

       1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
       2. Select the project. 
       3. Click person_add **Grant access**. 
       4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

       5. Click **Select a role** , then search for the role. 
       6. To grant additional roles, click add **Add another role** and add each additional role. 
       7. Click **Save**. 

    5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

       * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
       * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

    6. Enable the Cloud Bigtable and Cloud Bigtable Admin APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigtable.googleapis.com,bigtableadmin.googleapis.com)

    7. Make sure that you have the following role or roles on the project: roles/bigtable.admin 

#### Check for the roles

       1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
       2. Select the project. 
       3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

       4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

       1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
       2. Select the project. 
       3. Click person_add **Grant access**. 
       4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

       5. Click **Select a role** , then search for the role. 
       6. To grant additional roles, click add **Add another role** and add each additional role. 
       7. Click **Save**. 




## Create a Bigtable free trial instance

The following steps explain how to create a Bigtable free trial instance using the Google Cloud console.

  1. Open the **Welcome to Bigtable** page in the Google Cloud console.

[Welcome to Bigtable](https://console.cloud.google.com/bigtable/welcome)

  2. In the **Experience Bigtable at no cost and no commitment** section, enter the following:

     1. For **Instance name** , enter the name of your instance. For example, `Free trial instance`.
     2. (Optional) In the **Instance ID** , review the auto-generated instance identifier and change it, if required. Examples in this guide use the `free-trial-instance` ID.
     3. For **Region** , select a region near you.
     4. For **Zone** , select **Any**.
  3. Click **Create free instance**.




## Learn Bigtable fundamentals

Your Bigtable free trial instance interface in Google Cloud console provides an optional interactive tutorial, which guides you through the journey of learning and trying out Bigtable fundamentals.

As an option, you can watch this 4-minute introductory video in your Bigtable free trial instance's overview:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click your Bigtable free trial instance (`free-trial-instance`).

  3. In the navigation pane, click **Overview**.

  4. In the **Get the most out of your free instance** section, select **Bigtable fundamentals** , then click **Play video**.

  5. To finish this tutorial step, click **Mark as complete**.




## Query sample data

When you create your Bigtable free trial instance in the Google Cloud console, Bigtable creates a sample table and sample queries for you to explore and familiarize yourself with Bigtable features and capabilities.

The `weather-data` table contains sample weather data reported by airports around the world. To run an example query on this table in Bigtable Studio:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click your Bigtable free trial instance (`free-trial-instance`).

  3. In the navigation pane, click **Overview**.

  4. In the **Get the most out of your free instance** section, select **Query table** , then click **Query table**.

A short welcome tour explains the basics of SQL queries in Bigtable Studio.

**Note:** If this step isn't available, check that the previous step is marked as complete.
  5. The following query for the sample data is created in Bigtable Studio:
         
         SELECT *
         FROM `weather-data`(WITH_HISTORY=>FALSE)
         LIMIT 10;
         

  6. Click **Run**. The results of your query appear in the **Results** table.

  7. To finish this tutorial step, go back to **Oveview** and click **Mark as complete**.




### Explore sample queries

Your free instance has more sample queries to explore. You can check them out in the **Queries** section.

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click your Bigtable free trial instance (`free-trial-instance`).

  3. In the navigation pane, click **Bigtable Studio**.

  4. In the **Explorer** pane, expand **Queries**.

  5. Explore sample queries that demonstrate different aspects of Bigtable querying.

For more information about the query syntax, see [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).




## Import test table for performance benchmarks

To explore Bigtable's capabilities when working with large volumes of data, you can import a test table to run realistic performance benchmarks and explore monitoring tools. The test table contains 100 GB of sample data based on the [Yahoo! Cloud Serving Benchmark (YCSB)](https://en.wikipedia.org/wiki/YCSB) test.

To import the table for performance testing:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click your Bigtable free trial instance (`free-trial-instance`).

  3. In the navigation pane, click **Overview**.

  4. In the **Get the most out of your free instance** section, select **Bigtable performance** , then click **Import YCSB data** and wait until the table is created.

  5. Click **Tables** in the navigation pane, then click the `YCSB` table.

  6. Once data is populated in the YCSB table, you can run a query the table in the Bigtable Studio.

  7. To finish this tutorial step, go back to **Oveview** and click **Mark as complete**.




To dive deeper, you can follow the [PerfKitBenchmarker tutorial](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker/tree/master/tutorials/bigtable_walkthrough) for Bigtable to create custom tests tailored to your specific use cases. To learn more about performance testing, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).

## Import data

You can continue exploring Bigtable by loading large quantities of data, such as time-series, telemetry logs, or machine learning data, into your tables.

Bigtable supports many [ways to import data](https://docs.cloud.google.com/bigtable/docs/import-export). For example, you can start by importing data from a CSV file in Cloud Shell:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click your Bigtable free trial instance (`free-trial-instance`).

  3. In the navigation pane, click **Overview**.

  4. In the **Get the most out of your free instance** section, select **Import data**.

  5. Click **Import** and select **Import CSV via CLI**.

  6. Import CSV data using one of the options:

     * Follow the steps outlined in [Import CSV data](https://docs.cloud.google.com/bigtable/docs/import-export#csv) to upload a local CSV file to Cloud Shell.

     * Create a new example file in Cloud Shell:

### Create an example CSV file and fill it with data

       1. Run the following command in the Cloud Shell to create a new file:
              
              nano example-data.csv
              

       2. Copy the following example data into the file:
              
              ,timestamp_start,timestamp_end,point,description
              ,timestamp,timestamp,coordinate,value
              0001, 2026-045T08:12:22.668, 2026-045T08:30:59.193, 35.403, HIGH_RES
              0002, 2026-045T08:16:06.072, 2026-045T08:17:21.548, -25.831, LOW_RES
              0003, 2026-045T08:05:29.093, 2026-045T08:40:22.250, 23.703, HIGH_RES
              0004, 2026-045T08:18:30.030, 2026-045T08:20:16.674, -5.818, LOW_RES
              0005, 2026-045T08:43:49.486, 2026-045T08:51:36.868, 42.041, HIGH_RES
              0006, 2026-045T08:17:55.572, 2026-045T08:22:32.530, 96.509, HIGH_RES
              0007, 2026-045T08:02:02.056, 2026-045T08:59:34.785, 87.653, HIGH_RES
              0008, 2026-045T08:12:50.590, 2026-045T08:43:19.412, -10.296, LOW_RES
              0009, 2026-045T08:18:29.009, 2026-045T08:47:44.556, 23.375, LOW_RES
              0010, 2026-045T08:14:26.152, 2026-045T08:37:10.951, -11.726, HIGH_RES
              0011, 2026-045T08:07:44.270, 2026-045T08:37:29.702, -55.675, HIGH_RES
              0012, 2026-045T08:17:47.771, 2026-045T08:19:23.476, 37.794, HIGH_RES
              0013, 2026-045T08:29:27.933, 2026-045T08:59:45.301, -12.718, LOW_RES
              0014, 2026-045T08:12:31.432, 2026-045T08:48:47.590, -65.408, HIGH_RES
              0015, 2026-045T08:13:15.119, 2026-045T08:37:50.639, 99.327, LOW_RES
              

       3. Press `Ctrl+X`, then confirm with `y`.

  7. Make sure that the table you want to import your data to is already created and matches the CSV data structure.

If you don't have a table, you can [Create a new table](https://docs.cloud.google.com/bigtable/docs/managing-tables#create-table) that matches your CSV structure. For example, you can do it in the Google Cloud console, or using the `cbt` commands.

The following command in the Cloud Shell creates a new table for the provided example CSV file:
         
         cbt -project PROJECT_ID \
           -instance free-trial-instance \
           createtable TABLE_ID \
           families=timestamp_start,timestamp_end,point,description
         

Replace the following:

     * PROJECT_ID: the project where your Bigtable free trial instance is located.
     * TABLE_ID: the ID for the new table. For example, `example-table`.
  8. Run the following command in the Cloud Shell prompt to import data from the CSV file to the table:
         
         cbt -project PROJECT_ID \
           -instance free-trial-instance  \
           import TABLE_ID \
            FILE_NAME
         

Replace the following:

     * PROJECT_ID: the project where your Bigtable free trial instance is located.
     * TABLE_ID: the ID of the table you want to import the data to.
     * FILE_NAME: the name of the CSV file to import.

Example:
    
    cbt -project example-project -instance free-trial-instance import \
    example-table example-data.csv
    




or other ways to import data to Bigtable, see [Import and export data](https://docs.cloud.google.com/bigtable/docs/import-export).

## Extend the free trial period

You can extend the 10-day trial period to 90 days if your project has an active Cloud Billing account.

To extend the free trial period to 90 days:

  1. Make sure that your project has an active Cloud Billing account.

If you are a new Google Cloud customer, sign in to the Google Cloud console with your Google Account and set up a Cloud Billing account with your [credit card or other payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods#available_payment_methods) first before creating a Bigtable free trial instance. Google uses this payment information to verify your identity. We don't charge your Bigtable instance unless you explicitly [upgrade your Cloud Billing account to a paid account](https://docs.cloud.google.com/free/docs/free-cloud-features#how-to-upgrade), and you upgrade your Bigtable free trial instance.

  2. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  3. Click your Bigtable free trial instance (`free-trial-instance`).

  4. In the navigation pane, click **Overview**.

  5. In the **Overview** section, click **Extend trial**.




## Upgrade the Bigtable free trial instance

After your upgrade your Bigtable free trial instance, the trial is finished and [trial capabilities limitations](https://docs.cloud.google.com/bigtable/docs/free-trial-instance#cost-and-eligibility) no longer apply to your instance. For example, you can scale it or enable replication.

The following steps explain how to upgrade your Bigtable free trial instance:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click your Bigtable free trial instance (`free-trial-instance`).

  3. In the navigation pane, click **Overview**.

  4. In the **Overview** section, click **Upgrade**.

The **Upgrade your Bigtable free instance** page opens and displays a comparison between trial capabilities and full capabilities.

**Note:** If this button isn't available, extend the free trial first.
  5. Click **Upgrade**.

After your instance is upgraded you can [Modify your instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance) to configure replication, autoscaling and other options.




## Delete the Bigtable free trial instance

**Warning:** Deleting a Bigtable free trial instance permanently removes the instance and all its data. You can't undo this later. Also, **you can't create another Bigtable free trial instance** after you've deleted your first Bigtable free trial instance. You can create one Bigtable free trial instance per project lifecycle.

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click your Bigtable free trial instance (`free-trial-instance`).

  3. Click **Delete instance**.

  4. Confirm deletion by typing the instance ID and click **Delete**.




## Troubleshooting

The **Welcome to Bigtable** page doesn't have fields to create a Bigtable free trial instance
    You can create one Bigtable free trial instance per project. If you've already created a Bigtable free trial instance in your project, you can't create another one, even if you delete the original instance.

## What's next

  * Learn more about [Bigtable free trial instance](https://docs.cloud.google.com/bigtable/docs/free-trial-instance).
  * Learn more about Bigtable [Instances, clusters, and nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes).
  * Learn more about [modifying your instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance).
  * For details on Bigtable pricing after the free trial period, see the [Pricing page](https://docs.cloud.google.com/bigtable/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
