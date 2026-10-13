---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.customModels/list/
title: Method: projects.locations.collections.dataStores.customModels.list \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:09.298110+00:00
---

# Method: projects.locations.collections.dataStores.customModels.list  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.customModels/list/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.customModels.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * CustomTuningModel
    * JSON representation
  * ModelState



Gets a list of all the custom models.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1alpha/{dataStore=projects/*/locations/*/collections/*/dataStores/*}/customModels`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`dataStore` |  `string` Required. The resource name of the parent Data Store, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store`. This field is used to identify the data store where to fetch the models from.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[SearchTuningService.ListCustomModels](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.customModels/list#google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustomModels)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "models": [
        {
          object ([CustomTuningModel](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.customModels/list#CustomTuningModel))
        }
      ]
    }  
  
Fields  
---  
`models[]` |  `object (`[CustomTuningModel](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.customModels/list#CustomTuningModel)`)` List of custom tuning models.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `dataStore` resource:

  * `discoveryengine.dataStores.listCustomModels`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CustomTuningModel

Metadata that describes a custom tuned model.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "modelVersion": string,
      "modelState": enum ([ModelState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.customModels/list#ModelState)),
      "createTime": string,
      "trainingStartTime": string,
      "metrics": {
        string: number,
        ...
      },
      "errorMessage": string
    }  
  
Fields  
---  
`name` |  `string` Required. The fully qualified resource name of the model.Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/customTuningModels/{custom_tuning_model}`.Model must be an alpha-numerical string with limit of 40 characters.  
`displayName` |  `string` The display name of the model.  
`modelVersion` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The version of the model.  
`modelState` |  `enum (`[ModelState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.customModels/list#ModelState)`)` The state that the model is in (e.g.`TRAINING` or `TRAINING_FAILED`).  
`createTime  
**(deprecated)**` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` This item is deprecated!Deprecated: Timestamp the Model was created at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`trainingStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp the model training was initiated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`metrics` |  `map (key: string, value: number)` The metrics of the trained model.  
`errorMessage` |  `string` Currently this is only populated if the model state is `INPUT_VALIDATION_FAILED`.  
  
## ModelState

The state of the model.

Enums  
---  
`MODEL_STATE_UNSPECIFIED` | Default value.  
`TRAINING_PAUSED` | The model is in a paused training state.  
`TRAINING` | The model is currently training.  
`TRAINING_COMPLETE` | The model has successfully completed training.  
`READY_FOR_SERVING` | The model is ready for serving.  
`TRAINING_FAILED` | The model training failed.  
`NO_IMPROVEMENT` | The model training finished successfully but metrics did not improve.  
`INPUT_VALIDATION_FAILED` | Input data validation failed. Model training didn't start.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
