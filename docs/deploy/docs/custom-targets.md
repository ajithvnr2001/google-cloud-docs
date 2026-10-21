---
url: https://docs.cloud.google.com/deploy/docs/custom-targets/
title: About custom targets \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:47.152075+00:00
---

# About custom targets  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/custom-targets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  About custom targets Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how custom targets work in Cloud Deploy.

Cloud Deploy includes built-in support for various runtime environments as [targets](https://docs.cloud.google.com/deploy/docs/terminology#target). But the list of supported target types is finite. With custom targets, you can deploy to other systems besides the supported runtimes.

A custom target is a target that represents an arbitrary output environment other than a runtime that Cloud Deploy supports.

The page [Create a custom target](https://docs.cloud.google.com/deploy/docs/create-custom-target) describes the process of defining a custom target type and implementing it as a target in a delivery pipeline.

### What goes into a custom target?

Each custom target consists of the following components:

  * [Tasks](https://docs.cloud.google.com/deploy/docs/tasks), that define how to render and deploy for your custom target type

Your implementations of the custom render and custom deploy consume values provided by Cloud Deploy and must fulfill a set of required outputs.

The custom render is optional, but you must create one unless your custom target will work correctly if rendered with the [Cloud Deploy built-in renderers](https://docs.cloud.google.com/deploy/docs/release-configuration-file#render).

  * A [custom target type definition](https://docs.cloud.google.com/deploy/docs/create-custom-target#define_custom_target_type)

The `CustomTargetType` is a Cloud Deploy resource that identifies the tasks that targets of this type use for release render and rollout deploy activities.

  * A [target definition](https://docs.cloud.google.com/deploy/docs/create-custom-target#define_target)

The target definition for a custom target is the same as for any target type, except that it includes the `customTarget` property, whose value is the name of the `CustomTargetType`.




With those components in place, you can use the target as you would any target, referencing it from your delivery pipeline progression, and making full use of Cloud Deploy features, such as [promotion and approvals](https://docs.cloud.google.com/deploy/docs/promote-release), and [rollbacks](https://docs.cloud.google.com/deploy/docs/roll-back).

### An example

The quickstart [Define and use a custom target type](https://docs.cloud.google.com/deploy/docs/deploy-app-custom-target) creates a custom target type that includes commands to run on a container image—one command for render and one for deploy. The commands, in this case, just add text to the required output files for render and deploy.

For more examples, see Custom target examples.

## Required inputs and outputs

Any custom target type defined for Cloud Deploy must satisfy requirements for input and output, for both render and deploy. This section lists what inputs and outputs are required, and how they're provided.

Cloud Deploy provides the required inputs, for both render and deploy, as environment variables. The following sections list these inputs, as well as the outputs that your custom render and deploy must return.

### Deploy parameters as environment variables

In addition to the environment variables listed in this section, Cloud Deploy can pass to your custom containers any [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) you've set.

[Learn more](https://docs.cloud.google.com/deploy/docs/parameters#deploy_parameters_with_custom_targets).

### Inputs to custom renders

For custom renders, Cloud Deploy provides the following inputs, as environment variables. For multi-phase rollouts ([canary deployments](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary)), Cloud Deploy provides these variables for each phase.

  * `CLOUD_DEPLOY_PROJECT`

The Google Cloud project number for the project in which the custom target is created.

  * `CLOUD_DEPLOY_PROJECT_ID`

The Google Cloud project ID for the project.

  * `CLOUD_DEPLOY_LOCATION`

The Google Cloud region for the custom target type.

  * `CLOUD_DEPLOY_DELIVERY_PIPELINE`

The name of the Cloud Deploy delivery pipeline referencing the custom target type.

  * `CLOUD_DEPLOY_RELEASE`

The name of the release for which the render operation is invoked.

  * `CLOUD_DEPLOY_TARGET`

The name of the Cloud Deploy target that uses the custom target type.

  * `CLOUD_DEPLOY_PHASE`

The [rollout phase](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#phases) to which the render corresponds.

  * `CLOUD_DEPLOY_REQUEST_TYPE`

For the custom render, this is always `RENDER`.

  * `CLOUD_DEPLOY_FEATURES`

A comma-separated list of Cloud Deploy features which the custom container must support. This variable is populated based on features configured in your delivery pipeline.

If your implementation doesn't support the features in this list, we recommend that it fail during rendering.

For [standard deployments](https://docs.cloud.google.com/deploy/docs/deployment-strategies#what_deployment_strategies_does_support), this is empty. For canary deployments, the value is `CANARY`. If the value provided by Cloud Deploy is `CANARY`, your render is invoked for each phase in the canary. The canary percentage for each phase is provided in the `CLOUD_DEPLOY_PERCENTAGE_DEPLOY` environment variable.

  * `CLOUD_DEPLOY_PERCENTAGE_DEPLOY`

The percentage of deployment associated with this render operation. If the `CLOUD_DEPLOY_FEATURES` environment variable is set to `CANARY`, your custom render is called for each phase, and this variable is set to the canary percentage for each phase. For [standard deployments](https://docs.cloud.google.com/deploy/docs/deployment-strategies#what_deployment_strategies_does_support) and for canary deployments that have reached the `stable` phase, this is `100`.

  * `CLOUD_DEPLOY_STORAGE_TYPE`

The storage provider. Always `GCS`.

  * `CLOUD_DEPLOY_INPUT_GCS_PATH`

The Cloud Storage path for the render-file archive written when the release was created.

  * `CLOUD_DEPLOY_OUTPUT_GCS_PATH`

The Cloud Storage path where the custom render container is expected to upload artifacts to be used for deployment. Note that the render must upload a file named `results.json` containing the results of this render operation. For more information, see Outputs from custom render.




### Outputs from custom render

Your custom render must provide the information described in this section. The information must be included in the results file, named `results.json`, located in the Cloud Storage bucket provided by Cloud Deploy (`CLOUD_DEPLOY_OUTPUT_GCS_PATH`).

  * Rendered configuration file or files

  * A `results.json` file, containing the following information:

    * An indication of the success or failure state of the custom render.

Valid values are `SUCCEEDED` and `FAILED`.

    * (Optional) any error messages that are generated by the custom render.

    * The Cloud Storage path for the rendered configuration file or files.

The path for all the rendered configuration files is the full URI. You populate it partly using the value of the `CLOUD_DEPLOY_OUTPUT_GCS_PATH` provided by Cloud Deploy.

You must provide the rendered configuration file, even if it's empty. The contents of the file can be anything, in any format, as long as it's consumable by your custom deploy. We recommend this file be human readable, so that you and other users in your organization can view this file in the [release inspector](https://docs.cloud.google.com/deploy/docs/view-release).

    * (Optional) a map of any metadata you want to include

Your custom target creates this metadata. This metadata is stored on the release, in the `custom_metadata` field.




If you need to examine the `results.json` file, for example for debugging, you can find the Cloud Storage URI to it in the Cloud Build logs.

### Example render results file

The following is a sample `results.json` file output from a custom render:
    
    
    {
      "resultStatus": "SUCCEEDED",
      "manifestFile": "gs://bucket/my-pipeline/release-001/rollout-a/01234/custom-output/manifest.yaml",
      "failureMessage": "",
      "metadata": {
        "key1": "val",
        "key2": "val"
      }
    }
    

### Inputs to custom deploys

For custom deploys, Cloud Deploy provides the following inputs, as environment variables:

  * `CLOUD_DEPLOY_PROJECT`

The Google Cloud project number for the project in which the custom target is created.

  * `CLOUD_DEPLOY_PROJECT_ID`

The Google Cloud project ID for the project.

  * `CLOUD_DEPLOY_LOCATION`

The Google Cloud region for the custom target type.

  * `CLOUD_DEPLOY_DELIVERY_PIPELINE`

The name of the Cloud Deploy delivery pipeline referencing the target that uses the custom target type.

  * `CLOUD_DEPLOY_RELEASE`

The name of the release for which the deploy operation is invoked.

  * `CLOUD_DEPLOY_ROLLOUT`

The name of the Cloud Deploy rollout that this deploy is for.

  * `CLOUD_DEPLOY_TARGET`

The name of the Cloud Deploy target that uses the custom target type.

  * `CLOUD_DEPLOY_PHASE`

The [rollout phase](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#phases) to which the deploy corresponds.

  * `CLOUD_DEPLOY_REQUEST_TYPE`

For the custom deploy, this is always `DEPLOY`.

  * `CLOUD_DEPLOY_FEATURES`

A comma-separated list of Cloud Deploy features which the custom container must support. This variable is populated based on features configured in your delivery pipeline.

If your implementation doesn't support the features in this list, we recommend that it fail during rendering.

For [standard deployments](https://docs.cloud.google.com/deploy/docs/deployment-strategies#what_deployment_strategies_does_support), this is empty. For canary deployments, the value is `CANARY`. If the value provided by Cloud Deploy is `CANARY`, your deploy is invoked for each phase in the canary. The canary percentage for each phase is provided in the `CLOUD_DEPLOY_PERCENTAGE_DEPLOY` environment variable.

  * `CLOUD_DEPLOY_PERCENTAGE_DEPLOY`

The percentage of deployment associated with this deploy operation. If the `CLOUD_DEPLOY_FEATURES` environment variable is set to `CANARY`, your custom deploy is called for each phase, and this variable is set to the canary percentage for each phase. Your deploy must run for each phase.

  * `CLOUD_DEPLOY_STORAGE_TYPE`

The storage provider. Always `GCS`.

  * `CLOUD_DEPLOY_INPUT_GCS_PATH`

The Cloud Storage path where the custom renderer wrote the rendered configuration files.

  * `CLOUD_DEPLOY_SKAFFOLD_GCS_PATH`

The Cloud Storage path to the rendered Skaffold configuration. If you provided a Skaffold config with your release.

  * `CLOUD_DEPLOY_MANIFEST_GCS_PATH`

The Cloud Storage path to the rendered manifest file.

  * `CLOUD_DEPLOY_OUTPUT_GCS_PATH`

The path to the Cloud Storage directory where the custom deploy container is expected to upload deploy artifacts. For more information, see Outputs from custom deploy.




### Outputs from custom deploy

Your custom deploy must write a `results.json` output file. This file must be located in the Cloud Storage bucket provided by Cloud Deploy (`CLOUD_DEPLOY_OUTPUT_GCS_PATH`).

The file must include the following:

  * An indication of the success or failure state of the custom deploy.

The following are the valid statuses:

    * `SUCCEEDED`

    * `FAILED`

    * `SKIPPED`

This is for canary deployments where [canary phases are skipped](https://docs.cloud.google.com/deploy/docs/deployment-strategies#skip_phases), to go straight to `stable`.

  * (Optional) a list of deploy artifact files, in the form of Cloud Storage paths

The path is the full URI. You populate it partly using the value of the `CLOUD_DEPLOY_OUTPUT_GCS_PATH` provided by Cloud Deploy.

Files listed here are populated in [job run resources](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#jobs_and_job_runs) as deploy artifacts.

  * (Optional) a failure message, if the custom deploy is unsuccessful (returning a `FAILED` state)

This message is used to populate the `failure_message` on the [job run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#jobs_and_job_runs) for this deploy.

  * (Optional) a skip message, to provide additional information if the deploy returns a `SKIPPED` status.

  * (Optional) a map of any metadata you want to include

Your custom target creates this metadata. This metadata is stored on the [job run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#jobs_and_job_runs) and on the rollout, in the `custom_metadata` field.




If you need to examine the `results.json` file, for example for debugging, you can find the Cloud Storage URI for it in the Cloud Build logs.

### Example deploy results file

The following is a sample `results.json` file output from a custom deploy:
    
    
    {
      "resultStatus": "SUCCEEDED",
      "artifactFiles": [
        "gs://bucket/my-pipeline/release-001/rollout-a/01234/custom-output/file1.yaml",
        "gs://bucket/my-pipeline/release-001/rollout-a/01234/custom-output/file2.yaml"
      ],
      "failureMessage": "",
      "skipMessage": "",
      "metadata": {
        "key1": "val",
        "key2": "val"
      }
    }
    

## Further information about custom targets

Here are some things to keep in mind when setting up and using custom target types.

### Executing the tasks

Your custom render and deploy tasks run in the Cloud Deploy [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment). You can't configure your tasks to run on a Google Kubernetes Engine cluster.

### Custom targets and deployment strategies

Custom targets are fully supported for [standard](https://docs.cloud.google.com/deploy/docs/terminology#standard_deployment_strategy) deployments.

Cloud Deploy supports [canary deployments](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary) as long as the custom renderer and deployer support the canary feature.

You must use [custom canary configuration](https://docs.cloud.google.com/deploy/docs/config-files#custom-canary-configuration). [Automated and custom-automated](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#types_of_canary) canaries are not supported with custom targets.

### Custom targets and deploy parameters

You can use [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) with custom targets. You can set them on the delivery pipeline [stage](https://docs.cloud.google.com/deploy/docs/parameters#add_to_pipeline_stage), on the target that uses a custom target type, or on the [release](https://docs.cloud.google.com/deploy/docs/parameters#pass_to_releases_create).

Deploy parameters are passed to your custom render and deploy containers, as environment variables, in addition to those already provided.

## Custom target examples

The [cloud-deploy-samples repository](https://github.com/GoogleCloudPlatform/cloud-deploy-samples/tree/main/custom-targets/) contains a set of sample custom target implementations. The following samples are available:

  * GitOps

  * Vertex AI

  * Terraform

  * Infrastructure Manager

  * Helm




Each sample includes a quickstart.

These samples are not a supported Google Cloud product, and are not covered by a Google Cloud support contract. To report bugs or request features in a Google Cloud product, contact Google Cloud support.

## What's next

  * Now that you know about custom targets, find out how to [configure and use them](https://docs.cloud.google.com/deploy/docs/create-custom-target).

  * Try the [quickstart: Define and use a custom target type](https://docs.cloud.google.com/deploy/docs/deploy-app-custom-target).

  * Learn more about [configuring Cloud Deploy targets](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions).

  * Learn about Cloud Deploy [execution environments](https://docs.cloud.google.com/deploy/docs/execution-environment). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
