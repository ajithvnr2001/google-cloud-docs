---
url: https://docs.cloud.google.com/deploy/docs/parallel/
title: Deploy to multiple targets at the same time \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:45.535296+00:00
---

# Deploy to multiple targets at the same time  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/parallel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Deploy to multiple targets at the same time Stay organized with collections  Save and categorize content based on your preferences. 

Using Cloud Deploy, you can deploy to a target that's configured to represent multiple targets, and your application is deployed to those targets in parallel (concurrently). The target you identify as a stage in your pipeline is called a [multi-target](https://docs.cloud.google.com/deploy/docs/terminology#multi-target), and the targets that multi-target comprises are called [child targets](https://docs.cloud.google.com/deploy/docs/terminology#child-target).

You can use parallel deployment with any target type that Cloud Deploy supports.

### Why parallel deployment

You can use parallel deployment, for example, to deploy your application to multiple production targets. In this case, you don't need to deploy to each target in succession, because there's no progression (for example, from dev to staging to production).

And this parallel deployment can be a part of a normal delivery pipeline progression:  
`dev -> staging -> prod [prod1, prod2, prod3, prod4, ...]`.

**Note:** you can use parallel deployment for any stage in your delivery pipeline.

## Cloud Deploy resources used for parallel deployment

Parallel deployment uses the following Cloud Deploy specialized resources:

  * multi-targets

A multi-target is a target that is configured with the property `multiTarget`, at the top level of the target config YAML, and instead of referencing the runtime cluster or service, it references one or more other targets, using `multiTarget.targetIds`.

  * Child targets

A child target is any target referenced by a multi-target as `multiTarget.targetIds`.

  * Controller rollouts

A controller rollout is a rollout that corresponds to the multi-target.

See Limitations for more information about what you can and can't do with a controller rollout.

  * [Child rollouts](https://docs.cloud.google.com/deploy/docs/terminology#child_rollout)

See Limitations for more information about what you can and can't do with a child rollout.




## Set up parallel deployment

Setting up parallel deployment consists of defining one multi-target and the number of child targets you need (up to the limit). Target definitions are the same as for all targets, except for the following:

  * Multi-targets include the `multiTarget` property.
  * Child targets do not include the `multiTarget` property, but are referenced from the multi-target using the `multiTarget.targetIds` property.
  * You can configure the multi-target for approval, but not the child targets, which cannot include `requireApproval:true`.



Multi-targets and child targets can include custom [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment) configs. If a child target doesn't specify an execution environment, it inherits the one defined in the multi-target definition, or the default. See Execution environments and parallel deployment for more details.

### Configure the multi-target

A multi-target is a single target identified as a stage in your delivery pipeline, but pointing to one or more child targets.

The multi-target configuration includes the `multiTarget` property. A multi-target cannot have the `gke` or `run` or `anthosCluster` properties. Configuration for a multi-target is the same regardless of which runtime you're deploying to.

In your delivery pipeline YAML or in a separate YAML file, create the basic target definition, including `multiTarget`:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
     name: TARGET_NAME
    description: TARGET_DESCRIPTION
    multiTarget:
     targetIds: [ CHILD_TARGET1, CHILD_TARGET2, CHILD_TARGETn ]
    

In this YAML...

  * TARGET_NAME is the name of this multi-target, which is used in the [delivery pipeline definition](https://docs.cloud.google.com/deploy/docs/config-files#stages), `stages.targetId` property.

  * CHILD_TARGET1, CHILD_TARGET2,...CHILD_TARGETn are the names of the child targets this multi-target deploys to. Each name corresponds to the `name` property in the child target definition.




The presence of the `multiTarget.targetIds` property makes this target a multi-target.

### Configure the child targets

For each target identified as a child in your multi-target configuration, configure another target, as a child target:

In your [delivery pipeline YAML](https://docs.cloud.google.com/deploy/docs/config-files) or in a separate YAML file, create the basic target definition:

###  GKE 
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
     name: CHILD_TARGET1
    description: TARGET_DESCRIPTION
    gke:
     cluster: projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME
    

In this YAML...

  * CHILD_TARGET1 is the name of this child target. The name corresponds to one member in the list of targets in the `multiTarget.targetIds` property in the multi-target definition.

  * The value of the `gke.cluster` property is the resource name of the cluster this target refers to, including the project ID, the region, and the cluster name.




This target is configured the same as a standard GKE target. The only thing that makes this a child target is that its referenced by the `multiTarget.targetIds` property in the multi-target.

###  Cloud Run 
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
     name: CHILD_TARGET1
    description: TARGET_DESCRIPTION
    run:
     location: projects/PROJECT_ID/locations/REGION
    

In this YAML...

  * CHILD_TARGET1 is the name of this child target. The name corresponds to one member in the list of targets in the `multiTarget.targetIds` property in the multi-target definition.

  * The value of the `run.location` property is the resource name of the Cloud Run service this target refers to, including the project ID and the region.




This target is configured the same as a standard Cloud Run target. The only thing that makes this a child target is that its referenced by the `multiTarget.targetIds` property in the multi-target.

###  GKE attached clusters 
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
     name: CHILD_TARGET1
    description: TARGET_DESCRIPTION
    anthosCluster:
     membership: projects/PROJECT_ID/locations/global/memberships/MEMBERSHIP_NAME
    

In this YAML...

  * CHILD_TARGET1 is the name of this child target. The name corresponds to one member in the list of targets in the `multiTarget.targetIds` property in the multi-target definition.

  * MEMBERSHIP_NAME is the name that you chose when you [registered the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to a fleet.




###  Custom Target 
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: Target
    metadata:
     name: CHILD_TARGET1
    description: TARGET_DESCRIPTION
    customTarget:
      customTargetType: CUSTOM_TARGET_TYPE_NAME
    

In this YAML...

  * CHILD_TARGET1 is the name of this child target. The name corresponds to one member in the list of targets in the `multiTarget.targetIds` property in the multi-target definition.

  * CUSTOM_TARGET_TYPE_NAME is the name of the [custom target type](https://docs.cloud.google.com/deploy/docs/create-custom-target#define_custom_target_type) used by this target.




### Pass deploy parameters to targets

You can differentiate among child targets by including parameters in your manifest and values in your delivery pipeline definition. Those values can be [applied separately](https://docs.cloud.google.com/deploy/docs/parameters#add_to_pipeline_stage) to the separate manifests, based on label matching on the corresponding targets.

For example, you might want a different number of replicas for each child target. To do so, you would include the parameters and values in the delivery pipeline's [progression](https://docs.cloud.google.com/deploy/docs/terminology#progression), along with labels on the child targets to match for each parameter-value pair.

Learn more about [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters).

### Create the release

With a multi-target and child targets configured, [create the delivery pipeline and target resources](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets), and then create a release, as normal.

The lifecycle of the delivery pipeline is the same as with any Cloud Deploy pipeline and targets, except that when it gets to the stage with the multi-target, Cloud Deploy creates a controller rollout for the multi-target and a child rollout to deploy the application to each child target.

Pub/Sub messages in response to Cloud Deploy operations distinguish between controller rollouts and child rollouts.

## Limitations

  * A multi-target can have no more than 100 child targets.

  * All child targets of a single multi-target must have the same target runtime (all GKE or all Cloud Run, for example).

  * Within a delivery pipeline, a child target can have only one parent multi-target.

  * A multi-target can't be childless, and it can't reference itself or another multi-target as child targets.

  * You can't use a child target more than once within a single delivery pipeline, but you can re-use them in different pipeline.

  * If the child targets are [Custom Targets](https://docs.cloud.google.com/deploy/docs/custom-targets), they must all reference the same `CustomTargetType`.

  * [Default pools](https://docs.cloud.google.com/deploy/docs/execution-environment#about_worker_pools) have concurrency limits, but private pools don't.

When you deploy to a multi-target, all child rollouts are deployed at the same time, up to the Cloud Build concurrency limit. If you have more child targets than that limit, the deploy jobs for some targets won't run until others finish, which means that Cloud Deploy doesn't deploy to all child targets at the same time, in this case.

Additionally, if the targets include [verify jobs](https://docs.cloud.google.com/deploy/docs/verify-deployment), it's possible for one or more of those verify jobs to start before the application has been deployed to all child targets.

If you need to be able to deploy concurrently to more targets than the limit specified in the [Cloud Build documentation](https://docs.cloud.google.com/build/quotas#quotas), you have two options:

    * [Request an increase](https://docs.cloud.google.com/build/quotas#increasing_quota) of the number of concurrent builds you can run.

    * [Set up a private pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) and [configure your targets to use that pool](https://docs.cloud.google.com/docs/execution-environment#changing_from_the_default_pool_to_a_private_pool).




## Execution environments and parallel deployment

Each target can be configured to use a non-default execution environment.

  * If the multi-target has a non-default execution environment, all child targets using the default execution environment, inherit the non-default one from the multi-target

  * If the multi-target uses the default execution environment, any child target that is configured with a non-default execution environment uses that non-default one.




These rules make it easier to propagate execution environments to child targets from a multi-target, so you don't have to define or change the execution environment for each child target, while still allowing you to customize the execution environment for one or more child targets if you need to do so.

See [Using Cloud Deploy execution environments](https://docs.cloud.google.com/deploy/docs/execution-environment) for more information about execution environments in Cloud Deploy.

## Roll back a parallel deployment

If you need to roll back a deployment from multiple, parallel targets, Roll back the multi-target, as described in [Roll back a target](https://docs.cloud.google.com/deploy/docs/roll-back).

## Approvals for parallel deployment

As with any targets, you can configure your parallel deployment to require [approvals](https://docs.cloud.google.com/deploy/docs/promote-release#manage_approvals_for_a_delivery_pipeline). With parallel deployment, however, you can only configure approval on the multi-target. The approval or rejection affects all child targets together.

## View parallel deployment in Google Cloud console

You can view details for your multi-target, child targets, the controller rollout, and child rollouts in Google Cloud console.

When you view the list of targets for a given delivery pipeline, in the Delivery Pipeline Details, the multi-target is listed, but child targets aren't. When you view release details, however, you can see the controller rollout and the child rollouts. You can also see controller and child rollouts listed on the **Rollouts** tab on the Delivery Pipeline details page.

In the [release inspector](https://docs.cloud.google.com/deploy/docs/view-release), you can view, and diff, rendered manifests for child rollouts.

## Use parallel deployment with a deployment strategy

You can deploy in parallel when you're using a [canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary). See [Use parallel deployment with a canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#parallel_canary) for more information.

## What's next

  * Try the [quickstart: Deploy an app to multiple targets at the same time](https://docs.cloud.google.com/deploy/docs/deploy-app-parallel).

  * Learn more about [using deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters).

  * See the [target configuration schema](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions).

  * Review the article [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
