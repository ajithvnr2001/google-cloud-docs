---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments
title: REST Resource: projects.locations.agents.environments.experiments \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:03.133603+00:00
---

# REST Resource: projects.locations.agents.environments.experiments  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.environments.experiments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Experiment
    * JSON representation
  * State
  * Definition
    * JSON representation
  * VersionVariants
    * JSON representation
  * Variant
    * JSON representation
  * RolloutConfig
    * JSON representation
  * RolloutStep
    * JSON representation
  * RolloutState
    * JSON representation
  * Result
    * JSON representation
  * VersionMetrics
    * JSON representation
  * Metric
    * JSON representation
  * MetricType
  * CountType
  * ConfidenceInterval
    * JSON representation
  * VariantsHistory
    * JSON representation
  * Methods



## Resource: Experiment

Represents an experiment in an environment.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#State)),
      "definition": {
        object ([Definition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Definition))
      },
      "rolloutConfig": {
        object ([RolloutConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#RolloutConfig))
      },
      "rolloutState": {
        object ([RolloutState](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#RolloutState))
      },
      "rolloutFailureReason": string,
      "result": {
        object ([Result](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Result))
      },
      "createTime": string,
      "startTime": string,
      "endTime": string,
      "lastUpdateTime": string,
      "experimentLength": string,
      "variantsHistory": [
        {
          object ([VariantsHistory](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#VariantsHistory))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The name of the experiment. Format: projects//locations//agents//environments//experiments/.  
`displayName` |  `string` Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters.  
`description` |  `string` The human-readable description of the experiment.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#State)`)` The current state of the experiment. Transition triggered by Experiments.StartExperiment: DRAFT->RUNNING. Transition triggered by Experiments.CancelExperiment: DRAFT->DONE or RUNNING->DONE.  
`definition` |  `object (`[Definition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Definition)`)` The definition of the experiment.  
`rolloutConfig` |  `object (`[RolloutConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#RolloutConfig)`)` The configuration for auto rollout. If set, there should be exactly two variants in the experiment (control variant being the default version of the flow), the traffic allocation for the non-control variant will gradually increase to 100% when conditions are met, and eventually replace the control variant to become the default version of the flow.  
`rolloutState` |  `object (`[RolloutState](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#RolloutState)`)` State of the auto rollout process.  
`rolloutFailureReason` |  `string` The reason why rollout has failed. Should only be set when state is ROLLOUT_FAILED.  
`result` |  `object (`[Result](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Result)`)` Inference result of the experiment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Creation time of this experiment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Start time of this experiment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` End time of this experiment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last update time of this experiment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`experimentLength` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Maximum number of days to run the experiment/rollout. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`variantsHistory[]` |  `object (`[VariantsHistory](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#VariantsHistory)`)` The history of updates to the experiment variants.  
  
## State

The state of the experiment.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`DRAFT` | The experiment is created but not started yet.  
`RUNNING` | The experiment is running.  
`DONE` | The experiment is done.  
`ROLLOUT_FAILED` | The experiment with auto-rollout enabled has failed.  
  
## Definition

Definition of the experiment.

JSON representation  
---  
      
    
    {
      "condition": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "versionVariants": {
        object ([VersionVariants](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#VersionVariants))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`condition` |  `string` The condition defines which subset of sessions are selected for this experiment. If not specified, all sessions are eligible. E.g. "queryInput.language_code=en" See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition).  
The variants of the experiment. We currently only support single variant experiment. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`versionVariants` |  `object (`[VersionVariants](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#VersionVariants)`)` The flow versions as the variants of this experiment.  
End of mutually exclusive fields.  
  
## VersionVariants

A list of flow version variants.

JSON representation  
---  
      
    
    {
      "variants": [
        {
          object ([Variant](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Variant))
        }
      ]
    }  
  
Fields  
---  
`variants[]` |  `object (`[Variant](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Variant)`)` A list of flow version variants.  
  
## Variant

A single flow version with specified traffic allocation.

JSON representation  
---  
      
    
    {
      "version": string,
      "trafficAllocation": number,
      "isControlGroup": boolean
    }  
  
Fields  
---  
`version` |  `string` The name of the flow version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>`.  
`trafficAllocation` |  `number` Percentage of the traffic which should be routed to this version of flow. Traffic allocation for a single flow must sum up to 1.0.  
`isControlGroup` |  `boolean` Whether the variant is for the control group.  
  
## RolloutConfig

The configuration for auto rollout.

JSON representation  
---  
      
    
    {
      "rolloutSteps": [
        {
          object ([RolloutStep](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#RolloutStep))
        }
      ],
      "rolloutCondition": string,
      "failureCondition": string
    }  
  
Fields  
---  
`rolloutSteps[]` |  `object (`[RolloutStep](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#RolloutStep)`)` Steps to roll out a flow version. Steps should be sorted by percentage in ascending order.  
`rolloutCondition` |  `string` The conditions that are used to evaluate the success of a rollout step. If not specified, all rollout steps will proceed to the next one unless failure conditions are met. E.g. "containment_rate > 60% AND callback_rate < 20%". See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition).  
`failureCondition` |  `string` The conditions that are used to evaluate the failure of a rollout step. If not specified, no rollout steps will fail. E.g. "containment_rate < 10% OR average_turn_count < 3". See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition).  
  
## RolloutStep

A single rollout step with specified traffic allocation.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "trafficPercent": integer,
      "minDuration": string
    }  
  
Fields  
---  
`displayName` |  `string` The name of the rollout step;  
`trafficPercent` |  `integer` The percentage of traffic allocated to the flow version of this rollout step. (0%, 100%].  
`minDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The minimum time that this step should last. Should be longer than 1 hour. If not set, the default minimum duration for each step will be 1 hour.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## RolloutState

State of the auto-rollout process.

JSON representation  
---  
      
    
    {
      "step": string,
      "stepIndex": integer,
      "startTime": string
    }  
  
Fields  
---  
`step` |  `string` Display name of the current auto rollout step.  
`stepIndex` |  `integer` Index of the current step in the auto rollout steps list.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Start time of the current step.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Result

The inference result which includes an objective metric to optimize and the confidence interval.

JSON representation  
---  
      
    
    {
      "versionMetrics": [
        {
          object ([VersionMetrics](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#VersionMetrics))
        }
      ],
      "lastUpdateTime": string
    }  
  
Fields  
---  
`versionMetrics[]` |  `object (`[VersionMetrics](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#VersionMetrics)`)` Version variants and metrics.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last time the experiment's stats data was updated. Will have default value if stats have never been computed for this experiment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## VersionMetrics

Version variant and associated metrics.

JSON representation  
---  
      
    
    {
      "version": string,
      "metrics": [
        {
          object ([Metric](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Metric))
        }
      ],
      "sessionCount": integer
    }  
  
Fields  
---  
`version` |  `string` The name of the flow `[Version](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions#Version)`. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>`.  
`metrics[]` |  `object (`[Metric](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Metric)`)` The metrics and corresponding confidence intervals in the inference result.  
`sessionCount` |  `integer` Number of sessions that were allocated to this version.  
  
## Metric

Metric and corresponding confidence intervals.

JSON representation  
---  
      
    
    {
      "type": enum ([MetricType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#MetricType)),
      "countType": enum ([CountType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#CountType)),
      "confidenceInterval": {
        object ([ConfidenceInterval](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#ConfidenceInterval))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "ratio": number,
      "count": number
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`type` |  `enum (`[MetricType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#MetricType)`)` Ratio-based metric type. Only one of type or countType is specified in each Metric.  
`countType` |  `enum (`[CountType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#CountType)`)` Count-based metric type. Only one of type or countType is specified in each Metric.  
`confidenceInterval` |  `object (`[ConfidenceInterval](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#ConfidenceInterval)`)` The probability that the treatment is better than all other treatments in the experiment  
The actual value of the metric. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`ratio` |  `number` Ratio value of a metric.  
`count` |  `number` Count value of a metric.  
End of mutually exclusive fields.  
  
## MetricType

Types of ratio-based metric for Dialogflow experiment.

Enums  
---  
`METRIC_UNSPECIFIED` | Metric unspecified.  
`CONTAINED_SESSION_NO_CALLBACK_RATE` | Percentage of contained sessions without user calling back in 24 hours.  
`LIVE_AGENT_HANDOFF_RATE` | Percentage of sessions that were handed to a human agent.  
`CALLBACK_SESSION_RATE` | Percentage of sessions with the same user calling back.  
`ABANDONED_SESSION_RATE` | Percentage of sessions where user hung up.  
`SESSION_END_RATE` | Percentage of sessions reached Dialogflow 'END_PAGE' or 'END_SESSION'.  
  
## CountType

Types of count-based metric for Dialogflow experiment.

Enums  
---  
`COUNT_TYPE_UNSPECIFIED` | Count type unspecified.  
`TOTAL_NO_MATCH_COUNT` | Total number of occurrences of a 'NO_MATCH'.  
`TOTAL_TURN_COUNT` | Total number of turn counts.  
`AVERAGE_TURN_COUNT` | Average turn count in a session.  
  
## ConfidenceInterval

A confidence interval is a range of possible values for the experiment objective you are trying to measure.

JSON representation  
---  
      
    
    {
      "confidenceLevel": number,
      "ratio": number,
      "lowerBound": number,
      "upperBound": number
    }  
  
Fields  
---  
`confidenceLevel` |  `number` The confidence level used to construct the interval, i.e. there is X% chance that the true value is within this interval.  
`ratio` |  `number` The percent change between an experiment metric's value and the value for its control.  
`lowerBound` |  `number` Lower bound of the interval.  
`upperBound` |  `number` Upper bound of the interval.  
  
## VariantsHistory

The history of variants update.

JSON representation  
---  
      
    
    {
      "updateTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "versionVariants": {
        object ([VersionVariants](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#VersionVariants))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Update time of the variants.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
The variants updated. We currently only support single variant experiment. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`versionVariants` |  `object (`[VersionVariants](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#VersionVariants)`)` The flow versions as the variants.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/create)`

|  Creates an `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)` in the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/delete)`

|  Deletes the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/get)`

|  Retrieves the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/list)`

|  Returns the list of all experiments in the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/patch)`

|  Updates the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
  
### `[start](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/start)`

|  Starts the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
  
### `[stop](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/stop)`

|  Stops the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
