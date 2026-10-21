---
url: https://docs.cloud.google.com/source-repositories/docs/integrating-with-cloud-build/
title: Automating builds with Cloud Build \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:44.616001+00:00
---

# Automating builds with Cloud Build  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/integrating-with-cloud-build/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Automating builds with Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to automate builds using Cloud Build and Cloud Source Repositories.

You can configure Cloud Build to automatically build a new image any time a user pushes a change to files stored in Cloud Source Repositories. Events that initiate automatic builds are called _[build triggers](https://docs.cloud.google.com/build/docs/triggers)_. These triggers can help ensure that your container images are kept up to date. You can also use them to build and test feature branches.

Build triggers can perform a build based on either a Dockerfile or a build config file.

### Using a Dockerfile

To use a Dockerfile for your build configuration, you'll need to specify the Dockerfile directory and supply a name for the resulting image. For details about creating Dockerfiles, see the [Docker documentation](https://docs.docker.com/engine/reference/builder/).

After you provide the Dockerfile and image name, you'll see a preview of the `docker build` command that your build executes and a summary of the trigger configuration.

### Using a build config file

To use a build config file for your build configuration, you'll need to provide the location of a [build config file](https://docs.cloud.google.com/build/docs/build-config-file-schema).

Once you've set the location, you'll see a summary of the trigger.

## Before you begin

  * Enable the Cloud Build API. 

[Enable the Cloud Build API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https://cloud.google.com//source-repositories/docs/automate-app-engine-deployments-cloud-build)

  * Ensure you have source code in Cloud Source Repositories.

  * Ensure you have either a Dockerfile or a [build config file](https://docs.cloud.google.com/build/docs/build-config-file-schema).

  * If using a service account other than the default Cloud Build service account, see the Cloud Build page on [Configuring user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).




## Additional information

  * Build triggers use _shallow clones_ of a repository. With shallow clones, only the single commit that triggered an automatic build is checked out in the workspace. For more information, and to learn how to include more of your repositories history, see Unshallowing clones.

  * If you use another hosted Git provider, such as on GitHub or Bitbucket, and still need to mirror the repository into Cloud Source Repositories, you must have the `cloudbuilds.builds.create` permission for the Google Cloud project with which you're working. This permission is typically granted through the [`cloudbuild.builds.editor`](https://docs.cloud.google.com/build/docs/iam-roles-permissions) role.

When you set up a build trigger with an external repository for the first time, you'll need to set up authorization with that repository. For more information, see [Adding a repository as a remote](https://docs.cloud.google.com/source-repositories/docs/adding-repositories-as-remotes).

After you set up your external repository, Cloud Source Repositories creates a mirror of your repository.

  * For information on the quotas and limits for Cloud Build, see [Quotas and limits](https://docs.cloud.google.com/build/quotas) in the Cloud Build documentation.




## Create a build trigger

###  Console 

  1. Open the **Triggers** page in the Google Cloud console.

[Open the Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Select your project from the project selector drop-down menu at the top of the page.

  3. Click **Open**.

  4. Click **Create trigger**.

  5. Enter the following trigger settings:

     * **Name** : Enter a name for your trigger.

     * **Description** (optional): Enter a description for your trigger.

     * **Event** : Select the repository event to invoke your trigger.

       * **Push to a branch** : Set your trigger to start a build on commits to a particular branch.

       * **Push new tag** : Set your trigger to start a build on commits that contain a particular tag.

**Note:** Whether based on branch commits or tag commits, builds are only invoked on _pushes to the remote origin_ \-- not on local changes, pre-submits, or pull requests.
     * **Source** : Select the repository and the corresponding branch or tag to watch for events.

       * **Repository** : From the list of available repositories, select the desired repository. To connect a new repository, see Connecting to source repositories.

When your build executes, the contents of your repository will be copied to `/workspace`, the default working directory used by Cloud Build. Learn more about working directories on the [Build configuration overview page](https://docs.cloud.google.com/build/docs/build-config).

       * **Branch** or **Tag** : Specify a regular expression with the branch or tag value to match. Forward slashes (`/`) cannot be used in tags. For more information on acceptable regular expression syntax, see [RE2 syntax](https://github.com/google/re2/wiki/Syntax).
     * **Configuration** : Select the build config file located in your remote repository or create an inline build config file to use for your build.

       * **Type** : Select the type of configuration to use for your build. 
         * **Cloud Build configuration file (yaml or json)** : Use a build config file for your configuration.
         * **Dockerfile** : Use a `Dockerfile` for your configuration.
         * **Buildpacks** : Use [buildpacks](https://buildpacks.io/) for your configuration.
       * **Location** : Specify the location for your configuration.

         * **Repository** : If your config file is located in your remote repository, provide the location of your [build config file](https://docs.cloud.google.com/build/docs/build-config), the `Dockerfile` directory, or the buildpacks directory. If your build config type is a `Dockerfile` or a buildpack, you will need to provide a name for the resulting image and optionally, a timeout for your build. When you've provided the `Dockerfile` or buildpack image name, you'll see a preview of the `docker build` or `pack` command that your build will execute.
         * **Buildpack environment variables** (optional): If you selected `buildpacks` as your configuration type, click **Add pack environment variable** to specify your buildpack environment variables and values. To learn more about buildpack environment variables, see [Environment variables](https://buildpacks.io/docs/app-developer-guide/environment-variables/).
         * **Inline** : If you selected **Cloud Build configuration file (yaml or json)** as your configuration option, you can specify your build config inline. Click **Open Editor** to write your build config file in the Google Cloud console using YAML or JSON syntax. Click **Done** to save your build config.

**Note:** Inline build configuration support is not available for `Dockerfile` or buildpacks.
     * **Service account** : Select the service account to use when invoking your trigger. If you do not select a service account, the default [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) is used.

**Note:** Only the service account specified on your trigger will be used for builds executed by triggers. If you specified a service account in your build config, it will be ignored during build execution when using triggers.
  6. Click **Create** to save your build trigger.




###  gcloud 

Run the following command:
    
    
        gcloud beta builds triggers create cloud-source-repositories \
        --repo=REPO_NAME \
        --branch-pattern=BRANCH_PATTERN \ # or --tag-pattern=TAG_PATTERN
        --build-config=BUILD_CONFIG_FILE \
        --service-account=SERVICE_ACCOUNT \
        --require-approval
    

Where:

  * REPO_NAME is the name of your repository.
  * BRANCH_PATTERN is the branch name in your repository to invoke the build on.
  * TAG_PATTERN is the tag name in your repository to invoke the build on.
  * BUILD_CONFIG_FILE is the path to your build configuration file.
  * SERVICE_ACCOUNT ([preview](https://cloud.google.com/products#product-launch-stages)) is the email associated with your service account. If you don't include this flag, the default [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) is used.

**Note:** Only the service account specified in the `gcloud beta build triggers create` command is used for builds invoked with triggers. Build triggers ignore the service account specified in the build config file.

  * [Optional] `--require-approval` is the flag to include to configure your trigger to require approval.



For a complete list of flags, see the [`gcloud` reference for how to create triggers for Cloud Source Repositories](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/triggers/create/cloud-source-repositories).

After you run the `gcloud` command to create a trigger using Cloud Source Repositories, you should see an output similar to the following:
    
    
      NAME         CREATE_TIME                STATUS
      trigger-001  2019-10-30T20:45:03+00:00
    

**Note:** The trigger name is automatically generated for you. You can change the name of your trigger via the [Google Cloud console](https://console.cloud.google.com/cloud-build/triggers).

## View build triggers

To view triggers in the Google Cloud console, open the Cloud Build **Triggers** page.

To view triggers for a given project in Cloud Source Repositories, click **Settings** settings in the top-right, then click **Cloud Build Triggers**.

## Skip a build trigger

In some cases, you might want to change your source code but don't want to trigger a build, for example, when you update documentation or configuration files.

In such cases, you can include `[skip ci]` or `[ci skip]` in the commit message, and a build will not be triggered.

For example:
    
    
    Author: A User <auser@example.com>
    Date:   Tue Apr 3 12:03:35 2018 -0700
    
    Fixed customer affecting issue. [skip ci]
    

If you want to run a build on that commit later, use the **Run trigger** button.

## Unshallowing clones

To build your source on a Git repository, Cloud Source Repositories performs a _shallow clone_ of the repository. When Cloud Source Repositories performs a shallow clone, it checks out from the workspace only the single commit that triggered the build, and then it builds from that source. Cloud Source Repositories doesn't check out any other branches or history. This is done for efficiency. Builds aren't delayed while Cloud Source Repositories fetches the whole repository and history just to build from a single commit.

To include more of your repo's history in the build, add a build step in your build config file to "unshallow" the clone. For example:
    
    
    steps:
    - name: gcr.io/cloud-builders/git
      args: ['fetch', '--unshallow']
    ...
    

For more information on `git fetch`, see [git reference](https://git-scm.com/docs/git-fetch). For instructions on writing a build config file, see [Build config overview](https://docs.cloud.google.com/build/docs/build-config).

## What's next

  * Learn how to [start builds manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) in Cloud Build.
  * Learn more about [building, testing, and deploying artifacts](https://docs.cloud.google.com/build/docs/configuring-builds/build-test-deploy-artifacts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
