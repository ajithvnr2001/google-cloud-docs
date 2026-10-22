---
url: https://docs.cloud.google.com/build/docs/manually-build-code-source-repos/
title: Manually build code in source repositories \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:29.001276+00:00
---

# Manually build code in source repositories  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/manually-build-code-source-repos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Manually build code in source repositories Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

This page explains how to create manual triggers to build code in source repositories. Manual triggers can be used to invoke builds manually, with the ability to override defined substitution variable values at invocation time prior to running a build. You can also schedule manual triggers to automatically run at a specific time.

To learn how to start builds manually using the gcloud CLI or the Cloud Build API, see [Starting builds manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually).

## Before you begin

  * Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/create-manual-triggers)



  * Have your source code ready.



## Manual triggers

Manual triggers enable you to set up builds that are only executed when you invoke your trigger on connected repositories. For example, you create a pipeline for deploying your source code to a staging or production environment. You might want to automate your workflow, but are only looking to execute builds manually. You can define manual triggers to do so.

Manual triggers enable you to manually invoke builds by:

  * Fetching source code from a hosted repository with a specified branch or tag.
  * Parameterizing your build with substitutions that don't need to be passed in manually each time you execute a build.
  * Overriding defined substitution variable values at invocation time prior to invoking a build.



If you want to execute builds from your local working directory instead of a hosted repository or want to submit builds without creating a trigger, you can run the following `gcloud` command in your working directory:
    
    
    gcloud builds submit --config BUILD_CONFIG SOURCE_CODE
    

Where:

  * BUILD_CONFIG is the path to the build config file.
  * SOURCE_CODE is the path or URL source code.



To learn more about how to use the `gcloud` command to start builds manually in your local directory, see [Starting builds manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually).

## Creating manual triggers

###  Console 

To create a manual trigger:

  1. Open the **Triggers** page:

[Open the Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Select your project from the top of the page and click **Open**.

  3. Click **Create trigger**.

  4. Enter the following trigger settings:

     * **Name** : A name for your trigger.
     * **Region** : Select the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger.

       * If you select **global** as the region, Cloud Build uses the default pool to run your build.
       * If you select a non-global region and the build config file associated with the trigger specifies a [private pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview), Cloud Build uses the private pool to run your build. In this case, the region you specify in your trigger must match the region where you created your private pool.
       * If you select a non-global region and the build config file associated with the trigger does **not** specify a private pool, Cloud Build uses the default pool to run your build in the same region as your trigger.
     * **Description** (Optional): A description for your trigger.

     * **Event** : Select **Manual invocation** to set up your trigger so that builds only run when the trigger is manually invoked.

     * **Source** : Select the repository to build when the manual trigger runs.

**Note:** The region of your repository must match the region of your trigger. If your source is in Cloud Source Repositories, your repository is not connected to a particular region, but to your project.

**Caution:** Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

     * **Repository generation** : Select **2nd gen**. 

     * **Branch** or **Tag** : Set one of the following:

       * **Branch** : Set a trigger to build on this branch. You must specify a literal value. Regular expressions aren't supported.
       * **Tag** : Set a trigger to build on this tag. You must specify a literal value. Regular expressions aren't supported.
     * **Configuration** : Select the build config file located in your remote repository or create an inline build config file to use for your build.

       * **Type** : Select the type of configuration to use for your build. 
         * **Cloud Build configuration file (yaml or json)** : Use a build config file for your configuration.
         * **Dockerfile** : Use a `Dockerfile` for your configuration.
       * **Location** : Specify the location for your configuration.

         * **Repository** : If your config file is located in your remote repository, provide the location of your [build config file](https://docs.cloud.google.com/build/docs/build-config), the `Dockerfile` directory, or the buildpacks directory. If your build config type is a `Dockerfile` or a buildpack, you will need to provide a name for the resulting image and optionally, a timeout for your build. When you've provided the `Dockerfile` or buildpack image name, you'll see a preview of the `docker build` or `pack` command that your build will execute.
         * **Inline** : If you selected **Cloud Build configuration file (yaml or json)** as your configuration option, you can specify your build config inline. Click **Open Editor** to write your build config file in the Google Cloud console using YAML or JSON syntax. Click **Done** to save your build config.
**Note:** Inline build configuration support is not available for `Dockerfile`.
  5. Click **Create** to create your manual trigger.




###  gcloud 

**Preview — Manual triggers: Cloud Build repositories (2nd gen) support**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create a manual trigger:

  1. Open a terminal window.
  2. Run the following `gcloud` command to create a build trigger in your project:
         
         gcloud builds triggers create manual \
           --region=REGION \
           --name=TRIGGER_NAME \
           --repository=projects/PROJECT_ID/locations/REGION/connections/CONNECTION_NAME/repositories/REPO_NAME \
           --branch=BRANCH_NAME \
           --build-config=BUILD_CONFIG_FILE \
           --service-account=SERVICE_ACCOUNT
         




Where:

  * `REGION` is the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger.
  * `TRIGGER_NAME` is the name of your trigger.
  * `PROJECT_ID` is your Google Cloud project ID.
  * `CONNECTION_NAME` is the name of your host connection.
  * `REPO_NAME` is the name of your repository.
  * `BRANCH_NAME` is the name of your branch. You can also specify a tag using `--tag` or a commit ID using `--sha`.
  * `BUILD_CONFIG_FILE` is the path to your build configuration file. You can also specify an inline build configuration file using `--inline-config` or a Dockerfile using `--dockerfile`, `--dockerfile-dir`, and `dockerfile-image`.
  * `SERVICE_ACCOUNT` is the email associated with your service account. If you don't include this flag, a [default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) is used.



For a complete list of flags, see the [`gcloud` reference for how to create manual triggers](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/manual).

## Running manual triggers

###  Console 

To run a manual trigger using Google Cloud console:

  1. Open the **Triggers** page in the Google Cloud console.

[Open the triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Locate your trigger in the list.

  3. Click **Run trigger**.

After clicking **Run trigger** , you will see the **Run trigger** window pane on the right side. If you specified fields such as a branch name, tag name, or substitution variables, you will be able to override these fields at invocation time.

If the trigger uses a repository with more than 500 branches or tags, some of them may be missing from the suggestions. You can still enter a branch or tag name manually.

**Note:** You cannot specify any new fields or variables in this window pane. To do so, see instructions in the `gcloud` tab in this section.

If you specified new variable values for your substitution, click **Run trigger** to execute your build.

To run manual triggers on schedule, see [Scheduling builds](https://docs.cloud.google.com/build/docs/schedule-builds).




###  gcloud 

To run a manual trigger using the `gcloud` command-line tool, run the following command:
    
    
          gcloud builds triggers run TRIGGER_NAME \
             --region=REGION \
             --branch=BRANCH_NAME \
             --substitutions=SUBSTITUTION_VAR=SUBSTITUTION_VALUE
    

Where:

  * `TRIGGER_NAME` is the name of your trigger.
  * `REGION` is the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger. 
  * `BRANCH_NAME` is the name of your branch. You can also specify a tag using `--tag` or a commit ID using `--sha`.
  * `SUBSTITUTION_VAR` (Optional) is the variable name for your substitution value.
  * `SUBSTITUTION_VALUE` (Optional) is the value associated with your substitution variable.



To run manual triggers on schedule, see [Scheduling builds](https://docs.cloud.google.com/build/docs/schedule-builds).

## Next steps

  * Learn how to [start builds manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) using `gcloud` commands or the Cloud Build API.
  * Learn how to [schedule builds](https://docs.cloud.google.com/build/docs/automating-builds/schedule-builds).
  * Learn how to [create and manage triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
