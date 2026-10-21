---
url: https://docs.cloud.google.com/build/docs/automate-builds-webhook-events/
title: Automate builds in response to webhook events \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:24.169062+00:00
---

# Automate builds in response to webhook events  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automate-builds-webhook-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Automate builds in response to webhook events Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

Cloud Build lets you define **webhook triggers** to authenticate and accept incoming webhook events. These events, sent to a custom URL, let you connect external systems and source code management platforms, such as Bitbucket.com, Bitbucket Server, or GitLab, directly to Cloud Build.

With webhook triggers, you can specify an inline build configuration rather than a source repository. This inline configuration gives you control over Git operations and the build workflow. To automate builds on repository events instead, you can use [Cloud Build repository triggers](https://docs.cloud.google.com/build/docs/repositories), which integrate directly with providers like GitHub and GitLab.

With webhook triggers, you can define an inline build configuration file rather than specify a source when creating your trigger. The inline build configuration gives you control over Git operations and lets you define the rest of your build.

This page outlines how you can create webhook triggers to automate builds in response to webhook events.

**Note:** If you're creating a trigger that automates builds on repository events, we recommend using Cloud Build repository triggers. Repository triggers that use Cloud Build repositories (2nd gen) can be configured programmatically and are integrated with source providers, including support for GitHub and GitLab. Cloud Build repositories (2nd gen) also manage authentication tokens and information on your behalf using Secret Manager. Repository triggers let you filter incoming events and post build status back to the source provider, and can also be configured to work with a private network. To learn more, see the [Repositories overview](https://docs.cloud.google.com/build/docs/repositories) page.

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/create-webhook-triggers)



  * To use `gcloud` commands on this page, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  * If your webhook trigger uses a Cloud Build repository as a source, ensure that you're familiar with [Cloud Build repositories](https://docs.cloud.google.com/build/docs/repositories).




## Create webhook triggers

###  Console 

To create a webhook trigger using the Google Cloud console:

  1. Open the **Triggers** page:

[Open the Build triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Select your project from the top of the page and click **Open**.

  3. Click **Create trigger**.

  4. Enter the following trigger settings:

     * **Name** : A name for your trigger.
     * **Region** : Select the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger.

       * If the build config file associated with the trigger specifies a [private pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview), then Cloud Build uses the private pool to run your build. In this case, the region you specify in your trigger must match the region where you created your private pool.
       * If the build config file associated with the trigger **doesn't** specify a private pool, then Cloud Build uses the default pool to run your build in the same region as your trigger.
     * **Description** (Optional): A description for your trigger.

     * **Event** : Select **Webhook event** to set up your trigger to start builds in response to incoming webhook events.

     * **Webhook URL** : Use the webhook URL to authenticate incoming webhook events. You'll need a secret to authenticate incoming webhook events. You can create a new secret or use an existing secret. This secret is separate from the secret associated with your SSH key.

To create a secret:

       1. Select **Use a new secret (generated by Cloud Build)**.
       2. Click **Create Secret**.

You will see the **Create a webhook secret** dialog.

       3. In the **Secret name** field, enter a name for your secret.

       4. Click **Create secret** to save your secret, which will automatically be created and stored for you in Secret Manager.

To use an existing secret:

       1. Select **Use an existing secret or create your own**.
       2. In the **Secret** field, select the name of the secret you want to use from the drop-down menu or follow the instructions to add a secret by resource ID.
       3. In the **Secret version** field, select your secret version from the drop-down menu.

If you use an existing secret, you may need to manually grant the Secret Manager Secret Accessor role to your Cloud Build service account, `service-${PROJECT_NUMBER}@gcp-sa-cloudbuild.iam.gserviceaccount.com`. To learn more, see [Granting Secret Manager role to your service account](https://docs.cloud.google.com/build/docs/automating-builds/create-webhook-triggers#optional_granting_role_to_your_service_account).

After you have created or selected your secret, you'll see a **Webhook URL preview**. Your URL will contain an API key generated by Cloud Build and your secret. If Cloud Build is unable to retrieve your API key, you can manually add your API key to the URL or learn how to [obtain an API key](https://docs.cloud.google.com/build/docs/automating-builds/create-webhook-triggers#optional_obtaining_an_api_key) if you don't have one yet.

You can use the URL to [invoke a webhook event](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events#invoke) by making an HTTP request using the POST method.

After completing these steps, the **Secret Manager Secret Accessor** role is automatically granted to your Cloud Build service agent, `service-${PROJECT_NUMBER}@gcp-sa-cloudbuild.iam.gserviceaccount.com`. If you don't see this role automatically added to your service agent, complete the following steps outlined in [Granting Secret Manager role to your service account](https://docs.cloud.google.com/build/docs/automating-builds/create-webhook-triggers#optional_granting_role_to_your_service_account).

     * **Source** (optional): If you're specifying an inline build configuration, you're not required to specify a source. Otherwise, do the following:

       * **Repository generation** : Select **2nd generation**.

       * **Repository** : From the list of available repositories, select the repository from which you want to build. The region of your repository must match the region of your trigger.

       * **Branch** or **Tag** : Specify a regular expression with the branch or tag value to match. For information on acceptable regular expression syntax, see [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

       * **Comment control** : If you selected **Pull request** as your **Event** , choose one of the following options to control whether the trigger automatically invokes a build:

**Warning:** Any user with read access to the repository can submit a pull request, which may run a build that includes changes to the source code in the pull request. To disable this behavior, we recommend using [manual approvals](https://docs.cloud.google.com/build/docs/automating-builds/approve-builds) to gate builds when making pull requests on public repositories. You can also learn more about the [build-time privileges of triggers](https://docs.cloud.google.com/build/docs/cloud-build-service-account#build_triggers).
         * **Required except for owners and collaborators** : When a pull request is created or updated by a repository owner or collaborator, builds are run automatically. If an external contributor initiates the action, builds are run only after an owner or collaborator comments `/gcbrun` on the pull request.

         * **Required** : When a pull request is created or updated by any contributor, builds are run only after an owner or collaborator comments `/gcbrun` on the pull request. Builds are run each time a change to a pull request is made.

         * **Not required** : When a pull request is created or updated by any contributor, builds are run automatically.

     * **Configuration** : Select the build config file located in your remote repository or create an inline build config file to use for your build. If you did not specify a source repository, you must select an **Inline** build config file as your configuration option:

       * **Type** : Select the type of configuration to use for your build.

         * **Cloud Build configuration file (yaml or json)** : Use a build config file for your configuration.
         * **Dockerfile** : Use a `Dockerfile` for your configuration.
         * **Buildpacks** : Use [buildpacks](https://buildpacks.io/) for your configuration.
       * **Location** : Specify the location for your configuration.

         * **Repository** : If your config file is located in your remote repository, provide the location of your [build config file](https://docs.cloud.google.com/build/docs/build-config), the `Dockerfile` directory, or the buildpacks directory. If your build config type is a `Dockerfile` or a buildpack, you will need to provide a name for the resulting image and optionally, a timeout for your build. When you've provided the `Dockerfile` or buildpack image name, you'll see a preview of the `docker build` or `pack` command that your build will run.
         * **Buildpack environment variables** (optional): If you selected `buildpacks` as your configuration type, click **Add pack environment variable** to specify your buildpack environment variables and values. To learn more about buildpack environment variables, see [Environment variables](https://buildpacks.io/docs/app-developer-guide/environment-variables/).
         * **Inline** : If you selected **Cloud Build configuration file (yaml or json)** as your configuration option, you can specify your build config inline. Click **Open Editor** to write your build config file in the Google Cloud console using YAML or JSON syntax. Click **Done** to save your build config.

**Note:** Inline build configuration support is not available for `Dockerfile` or buildpacks.

In the following example, the inline build config file logs echoes "hello world":
    
    steps:
     - name: 'ubuntu'
       args: ['echo', 'hello world']
    

     * **Substitutions** (optional): If you selected the build config file as your build config option or created an inline build config file, you can choose to define trigger-specific [substitution variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) using this field. You can also obtain data using [payload bindings](https://docs.cloud.google.com/build/docs/configuring-builds/use-bash-and-bindings-in-substitutions#payload_bindings) when defining substitution variables values.

     * **Filters** (optional): You can create a rule within a trigger that determines whether or not your trigger will run a build based on your substitution variables.

  5. Click **Create** to create your build trigger.




###  gcloud 

To create a webhook trigger:
    
    
    gcloud builds triggers create webhook \
      --trigger-config=TRIGGER_CONFIG_PATH \
      --name=TRIGGER_NAME \
      --description=DESCRIPTION \
      --region=REGION \
      --secret=projects/PROJECT_ID/secrets/SECRET_NAME/versions/SECRET_VERSION \
      --service-account=SERVICE_ACCOUNT \ 
      --repository=projects/PROJECT_ID/locations/REGION/connections/CONNECTION_NAME/repositories/REPO_NAME \ 
      --build-config=PATH_TO_BUILD_CONFIG \
      --inline-config=PATH_TO_INLINE_BUILD_CONFIG \
      --dockerfile=DOCKERFILE \
      --dockerfile-dir=DOCKERFILE_DIR \
      --dockerfile-image=DOCKERFILE_IMAGE \
      --tag=TAG_NAME \
      --branch=BRANCH_NAME \
      --substitutions=_SUB_ONE=SUBSTITUTION \
      --subscription-filter=FILTER \
      --require-approval
    

Where:

  * `TRIGGER_CONFIG_PATH` Is the path to a trigger config file. If you use a trigger config file, then the `name`, `description`, `region`, `secret`, `service-account`, `subscription-filter`, and `substitution` fields must remain undefined. For more information, see [BuildTrigger](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.triggers) in the Cloud Build reference documentation.
  * `TRIGGER_NAME` is the name of your trigger.
  * `DESCRIPTION` (Optional) is a description for your trigger.
  * `REGION` is the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger. This value must be a region other than "global".
  * `SECRET_NAME` is the name of your secret as stored in Secret Manager.
  * `SECRET_VERSION` is the version associated with your secret as stored in Secret Manager.
  * `SERVICE_ACCOUNT` is the service account used to run all user-controlled operations related to your build trigger. If you don't define a service account, Cloud Build uses the default Cloud Build service account.
  * `PROJECT_ID` is your Google Cloud project ID.
  * `CONNECTION_NAME` is the name of your host connection.
  * `REPO_NAME` is the name of your repository.
  * `PATH_TO_BUILD_CONFIG` is the path to a build config file. Use this parameter if your trigger refers to a build config file in a Cloud Build repository. If you set this parameter, you can't define an `inline-config` or use parameters for a Dockerfile.
  * `PATH_TO_INLINE_BUILD_CONFIG` is the path to an inline build config. Use this parameter if trigger refers to a local build config file. If you set this parameter, you can't define a `build-config` or use parameters for a Dockerfile.
  * `DOCKERFILE` is the path to a Dockerfile. Use this parameter if your trigger refers to a Dockerfile. If you set Dockerfile parameters, you can't define a `build-config` or an `inline-config`.
  * `DOCKERFILE_DIR` is the directory of the Dockerfile.
  * `DOCKERFILE_IMAGE` is the name of the Docker image that Cloud Build builds.
  * `BRANCH_NAME` is the name of your branch if you want to set your trigger to build on a branch. If you set this parameter, you can't define a `tag`.
  * `TAG_NAME` is the name of your tag if you want to set your trigger to build on a tag. If you set this parameter, you can't define a `branch`.
  * `SUBSTITUTION` (Optional) are parameters to be substituted in the build specification. For example, `_SUB_ONE='$(body.message.test)',_SUB_TWO='$(body.message.output)'`.
  * `FILTER` (Optional) is a CEL filter expression for the trigger, such as `'_SUB_ONE == "prod"'`.
  * (Optional) When `--require-approval` is present in the command, Cloud Build requires manual approval for triggered builds.



## Invoke a webhook event

Use the following command to invoke a webhook event:
    
    
    curl -X POST -H "Content-type: application/json" "https://cloudbuild.googleapis.com/v1/projects/${PROJECT_ID}/locations/${REGION}/triggers/${TRIGGER_NAME}:webhook?key=${API_KEY}&secret=${SECRET_VALUE}&trigger=${TRIGGER_NAME}&projectId=${PROJECT_ID}" -d "{}"
    

## (Optional) Grant Secret Manager role to your service account

When you configure your secret during webhook trigger creation, in most cases, Cloud Build automatically grants the **Secret Manager Secret Accessor** role to service accounts that require the role. However, if you use an existing secret, you may also need to manually grant the Secret Manager Secret Accessor role to your Cloud Build service account:

  1. Open the IAM page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Optional: To see Google-provided accounts, select the **Include Google-provided role grants** checkbox.

  3. Take note of the build service account you would like to grant the role to.

  4. Open the **Secret Manager** page in the Google Cloud console:

[Open the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

  5. Click the name of your secret.

You will see the **Secret details** page.

     1. Click the **Permissions** tab.

     2. Click **Grant access**.

You will see the **Grant access** panel.

     3. In the **Add Principals** section, add the email associated with the build service account.

     4. In the **Assign roles** section, select **Secret Manager** > **Secret Manager Secret Accessor**.

     5. Click **Save**.




## (Optional) Obtain an API key

To authenticate an incoming webhook event, you need an API key. This API key is part of the secret that you choose when configuring your webhook trigger. If you don't have an API key yet, or Cloud Build wasn't able to retrieve one when configuring your secret in the Google Cloud console, then you can manually create an API key:

To obtain an API key:

  1. Open the **Credentials** page in the Google Cloud console:

[Open the Credentials page](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials**.

  3. Click **API Key**.

You will see a dialog with your API key created. Take note of your API key.

  4. If you would like to restrict your key for product applications, click **Restrict key** to complete additional steps to secure your key. Otherwise, click **Close**.

To learn how to restrict your key, see [Applying API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).




## What's next

  * Learn how to [create and manage triggers](https://docs.cloud.google.com/build/docs/running-builds/create-manage-triggers).
  * Learn how to [build repositories hosted on on Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/build-hosted-repos-bitbucket-server).
  * Learn how to [start builds manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually).
  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
