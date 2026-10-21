---
url: https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema/
title: Triggers file schema \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:11.563817+00:00
---

# Triggers file schema  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Triggers file schema Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the schema of the Secure Source Manager triggers file. For instructions on creating a triggers file, see [Create a triggers file](https://docs.cloud.google.com/secure-source-manager/docs/create-triggers-file).

A triggers file contains instructions for Secure Source Manager to trigger the steps defined in a Cloud Build config file based on a push or pull request event in Secure Source Manager.

You can configure your branch protection rules to require a successful status check from specific triggers. To learn more about branch protection, read the [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview).

## Structure of a triggers file

The triggers configuration file must be created in the default branch of your repository. You can write the triggers file using YAML syntax.

A triggers file has the following structure:
    
    
    triggers:
    - name: string
      project: string
      configFilePath: string
      eventType: string
      includedGitRefs: string
      ignoredGitRefs: string
      includedFiles: string
      ignoredFiles: string
      serviceAccount: string
      disabled: bool
      substitutions: map[string]string
    - name: string
    ...
    
    

Each named section of the triggers file defines the Cloud Build configuration to use for the given event type in Secure Source Manager.

## Triggers

A trigger specifies what Secure Source Manager event type you want to use to trigger the completion of the steps in a specific Cloud Build config file. You can also specify which branches are monitored for the specified event.

Use the `name` field in the triggers file to identify a trigger. Here's an example of the kind of configuration you might set in the triggers file:
    
    
    triggers:
    - name: presubmit-test
      project: my-project
      configFilePath: test.yaml
      eventType: pull_request
      includedGitRefs: ^main$
      ignoredGitRefs: .*log
      serviceAccount: projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
      includedFiles: .*
      ignoredFiles: my-file.txt
      disabled: false
    - name: postsubmit-run
      project: my-project
      configFilePath: run.yaml
      eventType: push
      includedGitRefs: ^main$
      ignoredGitRefs: dev-branch
      serviceAccount: projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
      disabled: false
      substitutions:
        _NODE_VERSION_1: v6.9.1
        REPO_NAME: dev
    

### `name`

Required. Use the `name` field of the trigger to identify your trigger. Trigger names can only contain alphanumeric characters and dashes, and can't start or end with a dash. Trigger names must be less than 64 characters long.

### `project`

Optional. Use the `project` field to identify the Google Cloud project where you enabled Cloud Build.

The default is the Secure Source Manager project.

### `configFilePath`

Optional. Path to the Cloud Build configuration file.

The default is `.cloudbuild/cloudbuild.yaml`.

### `eventType`

Optional. The event type to trigger on. Options are `push` for pushes to the selected branches or `pull_request` for pull requests to the selected branches.

The default is `push`.

### `includedGitRefs`

Optional. A [RE2 format regular expression](https://github.com/google/re2/wiki/Syntax) matching the [Git references](https://git-scm.com/book/en/v2/Git-Internals-Git-References) that trigger a build.

The default is empty. An empty `includedGitRefs` filter field indicates that there are no restrictions.

If the Git reference isn't included in the `ignoredGitRefs` filter field, Secure Source Manager checks the `includedGitRefs` filter field. If the Git reference is in the `includedGitRefs` filter field, a build is triggered. If the `includedGitRefs` filter field isn't empty, and the Git reference isn't included in the `includedGitRefs` filter field, a build isn't triggered.

### `ignoredGitRefs`

Optional. A RE2 format regular expression matching Git references that shouldn't trigger a build.

The default is empty. An empty `ignoredGitRefs` filter field indicates that there are no restrictions.

Secure Source Manager checks the `ignoredGitRefs` filter field first. If it's not empty and the Git reference matches the `ignoredGitRefs` filter field, a build isn't triggered.

### `serviceAccount`

Required. The [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) to use for the build.

Format: `projects/PROJECT_ID/serviceAccounts/ACCOUNT`

Replace the following:

  * `PROJECT_ID`: with the Google Cloud project ID where you created the service account.
  * `ACCOUNT`: with the email address or unique ID of the service account.



### `includedFiles`

Optional. A RE2 format regular expression matching files that should trigger a build when changed.

If the changed files are not in the `ignoredFiles` filter field, and the changed files match the `includedFiles` filter field, a build is triggered.

The default is empty. An empty filter field indicates that there are no restrictions.

### `ignoredFiles`

Optional. A RE2 format regular expression matching files that shouldn't trigger a build when changed.

If the `ignoredFiles` filter field isn't empty, commits that only include files that match the `ignoredFiles` filter field won't trigger a build. The default is empty. An empty filter indicates that there are no restrictions.

### `disabled`

Optional. A boolean to set if the trigger is disabled or not. Values are `true` or `false`.

The default is `false`.

### `substitutions`

Use substitutions in your triggers file to substitute specific variables at build time in your Cloud Build config file.

Substitutions must begin with an underscore, and can only contain uppercase-letters, underscores and numbers, or be one of the Secure Source Manager substitution variables.

Secure Source Manager provides the following default substitution variables:

  * `TRIGGER_NAME`: the name associated with the trigger.
  * `COMMIT_SHA`: the commit ID associated with the trigger.
  * `REVISION_ID`: the commit ID associated with the trigger.
  * `SHORT_SHA`: the first seven characters of `COMMIT_SHA`.
  * `REPO_NAME`: the name of the repository. For example: `my-repo`.
  * `REPO_FULL_NAME`: the resource path of the repository, for example: `projects/my-project/locations/us-central/repositories/test-repo`.
  * `REF_NAME`: the name of the branch or tag associated with the trigger.
  * `TRIGGER_BUILD_CONFIG_PATH`: the path to the build configuration file used during your build execution.



For information on how to include Secure Source Manager substitution variables in your Cloud Build configuration file, see [Substituting variable values](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values).

## What's next

  * [Create a triggers file](https://docs.cloud.google.com/secure-source-manager/docs/create-triggers-file)
  * Learn more about Cloud Build configuration files by reading [Build configuration file schema](https://docs.cloud.google.com/build/docs/build-config-file-schema)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
