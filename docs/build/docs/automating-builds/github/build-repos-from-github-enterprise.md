---
url: https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise/
title: Building repositories from GitHub Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:24.869585+00:00
---

# Building repositories from GitHub Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Building repositories from GitHub Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen Developer Connect

Cloud Build lets you create triggers to build from repositories hosted on [GitHub Enterprise](https://github.com/about/). You can execute builds in response to events such as commit pushes or merge requests associated with your GitHub Enterprise repository.

This page explains how you can enable build triggers for a GitHub Enterprise instance. For more information, see [Cloud Build triggers](https://docs.cloud.google.com/build/docs/triggers) and [Cloud Build repositories](https://docs.cloud.google.com/build/docs/repositories).

## Before you begin

Follow the instructions to [connect to a GitHub Enterprise host](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise). 

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise)




To create a trigger for a GitHub Enterprise repository, you must have a connection between Google Cloud and your repository. To create a connection through the GitHub Enterprise app in Google Cloud, see [Connect to a GitHub Enterprise repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise).

## Create a GitHub Enterprise trigger

This section explains how you can create a trigger and link it your GitHub Enterprise installation. If you want to use GitHub Enterprise triggers in a private network, see [Building repositories from GitHub Enterprise in a private network](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network) for further instructions.

**Note:** [Manual triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manual-triggers) and [Pub/Sub triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-pubsub-triggers) cannot build GitHub Enterprise repositories through Cloud Build's integration. To clone and build repositories through GitHub Enterprise, see [Creating and managing build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) to learn how to specify a build configuration inline.

###  Google Cloud console 

To create GitHub Enterprise triggers using the Google Cloud console, do the following:

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

**Note:** Running builds initiated by a GitHub App pull request trigger are canceled when you close the pull request associated with your build. Running builds and builds that have not been started yet won't be canceled when merging a pull request.
     * **Source** : Configure information about your GitHub Enterprise repository:

       * **Repository service** : Select Cloud Build.

       * **Repository generation** : Select **2nd generation** as your source.

**Note:** The region of your repository must match the region of your trigger.
       * **Repository** : From the list of available repositories, select the repository.

       * **Branch** or **Tag** : Specify a regular expression with the branch or tag value to match. For information on acceptable regular expression syntax, see [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

       * **Comment control** : If you selected **Pull request** as your **Event** , choose one of the following options to control whether a build is automatically executed by the trigger:

         * **Required except for owners and collaborators** : When a pull request is created or updated by a repository owner or collaborator, builds are automatically executed by the trigger. If an external contributor initiates the action, builds are executed only after an owner or collaborator comments `/gcbrun` on the pull request.

         * **Required** : When a pull request is created or updated by any contributor, builds are executed only after an owner or collaborator comments `/gcbrun` on the pull request. Builds are executed each time a change to a pull request is made.

         * **Not required** : When a pull request is created or updated by any contributor, builds are automatically be executed by triggers.

**Warning:** Any user with read access to the repository can submit a pull request, which may execute a build that includes changes to the source code in the pull request. To disable this behavior, we recommend using [manual approvals](https://docs.cloud.google.com/build/docs/automating-builds/approve-builds) to gate builds when making pull requests on public repositories. You can also learn more about the [build-time privileges of triggers](https://docs.cloud.google.com/build/docs/cloud-build-service-account#build_triggers).
     * **Configuration** : Select the build config file located in your remote repository or create an inline build config file to use for your build.

       * **Type** : Select the type of configuration to use for your build. 
         * **Autodetected** : Cloud Build autodetects your configuration type if you have a `cloudbuild.yaml` or `Dockerfile` in your repository.
         * **Cloud Build configuration file (yaml or json)** : Use a build config file for your configuration.
         * **Dockerfile** : Use a `Dockerfile` for your configuration.
         * **Buildpacks** : Use [buildpacks](https://buildpacks.io/) for your configuration.
       * **Location** : Specify the location for your configuration.

         * **Repository** : If your config file is located in your remote repository, provide the location of your [build config file](https://docs.cloud.google.com/build/docs/build-config) or the `Dockerfile` directory and a name for the resulting image. If your configuration is a `Dockerfile`, you can optionally provide a timeout for your build. When you've provided the `Dockerfile` and image name, you'll see a preview of the `docker build` command that your build will execute.
         * **Inline** : If you selected **Cloud Build configuration file (yaml or json)** as your configuration option, you can specify your build config inline. Click **Open Editor** to write your build config file in the Google Cloud console using YAML or JSON syntax. Click **Done** to save your build config.
**Note:** Inline build configuration support is not available for `Dockerfile`.
     * **Substitution variables** (optional): If you selected the Cloud Build config file as your build config option, you can choose to define trigger-specific substitution variables using this field. For example, say you're creating multiple triggers where each trigger deploys your app to a specific environment. You can specify that your app is deployed to an environment in your build config file and then use this field to define substitution variables specifying which environment this trigger should deploy to. For information on specifying substitution values in build config files, see [Substituting variable values](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values).

     * **Build logs** (optional): Check the box to send build logs to GitHub. To learn how to view build logs, see [Viewing build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-view-build-logs#viewing_build_logs).

     * **Service account** : Select the service account to use when invoking your trigger. If your organization policy allows using the legacy Cloud Build service account, you can leave this blank to use the legacy service account. Otherwise, you must select the specific service account to use, even if it's the Compute Engine default service account.

**Note:** Only the service account specified on your trigger is used for builds executed by triggers. If you specified a service account in your build config, it's ignored during build execution when using triggers.
  5. Click **Create** to save your build trigger.




To create GitHub triggers using `gcloud` commands, see the `gcloud` commands for [Creating a build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

###  gcloud CLI 

To create GitHub Enterprise triggers using `gcloud` commands, run the following command:
    
    
        gcloud builds triggers create github \
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
  * CONNECTION_NAME is the name of your GitHub Enterprise connection.
  * REPO_NAME is the name of your repository
  * BRANCH_PATTERN is the branch name in your repository to invoke the build on.
  * TAG_PATTERN is the tag name in your repository to invoke the build on.
  * BUILD_CONFIG_FILE is the path to your build configuration file.
  * SERVICE-ACCOUNT is the service account to use for trigger and build operations.



###  API 

To create a GitHub Enterprise trigger with the API, use the following JSON template:
    
    
    {
        "filename": "cloudbuild.yaml",
        "name": "curl-trigger",
        "description": "curl trigger",
        "repository_event_config": {
          "repository": "REPO_NAME",
          "repository_type": "GITHUB_ENTERPRISE",
          // Field filter must be only one of the following:
          "pullRequest": "PULL_REQUEST_FILTER",
          "push": "PUSH_FILTER"
        }
    }
    

Where:

  * "REPO_NAME" is the name of the repository connection that you configured in Cloud Build.
  * "PULL_REQUEST_FILTER" is an instance of [`PullRequestFilter`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter), which defines the filter that allows Cloud Build to trigger a build when a matching pull request is made in GitHub Enterprise.
  * "PUSH_FILTER" is an instance of [`PushFilter`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter), which defines the filter that allows Cloud Build to trigger a build when a matching push is made in GitHub Enterprise.



Enter the following `curl` command in your terminal:
    
    
      curl -X POST -H "Authorization: Bearer "$(gcloud auth print-access-token) -H "Content-Type: application/json; charset=utf-8" -H "x-goog-user-project: PROJECT_NUMBER" https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/triggers -d @trigger.json
    

Where:

  * PROJECT_NUMBER is your Google Cloud project number.
  * PROJECT_ID is your Google Cloud project ID.



## Data sharing

The data sent to GitHub Enterprise from Cloud Build helps you identify triggers by name and see build results on GitHub Enterprise.

The following data is currently shared between Cloud Build and GitHub Enterprise:

  * Cloud project ID
  * Trigger name
  * Build logs

**Note:** Build logs are only shared if you configure your trigger to send build logs.

If you created triggers prior to August 2020, data sharing may not be enabled for your project. You can enable data sharing for all GitHub Enterprise triggers in your project by clicking **Enable** on the [Cloud Build Data sharing tab](https://console.cloud.google.com/cloud-build/settings/data-sharing).

If you have [required status checks](https://docs.github.com/en/github/administering-a-repository/enabling-required-status-checks) enabled for a GitHub Enterprise repository, enabling data sharing may temporarily break status checks. You can adjust status check configurations to look for your trigger name by:

  * Disabling any Cloud Build-specific required checks on the GitHub Enterprise repository
  * Ensuring that data sharing is enabled in Cloud Build
  * Executing a new build in Cloud Build that posts statuses to your repository
  * Re-enabling required status checks, selecting trigger name

**Note:** Enabling data sharing for a project is not reversible.

## Next steps

  * Learn how to [create and manage triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [build repositories from GitHub Enterprise in a private network](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
