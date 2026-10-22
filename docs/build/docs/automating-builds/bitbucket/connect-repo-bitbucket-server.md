---
url: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-server/
title: Connect to a Bitbucket Server repository \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:41.754352+00:00
---

# Connect to a Bitbucket Server repository  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a Bitbucket Server repository Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect to a [Bitbucket Server](https://confluence.atlassian.com/bitbucketserver/bitbucket-data-center-and-server-documentation-776639749.html) repository to Cloud Build.

## Before you begin

  * Enable the Cloud Build, Secret Manager, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com,compute.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-server)



  * Follow the instructions to [connect a Bitbucket Server host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-server) before connecting repositories.



## Connecting to a Bitbucket Server repository

###  Console 

To connect a Bitbucket Server repository to Cloud Build using the Google Cloud console:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

  2. At the top of the page, select the **1st gen** tab.

  3. Click **Connect Repository**.

  4. Select **Bitbucket Server**.

You will see the **Connect Repository** panel. Complete the following steps to connect your Bitbucket Server repository:

     1. **Region** : Select a region your connection is in.

     2. Under **Select source code management provider** , select **Bitbucket Server**.

     3. **Host connection** : Select the name of your host connection from the drop-down menu.

     4. Click **Continue**.

     5. Under **Select Repository** , select the Bitbucket Server repositories you wish to connect to Cloud Build.

     6. Once you have selected your Bitbucket Server account and repositories, read the consent disclaimer and select the checkbox next to it to indicate that you accept the presented terms.

     7. Click **Connect** to connect your repositories.

When a repository is connected, Cloud Build configures a webhook on the repository in your Bitbucket Server instance. The repository then sends webhooks to invoke the corresponding Bitbucket Server triggers when you make changes to your repository. A repository can also be connected multiple times with multiple host connections. To learn how to manage webhooks, see [Manage webhooks](https://confluence.atlassian.com/bitbucketserver/manage-webhooks-938025878.html#Managewebhooks-troubleshootingwebhooks).

To locate the webhook, you need the webhook ID. The webhook ID for each connected repository can be found in the `BitbucketServerConfig`.

Enter the following command to retrieve the webhook ID:
    
    gcloud alpha builds enterprise-config bitbucketserver describe CONFIG_NAME  --region=REGION
    

Where:

     * CONFIG_NAME is the name of the Bitbucket Server config
     * REGION is the region of the Bitbucket Server host connection
  5. Click **Done**. Optionally, click **Create a trigger** to create a trigger.




###  API 

To connect your Bitbucket Server repository to Cloud Build using the API, complete the following steps:

  1. Use the following JSON template below to connect your repository:
         
         {
           "parent": "projects/PROJECT_NUMBER/locations/REGION/bitbucketServerConfigs/BITBUCKET_SERVER_CONFIG_NAME",
           "requests": {
             "parent": "projects/PROJECT_NUMBER/locations/REGION/bitbucketServerConfigs/BITBUCKET_SERVER_CONFIG_NAME",
            "bitbucketServerConnectedRepository": {
               "parent": "projects/PROJECT_NUMBER/locations/REGION/bitbucketServerConfigs/BITBUCKET_SERVER_CONFIG_NAME",
               "repo": {
                 "projectKey": "PROJECT_KEY",
                 "repoSlug": "REPO_SLUG"
                }
              }
           }
         }
         

Where:

     * PROJECT_NUMBER is the project number of your Cloud project.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) associated with your Bitbucket Server configuration.
     * BITBUCKET_SERVER_CONFIG_NAME is the name of your Bitbucket Server configuration.
     * PROJECT_KEY is the key of your Bitbucket Server project. If you want to connect a personal repository, your project key should contain the tilde (`~`) symbol before your username. For example, `~${USERNAME}`. The complete URL for a host repository may look like `https://${HOST_URI}/projects/~${USER_NAME}/repos/${REPO_SLUG}`.
     * REPO_SLUG is the [slug](https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-slug/) of your Bitbucket Server repository.
  2. Enter the following `curl` command in your terminal:
         
         curl -X POST -H "Authorization: Bearer "$(gcloud auth print-access-token) -H "Content-Type: application/json; charset=utf-8" -H "x-goog-user-project: PROJECT_NUMBER" https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/bitbucketServerConfigs/BITBUCKET_SERVER_CONFIG_NAME/connectedRepositories:batchCreate -d @requests.json
         

Where:

     * PROJECT_NUMBER is your Cloud project number.
     * PROJECT_ID is your Cloud project ID.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) associated with your Bitbucket Server configuration.
     * BITBUCKET_SERVER_CONFIG_NAME is the name of your Bitbucket Server configuration.

If successful, the response body contains a newly created instance of [Operation](https://cloud.google.com/build/docs/api/reference/rest/v1/operations#Operation).

  3. Enter the following `curl` command in your terminal:
         
         curl -X GET -H "Authorization: Bearer "$(gcloud auth print-access-token) -H "Content-Type: application/json; charset=utf-8"  -H "x-goog-user-project: PROJECT_NUMBER" https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID
         

Where:

     * PROJECT_NUMBER is your Cloud project number.
     * PROJECT_ID is your Cloud project ID.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) associated with your Bitbucket Server configuration.
     * OPERATION_ID is the ID of your Bitbucket Server configuration creation operation. You can find the Operation ID in the `name` field of your response. The format of the `name` field in your response looks like the following: `projects/project-id/locations/region/operations/operation-id`.

You may need to keep running the `GetOperation` API command until the response contains `done: true`, which indicates the operation is completed. If the Bitbucket Server repository is connected successfully, you can see the connected repository in the `response.bitbucketServerConnectedRepositories` field. Otherwise, see the `error` field for a detailed error report.




## What's next

  * Learn how to [build repositories from Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server).
  * Learn how to [build repositories from Bitbucket Server in a private network](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server-private-network).
  * Learn how to [perform blue/green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
