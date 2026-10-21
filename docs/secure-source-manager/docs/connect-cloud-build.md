---
url: https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build/
title: Connect to Cloud Build \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:44.748017+00:00
---

# Connect to Cloud Build  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Connect to Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

This page details how to invoke builds automatically from Secure Source Manager using Cloud Build configuration files and a triggers YAML file in your Secure Source Manager repository.

By default, Secure Source Manager uses a Google-managed service agent to interact with Cloud Build and other resources. To isolate team permissions, we recommend you configure a per-repository identity by associating a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-managed) with your repository. Secure Source Manager uses the user-managed service account associated with the repository to trigger builds.

Unlike the default service agent, you can configure a user-managed service account with the `iam.serviceAccounts.actAs` permission on custom Cloud Build service accounts. This lets you run builds using custom service accounts while keeping build permissions restricted to that repository.

## Before you begin

  1. [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance).
  2. [Create a Secure Source Manager repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository).
  3. [Configure a Cloud Build user-specified service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts). To let Cloud Build read from your Secure Source Manager repository, grant the Cloud Build service account (either the [default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) or a [user-managed service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts)) the following roles:

     * **Secure Source Manager Instance Accessor** (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance.
     * **Secure Source Manager Repository Reader** on the repository.

Depending on your use case, the Cloud Build service account might need additional roles, for example:

     * To store build logs in Cloud Logging, grant the **Logs Writer** role (`roles/logging.logWriter`) to the Cloud Build service account.
     * To access secrets in Secret Manager, grant the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) role to the Cloud Build service account.

For information about build logs, see [Setting up build logs](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts#set_up_build_logs).

  4. If your builds run in worker pools, grant the repository's user-managed service account the **Cloud Build WorkerPool User** role (`roles/cloudbuild.workerPoolUser`) on the project where the builds run.




### Required roles

To get the permissions that you need to connect a Secure Source Manager repository to Cloud Build, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Repository Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`) on your repository
  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Required service account roles

To connect Secure Source Manager to Cloud Build, you must configure IAM permissions for a per-repository identity.

### Per-repository identity setup

To use a per-repository identity, you must configure permissions.

**Note:** By default, you can only use a user-managed service account that is in the same Google Cloud project as the repository and builds. If your user-managed service account is in a different project (cross-project setup), you must disable the `iam.disableCrossProjectServiceAccountUsage` organization policy constraint in the project where the user-managed service account is located. For more information, see [Cross-project service account setup](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts#cross-project_set_up).

  1. **User** : The user who configures the repository service account needs the **Service Account User** role (`roles/iam.serviceAccountUser`) on the user-managed service account. This permission is checked during repository creation or update.
  2. **Secure Source Manager Service Agent** : Grant the Secure Source Manager Service Agent for the repository project the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`) on the user-managed service account.

The Secure Source Manager Service Agent email has the format `service-REPOSITORY_PROJECT_NUMBER@gcp-sa-sourcemanager.iam.gserviceaccount.com`, where `REPOSITORY_PROJECT_NUMBER` is the project number of the project hosting the repository.

  3. **User-managed service account** :

     * Grant the user-managed service account the **Service Account User** role (`roles/iam.serviceAccountUser`) on the custom Cloud Build service account (in the repository project).
     * Grant the user-managed service account the **Cloud Build Editor** role (`roles/cloudbuild.builds.editor`) and the **Service Usage Consumer** role (`roles/serviceusage.serviceUsageConsumer`) on the project where builds run.



For information about how to grant IAM roles, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#single-role).

## Create a build configuration file

A build configuration file defines the fields that are needed for Cloud Build to perform your build tasks. You can write the build configuration file using the YAML syntax.

You can create build configuration files in the branch or branches that you want to build from.

To create a build configuration file, do the following:

  1. In the Secure Source Manager web interface, select the repository you want to connect to Cloud Build.
  2. Select the branch you want to build from using Cloud Build.
  3. Create a build configuration file. For information about how to create build configuration files, follow the instructions in [create a build configuration file](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).

  4. Commit your changes to the branch.




## Create a triggers file

The triggers configuration file must be created in the **default branch** of your repository.

To create a triggers configuration file:

  1. In your local repository or the Secure Source Manager web interface, switch to the **default branch**.
  2. Create a file named `.cloudbuild/triggers.yaml`.

  3. Configure your trigger in the `.cloudbuild/triggers.yaml` file:
         
         triggers:
         - name: TRIGGER_NAME
           project: PROJECT_ID
           configFilePath: CLOUD_BUILD_CONFIG_PATH
           eventType: EVENT_TYPE
           ignoredGitRefs: IGNORED_GIT_REFS
           includedGitRefs: INCLUDED_GIT_REFS
           serviceAccount: SERVICE_ACCOUNT
           includedFiles: INCLUDED_FILES
           ignoredFiles: IGNORED_FILES
           disabled: DISABLED_BOOL
           substitutions:
             _VARIABLE_NAME: VARIABLE_VALUE
             OVERRIDE_VARIABLE_NAME: OVERRIDE_VARIABLE_VALUE
         

Replace the following:

     * `TRIGGER_NAME` with a name for your trigger. Trigger names can only contain alphanumeric characters and dashes, and can't start or end with a dash. Trigger names must be less than 64 characters long.
     * `PROJECT_ID` with the Google Cloud project ID where you enabled Cloud Build. This field is optional. The default is the Secure Source Manager project.
     * `CLOUD_BUILD_CONFIG_PATH` with the path to the Cloud Build configuration file you want to use for this trigger. This field is optional. The default value is `.cloudbuild/cloudbuild.yaml`
     * `EVENT_TYPE` with the event type you want to trigger the build. Options are as follows:

       * `push` to trigger on push to the specified branch(es)
       * `pull_request` to trigger on a pull request to the specified branch(es)

This field is optional. The default value is `push`.

     * `INCLUDED_GIT_REFS` with an optional [RE2 regular expression format](https://github.com/google/re2/wiki/Syntax) matching the [Git references](https://git-scm.com/book/en/v2/Git-Internals-Git-References) that you want to trigger a build. The default value is empty. An empty value indicates there are no restrictions.

     * `IGNORED_GIT_REFS` with an optional regular expression using the RE2 regular expression format matching the Git references that you don't want to trigger a build. The default value is empty. An empty value indicates there are no restrictions. The `ignoredGitRefs` field is checked before the `includedGitRefs` field. For more information on these fields, see [Triggers file schema](https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema).

     * `SERVICE_ACCOUNT` with the Cloud Build service account to use for the build in the format `projects/PROJECT_ID/serviceAccounts/ACCOUNT`. Replace ACCOUNT with the email address or unique ID of the service account. You can use either the [default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) or a [user-managed service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts). The legacy Cloud Build service account can't be used due to its [limitations](https://docs.cloud.google.com/build/docs/cloud-build-service-account#limitations).

     * `INCLUDED_FILES` with an optional RE2 format regular expression matching files you want to trigger a build.

If any of the changed files don't match the `ignoredFiles` filter field, and the changed files match the `includedFiles` filter field, a build is triggered. The default value is empty. An empty value indicates there are no restrictions.

     * `IGNORED_FILES` with an optional RE2 format regular expression matching files you don't want to trigger a build.

If all changed files in a commit match this filter field, a build isn't triggered. The default value is empty. An empty value indicates there are no restrictions.

     * `DISABLED_BOOL` with `true` to disable the trigger, or `false` to enable the trigger. This field is optional. The default value is `false`.

     * `VARIABLE_NAME` with the name of a variable you want to introduce in your triggers file.

     * `VARIABLE_VALUE` with the value of the variable.

     * `OVERRIDE_VARIABLE_NAME` with the Secure Source Manager default substitution variable name. For information on the available default substitution variables, see the substitutions section of [Triggers file schema](https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema#substitutions).

     * `OVERRIDE_VARIABLE_VALUE` with the value you want to override the default value for the default substitution variable with.

  4. Commit the trigger configuration file to your default branch.

After the triggers file is committed, Secure Source Manager triggers builds based on the configuration in your triggers file.

Secure Source Manager reads the configuration files and associated commit SHA or Git ref of the following types of events:

     * For `push` events, Secure Source Manager will read the commit SHA or Git ref when the push completes.
     * For `pull_request` events, Secure Source Manager will read the commit SHA or Git ref when the pull request changes are pulled from.



## View build status

When a build is triggered by a push or pull request event, the commit and build status is displayed in the Secure Source Manager web interface.

The possible values for build status are as follows:

  * ![success](https://docs.cloud.google.com/secure-source-manager/images/green-check-icon.png)SUCCESS: the build was completed successfully.
  * ![warning](https://docs.cloud.google.com/secure-source-manager/images/warning-icon.png)WARNING: a problem occurred when trying to build.
  * ![failure](https://docs.cloud.google.com/secure-source-manager/images/failed-build-icon.png)FAILURE: the build failed during execution.



You can prevent commits with unsuccessful builds from merging into important branches if you configure a branch protection rule to require a successful status check from triggers configured in your triggers file. To learn more about branch protection, read the [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview).

To view the build status for a push event:

  1. In the Secure Source Manager web interface, navigate to your repository.

If the most recent push event triggered a build, the status is displayed next to the commit SHA. To view details on that status, click the status.

  2. To view build status for previous commits, select **Commits** to view the commit history, and then click the status you want to view details for.




To view the build status for a pull request event:

  1. In the Secure Source Manager web interface, click **Pull requests**.
  2. Click the pull request you want to view.

If builds were triggered by the pull request, you will see a section titled either **All checks were successful** , or **Some checks reported warnings**.




## Troubleshoot

To find methods for diagnosing and resolving Cloud Build errors when connecting with Secure Source Manager, see [Triggers file doesn't trigger build](https://docs.cloud.google.com/secure-source-manager/docs/troubleshoot#triggers-file-not-triggering).

## What's next

  * Learn how to [view build results in Cloud Build](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
