---
url: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api/
title: Canary Deployments to GKE and GKE attached clusters using Gateway API networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:06.878993+00:00
---

# Canary Deployments to GKE and GKE attached clusters using Gateway API networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Canary Deployments to GKE and GKE attached clusters using Gateway API networking Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure and use canary deployments to deploy your applications to GKE or GKE attached clusters using Cloud Deploy with Kubernetes [Gateway API service mesh](https://gateway-api.sigs.k8s.io/).

A canary deployment is a progressive rollout of a new version of your application, where you gradually increase the percentage of traffic sent to the new version, while monitoring the application's performance. This helps you to catch potential problems early and minimize the impact on your users.

## How canary deployments work for GKE and GKE attached clusters using Gateway API

  1. In addition to the Deployment and Service references, you provide an HTTPRoute resource, with a `backendRefs` rule that references the Service.

  2. Cloud Deploy creates a new Deployment, with the name of your original Deployment plus `-canary`, and a new Service with the original Service name plus `-canary`.

Secrets, ConfigMaps, and Horizontal Pod Autoscalers are also copied and renamed with `-canary`.

  3. For each canary phase Cloud Deploy modifies the HTTPRoute to update the weighting between the original Deployment's pods and the canary Deployment's pods, based on the percentage for that phase.

Because there can be a delay propagating changes to `HTTPRoute` resources, you can include the `routeUpdateWaitTime` property in your configuration, so the system waits a specified amount of time for this propagation.

  4. During the `stable` phase, the `-canary` Deployment is scaled down to zero, and the original Deployment is updated to use the new release's Deployment.

Also, the HTTPRoute is now reverted to the original which you supplied.

Cloud Deploy doesn't modify the original Deployment or Service until the `stable` phase.




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

Your `skaffold.yaml` file defines how your Kubernetes manifests are rendered and deployed. For a canary deployment to GKE or GKE attached clusters, ensure the `skaffold.yaml` file correctly points to your manifests and defines any necessary build artifacts. No special canary-specific configuration is required within `skaffold.yaml` beyond what's needed for a [standard deployment](https://docs.cloud.google.com/deploy/docs/using-skaffold). You can also use Skaffold profiles to manage different manifest variations for custom canary phases.

### Prepare your Kubernetes manifests

Your Kubernetes manifests must include both a `Deployment` resource and a `Service` resource. The `Service` must define a `selector` that matches the labels of the pods managed by the `Deployment`. The default label Cloud Deploy looks for is `app`, but this can be configured in the pipeline.

In addition to the `Deployment` and `Service`, your manifests must include an `HTTPRoute` resource configured for traffic splitting, referencing the `Service` and associated Gateway.

### Configure an automated canary

Use Kubernetes Gateway API (with [Istio](https://istio.io) or any [supported implementation](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api.sigs.k8s.io/implementations)) for precise, percentage-based traffic splitting managed by the mesh/gateway, orchestrated by Cloud Deploy.

  1. Set up Gateway API Resources: Ensure your Gateway, and underlying service mesh (e.g., Istio) or Gateway controller are correctly configured in your cluster(s).

     * [Using Istio](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/)

     * [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)

  2. In your Kubernetes manifest, provided to Cloud Deploy when you created the release, include the following:

     * An [`HTTPRoute`](https://gateway-api.sigs.k8s.io/guides/traffic-splitting/) that references your Gateway resource

     * A Deployment

     * A Service

  3. Configure your delivery pipeline and the target that you will canary-deploy to:

     * Configuration for the target is the same as for any target.

     * The delivery pipeline configuration, in the progression sequence for the specific target, includes a `gatewayServiceMesh` stanza to reference your Kubernetes Gateway API `HTTPRoute` configuration, as well as your Deployment and Service.
           
           strategy:
            canary:
              runtimeConfig:
                kubernetes:
                  gatewayServiceMesh:
                    httpRoute: "ROUTE"
                    service: "SERVICE"
                    deployment: "DEPLOYMENT"
                    routeUpdateWaitTime: "WAIT_TIME"
                    podSelectorLabel: "LABEL"
              canaryDeployment:
                percentages:
                - 50
           

Where...

       * ROUTE is your httpRoute configuration that defines the routing behavior you want. 

       * SERVICE is your Service configuration, which Cloud Deploy requires for canary deployments to GKE and GKE attached clusters.

       * DEPLOYMENT is your Deployment configuration, which Cloud Deploy requires for canary deployments to GKE and GKE attached clusters.

       * WAIT_TIME is an amount of time for Cloud Deploy to wait for changes to the `HTTPRoute` resource to finish propagating, to avoid dropped requests. For example: `routeUpdateWaitTime: 60s`.

If you're running canary using Gateway API without Istio, and the Gateway API is connected to a Google Cloud load balancer, a small amount of traffic may be lost when the canary instance is scaled down. You can configure this setting if you observe this behavior.

       * LABEL is a pod selector label. This must match the label selector in the Kubernetes Service and Deployment defined in your manifest. This is optional. The default is `app`.




### Configure a custom-automated canary

A custom-automated canary combines custom phase definition (names, percentages, profiles, verify, hooks) with Cloud Deploy's automatic traffic management for GKE or GKE attached clusters. You define the phases, but Cloud Deploy handles the underlying resource manipulation based on the percentages and the chosen `runtimeConfig`.

To configure this, include both a `runtimeConfig` section with `serviceNetworking` and the `customCanaryDeployment` section (defining `phaseConfigs`) within the strategy.canary block. Cloud Deploy will use the specified Skaffold profiles for rendering but will automatically adjust traffic according to the `runtimeConfig` and phase percentages.
    
    
    serialPipeline:
      stages:
      - targetId: gke-prod
        profiles: []
        strategy:
          canary:
            # Include runtimeConfig for automatic traffic management
            runtimeConfig:
              kubernetes:
                gatewayServiceMesh:
                  httpRoute: "my-route"
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
                predeploy:
                  tasks: []
                postdeploy:
                  tasks: []
              - phaseId: "scaling"
                percentage: 50
                profiles: ["profile-b"] # Different profile for this phase
                verify:
                  tasks: []
                predeploy:
                  tasks: []
                postdeploy:
                  tasks: []
              - phaseId: "stable"
                percentage: 100
                profiles: ["profile-b"] # Can reuse profiles
                verify:
                  tasks: []
                predeploy:
                  tasks: []
                postdeploy:
                  tasks: []
    

## Deploy an HTTPRoute to a different cluster

When you have a canary configured using Gateway API service mesh, you can specify an alternate, non-target cluster on which to deploy the HTTPRoute.

To do so, you use a `routeDestinations` stanza, in your canary strategy configuration, to identify the destination cluster or clusters for the HTTPRoute, and a boolean setting to propagate the Service to the same non-target cluster. And you create an `associatedEntities` stanza in your target configuration to identify the clusters.

**Note:** You can only configure associated entities if you're using Kubernetes Gateway API service mesh.

  1. Configure `associatedEntities` on your target.

Each entity is a cluster where Cloud Deploy will deploy the HTTPRoute and, optionally, the Kubernetes Service. In your target definition, include an `associatedEntities` stanza:
         
         associatedEntities:
           [KEY]:
             gkeClusters:
             - cluster: [PATH]
               dnsEndpoint: [true|false]
               internalIp: [true|false]
               proxyUrl:
         

Where:

     * `KEY` is an arbitrary name for this group of associated entities. You'll use this name to reference the entities from the `routeDestinations` in your canary config.

     * `PATH` is the resource path identifying the GKE cluster where your HTTPRoute (and optionally the Service) will be deployed.

     * `dnsEndpoint` indicates whether or not to use the cluster's DNS Endpoint if multiple endpoints are configured. The default is `false`.

     * `internalIp` indicates whether or not to use the cluster's internal IP (private IP) if multiple endpoints are configured. The default is `false`.

You can include any number of clusters, with or without `internalIp`.

  2. Configure `routeDestinations` in your canary config.

Each route destination references an `associatedEntities` stanza, and indicates whether or not to also deploy the Service to the alternate cluster. Add the following inside `gatewayServiceMesh` stanza in your canary config:
         
         routeDestinations:
           destinationIds: ["KEY"]
           propagateService: [true|false]
         

Where:

     * `KEY` is the name you configured in the target, in `associatedEntities`. Use this name to reference the entities from the `routeDestinations` in your canary config.

You can also provide the value `@self` to deploy the HTTPRoute to the target cluster in addition to the associated destination.

     * `propagateService` indicates whether or not you want to deploy the Service to the associated cluster, in addition to the HTTPRoute. The default is `false`.




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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
