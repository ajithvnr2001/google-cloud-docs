---
url: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/custom/
title: Custom Canary Deployments \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:07.069323+00:00
---

# Custom Canary Deployments  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/custom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Custom Canary Deployments Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure and use custom canary deployments to deploy your applications to [all target types](https://docs.cloud.google.com/deploy/docs/deploying-application#set_up_for_the_runtime_environment_of_your_choice) using Cloud Deploy.

## How custom canary deployments work

When you deploy using a custom canary deployment strategy, Cloud Deploy does not modify your manifests in order to facilitate the chosen traffic-balancing configuration. Instead you are responsible for providing manifests that are applied to your target runtime for each canary phase.

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

Your `skaffold.yaml` file defines how your manifests are rendered and deployed. For a custom canary deployment you are responsible for defining profiles that are associated with each canary phase in order to facilitate the chosen traffic-balancing configuration. These profiles are mapped to phases in the delivery pipeline strategy configuration.

The following is an example `skaffold.yaml` configuration used by a custom canary:
    
    
    apiVersion: skaffold/v4beta7
    kind: Config
    profiles:
    - name: canary-25
      manifests:
        rawYaml:
        - canary-25-resources.yaml
    - name: canary-50
      manifests:
        rawYaml:
        - canary-50-resources.yaml
    - name: stable
      manifests:
        rawYaml:
        - stable-resources.yaml
    

### Configure a custom canary

With custom canary configuration, you specify the following, in your delivery pipeline definition:

  * Rollout phase names

In a fully-automated canary, Cloud Deploy names the phases for you (`canary-25`, `canary-75`, `stable`, for example). With a custom canary, however, you can give each phase any name, as long as it's unique among all phases for this canary stage, and it honors [resource ID restrictions](https://docs.cloud.google.com/apis/design/resource_names#resource-id-segments). But the final (100%) phase name must be `stable`.

  * Percentage goals for each phase

Specify the percentages separately, per phase.

  * Skaffold profiles to use for the phase

You can use a separate Skaffold profile for each phase, or the same profile, or any combination. And each profile can use a different Cloud Run service definition. You can also use more than one profile for a given phase. Cloud Deploy combines them.

  * Whether there is a [verify job](https://docs.cloud.google.com/deploy/docs/verify-deployment) for the phase

  * Whether there are [predeploy or postdeploy jobs](https://docs.cloud.google.com/deploy/docs/hooks) for the phase




#### Custom canary configuration elements

The following YAML shows the configuration for the phases of fully custom canary deployment:
    
    
    strategy:
      canary:
        # Custom configuration for each canary phase
        customCanaryDeployment:
          phaseConfigs:
          - phaseId: "PHASE1_NAME"
            percentage: PERCENTAGE1
            profiles: [ "PROFILE_NAME" ]
            verify:
              tasks: [TASKS]
            predeploy:
              tasks: [TASKS]
            postdeploy:
              tasks: [TASKS]
          - …
          - phaseId: "stable"
            percentage: 100
            profiles: [ "LAST_PROFILE_NAME" ]
            verify:
              tasks: [TASKS]
            predeploy:
              tasks: [TASKS]
            postdeploy:
              tasks: [TASKS]
    

In this YAML

  * `PHASE1_NAME`

Is the name of the phase. Each phase name must be unique.

  * `[ "PROFILE_NAME" ]`

Is the name of the profile to use for the phase. You can use the same profile for each phase, or a different one for each, or any combination. Also, you can specify more than one profile. Cloud Deploy uses all of the profiles you specify, _plus_ the profile or manifest used by the overall stage.

  * `stable`

The final phase must be named `stable`.

  * `PERCENTAGE1`

Is the percentage to deploy for the first phase. Each phase must have a unique percentage value, and that value must be a whole percentage (not `10.5`, for example), and the phases must be in ascending order.

  * You can enable [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) by configuring the `verify` stanza. If you do so, a `verify` job is added to the phase.

  * You can enable [predeploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) by configuring the `predeploy` stanza. If you do so, a `predeploy` job is added to the phase.

  * You can enable [postdeploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) by configuring the `postdeploy` stanza. If you do so, a `postdeploy` job is added to the phase.

  * The `tasks` property under `verify`, `predeploy` and `postdeploy` consists of one or more [tasks](https://docs.cloud.google.com/deploy/docs/tasks) to run as part of that job. Any configured tasks will run sequentially in the order they are defined.




The percentage for the last phase must be `100`. Phases are executed according in the order you configure them in this `customCanaryDeployment` stanza, but if the percentage values are not in ascending order, the command to [register the delivery pipeline](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets) fails with an error.

Note that the configuration for a custom canary doesn't include a `runtimeConfig` stanza. If you include `runtimeConfig`, it's considered a [custom-automated canary](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#types_of_canary).

## What's next

  * Try the [canary deployment quickstart](https://docs.cloud.google.com/deploy/docs/deploy-app-canary).

  * Find out how to [manage the lifecycle of your canary's rollouts](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout).

  * Learn more about [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel).

  * Learn more about [Cloud Deploy deployment strategies](https://docs.cloud.google.com/deploy/docs/deployment-strategies).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
