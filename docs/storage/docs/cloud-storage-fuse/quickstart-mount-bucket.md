---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/quickstart-mount-bucket/
title: Mount a Cloud Storage bucket using Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:12.363223+00:00
---

# Mount a Cloud Storage bucket using Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/quickstart-mount-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Mount a Cloud Storage bucket using Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) lets you mount a Cloud Storage bucket as a local file system, so you can interact with your objects using standard file system semantics. In this quickstart, you install Cloud Storage FUSE on Debian or Ubuntu, mount a bucket as a folder on your machine, and upload an object to the bucket.

You'll use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) to create and manage the object in your storage bucket, and you'll use the [Cloud Storage FUSE CLI](https://github.com/GoogleCloudPlatform/gcsfuse) to mount your bucket to your machine.

## Before you begin

To set up a project, complete the following steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Make sure that you have the following role or roles on the project: Storage Admin (`roles/storage.admin`), Storage Bucket Viewer (`roles/storage.bucketViewer`) 

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
  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Make sure that you have the following role or roles on the project: Storage Admin (`roles/storage.admin`), Storage Bucket Viewer (`roles/storage.bucketViewer`) 

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
  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Have a Cloud Storage bucket that you want to mount. If you don't already have one, [create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).



## Install Cloud Storage FUSE

To install Cloud Storage FUSE, follow the instructions in [Install Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/install).

## Mount the bucket

To mount the bucket to your local file system, complete the following steps:

  1. Generate Application Default Credentials using the `gcloud auth application-default login` command:
         
         gcloud auth application-default login

Cloud Storage FUSE automatically loads the credentials.

  2. Create a directory to mount the storage bucket to:
         
         mkdir "$HOME/mount-folder"

  3. Mount your storage bucket using the `gcsfuse` command:
         
         gcsfuse BUCKET_NAME "$HOME/mount-folder"

Replace BUCKET_NAME with the name of the bucket you want to mount.

If successful, the command returns output which contains text similar to the following:
         
         File system has been successfully mounted.




## Upload an object into the bucket

To download an example object and upload it to the mounted bucket, complete the following steps:

![The image of a kitten to upload into the bucket.](https://docs.cloud.google.com/static/storage/images/kitten.png)

  1. Right-click the image and save it somewhere on your computer, such as on the desktop.

You can also download the image using the cURL command `curl -O https://cloud.google.com/storage/images/kitten.png`.

  2. Copy the image from its saved location to the folder where your bucket is mounted, using the `cp` command:
         
         cp kitten.png "$HOME/mount-folder/kitten.png"

  3. Verify that the image was copied to your local file system and uploaded to the bucket successfully by following the steps:

     1. To check that `kitten.png` was copied to your local file system, run `ls` on the folder where your bucket is mounted:
            
            ls "$HOME/mount-folder"

If the copy operation was successful, `kitten.png` is returned in the output.

     2. To list the contents of your bucket, use the `gcloud storage ls` command:
            
            gcloud storage ls gs://BUCKET_NAME

Replace BUCKET_NAME with the name of your bucket.

If the image was successfully uploaded to your bucket, `kitten.png` is returned in the output.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the resources by completing the following steps:

  1. Unmount the storage bucket from your Linux machine by using the `fusermount` tool:
         
         fusermount -u "$HOME/mount-folder"

  2. To delete the bucket and everything inside of it, use the `gcloud storage rm` command with the `--recursive` flag:
         
         gcloud storage rm gs://BUCKET_NAME --recursive

Replace BUCKET_NAME with the name of your bucket.

If successful, the command returns output similar to the following:
         
         Removing gs://my-bucket/kitten.png#1676488739323620...
          Removing gs://my-bucket/...




## What's next

  * Get a [detailed overview of Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview).

  * Read about ways to [mount buckets for different use cases](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#examples).

  * Learn how to use [Cloud Storage agent skills](https://docs.cloud.google.com/storage/docs/agents-skills-overview#fuse-skill) to automate mounting and cache configuration with AI coding assistants.



  * Learn how [Vertex AI uses Cloud Storage FUSE](https://docs.cloud.google.com/vertex-ai/docs/training/code-requirements#fuse) to mount Cloud Storage buckets for custom training jobs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
