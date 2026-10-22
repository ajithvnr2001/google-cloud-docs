---
url: https://docs.cloud.google.com/deploy/docs/create-custom-target/
title: Create a custom target \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:00.050201+00:00
---

# Create a custom target  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/create-custom-target/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Create a custom target Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a custom Cloud Deploy target type and use that custom target type as a [target](https://docs.cloud.google.com/deploy/docs/terminology#target) in a Cloud Deploy [delivery pipeline](https://docs.cloud.google.com/deploy/docs/terminology#delivery_pipeline).

The following is the high-level process for creating a custom target type and using it in your delivery pipeline:

  1. Create a containerized application or applications that include the functionality to deploy to your custom target, and that fulfill the Cloud Deploy [requirements](https://docs.cloud.google.com/deploy/docs/custom-targets#required_inputs_and_outputs) for custom target types.

  2. Create a `CustomTargetType` definition with [tasks](https://docs.cloud.google.com/deploy/docs/tasks) that reference the container and specify the command or commands to run on it.

  3. Define a new target with a `customTarget` property that identifies your new custom target type.

  4. Reference that target from your delivery pipeline [progression](https://docs.cloud.google.com/deploy/docs/terminology#progression).

  5. Create a release.




Each of these steps is described in detail in the rest of this document.

## Create your containerized applications

The functionality to deploy to your custom target is defined in containerized applications, which you provide to Cloud Deploy in your `CustomTargetType` definition. When your delivery pipeline includes a target that uses a custom target type, Cloud Deploy calls the containers defined for that custom target type to execute the custom render and deploy you've defined.

The behavior of your applications is up to you. However, it must consume the input environment variables provided by Cloud Deploy, and it must return the [required outputs](https://docs.cloud.google.com/deploy/docs/custom-targets#required_inputs_and_outputs).

In most cases, you will create one container for your custom render and one for your custom deploy, for each custom target type you create. The custom render is optional, but you must create one unless your custom target will work correctly if rendered with the built-in renderers. Cloud Deploy uses [`skaffold render`](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) by default to render your manifests.

## Define your custom target type

You define a custom target by first creating a custom target _type_ , using the [`CustomTargetType` configuration](https://docs.cloud.google.com/deploy/docs/config-files#custom_target_type_definitions). You can create the `CustomTargetType` in the same file as your delivery pipeline definition, or with target definitions, or in a separate file.

The `CustomTargetType` definition is as follows:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: CustomTargetType
    metadata:
      name: [CUSTOM_TARGET_TYPE_NAME]
      annotations:
      labels:
    description:
    tasks:
      render: [RENDER_TASK]
      deploy: [DEPLOY_TASK]
    

Where

  * `CUSTOM_TARGET_TYPE_NAME`

Is an arbitrary name you give to this custom target type definition. This name is referenced in the [target definition](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions) for any target that uses the custom target type you're defining.

  * `RENDER_TASK`

Is the [task](https://docs.cloud.google.com/deploy/docs/tasks) that defines your [custom render](https://docs.cloud.google.com/deploy/docs/custom-targets#required_inputs_and_outputs). If not provided, Cloud Deploy uses the built-in renderer specified in your [Skaffold configuration](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests).

  * `DEPLOY_TASK`

Is the [task](https://docs.cloud.google.com/deploy/docs/tasks) that defines your [custom deploy](https://docs.cloud.google.com/deploy/docs/custom-targets#required_inputs_and_outputs).




### Register your custom target type

After you've configured the `CustomTargetType`, run the [`gcloud deploy apply`](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/apply) command to register the `CustomTargetType` resource in a Google Cloud project:
    
    
    gcloud deploy apply --file=[FILE] --project=[PROJECT] --region=[REGION]
    

Where:

`FILE` is the name of the file in which you've defined this custom target type.

`PROJECT` is the Google Cloud project in which to create this resource. The `CustomTargetType` must be in the same project as the `Target` resource that references it. You don't need to specify the project if you have set it as your default project for the Google Cloud CLI.

`REGION` is the region (for example, `us-central1`) in which to create this resource. The `CustomTargetType` must be in the same region as the `Target` resource that references it. You don't need to specify the region if you have set it as your default region for the gcloud CLI.

With the `CustomTargetType` now created as a Cloud Deploy resource, you can now use it in a `Target` definition to create your custom target.

For more information on the `CustomTargetType` definition, see the [Cloud Deploy configuration schema reference](https://docs.cloud.google.com/deploy/docs/config-files#custom_target_type_definitions).

## Define your target

The only difference between a target definition for a supported target type and a custom target definition is that the custom target definition includes a `customTarget` stanza. The syntax for a `customTarget` is as follows:
    
    
    customTarget:
      customTargetType: [CUSTOM_TARGET_TYPE_NAME]
    

Where `CUSTOM_TARGET_TYPE_NAME` is the value from the `name` property defined in your custom target type configuration.

**Note:** You can use [multi-targets](https://docs.cloud.google.com/deploy/docs/parallel) where the child targets are custom targets. In this case, all child targets must be of the same `CustomTargetType`.

## Add your target to the delivery pipeline

You can use a custom target in a delivery pipeline exactly as you would use a supported target type. That is, there is no difference in the delivery pipeline progression between targets of a supported target type and custom targets.

All targets in a delivery pipeline must use the same target type. For example, you can't have a delivery pipeline with some targets deploying to Google Kubernetes Engine and some custom targets.

As with supported target types, you can include [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) in the pipeline stage.

## Create a release

With your custom target type fully defined, and a target created to use that type, you can now create a release, in the normal way:
    
    
    gcloud deploy releases create [RELEASE_NAME] \
      --project=[PROJECT_NAME] \
      --region=[REGION] \
      --delivery-pipeline=[PIPELINE_NAME]
    

Upon release creation your custom render is executed for each target in your delivery pipeline, including processing [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) configured on the release, targets, or the delivery pipeline. Cloud Deploy provides the [deploy parameters as input](https://docs.cloud.google.com/deploy/docs/custom-targets#custom_targets_and_deploy_parameters) to the custom render container.

## View the output of your custom targets

If your custom render task satisfies the [requirements](https://docs.cloud.google.com/deploy/docs/custom-targets#required_inputs_and_outputs) for custom targets, you can use Google Cloud console to view the rendered artifacts.

Follow these steps to view the output of your custom render task.

  1. In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view your delivery pipeline.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click the name of your delivery pipeline.

The pipeline visualization shows the app's deployment status, and your release is listed on the **Releases** tab under **Delivery pipeline details**.

  3. Click the release name.

The **Release details** page is shown.

  4. Click the **Artifacts** tab.

  5. Under **Target artifacts** , click the arrow next to **View artifacts**.

The rendered artifacts are listed, including the rendered [Skaffold](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) configuration file and rendered manifest file generated by the custom renderer. And you can click the **Storage location** link next to each one to go to the Cloud Storage bucket to view those files.

You can also click the **View artifacts** link to view those files by release, by target, or by phase, using the [release inspector](https://docs.cloud.google.com/deploy/docs/view-release#view_release_artifacts).




## What's next

  * Try the [quickstart: Define and use a custom target type](https://docs.cloud.google.com/deploy/docs/deploy-app-custom-target)

  * See the available [sample custom target types](https://docs.cloud.google.com/deploy/docs/custom-targets#custom_target_examples).

  * Learn more about [Tasks](https://docs.cloud.google.com/deploy/docs/tasks)

  * [Create a delivery pipeline and targets](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets).

  * Learn more about [configuring Cloud Deploy targets](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
