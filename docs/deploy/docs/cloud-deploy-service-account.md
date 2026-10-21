---
url: https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account/
title: Cloud Deploy service accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:50.883113+00:00
---

# Cloud Deploy service accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Cloud Deploy service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes service accounts that are used to run Cloud Deploy and to call Cloud Deploy to run various operations.

Cloud Deploy uses the following service accounts:

  * The Cloud Deploy [service agent](https://docs.cloud.google.com/iam/docs/service-agents)

Cloud Deploy uses this service account to interact with your project. You can't replace this service agent with an alternate service account, but you can edit permissions on it, for example when you're using resources outside of the project (such as a service account or a private Cloud Build worker pool).

  * The Cloud Deploy execution service account

Cloud Deploy uses this service account to execute render and deploy operations in Cloud Build. This account needs permissions sufficient to read from and write to the Cloud Storage bucket and to access deployment targets.

The default service account for execution is the [default Compute Engine service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#default_service_account). You can specify an alternate service account in the [target configuration](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions).

  * The Cloud Deploy automation service account

This is the service account Cloud Deploy uses to perform [automations](https://docs.cloud.google.com/deploy/docs/automation). This can be the default execution service account or another service account. See [The automation service account](https://docs.cloud.google.com/deploy/docs/automation-resource#automation_service_account) For more information about this service account.




See [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) for instructions on how to edit service-account permissions and how to create an alternate service account.

## Cloud Deploy service agent

The Cloud Deploy service agent is a service account that Cloud Deploy uses to interact with other Google Cloud services that Cloud Deploy relies on. These services include Cloud Build, Pub/Sub, and Cloud Audit Logs.

The name of this service account follows this pattern:

`service-<project-number>@gcp-sa-clouddeploy.iam.gserviceaccount.com`

If this account is removed from your project, you can re-add it:

  1. Open the **IAM** page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select **Include Google-provided role grants** to display the service agent.

If the service agent is displayed, you can skip the rest of these steps.

  3. If the service agent isn't displayed, click **Grant access**.

  4. In the **New principals** field, enter the service agent address, in the following format:

     1. `service-<project-number>@gcp-sa-clouddeploy.iam.gserviceaccount.com`
  5. Click the **Select a role** drop-down list, and select **Cloud Deploy Service Agent**.

  6. Click **Save**.




## Cloud Deploy execution service account

By default, Cloud Deploy runs using the [default Compute Engine service account](https://docs.cloud.google.com/iam/docs/service-account-types#default).

The name of this service account follows this pattern:

`[project-number]-compute@developer.gserviceaccount.com`

Because this service account is used by many products, it may have broad permissions. The best practice is to change your [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment) so that Cloud Deploy runs as a different service account. You can change the execution service account for each [target](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions) using the `executionConfigs.privatePool.serviceAccount` property or the `executionConfigs.defaultPool.serviceAccount` property in the [target definition](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions).

Any service account you set for these properties must have the [Cloud Deploy Runner](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#clouddeploy.jobRunner) role in the Cloud Deploy project. If the default execution service account doesn't have this role, run the following command:
    
    
     gcloud projects add-iam-policy-binding PROJECT_ID \
         --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
         --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
         --role="roles/clouddeploy.jobRunner"
    

The service account will also need runtime-specific permissions to deploy to your chosen runtime. For Google Kubernetes Engine, you might choose the [Container Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) and [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) roles. For Cloud Run, you might choose the [Cloud Run Developer](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.developer) and [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) roles. Other runtimes used by [Custom Targets](https://docs.cloud.google.com/deploy/docs/custom-targets) may require their own permissions.

### What service accounts to create

If you choose not to use the default execution service account for rendering and deploying, you need to create one or more alternate service accounts to use. These are service accounts that Cloud Deploy runs as, and they're [configured in the target configuration](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions).

One reason to create more than one would be to have a specific service account or accounts for deploying to restricted targets, like a production target.

One possible approach is to use separate service accounts per delivery pipeline. Each such service account would include roles with sufficient permissions to render and to deploy.

For deployments to Google Kubernetes Engine, you can [restrict the service account to one namespace](https://docs.cloud.google.com/deploy/docs/securing/sa-by-namespace).

### Using service accounts from a different project

For your [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment), you can specify a service account that's in a different project from the one in which you create your target:

  1. On the project that owns the service account, [enable the cross-project SA organization policy](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

  2. Grant the Cloud Deploy service agent (`service-<project-number>@gcp-sa-clouddeploy.iam.gserviceaccount.com`) the `iam.serviceAccounts.actAs` permission for your service account.

In this case, `project-number` is the project in which you created your target.

You can also grant the [`roles/iam.serviceAccountUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role, which includes that permission, in the project of and on each service account that's in a different project from the one where Cloud Deploy is running.

  3. Grant the Cloud Build service agent (`service-<project-number>@gcp-sa-cloudbuild.iam.gserviceaccount.com`) the `roles/iam.serviceAccountTokenCreator` role.

In this case, `project-number` is the project in which you created your target, and this role is granted in the service account's project.

You must grant this role for each service account configured in a target's execution environment if that service account is in a different project from the one where Cloud Deploy is running.

  4. Grant the caller of `gcloud deploy releases create` and `gcloud deploy rollouts create` `iam.serviceAccounts.actAs` permission on the service account, or the [`roles/iam.serviceAccountUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role.




### Required permissions

  * The service account used for rendering configurations must have sufficient permissions to access the Cloud Storage bucket where your Cloud Deploy resources are stored (delivery pipelines, releases, rollouts).

The role `roles/clouddeploy.jobRunner` includes all permissions the render service account ([`privatePool` or `defaultPool`](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions)) needs.

  * The service account used for deploying must have sufficient permissions to deploy to the target cluster, _and_ permission to access the Cloud Storage bucket.

**Note:** If you use a custom Cloud Storage bucket, you can put it anywhere. (It doesn't need to be in the same region, for example, as the delivery pipeline.)
  * The service account that calls Cloud Deploy to create a release must have the `clouddeploy.releaser` role. It must also have the `iam.serviceAccount.actAs` permission to use the service account that renders manifests (for example through the [`roles/iam.serviceAccountUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role).

  * The service account that calls Cloud Deploy to promote a release or create a `rollout` must have the `iam.serviceAccount.actAs` permission to use the service account that deploys to targets (for example through the [`roles/iam.serviceAccountUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role).

  * The service account configured for an [automation](https://docs.cloud.google.com/deploy/docs/automation) must have permission to run the operations that are being automated. [Learn more](https://docs.cloud.google.com/deploy/docs/automation-resource#automation_service_account).




## The automation service account

You can automate some actions in a release. Cloud Deploy runs these automations using the automation service account, which can be the default execution service account, a non-default service account used as the execution service account, or another service account.

[Learn more](https://docs.cloud.google.com/deploy/docs/automation-resource#automation_service_account) about the automation service account.

## What's next

  * Learn about [IAM](https://docs.cloud.google.com/iam/docs).
  * Find out about [predefined Cloud Deploy roles](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#predefined_roles).
  * Understand how to [Create and manage service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
