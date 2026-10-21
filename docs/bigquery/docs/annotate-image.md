---
url: https://docs.cloud.google.com/bigquery/docs/annotate-image/
title: Annotate images with the ML.ANNOTATE_IMAGE function \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:22.334357+00:00
---

# Annotate images with the ML.ANNOTATE_IMAGE function  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/annotate-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback 

#  Annotate images with the ML.ANNOTATE_IMAGE function Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial explains how to use the [`ML.ANNOTATE_IMAGE` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-annotate-image) to extract insights from unstructured image data. When you work with large repositories of images, you might need to automatically categorize the files, detect specific objects, or extract image properties to make the dataset searchable. By creating a BigQuery ML [remote model](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-service) that connects to the Cloud Vision API, you can perform these image analysis tasks directly on a BigQuery [object table](https://docs.cloud.google.com/bigquery/docs/object-table-introduction) using standard SQL, eliminating the need to move files or build complex data pipelines. 

## Objectives

  * Create a dataset and a resource connection.
  * Create an object table for image files stored in Cloud Storage.
  * Create a remote model that connects to the Cloud Vision API.
  * Annotate images using the `ML.ANNOTATE_IMAGE` function. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [Cloud Vision API](https://cloud.google.com/vision/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigQuery, BigQuery Connection API, and Cloud Vision API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,bigqueryconnection.googleapis.com,vision.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigQuery, BigQuery Connection API, and Cloud Vision API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,bigqueryconnection.googleapis.com,vision.googleapis.com)




### Required roles

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on the project: 

  * Create and use BigQuery datasets, tables, and models: [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) 
  * Create, delegate, and use BigQuery connections: [BigQuery Connection Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.connectionAdmin) (`roles/bigquery.connectionAdmin`) 
  * Grant permissions to the connection's service account: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * Create BigQuery jobs: [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a dataset

To create a BigQuery dataset, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In **Explorer** , expand your project, and then click **Datasets**.

  4. On the **Datasets** page, click add **Create dataset**.

  5. In the **Create dataset** pane, do the following:

     * For **Dataset ID** , enter `bqml_tutorial`.

     * For **Data location** , select **US**.

Leave the remaining default settings as they are.

  6. Click **Create dataset**.




### bq

To create a new dataset, use the [`bq mk --dataset` command](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#mk-dataset).

  1. Create a dataset named `bqml_tutorial` with the data location set to `US`:
         
         bq mk --dataset \
           --location=US \
           --description "BigQuery ML tutorial dataset." \
           bqml_tutorial

  2. Confirm that the dataset was created:
         
         bq ls




###  API 

Call the [`datasets.insert`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets/insert) method with a defined [dataset resource](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets):
    
    
    {
      "datasetReference": {
         "datasetId": "bqml_tutorial"
      }
    }

## Create an object table

[Create an object table](https://docs.cloud.google.com/bigquery/docs/object-tables) named `my_object_table` that has image contents. The object table makes it possible to analyze the images without moving them from Cloud Storage.

The Cloud Storage bucket used by the object table should be in the same project where you plan to create the model and call the `ML.ANNOTATE_IMAGE` function. If you want to call the `ML.ANNOTATE_IMAGE` function in a different project than the one that contains the Cloud Storage bucket used by the object table, you must [grant the Storage Admin role at the bucket level](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

## Create a model

Create a remote model named `my_model` with a [`REMOTE_SERVICE_TYPE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-service#remote_service_type) of `CLOUD_AI_VISION_V1`:
    
    
    CREATE OR REPLACE MODEL
    `PROJECT_ID.bqml_tutorial.my_model`
    REMOTE WITH CONNECTION DEFAULT
    OPTIONS (REMOTE_SERVICE_TYPE = 'CLOUD_AI_VISION_V1');

Replace `PROJECT_ID` with your project ID.

## Annotate images

Use the `ML.ANNOTATE_IMAGE` function with your preferred [features](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-annotate-image#syntax) to annotate images in the object table.

  1. To label the items shown in the images, use the `ML.ANNOTATE_IMAGE` function with the [`label_detection`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-annotate-image#syntax) feature:
         
         SELECT *
         FROM ML.ANNOTATE_IMAGE(
         MODEL `PROJECT_ID.bqml_tutorial.my_model`,
         TABLE `PROJECT_ID.bqml_tutorial.my_object_table`,
         STRUCT(['label_detection'] AS vision_features)
         );

Replace `PROJECT_ID` with your project ID.

  2. To detect any faces shown in the images and return image attributes, like dominant colors, use the `ML.ANNOTATE_IMAGE` function with the [`face_detection`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-annotate-image#syntax) and [`image_properties`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-annotate-image#syntax) features:
         
         SELECT *
         FROM ML.ANNOTATE_IMAGE(
         MODEL `PROJECT_ID.bqml_tutorial.my_model`,
         TABLE `PROJECT_ID.bqml_tutorial.my_object_table`,
         STRUCT(['face_detection', 'image_properties'] AS vision_features)
         );

Replace `PROJECT_ID` with your project ID.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

###  Console 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



###  gcloud 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

If you plan to keep the project you used for this tutorial, you can avoid incurring further charges by deleting the individual resources you created:

  1. **Delete the dataset:** deleting the dataset also removes the remote model and the object table you created inside it.

     * In the Google Cloud console, go to [BigQuery Studio](https://console.cloud.google.com/bigquery).
     * In the **Explorer** pane, expand your project and select the dataset you created.
     * Click more_vert **View actions** , and then click **Delete**.
     * In the dialog, type `delete`, and then click **Delete**.
  2. **Delete the connection:**

     * In the **Explorer** pane, expand your project name and click **Connections**.
     * Click the more_vert **View actions** icon next to the connection you created, and select **Delete**.
     * In the dialog, click **Delete** to confirm. 



## What's next

  * For more information about model inference in BigQuery ML, see [Model inference overview](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/inference-overview).
  * For more information about using Cloud AI APIs to perform AI tasks, see [AI application overview](https://docs.cloud.google.com/bigquery/docs/ai-application-overview).
  * For information about supported SQL statements and functions for generative AI models, see [End-to-end user journeys for generative AI models](https://docs.cloud.google.com/bigquery/docs/e2e-journey-genai).
  * Try the [Unstructured data analytics with BigQuery ML and Gemini Enterprise Agent Platform pre-trained models](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/bigquery_ml/bq_ml_with_vision_translation_nlp.ipynb) notebook. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
