---
url: https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab/
title: Connect to a GitLab repository \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:05.885744+00:00
---

# Connect to a GitLab repository  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a GitLab repository Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect a [GitLab](https://about.gitlab.com/) repository to Cloud Build. To learn more about Cloud Build repositories, see [Cloud Build repositories](https://docs.cloud.google.com/build/docs/repositories).

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab)



  * Follow the instructions to [connect a GitLab host](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab) before connecting repositories.



## Connect to a GitLab repository

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You see the **Repositories** page.

  2. At the top of the page, select the **2nd gen** tab.

  3. In the project selector in the top bar, select your Google Cloud project.

  4. Click **Link repository** to link repositories from your connection.

You see the **Link repository** panel.

  5. In the **Link repository** panel, enter the following information:

     1. **Connection** : Select a connection from the drop-down menu.
     2. **Repository** : Select a repository to link to your connection.

     3. **Repository Name** : Enter a name for your repository.

        1. **Generated** : Select this option for Cloud Build to automatically generated repository names on your behalf for selected repositories.
        2. **Manual** : Select this option to manually specify names for your selected repositories.

If you select **Manual** , you can modify the names for your selected repositories in the **Repository names** section.

  6. Click **Link** to link your repository to your connection.




###  gcloud 

To add a GitLab repository to your connection, enter the following command:
    
    
       gcloud builds repositories create REPO_NAME \
         --remote-uri=REPO_URI \
         --connection=CONNECTION_NAME --region=REGION
    

Where:

  * REPO_NAME is the name of your repository.
  * REPO_URI is the link to your GitLab repository.
  * CONNECTION_NAME is the name given to the GitLab connection created in Cloud Build from [Connect to a GitLab host](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab#connecting_to_a_gitlab_host).
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.



You have now linked a repository to your GitLab connection.

## What's next

  * Learn how to [build repositories from GitLab](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab).
  * Learn how to build and deploy your workloads to Google Cloud using Google-managed CI/CD components in your GitLab pipeline. See [GitLab on Google Cloud](https://docs.cloud.google.com/docs/gitlab).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
