---
url: https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts/
title: Run builds with a user-managed service account \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:11.213301+00:00
---

# Run builds with a user-managed service account  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Run builds with a user-managed service account Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your builds to use a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed).

If you don't specify a user-managed service account for your builds, Cloud Build automatically uses the [default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account). This default service account might have unnecessarily broad permissions, such as access to your Cloud Source Repositories and any Cloud Storage bucket in your project.

We recommend following the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely) by assigning permissions and roles to service accounts scoped to the task they performs. For example, you can use one service account for building and pushing images to Artifact Registry, as shown on the [Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/practicing-principle-least-privilege-cloud-build-and-artifact-registry).

## Before you begin

  * Enable the Cloud Build and IAM APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,iam.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts)

  * If you plan to use this account to create and manage credentials, for example to [create short-lived credentials](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct), enable the IAM Service Account Credentials API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts)

  * [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts), if you haven't already done so.




## Set up the service account

Grant IAM roles to your user-managed service account so that it has the permissions it needs to run your builds. You can also configure Cloud Build to automatically choose this service account for new triggers.

  1. In the Google Cloud console, go to the _settings_ Cloud Build **Permissions** page: 

[Go to **Permissions**](https://console.cloud.google.com/cloud-build/settings)

  2. Go to the **Service account** menu and select your service account. To choose a service account in a different project, click **Switch project**.

  3. To use the selected service account as the service account for new triggers, turn on **Set as pre-selected for new triggers**.

  4. In the list of Google Cloud services, enable the IAM roles that you want to grant to your service account.

  5. If the role you need for your build pipeline is not listed here, you can [grant additional roles in the IAM configurations page](https://docs.cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role).

  6. If you selected a service account in a different project, complete the steps in Cross-project setup.




To learn more about the IAM roles commonly required for a build, see the following information:

  * [Default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).
  * [Configuring access to Cloud Build resources](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources).
  * [Cloud Build IAM roles and permissions](https://docs.cloud.google.com/build/docs/iam-roles-permissions).



## Set up build logs

When you specify your own service account for builds, you must store your build logs in one of the following bucket types:

  * Cloud Storage buckets in the user's project. These can be [user-created buckets](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-custom-logging) or [Google Cloud-created and user-owned buckets](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store_build_logs_in_a_user-owned_and_regionalized_bucket).

  * [Cloud Logging buckets](https://docs.cloud.google.com/logging/docs/buckets).




If you create a log bucket, make sure that it doesn't have a retention policy as the policy may prevent Cloud Build from writing build logs to the bucket.

You **can not** store your logs in a Google Cloud-owned log bucket.

For further information about where to store build logs, see [Build log storage options](https://docs.cloud.google.com/build/docs/securing-builds/build-log-storage).

## Run a build using a config file

To manually run a build using a config file:

  1. In your project root directory, create a Cloud Build build config file named `cloudbuild.yaml` or `cloudbuild.json`.

  2. Add the `serviceAccount` field and the preferred logging setup.

     * If you're storing the build logs in Cloud Logging, add a `logging` field and set the value of the field to `CLOUD_LOGGING_ONLY`.

     * If you're storing the build logs in a user-created Cloud Storage bucket:

       * Add a `logging` field and set its value to `GCS_ONLY`.
       * Add a `logsBucket` field and set its value to your Cloud Storage bucket location.

The following example configures Cloud Build to run builds using a user-managed service account and configures build logs to be stored in a user-created Cloud Storage bucket:

###  YAML 
    
    steps:
    - name: 'bash'
      args: ['echo', 'Hello world!']
    logsBucket: 'LOGS_BUCKET_LOCATION'
    serviceAccount: 'projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT'
    options:
      logging: GCS_ONLY
    

###  JSON 
    
    {
      "steps": [
      {
        "name": "bash",
        "args": [
          "echo",
          "Hello world!"
        ]
      }
      ],
      "logsBucket": "LOGS_BUCKET_LOCATION",
      "serviceAccount": "projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT",
      "options": {
        "logging": "GCS_ONLY"
      }
    }
    
    

Replace the variables in your build config file with the following:

     * `LOGS_BUCKET_LOCATION` is the Cloud Storage bucket to store build logs. For example, `gs://mylogsbucket`.
     * `PROJECT_ID` is the ID of the Google Cloud project where you're running the build.
     * `SERVICE_ACCOUNT` is the email address or unique ID of the service account you want to specify for builds. For example, a service account email address looks like: `service-account-name@project-id.iam.gserviceaccount.com`.
  3. Start the build using the build config file:
         
         gcloud builds submit --config CONFIG_FILE_PATH SOURCE_DIRECTORY
         

Replace the variables in the commands with the following values:

     * `CONFIG_FILE_PATH` is the path to the build config file.
     * `SOURCE_DIRECTORY` is the path or URL to the source code.

If you don't specify a CONFIG_FILE_PATH and SOURCE_DIRECTORY in the `gcloud builds submit` command, Cloud Build assumes that the build config file and the source code are in the current working directory.




## Run builds using triggers

To run a build with [Cloud Build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) using your own service account, set up your preferred logging option and select your preferred service account when creating the trigger.

If you want to use the same service account for all new triggers, you can configure Cloud Build to automatically select the service account.

  1. In the build config file:

     * If you're storing the build logs in Cloud Logging, add a `logging` field and set the value of the field to `CLOUD_LOGGING_ONLY`.

     * If you're storing the build logs in a user-created Cloud Storage bucket:

       * Add a `logging` field and set its value to `GCS_ONLY`.
       * Add a `logsBucket` field and set its value to your Cloud Storage bucket location.

The following example configures build logs to be stored in a user-created Cloud Storage bucket:

###  YAML 
    
    steps:
    - name: 'bash'
      args: ['echo', 'Hello world!']
    logsBucket: 'LOGS_BUCKET_LOCATION'
    options:
      logging: GCS_ONLY
    

###  JSON 
    
    {
      "steps": [
      {
        "name": "bash",
        "args": [
          "echo",
          "Hello world!"
        ]
      }
      ],
      "logsBucket": "LOGS_BUCKET_LOCATION",
      "options": {
        "logging": "GCS_ONLY"
      }
    }
    

Replace `LOGS_BUCKET_LOCATION` with the Cloud Storage bucket to store build logs. For example, `gs://mylogsbucket`.

  2. Specify a service account to use with your build trigger:

###  Console 

     1. [Create or edit your build trigger](https://console.cloud.google.com/cloud-build/triggers).

     2. In the **Service account** field, specify your service account. To choose a service account in a different project, click **Switch project**.

If you don't specify a service account, Cloud Build uses the [default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).

     3. Click **Create** to save your build trigger.

###  gcloud 

When creating a build trigger, specify your service account using the `--service-account` flag. In the following example, the `gcloud` command creates a build trigger that pulls code from a Git repository:
    
    gcloud builds triggers create github \
       --name=TRIGGER_NAME \
       --repo-name=REPO_NAME \
       --repo-owner=REPO_OWNER \
       --branch-pattern=BRANCH_PATTERN
       --build-config=BUILD_CONFIG_FILE
       --service-account=SERVICE_ACCOUNT
       --project=BUILD_PROJECT
    

Replace the variables in the build config file with the following values:

     * `TRIGGER_NAME` is the name of your build trigger.
     * `REPO_NAME` is the name of your repository.
     * `REPO_OWNER` is the username of the repository owner.
     * `BRANCH_PATTERN` is the branch name in your repository to invoke the build on.
     * `TAG_PATTERN` is the tag name in your repository to invoke the build on.
     * `BUILD_CONFIG_FILE` is the path to your build configuration file.
     * `SERVICE_ACCOUNT` is your service account in the format `/projects/PROJECT_ID/serviceAccounts/ACCOUNT_ID_OR_EMAIL`.
     * `BUILD_PROJECT` is the project where you're starting builds.


**Note:** If you specify a service account in your build config, it will be ignored during build invocation when you run your trigger. Only the service account specified on your trigger will be used for builds invoked with triggers.

## Cross-project setup

You can use a user-managed service account to run builds in a project that's different from the project where you created the service account only if the `iam.disableCrossProjectServiceAccountUsage` organization policy constraint isn't enforced. This constraint is enforced by default. [Learn more](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

  * The following command disables enforcement of that constraint and grants the necessary access. Your organization needs to be aware of the security trade-offs involved before setting the constraint in your organization policy:
        
        gcloud resource-manager org-policies disable-enforce \
           iam.disableCrossProjectServiceAccountUsage \
           --project=SERVICE_ACCOUNT_PROJECT_ID
        

In this command, SERVICE_ACCOUNT_PROJECT_ID is the project that contains your user-managed service account

  * In the project that has your user-managed service account, grant the `roles/iam.serviceAccountTokenCreator` role for the Cloud Build service agent of the project where you're running builds:
        
        gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
            --member="serviceAccount:BUILD_SERVICE_AGENT" \
            --role="roles/iam.serviceAccountTokenCreator"
        

Replace the variables in the command with the following:

    * `SERVICE_ACCOUNT_PROJECT_ID`: The project ID of the project that contains your user-managed service account.
    * `BUILD_SERVICE_AGENT`: The email ID of the service agent of the form `service-BUILD_PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com`, where `BUILD_PROJECT_NUMBER` is the project number of the project where you're running builds. You can get the project number from the [project settings page](https://console.cloud.google.com/iam-admin/settings).



**Limitations:**

  * Your Google Cloud project must be in a Google Cloud organization.

  * You must start builds in the command line using `gcloud builds submit` or `gcloud builds triggers create`.




## What's next

  * Learn more about [Cloud Build IAM roles and permissions](https://docs.cloud.google.com/build/docs/iam-roles-permissions).
  * Learn how the [service account changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates) impact how you run your builds.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
