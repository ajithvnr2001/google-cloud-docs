---
url: https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine/
title: Deploying to App Engine \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:00.600979+00:00
---

# Deploying to App Engine  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Deploying to App Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to deploy applications to App Engine using Cloud Build. If you're new to Cloud Build, read the [quickstarts](https://docs.cloud.google.com/build/docs/quickstarts) and the [build configuration overview](https://docs.cloud.google.com/build/docs/build-config) first.

App Engine is a fully managed, serverless platform for developing and hosting web applications at scale. For more information on App Engine, read the [App Engine documentation](https://docs.cloud.google.com/appengine/docs).

## Before you begin

  * Enable the App Engine API:

[ Enable the App Engine API](https://console.cloud.google.com/apis/library/appengine.googleapis.com)

  * Have your application source code ready. Your source code needs to be stored in a repository such as GitHub or Bitbucket.

  * To run the `gcloud` commands in this page, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk).




**Caution:** Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

## Required Identity and Access Management permissions

  1. In the Google Cloud console, go to the _settings_ Cloud Build **Permissions** page: 

[Go to **Permissions**](https://console.cloud.google.com/cloud-build/settings)

  2. For your [specified Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) or [default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account), set the status of the following roles to **Enabled** :

     * App Engine Admin (`roles/appengine.appAdmin`) | Lets Cloud Build deploy new versions to App Engine. 
       * In the Assign Service Account User Role panel, [choose a service account to impersonate](https://docs.cloud.google.com/build/docs/deploying-builds/cb-sa-imp) and then click **Grant Permission**.
     * Storage Admin (`roles/storage.admin`) | Enables reading and writing from Cloud Storage.
     * Artifact Registry Writer (`roles/artifactregistry.writer`) | Allows pulling images from and writing to Artifact Registry.
     * Logs Writer (`roles/logging.logWriter`) | Allows log entries to be written to Cloud Logging.
     * Cloud Build Editor (`roles/cloudbuild.builds.editor`) | Allows your service account to run builds.



## Configuring the deployment

Cloud Build lets you use any publicly available container image to execute your tasks. You can do this by specifying the image in a build `step` in the Cloud Build config file.

App Engine provides the `gcloud app deploy` command, which builds an image with your source code and deploys that image on App Engine. You can use the [`cloud-sdk` image](https://github.com/GoogleCloudPlatform/cloud-sdk-docker) as a build step in your config file to invoke `gcloud` commands within the image. Arguments passed to this build step are passed to the gcloud CLI directly, allowing you to run any `gcloud` command in this image.

To deploy an application to App Engine, use the following steps:

  1. Create a [Cloud Build configuration file](https://docs.cloud.google.com/build/docs/build-config) named `cloudbuild.yaml` or `cloudbuild.json`.

**Note:** Do not store the config file in the same directory as the source code because the gcloud CLI may interpret that you want to deploy the app using Docker using Cloud Build. Instead, store your source in a separate directory and create the config file in the parent directory.
  2. In the config file:

     * Add a `name` field to specify the `cloud-sdk` build step.
     * Add an `entrypoint` field to use the `bash` tool when `cloud-sdk` is invoked.
     * In the `args` field, invoke the `gcloud app deploy` command and set a `timeout` for [App Engine to use when it invokes Cloud Build](https://docs.cloud.google.com/appengine/docs/standard/nodejs/testing-and-deploying-your-app#deploying_your_application). This is required because Cloud Build build steps and builds have a default timeout of 10 minutes and App Engine deployments could take longer than that to complete. Specifying a longer timeout will make sure that the build doesn't timeout if `gcloud app deploy` takes longer than 10 minutes to complete.

**Timeout errors when using the App Engine standard environment** : You can configure timeouts as described here only when using the App Engine flexible environment. The App Engine standard environment does not allow the build timeout to be configured. If you're using Cloud Build for deploying on the App Engine standard environment, and your build is failing with a timeout error, consider using the App Engine flexible environment or [Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run) instead of the App Engine standard environment.

     * Add a [build `timeout`](https://docs.cloud.google.com/build/docs/build-config#build_steps) value of more than 10 minutes.

###  YAML 
    
    steps:
    - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
      entrypoint: 'bash'
      args: ['-c', 'gcloud config set app/cloud_build_timeout 1600 && gcloud app deploy']
    timeout: '1600s'
    

###  JSON 
    
    {
      "steps": [
      {
        "name": "gcr.io/google.com/cloudsdktool/cloud-sdk",
        "entrypoint": "bash",
        "args": [
          "-c",
          "gcloud config set app/cloud_build_timeout 1600 && gcloud app deploy"
         ]
      }
      ],
      "timeout": "1600s"
    }
    

  3. Start the build, where `SOURCE_DIRECTORY` is the path or URL to the source code and `REGION` is one of the [supported build regions](https://docs.cloud.google.com/build/docs/locations) to start the build:
         
         gcloud builds submit --region=REGION SOURCE_DIRECTORY
         




## Continuous deployment

You can automate the deployment of your software to App Engine by creating Cloud Build triggers. You can configure your triggers to build and deploy images whenever you update your source code.

To automate your deployment to App Engine:

  1. In your repository, add a config file with steps to invoke the `gcloud app deploy` command:

###  YAML 
         
         steps:
         - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
           entrypoint: 'bash'
           args: ['-c', 'gcloud config set app/cloud_build_timeout 1600 && gcloud app deploy']
         timeout: '1600s'
         

###  JSON 
         
         {
           "steps": [
           {
             "name": "gcr.io/google.com/cloudsdktool/cloud-sdk",
             "entrypoint": "bash",
             "args": [
               "-c",
               "gcloud config set app/cloud_build_timeout 1600 && gcloud app deploy"
              ]
           }
           ],
           "timeout": "1600s"
         }
         

  2. Create a build trigger with the config file created in the previous step:

     1. Open the **Triggers** page in the Google Cloud console:

[Open Triggers page](https://console.cloud.google.com/cloud-build/triggers)

     2. Select your project from the project selector drop-down menu at the top of the page.

     3. Click **Open**.

     4. Click **Create trigger**.

On the **Create trigger** page, enter the following settings:

        1. Enter a name for your trigger.

        2. Select the repository event to start your trigger.

        3. Select the repository that contains your source code and build config file.

        4. Specify the regular expression for the branch or tag name that will start your trigger.

        5. **Configuration** : Choose the build config file you created previously.

     5. Click **Create** to save your build trigger.




Anytime you push new code to your repository, you will automatically start a build and deploy on App Engine.

For more information on creating Cloud Build triggers, see [Creating and managing build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

## What's next

  * Learn how to [deploy on Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run)
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine)
  * Learn how to [deploy on GKE](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-gke)
  * Learn how to [deploy on Cloud Run functions](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-functions)
  * Learn how to [deploy on Firebase](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-firebase)
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
