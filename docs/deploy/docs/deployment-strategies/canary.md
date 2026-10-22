---
url: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/
title: Use a canary deployment strategy \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:20.515574+00:00
---

# Use a canary deployment strategy  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Use a canary deployment strategy Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure and use a canary deployment strategy.

## What is a canary deployment?

A canary deployment is a progressive rollout of an application that splits traffic between an already-deployed version and a new version, rolling it out to a subset of users before rolling out fully.

### Supported target types

Canary deployment in Cloud Deploy supports all target types, including the following:

  * Google Kubernetes Engine and GKE attached clusters

    * [Using service networking](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking)
    * [Using Gateway API](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api)
  * [Cloud Run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run) (services and worker pools—not jobs)




Canary also works with [multi-targets](https://docs.cloud.google.com/deploy/docs/terminology#multi-target).

### Why use a canary deployment strategy?

A canary deployment gives you a chance to partially release your application. In this way, you can ensure the new version of your application is reliable before you deliver it to all users.

If you're deploying to GKE (or GKE attached clusters) for example, you would deploy the new version of your application to a limited number of pods. The old version would continue to run, but with more of the traffic being sent to the new pods.

If you're deploying to Cloud Run, Cloud Run itself splits traffic between the old and new revisions, according to the percentages you configure.

### Types of canary

Cloud Deploy lets you configure the following types of canary deployment:

  * Automated

With an automated canary deployment (for [service networking](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking#configure_an_automated_canary), [gateway api](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api#configure_an_automated_canary) or [Cloud Run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run-canary#configure_an_automated_canary)), you configure Cloud Deploy with a series of percentages that express a progressive deployment. Cloud Deploy performs additional operations on your behalf, to apportion traffic percentages between the old and new versions.

  * Custom-automated

For a custom-automated canary (for [service networking](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking#custom-automated), [gateway api](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api#custom-automated) or [Cloud Run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run-canary#custom-automated)), you can provide the following:

    * The phase name
    * The percentage goal
    * The Skaffold profile to use for the phase
    * Whether or not to include a verify job
    * Whether or not to include a predeploy or postdeploy job, or both

But you don't need to provide traffic-balancing information; Cloud Deploy creates the necessary resources (for [service networking](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking#what_happens_during_an_automated_or_custom-automated_canary), [gateway api](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api#what_happens_during_an_automated_or_custom-automated_canary) or [Cloud Run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run-canary#what_happens_during_an_automated_or_custom-automated_canary)).

  * Custom

With a [custom canary](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/custom), you configure each canary phase separately, including the following:

    * The phase name
    * The percentage goal
    * The Skaffold profile to use for the phase
    * Whether or not to include a verify job
    * Whether or not to include a predeploy or postdeploy job, or both

Additionally for a fully custom canary, you provide all of the traffic-balancing configuration.

[All target types](https://docs.cloud.google.com/deploy/docs/deploying-application#set_up_for_the_runtime_environment_of_your_choice) are supported for custom canary.




### Phases of a canary deployment

When you create a release for a canary deployment, the rollout is created with a phase for each canary increment, plus a final `stable` phase for 100%.

For example, if you configure a canary for 25%, 50%, and 75% increments, the rollout will have the following phases:

  * `canary-25`
  * `canary-50`
  * `canary-75`
  * `stable`

**Note:** For a [GKE, Gateway API configuration](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api), 100% is allowed. This supports a 100% deployment from canary before switching over to `stable`. The 100% configuration is not allowed for GKE service-based canary, GKE attached clusters, or Cloud Run.

You can read more about rollout phases, jobs, and job runs in [Manage rollouts](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout).

## Use parallel deployment with a canary deployment strategy

You can run a canary deployment using [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel). This means the target you're progressively deploying to can comprise two or more child targets. For example, you can deploy progressively to clusters in separate regions, at the same time.

### How is a parallel canary different from single-target canaries

  * As with single-target canary deployment, if you're deploying to GKE targets, you need a Kubernetes Deployment configuration and a Kubernetes Service configuration in your manifest.

  * As with single-target canary deployment, your delivery pipeline configuration must include a `strategy.canary` stanza inside the stage definition for the applicable stage.

  * Additionally, you need to [configure a multi-target](https://docs.cloud.google.com/deploy/docs/parallel#configure_the_multi-target), and you need to [configure the child targets](https://docs.cloud.google.com/deploy/docs/parallel#configure_the_child_targets) which that multi-target references.

  * When you create a release, a [controller rollout](https://docs.cloud.google.com/deploy/docs/terminology#controller_rollout) and the [child rollouts](https://docs.cloud.google.com/deploy/docs/terminology#child_rollout) are created.

Both types of rollout—controller and child—have separate phases for all of the configured canary percentages, and a `stable` phase for the canary 100%.

  * You can't [advance](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#advance_rollout) a child rollout.

You can advance controller rollouts only. When you advance the controller rollout to the next stage, the child rollouts are advanced too, by Cloud Deploy.

  * You can't [retry](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#retry_failed_job) failed jobs in the controller rollout.

You can retry a job in child rollouts only.

  * You can't [ignore](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#ignore_job) failed jobs in the controller rollout.

You can ignore failed jobs in child rollouts only.

  * You can [cancel a controller rollout](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#cancel_rollout), but you can't cancel child rollouts.

  * You can [terminate job runs](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#terminate_job_run) under a child rollout only, not a controller rollout.




### What to do if a parallel rollout fails in canary

When a child rollout fails, the controller rollout can transition to different states, depending on what happens with the child rollouts:

  * If one or more child rollouts fail, but at least one child rollout is still `IN_PROGRESS`, the controller rollout remains `IN_PROGRESS`.

  * If one or more child rollouts fail, but at least one child rollout succeeds, the controller rollout is `HALTED` if there are more phases after the current one.

If this is the `stable` phase, the controller rollout is `FAILED`.

`HALTED` gives you a chance to either [ignore](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#ignore_job), [retry](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#retry_failed_job) failed jobs within the failed child rollout, or [cancel the controller rollout](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#cancel_rollout) and prevent further actions on the child rollouts.

  * If the controller rollout is in a `HALTED` state because of a failed child rollout, and you ignore the failed job in the child rollout, the controller rollout reverts to an `IN_PROGRESS` state.




## Use deploy analysis with a canary deployment strategy

In a canary deployment strategy, you can use [deploy analysis](https://docs.cloud.google.com/deploy/docs/analysis) with some or all phases (except `stable`) to help determine when to advance a rollout to the next phase. And you can combine the analysis with an [`advanceRolloutRule`](https://docs.cloud.google.com/deploy/docs/automation-rules#advancerollout_rule) automation so that the rollout advances automatically.

To do so, include an [`analysis`](https://docs.cloud.google.com/deploy/docs/config-files/analysis) stanza inside the configuration for each phase you want to analyze.

This analysis can [use metrics from Google Cloud Observability](https://docs.cloud.google.com/deploy/docs/analysis/cloud-monitoring-analysis) or [from the metrics provider of your choice](https://docs.cloud.google.com/deploy/docs/analysis/custom-analysis).

## What's next

  * Try the [canary deployment quickstart](https://docs.cloud.google.com/deploy/docs/deploy-app-canary).

  * Find out how to [manage the lifecycle of your canary's rollouts](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout).

  * Proceed to the guide relevant to your specific target environment:

    * [Canary Deployments to Cloud Run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run)
    * [Canary Deployments to GKE/GKE Enterprise using Service Networking](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/service-networking)
    * [Canary Deployments to GKE/GKE Enterprise using Gateway API](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
