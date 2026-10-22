---
url: https://docs.cloud.google.com/build/docs/deploy-containerized-application-cloud-run/
title: Quickstart: Deploy a containerized application to Cloud Run \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:09.852456+00:00
---

# Quickstart: Deploy a containerized application to Cloud Run  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/deploy-containerized-application-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a containerized application to Cloud Run using Cloud Build

This page shows you how to use Cloud Build to deploy a containerized application to Cloud Run.

**Note:** This quickstart shows you how to deploy an image to Cloud Run, but Cloud Build supports deployments on additional platforms such as App Engine, GKE, and Cloud Run functions.   
  
You can also use [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/deploy-app-run) to set up a continuous-delivery pipeline to deploy to Cloud Run.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://console.cloud.google.com/getting-started?walkthrough_tutorial_id=cloud_build_deploy)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Build, Cloud Run, Artifact Registry, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,artifactregistry.googleapis.com,compute.googleapis.com&redirect=https%3A//cloud.google.com/cloud-build/docs/quickstart-deploy)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Build, Cloud Run, Artifact Registry, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,artifactregistry.googleapis.com,compute.googleapis.com&redirect=https%3A//cloud.google.com/cloud-build/docs/quickstart-deploy)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you've already installed Google Cloud CLI previously, make sure you have the latest available version by running `gcloud components update`.




## Grant permissions

Cloud Build requires several permissions before it can deploy an image to Cloud Run. To grant these permissions, do the following:

  1. Open a terminal window.

  2. Set environment variables to store your project ID and project number.
         
         PROJECT_ID=$(gcloud config list --format='value(core.project)')
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
         

  3. Grant the **Cloud Run Admin** role to your [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
             --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
             --role=roles/run.admin \
         

  4. Grant the **Storage Object User** role to your Cloud Build service account.
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
             --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
             --role=roles/storage.objectUser \
         

  5. Grant the **Service Account User** role to your Cloud Build service account.
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
             --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
             --role=roles/iam.serviceAccountUser
         

**Note:** The **Service Account User** role grants overly-broad permissions to the Cloud Build service account. When you configure Cloud Build to deploy to Cloud Run in a production environment, we strongly recommend configuring the Cloud Build service account to impersonate an existing Cloud Run service identity. For more information, see [Configure Cloud Build service account impersonation for managed services](https://docs.cloud.google.com/build/docs/deploying-builds/cb-sa-imp).



## Deploy a prebuilt image

You can configure Cloud Build to deploy a prebuilt image that is stored in Artifact Registry to Cloud Run.

To deploy a prebuilt image:

  1. Open a terminal window (if not already open).

  2. Create a new directory named `helloworld` and navigate into it:
         
         mkdir helloworld
         cd helloworld
         

  3. Create a file named `cloudbuild.yaml` with the following contents. This file is the Cloud Build config file. It contains instructions for Cloud Build to deploy the image named `us-docker.pkg.dev/cloudrun/container/hello` on the Cloud Run service named `cloudrunservice`.
         
         steps:
         - name: 'gcr.io/cloud-builders/gcloud'
           script: |
             gcloud run deploy cloudrunservice --image us-docker.pkg.dev/cloudrun/container/hello --region us-central1 --platform managed --allow-unauthenticated

  4. Deploy the image by running the following command:
         
         gcloud builds submit --region=us-west2 --config cloudbuild.yaml
         




When the build is complete, you will see an output similar to the following:
    
    
    DONE
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    ID                                    CREATE_TIME                DURATION  SOURCE                                                                                            IMAGES  STATUS
    784653b2-f00e-4c4b-9f5f-96a5f115bef4  2020-01-23T14:53:13+00:00  23S       gs://cloudrunqs-project_cloudbuild/source/1579791193.217726-ea20e1c787fb4784b19fb1273d032df2.tgz  -       SUCCESS
    

You've just deployed the image `hello` to Cloud Run.

## Run the deployed image

  1. Open the Cloud Run page in the Google Cloud console:

[Open the Cloud Run page](https://console.cloud.google.com/run)

  2. Select your project and click **Open**.

You will see the **Cloud Run Services** page.

  3. In the table, locate the row with the name **cloudrunservice** , and click **cloudrunservice**.

The **Service details** page for **cloudrunservice** is displayed.

  4. To run the image that you deployed on **cloudrunservice** , click the URL:

![Screenshot of the Cloud Run Service details page](https://docs.cloud.google.com/build/images/run-service-url.png)




## What's next

  * [Learn how to build using Cloud Build](https://cloud.google.com/cloud-build/docs/quickstart-build).
  * [Learn how to create a basic build config file](https://cloud.google.com/cloud-build/docs/configuring-builds/create-basic-configuration).
  * [Learn how to view build results](https://cloud.google.com/cloud-build/docs/view-build-results).
  * [Learn about more ways to deploy to Cloud Run](https://cloud.google.com/cloud-build/docs/deploying-builds/deploy-cloud-run).
  * [Learn how to deploy to Google Kubernetes Engine](https://cloud.google.com/cloud-build/docs/deploying-builds/deploy-gke).
  * [Learn more about DevOps resources](https://cloud.google.com/devops).
  * [Explore the DevOps research program](https://www.devops-research.com/research.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
