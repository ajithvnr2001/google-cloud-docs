---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/automate-builds-on-events/
title: Automate builds on repository events \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:03:05.893709+00:00
---

# Automate builds on repository events  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/automate-builds-on-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Automate builds on repository events Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

You can configure automated Image Builder pipelines that run whenever you push configuration changes to your Git repository such as pushing to `main`. Automating builds on repository events ensures that Cloud Build immediately validates, builds, and publishes your custom OS images to Compute Engine and Artifact Registry upon code review or merge.

## Before you begin

  * Complete the environment setup steps in [Prepare your environment](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites). 
  * If you intend to deploy your pipeline by using Terraform or automate builds from a repository, connect your GitHub, GitLab, or Bitbucket repository by using [Cloud Build repositories (`2nd gen`) or Developer Connect connection links](https://docs.cloud.google.com/build/docs/repositories). 
  * Ensure your repository contains your [`cloudbuild.yaml` orchestration file](https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema), your [`imagebuilder.yaml` recipe file](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema), and any referenced build scripts. 
  * If you plan to use Terraform, install the [Terraform CLI](https://developer.hashicorp.com/terraform/downloads) version 1.3 or later. 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 




## Required roles

To get the permissions that you need to create repository event triggers, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure repository automation

You can configure repository event triggers by using either the gcloud CLI or Terraform. Select one of the following tabs to configure repository triggers:

###  gcloud 

You can create an automated repository trigger by using the [`gcloud builds triggers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/create) and pointing directly to your connected 2nd-gen repository link (`--repository`).
    
    
    gcloud builds triggers create repository \
        --name="TRIGGER_NAME" \
        --repository="projects/PROJECT_ID/locations/REGION/connections/CONNECTION_NAME/repositories/REPO_NAME" \
        --branch-pattern="^main$" \
        --build-config="CLOUDBUILD_YAML_PATH" \
        --service-account="projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL" \
        --substitutions="_GCS_WORKDIR=gs://STAGING_BUCKET/workdir/,_IMAGE_BUILDER_CONFIG_PATH=RECIPE_PATH,_SERVICE_ACCOUNT=projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL,_IMAGE_OUTPUT_PATH=image-builder/binaryOut" \
        --region=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `TRIGGER_NAME`: the name for your trigger, for example, `git-push-custom-os-builder`.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your repository connection is hosted and where the image customization pipeline job runs, for example, `us-central1`.
  * `CONNECTION_NAME`: the name of your Developer Connect connection, for example, `github-connection`.
  * `REPO_NAME`: the linked Git repository name.
  * `CLOUDBUILD_YAML_PATH`: the relative path to `cloudbuild.yaml` in your local directory.
  * `SERVICE_ACCOUNT_EMAIL`: the exact email address of your build service account.
  * `STAGING_BUCKET`: your Cloud Storage staging `workdir` bucket name.
  * `RECIPE_PATH`: the relative path to `imagebuilder.yaml` in your repository.



###  Terraform 

To configure an automated repository trigger by using Terraform, complete the following steps:

  1. Add the trigger resource to your [`main.tf`](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline#main-tf) configuration file:
         
         resource "google_cloudbuild_trigger" "repository_trigger" {
           name        = "TRIGGER_NAME"
           location    = "REGION"
           project     = "PROJECT_ID"
           description = "Triggers custom OS image builds on repository push events"
         
           repository_event_config {
             repository = "projects/PROJECT_ID/locations/REGION/connections/CONNECTION_NAME/repositories/REPO_NAME"
             push {
               branch = "^main$"
             }
           }
         
           filename = "CLOUDBUILD_YAML_PATH"
         
           substitutions = {
             _GCS_WORKDIR               = "gs://STAGING_BUCKET/workdir/"
             _IMAGE_BUILDER_CONFIG_PATH = "RECIPE_PATH"
             _SERVICE_ACCOUNT           = "projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL"
           }
         }
         

Replace the following:

     * `TRIGGER_NAME`: the name for your trigger, for example, `git-push-custom-os-builder`.
     * `PROJECT_ID`: your project ID.
     * `REGION`: the Google Cloud region where your repository connection is hosted, for example, `us-central1`.
     * `CONNECTION_NAME`: the name of your Developer Connect connection, for example, `github-connection`.
     * `REPO_NAME`: the linked Git repository name.
     * `CLOUDBUILD_YAML_PATH`: the relative path to `cloudbuild.yaml` in your local directory.
     * `STAGING_BUCKET`: your Cloud Storage staging bucket name.
     * `RECIPE_PATH`: the relative path to `imagebuilder.yaml` in your repository.
     * `SERVICE_ACCOUNT_EMAIL`: the email address of your build service account.
  2. Deploy the updated Terraform configuration:
         
         terraform plan
         terraform apply
         

To review the complete multi-file Terraform infrastructure project structure, see [Create and manage pipelines using Terraform](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline#create-config-files).




## What's next

  * Learn how to [Schedule custom OS image builds](https://docs.cloud.google.com/compute/docs/images/image-builder/schedule-builds) periodically for security patching by using Cloud Scheduler.
  * Explore [Supported customization actions](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions) (`Shell`, `FileCopy`, `UpdateKernelCommandLine`, `InstallGPU`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
