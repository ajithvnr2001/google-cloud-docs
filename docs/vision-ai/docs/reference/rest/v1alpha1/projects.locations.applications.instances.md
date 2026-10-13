---
url: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances
title: REST Resource: projects.locations.applications.instances \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:01.753428+00:00
---

# REST Resource: projects.locations.applications.instances  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback 

#  REST Resource: projects.locations.applications.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * InputResource
    * JSON representation
  * OutputResource
    * JSON representation
  * State
  * Methods



## Resource: Instance

Message describing Instance object

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
      "description": string,
      "inputResources": [
        {
          object ([InputResource](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances#InputResource))
        }
      ],
      "outputResources": [
        {
          object ([OutputResource](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances#OutputResource))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances#State))
    }  
  
Fields  
---  
`name` |  `string` Output only. name of resource  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. [Output only] Create timestampA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. [Output only] Update timestampA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` Required. A user friendly display name for the solution.  
`description` |  `string` A description for this application.  
`inputResources[]` |  `object (`[InputResource](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances#InputResource)`)` The input resources for the current application instance. For example: inputResources: visionai.googleapis.com/v1/projects/123/locations/us-central1/clusters/456/streams/stream-a  
`outputResources[]` |  `object (`[OutputResource](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances#OutputResource)`)` All the output resources associated to one application instance.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances#State)`)` State of the instance.  
  
## InputResource

Message of input resource used in one application instance.

JSON representation  
---  
      
    
    {
      "consumerNode": string,
      "inputResourceBinding": string,
    
      // Union field input_resource_information can be only one of the following:
      "inputResource": string,
      "annotatedStream": {
        object ([StreamWithAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/StreamWithAnnotation))
      }
      // End of list of possible types for union field input_resource_information.
    }  
  
Fields  
---  
`consumerNode` |  `string` The name of graph node who receives the input resource. For example: inputResource: visionai.googleapis.com/v1/projects/123/locations/us-central1/clusters/456/streams/input-stream-a consumerNode: stream-input  
`inputResourceBinding` |  `string` The specific input resource binding which will consume the current Input Resource, can be ignored is there is only 1 input binding.  
Union field `input_resource_information`. Required. Specify the input to the application instance. `input_resource_information` can be only one of the following:  
`inputResource` |  `string` The direct input resource name.  
`annotatedStream` |  `object (`[StreamWithAnnotation](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/StreamWithAnnotation)`)` If the input resource is VisionAI Stream, the associated annotations can be specified using annotatedStream instead.  
  
## OutputResource

Message of output resource used in one application instance.

JSON representation  
---  
      
    
    {
      "outputResource": string,
      "producerNode": string,
      "outputResourceBinding": string,
      "isTemporary": boolean,
      "autogen": boolean
    }  
  
Fields  
---  
`outputResource` |  `string` The output resource name for the current application instance.  
`producerNode` |  `string` The name of graph node who produces the output resource name. For example: outputResource: /projects/123/locations/us-central1/clusters/456/streams/output-application-789-stream-a-occupancy-counting producerNode: occupancy-counting  
`outputResourceBinding` |  `string` The specific output resource binding which produces the current OutputResource.  
`isTemporary` |  `boolean` Output only. Whether the output resource is temporary which means the resource is generated during the deployment of the application. Temporary resource will be deleted during the undeployment of the application.  
`autogen` |  `boolean` Output only. Whether the output resource is created automatically by the Vision AI App Platform.  
  
## State

State of the Instance

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the state is omitted.  
`CREATING` | State CREATING.  
`CREATED` | State CREATED.  
`DEPLOYING` | State DEPLOYING.  
`DEPLOYED` | State DEPLOYED.  
`UNDEPLOYING` | State UNDEPLOYING.  
`DELETED` | State DELETED.  
`ERROR` | State ERROR.  
`UPDATING` | State Updating  
`DELETING` | State Deleting.  
`FIXING` | State Fixing.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances/get)`

|  Gets details of a single Instance.  
  
### `[list](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.instances/list)`

|  Lists Instances in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
