---
url: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-cloud/
title: Connect to a Bitbucket Cloud repository \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:38:31.464067+00:00
---

# Connect to a Bitbucket Cloud repository  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a Bitbucket Cloud repository Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect a [Bitbucket Cloud](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/) repository to Cloud Build.

## Before you begin

  * Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-from-bitbucket-cloud)



  * Follow instructions in [Connect to a Bitbucket Cloud host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud).



## Connect to Bitbucket Cloud repositories

###  Console 

Connect Cloud Build to your Bitbucket Cloud repository by doing the following steps:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You will see the **Repositories** page.

  2. In the project selector, select your Google Cloud project.

  3. Select the **2nd gen** tab.

  4. Click **Link repository** to connect a new host to Cloud Build.

You will see the **Link repositories** side panel.

  5. **Connection** : Select a host connection from the drop-down menu.

  6. **Repository** : Select a repository from the drop-down menu.

  7. **Repository Resource Name** : This step creates resource names for the linked repositories.

     * **Generated** : Select this option for Cloud Build to automatically generate repository resource names on your behalf for selected repositories.
     * **Manual** : Select this option to manually specify repository resource names.

If you select **Manual** , then you can modify the names for your selected repositories in the **Repository names** section.

  8. Click **Link**.




###  gcloud 

Connect to your Bitbucket Cloud repository:
    
    
    gcloud builds repositories create REPO_NAME \
        --remote-uri=https://bitbucket.org/WORKSPACE/REPOSITORY.git \
        --connection=CONNECTION_NAME --region=REGION --project=PROJECT_ID
    

Where:

  * REPO_NAME is the name of your repository.
  * WORKSPACE is the workspace ID for your repository.
  * REPOSITORY is the name of the repository.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * CONNECTION_NAME is the name given to the Bitbucket Cloud host connection created in Cloud Build from [Connect to a Bitbucket Cloud host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud#connect-host).
  * PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project).



###  Terraform 

To add a Bitbucket Cloud repository to your connection, add the following code snippet to your Terraform configuration:
    
    
        resource "google_cloudbuildv2_repository" "my-repository" {
           project = "PROJECT_ID"
           name = "REPO_NAME"
           location = "REGION"
           parent_connection = google_cloudbuildv2_connection.RESOURCE_NAME.name
           remote_uri = "https://bitbucket.org/WORKSPACE_ID/REPO_NAME.git"
        }
    

Where:

  * PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project).
  * WORKSPACE_ID is the workspace ID for your repository.
  * REPO_NAME is the name of your repository.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * RESOURCE_NAME is the name of the `google_cloudbuildv2_connection` resource. For example, `my-connection` from the Terraform example in [Connect to a Bitbucket Cloud host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud#terraform).



## What's next

  * Learn how to [build repositories from a Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-cloud).
  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn how to [perform blue/green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
