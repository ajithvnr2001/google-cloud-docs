---
url: https://docs.cloud.google.com/build/docs/deploying-builds/deploy-firebase/
title: Deploy to Firebase \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:04.851815+00:00
---

# Deploy to Firebase  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/deploying-builds/deploy-firebase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Deploy to Firebase Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to deploy applications to [Firebase](https://firebase.google.com/) using Cloud Build. If you're new to Cloud Build, read the [quickstarts](https://docs.cloud.google.com/build/docs/quickstarts) and the [Build configuration overview](https://docs.cloud.google.com/build/docs/build-config) first.

## Before you begin

  * Enable the Cloud Build, Firebase, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,firebase.googleapis.com,firebasehosting.googleapis.com,cloudresourcemanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/deploying-builds/deploy-firebase)



  * To run the `gcloud` commands on this page, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk).

  * Keep your application source code including `firebase.json` handy. Your source code needs to be stored in a repository, such as Cloud Source Repositories, GitHub, or Bitbucket.

  * If you don't already have a project to deploy to Firebase, you can create a default project by [installing and initializing Firebase](https://firebase.google.com/docs/hosting/quickstart#initialize).




**Caution:** Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

### Required IAM permissions

  1. In the Google Cloud console, go to the _settings_ Cloud Build **Permissions** page: 

[Go to **Permissions**](https://console.cloud.google.com/cloud-build/settings)

  2. Select the service account for your build.

  3. Set the status of the following roles to **Enabled** :

     * Cloud Build Service Account | Allows the legacy Cloud Build service account to update builds, write build logs, and store build artifacts.
     * Firebase Admin | Allows Cloud Build to access Firebase.
     * API Keys Viewer | Allows Cloud Build to access the current Firebase Hosting configuration during build deployment.



## Using the `firebase` Docker image

Cloud Build provides a builder image that you can use to invoke `firebase` commands in Cloud Build. To use this builder in a Cloud Build config file, you can use the `firebase` build step to deploy to Firebase:

  1. Create a build config file named `cloudbuild.yaml` or `cloudbuild.json` where PROJECT_ID is your Google Cloud project ID and FIREBASE_PROJECT_ID is your Firebase project ID:

###  YAML 
         
         steps:
         - name: "us-docker.pkg.dev/firebase-cli/us/firebase"
            args: ['deploy', '--project=FIREBASE_PROJECT_ID', '--only=hosting']
         ## Or, target a specific version of firebase-tools
         - name: "us-docker.pkg.dev/firebase-cli/us/firebase":x.y.z
            args: ['deploy', '--project=FIREBASE_PROJECT_ID', '--only=hosting']
         

###  JSON 
         
         {
           "steps": [
            {
               "name": "us-docker.pkg.dev/firebase-cli/us/firebase",
               "args": [
                  "deploy",
                  "--project",
                  "FIREBASE_PROJECT_ID",
                  "--only",
                  "hosting"
                ]
           }
           ]
         }
         

You can choose a specific version of `firebase-tools` by using  
`name: "us-docker.pkg.dev/firebase-cli/us/firebase":x.y.z`

  2. Start the build using the build config file:
         
         gcloud builds submit --region=REGION --config CONFIG_FILE_PATH SOURCE_DIRECTORY
         

Where:

     * REGION is one of the [supported build regions](https://docs.cloud.google.com/build/docs/locations).
     * CONFIG_FILE_PATH is the path to the build config file.
     * SOURCE_DIRECTORY is the path or URL to the source code.



## Continuous deployment

You can automate the deployment of your software to Firebase by creating Cloud Build triggers. You can configure triggers to build and deploy images whenever you update your source code.

To automate your deployment to Firebase:

  1. In your repository, add a build config file with steps to invoke the `firebase deploy` command where PROJECT_ID is your Google Cloud project ID:

###  YAML
         
         steps:
               - name: us-docker.pkg.dev/firebase-cli/us/firebase
                 args: ['deploy', '--project=PROJECT_ID', '--only=hosting']
         

###  JSON 
         
         {
           "steps": [
            {
               "name": "us-docker.pkg.dev/firebase-cli/us/firebase",
               "args": [
                  "deploy",
                  "--project",
                  "PROJECT_ID",
                  "--only",
                  "hosting"
                ]
           }
           ]
         }
         

  2. Create a trigger with the build config file created in the previous step:

     1. Open the **Triggers** page in the Google Cloud console:

[Open Triggers page](https://console.cloud.google.com/cloud-build/triggers)

     2. Select your project from the project selector drop-down menu at the top of the page.

     3. Click **Open**.

     4. Click **Create trigger**.

On the **Create trigger** page, enter the following settings:

        1. Enter a name for your trigger.

        2. Select the repository event to start your trigger.

        3. Select the repository that contains your source code and build config file.

        4. Specify the regex for the branch or tag name that will start your trigger.

        5. **Configuration** : Choose the build config file you created previously.

     5. Click **Create** to save your build trigger.




Anytime you push new code to your repository, you will automatically start a build and deploy on Firebase.

For more information on creating Cloud Build triggers, see [Creating and managing build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

## Code example

To view a code sample for deploying to Firebase using Cloud Build, go to [deploy-firebase-example](https://github.com/GoogleCloudPlatform/cloud-build-samples/tree/main/deploy-firebase-example).

## What's next

  * Learn how to [perform blue/green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine)
  * Learn how to [deploy on Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run)
  * Learn how to [deploy on GKE](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-gke)
  * Learn how to [deploy on Cloud Run functions](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-functions)
  * Learn how to [deploy on App Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine)
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
