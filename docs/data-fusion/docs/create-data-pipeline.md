---
url: https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline/
title: Create a data pipeline by using Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:20.377614+00:00
---

# Create a data pipeline by using Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a data pipeline

This quickstart shows you how to do the following:

  1. Create a Cloud Data Fusion instance.
  2. Deploy a sample pipeline that's provided with your Cloud Data Fusion instance. The pipeline does the following: 
     1. Reads a JSON file containing NYT bestseller data from Cloud Storage.
     2. Runs transformations on the file to parse and clean the data.
     3. Loads the top-rated books added in the last week that cost less than $25 into BigQuery.



## Before you begin

Complete the following steps before creating a data pipeline.

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Cloud Data Fusion API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com)

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Cloud Data Fusion API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com)




### Required roles

To get the permissions that you need to create a Cloud Data Fusion instance and manage pipelines, ask your administrator to grant you the [Cloud Data Fusion Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To ensure that the Compute Engine default service account has the necessary permissions to run the Managed Service for Apache Spark job, ask your administrator to grant the following IAM roles to the Compute Engine default service account on your project: 

**Important:** You must grant these roles to the Compute Engine default service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)
  * [Cloud Data Fusion Runner ](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.runner) (`roles/datafusion.runner`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Compute Engine default service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud Data Fusion instance

  1. Click **Create an instance**. 

[ Go to Instances](https://console.cloud.google.com/data-fusion/instance-create)

  2. Enter an **Instance name**.
  3. Enter a **Description** for your instance.
  4. Enter the **Region** in which to create the instance.
  5. Choose the Cloud Data Fusion **Version** to use.
  6. Choose the Cloud Data Fusion [**Edition**](https://cloud.google.com/data-fusion/pricing).
  7. For Cloud Data Fusion versions 6.2.3 and later, in the **Authorization** field, choose the [**Managed Service for Apache Spark service account**](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts) to use for running your Cloud Data Fusion pipeline in Managed Service for Apache Spark. The default value, Compute Engine account, is pre-selected.
  8. Click **Create**. It takes up to 30 minutes for the instance creation process to complete. While Cloud Data Fusion creates your instance, a progress wheel displays next to the instance name on the **Instances** page. After completion, it turns into a green check mark and indicates that you can start using the instance.



## Navigate the Cloud Data Fusion web interface

When using Cloud Data Fusion, you use both the Google Cloud console and the separate Cloud Data Fusion web interface.

  * In the Google Cloud console, you can do the following:

    * Create a Google Cloud console project
    * Create and delete Cloud Data Fusion instances
    * View the Cloud Data Fusion instance details
  * In the Cloud Data Fusion web interface, you can use various pages, such as **Studio** or **Wrangler** , to use Cloud Data Fusion functionality.




To navigate the Cloud Data Fusion interface, follow these steps:

  1. In the Google Cloud console, open the **Instances** page. 

[ Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the instance **Actions** column, click the **View Instance** link.
  3. In the Cloud Data Fusion web interface, use the left navigation panel to navigate to the page you need.



## Deploy a sample pipeline

Sample pipelines are available through the Cloud Data Fusion **Hub** , which lets you share reusable Cloud Data Fusion pipelines, plugins, and solutions.

  1. In the Cloud Data Fusion web interface, click **Hub**.
  2. In the left panel, click **Pipelines**.
  3. Click the **Cloud Data Fusion Quickstart** pipeline.
  4. Click **Create**.
  5. In the Cloud Data Fusion Quickstart configuration panel, click **Finish**.
  6. Click **Customize Pipeline**.

A visual representation of your pipeline appears on the **Studio** page, which is a graphical interface for developing data integration pipelines. Available pipeline plugins are listed on the left, and your pipeline is displayed on the main canvas area. You can explore your pipeline by holding the pointer over each pipeline _node_ and clicking **Properties**. The properties menu for each node lets you view the objects and operations associated with the node.

  7. In the top-right menu, click **Deploy**. This step submits the pipeline to Cloud Data Fusion. You will execute the pipeline in the next section of this quickstart.




![Deploy the pipeline](https://docs.cloud.google.com/static/data-fusion/docs/images/quickstart/studio-deploy.png)

### View your pipeline

The deployed pipeline appears in the pipeline details view, where you can do the following:

  * View the structure and configuration of the pipeline.
  * Run the pipeline manually or set up a schedule or a trigger.
  * View a summary of historical runs of the pipeline, including execution times, logs, and metrics.



![Copy the service account](https://docs.cloud.google.com/static/data-fusion/docs/images/quickstart/studio-details.png)

## Execute your pipeline

In the pipeline details view, click **Run** to execute your pipeline.

![Run the pipeline](https://docs.cloud.google.com/static/data-fusion/docs/images/quickstart/details-run.png)

When executing a pipeline, Cloud Data Fusion does the following:

  1. Provisions an ephemeral Managed Service for Apache Spark cluster
  2. Executes the pipeline on the cluster using Apache Spark
  3. Deletes the cluster

**Note:** When the pipeline transitions to the _Running_ state, you can [monitor the Managed Service for Apache Spark cluster creation and deletion](https://console.cloud.google.com/dataproc/clusters). This cluster only exists for the duration of the pipeline.

## View the results

After a few minutes, the pipeline finishes. The pipeline status changes to **Succeeded** and the number of records processed by each node is displayed.

![Pipeline run complete](https://docs.cloud.google.com/static/data-fusion/docs/images/quickstart/run-complete.png)

  1. Go to the [BigQuery web interface](https://console.cloud.google.com/bigquery).
  2. To view a sample of the results, go to the `DataFusionQuickstart` dataset in your project, click the `top_rated_inexpensive` table, then run a simple query. For example:
         
         SELECT * FROM PROJECT_ID.GCPQuickStart.top_rated_inexpensive LIMIT 10
         

Replace PROJECT_ID with your project ID.




![View results](https://docs.cloud.google.com/static/data-fusion/docs/images/quickstart/bigquery-results-2.png)

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. [Delete the BigQuery dataset](https://console.cloud.google.com/bigquery) that your pipeline wrote to in this quickstart.
  2. [Delete the Cloud Data Fusion instance](https://console.cloud.google.com/data-fusion/locations/-/instances).

**Note:** Deleting your instance does not delete any of your data in the project.
  3. Optional: Delete the project.


**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Work through a Cloud Data Fusion [tutorial](https://docs.cloud.google.com/data-fusion/docs/tutorials/targeting-campaign-pipeline)
  * Learn about Cloud Data Fusion [concepts](https://docs.cloud.google.com/data-fusion/docs/concepts/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
