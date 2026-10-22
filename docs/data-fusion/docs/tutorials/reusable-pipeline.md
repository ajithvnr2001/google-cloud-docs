---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/reusable-pipeline/
title: Design and create a reusable pipeline \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:42.902396+00:00
---

# Design and create a reusable pipeline  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/reusable-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Design and create a reusable pipeline Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to build a reusable pipeline that reads data from Cloud Storage, performs data quality checks, and writes to Cloud Storage.

Reusable pipelines have a regular pipeline structure, but you can change the configuration of each [pipeline node](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#pipeline_node) based on configurations provided by an HTTP server. For example, a static pipeline might read data from Cloud Storage, apply transformations, and write to a BigQuery output table. If you want the transformation and BigQuery output table to change based on the Cloud Storage file that the pipeline reads, you create a reusable pipeline.

## Objectives

  * Use the Cloud Storage Argument Setter plugin to allow the pipeline to read different input in every run.
  * Use the Cloud Storage Argument Setter plugin to allow the pipeline to perform different quality checks in every run.
  * Write the output data of each run to Cloud Storage.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Data Fusion
  * Cloud Storage



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

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Data Fusion, Cloud Storage, BigQuery, and Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,storage.googleapis.com,bigquery.googleapis.com,dataproc.googleapis.com&redirect=https%3A//console.cloud.google.com)

  7. [ Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance#creating_an_instance).



### Navigate to the Cloud Data Fusion web interface

When using Cloud Data Fusion, you use both the Google Cloud console and the separate Cloud Data Fusion web interface. In the Google Cloud console, you can create a Google Cloud console project, and create and delete Cloud Data Fusion instances. In the Cloud Data Fusion web interface, you can use the various pages, such as **Pipeline Studio** or **Wrangler** , to use Cloud Data Fusion features.

  1. In the Google Cloud console, open the **Instances** page. 

[Open the Instances page](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the **Actions** column for the instance, click the **View Instance** link. The Cloud Data Fusion web interface opens in a new browser tab.




## Deploy the Cloud Storage Argument Setter plugin

  1. In the Cloud Data Fusion web interface, go to the **Studio** page.

  2. In the **Actions** menu, click **GCS Argument Setter**.




## Read from Cloud Storage

  1. In the Cloud Data Fusion web interface, go to the **Studio** page.
  2. Click _arrow_drop_down_ **Source** and select Cloud Storage. The node for a Cloud Storage source appears in the pipeline.
  3. On the Cloud Storage node, click **Properties**.

![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/reusable-pipeline/configure-gcs.png)
  4. In the **Reference name** field, enter a name.

  5. In the **Path** field, enter `${input.path}`. This macro controls what the Cloud Storage input path will be in the different pipeline runs.

  6. In the right Output Schema panel, remove the **offset** field from the output schema by clicking the trash icon in the offset field row. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/reusable-pipeline/gcs-properties.png)

  7. Click **Validate** and address any errors.

  8. Click the close to exit the **Properties** dialog.




## Transform your data

  1. In the Cloud Data Fusion web interface, go to your data pipeline on the **Studio** page.
  2. In the **Transform** drop-down menu _arrow_drop_down_ , select **Wrangler**.
  3. In the Pipeline Studio canvas, drag an arrow from the Cloud Storage node to the Wrangler node. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/reusable-pipeline/connect-wrangler.png)
  4. Go to the Wrangler node in your pipeline and click the **Properties**.
  5. In the **Input field name** , enter `body`.
  6. In the **Recipe** field, enter `${directives}`. This macro controls what the transform logic will be in the different pipeline runs. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/reusable-pipeline/wrangler-properties.png)
  7. Click **Validate** and address any errors.
  8. Click the close to exit the **Properties** dialog.



## Write to Cloud Storage

  1. In the Cloud Data Fusion web interface, go to your data pipeline on the **Studio** page.
  2. In the **Sink** drop-down menu _arrow_drop_down_ , select Cloud Storage.
  3. In the Pipeline Studio canvas, drag an arrow from the Wrangler node to the Cloud Storage node that you just added. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/reusable-pipeline/connect-gcs-sink.png)
  4. Go to the Cloud Storage sink node in your pipeline and click **Properties**.
  5. In the **Reference name** field, enter a name.
  6. In the **Path** field, enter the path of a Cloud Storage bucket in your project, where your pipeline can write the output files. If you don't have a Cloud Storage bucket, [create one](https://docs.cloud.google.com/storage/docs/creating-buckets). ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/reusable-pipeline/gcs-sink-properties.png)
  7. Click **Validate** and address any errors.
  8. Click the close to exit the **Properties** dialog.



## Set the macro arguments

  1. In the Cloud Data Fusion web interface, go to your data pipeline on the **Studio** page.
  2. In the _arrow_drop_down_ **Conditions and Actions** drop-down menu, click **GCS Argument Setter**.
  3. In the Pipeline Studio canvas, drag an arrow from the Cloud Storage Argument Setter node to the Cloud Storage _source_ node. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/reusable-pipeline/connect-argument-setter.png)
  4. Go to the Cloud Storage Argument Setter node in your pipeline and click **Properties**.
  5. In the **URL** field, enter the following URL:
         
         gs://reusable-pipeline-tutorial/args.json
         

The URL corresponds to a publicly accessible object in Cloud Storage that contains the following content:
         
         {
           "arguments" : [
             {
               "name": "input.path",
               "value": "gs://reusable-pipeline-tutorial/user-emails.txt"
             },
             {
               "name": "directives",
               "value": "send-to-error !dq:isEmail(body)"
             }
           ]
         }
         

The first of the two arguments is the value for `input.path`. The path `gs://reusable-pipeline-tutorial/user-emails.txt` is a publicly accessible object in Cloud Storage that contains the following test data:
         
         alice@example.com
         bob@example.com
         craig@invalid@example.com
         

The second argument is the value for `directives`. The value `send-to-error !dq:isEmail(body)` configures Wrangler to filter out any lines that are not a valid email address. For example, `craig@invalid@example.com` is filtered out.

  6. Click **Validate** to make sure you don't have any errors.

  7. Click the close to exit the **Properties** dialog.




## Deploy and run your pipeline

  1. In the top bar of the **Pipeline Studio** page, click **Name your pipeline**. Name your pipeline and click **Save**.

  2. Click **Deploy**.

  3. To open the **Runtime Arguments** and view the macro (runtime) `input.path` and `directives` arguments, click the _arrow_drop_down_ drop-down next to **Run**.

Leave the value fields blank to notify Cloud Data Fusion that the Cloud Storage Argument Setter node in the pipeline will set the values of these arguments during runtime. ![](https://docs.cloud.google.com/static/data-fusion/docs/images/tutorials/reusable-pipeline/run.png)

  4. Click **Run**.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you've finished the tutorial, clean up the resources you created on Google Cloud so they won't take up quota and you won't be billed for them in the future. The following sections describe how to delete or turn off these resources.

### Delete the Cloud Data Fusion instance

Follow the [instructions to delete your Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).

### Delete the project

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



## What's next

  * Read the [how-to guides](https://docs.cloud.google.com/data-fusion/docs/how-to)
  * Work through another [tutorial](https://docs.cloud.google.com/data-fusion/docs/tutorials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
