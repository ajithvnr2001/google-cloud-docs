---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements
title: REST Resource: projects.locations.instances.findingsRefinements \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:14.248040+00:00
---

# REST Resource: projects.locations.instances.findingsRefinements  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.findingsRefinements Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: FindingsRefinement
    * JSON representation
  * FindingsRefinementType
  * OutcomeFilter
    * JSON representation
  * Operator
  * Methods



## Resource: FindingsRefinement

Represents a set of logic conditions used to refine various types of findings such as curated rule detections.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "type": enum ([FindingsRefinementType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements#FindingsRefinementType)),
      "createTime": string,
      "updateTime": string,
      "query": string,
      "outcomeFilters": [
        {
          object ([OutcomeFilter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements#OutcomeFilter))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Full resource name for the findings refinement. Format: projects/{project}/locations/{region}/instances/{instance}/findingsRefinements/{findingsRefinement}  
`displayName` |  `string` Display name of the findings refinement.  
`type` |  `enum (`[FindingsRefinementType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements#FindingsRefinementType)`)` The type of findings refinement.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the findings refinement was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the findings refinement was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`query` |  `string` The query for the findings refinement. Works in conjunction with the type field to determine the findings refinement behavior. The syntax of this query is the same as a UDM search string. See the following for more information: <https://cloud.google.com/chronicle/docs/investigation/udm-search>  
`outcomeFilters[]` |  `object (`[OutcomeFilter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements#OutcomeFilter)`)` Optional. The outcome filters for the findings refinement. These allow you to specify filters that are applied to the outcome variables in the detection. All filters must be true for a detection to match the findings refinement.  
  
## FindingsRefinementType

The type of findings refinement, which determines what the findings refinement runs over and the mechanism by which it runs.

Enums  
---  
`FINDINGS_REFINEMENT_TYPE_UNSPECIFIED` | The findings refinement type is unspecified.  
`DETECTION_EXCLUSION` | Indicates that the findings refinement is a detection exclusion and should exclude matching detections.  
  
## OutcomeFilter

Outcome filter for the findings refinement. This is used to filter the findings refinement based on the outcome variable values.

JSON representation  
---  
      
    
    {
      "outcomeVariable": string,
      "outcomeValue": string,
      "outcomeFilterOperator": enum ([Operator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements#Operator))
    }  
  
Fields  
---  
`outcomeVariable` |  `string` Required. The outcome variable name.  
`outcomeValue` |  `string` Required. The value of the outcome variable to match.  
`outcomeFilterOperator` |  `enum (`[Operator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements#Operator)`)` Required. The operator to be applied to the outcome variable.  
  
## Operator

The operator to compare the outcome variable value with the outcome value in the outcome filter.

Enums  
---  
`OPERATOR_UNSPECIFIED` | The operator is unspecified.  
`EQUAL` | The outcome variable value must be equal to the outcome value in the outcome filter.  
`CONTAINS` | The outcome variable value must contain the outcome value in the outcome filter.  
`MATCHES_REGEX` | The outcome variable value must match the outcome value regex in the outcome filter.  
`MATCHES_CIDR` | The outcome variable value must be a valid IP address in the outcome filter value CIDR range.  
  
## Methods  
  
---  
  
### `[computeFindingsRefinementActivity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements/computeFindingsRefinementActivity)`

|  Returns findings refinement activity for a specific findings refinement.  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements/create)`

|  Creates a new findings refinement.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements/get)`

|  Gets a single findings refinement.  
  
### `[getDeployment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements/getDeployment)`

|  Gets a findings refinement deployment.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements/list)`

|  Lists a collection of findings refinements.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements/patch)`

|  Updates a findings refinement.  
  
### `[updateDeployment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.findingsRefinements/updateDeployment)`

|  Updates a findings refinement deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-22 UTC."],[],[]] 
