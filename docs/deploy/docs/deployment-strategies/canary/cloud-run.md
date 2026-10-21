---
url: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run/
title: Canary Deployments to Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:49.490535+00:00
---

# Canary Deployments to Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Canary Deployments to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure and use canary deployments to deploy your applications to Cloud Run. Cloud Deploy canary supports Cloud Run services and worker pools, but not jobs.

A canary deployment is a progressive rollout of a new version of your application, where you gradually increase the percentage of traffic sent to the new version, while monitoring the application's performance. This helps you to catch potential problems early and minimize the impact on your users.

## How canary deployments work for Cloud Run

When you deploy to Cloud Run using a canary deployment strategy, Cloud Deploy updates your existing service with a new revision. The new revision receives a specified percentage of traffic, and the old revision continues to receive the remainder. You gradually increase the traffic split to the new revision over time.

Using Cloud Deploy, you can configure canary deployments to Cloud Run in a single stage or in multiple stages.

The instructions here include only what is specific to canary configuration. The document [Deploy a Cloud Run service, job, or worker pool](https://docs.cloud.google.com/deploy/docs/run-targets) has the general instructions for configuring and executing your deployment pipeline.

### Make sure you have the required permissions

In addition to other Identity and Access Management permissions you need for using Cloud Deploy, you need the following permissions in order to perform additional actions that might be needed for a canary deployment:

  * `clouddeploy.rollouts.advance`
  * `clouddeploy.rollouts.ignoreJob`
  * `clouddeploy.rollouts.cancel`
  * `clouddeploy.rollouts.retryJob`
  * `clouddeploy.jobRuns.get`
  * `clouddeploy.jobRuns.list`
  * `clouddeploy.jobRuns.terminate`



See [IAM roles and permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions) for more information about what available roles include these permissions.

### Prepare your `skaffold.yaml`

Your `skaffold.yaml` file defines how your Cloud Run service definitions are rendered and deployed. For a canary deployment to Cloud Run, ensure it correctly points to your service definition file(s) and defines any necessary build artifacts (like container images). No special canary-specific configuration is required within `skaffold.yaml` itself beyond what's needed for a [standard deployment](https://docs.cloud.google.com/deploy/docs/using-skaffold). You might use Skaffold profiles to manage different service definition variations for custom canary phases.

### Prepare your service or worker pool definition

Your normal Cloud Run service definition file is sufficient, but without a `traffic` stanza. Cloud Deploy manages splitting traffic for you between the last successful revision and the new revision.

###  Service

Example `service.yaml` (without `traffic` stanza):
    
    
     apiVersion: serving.knative.dev/v1
     kind: Service
     metadata:
       name: my-cloudrun-service
     spec:
       template:
         spec:
           containers:
           - image: gcr.io/my-project/my-cloudrun-app
             ports:
             - containerPort: 8080
    

###  Worker pool

Example `worker-pool.yaml` (without `instanceSplit` stanza):
    
    
     apiVersion: run.googleapis.com/v1
     kind: WorkerPool
     metadata:
       name: my-wp
       annotations:
         run.googleapis.com/launch-stage: BETA
     spec:
       template:
         spec:
           containers:
           - image: us-docker.pkg.dev/cloudrun/container/worker-pool
    

### Configure an automated canary

Configure an automated canary directly within your delivery pipeline definition for a specific Cloud Run stage. Cloud Deploy automatically instructs Cloud Run to split traffic between the last stable revision and the new revision according to the specified percentages.
    
    
    serialPipeline:
      stages:
      - targetId: prod
        profiles: []
        strategy:
          canary:
            runtimeConfig:
              cloudRun:
                automaticTrafficControl: true
            canaryDeployment:
              percentages: [PERCENTAGES]
              verify:
                tasks: [TASKS]
              predeploy:
                tasks: [TASKS]
              postdeploy:
                tasks: [TASKS]
    

In this configuration:

  * PERCENTAGES is a comma-separated list of percentage values representing your canary increments, for example `[25, 50, 75]`. Note that this doesn't include `100`, because 100% percent deployment is _assumed_ in the canary, and is handled by the `stable` phase.

  * You can enable [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) by configuring the `verify` stanza. If you do so, a `verify` job is added to each canary phase.

  * You can enable [predeploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) by configuring the `predeploy` stanza. If you do so, a `predeploy` job is added to the first canary phase.

  * You can enable [postdeploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) by configuring the `postdeploy` stanza. If you do so, a `postdeploy` job is added to the `stable` phase.

  * Each `tasks` property under `verify`, `predeploy` and `postdeploy` consists of one or more [tasks](https://docs.cloud.google.com/deploy/docs/tasks) to run as part of that job. Any configured tasks will run sequentially in the order they are defined.




### Configure a custom-automated canary

This combines custom phase definition (names, percentages, profiles, verify, hooks) with Cloud Deploy's automatic traffic management for Cloud Run. You define the phases, but Cloud Deploy handles instructing Cloud Run to shift traffic based on the percentages.

To configure this, include both the `runtimeConfig.cloudRun.automaticTrafficControl: true` setting and the `customCanaryDeployment` section (defining `phaseConfigs`) within the `strategy.canary` block. Cloud Deploy will use the specified Skaffold profiles for rendering the service definition (which still shouldn't have a `traffic` stanza) but will automatically manage traffic according to the phase percentages.
    
    
    serialPipeline:
      stages:
      - targetId: cloudrun-prod
        profiles: []
        strategy:
          canary:
            # Include runtimeConfig for automatic traffic management
            runtimeConfig:
              cloudRun:
                automaticTrafficControl: true
            # Include customCanaryDeployment for phase customization
            customCanaryDeployment:
              phaseConfigs:
              - phaseId: "warmup-cr"
                percentage: 10
                profiles: ["base-config"] # Profile rendering service def (no traffic stanza)
                verify:
                  tasks: [TASKS]
              - phaseId: "scaling-cr"
                percentage: 50
                profiles: ["base-config"] # Can use the same profile
                verify:
                  tasks: [TASKS]
              - phaseId: "stable"
                percentage: 100
                profiles: ["base-config"]
                verify:
                  tasks: [TASKS]
    

## Execute the Cloud Run canary

  1. Register Pipeline and Targets: Apply your delivery pipeline and Cloud Run target configuration files.
         
         gcloud deploy apply --file=delivery-pipeline.yaml --region=REGION
         gcloud deploy apply --file=cloudrun-targets.yaml --region=REGION
         

The delivery pipeline includes the automated or custom canary configuration, for your chosen runtime.

  2. Create a Release: Start the deployment, providing the image name.
         
         gcloud deploy releases create RELEASE_NAME \
                                         --delivery-pipeline=PIPELINE_NAME \
                                         --region=REGION
         

The delivery pipeline identified by `PIPELINE_NAME` contains the automated or custom canary configuration described in this document.

  3. Advance the canary:

###  gcloud CLI 
         
         gcloud deploy rollouts advance ROLLOUT_NAME \
                                     --release=RELEASE_NAME \
                                     --delivery-pipeline=PIPELINE_NAME \
                                     --region=REGION
         

Where:

`ROLLOUT_NAME` is the name of the current rollout which you're advancing to the next phase.

`RELEASE_NAME` is the name of the release that this rollout is part of.

`PIPELINE_NAME` is the name of the delivery pipeline you're using to manage deployment of this release.

`REGION` is the name of the region in which the release was created, for example `us-central1`. This is required.

See the Google Cloud SDK reference for more information about the [`gcloud deploy rollouts advance` command](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/rollouts/advance).

###  Google Cloud console 

     1. [Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines).

     2. Click your pipeline shown in the list of delivery pipelines.

The Delivery pipeline details page shows a graphical representation of your delivery pipeline's progress.

     3. On the **Rollouts** tab, under **Delivery pipeline details** , click the name of your rollout.

The rollout details page is shown, for that rollout.

![rollout details in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/rollout-details-canary50.png)

Notice that in this example, the rollout has a `canary-50` phase and a `stable` phase. Your rollout might have more phases or different phases.

     4. Click **Advance rollout**.

The rollout is advanced to the next phase.




### Skipped phases

If you deploy a canary and your application has not been deployed to that runtime yet, Cloud Deploy skips the canary phase and runs the stable phase. See [Skipping phases the first time](https://docs.cloud.google.com/deploy/docs/deployment-strategies#skip_phases) to find out why this happens.

## What's next

  * Try the [canary deployment quickstart](https://docs.cloud.google.com/deploy/docs/deploy-app-canary).

  * Find out how to [manage the lifecycle of your canary's rollouts](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout).

  * Learn more about [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel).

  * Learn more about [Cloud Deploy deployment strategies](https://docs.cloud.google.com/deploy/docs/deployment-strategies).

  * Learn more about [Cloud Run](https://docs.cloud.google.com/run/docs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
