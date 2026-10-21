---
url: https://docs.cloud.google.com/deploy/docs/tasks/
title: Configure tasks \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:48.864910+00:00
---

# Configure tasks  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Configure tasks Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure tasks in Cloud Deploy. A task is a unit of work that can be used as a [deploy hook](https://docs.cloud.google.com/deploy/docs/hooks), for [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment), for [deploy analysis](https://docs.cloud.google.com/deploy/docs/analysis), or for a custom render or custom deploy in a [custom target type](https://docs.cloud.google.com/deploy/docs/custom-targets).

You can configure a task on the delivery pipeline (as part of the [strategy](https://docs.cloud.google.com/deploy/docs/config-files#strategy_configuration)) or the [custom target type](https://docs.cloud.google.com/deploy/docs/config-files#custom_target_type_definitions) render or deploy.

With tasks, you can use [system parameters](https://docs.cloud.google.com/deploy/docs/tasks#system_params) by templating them into your task configuration.

## Define a task

You can define a task in your delivery pipeline configuration or as part of a custom target type definition. The following YAML shows the `task` stanza used in either case:
    
    
      task:
        type: container
        image: IMAGE
        command: [COMMANDS_TO_RUN]
        args: [LIST_OF_ARGS]
        env:
        - KEY1:VAL1
        - KEY2:VAL2
        ...
    

For the `task` configuration:

  * `type`

Specifies the kind of task being configured. Only `container` is supported.

  * `image`

Is the path to the container image.

  * `command`

Is the command or commands to run on the container.

  * `args`

Is a collection of arguments to the `command`.

  * `env`

Is a collection of environment variables to be provided to the running container.


**Note:** When you define tasks in a delivery pipeline configuration, you create a list of one or more `task`s. When you're configuring a custom target type, you create only one `task`.

## System Parameters as task environment variables

Cloud Deploy offers system-generated parameters that you can use as environment variables in your tasks, using the `env` field in the `container` task. The templated parameters can be present in the key or value fields of an `env` map entry.

Here are a couple of example use cases:

  * Passing in the Cloud Run service name, service URL, and revision name as environment variables.
        
        task:
          type: container
          image: my-image
          command: ["/bin/bash"]
          env:
          - RUN_SERVICE_NAME : "${{ render.metadata.cloud_run.service.name }}"
          - RUN_SERVICE_URL: "${{ rollout.metadata.cloud_run.service_url }}"
          - RUN_REVISION_NAME: "${{ render.metadata.cloud_run.revision.name }}"
        

  * Using multiple parameters in a single entry.
        
        task:
          type: container
          image: my-image
          command: ["/bin/bash"]
          env:
          - DEPLOY_PARAMS_KEY : "${{ deploy_params['FOO'] }}-with-${{ deploy_params['BAR'] }}"
          - "${{ project.id }}_${{ location }}" : "${{ target.id }}"
        




### Available system parameters

Cloud Deploy provides the following system parameters that you can use in your tasks configuration using this format:

`${{ parameter }}`

**Note:** Cloud Deploy will attempt to evaluate instances of `${{ }}` in any task environment variable. If you want to escape this evaluation, then prepend another `$` to the template expression, like this:

`$${{ }}`.

The following is the list of parameters available for templating:

Name  |  Definition   
---|---  
`location` |  The region containing the Cloud Deploy resources.  
Available at release creation.   
`project.num` | The Google Cloud project number for the project containing the Cloud Deploy resources.  
Available at release creation.  
`project.id` | The Google Cloud project ID for the project.  
Available at release creation.  
`delivery_pipeline.name` | The fully specified resource name of the delivery pipeline.  
Available at release creation.  
`delivery_pipeline.id` | The ID of the delivery pipeline.  
Available at release creation.  
`target.name` | The fully specified resource name of the target.  
Available at release creation.  
`target.id` | The ID of the target.  
Available at release creation.  
`release.name` | The fully specified resource name of the release.  
Available at release creation.  
`release.id` | The ID of the release.  
Available at release creation.  
`rollout.name` | The fully specified resource name of the rollout.  
Available at rollout creation.  
`rollout.id` | The ID of the rollout.  
Available at rollout creation.  
`job.id` | The ID of the job being executed.  
Available at rollout creation.  
`phase.id` | The [phase](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#phases) in the rollout that contains the job for the tasks.  
Available at rollout creation.  
`job_run.name` | The fully specified resource name of the [job run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#jobs_and_job_runs) that represents the current execution of the job.  
Available at rollout creation.  
`job_run.id` | The ID of the [job run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#jobs_and_job_runs) that represents the current execution of the job.  
Available at rollout creation.  
`deploy_params` | A map of the [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) associated with the target.  
Example: `deploy_params['KEY']`   
Trying to access a key that doesn't exist results in an empty string.  
Available at release creation.  
For targets of type `RUN`:  
`cloud_run.project` | The project in which the Cloud Run service was created.  
Available at release creation.  
`cloud_run.location` | The region the Cloud Run service is deployed in.  
Available at release creation.  
`render.metadata.cloud_run.service.name` | The name of the Cloud Run service deployed.  
Available after the render operation has completed.  
`render.metadata.cloud_run.service.id` | The ID of the Cloud Run service deployed.  
Available after the render operation has completed.  
`rollout.metadata.cloud_run.service.url` | The URL that end users will use to access your service. You can find these in the Cloud Run service details for your service, in the Google Cloud console.  
Available after the deploy operation has completed.  
`render.metadata.cloud_run.revision.name` | The full name of the revision of the Cloud Run service being deployed.  
Available after the render operation has completed.  
`render.metadata.cloud_run.revision.id` | The revision ID of the Cloud Run service being deployed.  
Available after the render operation has completed.  
`rollout.metadata.cloud_run.previous_revision.name` | The full name of the previous revision of the Cloud Run service being deployed.  
Available after the deploy operation has completed.  
`rollout.metadata.cloud_run.previous_revision.id` | The previous revision ID of the Cloud Run service being deployed.  
Available after the deploy operation has completed.  
For targets of type `GKE`:  
`gke.cluster.name` | The fully specified resource name of the GKE cluster.  
Available at release creation.  
`gke.cluster.id` | The ID of the GKE cluster.  
Available at release creation.  
`gke.cluster.project` | The project ID/number of the GKE cluster.  
Available at release creation.  
`gke.cluster.location` | The location of the GKE cluster.  
Available at release creation.  
For targets of type `ANTHOS`:  
`anthos.membership.project` | The project ID/number of the GKE Enterprise cluster.  
Available at release creation.  
`anthos.membership.location` | The location of the GKE Enterprise cluster.  
Available at release creation.  
`anthos.membership.name` | The fully specified resource name of the GKE Enterprise membership.  
Available at release creation.  
`anthos.membership.id` | The ID of the GKE Enterprise membership.  
Available at release creation.  
For Kubernetes targets (targets of type `GKE` and `ANTHOS`):  
`render.metadata.kubernetes.deployment` | The name of the deployment being updated. This is not set if there is more than one deployment in the manifests.  
Available after the render operation has completed.  
`render.metadata.kubernetes.canary_deployment` | The name of the canary deployment in an automated canary. For the stable phase, this is the same as `render.metadata.kubernetes.deployment`, because there is no canary in the stable phase. For the other phases, this is the same as `render.metadata.kubernetes.deployment` with `-canary` on the end.  
Available after the render operation has completed.  
`render.metadata.kubernetes.namespace` | The namespace of the resources being deployed. This is not set if there's more than one namespace in the manifests.  
Available after the render operation has completed.  
For targets of type `CUSTOM_TARGET_TYPE`:  
`render.metadata.custom` | A map of the render metadata from a custom render.  
Example: `render.metadata.custom['KEY']`  
Trying to access a key that doesn't exist results in an empty string.  
Available after the render operation has completed.  
`rollout.metadata.custom` | A map of the rollout metadata from a custom deploy.  
Example: `rollout.metadata.custom['KEY']`  
Trying to access a key that doesn't exist results in an empty string.  
Available after the deploy operation has completed.  
  
## Available environment variables

Cloud Deploy also provides and populates the following environment variables in the [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment). You can use these environment variables as part of your [deploy hook](https://docs.cloud.google.com/deploy/docs/hooks), [verify job](https://docs.cloud.google.com/deploy/docs/verify-deployment), or [custom target](https://docs.cloud.google.com/deploy/docs/custom-targets) render or deploy.

  * `ANTHOS_MEMBERSHIP`

For targets of type `ANTHOS`, the fully specified resource name of the Anthos membership.

  * `CLOUD_RUN_LOCATION`

For targets of type `RUN`, the region the Cloud Run service is deployed in.

  * `CLOUD_RUN_PROJECT`

For targets of type `RUN`, the project in which the Cloud Run service was created.

  * `CLOUD_RUN_SERVICE`

For targets of type `RUN`, the name of the Cloud Run service deployed.

  * `CLOUD_RUN_SERVICE_URLS`

For targets of type `RUN`, the URL or URLs (comma-separated list) that end users will use to access your service. You can find these in the Cloud Run service details for your service, in the Google Cloud console. The URLs are generated by Cloud Run after your Cloud Run Service or Services have been successfully deployed. Therefore this environment variable is only available in postdeploy hooks and [verify jobs](https://docs.cloud.google.com/deploy/docs/verify-deployment).

  * `CLOUD_RUN_REVISION`

For targets of type `RUN`, the specific revision of the Cloud Run service.

  * `GKE_CLUSTER`

For targets of type `GKE`, the fully specified resource name of the Google Kubernetes Engine cluster, for example `projects/p/locations/us-central1/clusters/dev`.

  * `TARGET_TYPE`

The specific runtime type of the target. Either `GKE`, `ANTHOS`, or `RUN`. For custom targets, this won't be set.

  * `CLOUD_DEPLOY_LOCATION`

The region containing the Cloud Deploy resources.

  * `CLOUD_DEPLOY_DELIVERY_PIPELINE`

The ID of the delivery pipeline.

  * `CLOUD_DEPLOY_TARGET`

The ID of the target.

  * `CLOUD_DEPLOY_PROJECT`

The Google Cloud project number for the project containing the Cloud Deploy resources.

  * `CLOUD_DEPLOY_PROJECT_ID`

The Google Cloud project ID for the project.

  * `CLOUD_DEPLOY_RELEASE`

The ID of the release in which the hooks will run.

  * `CLOUD_DEPLOY_ROLLOUT`

The ID of the rollout that contains the jobs for the hooks.

  * `CLOUD_DEPLOY_JOB_RUN`

The ID of the [job run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#jobs_and_job_runs) that represents the current execution of the job.

  * `CLOUD_DEPLOY_PHASE`

The [phase](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#phases) in the rollout that contains the job for the deploy hook, verify job, or custom render or deploy.




## What's next

  * Learn how to run [deploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) using tasks
  * Learn how to [verify your deployment](https://docs.cloud.google.com/deploy/docs/verify-deployment) using tasks
  * Learn about [custom targets](https://docs.cloud.google.com/deploy/docs/create-custom-target)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
