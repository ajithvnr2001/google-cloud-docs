---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/rollouts/get/
title: Method: rollouts.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:58.574205+00:00
---

# Method: rollouts.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/rollouts/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: rollouts.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * Try it!



API Version : 2026-09-01

Gets details of a single project-scoped Rollout.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/rollouts/{rollout}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`rollout` |  `string` Name of the persistent rollout to return.  
  
### Request body

The request body must be empty.

### Response body

Rollout resource.

A Rollout is a specific instance of a RolloutPlan. It represents a single execution of a strategy to roll out a specific resource. It also provides APIs to interact with the rollout.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "selfLink": string,
      "selfLinkWithId": string,
      "rolloutEntity": {
        "orchestratedEntity": {
          "orchestrationAction": string,
          "orchestrationSource": string,
          "conflictBehavior": string
        }
      },
      "rolloutPlan": string,
      "state": enum,
      "etag": string,
      "currentWaveNumber": string,
      "waveDetails": [
        {
          "orchestratedWaveDetails": {
            "estimatedTotalResourcesCount": string,
            "completedResourcesCount": string,
            "failedResourcesCount": string,
            "failedLocations": [
              string
            ],
            "locationStatus": {
              string: {
                "state": enum
              },
              ...
            },
            "estimatedCompletionTime": string
          },
          "waveDisplayName": string,
          "waveNumber": string
        }
      ],
      "completionTime": string,
      "cancellationTime": string,
      "pauseTime": string,
      "resumeTime": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#rollout` for rollouts.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`selfLinkWithId` |  `string` Output only. Server-defined URL for this resource's resource id.  
`rolloutEntity` |  `object` Required. The resource being rolled out.  
`rolloutEntity.orchestratedEntity` |  `object` Optional. Entity details for products using the Orchestrated Integration model.  
`rolloutEntity.orchestratedEntity.orchestrationAction` |  `string` Required. Orchestration action during the Rollout. It can be one of the following values: 1) "update": Resources will be updated by the rollout. 2) "delete": Resources will be deleted by the rollout.  
`rolloutEntity.orchestratedEntity.orchestrationSource` |  `string` Required. Fully qualified resource name of the resource which contains the source of truth of the configuration being rolled out across locations/projects. For example, in the case of a global Rollout which is applied across regions, this contains the name of the global resource created by the user which contains a payload for a resource that is orchestrated across regions. This follows the following format: //.googleapis.com/projects//locations/global// e.g. //osconfig.googleapis.com/projects/1/locations/global/policyOrchestrators/po1  
`rolloutEntity.orchestratedEntity.conflictBehavior` |  `string` Required. Specifies the behavior of the Rollout if an out of band update is detected in a project during a Rollout. It can be one of the following values: 1) overwrite : Overwrite the local value with the rollout value. 2) no_overwrite : Do not overwrite the local value with the rollout value.  
`rolloutPlan` |  `string` Required. Rollout Plan used to model the Rollout. Ex. compute.googleapis.com/v1/projects/1234/rolloutPlans/rp1  
`state` |  `enum` Output only. The current state of the Rollout.  
`etag` |  `string` Output only. etag of the Rollout Ex. abc1234  
`currentWaveNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of the currently running wave. Ex. 1  
`waveDetails[]` |  `object` Output only. Details about each wave of the rollout.  
`waveDetails[].orchestratedWaveDetails` |  `object` Output only. Additional details of the wave for products using the Orchestrated Integration model.  
`waveDetails[].orchestratedWaveDetails.estimatedTotalResourcesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Estimated total count of resources.  
`waveDetails[].orchestratedWaveDetails.completedResourcesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Resource completed so far.  
`waveDetails[].orchestratedWaveDetails.failedResourcesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Resources failed.  
`waveDetails[].orchestratedWaveDetails.failedLocations[]` |  `string` Output only. Locations that failed during orchestration, and ProgressiveRollout stopped retrying. There may be some successful resources rolled out in the wave as the location may have failed later in the Rollout.  
`waveDetails[].orchestratedWaveDetails.locationStatus[]` |  `map (key: string, value: object)` Output only. Status of each location in the wave. Map keys (locations) must be specified like "us-east1" or "asia-west1-a".  
`waveDetails[].orchestratedWaveDetails.locationStatus[].state` |  `enum` Output only. Location state of the wave.  
`waveDetails[].orchestratedWaveDetails.estimatedCompletionTime` |  `string` Output only. Estimated timestamp at which the wave will complete. Extrapolated from current progress.  
`waveDetails[].waveDisplayName` |  `string` Output only. Wave name. Ex. wave1  
`waveDetails[].waveNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. System generated number for the wave.  
`completionTime` |  `string` Output only. The timestamp at which the Rollout was completed.  
`cancellationTime` |  `string` Output only. The timestamp at which the Rollout was cancelled.  
`pauseTime` |  `string` Output only. The timestamp at which the Rollout was paused.  
`resumeTime` |  `string` Output only. The timestamp at which the Rollout was resumed.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
