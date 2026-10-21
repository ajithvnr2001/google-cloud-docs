---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels
title: REST Resource: projects.locations.issueModels \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:39:51.714579+00:00
---

# REST Resource: projects.locations.issueModels  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.issueModels Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: IssueModel
    * JSON representation
  * State
  * InputDataConfig
    * JSON representation
  * IssueModelLabelStats
    * JSON representation
  * IssueStats
    * JSON representation
  * ModelType
  * Methods



## Resource: IssueModel

The issue model resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "issueCount": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#State)),
      "inputDataConfig": {
        object ([InputDataConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#InputDataConfig))
      },
      "trainingStats": {
        object ([IssueModelLabelStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#IssueModelLabelStats))
      },
      "modelType": enum ([ModelType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#ModelType)),
      "languageCode": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the issue model. Format: projects/{project}/locations/{location}/issueModels/{issueModel}  
`displayName` |  `string` The representative name for the issue model.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this issue model was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time at which the issue model was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`issueCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of issues in this issue model.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#State)`)` Output only. State of the model.  
`inputDataConfig` |  `object (`[InputDataConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#InputDataConfig)`)` Configs for the input data that used to create the issue model.  
`trainingStats` |  `object (`[IssueModelLabelStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#IssueModelLabelStats)`)` Output only. Immutable. The issue model's label statistics on its training data.  
`modelType` |  `enum (`[ModelType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#ModelType)`)` Type of the model.  
`languageCode` |  `string` Language of the model.  
  
## State

State of the model.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`UNDEPLOYED` | Model is not deployed but is ready to deploy.  
`DEPLOYING` | Model is being deployed.  
`DEPLOYED` | Model is deployed and is ready to be used. A model can only be used in analysis if it's in this state.  
`UNDEPLOYING` | Model is being undeployed.  
`DELETING` | Model is being deleted.  
  
## InputDataConfig

Configs for the input data used to create the issue model.

JSON representation  
---  
      
    
    {
      "medium": enum ([Medium](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Medium)),
      "trainingConversationsCount": string,
      "filter": string
    }  
  
Fields  
---  
`medium  
**(deprecated)**` |  `enum (`[Medium](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Medium)`)` This item is deprecated!Medium of conversations used in training data. This field is being deprecated. To specify the medium to be used in training a new issue model, set the `medium` field on `filter`.  
`trainingConversationsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of conversations used in training. Output only.  
`filter` |  `string` A filter to reduce the conversations used for training the model to a specific subset. Refer to <https://cloud.google.com/gemini-enterprise-cx/insights/filtering> for details.  
  
## IssueModelLabelStats

Aggregated statistics about an issue model.

JSON representation  
---  
      
    
    {
      "analyzedConversationsCount": string,
      "unclassifiedConversationsCount": string,
      "issueStats": {
        string: {
          object ([IssueStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#IssueStats))
        },
        ...
      }
    }  
  
Fields  
---  
`analyzedConversationsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of conversations the issue model has analyzed at this point in time.  
`unclassifiedConversationsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of analyzed conversations for which no issue was applicable at this point in time.  
`issueStats` |  `map (key: string, value: object (`[IssueStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#IssueStats)`))` Statistics on each issue. Key is the issue's resource name.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## IssueStats

Aggregated statistics about an issue.

JSON representation  
---  
      
    
    {
      "issue": string,
      "labeledConversationsCount": string,
      "displayName": string
    }  
  
Fields  
---  
`issue` |  `string` Issue resource. Format: projects/{project}/locations/{location}/issueModels/{issueModel}/issues/{issue}  
`labeledConversationsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of conversations attached to the issue at this point in time.  
`displayName` |  `string` Display name of the issue.  
  
## ModelType

Type of the model.

Enums  
---  
`MODEL_TYPE_UNSPECIFIED` | Unspecified model type.  
`TYPE_V1` | Type V1.  
`TYPE_V2` | Type V2.  
  
## Methods  
  
---  
  
### `[calculateIssueModelStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/calculateIssueModelStats)`

|  Gets an issue model's statistics.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/create)`

|  Creates an issue model.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/delete)`

|  Deletes an issue model.  
  
### `[deploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/deploy)`

|  Deploys an issue model.  
  
### `[export](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/export)`

|  Exports an issue model to the provided destination.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/get)`

|  Gets an issue model.  
  
### `[import](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/import)`

|  Imports an issue model from a Cloud Storage bucket.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/list)`

|  Lists issue models.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/patch)`

|  Updates an issue model.  
  
### `[undeploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/undeploy)`

|  Undeploys an issue model.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
