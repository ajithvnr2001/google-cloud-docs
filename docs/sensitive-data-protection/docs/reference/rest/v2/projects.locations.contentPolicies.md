---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies
title: REST Resource: projects.locations.contentPolicies \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:32.861309+00:00
---

# REST Resource: projects.locations.contentPolicies  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.locations.contentPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ContentPolicy
    * JSON representation
  * PolicyRule
    * JSON representation
  * PolicyCondition
    * JSON representation
  * InfoTypeCondition
    * JSON representation
  * InfoTypes
    * JSON representation
  * PolicyAction
    * JSON representation
  * ContentPolicyVerdict
  * LoggingConfig
    * JSON representation
  * LogToBigQuery
    * JSON representation
  * Methods



## Resource: ContentPolicy

A policy to apply to content based on its inspection findings.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "displayName": string,
      "inspectConfig": {
        object ([InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig))
      },
      "rules": [
        {
          object ([PolicyRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyRule))
        }
      ],
      "unsupportedFileType": {
        object ([PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction))
      },
      "inputTooLarge": {
        object ([PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction))
      },
      "failedToScanSupportedFileType": {
        object ([PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction))
      },
      "defaultAction": {
        object ([PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction))
      },
      "loggingConfigs": [
        {
          object ([LoggingConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#LoggingConfig))
        }
      ],
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name of the policy.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of a contentPolicy; output-only field.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of a contentPolicy; output-only field.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Optional. Display name (max 63 chars)  
`inspectConfig` |  `object (`[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`)` Optional. InspectConfig to use to produce findings.  
`rules[]` |  `object (`[PolicyRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyRule)`)` Required. Policies to apply, based on the findings returned by inspection. The first rule to match applies.  
`unsupportedFileType` |  `object (`[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction)`)` Optional. Action to take if the content is an unsupported file type.  
`inputTooLarge` |  `object (`[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction)`)` Optional. Action to take if the content is a supported file type but is too large to be scanned.  
`failedToScanSupportedFileType` |  `object (`[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction)`)` Optional. Action to take if the content is a supported file type and size but fails to be scanned, for example because the file is encrypted or corrupted.  
`defaultAction` |  `object (`[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction)`)` Action to take if the content is scanned and no rules match. Defaults to returning an ALLOW verdict if not set.  
`loggingConfigs[]` |  `object (`[LoggingConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#LoggingConfig)`)` Optional. Log the actions taken by the content policy to external systems.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` Output only. A stream of errors encountered when the policy was applied. Output only field. Will return the last 100 errors. Whenever the policy is modified this list will be cleared.  
  
## PolicyRule

A single policy rule. The first rule to match from the list above controls the result.

JSON representation  
---  
      
    
    {
      "conditions": [
        {
          object ([PolicyCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyCondition))
        }
      ],
      "action": {
        object ([PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction))
      }
    }  
  
Fields  
---  
`conditions[]` |  `object (`[PolicyCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyCondition)`)` Optional. Conditions that must match for this rule to apply. All conditions must match (`AND`). For `OR` conditions, use multiple rules.  
`action` |  `object (`[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyAction)`)` Required. Action to take if this rule applies.  
  
## PolicyCondition

A condition that must match for this rule to apply.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "infoTypeCondition": {
        object ([InfoTypeCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#InfoTypeCondition))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
A condition. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`infoTypeCondition` |  `object (`[InfoTypeCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#InfoTypeCondition)`)` A condition based on info types.  
End of mutually exclusive fields.  
  
## InfoTypeCondition

A info type based condition.

JSON representation  
---  
      
    
    {
      "minCount": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "infoTypes": {
        object ([InfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#InfoTypes))
      },
      "anyInfoType": {
        object
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`minCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The minimum total number of findings of all matching info types required for this condition to evaluate to true. Defaults to 1 if unset.  
A condition based on info types. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`infoTypes` |  `object (`[InfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#InfoTypes)`)` match any of these info types.  
`anyInfoType` |  `object` match any info types.  
End of mutually exclusive fields.  
  
## InfoTypes

Info types to match.

JSON representation  
---  
      
    
    {
      "infoTypeNames": [
        string
      ]
    }  
  
Fields  
---  
`infoTypeNames[]` |  `string` Required. A list of info types to match.  
  
## PolicyAction

A possible action to take when applying a content policy.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "returnVerdict": enum ([ContentPolicyVerdict](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#ContentPolicyVerdict))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`returnVerdict` |  `enum (`[ContentPolicyVerdict](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#ContentPolicyVerdict)`)` Optional. If set, the verdict will be returned to the user.  
End of mutually exclusive fields.  
  
## ContentPolicyVerdict

Possible results of applying a content policy. This may expand to include additional result types in the future.

Enums  
---  
`CONTENT_POLICY_VERDICT_UNSPECIFIED` | Not used.  
`ALLOW` | The policy allows the provided content to be used.  
`BLOCK` | The policy prevents the provided content from being used. This should result in a blocked file upload, exclusion from training dataset, or other similar block action. (specific action will depend on the caller).  
  
## LoggingConfig

A single logging configuration.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "logToBigQuery": {
        object ([LogToBigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#LogToBigQuery))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The destination for the action logs. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`logToBigQuery` |  `object (`[LogToBigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#LogToBigQuery)`)` Optional. Log the actions taken to a BigQuery table.  
End of mutually exclusive fields.  
  
## LogToBigQuery

Configuration for logging content policy actions to BigQuery.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "datasetId": string,
      "tableId": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. The ID of the project containing the BigQuery table to write to.  
`datasetId` |  `string` Required. The ID of the dataset containing the BigQuery table to write to.  
`tableId` |  `string` Required. The ID of the BigQuery table to write to.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/create)`

|  Create a ContentPolicy.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/delete)`

|  Delete a ContentPolicy.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/get)`

|  Get a ContentPolicy.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/list)`

|  Lists ContentPolicies in a parent.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/patch)`

|  Update a ContentPolicy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
