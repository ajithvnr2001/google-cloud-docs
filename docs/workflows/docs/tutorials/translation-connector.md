---
url: https://docs.cloud.google.com/workflows/docs/tutorials/translation-connector/
title: Run a batch translation using the Cloud Translation connector \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:23.244858+00:00
---

# Run a batch translation using the Cloud Translation connector  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/tutorials/translation-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Run a batch translation using the Cloud Translation connector Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to create a workflow that uses the [Cloud Translation API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/translate/Overview) to translate files to other languages in asynchronous batch mode. This provides real-time output as the inputs are being processed.

## Objectives

In this tutorial you will:

  1. Create an input Cloud Storage bucket.
  2. Create two files in English and upload them to the input bucket.
  3. Create a workflow that uses the Cloud Translation API connector to translate the two files to French and Spanish and saves the results in an output bucket.
  4. Deploy and execute the workflow to orchestrate the entire process.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Translation](https://docs.cloud.google.com/translate)
  * [Workflows](https://docs.cloud.google.com/workflows)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Storage, Translation, and Workflows APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable storage.googleapis.com translate.googleapis.com workflows.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Storage, Translation, and Workflows APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable storage.googleapis.com translate.googleapis.com workflows.googleapis.com

  14. Update gcloud components: 
         
         gcloud components update

  15. Log in using your account: 
         
         gcloud auth login

  16. Set the default location used in this tutorial: 
         
         gcloud config set workflows/location us-central1

Since this tutorial uses the default AutoML Translation model which resides in `us-central1`, you must set the location to `us-central1`.

If using an AutoML Translation model or glossary other than the default, ensure that it resides in the same [location](https://docs.cloud.google.com/workflows/docs/locations) as the call to the connector; otherwise, an `INVALID_ARGUMENT (400)` error is returned. For details, see the [batchTranslateText method](https://docs.cloud.google.com/workflows/docs/reference/googleapis/translate/v3beta1/projects.locations/batchTranslateText). 




## Create an input Cloud Storage bucket and files

You can use Cloud Storage to store objects. Objects are immutable pieces of data consisting of a file of any format, and are stored in containers called buckets.

  1. Create a Cloud Storage bucket to hold the files to translate:
         
         BUCKET_INPUT=${GOOGLE_CLOUD_PROJECT}-input-files
         gcloud storage buckets create gs://${BUCKET_INPUT}

  2. Create two files in English and upload them to the input bucket:
         
         echo "Hello World!" > file1.txt
         gcloud storage cp file1.txt gs://${BUCKET_INPUT}
         echo "Workflows connectors simplify calling services." > file2.txt
         gcloud storage cp file2.txt gs://${BUCKET_INPUT}




## Deploy and execute the workflow

A workflow is made up of a series of steps described using the Workflows syntax, which can be written in either YAML or JSON format. This is the workflow's definition. After creating a workflow, you deploy it to make it available for execution.

  1. Create a text file with the filename `workflow.yaml` and with the following content:
         
         main:
           steps:
           - init:
               assign:
               - projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
               - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
               - inputBucketName: ${projectId + "-input-files"}
               - outputBucketName: ${projectId + "-output-files-" + string(int(sys.now()))}
           - createOutputBucket:
                 call: googleapis.storage.v1.buckets.insert
                 args:
                   project: ${projectId}
                   body:
                     name: ${outputBucketName}
           - batchTranslateText:
               call: googleapis.translate.v3beta1.projects.locations.batchTranslateText
               args:
                   parent: ${"projects/" + projectId + "/locations/" + location}
                   body:
                       inputConfigs:
                         gcsSource:
                           inputUri: ${"gs://" + inputBucketName + "/*"}
                       outputConfig:
                           gcsDestination:
                             outputUriPrefix: ${"gs://" + outputBucketName + "/"}
                       sourceLanguageCode: "en"
                       targetLanguageCodes: ["es", "fr"]
               result: batchTranslateTextResult

The workflow assigns variables, creates an output bucket, and initiates the translation of the files, saving the results to the output bucket.

  2. After creating the workflow, deploy it:
         
         gcloud workflows deploy batch-translation --source=workflow.yaml

  3. Execute the workflow:
         
         gcloud workflows execute batch-translation

  4. To view the workflow status, you can run the returned command. For example:
         
         gcloud workflows executions describe eb4a6239-cffa-4672-81d8-d4caef7d8424 /
           --workflow batch-translation /
           --location us-central1

The workflow should be `ACTIVE`. After a few minutes, the translated files (in French and Spanish) are uploaded to the output bucket.




## List objects in the output bucket

You can confirm that the workflow worked as expected by listing the objects in your output bucket.

  1. Retrieve your output bucket name:
         
         gcloud storage ls

The output is similar to the following: 
         
         gs://PROJECT_ID-input-files/
         gs://PROJECT_ID-output-files-TIMESTAMP/

  2. List the objects in your output bucket:
         
         gcloud storage ls gs://PROJECT_ID-output-files-TIMESTAMP/** --recursive

After a few minutes, the translated files, two of each in French and Spanish, are listed.




## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and wish to keep it without the changes added in this tutorial, delete resources created for the tutorial.

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



### Delete tutorial resources

  1. Remove the gcloud default configuration you added during the tutorial setup:
         
         gcloud config unset workflows/location

  2. Delete the workflow created in this tutorial:
         
         gcloud workflows delete WORKFLOW_NAME

  3. Delete a bucket and its objects created in this tutorial:
         
         gcloud storage rm gs://BUCKET_NAME --recursive

Where `BUCKET_NAME` is the name of the bucket to delete. For example, `my-bucket`.

The response is similar to the following:
         
         Removing gs://my-bucket/...

**Note:** If you have to delete a large number of objects in your buckets, avoid using the gcloud CLI, as the operation takes a long time to complete. Instead, use the Google Cloud console or [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle).



## What's next

  * To learn more about Workflows, see [Understand Workflows](https://docs.cloud.google.com/workflows/docs/overview).
  * To learn more about the Workflows syntax, see the [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax).
  * To learn more about Workflows connectors, see [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
