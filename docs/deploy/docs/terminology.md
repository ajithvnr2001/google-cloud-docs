---
url: https://docs.cloud.google.com/deploy/docs/terminology/
title: Cloud Deploy Terminology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:33.328457+00:00
---

# Cloud Deploy Terminology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/terminology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Cloud Deploy Terminology Stay organized with collections  Save and categorize content based on your preferences. 

The terms in this document are defined according to how they're used in Cloud Deploy.

## Abandon

To [permanently deactivate a release](https://docs.cloud.google.com/deploy/docs/abandon-release).

## Analysis

A Cloud Deploy feature that lets you [check your newly deployed application](https://docs.cloud.google.com/deploy/docs/analysis) against a set of defined metrics or conditions using Google Cloud Observability or another metrics provider.

## Application

The software you are going to deploy using Cloud Deploy.

## Application delivery

Delivery of the assets necessary to deploy an application into an intended target environment. In Cloud Deploy, application delivery consists of generating, promoting, and delivering your application's Kubernetes manifests into the cluster.

## Artifact

The container images to be deployed (build artifacts), and configuration files, such as manifests and Skaffold configs, that are used for the deployment (target artifacts).

## Automation

Automation lets you configure your delivery pipeline and targets so that some actions can be performed on releases and rollouts for that pipeline, without requiring human intervention. For example, you can set up your delivery pipeline so that promotion into a specific target happens automatically, under the right circumstances. [Learn more](https://docs.cloud.google.com/deploy/docs/automation).

## Automation rule

The behavior of an [automation](https://docs.cloud.google.com/deploy/docs/automation) is defined in part by the automation rule. An automation rule defines what is automated, for example, promoting a release.

The available automation rules are listed in the document [Using automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules).

## Automation run

An instance of an Automation.

## Canary deployment

A deployment strategy in which you roll out your changes to a subset of users first, test it to ensure reliability, then roll it out fully.

## Child rollout

For Parallel deployment, the rollout generated to deploy to a child target.

See also, Controller rollout.

## Child target

For Parallel deployment, a target that represents one of the multiple GKE, GKE attached clusters, or Cloud Run individual targets you're deploying to simultaneously.

See also, Multi-target, Parallel deployment, Child rollout.

## Continuous delivery

A software engineering [practice](https://docs.cloud.google.com/solutions/devops/devops-tech-continuous-delivery) in which changes can be released to users safely, frequently, and mostly automatically.

## Continuous deployment

A software engineering practice that results in changes to code and configuration being deployed automatically.

Whereas continuous _delivery_ requires manual approval at one or more stages, continuous deployment is automatic, with no manual approval required.

## Controller rollout

A rollout generated for parallel deployment. The controller rollout isn't used to deploy to a single target cluster or service; rather, it has one child rollout for each child target.

See also, Parallel deployment, Multi-target.

## Custom target

A target that uses a user-defined [custom target type](https://docs.cloud.google.com/deploy/docs/custom-targets) rather than one of the [supported target types](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#define_the_delivery_pipeline_and_targets).

## Declarative

Configuration for a system, such as a Kubernetes cluster, that describes the intended state and relies on that system to achieve that state. Contrast with imperative configuration, in which you describe the specific steps to achieve that state.

Besides rendering and deploying declarative Kubernetes manifests, Cloud Deploy uses declarative resource definitions to define the rendering and delivery process. `skaffold.yaml` and `clouddeploy.yaml` are typical filenames for the Skaffold definition and delivery-pipeline definition.

## Delivery pipeline

A representation of the workflow that delivers an application to each target in a deployment progression.

Documentation for Cloud Deploy uses the term "_delivery_ pipeline" to distinguish it from other pipelines you might use, such as a CI pipeline.

In Cloud Deploy, the delivery pipeline is defined in a YAML configuration file—typically `clouddeploy.yaml`—and that definition consists of the following:

  * Deployment targets
  * The promotion sequence among those targets

**Note:** you can define targets in a separate file.

See also Pipeline instance.

## Deploy hook

An arbitrary [action](https://docs.cloud.google.com/deploy/docs/hooks#configure_in_skaffold) you can run before or after deploying. [Learn more](https://docs.cloud.google.com/deploy/docs/hooks).

## Deploy parameters

Placeholders that can be added to a manifest but that are not resolved as part of rendering. Instead, values for these placeholders are assigned after each target-specific manifest is rendered. [Learn more](https://docs.cloud.google.com/deploy/docs/parameters).

## Deployment strategy

A technique for safely deploying changes to your application while minimizing impact to users.

## Execution environment

A set of Google Cloud resources on which Cloud Deploy runs. It consists of the following:

  * The default or private [worker pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) in which Cloud Deploy executes rendering and deploying actions

  * The default or alternate [execution environment](https://docs.cloud.google.com/deploy/docs/execution-environment) service account that calls Cloud Deploy to perform rendering and deploying

  * The default or alternate storage location for rendered manifests in Cloud Storage.




## Hydrating

See Render.

## Job

A specific operation to be performed on a rollout, such as deploy or verify. [Learn more](https://docs.cloud.google.com/deploy/docs/verify-deployment).

## Job run

A child resource of a rollout, the job run is an instance of a job. That is, it represents an attempt to perform a job such as deploy or verify. [Learn more](https://docs.cloud.google.com/deploy/docs/verify-deployment).

## Manifest

A Kubernetes configuration object that is used to create, modify, and delete Kubernetes resources such as pods, deployments, services, or ingresses.

Manifests in Cloud Deploy exist in one of two states: rendered or unrendered. An unrendered manifest is not ready for deployment into a target. The rendering process, which includes populating specific values into the manifest, is often performed by tools like Helm, Kustomize, and kpt. Cloud Deploy uses Skaffold to orchestrate the rendering of configuration (the [`skaffold render`](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment) command).

See also, Render.

## Multi-target

When configuring or performing a parallel deployment, a multi-target is a single pipeline stage, but can consist of more than one runtime environment.

See also, Child target, Parallel deployment, Controller rollout.

## Parallel deployment

The practice of deploying an application to more than one target at the same time, in the same delivery pipeline stage. This technique allows you to deploy to multiple clusters or services in production, for example.

## Phase

The collection of operations (jobs) in a rollout that are logically grouped together, for example a deploy or a deploy and verify. [Learn more](https://docs.cloud.google.com/deploy/docs/verify-deployment).

## Pipeline

See Delivery pipeline

## Pipeline instance

A snapshot of a delivery pipeline, taken when a `release` is created. Cloud Deploy keeps this snapshot to ensure that all deployments of a release are consistently managed using the pipeline as it was defined when the `release` was created.

See [Pipeline instances per release](https://docs.cloud.google.com/deploy/docs/pipeline-instances) for more information.

## Pipeline mismatch

When a delivery pipeline or target is changed after a release is created, the pipeline instance associated with the `release` is now different from the pipeline definition.

If there's a pipeline mismatch, Cloud Deploy prompts you to examine the definitions before you promote a release or attempt a rollback.

See [Pipeline instances per release](https://docs.cloud.google.com/deploy/docs/pipeline-instances) for more information.

## Progression

A configuration, in your delivery pipeline configuration file, that describes a promotion sequence from one target or multi-target to another—for example from `test` to `staging` to `prod`.

## Promotion

The process of advancing a release from one target to another, according to the progression defined in the delivery pipeline.

## Register

To provide an application to the Cloud Deploy service, in the form of a delivery pipeline, so that the application's delivery is managed by the service.

## Release

A Cloud Deploy resource that represents the changes (code, configuration or both) to be deployed.

The release lifecycle is described in the document [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release).

## Render

To prepare a manifest for deployment in the target. Rendering a manifest consists mainly of providing values for the variables in the manifest. Cloud Deploy does this using [`skaffold render`](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment).

## Rollout

A resource that associates a release with a deployment target. A `rollout` is created per release per target, so in a simple progression across three targets in a delivery pipeline, there would be three `rollout` resources for the release—one for each target.

For more complex deployments, for example using a canary deployment strategy, a `rollout` can be more complicated. [Learn more](https://docs.cloud.google.com/deploy/docs/deployment-strategies#structure_of_a_rollout).

## Standard deployment strategy

The standard deployment strategy is the default way of deploying an application to a target. For each stage defined in the delivery pipeline, your application is deployed fully to the target, each time replacing the application as it was previously deployed.

## Stage

One target or multi-target in a delivery pipeline. For example, in a simple delivery pipeline that has the following stages:

  * `dev`
  * `staging`
  * `prod`



Each of those is one stage. 

When performing parallel deployment, the [multi-target](https://docs.cloud.google.com/deploy/docs/parallel) is a single stage, but the child targets are not separate stages.

## Suspend (a delivery pipeline)

To prevent creation and promotion of releases from a given delivery pipeline. For more information, see [Suspending a delivery pipeline](https://docs.cloud.google.com/deploy/docs/suspend-pipeline)

## Target

The specific runtime environment (Kubernetes cluster, Cloud Run service, or other supported runtime) into which to deploy the application. Also, the configuration for that environment.

You can define your targets in your delivery pipeline configuration file, or in a separate file.

Targets must be defined in the same project and region as the delivery pipeline. But the runtimes the targets deploy to can be in different projects and regions.

A target can also be a multi-target or a child target to support parallel deployment.

## Target artifact

A configuration file used for rendering and deploying an application on a target. These include Kubernetes manifest or Cloud Run service definition, Skaffold configuration files, and the rendering source used to create these.

## Task

A way to [configure a custom action](https://docs.cloud.google.com/deploy/docs/tasks) that can be used for pre-deploy and post-deploy [hooks](https://docs.cloud.google.com/deploy/docs/hooks), [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment), deploy [analysis](https://docs.cloud.google.com/deploy/docs/analysis), or a [custom target type](https://docs.cloud.google.com/deploy/docs/custom-targets).

## Verification

The ability to confirm that a deployment was successful, by running an arbitrary container, with tests. [Learn more about deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
