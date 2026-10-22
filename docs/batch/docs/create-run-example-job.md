---
url: https://docs.cloud.google.com/batch/docs/create-run-example-job/
title: Quickstart: create and run an example job \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:43.474175+00:00
---

# Quickstart: create and run an example job  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-example-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and run an example job

Learn how to create and run an example batch processing job that transcodes videos by using Batch for Google Cloud.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=batch--create-run-example-job)

* * *

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

  7. Enable the Batch, Compute Engine, Logging and Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable batch.googleapis.com compute.googleapis.com logging.googleapis.com storage.googleapis.com

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

  13. Enable the Batch, Compute Engine, Logging and Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable batch.googleapis.com compute.googleapis.com logging.googleapis.com storage.googleapis.com

  14. Make sure that you and the job's service account have the required permissions to complete this tutorial. This tutorial uses default service account for a job, which is the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). 

**Note** : If you created a new project, this step isn't required: 
     * As the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which already has all the permissions required for this tutorial. 
     * In a new project, the Compute Engine default service account is automatically granted the Editor role (`roles/editor`), which already has all the permissions required for this tutorial. 
     * To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles: 

       * To create, view, and delete jobs: 
         * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
         * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account
       * To create, view, and delete Cloud Storage buckets: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the project 
       * To view logs from jobs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

     * To ensure that the Compute Engine default service account has the necessary permissions to complete this tutorial, ask your administrator to grant the following IAM roles to the Compute Engine default service account: 

**Important:** You must grant these roles to the Compute Engine default service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 
       * [Batch Agent Reporter ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.agentReporter) (`roles/batch.agentReporter`) on the project
       * To let jobs access Cloud Storage buckets: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the project 
       * To let jobs generate logs in Logging: [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the project 

  15. Clone the [ Batch git repository](https://github.com/GoogleCloudPlatform/batch-samples) into the current directory: 
         
         git clone https://github.com/GoogleCloudPlatform/batch-samples.git

  16. Go to the `transcoding` directory: 
         
         cd batch-samples/transcoding/




## Prepare job inputs

  1. Create a Cloud Storage bucket:
         
         gcloud storage buckets create gs://BUCKET_NAME
         

Replace `BUCKET_NAME` with a globally unique name for the bucket.

**Caution:** Don't include sensitive information in a Cloud Storage bucket name. A bucket name is global and publicly visible.

The output is similar to the following:
         
         Creating gs://BUCKET_NAME/...
         

  2. Copy the `transcode.sh` script and the folder containing the video files to your Cloud Storage bucket:
         
         gcloud storage cp -R transcode.sh input gs://BUCKET_NAME
         

The output is similar to the following:
         
         Copying file://transcode.sh to gs://BUCKET_NAME/transcode.sh
         Copying file://input/video-2.mp4 to gs://BUCKET_NAME/input/video-2.mp4
         Copying file://input/video-1.mp4 to gs://BUCKET_NAME/input/video-1.mp4
         Copying file://input/video-0.mp4 to gs://BUCKET_NAME/input/video-0.mp4
           Completed files 4/4 | 37.5MiB/37.5MiB
         
         Average throughput: 48.4MiB/s
         




## Create a job

  1. In a text editor of your choice, open the `job.json` configuration file.

  2. Set the value of the `remotePath` field to the name of your Cloud Storage bucket:
         
         {
           "taskGroups": [
             {
               "taskSpec": {
                 "runnables": [
                   {
                     "script": {
                       "text": "bash /mnt/share/transcode.sh"
                     }
                   }
                 ],
                 "computeResource": {
                   "cpuMilli": 2000,
                   "memoryMib": 2048
                 },
                 "volumes": [
                   {
                     "gcs": {
                       **"remotePath" : "BUCKET_NAME"**
                     },
                     "mountPath": "/mnt/share"
                   }
                 ],
                 "maxRetryCount": 2,
                 "maxRunDuration": "600s"
               },
               "taskCount": 3,
               "parallelism": 3
             }
           ],
           "allocationPolicy": {
             "instances": [
               {
                 "policy": {
                   "machineType": "n2d-standard-4",
                   "provisioningModel": "SPOT"
                 }
               }
             ]
           },
           "labels": {
             "department": "creative",
             "env": "testing"
           },
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

  3. Save your changes and close the text editor.

  4. Create the `transcode` job:
         
         gcloud batch jobs submit transcode \
             --config=job.json \
             --location=us-central1
         

The output is similar to the following:
         
         Job transcode-7a1654ca-211c-40e8-b0fb-8a00 was successfully submitted.
         ...
         

The job runs 3 tasks concurrently. Each task runs the `transcode.sh` script, which encodes 1 of 3 video files and uploads it to the Cloud Storage bucket.




## Monitor the job

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. In the **Job name** column, click **transcode**.

The **Job details** page opens.

  3. Click the **Events** tab.

In the **Events list** section you can monitor the status of the `transcode` job. The time the job takes to finish being queued, scheduled, and running varies based on multiple factors. For this example, you can expect the job to be all finished in approximately 5 minutes.

  4. Optional: To update the page, click refresh **Refresh**.




Before proceeding to the next step, make sure that the status of the job is set to **Succeeded**. If your job fails, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting) instead.

## View the encoded videos

  1. In the Google Cloud console, go to the **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the **Name** column, click **BUCKET_NAME**.

The **Bucket details** page opens.

  3. In the **Name** column, click folder **output/** , and then click one of the encoded video files.

The **Object details** page opens.

  4. To view the encoded video, click **Preview** , and then click play_arrow **Play**.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

### Delete the project

The easiest way to eliminate billing is to delete the project you used in this tutorial.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

### Delete individual resources

If you want to keep using the current project, then delete the individual resources used in this tutorial.

#### Delete the job

After the Batch job has finished running, delete the `transcode` job:
    
    
    gcloud batch jobs delete transcode \
        --location=us-central1
    

The output is similar to the following:
    
    
    Job projects/example-project/locations/us-central1/jobs/transcode deletion is in progress
    

Deleting a job also deletes the job's details and history. The job's logs are automatically deleted at the end of the [Cloud Logging log retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

#### Delete the bucket

If you no longer need the Cloud Storage bucket you used in this tutorial and its content, delete the bucket:
    
    
    gcloud storage rm gs://BUCKET_NAME \
        --recursive
    

The output is similar to the following:
    
    
    Removing objects:
    Removing gs://BUCKET_NAME/input/video-0.mp4#1694788495332395...
    Removing gs://BUCKET_NAME/input/video-2.mp4#1694788495296173...
    Removing gs://BUCKET_NAME/input/video-1.mp4#1694788495228839...
    Removing gs://BUCKET_NAME/output/video-0.mp4#1694788495332395...
    Removing gs://BUCKET_NAME/output/video-2.mp4#1694788495296173...
    Removing gs://BUCKET_NAME/output/video-1.mp4#1694788495228839...
    Removing gs://BUCKET_NAME/transcode.sh#1694788495039427...
      Completed 4/4
    Removing Buckets:
    Removing gs://BUCKET_NAME/...
      Completed 1/1
    

#### Delete the git repository

If you no longer need the Batch git repository that you cloned for this tutorial, you can delete it:
    
    
    cd ../../ && rm -rf batch-samples
    

## What's next

  * Learn how to [get started with Batch](https://docs.cloud.google.com/batch/docs/get-started).

  * Learn more about [job creation and execution](https://docs.cloud.google.com/batch/docs/create-run-job).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
