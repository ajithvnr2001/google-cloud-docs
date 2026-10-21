---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/rollbackTarget/
title: Method: projects.locations.deliveryPipelines.rollbackTarget \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:57.550974+00:00
---

# Method: projects.locations.deliveryPipelines.rollbackTarget  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/rollbackTarget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  Method: projects.locations.deliveryPipelines.rollbackTarget Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * RollbackTargetConfig
    * JSON representation
  * Try it!



Creates a `Rollout` to roll back the specified target.

### HTTP request

Choose a location:

global asia-south1 asia-south2 us-central1 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4

  
`POST https://clouddeploy.googleapis.com/v1/{name=projects/*/locations/*/deliveryPipelines/*}:rollbackTarget`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The `DeliveryPipeline` for which the rollback `Rollout` must be created. The format is `projects/{projectId}/locations/{location_name}/deliveryPipelines/{pipeline_name}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "targetId": string,
      "rolloutId": string,
      "releaseId": string,
      "rolloutToRollBack": string,
      "rollbackConfig": {
        object ([RollbackTargetConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/rollbackTarget#RollbackTargetConfig))
      },
      "validateOnly": boolean,
      "overrideDeployPolicy": [
        string
      ]
    }  
  
Fields  
---  
`targetId` |  `string` Required. ID of the `Target` that is being rolled back.  
`rolloutId` |  `string` Required. ID of the rollback `Rollout` to create.  
`releaseId` |  `string` Optional. ID of the `Release` to roll back to. If this isn't specified, the previous successful `Rollout` to the specified target will be used to determine the `Release`.  
`rolloutToRollBack` |  `string` Optional. If provided, this must be the latest `Rollout` that is on the `Target`.  
`rollbackConfig` |  `object (`[RollbackTargetConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/rollbackTarget#RollbackTargetConfig)`)` Optional. Configs for the rollback `Rollout`.  
`validateOnly` |  `boolean` Optional. If set to true, the request is validated and the user is provided with a `RollbackTargetResponse`.  
`overrideDeployPolicy[]` |  `string` Optional. Deploy policies to override. Format is `projects/{project}/locations/{location}/deployPolicies/{deployPolicy}`.  
  
### Response body

The response object from `deliveryPipelines.rollbackTarget`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rollbackConfig": {
        object ([RollbackTargetConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/rollbackTarget#RollbackTargetConfig))
      }
    }  
  
Fields  
---  
`rollbackConfig` |  `object (`[RollbackTargetConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/rollbackTarget#RollbackTargetConfig)`)` The config of the rollback `Rollout` created or will be created.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `clouddeploy.rollouts.rollback`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## RollbackTargetConfig

Configs for the Rollback rollout.

JSON representation  
---  
      
    
    {
      "rollout": {
        object ([Rollout](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Rollout))
      },
      "startingPhaseId": string
    }  
  
Fields  
---  
`rollout` |  `object (`[Rollout](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Rollout)`)` Optional. The rollback `Rollout` to create.  
`startingPhaseId` |  `string` Optional. The starting phase ID for the `Rollout`. If unspecified, the `Rollout` will start in the stable phase.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
