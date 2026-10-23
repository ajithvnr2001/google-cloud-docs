---
url: https://docs.cloud.google.com/secure-source-manager/docs/create-triggers-file/
title: Create a triggers file \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:35.029225+00:00
---

# Create a triggers file  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/create-triggers-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Create a triggers file Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to create a triggers YAML file in Secure Source Manager. A triggers file can be used to automate builds based on push and pull request events in a Secure Source Manager repository.

To learn about the fields you can include in a triggers file, read [Triggers file schema](https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema).

## Before you begin

  1. [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance).
  2. [Create a Secure Source Manager repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository).
  3. Read the [Triggers file schema](https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema) to learn about the fields you can include in a triggers file.



### Required roles

To get the permissions that you need to create a triggers file, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the instance
  * [Secure Source Manager Repository Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`) on the repository



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud Build configuration file

Secure Source Manager triggers files require that you specify a build configuration file for each trigger.

A build config file contains instructions for Cloud Build to perform tasks based on your specifications. For example, your build config file can contain instructions to build, package, and push Docker images.

Create your build configuration files in the branch or branches where you want to build from. To create your build configuration files, follow the instructions in [Create a build configuration file](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).

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




## What's next

  * Use a triggers file to [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
