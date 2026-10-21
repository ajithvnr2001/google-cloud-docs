---
url: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking/
title: Canary Deployments to GKE and GKE attached clusters using service-based networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:00.805351+00:00
---

# Canary Deployments to GKE and GKE attached clusters using service-based networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Canary Deployments to GKE and GKE attached clusters using service-based networking Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure and use canary deployments to deploy your applications to GKE or GKE attached clusters using Cloud Deploy with service-based networking.

A canary deployment is a progressive rollout of a new version of your application, where you gradually increase the percentage of traffic sent to the new version, while monitoring the application's performance. This helps you to catch potential problems early and minimize the impact on your users.

## How canary deployments work for GKE and GKE attached clusters with service-based networking

  1. You provide the name of the Deployment resource and the Service resource.

  2. Cloud Deploy creates an additional Deployment resource, with the name of your current Deployment plus `-canary`.




Secrets and ConfigMaps are also copied and renamed with `-canary`.

  1. Cloud Deploy modifies the Service to adjust the selector to select the pods in the current Deployment and the canary pods.

Cloud Deploy calculates the number of pods to use for the canary based on the calculation described in the pod provisioning section. That calculation differs depending on whether you [enable or disable pod overprovisioning](https://docs.cloud.google.com/deploy/docs/config-files#strat_for_gke_targets).

If we're [skipping to the `stable` phase](https://docs.cloud.google.com/deploy/docs/deployment-strategies#skip_phases) Cloud Deploy adds the labels to be used to match pods, so they're available for subsequent canary runs.

Cloud Deploy creates a Deployment that includes the phase-specific percentage of pods, updating it for each phase. This is done by calculating the number of pods as a percentage of the original number of pods. This can result in an inexact traffic split. If you need an exact traffic split, you can achieve that using [Gateway API](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api).

  2. During the `stable` phase, the `-canary` Deployment is scaled down to zero, and the original Deployment is replaced with the new Deployment.

Cloud Deploy doesn't modify the original Deployment until the `stable` phase, unless you disable overprovisioning.




Cloud Deploy provisions pods to achieve the requested canary percentage as closely as possible. This is based on the number of pods, not traffic to the pods. If you want your canary to be based on traffic, you need to use [Gateway API](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api).

For GKE network-based canary, you can [enable or disable pod overprovisioning](https://docs.cloud.google.com/deploy/docs/config-files#strat_for_gke_targets). The following sections describe how Cloud Deploy calculates the number of pods to provision for the canary deployment for each canary phase.

#### Pod provisioning with overprovisioning enabled

Enabling overprovisioning ([`disablePodOverprovisioning: false`](https://docs.cloud.google.com/deploy/docs/config-files#strat_for_gke_targets)) allows Cloud Deploy to create enough additional pods to run the canary percentage you want, based on the number of pods running your existing deployment. The following formula shows how Cloud Deploy calculates the number of pods to provision for the canary deployment for each canary phase, when pod overprovisioning is enabled:

`math.Ceil( percentage * ReplicaCountOfDeploymentOnCluster / (100-percentage))`

With this formula, the current replica count (the number of pods you already have, before this canary) is multiplied by the canary percentage for the phase, and the result of that is divided by (100 minus the percentage).

For example, if you have 4 pods already, and your canary phase is 50%, then the number of canary pods is 4. (The result of `100-percentage` is used as a percentage: `100-50=50`, treated as `.50`.)

**Warning:** Using canary percentages larger than 50% may result in very large increases in the number of pods. In the previous example with 4 existing pods, a 90% canary will result in 36 canary pods. For this reason, if you want to use percentages larger than 50%, we recommend disabling overprovisioning, as described in the next section.

Pod overprovisioning is the default behavior.

#### Pod provisioning with overprovisioning disabled

You can disable overprovisioning ([`disablePodOverprovisioning: true`](https://docs.cloud.google.com/deploy/docs/config-files#strat_for_gke_targets)), to ensure that Cloud Deploy doesn't increase your replica count.

The following formula shows how Cloud Deploy calculates pod provisioning for the canary deployment for each canary phase, when pod overprovisioning is disabled:

`math.Ceil( (ReplicaCountOfDeploymentOnCluster + ReplicaCountOfCanaryDeploymentOnCluster) * percentage)`

In this formula, `ReplicaCountOfCanaryDeploymentOnCluster` only exists if there was already a canary phase. If this is the first canary phase, there is no `ReplicaCountOfCanaryDeploymentOnCluster`.

If you begin with 4 pods, that number is multiplied by the canary percentage (for example, 50%, or `.5`) to get `2`. So the original deployment is now scaled down to 2, and 2 new pods are created for the canary deployment. If you then have a 75% canary stage, you have `2` (original deployment) `+2` (first canary stage), `*.75`, to get `3` canary pods and `1` pod running the original deployment.

Using Cloud Deploy, you can configure canary deployments to GKE and GKE attached clusters in a single stage or in multiple stages.

The instructions here include only what is specific to canary configuration. The document [Deploy to a Google Kubernetes Engine cluster](https://docs.cloud.google.com/deploy/docs/gke-targets) has the general instructions for configuring and executing your deployment pipeline.

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

Your `skaffold.yaml` file defines how your Kubernetes manifests are rendered and deployed. For a canary deployment to GKE or GKE attached clusters, ensure it correctly points to your manifests and defines any necessary build artifacts. No special canary-specific configuration is required within `skaffold.yaml` itself beyond what's needed for a [standard deployment](https://docs.cloud.google.com/deploy/docs/using-skaffold). You might use Skaffold profiles to manage different manifest variations for custom canary phases.

### Prepare your Kubernetes manifests

Your Kubernetes manifests must include both a `Deployment` resource and a `Service` resource. The `Service` must define a `selector` that matches the labels of the pods managed by the `Deployment`. The default label Cloud Deploy looks for is `app`, but this can be configured in the pipeline.

### Configure an automated canary

Configure an automated canary directly within your delivery pipeline definition for a specific GKE or GKE attached clusters stage using standard Kubernetes Service networking.

In the pipeline stage, include a `strategy` property, as follows:
    
    
    serialPipeline:
      stages:
      - targetId: prod
        profiles: []
        strategy:
          canary:
            runtimeConfig:
              kubernetes:
                serviceNetworking:
                  service: "SERVICE_NAME"
                  deployment: "DEPLOYMENT_NAME"
                  podSelectorLabel: "LABEL"
            canaryDeployment:
              percentages: [PERCENTAGES]
              verify:
                tasks: []
              predeploy:
                tasks: []
              postdeploy:
                tasks: []
    

In this configuration...

  * SERVICE_NAME is the name of the Kubernetes Service, defined in your manifest.

  * DEPLOYMENT_NAME is the name of your Kubernetes Deployment, defined in your manifest.

  * LABEL is a pod selector label. This must match the label selector in the Kubernetes Service defined in your manifest. This is optional. The default is `app`.

  * PERCENTAGES is a comma-separated list of percentage values representing your canary increments, for example `[5, 25, 50]`.

Also, this doesn't include `100`, because 100% percent deployment is _assumed_ in the canary, and is handled by the `stable` phase

  * You can enable [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) by configuring the `verify` stanza. If you do so, a `verify` job is enabled on each phase.

  * You can enable [predeploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) by configuring the `predeploy` stanza. If you do so, a `predeploy` job is added to the first canary phase.

  * You can enable [postdeploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) by configuring the `postdeploy` stanza. If you do so, a `postdeploy` job is added to the stable phase.




### Configure a custom-automated canary

A custom-automated canary combines custom phase definition (names, percentages, profiles, verify, hooks) with Cloud Deploy's automatic traffic management for GKE or GKE attached clusters. You define the phases, but Cloud Deploy handles the underlying resource manipulation based on the percentages and the chosen `runtimeConfig`.

To configure a custom-automated canary, include both a `runtimeConfig` section with `serviceNetworking` and the `customCanaryDeployment` section (defining `phaseConfigs`) within the strategy.canary block. Cloud Deploy uses the specified Skaffold profiles for rendering but automatically adjusts traffic according to the `runtimeConfig` and phase percentages.
    
    
    serialPipeline:
      stages:
      - targetId: gke-prod
        profiles: []
        strategy:
          canary:
            # Include runtimeConfig for automatic traffic management
            runtimeConfig:
              kubernetes:
                serviceNetworking:
                  service: "my-app"
                  deployment: "my-deployment"
            # Include customCanaryDeployment for phase customization
            customCanaryDeployment:
              phaseConfigs:
              - phaseId: "warmup"
                percentage: 10
                profiles: ["profile-a"] # Profile used for rendering this phase
                verify:
                  tasks: []
              - phaseId: "scaling"
                percentage: 50
                profiles: ["profile-b"] # Different profile for this phase
                verify:
                  tasks: []
              - phaseId: "stable"
                percentage: 100
                profiles: ["profile-b"] # Can reuse profiles
                verify:
                  tasks: []
    

## Execute the GKE or GKE attached clusters canary

  1. Register Pipeline and Targets: Apply your delivery pipeline and GKE or GKE attached clusters target configuration files.
         
         gcloud deploy apply --file=delivery-pipeline.yaml --region=REGION
         gcloud deploy apply --file=gke-targets.yaml --region=REGION
         

The delivery pipeline includes the automated or custom canary configuration, for your chosen runtime.

  2. Create a Release: Start the deployment, providing the image name.
         
         gcloud deploy releases create RELEASE_NAME \
                                         --delivery-pipeline=PIPELINE_NAME \
                                         --region=REGION
           # e.g., --images=my-cloudrun-service=gcr.io/my-project/my-app:v1.1
           # Add --skaffold-file or --source if not using default Skaffold config discovery
         

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




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
