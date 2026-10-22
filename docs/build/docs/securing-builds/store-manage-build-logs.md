---
url: https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs/
title: Store and view build logs \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:59.971935+00:00
---

# Store and view build logs  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Store and view build logs Stay organized with collections  Save and categorize content based on your preferences. 

Set up your build config file to store your build logs in log buckets so that you can group and analyze them using Cloud Logging and Cloud Storage tools. Configuring your build log storage allows for greater control over the storage and analysis of your logs. If you leave your build log storage settings undefined, then Cloud Build stores them in a Google Cloud-owned bucket with fewer options for build log analysis.

This page describes how to store build logs in different types of buckets, and how to view and delete stored logs.

## Before you begin

Ensure that you are familiar with the build config file options for configuring build log storage and how bucket ownership impacts log accessibility. For more information, see [Build log storage options](https://docs.cloud.google.com/build/docs/securing-builds/build-log-storage).

## Store build logs in user-created buckets

User-created buckets give you greater control over managing and configuring your buckets.

**Note:** You will incur a cost for storing build logs in your own bucket. For pricing details, see [Cloud Storage pricing](https://cloud.google.com/storage/pricing) and [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing).

### Store build logs in a user-created Cloud Logging bucket

User-created Logging buckets let you adjust the retention period of stored build logs. To store your build logs in a user-created bucket in Logging, do the following:

**Grant IAM permissions** :

To get the permissions that you need to store build logs in a user-created Cloud Logging bucket, ask your administrator to grant you the [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) IAM role on the account or service account for your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Configure the Logging bucket** :

  1. [Create a bucket](https://docs.cloud.google.com/logging/docs/buckets#create_bucket) and set a value for the **Retention period** field.

  2. [Create a sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#creating_sink) to route your build logs to your new bucket:

     1. Enter the following for your sink's build inclusion filter:
            
            logName = "projects/PROJECT_ID/logs/cloudbuild"
            

Replace PROJECT_ID with your Google Cloud project ID.

     2. (Optional) To prevent your build logs from going to the default Logging bucket, follow the example in [Stop storing log entries in log buckets](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#stopping_logs_ingestion).




### Store build logs in a user-created Cloud Storage bucket

To store your build logs in a user-created Cloud Storage bucket, do the following:

**Grant IAM permissions** :

If your Cloud Storage bucket and Cloud Build are in the same Google Cloud project and you're using the Cloud Build [legacy service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account), your Cloud Build legacy service account has the necessary IAM permissions by default. You don't have to grant any additional permissions. Otherwise, do the following:

To get the permissions that you need to store build logs in a user-created Cloud Storage bucket, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the service account used for your build. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Configure the Cloud Storage bucket** :

  1. In your Google Cloud project, [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-console) with no retention policy set to store your build logs.

  2. In your build config file, add a `logsBucket` field pointing to the Cloud Storage bucket that you created to store build logs. The following example build config file contains instructions to build a container image and store the build logs in a bucket named `mylogsbucket`:

###  YAML 
         
         steps:
             - name: 'gcr.io/cloud-builders/docker'
               args: [ 'build', '-t', 'us-east1-docker.pkg.dev/myproject/myimage', '.' ]
             logsBucket: 'gs://mylogsbucket'
             options:
               logging: GCS_ONLY
         

###  JSON 
         
         {
               "steps": [
                {
                  "name": "gcr.io/cloud-builders/docker",
                  "args": [
                    "build",
                    "-t",
                    "us-east1-docker.pkg.dev/myproject/myimage",
                    "."
                  ]
                }
                ],
                "logsBucket": "gs://mylogsbucket",
                "options": {
                  "logging": "GCS_ONLY"
                }
             }
         

  3. Use the build config file to start a build [using the command line, the API](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




When the build completes, Cloud Build stores the build logs in the Cloud Storage bucket you specified in the build config file.

## Store build logs in region-specific Cloud Storage buckets

You can configure your build so that Cloud Build sends build logs to a user-owned Cloud Storage bucket in the same region as your build. Aligning the regions of your build and build log storage bucket can help you comply with data residency requirements.

**Grant IAM permissions** :

If your Cloud Storage bucket and Cloud Build are in the same Google Cloud project and you're using the Cloud Build [legacy service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account), then that service account has the necessary IAM permissions by default. You don't have to grant any additional permissions. Otherwise, do the following:

To get the permissions that you need to store build logs in a user-owned and region-specific bucket, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the service account used for your build. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Configure the region-specific Cloud Storage bucket** :

  1. In your build config file, add the `defaultLogsBucketBehavior` option and set its value to `REGIONAL_USER_OWNED_BUCKET`:

###  YAML 
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           args: [ 'build', '-t', 'us-central1-docker.pkg.dev/myproject/myrepo/myimage', '.' ]
         options:
           defaultLogsBucketBehavior: REGIONAL_USER_OWNED_BUCKET
         

###  JSON 
         
         {
           "steps": [
             {
               "name": "gcr.io/cloud-builders/docker",
               "args": [
                 "build",
                 "-t",
                 "us-central1-docker.pkg.dev/myproject/myrepo/myimage",
                 "."
               ]
             }
             ],
             "options": {
               "defaultLogsBucketBehavior": "REGIONAL_USER_OWNED_BUCKET"
             }
         }
         

  2. Use the build config file to start a build [using the command line, the API](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

When you run your build, Cloud Build creates the new bucket in the region where you are executing your build, then stores the build logs in this bucket. Further builds in the same project and region will use the existing bucket as long as `REGIONAL_USER_OWNED_BUCKET` is active. This bucket is user-owned, so you can configure it as if it were a user-created bucket.

If you set the `REGIONAL_USER_OWNED_BUCKET` option and create builds in multiple regions, then Cloud Build creates a Cloud Storage bucket for each unique region.




You can also use a user-created bucket if you need to align your build's region and log bucket. In this case, you can either select an existing user-created bucket that has the same region, or create one. If you want to create one, then follow the steps to [Store build logs in user-created buckets](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-custom-buckets) and ensure that your user-created bucket has the same region as your build.

## View build logs

To view your build logs, do the following:

**Grant IAM permissions** :

To get the permissions that you need to view build logs in Cloud Storage or Logging, ask your administrator to grant you the following IAM roles on the service account used for your build: 

  * View build logs in a user-created or user-owned Cloud Storage bucket: 
    * Storage Object Viewer (`roles/storage.objectViewer`) - the principals who want to view build logs 
    * Logs View Accessor (`roles/logging.viewAccessor`) - the principals who want to view build logs 
  * View build logs in the default Cloud Storage bucket: Viewer (`roles/viewer`) - the project where the build is configured 
  * View build logs in Logging: Logs Viewer (`roles/logging.viewer`) - the principals who want to view build logs 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** You can grant the Owner (`roles/owner`) or Editor (`roles/editor`) roles at the project level to allow principals to view build logs from Cloud Build-created and user-owned buckets. However, we recommend using the Viewer role in this case so that your role assignment complies with the [security principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege). If you don't want to grant the basic Viewer role, use user-created buckets instead. We recommend this practice especially if your builds are invoked by [triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) and you only want to grant access to invoke builds and view build progress.

### View build logs in Google Cloud

###  Console 

  1. Open the Cloud Build page in the Google Cloud console.

[Open the Cloud Build page](https://console.cloud.google.com/cloud-build)

  2. Select your project and click **Open**.

  3. In the **Region** drop-down menu, select the [region](https://docs.cloud.google.com/build/docs/locations) for your build.

  4. In the **Build history** page, select a particular build.

  5. In the **Build details** page, under **Steps** , click **Build summary** to view build logs for your entire build or select a build step to view build logs for that step.

  6. If your build logs are stored in Logging, in the **Build log** panel, then click the open_in_new icon to view the logs in **Logs Explorer**.




###  gcloud 

Run the [`gcloud builds log`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/log) command where build-id is the ID of the build for which you want to get build logs. The build ID is displayed at the end of the build submission process when you run `gcloud builds submit`, or in the ID column when you run `gcloud builds list`.
    
    
    gcloud builds log build-id
    

### View build logs in GitHub and GitHub Enterprise

If you create a [GitHub](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github) or [GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise) trigger with the gcloud CLI or the Cloud Build API and specified `--include-logs-with-status` as an option, then you can view your build logs in GitHub and GitHub Enterprise.

To view build logs in GitHub and GitHub Enterprise, do the following:

  1. Navigate to the repository associated with your trigger.

  2. Navigate to your list of commits.

  3. Locate the row of the commit you want to view build logs for.

  4. Click the result icon in the row of your commit.

You will see a list of checks associated with your commit.

  5. Click **Details** for the row you want to view build logs for.

You will see the **Summary** page associated with your commit. If you have created a trigger using the `--include-logs-with-status` flag, you will see your build logs displayed under the **Details** section of the page.


**Note:** The service account you used for the trigger must include the [`roles/logging.viewer`](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer) role to be able to send the build logs to GitHub.

## Delete build logs and buckets

To get the permissions that you need to delete build logs and buckets in Cloud Storage, ask your administrator to grant you the following IAM roles on the service account used for your build: 

  * Delete build logs in a user-created or user-owned Cloud Storage bucket: Storage Admin (`roles/storage.admin`) - the user or service account deleting build logs 
  * Delete a user-created or user-owned Cloud Storage bucket: Storage Admin (`roles/storage.admin`) - the user or service account deleting buckets 
  * Delete a user-created Logging bucket: Logs Configuration Writer (`roles/logging.configWriter`) - your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To delete build logs in a user-created or user-owned Cloud Storage bucket, follow the instructions in [Deleting objects](https://docs.cloud.google.com/storage/docs/deleting-objects) in the Cloud Storage documentation.

To delete a user-created or user-owned Cloud Storage bucket, follow the instructions in [Deleting buckets](https://docs.cloud.google.com/storage/docs/deleting-buckets) in the Cloud Storage documentation.

To delete a user-created Logging bucket, follow the instructions in [Delete a bucket](https://docs.cloud.google.com/logging/docs/buckets#deleting-logs-bucket) in the Logging documentation.

## What's next

  * Learn about [audit logs created by Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/audit-logs).
  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn more about [Cloud Build IAM permissions](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
