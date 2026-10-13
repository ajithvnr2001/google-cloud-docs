---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/rollouts/list/
title: Method: rollouts.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:20.669321+00:00
---

# Method: rollouts.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/rollouts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: rollouts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * Try it!



API Version : 2026-09-01

Lists Rollouts in a given project and location.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/rollouts?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)  
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.  
`filter` |  `string` A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal [AIP-160](https://google.aip.dev/160). These two types of filter expressions cannot be mixed in one request.If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use:
    
    
    labels.owner:*
    

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based on [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources).To filter on multiple expressions, provide each separate expression within parentheses. For example:
    
    
    (scheduling.automaticRestart = true)
    (cpuPlatform = "Intel Skylake")
    

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example:
    
    
    (cpuPlatform = "Intel Skylake") OR
    (cpuPlatform = "Intel Broadwell") AND
    (scheduling.automaticRestart = true)
    

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`The literal value is interpreted as a regular expression using Google [RE2](https://github.com/google/re2/wiki/Syntax) library syntax. The literal value must match the entire field.For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.You cannot combine constraints on multiple fields using regular expressions.  
`orderBy` |  `string` Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.Currently, only sorting by `name` or `creationTimestamp desc` is supported.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "id": string,
      "items": [
        {
          "kind": string,
          "id": string,
          "creationTimestamp": string,
          "name": string,
          "description": string,
          "selfLink": string,
          "selfLinkWithId": string,
          "rolloutEntity": {
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "orchestratedEntity": {
              "orchestrationAction": string,
              "orchestrationSource": string,
              "conflictBehavior": string
            }
            // End of mutually exclusive fields.
          },
          "rolloutPlan": string,
          "state": enum,
          "etag": string,
          "currentWaveNumber": string,
          "waveDetails": [
            {
              "waveDisplayName": string,
              "waveNumber": string,
    
              // The following is a list of mutually exclusive fields. At most one of the
              // fields will be set in a response:
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
              }
              // End of mutually exclusive fields.
            }
          ],
          "completionTime": string,
          "cancellationTime": string,
          "pauseTime": string,
          "resumeTime": string
        }
      ],
      "nextPageToken": string,
      "selfLink": string,
      "warning": {
        "code": enum,
        "message": string,
        "data": [
          {
            "key": string,
            "value": string
          }
        ]
      },
      "etag": string,
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of Rollout resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#rollout` for rollouts.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`items[].selfLinkWithId` |  `string` Output only. Server-defined URL for this resource's resource id.  
`items[].rolloutEntity` |  `object` Required. The resource being rolled out.  
`items[].rolloutEntity.orchestratedEntity` |  `object` Optional. Entity details for products using the Orchestrated Integration model.  
`items[].rolloutEntity.orchestratedEntity.orchestrationAction` |  `string` Required. Orchestration action during the Rollout. It can be one of the following values: 1) "update": Resources will be updated by the rollout. 2) "delete": Resources will be deleted by the rollout.  
`items[].rolloutEntity.orchestratedEntity.orchestrationSource` |  `string` Required. Fully qualified resource name of the resource which contains the source of truth of the configuration being rolled out across locations/projects. For example, in the case of a global Rollout which is applied across regions, this contains the name of the global resource created by the user which contains a payload for a resource that is orchestrated across regions. This follows the following format: //.googleapis.com/projects//locations/global// e.g. //osconfig.googleapis.com/projects/1/locations/global/policyOrchestrators/po1  
`items[].rolloutEntity.orchestratedEntity.conflictBehavior` |  `string` Required. Specifies the behavior of the Rollout if an out of band update is detected in a project during a Rollout. It can be one of the following values: 1) overwrite : Overwrite the local value with the rollout value. 2) no_overwrite : Do not overwrite the local value with the rollout value.  
`items[].rolloutPlan` |  `string` Required. Rollout Plan used to model the Rollout. Ex. compute.googleapis.com/v1/projects/1234/rolloutPlans/rp1  
`items[].state` |  `enum` Output only. The current state of the Rollout.  
`items[].etag` |  `string` Output only. etag of the Rollout Ex. abc1234  
`items[].currentWaveNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of the currently running wave. Ex. 1  
`items[].waveDetails[]` |  `object` Output only. Details about each wave of the rollout.  
`items[].waveDetails[].orchestratedWaveDetails` |  `object` Output only. Additional details of the wave for products using the Orchestrated Integration model.  
`items[].waveDetails[].orchestratedWaveDetails.estimatedTotalResourcesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Estimated total count of resources.  
`items[].waveDetails[].orchestratedWaveDetails.completedResourcesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Resource completed so far.  
`items[].waveDetails[].orchestratedWaveDetails.failedResourcesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Resources failed.  
`items[].waveDetails[].orchestratedWaveDetails.failedLocations[]` |  `string` Output only. Locations that failed during orchestration, and ProgressiveRollout stopped retrying. There may be some successful resources rolled out in the wave as the location may have failed later in the Rollout.  
`items[].waveDetails[].orchestratedWaveDetails.locationStatus[]` |  `map (key: string, value: object)` Output only. Status of each location in the wave. Map keys (locations) must be specified like "us-east1" or "asia-west1-a".  
`items[].waveDetails[].orchestratedWaveDetails.locationStatus[].state` |  `enum` Output only. Location state of the wave.  
`items[].waveDetails[].orchestratedWaveDetails.estimatedCompletionTime` |  `string` Output only. Estimated timestamp at which the wave will complete. Extrapolated from current progress.  
`items[].waveDetails[].waveDisplayName` |  `string` Output only. Wave name. Ex. wave1  
`items[].waveDetails[].waveNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. System generated number for the wave.  
`items[].completionTime` |  `string` Output only. The timestamp at which the Rollout was completed.  
`items[].cancellationTime` |  `string` Output only. The timestamp at which the Rollout was cancelled.  
`items[].pauseTime` |  `string` Output only. The timestamp at which the Rollout was paused.  
`items[].resumeTime` |  `string` Output only. The timestamp at which the Rollout was resumed.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`etag` |  `string`  
`unreachables[]` |  `string` Output only. Unreachable resources. end_interface: MixerListResponseWithEtagBuilder  
  
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
