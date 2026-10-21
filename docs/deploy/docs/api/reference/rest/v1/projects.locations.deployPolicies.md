---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies
title: REST Resource: projects.locations.deployPolicies \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:00.031271+00:00
---

# REST Resource: projects.locations.deployPolicies  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.deployPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DeployPolicy
    * JSON representation
  * DeployPolicyResourceSelector
    * JSON representation
  * DeliveryPipelineAttribute
    * JSON representation
  * PolicyRule
    * JSON representation
  * RolloutRestriction
    * JSON representation
  * Invoker
  * RolloutActions
  * TimeWindows
    * JSON representation
  * OneTimeWindow
    * JSON representation
  * Date
    * JSON representation
  * TimeOfDay
    * JSON representation
  * WeeklyWindow
    * JSON representation
  * DayOfWeek
  * Methods



## Resource: DeployPolicy

A `DeployPolicy` resource in the Cloud Deploy API.

A `DeployPolicy` inhibits manual or automation-driven actions within a Delivery Pipeline or Target.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "description": string,
      "annotations": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "suspended": boolean,
      "selectors": [
        {
          object ([DeployPolicyResourceSelector](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#DeployPolicyResourceSelector))
        }
      ],
      "rules": [
        {
          object ([PolicyRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#PolicyRule))
        }
      ],
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the `DeployPolicy`. Format is `projects/{project}/locations/{location}/deployPolicies/{deployPolicy}`. The `deployPolicy` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`  
`uid` |  `string` Output only. Unique identifier of the `DeployPolicy`.  
`description` |  `string` Optional. Description of the `DeployPolicy`. Max length is 255 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints:

  * Annotations are key/value pairs.
  * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`).
  * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
  * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`).

See <https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the deploy policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Most recent time at which the deploy policy was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`suspended` |  `boolean` Optional. When suspended, the policy will not prevent actions from occurring, even if the action violates the policy.  
`selectors[]` |  `object (`[DeployPolicyResourceSelector](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#DeployPolicyResourceSelector)`)` Required. Selected resources to which the policy will be applied. At least one selector is required. If one selector matches the resource the policy applies. For example, if there are two selectors and the action being attempted matches one of them, the policy will apply to that action.  
`rules[]` |  `object (`[PolicyRule](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#PolicyRule)`)` Required. Rules to apply. At least one rule must be present.  
`etag` |  `string` The weak etag of the `DeployPolicy` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
  
## DeployPolicyResourceSelector

Contains information on the resources to select for a deploy policy. Attributes provided must all match the resource in order for policy restrictions to apply. For example, if delivery pipelines attributes given are an id "prod" and labels "foo: bar", a delivery pipeline resource must match both that id and have that label in order to be subject to the policy.

JSON representation  
---  
      
    
    {
      "deliveryPipeline": {
        object ([DeliveryPipelineAttribute](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#DeliveryPipelineAttribute))
      },
      "target": {
        object ([TargetAttribute](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/TargetAttribute))
      }
    }  
  
Fields  
---  
`deliveryPipeline` |  `object (`[DeliveryPipelineAttribute](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#DeliveryPipelineAttribute)`)` Optional. Contains attributes about a delivery pipeline.  
`target` |  `object (`[TargetAttribute](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/TargetAttribute)`)` Optional. Contains attributes about a target.  
  
## DeliveryPipelineAttribute

Contains criteria for selecting DeliveryPipelines.

JSON representation  
---  
      
    
    {
      "id": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`id` |  `string` Optional. ID of the `DeliveryPipeline`. The value of this field could be one of the following:

  * The last segment of a pipeline name
  * "*", all delivery pipelines in a location

  
`labels` |  `map (key: string, value: string)` DeliveryPipeline labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## PolicyRule

Deploy Policy rule.

JSON representation  
---  
      
    
    {
    
      // Union field rule can be only one of the following:
      "rolloutRestriction": {
        object ([RolloutRestriction](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#RolloutRestriction))
      }
      // End of list of possible types for union field rule.
    }  
  
Fields  
---  
Union field `rule`.`rule` can be only one of the following:  
`rolloutRestriction` |  `object (`[RolloutRestriction](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#RolloutRestriction)`)` Optional. Rollout restrictions.  
  
## RolloutRestriction

Rollout restrictions.

JSON representation  
---  
      
    
    {
      "id": string,
      "invokers": [
        enum ([Invoker](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Invoker))
      ],
      "actions": [
        enum ([RolloutActions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#RolloutActions))
      ],
      "timeWindows": {
        object ([TimeWindows](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeWindows))
      }
    }  
  
Fields  
---  
`id` |  `string` Required. Restriction rule ID. Required and must be unique within a DeployPolicy. The format is `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.  
`invokers[]` |  `enum (`[Invoker](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Invoker)`)` Optional. What invoked the action. If left empty, all invoker types will be restricted.  
`actions[]` |  `enum (`[RolloutActions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#RolloutActions)`)` Optional. Rollout actions to be restricted as part of the policy. If left empty, all actions will be restricted.  
`timeWindows` |  `object (`[TimeWindows](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeWindows)`)` Required. Time window within which actions are restricted.  
  
## Invoker

What invoked the action. Filters enforcing the policy depending on what invoked the action.

Enums  
---  
`INVOKER_UNSPECIFIED` | Unspecified.  
`USER` | The action is user-driven. For example, creating a rollout manually via a gcloud create command.  
`DEPLOY_AUTOMATION` | Automated action by Cloud Deploy.  
  
## RolloutActions

Rollout actions to be restricted as part of the policy.

Enums  
---  
`ROLLOUT_ACTIONS_UNSPECIFIED` | Unspecified.  
`ADVANCE` | Advance the rollout to the next phase.  
`APPROVE` | Approve the rollout.  
`CANCEL` | Cancel the rollout.  
`CREATE` | Create a rollout.  
`IGNORE_JOB` | Ignore a job result on the rollout.  
`RETRY_JOB` | Retry a job for a rollout.  
`ROLLBACK` | Rollback a rollout.  
`TERMINATE_JOBRUN` | Terminate a jobrun.  
  
## TimeWindows

Time windows within which actions are restricted. See the [documentation](https://cloud.google.com/deploy/docs/deploy-policy#dates_times) for more information on how to configure dates/times.

JSON representation  
---  
      
    
    {
      "timeZone": string,
      "oneTimeWindows": [
        {
          object ([OneTimeWindow](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#OneTimeWindow))
        }
      ],
      "weeklyWindows": [
        {
          object ([WeeklyWindow](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#WeeklyWindow))
        }
      ]
    }  
  
Fields  
---  
`timeZone` |  `string` Required. The time zone in IANA format [IANA Time Zone Database](https://www.iana.org/time-zones) (e.g. America/New_York).  
`oneTimeWindows[]` |  `object (`[OneTimeWindow](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#OneTimeWindow)`)` Optional. One-time windows within which actions are restricted.  
`weeklyWindows[]` |  `object (`[WeeklyWindow](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#WeeklyWindow)`)` Optional. Recurring weekly windows within which actions are restricted.  
  
## OneTimeWindow

One-time window within which actions are restricted. For example, blocking actions over New Year's Eve from December 31st at 5pm to January 1st at 9am.

JSON representation  
---  
      
    
    {
      "startDate": {
        object ([Date](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Date))
      },
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay))
      },
      "endDate": {
        object ([Date](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Date))
      },
      "endTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay))
      }
    }  
  
Fields  
---  
`startDate` |  `object (`[Date](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Date)`)` Required. Start date.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay)`)` Required. Start time (inclusive). Use 00:00 for the beginning of the day.  
`endDate` |  `object (`[Date](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Date)`)` Required. End date.  
`endTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay)`)` Required. End time (exclusive). You may use 24:00 for the end of the day.  
  
## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * `[google.type.TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay)`
  * `google.type.DateTime`
  * `[google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `[google.type.Date](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Date)` and `google.protobuf.Timestamp`.

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
## WeeklyWindow

Weekly windows. For example, blocking actions every Saturday and Sunday. Another example would be blocking actions every weekday from 5pm to midnight.

JSON representation  
---  
      
    
    {
      "daysOfWeek": [
        enum ([DayOfWeek](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#DayOfWeek))
      ],
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay))
      },
      "endTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay))
      }
    }  
  
Fields  
---  
`daysOfWeek[]` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#DayOfWeek)`)` Optional. Days of week. If left empty, all days of the week will be included.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay)`)` Optional. Start time (inclusive). Use 00:00 for the beginning of the day. If you specify startTime you must also specify endTime. If left empty, this will block for the entire day for the days specified in daysOfWeek.  
`endTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#TimeOfDay)`)` Optional. End time (exclusive). Use 24:00 to indicate midnight. If you specify endTime you must also specify startTime. If left empty, this will block for the entire day for the days specified in daysOfWeek.  
  
## DayOfWeek

Represents a day of the week.

Enums  
---  
`DAY_OF_WEEK_UNSPECIFIED` | The day of the week is unspecified.  
`MONDAY` | Monday  
`TUESDAY` | Tuesday  
`WEDNESDAY` | Wednesday  
`THURSDAY` | Thursday  
`FRIDAY` | Friday  
`SATURDAY` | Saturday  
`SUNDAY` | Sunday  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/create)`

|  Creates a new DeployPolicy in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/delete)`

|  Deletes a single DeployPolicy.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/get)`

|  Gets details of a single DeployPolicy.  
  
### `[getIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/list)`

|  Lists DeployPolicies in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/patch)`

|  Updates the parameters of a single DeployPolicy.  
  
### `[setIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-26 UTC."],[],[]] 
