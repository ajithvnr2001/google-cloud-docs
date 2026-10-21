---
url: https://docs.cloud.google.com/run/docs/tutorials/video-encoding/
title: GPU-accelerated video transcoding with FFmpeg on Cloud Run jobs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:56.429651+00:00
---

# GPU-accelerated video transcoding with FFmpeg on Cloud Run jobs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/video-encoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  GPU-accelerated video transcoding with FFmpeg on Cloud Run jobs Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to transcode low-priority offline videos using Cloud Run jobs.

## Objectives

In this tutorial, you will do the following:

  * Create Cloud Storage buckets to store the videos for processing and to store the encoding results.
  * Deploy a Cloud Run job using GPUs to accelerate video transcoding.
  * Run the job and make sure the video transcoded successfully.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build/docs)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Run](https://cloud.google.com/run)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

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

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Cloud Run, Artifact Registry, and Cloud Build APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com

  13. Set your region as an environment variable: 
         
         export REGION=REGION

  14. Create a service account: 
         
         gcloud iam service-accounts create video-encoding

  15. By default, new projects are automatically granted 3 GPU quota upon initial deployment. If you need additional quota, request `Total Nvidia L4 GPU allocation without zonal redundancy, per project per region` quota under Cloud Run Admin API in the [Quotas and system limits page](https://g.co/cloudrun/gpu-quota).



### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

#### Grant the roles

#### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address that is used to deploy the Cloud Run service.

  5. In the **Select a role** list, select a role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



#### gcloud

To grant the required IAM roles to your account on your project:
    
    
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=PRINCIPAL \
             --role=ROLE
         

Replace:

  * PROJECT_NUMBER with your Google Cloud project number.
  * PROJECT_ID with your Google Cloud project ID.
  * PRINCIPAL with the account you are adding the binding for. This is typically the email address that is used to deploy the Cloud Run service.
  * ROLE with the role you are adding to the deployer account.



## Prepare your application

To retrieve the code sample for use:

  1. Clone the sample repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/cloud-run-samples
         

  2. Change to the directory that contains the Cloud Run sample code:
         
         cd cloud-run-samples/jobs-video-encoding
         




## Create Cloud Storage buckets

To store the videos for processing, and to save the results of encoding, create the following two Cloud Storage buckets:

  1. Create a bucket to store videos before processing:
         
         gcloud storage buckets create gs://preprocessing-PROJECT_ID \
           --location LOCATION
         

Replace the following:

     * PROJECT_ID: your project ID.
     * LOCATION: the Cloud Storage location.
  2. Grant the service account access to read from this bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://preprocessing-PROJECT_ID \
           --member="serviceAccount:video-encoding@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/storage.objectViewer"
         

Replace PROJECT_ID with your project ID.

  3. Create a bucket to store transcoded videos after processing:
         
         gcloud storage buckets create gs://transcoded-PROJECT_ID \
           --location LOCATION
         

Replace the following:

     * PROJECT_ID: your project ID.
     * LOCATION: the Cloud Storage location.
  4. Grant the service account access to read from and write to this bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://transcoded-PROJECT_ID \
           --member="serviceAccount:video-encoding@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/storage.objectAdmin"
         

Replace PROJECT_ID with your project ID.




## Deploy a Cloud Run job

Create a Cloud Run job by using the Dockerfile in the sample repository and mounting the buckets that you created: 

  1. Navigate to the sample directory:
         
         cd cloud-run-samples/jobs-video-encoding
         




  1. Create an Artifact Registry if the default Cloud Run registry doesn't already exist:
         
         gcloud artifacts repositories create cloud-run-source-deploy \
           --repository-format=docker \
           --location LOCATION
         

Replace LOCATION with the name of the location of the registry.

  2. Build the container image:
         
         gcloud builds submit \
           --tag LOCATION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/IMAGE_NAME \
           --machine-type E2-HIGHCPU-32
         

Replace the following:

     * PROJECT_ID: your project ID.
     * LOCATION:name of the location of the registry.
     * IMAGE_NAME: name for the container image, for example: `ffmpeg-image`.

Cloud Run uses a larger machine type to reduce build time.

  3. Deploy the job:
         
         gcloud run jobs create video-encoding-job \
             --image LOCATION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/IMAGE_NAME \
             --region REGION \
             --memory 32Gi \
             --cpu 8 \
             --gpu 1 \
             --gpu-type nvidia-l4 \
             --no-gpu-zonal-redundancy \
             --max-retries 1 \
             --service-account video-encoding@PROJECT_ID.iam.gserviceaccount.com \
             --add-volume=name=input-volume,type=cloud-storage,bucket=preprocessing-PROJECT_ID,readonly=true \
             --add-volume-mount=volume=input-volume,mount-path=/inputs \
             --add-volume=name=output-volume,type=cloud-storage,bucket=transcoded-PROJECT_ID \
             --add-volume-mount=volume=output-volume,mount-path=/outputs
         

Replace the following:

     * PROJECT_ID: your project ID.
     * REGION: the name of the region. Note: This must be the same region that you have GPU quota for.
     * IMAGE_NAME: name for the container image, for example, `ffmpeg-image`.

If this is the first time you deployed from source in this project, Cloud Run prompts you to create a default Artifact Registry repository.




## Run the job

To run the job, follow these steps:

  1. Upload an example video to encode:
         
         gcloud storage cp gs://cloud-samples-data/video/cat.mp4 gs://preprocessing-PROJECT_ID
         

  2. Run the job:
         
         gcloud run jobs execute video-encoding-job  \
             --region REGION \
             --wait \
             --args="cat.mp4,encoded_cat.mp4,-vcodec,h264_nvenc,-cq,21,-movflags,+faststart"
         

The `entrypoint.sh` file requires an input file, output file, and any arguments to send to FFmpeg.

  3. Review the Cloud Run logs to make sure the video trancoded:
         
         gcloud run jobs logs read video-encoding-job --region REGION
         

  4. Download the transcoded video:
         
         gcloud storage cp gs://transcoded-PROJECT_ID/encoded_cat.mp4 .
         




## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this quickstart.

### Delete your repository

Cloud Run only charges for the time your job executes. However, you might still be [charged for storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing). To delete Artifact Registry repositories, follow the steps in [Delete repositories](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#delete) in the Artifact Registry documentation.

### Delete your job

Cloud Run jobs only incur cost when a job task is executing. To delete your Cloud Run job, follow one of these steps:

### Console

To delete a job:

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Locate the job you want to delete in the jobs list, and click its checkbox to select it.

  3. Click **Delete**. This terminates all the job executions in progress and all running container instances.




###  gcloud 

To delete a job, run the following command:
    
    
    gcloud run jobs delete JOB_NAME

Replace `JOB_NAME` with the name of the job.

### Delete your test project

Deleting your Google Cloud project stops billing for all resources in that project. To release all Google Cloud resources in your project, follow these steps:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * Explore other [Cloud Run demos, tutorials, and samples](https://docs.cloud.google.com/run/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
