---
url: https://docs.cloud.google.com/vision-ai/docs/face-blur-python/
title: Use the Face Blur model with the Python SDK \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:25.685469+00:00
---

# Use the Face Blur model with the Python SDK  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/face-blur-python/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Use the Face Blur model with the Python SDK Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use the Python SDK to blur faces in video. The example blurs video files from a Cloud Storage bucket and generates blurred video outputs. These output videos are stored to the same Cloud Storage bucket as the source videos.

## Objectives

This tutorial shows you how to do the following:

  * Create a Cloud Storage bucket.
  * Upload a local video file to the bucket.
  * Send a request using the Python SDK.
  * View blurred output videos.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Gemini Enterprise Agent Platform Vision](https://docs.cloud.google.com/vision-ai/pricing) (Models - Person / face blur) 
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

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

  7. Enable the Vertex AI Vision, Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable visionai.googleapis.com storage.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/visionai.editor, roles/storage.objectAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Vertex AI Vision, Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable visionai.googleapis.com storage.googleapis.com

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/visionai.editor, roles/storage.objectAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. Get the Gemini Enterprise Agent Platform Vision SDK source code: 
         
         git clone https://github.com/google/visionai.git

The Python examples are located in the `visionai/python/example/` directory. 

  19. Get the Python SDK: 
         
         wget https://github.com/google/visionai/releases/download/v0.0.5/visionai-0.0.5-py3-none-any.whl




## Add input files to Cloud Storage

Before you can send a request using the Python SDK, create a Cloud Storage bucket and upload a local video to use as input.

  1. Create a Cloud Storage bucket:
         
         gcloud storage buckets create gs://BUCKET_NAME
         

  2. Upload a local video file to the new bucket:
         
         gcloud storage cp LOCAL_FILE gs://BUCKET_NAME
         




## Install dependencies and send the request

After you create your Cloud Storage bucket for input and output videos and add a local video, install the necessary dependencies and send your request.

  1. Optional. Set up your virtual environment:

     1. If not installed, install `virtualenv`:
            
            sudo apt-get install python3-venv
            

     2. Create a new virtual environment:
            
            python3 -m venv vaivenv
            

     3. Activate your virtual environment:
            
            source vaivenv/bin/activate
            

  2. Install dependencies:
         
         pip3 install visionai-0.0.5-py3-none-any.whl
         pip3 install google-cloud-storage
         

  3. Send your request with the Python SDK.

Make the following variable substitutions:

     * PROJECT_ID: Your Google Cloud project ID.
     * LOCATION_ID: Your location ID. For example, `us-central1`. [More information](https://docs.cloud.google.com/about/locations). [Supported regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions).
     * BUCKET_NAME: The Cloud Storage bucket you created.
    
    python3 visionai/python/example/blur_gcs_video.py \
    --project_id=PROJECT_ID –cluster_id=application-cluster-0 \
    –location_id=LOCATION_ID –bucket_name=BUCKET_NAME
    

You should see output similar to the following:
    
    Listing mp4 files...
     test1.mp4
     test2.mp4
     Creating deid processes...
     process vnluvxgl is created
     process rvrdoucx is created
     Waiting for processes to finish...
     process vnluvxgl state is COMPLETED
     process rvrdoucx state is COMPLETED
     All processes have finished, please check the GCS bucket!
     ```
    




## Examine output

After your video has finished processing you can examine the output in your Cloud Storage bucket. The generated blurred video files will be in the same Cloud Storage bucket as the source video.

  1. List all objects in your bucket with the [`gcloud storage ls`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls) command:
         
         gcloud storage ls gs://bucket
         

You should see the source files and output files similar to the following:
         
         test1.mp4
         test2.mp4
         test1_deid_output.mp4
         test2_deid_output.mp4
         

  2. Optional. Download the output files locally with the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command and view the blurred videos:
         
         gcloud storage cp gs://BUCKET_NAME/FILE_NAME .
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

## What's next

  * Read more about the [Person blur model](https://docs.cloud.google.com/vision-ai/docs/person-blur-model).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
