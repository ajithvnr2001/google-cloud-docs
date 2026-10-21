---
url: https://docs.cloud.google.com/deploy/docs/config-files/
title: Configuration schema reference \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:04.425812+00:00
---

# Configuration schema reference  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/config-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Configuration schema reference Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Deploy configuration file or files define the [delivery pipeline](https://docs.cloud.google.com/deploy/docs/terminology#delivery_pipeline), the [targets](https://docs.cloud.google.com/deploy/docs/terminology#target) to deploy to, and the [progression](https://docs.cloud.google.com/deploy/docs/terminology#progression) of those targets.

The delivery pipeline configuration file _can_ include target definitions, or those can be in a separate file or files. By convention, a file containing both the delivery pipeline config and the target configs is called `clouddeploy.yaml`, and a pipeline config without targets is called `delivery-pipeline.yaml`. But you can give these files any name you want. Other resource definitions, such as [automations](https://docs.cloud.google.com/deploy/docs/automation) and [deploy policies](https://docs.cloud.google.com/deploy/docs/deploy-policy), can also be in the same file as a delivery pipeline or target definition.

**Note:** your organization might prefer to separate target definitions from the pipeline definition, so that different roles can manage those configurations separately. Cloud Deploy supports that practice.

## What goes where

Cloud Deploy uses two main configuration files:

  * Delivery pipeline definition
  * Target definition



These can be separate files, or the delivery pipeline and targets can be configured in the same file.

**Note:** After you define the configuration file or files, you create the delivery pipeline and target resources using the command line, as described in [Registering the delivery pipeline and targets](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets).

## Structure of a delivery pipeline configuration file

The following is the structure of a delivery pipeline configuration, including properties for target definitions. Some target properties are not included here. See Target definitions for all target configuration properties.
    
    
    # Delivery pipeline config
    apiVersion: deploy.cloud.google.com/v1
    kind: DeliveryPipeline
    metadata:
     name:
     annotations:
     labels:
    description:
    suspended:
    serialPipeline:
     stages:
     - targetId:
       profiles: []
    # Deployment strategies
    # One of:
    #   standard:
    #   canary:
    # See the strategy section in this document for details.
       strategy:
         standard:
           predeploy:
             tasks: []
           verify:
             tasks: []
           analysis:
           postdeploy:
             tasks: []
       deployParameters:
       - values:
         matchTargetLabels:
     - targetId:
       profiles: []
       strategy:
       deployParameters:
    ---
    
    # Target config
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
     name:
     annotations:
     labels:
    description:
    multiTarget:
     targetIds: []
    deployParameters:
    requireApproval:
    #
    # Runtimes
    # one of the following runtimes:
    gke:
     cluster:
     dnsEndpoint:
     internalIp:
     proxyUrl:
    #
    # or:
    anthosCluster:
     membership:
    #
    # or:
    run:
     location:
    #
    # or:
    customTarget:
      customTargetType:
    #
    # (End runtimes. See documentation in this article for more details.)
    #
    executionConfigs:
    - usages:
      - [RENDER | PREDEPLOY | DEPLOY | VERIFY | POSTDEPLOY | ANALYSIS]
      workerPool:
      serviceAccount:
      artifactStorage:
      executionTimeout:
      verbose:
    ---
    
    # Custom target type config
    apiVersion: deploy.cloud.google.com/v1
    kind: CustomTargetType
    metadata:
      name:
      annotations:
      labels:
    description:
    tasks:
      render:
      deploy:
    ---
    
    # Automation config
    apiVersion: deploy.cloud.google.com/v1
    kind: Automation
    metadata:
      name:
      labels:
      annotations:
    description:
    suspended:
    serviceAccount:
    selector:
      targets:
        -  id: [TARGET_ID]
           labels:
             [LABEL_KEY]:[LABEL_VALUE]
    rules:
    - [RULE_TYPE]:
      id:
      [RULE-SPECIFIC_CONFIG]
    
    

This YAML has three main components:

  * The main delivery pipeline and progression

The configuration file can include any number of pipeline definitions.

  * The target definitions

For simplicity, only one target is shown in this example, but there can be any number of them. Also, targets can be defined in a separate file or files.

  * Custom target type definitions

[Custom targets](https://docs.cloud.google.com/deploy/docs/custom-targets), require a custom target type definition. As with targets and automations, custom target types can be defined in the same file as the delivery pipeline, or in separate file.

  * Automation definitions

You can create any [deploy automations](https://docs.cloud.google.com/deploy/docs/automation) in the same file as your delivery pipeline and targets, or in a separate file or files. For simplicity, only one `Automation` is shown here, but you can create as many as you want.




These components are defined in the rest of this document.

## Pipeline definition and progression

In addition to pipeline metadata, such as `name`, the main pipeline definition includes a list of references to [targets](https://docs.cloud.google.com/deploy/docs/terminology#target) in deployment sequence order. That is, the first target listed is the first deployment target. After you've deployed to that target, promoting the release deploys to the next target in the list.

The following are the configuration properties for a delivery pipeline, not including target definitions.

### `metadata.name`

The `name` field takes a string that must be unique per project and location.

### `metadata.annotations` and `metadata.labels`

Delivery pipeline configuration can include annotations and labels. Annotations and labels are stored with the delivery pipeline resource after the pipeline has been [registered](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets).

For more information, see [Using labels and annotations with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/labels-annotations).

### `description`

An arbitrary string describing this delivery pipeline. This description is shown in the delivery pipeline details in Google Cloud console.

### `suspended`

A Boolean, which if `true` [suspends the delivery pipeline](https://docs.cloud.google.com/deploy/docs/suspend-pipeline) such that it can't be used to create, promote, roll back, or redeploy releases. Also, if the delivery pipeline is suspended, you can't approve or reject a rollout created from that pipeline.

The default is `false`.

### `serialPipeline`

The beginning of the definition of a serial-progression delivery pipeline. This stanza is required.

### `stages`

A list of all targets to which this delivery pipeline is configured to deploy.

The list must be in the order of the delivery sequence you want. For example, if you have targets called `dev`, `staging`, and `production`, list them in that same order, so that your first deployment is to `dev`, and your final deployment is into `production`.

Populate each `stages.targetId` field with the value of the `metadata.name` field in the corresponding target definition. And under `targetId`, include `profiles`:
    
    
    serialPipeline:
     stages:
     - targetId:
       profiles: []
       strategy:
         standard:
           verify:
    

### `targetId`

Identifies the specific target to use for this stage of the delivery pipeline. The value is the `metadata.name` property from the target definition.

`strategy.standard.verify` set to `true` enables [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) on the target. If no deployment strategy is specified, the `standard` deployment strategy is used, with verification set to `false`.

### `profiles`

Takes a list of zero or more Skaffold profile names, from `skaffold.yaml`. Cloud Deploy uses the profile with [`skaffold render`](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment) when creating the release. Skaffold profiles let you vary configuration between targets while using a single configuration file.

## `strategy`

Includes properties for specifying a deployment strategy. The following strategies are supported:

  * `standard:`

The application is deployed fully to the specified target.

This is the default deployment strategy. If you omit `strategy`, Cloud Deploy uses the `standard` deployment strategy.

  * `canary:`

In a [canary deployment](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary), you deploy a new version of your application progressively, replacing the already running version by percentage-based increments (for example, 25%, then 50%, then 75%, then fully.)




The deployment strategy is defined per target. For example, you might have a canary strategy for your `prod` target, but a standard strategy (no `strategy` specified) for your other targets.

For more information, see [Use a deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies).

### `strategy` configuration

This section shows the configuration elements for `strategy`, for each supported runtime.

#### Standard deployment strategy

The standard strategy includes only the following elements:
    
    
    strategy:
      standard:
        verify:
          tasks: []
        analysis:
    

The [verify](https://docs.cloud.google.com/deploy/docs/verify-deployment) property lets you reference one or more [tasks](https://docs.cloud.google.com/deploy/docs/tasks) to execute to verify your deployment. If configured, the verify tasks will run sequentially, immediately after the 'deploy' job.

The `verify` property is optional. If not specified, there will be no [verify](https://docs.cloud.google.com/deploy/docs/verify-deployment) job in the resulting rollouts.

The `analysis` stanza is optional, for use with [Cloud Deploy analysis](https://docs.cloud.google.com/deploy/docs/analysis).

You can omit the `strategy` element for a [standard](https://docs.cloud.google.com/deploy/docs/deployment-strategies#what_strategies) deployment strategy.

#### Canary deployment strategy

The following sections describe configuration for a [canary deployment](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary) strategy, for each runtime that Cloud Deploy supports.

##### For Cloud Run targets
    
    
    strategy:
      canary:
        runtimeConfig:
          cloudRun:
            automaticTrafficControl: true | false
        canaryDeployment:
          percentages: [PERCENTAGES]
          verify:
            tasks: []
          analysis:
    

For Cloud Run targets, `AutomaticTrafficControl` must be `true` unless you're configuring a [custom canary](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/custom).

##### For GKE and GKE attached clusters targets

The following YAML shows how to configure a deployment strategy for a target that deploys to GKE or GKE attached clusters, using [service-based networking](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking):
    
    
          canary:
            runtimeConfig:
              kubernetes:
                serviceNetworking:
                  service: "SERVICE_NAME"
                  deployment: "DEPLOYMENT_NAME"
                  disablePodOverprovisioning: true | false
            canaryDeployment:
              percentages: [PERCENTAGES]
              verify:
                tasks: []
    

The following YAML shows how to configure a deployment strategy for a target that deploys to GKE or GKE attached clusters, using [Gateway API](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api):
    
    
          canary:
            runtimeConfig:
              kubernetes:
                gatewayServiceMesh:
                  httpRoute: "HTTP_ROUTE_NAME"
                  service: "SERVICE_NAME"
                  deployment: "DEPLOYMENT_NAME"
                  routeUpdateWaitTime: "WAIT_TIME"
                  routeDestinations:
                    destinationIds: ["KEY"]
                    propagateService: [true|false]
            canaryDeployment:
              percentages: ["PERCENTAGES"]
              verify:
                tasks: []
    

Notice in this example [`routeUpdateWaitTime`](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api). This is included because Gateway API splits traffic using an `HTTPRoute` resource, and sometimes there is a delay propagating changes made to the `HTTPRoute`. In such cases requests may be dropped, because traffic is being sent to resources that are unavailable. You can use `routeUpdateWaitTime` to cause Cloud Deploy to wait after applying `HTTPRoute` changes, if you observe this delay.

The following YAML shows how to configure a custom canary deployment strategy (for [service networking](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking#custom), [gateway api](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api#custom) or [Cloud Run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run#custom)) or custom-automated canary deployment strategy (for [service networking](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking#custom-automated), [gateway api](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api#custom-automated) or [Cloud Run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run#custom-automated)). Runtime-specific configuration, in the `runtimeConfig` section, is omitted for custom canary, but included in automated and custom automated canary configuration.

#### Custom Canary configuration
    
    
    strategy:
      canary:
        # Runtime configs are configured as shown in the
        # Canary Deployment Strategy section of this document.
        runtimeConfig:
    
        # Manual configuration for each canary phase
        customCanaryDeployment:
          - name: "PHASE1_NAME"
            percent: PERCENTAGE1
            profiles: [ "PROFILE1_NAME" ]
            verify:
              tasks: []
          - …
          - name: "stable"
            percent: 100
            profiles: [ "LAST_PROFILE_NAME" ]
            analysis: [ANALYSIS_CONFIGS]
            verify:
              tasks: []
    

### `verify`

The `verify` stanza can be included under `strategy.standard`, `strategy.canary.canaryDeployment`, or under each phase in `strategy.canary.customCanaryDeployment`. It's used to enable [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) for a target. This stanza is optional; if omitted, no verification is performed for the rollout or canary phase.

You can configure `verify` in either of two ways:

  * Set `verify: true`.

If you do this, you must also configure a `verify` stanza in your `skaffold.yaml`, as described in [Configure Skaffold for verification](https://docs.cloud.google.com/deploy/docs/verify-deployment#configure_skaffold).

  * Configure `verify` using one or more [tasks](https://docs.cloud.google.com/deploy/docs/tasks) to run for verification:
        
        verify:
          tasks: [VERIFY_TASKS]
        




### `analysis`

Deploy analysis, which you can use to run one or more checks against Google Cloud Observability alerts, is configured inside a `strategy` stanza. See Analysis definitions for configuration details.

### `deployParameters`

Lets you specify key value pairs to pass values to manifests for label-matched targets, when using [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters).

You can also include this on targets.

Deploy parameters set on a delivery pipeline use labels to match targets:
    
    
    deployParameters:
    - values:
        someKey: "value1"
      matchTargetLabels:
        label1: firstLabel
    - values:
        someKey: "value2"
      matchTargetLabels:
        label2: secondLabel
    

In this example, there are two values provided for the key, and for each value, there is a label. The value is applied to the manifest for any target that has a matching label.

### `predeploy` and `postdeploy` jobs

Predeploy and postdeploy hooks are jobs to run before or after the deploy job in a rollout. You can define predeploy and postdeploy hooks in either of two ways:

  * Configure [tasks](https://docs.cloud.google.com/deploy/docs/tasks)
  * Reference reference custom [actions](https://docs.cloud.google.com/deploy/docs/hooks#configure_in_skaffold).



Predeploy jobs run immediately before the deploy job in a rollout. Postdeploy jobs run after all other jobs in the rollout, including verify and analysis, if applicable.

Deploy hooks are configured under `strategy.standard` or `strategy.canary` as follows:

  * Using `tasks`
        
        serialPipeline:
          stages:
          - targetId:
            strategy:
              standard:
                predeploy:
                  tasks: [PREDEPLOY_TASKS]
                postdeploy:
                  tasks: [POSTDEPLOY_TASKS]
        

Where:

    * PREDEPLOY_TASKS are one or more [Tasks](https://docs.cloud.google.com/deploy/docs/tasks) you want to run in your predeploy hook.

    * POSTDEPLOY_TASKS are one or more [Tasks](https://docs.cloud.google.com/deploy/docs/tasks) you want to run in your postdeploy hook.

  * Using `actions` (and Skaffold)
        
        serialPipeline:
          stages:
          - targetId:
            strategy:
              standard:
                predeploy:
                  actions: [ACTION_NAME]
                postdeploy:
                  actions: [ACTION_NAME]
        

Where ACTION_NAME is the name configured in `skaffold.yaml` for `customActions.name`.

You can configure `predeploy` and `postdeploy` jobs under any strategy (`standard`, `canary`, for example).




For more information about configuring and using pre- and post-deploy hooks, see [Run hooks before and after deploying](https://docs.cloud.google.com/deploy/docs/hooks).

## Target definitions

The delivery pipeline definition file can contain target definitions, or you can specify targets in a separate file.

You can reuse targets among multiple delivery pipelines. However, you can only reference a target once from within a single delivery pipeline's progression.

See also: Custom target type definitions

### For GKE targets

The following YAML shows how to configure a target that [deploys to a GKE cluster](https://docs.cloud.google.com/deploy/docs/gke-targets):
    
    
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
          name:
          annotations:
          labels:
         description:
         deployParameters:
         multiTarget:
          targetIds: []
    
         requireApproval:
         gke:
          cluster: projects/[project_name]/locations/[location]/clusters/[cluster_name]
          dnsEndpoint:
          internalIp:
          proxyUrl:
    
         associatedEntities:
           [KEY]:
             gkeClusters:
             - cluster: projects/[project_name]/locations/[location]/clusters/[cluster_name]
               dnsEndpoint: [true|false]
               internalIp: [true|false]
               proxyUrl:
    
         executionConfigs:
         - usages:
           - [RENDER | PREDEPLOY | DEPLOY | VERIFY | POSTDEPLOY | ANALYSIS]
           workerPool:
           serviceAccount:
           artifactStorage:
           executionTimeout:
           verbose:
    

#### `metadata.name`

The name of this target. This name must be unique per region.

#### `metadata.annotations` and `metadata.labels`

Target configuration supports [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) and [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/), but Cloud Deploy does not require them.

Annotations and labels are stored with the target resource. For more information, see [Using labels and annotations with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/labels-annotations).

#### `description`

This field takes an arbitrary string that describes the use of this target.

#### `deployParameters`

You can include [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) on any target, along with values. Those values are assigned to the corresponding keys in your manifest, after rendering.

The `deployParameters` stanza takes key-value pairs, as shown:
    
    
    deployParameters:
      someKey: "someValue"
      someOtherKey: "someOtherValue"
    

If you set deploy parameters on a [multi-target](https://docs.cloud.google.com/deploy/docs/terminology#multi-target), the value is assigned to the manifest for all of that multi-target's [child targets](https://docs.cloud.google.com/deploy/docs/terminology#child_target).

#### `multiTarget.targetIds: []`

This property is optional, and is used to configure a [multi-target](https://docs.cloud.google.com/deploy/docs/terminology#multi_target) to be used for [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel).

The value is a comma-separated list of [child targets](https://docs.cloud.google.com/deploy/docs/terminology#child_target). Child targets are configured as normal targets, and don't include this `multiTarget` property.

#### `requireApproval`

Whether promotion to this target requires manual approval. Can be `true` or `false`.

This property is optional. The default is `false`.

When you configure [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel), you can require approval on the multi-target only—not on child targets.

#### `gke`

For GKE clusters only, the resource path identifying the cluster where your application will be deployed:
    
    
    gke:
      cluster: projects/[project_name]/locations/[location]/clusters/[cluster_name]
    

  * `project_name`

The Google Cloud project in which the cluster lives.

  * `location`

The location where the cluster lives. For example, `us-central1`. The cluster can also be zonal (`us-central1-c`).

  * `cluster_name`

The name of the cluster, as it appears in your list of clusters in Google Cloud console.




Here's an example:
    
    
    gke:
      cluster: projects/cd-demo-01/locations/us-central1/clusters/prod
    

Omit the `gke` property when configuring a [multi-target](https://docs.cloud.google.com/deploy/docs/terminology#multi-target). The GKE cluster is configured instead inside the corresponding child target.

See `executionConfigs`, in this document, for descriptions of the execution environment properties. See [Deploy an HTTPRoute to a different cluster](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#httproute-to-cluster) for information about deploying the HTTPRoute to an alternate, non-target cluster.

### `associatedEntities.[KEY]`

In a canary configuration, you use this name to reference the entities from `routeDestinations`. [Learn more](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api#httproute-to-cluster).

#### `dnsEndpoint`

When set to `true`, Cloud Deploy will connect to the GKE cluster using the DNS endpoint instead of the default endpoint, which may be a public IP, private IP, or the DNS endpoint, depending on the cluster configuration.

This option cannot be used at the same time as the `internalIp` option.

#### `internalIp`

When set to `true`, Cloud Deploy will connect to the GKE cluster using the private IP address instead of the default endpoint, which may be a public IP, private IP, or the DNS endpoint, depending on the cluster configuration.

This option cannot be used at the same time as the `dnsEndpoint` option. Because network configuration for `dnsEndpoint` is much simpler, we [recommend using that instead](https://docs.cloud.google.com/deploy/docs/gke-targets#dns-based-endpoint).

#### `proxyUrl`

If you access clusters through an HTTP proxy, provide the `proxyUrl` property here. The value is the URL of the proxy, which is [passed to kubectl](https://www.google.com/url?sa=D&q=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Fconfiguration%2Forganize-cluster-access-kubeconfig%2F%23proxy) when connecting to your cluster.

### For Cloud Run targets

The following YAML shows how to configure a target that [deploys to a Cloud Run service](https://docs.cloud.google.com/deploy/docs/run-targets):
    
    
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
          name:
          annotations:
          labels:
         description:
         multiTarget:
          targetIds: []
    
         requireApproval:
         run:
          location: projects/[project_name]/locations/[location]
    
         executionConfigs:
         - usages:
           - [RENDER | PREDEPLOY|  DEPLOY | VERIFY | POSTDEPLOY | ANALYSIS]
           workerPool:
           serviceAccount:
           artifactStorage:
           executionTimeout:
           verbose:
    

#### `metadata.name`

The name of this target. This name must be unique per region.

#### `metadata.annotations` and `metadata.labels`

Target configuration supports [annotations and labels](https://docs.cloud.google.com/deploy/docs/labels-annotations), but Cloud Deploy does not require them.

Annotations and labels are stored with the target resource. For more information, see [Using labels and annotations with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/labels-annotations).

#### `description`

This field takes an arbitrary string that describes the use of this target.

#### `multiTarget.targetIds: []`

This property is optional, and is used to configure a [multi-target](https://docs.cloud.google.com/deploy/docs/terminology#multi_target) to be used for [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel).

The value is a comma-separated list of [child targets](https://docs.cloud.google.com/deploy/docs/terminology#child_target). Child targets are configured as normal targets, and don't include this `multiTarget` property.

#### `requireApproval`

Whether promotion to this target requires manual approval. Can be `true` or `false`.

This property is optional. The default is `false`.

When you configure [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel), you can require approval on the multi-target only—not on child targets.

#### `run`

For Cloud Run services only, the location where the service will be created:
    
    
    run:
      location: projects/[project_name]/locations/[location]
    

  * `project_name`

The Google Cloud project in which the service will live.

  * `location`

The location where the service will lives. For example, `us-central1`.




Omit the `run` property when configuring a [multi-target]. The location of the Cloud Run service is configured instead inside the corresponding child target.

See `executionConfigs`, in this article, for descriptions of the execution environment properties.

### For GKE attached clusters targets

Target configuration for [deploying to GKE attached clusters](https://docs.cloud.google.com/deploy/docs/anthos-targets) is similar to configuring a target for a GKE target, except that the property is `anthosCluster.membership`, instead of `gke.cluster`, the resource path is different, and specific connection methods (`dnsEndpoint` or `internalIp`) are not applicable.
    
    
    anthosCluster:
      membership: projects/[project_name]/locations/global/memberships/[membership_name]
    

  * `project_name`

The Google Cloud project in which the cluster lives.

  * `/location/global/`

The location where the cluster is registered. `global`, in all cases.

  * `membership_name`

The name of the cluster membership.




Here's an example:
    
    
    anthosCluster:
      membership: projects/cd-demo-01/locations/global/memberships/prod
    

Omit the `anthosCluster` property when configuring a [multi-target]. The cluster is configured instead inside the corresponding child target.

For more information about deploying to GKE attached clusters, see [Deploy to GKE attached clusters](https://docs.cloud.google.com/deploy/docs/anthos-targets).

### For custom targets

Configuration for [custom targets](https://docs.cloud.google.com/deploy/docs/custom-targets) is similar to all other target types, except that it does not include a `gke` stanza, nor a `run` stanza, nor an `anthosCluster` stanza.

Instead, custom targets include a `customTarget` stanza:
    
    
    customTarget:
      customTargetType: [CUSTOM_TARGET_TYPE_NAME]
    

Where `CUSTOM_TARGET_TYPE_NAME` is the name you used in the custom target type definition.

Here's an example:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
      name: sample-env
    customTarget:
      customTargetType: basic-custom-target
    

### `executionConfigs`

A set of fields to specify a non-default [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment) for this target.

**Note:** all configuration properties under `executionConfigs` are optional. You don't need to [specify an execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment) if you can use the default worker pool, service account, and storage bucket.

  * `usages`

Either `RENDER` or `DEPLOY` or both, plus `PREDEPLOY`, `VERIFY`, or `POSTDEPLOY` if [verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) or [deploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) are enabled on the target. These indicate which of those operations to [perform](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit) for this target using this execution environment. To indicate that a custom execution environment is to be used for predeploy hook, render, deploy, postdeploy hook, and verification, you would configure it as follows:
        
        usages:
        - RENDER
        - PREDEPLOY
        - DEPLOY
        - VERIFY
        - POSTDEPLOY
        - ANALYSIS
        

If verification is [enabled on the pipeline stage](https://docs.cloud.google.com/deploy/docs/verify-deployment#configure_pipeline), and you don't specify `VERIFY` in a `usages` stanza, Cloud Deploy uses the default execution environment for verification. Predeploy and postdeploy [hooks](https://docs.cloud.google.com/deploy/docs/hooks) work the same way.

However, if there is a custom execution environment for `RENDER` and `DEPLOY`, you _must_ specify one for `VERIFY`, `PREDEPLOY`, `POSTDEPLOY`, or `ANALYSIS` if they're configured on the delivery pipeline.`VERIFY`, `PREDEPLOY`, `POSTDEPLOY`, and `ANALYSIS` can be in the same `usages` as `RENDER` or `DEPLOY`, or in separate `usages`.

You can't specify `usages.VERIFY`, `usages.PREDEPLOY`, `usages.POSTDEPLOY`, or `usages.ANALYSIS` unless `RENDER` and `DEPLOY` are specified in the same or separate custom execution environments.

  * `workerPool`

Configuration for the worker pool to use. This takes a resource path identifying the Cloud Build worker pool to use for this target. For example:

`projects/p123/locations/us-central1/workerPools/wp123`.

To use the [default Cloud Build pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview#overview_of_default_pools_and_private_pools), omit this property.

A given target can have two `workerPool`s (one for `RENDER` and one for `DEPLOY`). When configuring the default pool, you can specify an alternate service account or storage location or both.

  * `serviceAccount`

The name of the service account to use for this operation (`RENDER` or `DEPLOY`) for this target.

  * `artifactStorage`

The Cloud Storage bucket to use for this operation (`RENDER` or `DEPLOY`) for this target, instead of the default bucket.

  * `executionTimeout`

Optional. Sets the timeout, in seconds, for operations that Cloud Build performs for Cloud Deploy. By default this is `3600` seconds (1 hour).  
Example: `executionTimeout: "5000s"`

  * `verbose`

Optional. If `true`, the verbosity levels are set to `debug` for the following tools:

    * Skaffold [`--verbosity`](https://skaffold.dev/docs/references/cli/#global-flags) is set to `debug`. Skaffold default is `warn`.

    * [kubectl `--v`](https://kubernetes.io/docs/reference/kubectl/quick-reference/#kubectl-output-verbosity-and-debugging) is set to `4`, which is debug. The kubectl default is `2`.

    * [Google Cloud CLI `--verbosity`](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity) is set to `debug`. The default is `warning`.


**Note:** If you specify a configuration for either RENDER or DEPLOY, you must do so for the other, even if one uses default values (only the `usages:` property).

#### Alternative supported syntax

The `executionConfigs` configuration described in this document is new. The previous syntax is still supported:
    
    
    executionConfigs:
    - privatePool:
        workerPool:
        serviceAccount:
        artifactStorage:
      usages:
      - [RENDER | DEPLOY]
    - defaultPool:
        serviceAccount:
        artifactStorage:
      usages:
      - [RENDER | DEPLOY]
    

When you're configuring an `executionConfigs` stanza for a [multi-target](https://docs.cloud.google.com/deploy/docs/terminology#multi-target), each child target [can inherit that execution environment](https://docs.cloud.google.com/deploy/docs/parallel#execution_environments_and_parallel_deployment) from that multi-target.

## Custom target type definitions

This section describes the fields used to define [custom target types](https://docs.cloud.google.com/deploy/docs/custom-targets)

As with standard targets and automations, `CustomTargetType` definitions can be included with your delivery pipeline definition, or in a separate file or files.

The following YAML shows how to configure a custom target type:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: CustomTargetType
    metadata:
      name: [CUSTOM_TARGET_TYPE_NAME]
      annotations:
      labels:
    description:
    customActions:
      renderAction: [RENDER_ACTION_NAME]
      deployAction: [DEPLOY_ACTION_NAME]
      includeSkaffoldModules:
        - configs:
        # either:
        googleCloudStorage:
          source:
          path:
        # or:
        git:
          repo:
          path:
          ref:
    

Where:

  * `[CUSTOM_TARGET_TYPE_NAME]`

Is an arbitrary name you give to this custom target type definition. This name is referenced in the target definition for any target that uses the custom target type you're defining.

  * `[RENDER_ACTION_NAME]`

Is the name of the custom render action. This value is the `customAction.name` defined in `skaffold.yaml`.

  * `[DEPLOY_ACTION_NAME]`

Is the name of the custom deploy action. This value is the `customAction.name` defined in `skaffold.yaml`.

  * For `includeSkaffoldModules`, see [Use remote Skaffold configs](https://docs.cloud.google.com/deploy/docs/create-custom-target#remote_skaffold).




## Automation definitions

This section describes the fields used to define the Cloud Deploy [automation](https://docs.cloud.google.com/deploy/docs/automation-resource#the_automation_resource) resources.

As with targets, `Automation` definitions can be included with your delivery pipeline definition, or in a separate file or files.

For more information about automation in Cloud Deploy, see the [automation documentation](https://docs.cloud.google.com/deploy/docs/automation).

The following YAML shows how to configure an automation. Note that the specifics of an automation _rule_ are different per rule. (Configuration for the available automation rule types is in the document [Using automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules).)
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: Automation
    metadata:
      name: [PIPELINE_NAME]/[PURPOSE]
      labels:
      annotations:
    description: [DESCRIPTION]
    suspended: true | false
    serviceAccount: [SERVICE_ACCOUNT_ID]
    selector:
      targets:
        -  id: [TARGET_ID]
           labels:
             [LABEL_KEY]:[LABEL_VALUE]
    
    rules:
    - [RULE_TYPE]:
        id:[RULE_NAME]
      [RULE-SPECIFIC_CONFIG]
    

Where:

  * `[PIPELINE_NAME]`

Is the same as the `metadata.name` value in the delivery pipeline that uses this automation. All automations are exclusive to the delivery pipelines for which they're created. That is, you can't share an automation across more than one delivery pipeline.

  * `[PURPOSE]`

Is any further descriptive name for this automation. Typically, this would be the action that's automated. For example, `my-app-pipeline/promote`.

  * `labels` and `annotations` are any labels or annotations you want to associate with this automation.

  * `[DESCRIPTION]`

Is an optional description for this automation.

  * `suspended`

`true` or `false`, indicating whether this automation is active or suspended. If set to `true`, the automation is not used. This can be useful for [testing an automation without affecting the delivery pipeline](https://docs.cloud.google.com/deploy/docs/automation#suspend).

  * `[SERVICE_ACCOUNT_ID]`

Is the ID of the service account used to perform the [automation](https://docs.cloud.google.com/deploy/docs/automation-resources#automation_service_account). For example, if the automation uses the `promoteReleaseRule`, then this service account performs the release promotion, and thus requires the [permissions that are needed](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#permissions) to promote a release.

A value is required for this property. Cloud Deploy doesn't use the [default service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account) for automations.

This service account must have the following permissions:

    * `actAs` permission to impersonate the execution service account.

    * [permission](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#permissions) to perform the operation being automated, for example, `clouddeploy.releases.promote` to promote a release, or `clouddeploy.rollouts.advance` to advance a rollout phase.

  * `[TARGET_ID]`

Is the ID of the target for which this automation is used. Although an automation is tied to a delivery pipeline, it's only executed on the specified target or targets.

You can set this to `*` to select all targets in the delivery pipeline.

  * `[LABEL_KEY]:[LABEL_VALUE]`

Is a key-value pair to match against a key-value pair defined on the target. This select all targets associated with the delivery pipeline that have the same label and value.

  * `[RULE_TYPE]`

Is the name of the automation rule used for this automation. This is either `promoteReleaseRule`, `timedPromoteReleaseRule`, `advanceRolloutRule`, or `repairRolloutRule`. You can include more than one rule in an automation, including more than one of the same `RULE_TYPE`. For example, you can have more than one `promoteReleaseRule` rule in the same automation. [Learn more](https://docs.cloud.google.com/deploy/docs/automation-rules).

  * `[RULE_NAME]`

A name for the rule. This name must be unique within the automation resource. A value is required for this property.

  * `[RULE-SPECIFIC_CONFIG]`

Configuration is different for each supported automation type. Those configurations are shown in [Using automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules).




## Deploy policy definitions

This section describes the fields used to define [deploy policies](https://docs.cloud.google.com/deploy/docs/deploy-policy).

As with other Cloud Deploy resources, you can include `DeployPolicy` definitions with your delivery pipeline definition or in a separate file.

The following YAML shows how to configure a deploy policy:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: DeployPolicy
    metadata:
      name: [POLICY_NAME]
      annotations: [ANNOTATIONS]
      labels: [LABELS]
    description: [DESCRIPTION]
    suspended: [true | false]
    selectors:
    - deliveryPipeline:
        id: [PIPELINE_ID]
        labels:
          [LABEL_KEY]:[LABEL_VALUE]
      target:
        id: [TARGET_ID]
        labels:
          [LABEL_KEY]:[LABEL_VALUE]
    rules:
      - [RULE_TYPE]
          [CONFIGS]
    

Where:

  * `[DESCRIPTION]`

Is optional text describing this policy.

  * `[POLICY_NAME]`

A name for the policy. This field takes a string that must be unique per project and location. This must be lower-case letters, numbers, and hyphens, with the first character a letter, the last character a letter or a number, and a 63-character maximum. This name is used as a display name in the Google Cloud console.

  * `[ANNOTATIONS]` and `[LABELS]`

Policies can include annotations and labels, which are part of the policy resource after it's created. For more information, see [Using annotations and labels with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/labels-annotations).

  * `suspended: [true | false]`

Setting `suspended` to `true` deactivates this policy.

  * `[PIPELINE_ID]`

Is the ID for the delivery pipeline you want this policy to affect. You can use `*` to denote all pipelines. This ID is the same as the `metadata.name` property on the delivery pipeline.

  * `[TARGET_ID]`

Is the ID for the target you want this policy to affect. You can use `*` to denote all targets. This ID is the same as the `metadata.name` property on the target.

  * `[LABEL_KEY]:[LABEL_VALUE]`

Is a key-value pair to match against a key-value pair defined on the delivery pipeline or target. This selects all pipelines or targets that have the same label and value. You can specify `labels` instead of or in addition to `id`.

  * `[RULE_TYPE]`

Is the specific policy rule type you're configuring. The only valid value is `rolloutRestriction`.

  * `[CONFIGS]`

Is the set of configuration properties for the specific policy rule you're creating. Configuration for rules is described later in this section of this reference, for each of the available rules.




### Deploy policy rules

This section describes how to configure each deploy policy rule.

#### `rolloutRestriction`

The `rolloutRestriction` rule prevents Cloud Deploy from performing [certain operations](https://docs.cloud.google.com/deploy/docs/deploy-policy#rules) on rollouts during the time window or windows specified, for the delivery pipelines and targets indicated by the `selectors` for the deploy policy.

The following YAML shows how to configure a `rolloutRestriction` rule:
    
    
    rules:
    - rolloutRestriction:
        id: [RULE_ID]
        actions:
        - [ACTIONS]
        invokers:
        - [INVOKERS]
        timeWindows:
          timeZone: [TIMEZONE]
          oneTimeWindows:
          - start: [START_DATE_TIME]
            end: [END_DATE_TIME]
          weeklyWindows:
          - daysOfWeek:
            - [DAY_OF_WEEK]
            - [DAY_OF_WEEK]
            startTime: [START_TIME]
            endTime: [END_TIME]
    

Where:

  * `RULE_ID`

An identifier for this rule. This is required. It must consist of lower-case letters, numbers, and hyphens, with the first character a letter, the last character a letter or a number, and a 63-character maximum. It must be unique within the deploy policy.

  * `ACTIONS`

Optional: rollout actions to be restricted as part of the policy. If empty, all actions are restricted. Valid values are:

    * `ADVANCE`

Rollout phases can't be [advanced](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#advance_rollout).

    * `APPROVE`

Rollout promotion can't be approved.

    * `CANCEL`

Rollouts can't be canceled.

    * `CREATE`

Rollouts can't be created.

    * `IGNORE_JOB`

Jobs can't be [ignored](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#ignore_job).

    * `RETRY_JOB`

Jobs can't be [retried](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#retry_failed_job).

    * `ROLLBACK`

Rollouts can't be [rolled back](https://docs.cloud.google.com/deploy/docs/roll-back).

    * `TERMINATE_JOBRUN`

Job runs can't be [terminated](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#terminate_job_run)

  * `INVOKERS`

Specifying invokers will filter policy enforcement depending on whether the action being restricted was invoked by a user or by a deploy automation. Valid values are:

    * `USER`

The action is user-driven. For example, creating a rollout manually using a gcloud CLI command.

    * `DEPLOY_AUTOMATION`

An [automated action](https://docs.cloud.google.com/deploy/docs/automation) by Cloud Deploy.

You can specify either value or both values. The default, if you specify nothing, is both.

  * `TIMEZONE`

The time zone, in [IANA format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), in which you're expressing the time window. For example, `America/New_York`. This is required.

  * `START_DATE_TIME`

For `oneTimeWindows`, the date and time that marks the beginning of the restriction window, in the format `"yyyy-mm-dd hh:mm"`. For the beginning of the day, use `00:00`. This field is required.

  * `END_DATE_TIME`

For `oneTimeWindows`, the date and time that marks the end of the restriction window, in the format `"yyyy-mm-dd hh:mm"`. For the end of the day, use `24:00`. This field is required.

  * `DAY_OF_WEEK`

For `weeklyWindows`, the day of the week, `SUNDAY`, `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, or `SATURDAY`. If you leave this blank, it matches all days of the week

  * `START_TIME`

For `weeklyWindows`, the start time on the specified day of the week. If you include a start time, you must include an end time. For the beginning of the day, use `00:00`.

  * `END_TIME`

For `weeklyWindows`, the end time on the specified day of the week. If you include a start time, you must include an end time. For the end of the day, use `24:00`.




## Analysis definitions

An `analysis` stanza lets you configure an [analysis job](https://docs.cloud.google.com/deploy/docs/analysis) to run one or more checks against Google Cloud Observability alerts, or similar data from other monitoring providers, in order to take actions based on those alerts.

The `analysis` stanza differs based on whether you're configuring it for Google Cloud Observability or for a different provider using [custom analysis](https://docs.cloud.google.com/deploy/docs/analysis/custom-analysis).

#### `analysis` for Google Cloud Observability

The `analysis` stanza can be used directly inside a deployment strategy config (`strategy.standard.analysis`, for a standard strategy). If you want to configure analysis per phase, you use a custom canary (`strategy.canary.customCanaryDepolyment.phaseConfigs.phaseId.analysis`).
    
    
    analysis:
      duration: DURATION
      googleCloud:
        alertPolicyChecks:
        - id: CHECK_ID
          alertPolicies:
          - ALERT_POLICY_NAME
          labels:
            LABEL_KEY: LABEL_VALUE
    

The following are the configuration properties for `analysis`, when using Google Cloud Observability:

  * You can have any number of `alertPolicyChecks`.

  * `DURATION` is the amount of time, in seconds, minutes, or hours, to run the analysis. After this time expires, the analysis is no longer affected by alerts from Google Cloud Observability. For example: `200s`.

`CHECK_ID` is a unique ID for the alert policy check. This is displayed in the results of the analysis, for each check.

  * `ALERT_POLICY_NAME` is the name of the alert policy you created in Google Cloud Observability.

  * `LABEL_KEY` is a label name for any labels your check will use to match against the Google Cloud Observability alerting policy.

  * `LABEL_VALUE` is the value to match for each label.




#### Custom `analysis`

An analysis job that uses custom checks (against data from a monitoring provider other than Google Cloud Observability). A custom check uses a [task](https://docs.cloud.google.com/deploy/docs/tasks) to specify the container that includes the custom behavior, and the command or commands to run on that container.

Configuration for a custom analysis is as follows:
    
    
    analysis:
      duration: DURATION
      customChecks:
      - id: CHECK_ID
        frequency: FREQUENCY
        task:
          type: container
          image: IMAGE_NAME
          command: [COMMAND]
          args: [ARGS]
          env:
            [VAR: VALUE]
    

  * `DURATION` is the amount of time, in seconds, minutes, or hours, to run the analysis. After this time expires, the analysis is no longer affected by incoming telemetry from your monitoring system. For example: `200s`.

  * `CHECK_ID` is a unique ID you provide for the alert policy check. This is displayed in the results of the analysis, for each check.

  * `FREQUENCY` specifies how often, in seconds, minutes, or hours, to run the check. For example, `300s`.

  * `IMAGE_NAME` is the path to the container image in an image repository.

  * `COMMAND` is the entrypoint to run on that container. "`/bin/sh`" is a typical command to specify here, to invoke a shell, and you would include the command or commands to run in that shell in the args.

  * `ARGS` is a list of arguments to provide to the command. If your `COMMAND` is "`/bin/sh`", then one of the arguments here would be "`-c`", and another argument would be the entire command you want to run in the shell you're invoking.

## What's next

  * Find out more about [how Cloud Deploy works](https://docs.cloud.google.com/deploy/docs/overview).

  * Learn how to [set up a delivery pipeline for your application](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets).

  * Learn how to [manage your manifests](https://docs.cloud.google.com/deploy/docs/skaffold).

  * Avoid mismatches between your release and your delivery pipeline by learning about [pipeline instances](https://docs.cloud.google.com/deploy/docs/pipeline-instances).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
