---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement/
title: Method: projects.locations.requirements.checkRequirement \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:51.928646+00:00
---

# Method: projects.locations.requirements.checkRequirement  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.requirements.checkRequirement Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Requirement
    * JSON representation
  * MetricBinding
    * JSON representation
  * ThresholdBinding
    * JSON representation
  * ThresholdValue
    * JSON representation
  * ViolationSamplesBinding
    * JSON representation
  * MetricQueryResult
    * JSON representation



Check a particular requirement.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{location=projects/*/locations/*}/requirements:checkRequirement`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`location` |  `string` Required. Full resource name of the location. Format `projects/{project_number_or_id}/locations/{location}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requirementType": string,
      "resources": [
        {
          object ([MonitoredResource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/MonitoredResource))
        }
      ]
    }  
  
Fields  
---  
`requirementType` |  `string` The type specifying the requirement to check. The supported types are:

  * `discoveryengine.googleapis.com/media_recs/general/all/warning`
  * `discoveryengine.googleapis.com/media_recs/oyml/cvr/warning`
  * `discoveryengine.googleapis.com/media_recs/rfy/cvr/warning`
  * `discoveryengine.googleapis.com/media_recs/mlt/cvr/warning`
  * `discoveryengine.googleapis.com/media_recs/mp/cvr/warning`
  * `discoveryengine.googleapis.com/media_recs/oyml/wdps/warning`
  * `discoveryengine.googleapis.com/media_recs/rfy/wdps/warning`
  * `discoveryengine.googleapis.com/media_recs/mlt/wdps/warning`

  
`resources[]` |  `object (`[MonitoredResource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/MonitoredResource)`)` The resources to be checked for this requirement. The type needed for the monitored resources:

  * `discoveryengine.googleapis.com/Branch`.
    * The labels needed for this resource: 
      * `project_number`
      * `location_id`
      * `collection_id`
      * `datastore_id`
      * `branch_id`
  * `discoveryengine.googleapis.com/DataStore`
    * The labels needed for this resource: 
      * `project_number`
      * `location_id`
      * `collection_id`
      * `datastore_id`

  
  
### Response body

Response for the requirements.checkRequirement method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requirement": {
        object ([Requirement](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#Requirement))
      },
      "requirementCondition": {
        object ([Expr](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/Binding#Expr))
      },
      "metricResults": [
        {
          object ([MetricQueryResult](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#MetricQueryResult))
        }
      ],
      "oldestMetricTimestamp": string,
      "result": string
    }  
  
Fields  
---  
`requirement` |  `object (`[Requirement](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#Requirement)`)` Requirement definition.  
`requirementCondition` |  `object (`[Expr](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/Binding#Expr)`)` The condition for evaluating the requirement result.  
`metricResults[]` |  `object (`[MetricQueryResult](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#MetricQueryResult)`)` Metric results.  
`oldestMetricTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the oldest calculated metric (i.e. the most stale metric). Indicates that the `result` may not accurately reflect any Event and Product Catalog updates performed after this time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`result` |  `string` The result of the requirement. It should be one of the `severity` fields in the requirement definition. If any error happens during the evaluation, it will be `UNKNOWN`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Requirement

A data requirement.

JSON representation  
---  
      
    
    {
      "type": string,
      "displayName": string,
      "description": string,
      "condition": {
        object ([Expr](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/Binding#Expr))
      },
      "metricBindings": [
        {
          object ([MetricBinding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#MetricBinding))
        }
      ],
      "thresholdBindings": [
        {
          object ([ThresholdBinding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#ThresholdBinding))
        }
      ],
      "violationSamplesBindings": [
        {
          object ([ViolationSamplesBinding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#ViolationSamplesBinding))
        }
      ],
      "severity": [
        string
      ]
    }  
  
Fields  
---  
`type` |  `string` The requirement type, used as an identifier. Must be unique.The type should prefix with service name to avoid possible collision. It's encouraged to use natural hierarchical grouping for similar requirements.Examples:

  * `library.googleapis.com/books/min_available_books`
  * `discoveryengine.googleapis.com/media_rec/recommended_for_you/conversion_rate`

  
`displayName` |  `string` The name of the requirement.  
`description` |  `string` The description of the requirement.  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/Binding#Expr)`)` The condition for evaluating the requirement result.Variables in the expression should be provided by `metrics_bindings` or `thresholdBindings`. Where `metrics_bindings` are used for computed metrics and `thresholdBindings` are used to define thresholds for corresponding `metricBindings`.  
`metricBindings[]` |  `object (`[MetricBinding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#MetricBinding)`)` A list of the metric bindings to be used in `condition`.  
`thresholdBindings[]` |  `object (`[ThresholdBinding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#ThresholdBinding)`)` A list of threshold bindings to be used in `condition`.  
`violationSamplesBindings[]` |  `object (`[ViolationSamplesBinding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#ViolationSamplesBinding)`)` A list of the metric bindings to be used in `condition`.  
`severity[]` |  `string` The severity of errors if the requirement is not met. It must be ordered from the most strict to the least strict. Examples:

  * `BLOCKING`
  * `CRITICAL`
  * `WARNING`

All thresholds in the requirement must have all the severity here.  
  
## MetricBinding

Specifies a metrics query and bind its result to a variable which will be used in the `condition`.

JSON representation  
---  
      
    
    {
      "variableId": string,
      "resourceType": string,
      "metricFilter": string,
      "description": string,
      "category": string
    }  
  
Fields  
---  
`variableId` |  `string` The variable ID to be referenced in `condition`.  
`resourceType` |  `string` The resource being monitored for the metric.  
`metricFilter` |  `string` The filter string used for metrics query.Example:"metric.type = "discoveryengine.googleapis.com/events/day_count" AND " "metric.conditions.time_range = "NINETY_DAYS""  
`description` |  `string` Human readable description of the corresponding metric filter.  
`category` |  `string` The category of the metric's target resource. Example: "Events"  
  
## ThresholdBinding

Specifies a multi-level threshold to apply to apply to a `metricBindings` in the `condition` CEL expression.

JSON representation  
---  
      
    
    {
      "variableId": string,
      "description": string,
      "thresholdValues": [
        {
          object ([ThresholdValue](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#ThresholdValue))
        }
      ]
    }  
  
Fields  
---  
`variableId` |  `string` The variable ID to be referenced in `condition`. Must be unique across all `metricBindings` and `thresholdBindings`.  
`description` |  `string` Human readable description of the corresponding threshold and sub-requirement.  
`thresholdValues[]` |  `object (`[ThresholdValue](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.requirements/checkRequirement#ThresholdValue)`)` The values of the threshold. The values should be ordered from the most strict to the least strict.  
  
## ThresholdValue

Specifies a threshold value for a given severity.

JSON representation  
---  
      
    
    {
      "severity": string,
      "value": number
    }  
  
Fields  
---  
`severity` |  `string` The severity of errors if the threshold is not met. It should be one of the `severity` fields in the requirement.  
`value` |  `number` The value of the threshold.  
  
## ViolationSamplesBinding

Specifies a samples query and bind its result to a variable which will be used in the `condition`.

JSON representation  
---  
      
    
    {
      "variableId": string,
      "sampleFilter": string,
      "description": string
    }  
  
Fields  
---  
`variableId` |  `string` The variable ID to be referenced in `condition`.  
`sampleFilter` |  `string` The filter string used for samples query.Example: "sample.type = "retail.googleapis.com/userEvent" AND " "sample.labels.event_type = "PURCHASE" "  
`description` |  `string` Description of this sample binding. Used by the UI to render user friendly descriptions for each requirement condition.Should be less than 128 characters long.  
  
## MetricQueryResult

Metric result. The metric are in the requirementCondition.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": {
        object ([TypedValue](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/Point#TypedValue))
      },
      "timestamp": string,
      "unit": string,
      "metricType": string
    }  
  
Fields  
---  
`name` |  `string` This metric query name is mapping to variables in the requirementCondition.  
`value` |  `object (`[TypedValue](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/Point#TypedValue)`)` Value of the metric query.  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time corresponding to when this metric value was calculated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`unit` |  `string` The unit in which this metric is reported. Follows [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard.  
`metricType` |  `string` Type identifier of the metric corresponding to this query result.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
