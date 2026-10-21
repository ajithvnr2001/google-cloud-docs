---
url: https://docs.cloud.google.com/build/docs/deploying-builds/deploy-functions/
title: Deploying to Cloud Run functions \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:04.236994+00:00
---

# Deploying to Cloud Run functions  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/deploying-builds/deploy-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Deploying to Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to deploy applications to Cloud Run functions using Cloud Build. If you're new to Cloud Build, read the [quickstarts](https://docs.cloud.google.com/build/docs/quickstarts) and the [Build configuration overview](https://docs.cloud.google.com/build/docs/build-config) first.

Cloud Run functions is a serverless execution environment for building and connecting cloud services. With Cloud Run functions, you can write single-purpose functions that are attached to events emitted from your cloud infrastructure and services. Your function is triggered when an event being watched is fired. For more information on Cloud Run functions, read [Cloud Run functions documentation](https://docs.cloud.google.com/functions/docs).

## Before you begin

  * Enable the Cloud Run functions API:

[ Enable the Cloud Run functions API](https://console.cloud.google.com/apis/library/cloudfunctions.googleapis.com)

  * Have your application source code ready. Your source code needs to be stored in a repository such as GitHub or Bitbucket.

  * To run the `gcloud` commands in this page, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk).




**Caution:** Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

## Required Identity and Access Management permissions

  1. In the Google Cloud console, go to the _settings_ Cloud Build **Permissions** page: 

[Go to **Permissions**](https://console.cloud.google.com/cloud-build/settings)

  2. For your [specified Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) or [default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account), set the status of the following roles to **Enabled** :

     * Cloud Functions Developer (`roles/cloudfunctions.developer`) | To deploy and manage functions. 
       * In the Assign Service Account User Role panel, [choose a service account to impersonate](https://docs.cloud.google.com/build/docs/deploying-builds/cb-sa-imp) and then click **Grant Permission**.
     * Cloud Run Admin (`roles/run.admin`) | Allows your Cloud Build service account to deploy new versions to Cloud Run.
     * Storage Admin (`roles/storage.admin`) | Enables reading and writing from Cloud Storage.
     * Artifact Registry Writer (`roles/artifactregistry.writer`) | Allows pulling images from and writing to Artifact Registry.
     * Logs Writer (`roles/logging.logWriter`) | Allows log entries to be written to Cloud Logging.
     * Cloud Build Editor (`roles/cloudbuild.builds.editor`) | Allows your service account to run builds.



## Configuring the deployment

Cloud Build lets you use any publicly available container image to execute your tasks. You can do this by specifying the image in a build `step` in the Cloud Build config file.

Cloud Run functions provides the `gcloud functions deploy` command, which deploys your function from the directory containing your function code. You can use the [`cloud-sdk` image](https://github.com/GoogleCloudPlatform/cloud-sdk-docker) as a build step in your config file to invoke `gcloud` commands within the image. Arguments passed to this build step are passed to Google Cloud CLI directly, allowing you to run any `gcloud` command in this image.

To deploy an application to Cloud Run functions, use the following steps:

  1. In your project root directory, create the [Cloud Build configuration file](https://docs.cloud.google.com/build/docs/build-config) named `cloudbuild.yaml` or `cloudbuild.json`.
  2. In the config file:

     * Add a `name` field and specify the `gcloud` build step.
     * Add `functions deploy` to the `args` field to invoke the `gcloud functions deploy` command. For available configuration options, see [`gcloud functions deploy` reference](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy).
     * `--source=.` implies that the source code is in the current working directory.

###  YAML 
    
    steps:
    - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
      args:
      - gcloud
      - functions
      - deploy
      - FUNCTION_NAME
      - --region=FUNCTION_REGION
      - --source=.
      - --trigger-http
      - --runtime=RUNTIME
    

###  JSON 
    
    {
     "steps": [
      {
         "name": "gcr.io/google.com/cloudsdktool/cloud-sdk",
         "args": [
           "gcloud",
           "functions",
           "deploy",
            [
              "FUNCTION_NAME"
            ],
            "--region=FUNCTION_REGION",
            "--source=.",
            "--trigger-http",
            "--runtime=RUNTIME"
         ]
       }
      ]
    }
    

Replace the placeholder values in the config file above with the following:

     * `FUNCTION_NAME` is the name of the Cloud Run functions you are deploying. If you're updating an existing function, this value must match the name of the function you're updating.
     * `FUNCTION_REGION` is the region to which you're deploying Cloud Run functions. For a list of supported regions, see [Cloud Run functions locations](https://docs.cloud.google.com/functions/docs/locations).
     * `--trigger-http` is the trigger type for this function, in this case an HTTP request (webhook).
     * `RUNTIME` is the [runtime](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) in which to run the function.

For more information on using `gcloud functions deploy`, see the [Cloud Run functions documentation](https://docs.cloud.google.com/functions/docs/deploying/filesystem).

  3. Start the build using the config file created in the previous step:
         
         gcloud builds submit --region=REGION --config CONFIG_FILE_PATH SOURCE_DIRECTORY
         

Replace the placeholder values in the config file above with the following:

     * `CONFIG_FILE_PATH` is the path to the build config file.
     * `SOURCE_DIRECTORY` is the path or URL to the source code.
     * `REGION` is one of the [supported build regions](https://docs.cloud.google.com/build/docs/locations).

If you don't specify a `CONFIG_FILE_PATH` and `SOURCE_DIRECTORY` in the `gcloud builds submit` command, Cloud Build assumes that the config file and the source code are in the current working directory.




## Continuous deployment

You can automate the deployment of your software to Cloud Run functions by creating Cloud Build triggers. You can configure your triggers to build and deploy images whenever you update your source code.

To automate your deployment to Cloud Run functions:

  1. In your repository root, add a config file with steps to invoke the `gcloud functions deploy` command:

###  YAML 
         
         steps:
         - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
           args:
           - gcloud
           - functions
           - deploy
           - FUNCTION_NAME
           - --region=FUNCTION_REGION
           - --source=.
           - --trigger-http
           - --runtime=RUNTIME
         

###  JSON 
         
         {
          "steps": [
           {
              "name": "gcr.io/google.com/cloudsdktool/cloud-sdk",
              "args": [
                "gcloud",
                "functions",
                "deploy",
                 [
                   "FUNCTION_NAME"
                 ],
                 "--region=FUNCTION_REGION",
                 "--source=.",
                 "--trigger-http",
                 "--runtime=RUNTIME"
              ]
            }
           ]
         }
         

Replace the placeholder values in the config file above with the following:

     * `FUNCTION_NAME` is the name of the Cloud Run functions you are deploying. If you're updating an existing function, this value must match the name of the function you're updating.
     * `FUNCTION_REGION` is the region to which you're deploying Cloud Run functions. For a list of supported regions, see [Cloud Run functions locations](https://docs.cloud.google.com/functions/docs/locations).
     * `--trigger-http` is the trigger type for this function, in this case an HTTP request (webhook).
     * `RUNTIME` is the [runtime](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) in which to run the function.
  2. Create a build trigger with the config file created in the previous step:

     1. Open the **Triggers** page in the Google Cloud console:

[Open Triggers page](https://console.cloud.google.com/cloud-build/triggers)

     2. Select your project from the project selector drop-down menu at the top of the page.

     3. Click **Create Trigger**.

     4. In the **Name** field, enter a name for your trigger.

     5. Under **Region** , select the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger.

**Note:** The region for your trigger must match the region of the function you're deploying to.
     6. Under **Event** , select the repository event to start your trigger.

     7. Under **Source** , select your repository and the branch or tag name that will start your trigger. For more information on specifying which branches to autobuild, see [Creating a build trigger](https://docs.cloud.google.com/build/docs/running-builds/automate-builds#build_trigger).

     8. Under **Configuration** , select **Cloud Build configuration file (YAML or JSON)**.

     9. In the **Cloud Build configuration file location** field, type `cloudbuild.yaml` after the `/`.

     10. Click **Create** to save your build trigger.




Anytime you push new code to your repository, you will automatically trigger a build and deploy on Cloud Run functions.

For more information on creating Cloud Build triggers, see [Creating and managing build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

## What's next

  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine)
  * Learn how to [deploy on Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run)
  * Learn how to [deploy on GKE](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-gke)
  * Learn how to [deploy on Firebase](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-firebase)
  * Learn how to [deploy on App Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine)
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
