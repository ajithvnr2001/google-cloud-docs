---
url: https://docs.cloud.google.com/deploy/docs/create-pipeline-targets/
title: Create your delivery pipeline and targets \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:43.887430+00:00
---

# Create your delivery pipeline and targets  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/create-pipeline-targets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Create your delivery pipeline and targets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create the delivery pipeline and targets that describe where and how Cloud Deploy will deploy your application. See [Configuration file schema](https://docs.cloud.google.com/deploy/docs/config-files) for a description of the YAML file structure for delivery pipelines and targets.

## About the delivery pipeline and targets

Your delivery pipeline describes a [progression](https://docs.cloud.google.com/deploy/docs/terminology#progression) of deployment [targets](https://docs.cloud.google.com/deploy/docs/terminology#target). You can define those targets in the same file as the delivery pipeline or in one or more separate files.

After you create the delivery pipeline and target definition file or files, you run `gcloud deploy apply` against each of those files to register them as Cloud Deploy resources.

## Define the delivery pipeline and targets

The structure of the delivery pipeline and target configuration files is described [here](https://docs.cloud.google.com/deploy/docs/config-files).

You can call this file anything you want. By convention, a delivery pipeline config that _includes_ [target](https://docs.cloud.google.com/deploy/docs/terminology#target) definitions is called `clouddeploy.yaml`, and one that instead references targets defined in one or more separate files is named `delivery-pipeline.yaml`.

The target can point to [GKE](https://docs.cloud.google.com/deploy/docs/config-files#for_gke_targets), [GKE attached clusters](https://docs.cloud.google.com/deploy/docs/config-files#for_anthos_targets), [Cloud Run](https://docs.cloud.google.com/deploy/docs/config-files#for_run_targets), or [custom targets](https://docs.cloud.google.com/deploy/docs/deploy-to-custom-targets). Within a delivery pipeline, all targets must reference the same runtime type (all GKE, or all Cloud Run, for example).

## Create a delivery pipeline and targets using the Google Cloud console

You can use the Google Cloud console to create a new delivery pipeline and target or targets. This is useful for trying out Cloud Deploy, but is not suitable for production workloads. (You can also use the Google Cloud console to [create a release](https://docs.cloud.google.com/deploy/docs/deploying-application#create_pipeline_in_ui).)

To create the delivery pipeline:

  1. From the **Delivery pipelines** page, click **Create**.

  2. Provide a name (or keep the default) and, optionally, a description.

  3. Select your region.

  4. Choose your runtime environment.

For GKE, choose **Google Kubernetes Engine** , or select **Cloud Run** if that's the runtime you're deploying to.

  5. Under **New target** , provide a name (or keep the default).

  6. If you want to require [approval](https://docs.cloud.google.com/deploy/docs/promote-release#manage_approvals_for_a_delivery_pipeline) on this target, select the **Require approval for rollouts** checkbox.

  7. If you're going to use a [canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary) on this target, select the **Enable canary** checkbox.

**Note:** You can enable canary here for Cloud Run only. For GKE, you need to configure it as described in [Canary deployments](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary).
  8. Click **Done**.

  9. Click **Add target** and follow these steps for each additional target you want to create.

  10. When you have all your targets, click **Create** to create the delivery pipeline and target resources.




## Register the delivery pipeline and targets

**If you created your pipeline and targets using the Google Cloud console, you don't need to do this.**

To register your delivery pipeline with Cloud Deploy, you run `gcloud deploy apply` once for each separate definition file. That is, if you define three targets in three files, you would run the command four times—once for the delivery pipeline, and once for each target.

The following command registers a delivery pipeline with its targets defined in the same file.
    
    
    gcloud deploy apply --file=PIPELINE_CONFIG \
                        --region=LOCATION \
                        --project=PROJECT
    

You now have a delivery pipeline that can manage deployment of your releases, and target resources that can be used by any delivery pipeline in the same project and region.

### A single-file example

The command in this example registers a delivery pipeline and targets that are all defined in the same file:
    
    
    gcloud deploy apply --file=clouddeploy.yaml --region=us-central1
    

### An example using separate files

For this example, there are three targets defined in three separate files, so you run four commands:
    
    
    gcloud deploy apply --file=delivery-pipeline.yaml --region=us-central1 && \
    gcloud deploy apply --file=target_dev.yaml --region=us-central1 && \
    gcloud deploy apply --file=target_staging.yaml --region=us-central1 && \
    gcloud deploy apply --file=target_prod.yaml --region=us-central1
    

The `--region` flag is required unless you've set a default (using `gcloud config set deploy/region [REGION]`). The region must be the same for the delivery pipeline and all targets that pipeline references.

## Create the delivery pipeline and targets using Terraform

You can also use the [Google Cloud Terraform provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) to create [delivery pipeline](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/clouddeploy_delivery_pipeline) and [target](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/clouddeploy_target) resources.

The [Google Cloud beta Terraform provider](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs) may include support for Cloud Deploy features in [Preview](https://cloud.google.com/products#product-launch-stages).

## Edit existing pipelines and targets

You can later edit any delivery pipeline or target config and run `gcloud deploy apply` to update the pipeline or target resource. But those changes [do not affect any existing releases, as they are managed by the original delivery pipeline](https://docs.cloud.google.com/deploy/docs/pipeline-instances).

## Require manual approval for a deployment

To require manual approval for a given target, include the following property on the [target definition](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions):

`requireApproval: true`

The default is `false`. If you omit this property from the delivery-pipeline config, or provide no value for it, deploying to this target doesn't require approval. (But the caller trying to promote to the target still needs the `clouddeploy.rollouts.create` IAM permission.)

You can even require manual approval on the first target. When a release is created, using the CLI, for the first target, the `rollout` is created automatically. If approval is required, Cloud Deploy creates the `rollout`, but in a pending-release state until approval is given.

## What's next

  * [Create your Skaffold configuration](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold).

  * See [Deploying your application](https://docs.cloud.google.com/deploy/docs/deploying-application) to find out how to invoke your delivery pipeline and create a release.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
