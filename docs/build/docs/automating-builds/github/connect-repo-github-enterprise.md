---
url: https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise/
title: Connect to a GitHub Enterprise repository \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:05.199134+00:00
---

# Connect to a GitHub Enterprise repository  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a GitHub Enterprise repository Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

This page explains how to connect a [GitHub Enterprise](https://docs.github.com/en/enterprise-server) repository to Cloud Build. To learn more about Cloud Build repositories, see [Cloud Build repositories](https://docs.cloud.google.com/build/docs/repositories).

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise)



  * Follow the instructions to [connect a GitHub Enterprise host](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise).
  * Ensure you have administrator access on repositories where you want to enable GitHub Enterprise triggers.



## Connect to a GitHub Enterprise repository

###  Console 

To connect a GitHub Enterprise repository to a host connection, complete the following steps:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You see the **Repositories** page.

  2. At the top of the page, select the **2nd gen** tab.

  3. Click **Link Repository** to link repositories from your connection.

You see the **Link repositories** panel.

  4. In the **Link Repositories** panel, enter the following information:

     1. **Connection** : Select a connection from the drop-down menu.
     2. **Repository** : Select a repository to link to your connection.

     3. **Repository Name** : Enter a name for your repository.

        1. **Generated** : Select this option for Cloud Build to automatically generated repository names on your behalf for selected repositories.
        2. **Manual** : Select this option to manually specify names for your selected repositories.

If you select **Manual** , you can modify the names for your selected repositories in the **Repository names** section.

**Note:** If you're a collaborator, you need administrator permissions in GitHub to see the repository.
  5. Click **Link** to link your repository to your connection.




You have now successfully linked your GitHub Enterprise repository to your connection.

###  gcloud 

To add a GitHub Enterprise repository to your connection, enter the following command:
    
    
       gcloud builds repositories create REPO_NAME \
         --remote-uri=REPO_URI \
         --connection=CONNECTION_NAME --region=REGION
    

Where:

  * REPO_NAME is the name of your repository.
  * REPO_URI is the link to your GitHub repository.
  * CONNECTION_NAME is the name given to the GitHub Enterprise host connection created in Cloud Build from [Connect to a GitHub Enterprise host](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise#connecting_to_a_github_enterprise_host).
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.

**Note:** If you're a collaborator, you need administrator permissions in GitHub to connect to the repository.

###  Terraform 

To add a GitHub Enterprise repository to your connection, add the following code snippet to your Terraform configuration:
    
    
        resource "google_cloudbuildv2_repository" "my-repository" {
          project = "PROJECT_ID"
          name = "REPO_NAME"
          location = :REGION"
          parent_connection = google_cloudbuildv2_connection.my-connection.name
          remote_uri = "REMOTE_URI'
      }
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * REPO_NAME is the name of your GitHub repository.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * URI is the remote URI of your repository. For example, `https://github.com/myuser/myrepo.git`.

**Note:** If you're a collaborator, you need administrator permissions in GitHub to connect to the repository.

## Next steps

  * Learn how to [build repositories from GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise).
  * Learn how to [build repositories from GitHub Enterprise in a private network](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).
  * Learn how to [specify additional repositories](https://docs.cloud.google.com/build/docs/building/manage-dependencies) as dependencies to your build.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
