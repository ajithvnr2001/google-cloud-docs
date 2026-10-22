---
url: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server/
title: Build repositories from Bitbucket Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:29.998479+00:00
---

# Build repositories from Bitbucket Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build repositories from Bitbucket Server Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen Developer Connect

Cloud Build lets you create triggers to build from repositories hosted on [Bitbucket Server](https://confluence.atlassian.com/bitbucketserver/bitbucket-data-center-and-server-documentation-776639749.html). You can execute builds in response to events such as commit pushes or merge requests associated with your Bitbucket Server repository.

This page explains how you can enable build triggers for a Bitbucket Server instance. For more information, see [Cloud Build triggers](https://docs.cloud.google.com/build/docs/triggers) and [Cloud Build repositories](https://docs.cloud.google.com/build/docs/repositories).

## Before you begin

Follow the instructions to [connect to a Bitbucket Server host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-server).

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-server)




To create a trigger for a Bitbucket Server repository, you must have a connection between Google Cloud and your repository. To create a connection through the Bitbucket Server app in Google Cloud, see [Connect to a Bitbucket Server repository](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-server).

## Create a Bitbucket Server trigger

This sections explains how you can connect your Bitbucket Server repositories to Cloud Build and create a trigger to automatically invoke builds on your connected repositories. If you want to use Bitbucket Server triggers in a private network, then see [Building repositories from Bitbucket Server in a private network](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server-private-network).

###  Google Cloud console 

To create Bitbucket Server triggers using the Google Cloud console, do the following:

  1. Open the **Triggers** page in the Google Cloud console.

[Open the Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Select your Google Cloud project and click **Open**.

  3. Click **Create trigger**.

  4. Enter the following trigger settings:

     * **Name** : Enter a name for your trigger.

     * **Region** : Select the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger.

       * If the build config file associated with the trigger specifies a [private pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview), then Cloud Build uses the private pool to run your build. In this case, the region you specify in your trigger must match the region where you created your private pool.
       * If the build config file associated with the trigger **doesn't** specify a private pool, then Cloud Build uses the default pool to run your build in the same region as your trigger.
     * **Description** (optional): Enter a description for your trigger.

     * **Event** : Select the repository event to invoke your trigger.

       * **Push to a branch** : Set your trigger to start a build on commits to a particular branch.

       * **Push new tag** : Set your trigger to start a build on commits that contain a particular tag.

       * **Pull request** : Set your trigger to start a build on commits to a pull request.

     * **Source** : Configure information about your Bitbucket Server repository:

       * **Repository service** : Select Cloud Build repositories.

       * **Repository generation** : Select **2nd generation** as your source.

**Note:** The region of your repository must match the region of your trigger.
       * **Repository** : From the list of available repositories, select the repository.

       * **Branch** or **Tag** : Specify a regular expression with the branch or tag value to match. For information on acceptable regular expression syntax, see [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

       * **Comment control** : If you selected **Pull request** as your **Event** , choose one of the following options to control whether a build is automatically executed by the trigger:

         * **Required except for owners and collaborators** : When a pull request is created or updated by a repository owner or collaborator, builds are automatically executed by the trigger. If an external contributor initiates the action, builds are executed only after an owner or collaborator comments `/gcbrun` on the pull request.

         * **Required** : When a pull request is created or updated by any contributor, builds are executed only after an owner or collaborator comments `/gcbrun` on the pull request. Builds are executed each time a change to a pull request is made.

         * **Not required** : When a pull request is created or updated by any contributor, builds are automatically be executed by triggers.

**Warning:** Any user with read access to the repository can submit a pull request, which may execute a build that includes changes to the source code in the pull request. To disable this behavior, we recommend using [manual approvals](https://docs.cloud.google.com/build/docs/automating-builds/approve-builds) to gate builds when making pull requests on public repositories. You can also learn more about the [build-time privileges of triggers](https://docs.cloud.google.com/build/docs/cloud-build-service-account#build_triggers).
     * **Configuration** : Select the build config file located in your repository or configure your build inline on the trigger.

     * **Type** : Select the type of configuration to use for your build.

       * **Cloud Build configuration file (yaml or json)** : Use a build config file for your configuration.
       * **Dockerfile** : Use a `Dockerfile` for your configuration.
     * **Location** : Specify the location for your configuration.

       * **Repository** : If your config file is located in your repository, provide the location of your [build config file](https://docs.cloud.google.com/build/docs/build-config) or the `Dockerfile` directory and a name for the resulting image. If your configuration is a `Dockerfile`, you can optionally provide a timeout for your build. When you've provided the `Dockerfile` and image name, you'll see a preview of the `docker build` command for your build.

       * **Inline** : If you selected **Cloud Build configuration file (yaml or json)** as your configuration option, you can specify your build config inline. Click **Open Editor** to write your build config file in the Google Cloud console using YAML or JSON syntax. Click **Done** to save your build config.

**Note:** Inline build configuration support is not available for `Dockerfile`.
  5. Click **Create** to create your Bitbucket Cloud trigger.




###  gcloud CLI 

To create Bitbucket Server triggers using `gcloud` commands, run the following command:
    
    
        gcloud builds triggers create bitbucketserver \
          --name=TRIGGER_NAME \
          --repository=projects/PROJECT_ID/locations/REGION/connections/CONNECTION_NAME/repositories/REPO_NAME \
          --branch-pattern=BRANCH_PATTERN # or --tag-pattern=TAG_PATTERN \
          --build-config=BUILD_CONFIG_FILE \
          --region=REGION \
          --service-account=SERVICE-ACCOUNT
    

Where:

  * TRIGGER_NAME is the name of your trigger.
  * PROJECT_ID is your Google Cloud project ID.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) of your trigger.
  * CONNECTION_NAME is the name of your Bitbucket Server connection.
  * REPO_NAME is the name of your repository
  * BRANCH_PATTERN is the branch name in your repository to invoke the build on.
  * TAG_PATTERN is the tag name in your repository to invoke the build on.
  * BUILD_CONFIG_FILE is the path to your build configuration file.
  * SERVICE-ACCOUNT is the service account to use for trigger and build operations.



###  API 

To create a Bitbucket Server trigger with the API, use the following JSON template:
    
    
    {
        "filename": "cloudbuild.yaml",
        "name": "curl-trigger",
        "description": "curl trigger",
        "repository_event_config": {
          "repository": "REPO_NAME",
          "repository_type": "BITBUCKET_SERVER",
          // Field filter must be only one of the following:
          "pullRequest": "PULL_REQUEST_FILTER",
          "push": "PUSH_FILTER"
        }
    }
    

Where:

  * "REPO_NAME" is the name of your repository.
  * "PULL_REQUEST_FILTER" is an instance of [`PullRequestFilter`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter), which defines the filter that allows Cloud Build to trigger a build when a matching pull request is made in Bitbucket Server.
  * "PUSH_FILTER" is an instance of [`PushFilter`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter), which defines the filter that allows Cloud Build to trigger a build when a matching push is made in Bitbucket Server.



Enter the following `curl` command in your terminal:
    
    
      curl -X POST -H "Authorization: Bearer "$(gcloud auth print-access-token) -H "Content-Type: application/json; charset=utf-8" -H "x-goog-user-project: PROJECT_NUMBER" https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/triggers -d @trigger.json
    

Where:

  * PROJECT_NUMBER is your Google Cloud project number.
  * PROJECT_ID is your Google Cloud project ID.



## Data sharing

The data sent to Bitbucket Server from Cloud Build helps you identify triggers by name and see build results on Bitbucket Server.

The following data is shared between Cloud Build and Bitbucket Server:

  * Google Cloud project ID
  * Trigger name



Data sharing is automatically enabled for Bitbucket Server.

## What's next

  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [build repositories from Bitbucket Server in a private network](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server-private-network).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
