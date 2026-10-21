---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/promote/
title: Method: projects.locations.deliveryPipelines.releases.promote \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:40:18.274210+00:00
---

# Method: projects.locations.deliveryPipelines.releases.promote  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/promote/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)



Send feedback 

#  Method: projects.locations.deliveryPipelines.releases.promote Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization Scopes
  * Promotion
    * JSON representation
  * Try it!



Promotes a Release in the Delivery Pipeline.

### HTTP request

`POST https://clouddeploy.googleapis.com/v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*}:promote`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The `Release` being promoted. Format is projects/{projectId}/locations/{location_name}/deliveryPipelines/{pipeline_name}/release/{release_name}.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "toTarget": string,
      "destinationTarget": string,
      "rolloutId": string,
      "annotations": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`toTarget` |  `string` Optional. The name of the `Target` to which we are promoting the Release.  
`destinationTarget` |  `string` Optional. The name of the `Target` to which we are promoting the Release.  
`rolloutId` |  `string` Optional. The ID to assign to the generated `Rollout`.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations to place on the created `Rollout`. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels to be placed on the created `Rollout`. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: Each resource is limited to 64 labels. Keys must conform to the regexp: [a-zA-Z][a-zA-Z0-9_-]{0,62} Values must conform to the regexp: [a-zA-Z0-9_-]{0,63} Both keys and values are additionally constrained to be <= 128 bytes in size.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### Response body

If successful, the response body contains data with the following structure:

The response object from `releases.promote`.

JSON representation  
---  
      
    
    {
      "release": string,
      "rollout": {
        object ([Promotion](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/promote#Promotion))
      },
      "rolloutResource": string,
      "target": string,
      "operation": string
    }  
  
Fields  
---  
`release` |  `string` The `Release` being deployed.  
`rollout` |  `object (`[Promotion](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/promote#Promotion)`)` `Rollout` that was created from this promotion.  
`rolloutResource` |  `string` The name of the `Rollout` that is being deployed.  
`target` |  `string` The name of the `Target` to which is being deployed.  
`operation` |  `string` The name of the operation that is tracking the `Rollout` creation.  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Promotion

Details around a `Release` promotion.

JSON representation  
---  
      
    
    {
      "target": string,
      "rollout": string,
      "operation": string
    }  
  
Fields  
---  
`target` |  `string` The name of the `Target` to which is being deployed.  
`rollout` |  `string` The name of the `Rollout` that is being deployed.  
`operation` |  `string` The name of the operation that is tracking the `Rollout` creation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
