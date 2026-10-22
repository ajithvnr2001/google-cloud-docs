---
url: https://docs.cloud.google.com/deploy/docs/automation-rules/
title: Using automation rules \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:50.050500+00:00
---

# Using automation rules  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/automation-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Using automation rules Stay organized with collections  Save and categorize content based on your preferences. 

This document describes automation rules, which are actions that can be taken on your delivery pipeline automatically. For example, you can configure your delivery pipeline so that promotion into a specific target happens automatically, under the right circumstances.

You can only use automation rules that are built into Cloud Deploy. The available automation rules are listed in this document.

**Note:** You can have a maximum of 250 automation rules per delivery pipeline.

## Available automation rules

The following automation rules are available in Cloud Deploy:

Rule | Description  
---|---  
`timedPromoteReleaseRule` | Automatically promote from one target to the next  based on a cron schedule.  
`promoteReleaseRule` | Automatically promotes a release into the indicated target after successful rollout in the previous target in the progression.  
`advanceRolloutRule` | Automatically advances a rollout from the indicated [phase](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#phases) to the next phase.  
`repairRolloutRule` | Automatically retry the failed job or jobs in the rollout a  specified number of times, and roll back if all retries fail.  
  
## Configure automation rules

Configuration for each automation rule depends on the specific rule. This section describes configuration that all rules have in common, as well as how to configure each of the available rules.

Each automation rule is configured as part of the configuration for the [automation resource](https://docs.cloud.google.com/deploy/docs/automation-resource). This can be inside the same file as configuration for the relevant delivery pipeline (usually called `clouddeploy.yaml`) or in any file you want. Learn more about [configuring automations](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions).

The following sections describe configuration specific to individual automation rules. See [Automate your deployment](https://docs.cloud.google.com/deploy/docs/automation#create_automation) for configuration of the automation itself.

### Configure a `timedPromoteReleaseRule` automation rule

The `timedPromoteReleaseRule` rule lets you schedule when to promote a release from the selected target or targets to the next target in the progression, or to a specified target. When you configure a `timedPromoteReleaseRule` automation, you specify when to promote the release, based on a cron schedule.
    
    
    rules:
    - timedPromoteReleaseRule:
        id: "[RULE_ID]"
        schedule: "[CRON]"
        timeZone: "[TIME_ZONE]"
        destinationTargetId: "[TO_TARGET]"
        destinationPhase: "[TO_PHASE]"
    

Where:

  * `[RULE_ID]`

Is any name you want to give to this rule. This name must be unique within the automation resource.

  * `[CRON]`

Is the cron schedule that specifies when to promote the release. Use this schedule to specify the date and time when you want to promote the release.

This schedule uses the standard `cron` syntax:

`* * * * *`

In this schedule...

    * The first position is the minute (`0`-`59`).
    * The second position is the hour (`0`-`23`).
    * The third position is the day of the month (`1`-`31`).
    * The fourth position is the month (`1`-`12`).
    * The fifth position is the day of the week (`0`-`6`, Sunday to Saturday)

For example, if your timed-promote rule includes the following schedule: `0 9 * * 1`, your release is promoted every Monday at 9am.

You can also use standard cron schedule features, such as:

    * A range (`0`-`5`)
    * A list (`1`,`3`,`5`)
    * A step function (for example, `*/3` in the hours field activates every third hour)
  * `[TIME_ZONE]`

Is the time zone you want to use for scheduling the promotion, in IANA format.

  * `[TO_TARGET]`

Is the `targetId` of the target to promote to, or `@next` to promote the release automatically to the next target after the target specified in the `selector.targets property` in this automation config. This is optional; the default is `@next`.

  * `[TO_PHASE]`

Is the phase name of the [phase](https://docs.cloud.google.com/deployment-strategies/manage-rollout#phases) you want to promote to, for example `canary-25` or `stable`. This property is optional; if you omit it, the release is promoted to the first phase in the target.




### Configure a `promoteReleaseRule` automation rule

The `promoteReleaseRule` rule promotes your release after a successful rollout into a target. For example, if you have three targets, you can set up this rule so that when the release is successfully deployed into the first target, it's automatically promoted to the second target.

**Note:** The service account configured in the automation (the "automation service account") must have the `clouddeploy.rollouts.create` permission. The automation service account must have `iam.serviceAccount.actAs` permission to impersonate the Cloud Deploy [execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account). See [IAM roles and permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions) for more information.

When you configure a `promoteReleaseRule` automation, you can specify either a target to promote to (`destinationTargetId`) or `@next`. When the rollout finishes successfully in target specified in the `Automation` definition, the release is then promoted to the target specified in `destinationTargetId`, subject to a `wait` time interval.

You can also promote a release to a specific phase in the intended target, using the `destinationPhase` property. The `rules` stanza shown here goes inside your [automation definition](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions).
    
    
    rules:
    - promoteReleaseRule:
        id: "[RULE_ID]"
        wait: [WAIT_TIME]
        destinationTargetId: "[TO_TARGET]"
        destinationPhase: "[TO_PHASE]"
    

Where:

  * `[RULE_ID]`

Is any name you want to give to this rule. This name must be unique within the automation resource.

  * `[WAIT_TIME]`

Is the amount of time, in minutes, to wait after the release is ready for promotion before it's promoted. For example, `1m`. The `m` is required.

The default value is `0`, or no wait time. The maximum is `20160m` (or 14 days).

  * `[TO_TARGET]`

Is the [`targetId`](https://docs.cloud.google.com/deploy/docs/config-files#targetid) of the target to promote to.

This can also be `@next`, which promotes the release automatically to the next target after the target specified in the `selector.targets` property in this [automation config](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions). This is the default if you omit the value from `destinationTargetId`.

  * `[TO_PHASE]`

Is the phase name of the phase you want to promote to, for example `canary-25` or `stable`. This property is optional; if you omit it, the release is promoted to the first phase in the target.




### Configure an `advanceRolloutRule` automation rule

The `advanceRolloutRule` advances your rollout, automatically, after successful completion of one phase, into the next phase. This automation rule is useful for canary deployments. For example, if you have a canary deployment strategy configured on a target, with phases of `25%`, `50%`, and `stable`, you could configure an automation rule that advances the phase automatically to `stable` after the `50%` phase finishes.

**Note:** The service account configured in the automation (the "automation service account") must have the `clouddeploy.rollouts.advance` permission. The automation service account must have `iam.serviceAccount.actAs` permission to impersonate the Cloud Deploy [execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account). See [IAM roles and permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions) for more information.

When you configure a `advanceRolloutRule` automation, you identify the phase to advance _from_ (the `sourcePhase`). The `rules` stanza shown here goes inside your [automation definition](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions).
    
    
    rules:
    - advanceRolloutRule:
        id: "[RULE_ID]"
        sourcePhases: ["[START_PHASE]", "[START_PHASE]"...]
        wait: [WAIT_TIME]
    

Where:

  * `[RULE_ID]`

Is any name you want to give to this rule. This name must be unique within the automation resource.

  * `[WAIT_TIME]`

Is the amount of time, in minutes, to wait to advance the rollout after the rollout is ready. For example, `1m`. The `m` is required.

The default value is `0`, or no wait time. The maximum is `20160m` (or 14 days).

  * `["[START_PHASE]", "[START_PHASE]"...]`

Is the phase or phases _from which_ the rollout is automatically advanced. That is, when any of the phases listed finish successfully, the rollout is automatically advanced from that phase to the next phase.

Phase names are case sensitive. Also, these phase names are optional; if you omit `sourcePhases`, all phases in the rollout are automatically advanced.




### Configure a `repairRolloutRule` automation rule

The `repairRolloutRule` rule retries a failed rollout a specified number of times. If that number of retries is exhausted, this rule can then automatically roll back the target to the last successful release.

When you configure a `repairRolloutRule` automation, you can specify how many times to retry the rollout, and the wait time between retries. You can also configure specific phases or jobs, or both, to retry. If each retry attempt fails, the rollout fails. If any retry succeeds, the automation stops and the rollout succeeds. 

Optionally, you can configure the automation to roll back to the last successful release on the target. Retries are also optional, but you need to have either some number of retries _or_ a rollback, or both.

The `rules` stanza shown here goes inside your [automation definition](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions).
    
    
    rules:
    - repairRolloutRule:
        id: "[RULE_ID]"
        phases: [PHASES_TO_REPAIR]
        jobs: [JOBS_TO_REPAIR]
        repairPhases:
        - retry:
            attempts: [NUMBER_OF_ATTEMPTS]
            wait: [WAIT_TIME]
            backoffMode: [LINEAR | EXPONENTIAL]
        - rollback:
            destinationPhase: [PHASE_NAME]
            disableRollbackIfRolloutPending: [true | false]
    

Where:

  * `[RULE_ID]`

Is any name you want to give to this rule. This name must be unique within the automation resource.

  * `[PHASES_TO_REPAIR]`

Is the rollout phase or phases to retry. This is optional, and the default is all phases in the rollout.

  * `[JOBS_TO_REPAIR]`

Is the job or jobs to retry. This is optional, and the default is all jobs.

  * `[NUMBER_OF_ATTEMPTS]`

Optional, the number of times to retry the rollout before considering it failed.

  * `[WAIT_TIME]`

Is the amount of time to wait between retry attempts. For example, `1m` for a one-minutes interval. The time unit (`m` in this case) is required.

If `mode` is `linear`, this interval is the same for each retry. If `mode` is `exponential`, the interval increases each time. (See `mode` for further description.)

  * `backoffMode`

`LINEAR` or `EXPONENTIAL`, indicating whether or not to increase the time between retires. If `LINEAR`, the time between retries is constant, at `WAIT_TIME`. If `EXPONENTIAL`, the time between retries doubles with each successive retry. Default is `LINEAR`.

For example, if `WAIT_TIME` is 1m, and `backoffMode` is set to `EXPONENTIAL`, then the time between the failure and the first retry is 1 minute, the time between the first and second retries is 2 minutes, and the time between the second and third retries is 4 minutes.

  * `rollback`

Optional, whether or not to roll back the failed rollout after all retry attempts are exhausted.

  * `[PHASE_NAME]`

Is the name of a specific phase you want to roll back to. If you omit `toPhase`, the rollback defaults to the `stable` phase.

  * `disableRollbackIfRolloutPending`:

If set to `true`, the rollback operation is aborted if there's a pending rollout on the target.




#### Abort a `repairRolloutRule` automation run

If you run any of the following commands on your rollout, the `repairRolloutRule` automation is aborted:

  * [Retry job](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#retry_failed_job)
  * [Cancel rollout](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#cancel_rollout)
  * [Ignore job](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#ignore_job)
  * [Terminate job run](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#terminate_job_run)



#### Example

The following is an example of an automation configuration with a `repairRolloutRule`:
    
    
    apiVersion: deploy.cloud.google.com/v1
    kind: Automation
    metadata:
      name: regular-repair/regular
    description: repair regular rollouts
    suspended: false
    serviceAccount: (REDACTED)
    selector:
      targets:
      - id: t1
    rules:
    - repairRolloutRule:
        id: "repair-rollout"
        repairPhases:
        - retry:
            attempts: 3
            wait: 1m
            backoffMode: LINEAR
        - rollback:
            destinationPhase: "stable"
    
    

In this automation, if a rollout fails on the identified target, that rollout is retried up to 3 times, with a one-minute wait between retry attempt. If all retry attempts fail, a rollback is started by creating a new rollout to deploy the target's most recent successful release to that target.

## What's next

  * Try the [quickstart: Automate release creation and rollout advancement](https://docs.cloud.google.com/deploy/docs/deploy-app-automation).

  * [Learn more](https://docs.cloud.google.com/deploy/docs/automation) about deployment automation in Cloud Deploy.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
