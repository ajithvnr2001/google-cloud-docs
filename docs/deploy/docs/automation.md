---
url: https://docs.cloud.google.com/deploy/docs/automation/
title: Automate your deployment \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:00.500930+00:00
---

# Automate your deployment  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/automation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Automate your deployment Stay organized with collections  Save and categorize content based on your preferences. 

This document is an overview of deploy automation.

You can configure Cloud Deploy to automatically perform release-related and rollout-related tasks for a given delivery pipeline. These tasks include [release promotion](https://docs.cloud.google.com/deploy/docs/automation-rules#configuring_a_promoterelease_automation_rule) and [phase advancement](https://docs.cloud.google.com/deploy/docs/automation-rules#configuring_an_advancerollout_automation_rule).

[Learn more](https://docs.cloud.google.com/deploy/docs/automation-resource) about the resources used for release automation in Cloud Deploy.

[Learn more](https://docs.cloud.google.com/deploy/docs/automation-rules) about how to set up the rules that define how these automations work.

## Actions you can automate

In Cloud Deploy, you can automate the following release and rollout activities:

  * [Promote a release automatically](https://docs.cloud.google.com/deploy/docs/automation-rules#promoterelease_rule)

You can configure Cloud Deploy to promote your release automatically, upon a successful rollout to a target. For example, if you have three targets, `dev`, `staging`, and `prod`, you can configure an automation such that the release is promoted to `prod`, without further human interaction, upon a successful deployment into `staging`. You can also specify a delay time.

  * [Promote a release on a schedule](https://docs.cloud.google.com/deploy/docs/automation-rules#timedpromote_rule)

You can configure Cloud Deploy to promote your release according to a cron schedule.

  * [Advance a rollout](https://docs.cloud.google.com/deploy/docs/automation-rules#advancerollout_rule)

You can configure Cloud Deploy to advance a rollout from one [phase](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#phases) to the next, after a successful rollout to the previous target. Phase advancement is available only in targets that use a [canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary).

  * [Repair a rollout](https://docs.cloud.google.com/deploy/docs/automation-rules#repairrollout_rule)

You can configure Cloud Deploy to automatically retry a failed rollout. This includes retrying the rollout a specified number of times, and automatically rolling back if that number of retries fail.




See [Automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules) for more information on these actions, and how to configure them.

## How does automation work?

Each automation is tied to the delivery pipeline for which it's used. You can't share an automation across multiple delivery pipelines.

The following is the general process for configuration and execution of an automation:

  1. You [configure an Automation](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions)

This automation is associated with one delivery pipeline.

  2. You register that automation using `gcloud deploy apply`.

This creates the [Automation resource](https://docs.cloud.google.com/deploy/docs/automation-resource#the_automation_resource).

  3. You invoke the delivery pipeline associated with this automation by [creating a release](https://docs.cloud.google.com/deploy/docs/deploying-application#invoke_your_delivery_pipeline_to_create_a_release).

  4. The rollout succeeds for at least one target, or fails.

If the rollout succeeds, and the automation is `promoteReleaseRule`:

     1. Execution waits for the rollout to succeed into the source target. The source target is the `selector.targets` configured for the automation, not in the `AutomationRule`.

     2. If there is a `wait` time configured, execution waits for that time also.

     3. The release is automatically promoted to the next target in the pipeline progression, or to a specific target, [if indicated](https://docs.cloud.google.com/deploy/docs/automation-rules#promoterelease_rule).

If the rollout succeeds, and the automation is `advanceRolloutRule` and the target uses a canary deployment strategy:

     1. Execution waits for the identified [source phase](https://docs.cloud.google.com/deploy/docs/automation-rules#advancerollout_rule), if there is one.

The `sourcePhase` property is optional, and if no source phases are specified, each phase in the rollout is advanced automatically. The automatic phase advancement happens when the source phase is `IN_PROGRESS`, subject to `wait` time.

     2. If there is a `wait` time configured, execution waits for that time also.

When you're automating a canary deployment, you use this wait time to specify the duration of each canary phase.

     3. The rollout is automatically advanced from that source phase to the next phase in the rollout.

     4. If there's an additional source phase, it's treated the same, including the same wait time, if applicable.

If the rollout fails, and there's an automation with a `repairRollout` rule:

     1. The rollout is retried, after the configured [`wait` time](https://docs.cloud.google.com/deploy/docs/automation-rules#repairrollout_rule), if any.

If specific phases or jobs are configured in this `repairRollout` rule, only those phases or jobs are retried. The default, if no jobs or no phases are specified, is to retry all phases and jobs in the rollout.

Because retries are optional, if your automation isn't configured to retry, then this step doesn't happen.

     2. If the first retry fails, execution waits for the configured `wait` time, then tries again.

     3. Retries are repeated until Cloud Deploy has exhausted the retry [`attempts`](https://docs.cloud.google.com/deploy/docs/automation-rules#repairrollout_rule).

If each attempt fails, and the `attempts` are exhausted, the rollout fails.

During retries, the rollout [state](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#rollout_states) is `IN_PROGRESS` until either the rollout succeeds or fails following the final retry attempt. The phase state is `IN_PROGRESS` during retries, but `FAILED` after each rollout failure.

     4. If all retries fail (or none are configured), a new rollout is created to rollback to the most recent successful release on the target.


**Note:** You can have a maximum of 250 automation rules per delivery pipeline.

### Automation resources

There are two Cloud Deploy resources that are specifically for automation:

  * Automation

An `Automation` is a child resource of a delivery pipeline, and it includes the following information:

    * A pointer to the target or targets for which the automation is used
    * The rule or rules that govern what the automation does and how it does it

Configuration for the Automation resource is described in the document [About the automation resource](https://docs.cloud.google.com/deploy/docs/automation-resource).

When you run `gcloud deploy apply` against a file that includes an automation configuration (`kind: Automation`), Cloud Deploy creates an [automation resource](https://docs.cloud.google.com/deploy/docs/automation-resource#the_automation_resource), which associates a delivery pipeline and a target or targets with one or more [automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules).

  * Automation run

The `AutomationRun` is an instance of an automation. It's a pointer to its corresponding Automation resource, plus information about the rollout that spawned it, and other metadata.

The automation run is created when an automation is triggered.




[Learn more about automation resources](https://docs.cloud.google.com/deploy/docs/automation-resource).

### Automation rules

An automation rule defines an action that can be taken on your delivery pipeline automatically, as well as details about how the automation is to be performed.

[Learn more about automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules).

### Identity and Access Management roles and permissions required

In addition to the permissions you need to run any Cloud Deploy delivery pipeline, and to perform the tasks to be automated (like advancing a rollout), there are several permissions that are needed in order to perform certain operations on the `Automation` and `AutomationRun` resources:

  * `clouddeploy.automations.create`
  * `clouddeploy.automations.delete`
  * `clouddeploy.automations.get`
  * `clouddeploy.automations.list`
  * `clouddeploy.automations.update`
  * `clouddeploy.automationRuns.cancel`
  * `clouddeploy.automationRuns.get`
  * `clouddeploy.automationRuns.list`



In addition to these permissions, each automation rule might require further permissions to perform the automated operation. See [Configure automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules#configure_automation_rules) for the specific permissions needed per automation rule.

See [IAM roles and permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions) For more information, including which Cloud Deploy [roles include these permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#predefined_roles).

## Create an automation

You can create an automation, including using any of the [available automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules#available_automation_rules), by configuring an automation, then creating the automation resource using `gcloud deploy apply`

See the following section (Configuring automation), and [Configuring automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules#configuring_automation_rules).

### Configuring automation

See the [Configuration file schema](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions) for details on how to configure the [`Automation` resource](https://docs.cloud.google.com/deploy/docs/automation-resource#the_automation_resource).

### Automation rule configuration

In addition to this automation configuration, you specify [automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules). Configuration is different for each of the available rules.

See [Using automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules) for descriptions of each of the available rules.

## Suspend an automation

You can suspend an existing resource without deleting it. This can be useful for testing an automation without affecting the delivery pipeline. When you suspend an automation, the automation isn't run, but [platform logs](https://docs.cloud.google.com/deploy/docs/platform-logs) are still generated.

  1. In the [`Automation` configuration](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions), Update the `suspended` property to `true`.

  2. Run `gcloud deploy apply` against that configuration file.

  3. [Platform logs](https://docs.cloud.google.com/sdeploy/docs/platform-logs) are still generated when the automation is instantiated, even if it's suspended. You can use this to test and debug the automation without affecting the delivery pipeline.




## What's next

  * Try the [quickstart: Automate release creation and rollout advancement](https://docs.cloud.google.com/deploy/docs/deploy-app-automation).

  * [Learn more](https://docs.cloud.google.com/deploy/docs/automation-rules) about Cloud Deploy automation rules.

  * [Learn more](https://docs.cloud.google.com/deploy/docs/automation-resource) about Cloud Deploy automation resources.

  * See the [configuration file schema documentation](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions) for details on the automation configuration files.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
