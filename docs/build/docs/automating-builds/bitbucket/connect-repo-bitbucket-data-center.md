---
url: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-data-center/
title: Connect to a Bitbucket Data Center repository \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:02.904596+00:00
---

# Connect to a Bitbucket Data Center repository  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-data-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a Bitbucket Data Center repository Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

This page explains how to connect to a [Bitbucket Data Center](https://confluence.atlassian.com/bitbucketserver/bitbucket-data-center-and-server-documentation-776639749.html) repository to Cloud Build.

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center)



  * Follow the instructions to [connect a Bitbucket Data Center host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center) before connecting to a repository.



## Connect to a Bitbucket Data Center repository

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You will see the **Repositories** page.

  2. At the top of the page, select the **2nd gen** tab.

  3. In the project selector, select your Google Cloud project.

  4. Click **Link repository** to link repositories from your connection.

You will see the **Link repositories** panel.

  5. In the **Link repositories** panel, enter the following information:

     1. **Connection** : Select a connection from the drop-down menu.

     2. **Repository** : Select one or more repositories to link to your connection.

     3. **Repository Resource Name** : Use these fields to create resource names for the repositories that are linked.

        1. **Generated** : Select this option for Cloud Build to automatically generate repository resource names on your behalf for selected repositories.
        2. **Manual** : Select this option to manually specify repository resource names.

If you select **Manual** , you can modify the names for your selected repositories in the **Repository names** section.

  6. Click **Link** to link your repository to your connection.




###  gcloud 

To add a Bitbucket Data Center repository to your connection, run the following command:
    
    
    gcloud builds repositories create REPO_NAME \
        --remote-uri=REPO_URI \
        --connection=CONNECTION_NAME --region=REGION
    

Where:

  * REPO_NAME is the name of your repository.
  * REPO_URI is the link to your Bitbucket Data Center repository. For example, `https://bbdc-host.com/scm/myproject/myrepo.git`.
  * CONNECTION_NAME is the name given to the Bitbucket Data Center host connection created in Cloud Build from [Connect to a Bitbucket Data Center host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center#connect).
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.



###  Terraform 

To add a Bitbucket Data Center repository to your connection, add the following code snippet to your Terraform configuration:
    
    
        resource "google_cloudbuildv2_repository" "my-repository" {
            project = "PROJECT_ID"
            name = "REPO_NAME"
            location = "REGION"
            parent_connection = google_cloudbuildv2_connection.RESOURCE_NAME.name
            remote_uri = "REPO_URI"
        }
    

Where:

  * PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project).
  * REPO_NAME is the name of your repository.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * RESOURCE_NAME is the name of the `google_cloudbuildv2_connection` resource. For example, `my-connection` from the Terraform example in [Connect to a Bitbucket Data Center host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center?generation=2nd-gen#terraform).
  * REPO_URI is the link to your Bitbucket Data Center repository. For example, `https://bbdc-host.com/scm/myproject/myrepo.git`.



## What's next

  * Learn how to [build repositories from Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center).
  * Learn how to [build repositories from Bitbucket Data Center in a private network](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center-private-network).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
