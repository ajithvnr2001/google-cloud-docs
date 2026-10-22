---
url: https://docs.cloud.google.com/deploy/docs/hooks/
title: Run hooks before and after deploying \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:46.465011+00:00
---

# Run hooks before and after deploying  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/hooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Run hooks before and after deploying Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to run arbitrary programs or operations before or after you deploy.

You can configure Cloud Deploy to perform pre-deployment actions or post-deployment actions, or both. These programs, run in this way, are called "hooks." Predeploy and postdeploy hooks run as predeploy and postdeploy [jobs](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#jobs_and_job_runs) on the rollout.

You can configure each hook to run in a specified Cloud Deploy [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment), but if you're deploying to Google Kubernetes Engine you can optionally configure it to run on the GKE cluster where you're deploying your application.

Deploy hooks are assumed to be idempotent. If a given action is run more than once, there is no additional effect.

**Note:** the user who provides the program to run is responsible for that program's behavior, including idempotency.

## How do deploy hooks work?

The following describes how deploy hooks run in Cloud Deploy and how to set them up:

  1. You configure hooks in one or more stages in your delivery pipeline progression.

  2. Before the rollout's deploy job runs, Cloud Deploy runs any tasks configured in a `predeploy` definition in the pipeline progression.

The `predeploy` hook always runs as the first job in the phase.

  3. After the rollout's deploy job runs, Cloud Deploy runs any tasks configured in a `postdeploy` definition in the pipeline progression.

**Note:** if there is a `verify` job configured for the stage, [verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) runs _before_ the `postdeploy` job.



Deploy hooks are run in the Cloud Deploy [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment).

### Using deploy hooks with a canary deployment

When you configure deploy hooks for a canary deployment, there are several things to know:

  * In the delivery pipeline stage, [configuration of the hook](https://docs.cloud.google.com/deploy/docs/config-files#predeploy_and_postdeploy_hooks) (`predeploy` and `postdeploy`) is under `strategy.canary.canaryDeployment` or `strategy.canary.customCanaryDeployment.phaseConfigs`, rather than under `strategy.standard`.

  * For an automated canary, `predeploy` hooks are executed before the deploy in the first phase only, and `postdeploy` hooks are executed after the deploy in the last phase (stable) only.




## Configure your pipeline to run hooks

You configure Pre- and post-deploy hooks in one or more specific stages in the pipeline [progression](https://docs.cloud.google.com/deploy/docs/terminology#progression).

The following is how you would configure pre-and post-deploy hooks in a pipeline stage when using a `standard` deployment strategy:
    
    
    serialPipeline:
      stages:
      - targetId: hooks-staging
        profiles: []
        strategy:
          standard:
            predeploy:
              tasks: [TASKS]
            postdeploy:
              tasks: [TASKS]
    

In this yaml:

  * TASKS

Is a list of one or more [Tasks](https://docs.cloud.google.com/deploy/docs/tasks) that you want to run as part of your predeploy or postdeploy hooks. When you specify more than one task, they execute serially, in the order they're specified. The job (predeploy or postdeploy) fails on the first task that fails, and the remaining tasks aren't run.




## Run the hooks on the application cluster

By default, deploy hooks run in the Cloud Deploy [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment). You can also configure Skaffold to run deploy hooks on the same cluster where your application is running.

To run hooks on the application cluster, you must configure them as [`customActions`](https://skaffold.dev/docs/custom-actions/) in your `skaffold.yaml`, and reference them using `actions` in the `predeploy` or `postdeploy` stanza in your delivery pipeline stage configuration:
    
    
    serialPipeline:
      stages:
      - targetId: hooks-staging
        profiles: []
        strategy:
          standard:
            predeploy:
              actions: ["my-predeploy-action"]
            postdeploy:
              actions: ["my-postdeploy-action"]
    

**Note:** If you configure hooks using `tasks`, those hooks run only in the Cloud Deploy execution environment. To run hooks on the cluster, you must use `actions`.

This ability is available for deployments to GKE only, not for Cloud Run. Deployments to Cloud Run can only run hooks in the Cloud Deploy execution environment.

To configure your hook to run on the cluster, include an `executionMode.kubernetesCluster` stanza in your `skaffold.yaml` configuration file, inside the `customActions` stanza for each action you want to run on the cluster:
    
    
    customActions:
    - name: ACTION_NAME
      containers:
      - name: CONTAINER_NAME
        image: IMAGE
        command: [COMMANDS_TO_RUN]
        args: [LIST_OF_ARGS]
      executionMode:
        kubernetesCluster: {}
    

**Note:** you can also include the `jobManifestPath` and `overrides` properties, under `kubernetesCluster`, to point to a manifest for your container, and any values you want to override. (`overrides` takes Kubernetes inline JSON with the values you want to replace.) [Learn more](https://skaffold.dev/docs/custom-actions/#remote-k8s-job).

The following is an example `customActions` stanza that includes `executionMode` to invoke the hook container on the application cluster:
    
    
    customActions:
    - name: predeploy-action
      containers:
      - name: predeploy-echo
        image: ubuntu
        command: ["/bin/sh"]
        args: ["-c", 'echo "this is a predeploy action"' ]
      executionMode:
        kubernetesCluster: {}
    

The `executionMode` stanza is optional, and if you omit it, Skaffold runs the custom action container in the Cloud Deploy execution environment.

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




### Deploy parameters as environment variables

In addition to the environment variables listed in this section, Cloud Deploy can pass to your custom containers any [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) you've set.

[Learn more](https://docs.cloud.google.com/deploy/docs/parameters).

## What's next

  * Learn more about [tasks](https://docs.cloud.google.com/deploy/docs/tasks)
  * Try the [quickstart: Run hooks before and after deploying](https://docs.cloud.google.com/deploy/docs/deploy-app-hooks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
