---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations
title: REST Resource: projects.locations.deliveryPipelines.automations \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:58.153967+00:00
---

# REST Resource: projects.locations.deliveryPipelines.automations  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.deliveryPipelines.automations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Automation
    * JSON representation
    * AutomationResourceSelector
      * JSON representation
    * AutomationRule
      * JSON representation
    * PromoteReleaseRule
      * JSON representation
    * AutomationRuleCondition
      * JSON representation
    * TimedPromoteReleaseCondition
      * JSON representation
    * Targets
      * JSON representation
    * AdvanceRolloutRule
      * JSON representation
    * RepairRolloutRule
      * JSON representation
    * RepairPhaseConfig
      * JSON representation
    * Retry
      * JSON representation
    * Rollback
      * JSON representation
    * TimedPromoteReleaseRule
      * JSON representation
  * Methods



## Resource: Automation

An `Automation` resource in the Cloud Deploy API.

An `Automation` enables the automation of manually driven actions for a Delivery Pipeline, which includes Release promotion among Targets, Rollout repair and Rollout deployment strategy advancement. The intention of Automation is to reduce manual intervention in the continuous delivery process.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "annotations": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      },
      "etag": string,
      "suspended": boolean,
      "serviceAccount": string,
      "selector": {
        object ([AutomationResourceSelector](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationResourceSelector))
      },
      "rules": [
        {
          object ([AutomationRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the `Automation`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/automations/{automation}`.  
`uid` |  `string` Output only. Unique identifier of the `Automation`.  
`description` |  `string` Optional. Description of the `Automation`. Max length is 255 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the automation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the automation was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints:

  * Annotations are key/value pairs.
  * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`).
  * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
  * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`).

See <https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 63 characters.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Optional. The weak etag of the `Automation` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`suspended` |  `boolean` Optional. When Suspended, automation is deactivated from execution.  
`serviceAccount` |  `string` Required. Email address of the user-managed IAM service account that creates Cloud Deploy release and rollout resources.  
`selector` |  `object (`[AutomationResourceSelector](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationResourceSelector)`)` Required. Selected resources to which the automation will be applied.  
`rules[]` |  `object (`[AutomationRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRule)`)` Required. List of Automation rules associated with the Automation resource. Must have at least one rule and limited to 250 rules per Delivery Pipeline. Note: the order of the rules here is not the same as the order of execution.  
  
### AutomationResourceSelector

AutomationResourceSelector contains the information to select the resources to which an Automation is going to be applied.

JSON representation  
---  
      
    
    {
      "targets": [
        {
          object ([TargetAttribute](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/TargetAttribute))
        }
      ]
    }  
  
Fields  
---  
`targets[]` |  `object (`[TargetAttribute](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/TargetAttribute)`)` Optional. Contains attributes about a target.  
  
### AutomationRule

`AutomationRule` defines the automation activities.

JSON representation  
---  
      
    
    {
    
      // Union field rule can be only one of the following:
      "promoteReleaseRule": {
        object ([PromoteReleaseRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.PromoteReleaseRule))
      },
      "advanceRolloutRule": {
        object ([AdvanceRolloutRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AdvanceRolloutRule))
      },
      "repairRolloutRule": {
        object ([RepairRolloutRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.RepairRolloutRule))
      },
      "timedPromoteReleaseRule": {
        object ([TimedPromoteReleaseRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.TimedPromoteReleaseRule))
      }
      // End of list of possible types for union field rule.
    }  
  
Fields  
---  
Union field `rule`. The configuration of the Automation rule. `rule` can be only one of the following:  
`promoteReleaseRule` |  `object (`[PromoteReleaseRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.PromoteReleaseRule)`)` Optional. `PromoteReleaseRule` will automatically promote a release from the current target to a specified target.  
`advanceRolloutRule` |  `object (`[AdvanceRolloutRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AdvanceRolloutRule)`)` Optional. The `AdvanceRolloutRule` will automatically advance a successful Rollout.  
`repairRolloutRule` |  `object (`[RepairRolloutRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.RepairRolloutRule)`)` Optional. The `RepairRolloutRule` will automatically repair a failed rollout.  
`timedPromoteReleaseRule` |  `object (`[TimedPromoteReleaseRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.TimedPromoteReleaseRule)`)` Optional. The `TimedPromoteReleaseRule` will automatically promote a release from the current target(s) to the specified target(s) on a configured schedule.  
  
### PromoteReleaseRule

The `PromoteRelease` rule will automatically promote a release from the current target to a specified target.

JSON representation  
---  
      
    
    {
      "id": string,
      "wait": string,
      "destinationTargetId": string,
      "condition": {
        object ([AutomationRuleCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRuleCondition))
      },
      "destinationPhase": string
    }  
  
Fields  
---  
`id` |  `string` Required. ID of the rule. This id must be unique in the `Automation` resource to which this rule belongs. The format is `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.  
`wait` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How long the release need to be paused until being promoted to the next target.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`destinationTargetId` |  `string` Optional. The ID of the stage in the pipeline to which this `Release` is deploying. If unspecified, default it to the next stage in the promotion flow. The value of this field could be one of the following:

  * The last segment of a target name
  * "@next", the next target in the promotion sequence

  
`condition` |  `object (`[AutomationRuleCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRuleCondition)`)` Output only. Information around the state of the Automation rule.  
`destinationPhase` |  `string` Optional. The starting phase of the rollout created by this operation. Default to the first phase.  
  
### AutomationRuleCondition

`AutomationRuleCondition` contains conditions relevant to an `Automation` rule.

JSON representation  
---  
      
    
    {
      "targetsPresentCondition": {
        object ([TargetsPresentCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/TargetsPresentCondition))
      },
    
      // Union field rule_type_condition can be only one of the following:
      "timedPromoteReleaseCondition": {
        object ([TimedPromoteReleaseCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.TimedPromoteReleaseCondition))
      }
      // End of list of possible types for union field rule_type_condition.
    }  
  
Fields  
---  
`targetsPresentCondition` |  `object (`[TargetsPresentCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/TargetsPresentCondition)`)` Optional. Details around targets enumerated in the rule.  
Union field `rule_type_condition`. Details specific to the automation rule type. `rule_type_condition` can be only one of the following:  
`timedPromoteReleaseCondition` |  `object (`[TimedPromoteReleaseCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.TimedPromoteReleaseCondition)`)` Optional. TimedPromoteReleaseCondition contains rule conditions specific to a an Automation with a timed promote release rule defined.  
  
### TimedPromoteReleaseCondition

`TimedPromoteReleaseCondition` contains conditions specific to an Automation with a Timed Promote Release rule defined.

JSON representation  
---  
      
    
    {
      "nextPromotionTime": string,
      "targetsList": [
        {
          object ([Targets](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.Targets))
        }
      ]
    }  
  
Fields  
---  
`nextPromotionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the next scheduled promotion(s) will occur.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`targetsList[]` |  `object (`[Targets](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.Targets)`)` Output only. A list of targets involved in the upcoming timed promotion(s).  
  
### Targets

The targets involved in a single timed promotion.

JSON representation  
---  
      
    
    {
      "sourceTargetId": string,
      "destinationTargetId": string
    }  
  
Fields  
---  
`sourceTargetId` |  `string` Optional. The source target ID.  
`destinationTargetId` |  `string` Optional. The destination target ID.  
  
### AdvanceRolloutRule

The `rollouts.advance` automation rule will automatically advance a successful Rollout to the next phase.

JSON representation  
---  
      
    
    {
      "id": string,
      "sourcePhases": [
        string
      ],
      "wait": string,
      "condition": {
        object ([AutomationRuleCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRuleCondition))
      }
    }  
  
Fields  
---  
`id` |  `string` Required. ID of the rule. This id must be unique in the `Automation` resource to which this rule belongs. The format is `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.  
`sourcePhases[]` |  `string` Optional. Proceeds only after phase name matched any one in the list. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.  
`wait` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How long to wait after a rollout is finished.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`condition` |  `object (`[AutomationRuleCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRuleCondition)`)` Output only. Information around the state of the Automation rule.  
  
### RepairRolloutRule

The `RepairRolloutRule` automation rule will automatically repair a failed `Rollout`.

JSON representation  
---  
      
    
    {
      "id": string,
      "phases": [
        string
      ],
      "jobs": [
        string
      ],
      "condition": {
        object ([AutomationRuleCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRuleCondition))
      },
      "repairPhases": [
        {
          object ([RepairPhaseConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.RepairPhaseConfig))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. ID of the rule. This id must be unique in the `Automation` resource to which this rule belongs. The format is `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.  
`phases[]` |  `string` Optional. Phases within which jobs are subject to automatic repair actions on failure. Proceeds only after phase name matched any one in the list, or for all phases if unspecified. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.  
`jobs[]` |  `string` Optional. Jobs to repair. Proceeds only after job name matched any one in the list, or for all jobs if unspecified or empty. The phase that includes the job must match the phase ID specified in `sourcePhase`. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.  
`condition` |  `object (`[AutomationRuleCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRuleCondition)`)` Output only. Information around the state of the 'Automation' rule.  
`repairPhases[]` |  `object (`[RepairPhaseConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.RepairPhaseConfig)`)` Required. Defines the types of automatic repair phases for failed jobs.  
  
### RepairPhaseConfig

Configuration of the repair phase.

JSON representation  
---  
      
    
    {
    
      // Union field repair_phase can be only one of the following:
      "retry": {
        object ([Retry](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.Retry))
      },
      "rollback": {
        object ([Rollback](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.Rollback))
      }
      // End of list of possible types for union field repair_phase.
    }  
  
Fields  
---  
Union field `repair_phase`. The repair phase to perform. `repair_phase` can be only one of the following:  
`retry` |  `object (`[Retry](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.Retry)`)` Optional. Retries a failed job.  
`rollback` |  `object (`[Rollback](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.Rollback)`)` Optional. Rolls back a `Rollout`.  
  
### Retry

Retries the failed job.

JSON representation  
---  
      
    
    {
      "attempts": string,
      "wait": string,
      "backoffMode": enum ([BackoffMode](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/BackoffMode))
    }  
  
Fields  
---  
`attempts` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Total number of retries. Retry is skipped if set to 0; The minimum value is 1, and the maximum value is 10.  
`wait` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How long to wait for the first retry. Default is 0, and the maximum value is 14d.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`backoffMode` |  `enum (`[BackoffMode](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/BackoffMode)`)` Optional. The pattern of how wait time will be increased. Default is linear. Backoff mode will be ignored if `wait` is 0.  
  
### Rollback

Rolls back a `Rollout`.

JSON representation  
---  
      
    
    {
      "destinationPhase": string,
      "disableRollbackIfRolloutPending": boolean
    }  
  
Fields  
---  
`destinationPhase` |  `string` Optional. The starting phase ID for the `Rollout`. If unspecified, the `Rollout` will start in the stable phase.  
`disableRollbackIfRolloutPending` |  `boolean` Optional. If pending rollout exists on the target, the rollback operation will be aborted.  
  
### TimedPromoteReleaseRule

The `TimedPromoteReleaseRule` will automatically promote a release from the current target(s) to the specified target(s) on a configured schedule.

JSON representation  
---  
      
    
    {
      "id": string,
      "destinationTargetId": string,
      "schedule": string,
      "timeZone": string,
      "condition": {
        object ([AutomationRuleCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRuleCondition))
      },
      "destinationPhase": string
    }  
  
Fields  
---  
`id` |  `string` Required. ID of the rule. This ID must be unique in the `Automation` resource to which this rule belongs. The format is `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.  
`destinationTargetId` |  `string` Optional. The ID of the stage in the pipeline to which this `Release` is deploying. If unspecified, default it to the next stage in the promotion flow. The value of this field could be one of the following:

  * The last segment of a target name
  * "@next", the next target in the promotion sequence

  
`schedule` |  `string` Required. Schedule in crontab format. e.g. "0 9 * * 1" for every Monday at 9am.  
`timeZone` |  `string` Required. The time zone in IANA format [IANA Time Zone Database](https://www.iana.org/time-zones) (e.g. America/New_York).  
`condition` |  `object (`[AutomationRuleCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation.AutomationRuleCondition)`)` Output only. Information around the state of the Automation rule.  
`destinationPhase` |  `string` Optional. The starting phase of the rollout created by this rule. Default to the first phase.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/create)`

|  Creates a new Automation in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/delete)`

|  Deletes a single Automation resource.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/get)`

|  Gets details of a single Automation.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/list)`

|  Lists Automations in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/patch)`

|  Updates the parameters of a single Automation resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-26 UTC."],[],[]] 
