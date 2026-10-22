---
url: https://docs.cloud.google.com/deploy/docs/deploy-policy/
title: Restrict deploy behavior using policies \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:56.259200+00:00
---

# Restrict deploy behavior using policies  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Restrict deploy behavior using policies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use deploy policies to restrict manual or [automated](https://docs.cloud.google.com/deploy/docs/automation) delivery-pipeline actions.

A deploy policy is a Cloud Deploy resource that you can use to restrict manual or automatic actions against a selected delivery pipeline or target (or all pipelines or targets).

## What behavior can be restricted?

You can create deploy policies to restrict or prevent Cloud Deploy from performing certain actions on rollouts. For example, a policy can prevent rollout creation for a given delivery pipeline during a specified time period. You might use this for seasonal restrictions, for example.

## How are policies evaluated and enforced

For any manual or automated action, Cloud Deploy does the following:

  1. Checks Identity and Access Management permissions.

If the user or service account doesn't have adequate IAM permissions, the action isn't taken and there is no need to evaluate deploy policies.

  2. Checks whether there's an applicable policy for the target or delivery pipeline, and if there is, the policy is evaluated.

     * Cloud Deploy evaluates the action being taken to see if this rule is applicable.

That is, does the action type and invoker match the policy?

     * Cloud Deploy checks date and time ranges defined for the policy to see if that policy is in effect at the time of the request.

     * If the policy is in effect and the rule does apply to the delivery pipeline or target and the action, that rule is enforced and the action is blocked.




## Requirements and Limitations

  * Each policy must have at least one selector.

  * Each policy must have at least one rule.

All rule IDs must be unique within a deploy policy.

  * Each rule must have at least one `timeWindows`, and within that `timeWindows`, there must be either a `oneTimeWindows` or a `weeklyWindows`.

See Dates and times for more details on using time blocks.

  * You can have no more than 1000 deploy policies per project/location.




## Identity and Access Management roles and permissions required

In addition to the permissions you need to run any Cloud Deploy delivery pipeline, and to perform the tasks to that would be restricted by policy, there are several permissions that are needed in order to perform certain operations on the policy resource:

  * `clouddeploy.deployPolicies.create`
  * `clouddeploy.deployPolicies.delete`
  * `clouddeploy.deployPolicies.get`
  * `clouddeploy.deployPolicies.list`
  * `clouddeploy.deployPolicies.update`
  * `clouddeploy.deployPolicies.override`



Those permissions are included in the `roles/clouddeploy.policyAdmin` role. Additionally, the `roles/clouddeploy.policyOverrider` role includes the `.override` permission.

## Create a deploy policy

Creating a deploy-policy resource consists of the following steps:

  1. Create a YAML file with the deploy policy [configuration](https://docs.cloud.google.com/deploy/docs/config-files#deploy_policy_definitions).

The configuration includes a header, which identifies the resource as a deploy policy. The `name` is required.
         
         apiVersion: deploy.cloud.google.com/v1
          kind: DeployPolicy
          metadata:
            name: 
          description: 
         

  2. Add a reference to the delivery pipelines and targets to which the policy applies (the `selectors`).

See Deploy policy selectors and the [Configuration schema reference](https://docs.cloud.google.com/deploy/docs/config-files#deploy_policy_definitions) for more information on policy selectors and how to configure them..

  3. Add one or more policy `rules`.

Each rule describes a restriction and the circumstances under which that restriction is enforced. See Deploy policy rules and the [Configuration schema reference](https://docs.cloud.google.com/deploy/docs/config-files#deploy_policy_definitions) for more information on policy rules and how to configure them.

  4. Apply that file to create the policy:
         
         gcloud deploy apply --file=FILENAME \
                              --region=REGION \
                              --project=PROJECT_ID
         

Where `FILENAME` is the name of the YAML file containing your `DeployPolicy` definition, `REGION` is the region in which you want to create the deploy policy resource, and `PROJECT_ID` is project in which you want to create the resource.




The referenced delivery pipelines or targets are now restricted according to the rules in the deploy-policy resource.

## Deploy policy selectors

Selectors, defined in deploy policy [configurations](https://docs.cloud.google.com/deploy/docs/config-files#deploy_policy_definitions), determine what delivery pipelines and targets are affected by a given rule.

A selector is defined in a `selectors` stanza in the deploy policy configuration, as a top-level property:
    
    
    selectors:
    - deliveryPipeline:
        id:
        labels:
      target:
        id:
        labels:
    

In this configuration YAML, `deliveryPipeline.id` takes the name of the delivery pipeline, and `target.id` takes the name of the target (in both cases, `metadata.name`).

You can use `id: *` to select all delivery pipelines or all targets. Note that `*` is a special field value to select all—arbitrary wildcarding isn't supported. You can also use labels to match delivery pipelines or targets or both.

Within a given selector, items are ANDed together. Multiple selectors are ORed. That is, for a given request to be restricted by the policy, it must apply to at least one selector. But within that selector, the request must match all items.

## Deploy policy rules

Each deploy policy includes one or more policy rules, which define what action is restricted in the selected delivery pipeline or target. The rule also defines under what circumstances the rule is applied.

The following rules are available:

  * `rolloutRestriction`



The `rolloutRestriction` rule prevents the specified rollout actions from being performed on selected targets used by selected delivery pipelines. This rule uses a time window that defines _when_ a rollout can't be created for the selected delivery pipeline and target. See Dates and times for a description of how dates and times are specified in deploy policy rules.

The following actions can be restricted while the rule is in effect:

  * `ADVANCE`

Rollout phases can't be [advanced](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#advance_rollout).

  * `APPROVE`

Rollout [promotion](https://docs.cloud.google.com/deploy/docs/promote-release) can't be approved.

  * `CANCEL`

Rollouts can't be [canceled](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#cancel_rollout).

  * `CREATE`

Rollouts can't be created. You can [create a release](https://docs.cloud.google.com/deploy/docs/deploying-application#invoke_your_delivery_pipeline_to_create_a_release) if a policy is preventing this action, but that release won't spawn a rollout.

  * `IGNORE_JOB`

Jobs can't be [ignored](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#ignore_job).

  * `RETRY_JOB`

Jobs can't be [retried](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#retry_failed_job).

  * `ROLLBACK`

Rollouts can't be [rolled back](https://docs.cloud.google.com/deploy/docs/roll-back).

  * `TERMINATE_JOBRUN`

Job runs can't be [terminated](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#terminate_job_run)

See the [Configuration schema reference](https://docs.cloud.google.com/deploy/docs/config-files#deploy_policy_definitions) for the YAML structure for this rule.




### Dates and times in a `rolloutRestriction` rule

You [configure](https://docs.cloud.google.com/deploy/docs/config-files#deploy_policy_definitions) date and time blocks to specify repeating and non-repeating time windows during which the deploy policy is in effect.

The following are the requirements for expressing dates and time:

  * Dates are expressed as `yyyy-mm-dd`.

  * When expressing time of day, the start of the day is `00:00`, and the end of the day is `24:00`.

  * For `oneTimeWindows`, dates must include the time. For `weeklyWindows`, you can omit the time of day. But if you include `startTime` you must include `endTime`, and the other way around.

For example, a freeze on Sundays only would be as follows:
        
        - daysOfWeek: [SUNDAY]
          startTime: "00:00"
          endTime: "24:00"
        

You could also do this:
        
        - daysOfWeek: [SUNDAY]
        

But not this:
        
        - daysOfWeek: [SUNDAY]
          startTime: "00:00"
        

  * You must include a time zone, in the `timeWindows` stanza.

For example: `timeZone: America/New_York`.




#### Non-repeating time windows

A non-repeating time window starts and ends on an specific day and time. You would use this for any block of time for which you want to restrict rollouts.

Non-repeating time windows are configured using a `oneTimeWindows` stanza.

#### Repeating time windows

A repeating time window describes a repeating block of time during which you want to restrict rollouts. For example, you could use this to restrict rollouts on weekends.

Repeating time windows are configured using a `weeklyWindows` stanza.

### Examples

This section contains some examples of using dates and times to configure when a deploy policy is enforced.

#### Annual freeze

If there's a time of year during which you want to freeze rollouts, you can configure a `oneTimeWindows` block to do so. If the dates are predictable, from year to year, you still need to use multiple `oneTimeWindow` blocks.

The following YAML shows a one-time (non-repeating) time window to enforce a deploy policy for an annual freeze:
    
    
    timeWindows:
      timeZone: "America/New_York"
      oneTimeWindows:
      - start: "2024-12-22 17:00"
        end: "2025-01-02 09:00"
    

This YAML describes a time window from December 22, 2024 at 5pm, through January 2, 2025, at 9am.

#### Repeating weekend freeze

The following YAML shows a repeating time window to enforce a deploy policy that restricts rollouts on weekends, from Friday at 5pm through Monday morning at 9am:
    
    
    timeWindows:
      timeZone: "America/New_York"
      weeklyWindows:
      - daysOfWeek: [FRIDAY]
        startTime: "17:00"
        endTime: "24:00"
      - daysOfWeek: [SATURDAY, SUNDAY]
        startTime: "00:00"
        endTime: "24:00"
      - daysOfWeek: [MONDAY]
        startTime: "00:00"
        endTime: "09:00"
    

## Update a deploy policy

Updating a deploy policy consists of the following steps:

  1. Edit the policy configuration YAML.

If you created the policy using the Google Cloud console, you can get the YAML configuration by selecting the **YAML** tab on the **Deploy policy details** page. Then you can copy that text into a file locally and edit it there.

  2. Apply that file to update the policy:
         
         gcloud deploy apply --file=FILENAME \
                              --region=REGION \
                              --project=PROJECT_ID
         

This updates the deploy policy resource with the new configuration.




Because deploy policies are evaluated when the restricted action is attempted, all such actions against all Cloud Deploy resources are subject to the updated policy. That is, there is no remnant of the previous restrictions. For example, if you have a `restrictRollouts` block for the entire month of December, and on December 14, you update the policy so that the restriction ends on December 15, rollouts are no longer blocked after December 15.

## Override a deploy policy

You can override a deploy policy, if necessary. For example, if there's a problem with a deployment in production and you need to roll it back, but there's a deploy policy preventing any rollouts, you can override that policy in order to roll back the bad rollout.

In order to override a deploy policy, you must have the `clouddeploy.deployPolicies.override` IAM permission.

You can override the policy either from the gcloud CLI or using the Google Cloud console:

###  console 

  1. In the Google Cloud console, try to take an action that's blocked by a policy.

A dialog is displayed indicating that the action is blocked by a deploy policy. This dialog includes a link to the specific policy that's blocking this action.

  2. In the text field provided, type the name of the policy and click **Attempt to override policies**.

If you have permission to override the policy, Cloud Deploy now executes the action.




###  gcloud CLI 

To override a deploy policy using gcloud CLI, add the `--override-deploy-policies` to the command for any action that would be prevented by that policy. For example, the following command promotes a release, overriding a specific deploy policy that would otherwise prevent the promotion:
    
    
     gcloud deploy releases promote --release=my-release-001 \
       --project=my-policy-testing-project \
       --region=us-central1 \
       --delivery-pipeline=my-pipeline \
       --to-target=prod-target \
       --override-deploy-policies=my-deploy-policy
    

## Delete a deploy policy

To delete a deploy policy:

###  console 

  1. In the Google Cloud console, navigate to the Cloud Deploy **Deploy policies** page.

[Open the Deploy policies page](https://console.cloud.google.com/deploy/deploy-policies)

The page includes a list of the deploy policies available in your current project, if any.

  2. Select the more_vert **Actions** button for the policy you want to delete, and click **Delete deploy policy**.

  3. Confirm the deletion by typing the deploy policy name, and click **Confirm**.

The policy is now deleted, and you can now perform any of the actions that the policy restricted.




###  gcloud CLI 

To delete a deploy policy using the gcloud CLI, run the following command:
    
    
     gcloud deploy deploy-policies delete \
        --project=[PROJECT] \
        --region=[REGION] \
        [POLICY_NAME]
    

Replace the following:

  * `[POLICY_NAME]`

The name of the policy as defined in the [policy configuration file](https://docs.cloud.google.com/deploy/docs/config-files#deploy_policy_definitions).

  * `[PROJECT]`

The project ID of the Google Cloud project in which you created the deploy policy.

  * `[REGION]`

The region in which you created the deploy policy.




After you delete the deploy policy resource, the affected delivery pipelines and targets are no longer subject to the policy, and won't be restricted unless affected by another deploy policy.

## Logging of deploy policy

When a deploy policy is evaluated, [platform log](https://docs.cloud.google.com/deploy/docs/platform-logs) entries are created for the following actions:

  * Policy evaluation

Platform logs are written when a request is evaluated and violates the policy. A log is written also when the policy is violated by a request but the request is allowed because the policy is suspended or was overridden. No log is written when the request is granted because the policy is not violated.

  * Pub/Sub notification failure upon change of a deploy policy resource.




## What's next

  * See the [Configuration file schema](https://docs.cloud.google.com/deploy/docs/config-files#deploy_policy_definitions) for details on configuring deploy policies.

  * Learn about [Cloud Deploy deploy automation](https://docs.cloud.google.com/deploy/docs/automation).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
