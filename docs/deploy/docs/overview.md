---
url: https://docs.cloud.google.com/deploy/docs/overview/
title: Overview of Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:58.892278+00:00
---

# Overview of Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Overview of Cloud Deploy Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Deploy is a managed service that automates delivery of your applications to a series of [target](https://docs.cloud.google.com/deploy/docs/terminology#target) environments in a defined promotion sequence. When you want to deploy your updated application, you create a [release](https://docs.cloud.google.com/deploy/docs/terminology#release), whose [lifecycle](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release) is managed by a [delivery pipeline](https://docs.cloud.google.com/deploy/docs/terminology#delivery_pipeline).

## How a Cloud Deploy pipeline works

The Cloud Deploy delivery pipeline contains the following information:

  * A name, which you use when referring to the delivery pipeline, and a description.

  * The promotion sequence, describing the order in which to deploy to the configured [targets](https://docs.cloud.google.com/deploy/docs/terminology#target).

  * Optionally, [labels and annotations](https://docs.cloud.google.com/deploy/docs/labels-annotations).

  * Also optionally, the target definitions themselves.




Targets can be [defined](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions) in the same delivery pipeline [configuration file](https://docs.cloud.google.com/deploy/docs/config-files), or in one or more separate files. Multiple delivery pipelines can use the same target or targets, but a given target can be used only once in a given delivery pipeline.

### The Cloud Deploy delivery process

The following is a description of a Cloud Deploy continuous delivery scenario.

  1. You define your [delivery pipeline](https://docs.cloud.google.com/deploy/docs/terminology#delivery_pipeline) in a [YAML configuration file](https://docs.cloud.google.com/deploy/docs/config-files#structure_of_a_delivery_pipeline_configuration_file).

This configuration file defines the promotion sequence in which to deploy your application to a series of [targets](https://docs.cloud.google.com/deploy/docs/terminology#target).

You also need a [configuration](https://skaffold.dev/docs/references/yaml/) for [Skaffold](https://cloud.google.com/skaffold), which Cloud Deploy needs in order to perform render and deploy operations.

  2. You define your targets, either in the pipeline configuration file or in a separate file or files.

  3. You register your pipeline with the Cloud Deploy service.

Now that the service knows about your application, it manages the deployment to targets according to your defined promotion sequence.

  4. The output of your CI process includes a call to Cloud Deploy to initiate your delivery pipeline.

This call creates a `release` resource, representing the rendered manifest for each target, each of which is generated using the provided rendering source, skaffold.yaml, and references to specific container images to deploy. For this first call to create a [release](https://docs.cloud.google.com/deploy/docs/terminology#release), Cloud Deploy automatically creates a [`rollout`](https://docs.cloud.google.com/deploy/docs/terminology#rollout) resource, which associates the release with the first target environment. Based on that rollout, your application is deployed to the first target.

You can use any CI tool as long as it outputs one or more container images to provide to your Cloud Deploy delivery pipeline.

Furthermore, the call to create a release and invoke a delivery pipeline doesn't have to come from the CI tool. It can come from a script or any system responding to the completion of the CI process.

  5. When you're ready to deploy your application to the next target, you call Cloud Deploy to promote it.

In each case, the call to invoke the promotion causes Cloud Deploy to create a new rollout.

  6. Promotion continues through all targets in your promotion sequence, the last of which is `prod` (or whatever name you use for your final target to put the application into production).

The process of release creation and promotion is described in more detail in [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release).




Throughout pipeline execution, Cloud Deploy collects metrics and [audit](https://docs.cloud.google.com/deploy/docs/audit-logs) details.

### Promotion

To [promote a release](https://docs.cloud.google.com/deploy/docs/promote-release) is to deploy it to the next target in the promotion sequence defined in your pipeline. The first call to Cloud Deploy creates a `release`, then a `rollout` resource that's used to deploy to the first target in the promotion sequence. Each subsequent call to promote the release results in a rollout to the next target.

### Approvals

You can specify that an approval is needed for promotion to any target. For example, you might want to require approval for promotion into a production target. To require approval for a target, set the `requireApproval` property in the [target definition](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions).

When a target requires approval, Cloud Deploy generates a Pub/Sub message that can be consumed by an integrated system. For example, a ticketing system could subscribe to the message to kick off an approval workflow.

See [Require approval](https://docs.cloud.google.com/deploy/docs/promote-release#require_approval) for more information on promotions and managing approval for promotions.

### Notifications

Cloud Deploy provides Pub/Sub notifications for the following events:

  * Render: start, success, and failure
  * Deploy: start, success, and failure
  * Approval required
  * Approval approved
  * Approval rejected



Cloud Deploy uses a Pub/Sub topic to send these notifications.

See [Using Cloud Deploy notifications](https://docs.cloud.google.com/deploy/docs/subscribe-deploy-notifications) for more details.

### Rollbacks

Cloud Deploy supports rolling back your deployed application in any target. A rollback in Cloud Deploy consists of triggering a rollout against the last successfully deployed release. The new rollout uses the same parameters that were used in that successful deployment.

See [Rolling back a deployment](https://docs.cloud.google.com/deploy/docs/roll-back) for more details.

## About Skaffold and Cloud Deploy

Cloud Deploy uses [Skaffold](https://cloud.google.com/skaffold) for rendering, deployment, and verification. With Skaffold, you can also connect your local development loop to a Cloud Deploy continuous delivery pipeline.

To learn more about how Cloud Deploy integrates with Skaffold, see the [Skaffold overview](https://docs.cloud.google.com/deploy/docs/using-skaffold).

## Cloud Deploy with other Google Cloud tools

Cloud Deploy supports almost any tool upstream in a CI/CD pipeline. That is, you can use any development environment and source code repository, any continuous integration (CI) system, and any artifact repository.

Downstream, Cloud Deploy deploys to Cloud Run and Google Kubernetes Engine, including GKE attached clusters.

If you used mostly Google Cloud tools, your source-to-prod flow would look like this:

  1. Use [Cloud Code](https://docs.cloud.google.com/code/docs) to create your application source.

Cloud Code extends several popular IDEs (VS Code, IntelliJ, Cloud Shell) to make it easier to build applications to deploy and run on Google Cloud.

  2. Use [Skaffold](https://skaffold.dev) to manage your local development loop.

Cloud Deploy uses Skaffold, through Cloud Build, to render and deploy your manifests. This integration means that you need to maintain a `skaffold.yaml` file, but does not otherwise mean you need to make Skaffold part of your local development flow. But you can take advantage of it for [continuous development](https://skaffold.dev/docs/workflows/dev/).

  3. Build your application using Cloud Build.

[Cloud Build](https://docs.cloud.google.com/build/docs) lets you set up a CI pipeline that can be triggered from a commit to your source code repository. The output from Cloud Build will be artifacts including deployable container images. You can add a call to Cloud Deploy to create a release and invoke your delivery pipeline.

  4. Store your artifacts in Artifact Registry.

Cloud Deploy retrieves the container image or images from [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs), which lets you centrally store artifacts and dependencies.

  5. Configure your delivery pipeline in Cloud Deploy to take the container image and deploy it in a progression of _n_ targets.

Targets identified in your delivery pipeline represent GKE clusters, Cloud Run services or jobs, or GKE attached clusters where your application is ultimately deployed.

  6. Manage your application on GKE or Cloud Run.

[GKE](https://docs.cloud.google.com/kubernetes-engine/docs) is the Google Cloud managed environment for running containerized applications on Kubernetes.

With [Cloud Run](https://docs.cloud.google.com/run/docs), you can run containers in a serverless environment.

[GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached) provide a consistent development and operations experience for cloud and on-premises environments.

  7. Monitor the performance of your application using Google Cloud Observability.

[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) offers integrated monitoring and logging for your application.




## What's next

  * For a quick-and-easy look at how to create a delivery pipeline and use it to deploy an application, try the [quickstarts](https://docs.cloud.google.com/deploy/docs/quickstarts).

  * Try out one of the [Cloud Deploy walkthroughs](https://docs.cloud.google.com/deploy/docs/tutorials).

  * Learn more about [how Cloud Deploy components work together](https://docs.cloud.google.com/deploy/docs/architecture).

  * Review [Google Cloud Well-Architected Framework: Operational excellence](https://docs.cloud.google.com/architecture/framework/operational-excellence) for articles on how to use the principles of operational excellence to build an automated delivery foundation.

  * [Learn how to combine Google Cloud CI/CD tools to develop and deliver software effectively to GKE](https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
