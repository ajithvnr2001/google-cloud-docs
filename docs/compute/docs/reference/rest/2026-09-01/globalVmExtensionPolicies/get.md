---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalVmExtensionPolicies/get/
title: Method: globalVmExtensionPolicies.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:12.457019+00:00
---

# Method: globalVmExtensionPolicies.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalVmExtensionPolicies/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: globalVmExtensionPolicies.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Gets details of a global VM extension policy.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/vmExtensionPolicies/{globalVmExtensionPolicy}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`globalVmExtensionPolicy` |  `string` Name of the GlobalVmExtensionPolicy resource to return.  
  
### Request body

The request body must be empty.

### Response body

Message describing GlobalVmExtensionPolicy object.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "updateTimestamp": string,
      "name": string,
      "description": string,
      "selfLink": string,
      "selfLinkWithId": string,
      "extensionPolicies": {
        string: {
          "stringConfig": string,
          "pinnedVersion": string
        },
        ...
      },
      "instanceSelectors": [
        {
          "labelSelector": {
            "inclusionLabels": {
              string: string,
              ...
            }
          }
        }
      ],
      "priority": integer,
      "scopedResourceStatus": enum,
      "rolloutOperation": {
        "rolloutInput": {
          "retryUuid": string,
          "conflictBehavior": string,
    
          // The following is a list of mutually exclusive fields. At most one of the
          // fields will be set in a response:
          "name": string,
          "predefinedRolloutPlan": enum
          // End of mutually exclusive fields.
        },
        "rolloutStatus": {
          "currentRollouts": [
            {
              "rollout": string,
              "rolloutPlan": string,
              "state": enum,
              "locationRolloutStatus": {
                string: {
                  "state": enum
                },
                ...
              }
            }
          ],
          "previousRollout": {
            "rollout": string,
            "rolloutPlan": string,
            "state": enum,
            "locationRolloutStatus": {
              string: {
                "state": enum
              },
              ...
            }
          }
        }
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#globalVmExtensionPolicy` for globalVmExtensionPolicies.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`updateTimestamp` |  `string` Output only. globalVmExtensionPolicies.update timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`selfLinkWithId` |  `string` Output only. Server-defined URL for this resource's resource id.  
`extensionPolicies[]` |  `map (key: string, value: object)` Required. Map from extension (eg: "cloudops") to its policy configuration. The key is the name of the extension.  
`extensionPolicies[].stringConfig` |  `string` Optional. String configuration. Any string payload that the extension understands.  
`extensionPolicies[].pinnedVersion` |  `string` Optional. The version pinning for the extension. If empty, the extension will be installed with the latest version released by the extension producer.  
`instanceSelectors[]` |  `object` Optional. Selector to target VMs for a policy. There is a logical "AND" between instanceSelectors.  
`instanceSelectors[].labelSelector` |  `object` Optional. Labels within the LabelSelector are OR'd.  
`instanceSelectors[].labelSelector.inclusionLabels` |  `map (key: string, value: string)` Optional. Labels as key value pairs. A VM should contain all the pairs specified in this map to be selected; Labels within the LabelSelector are OR'ed.  
`priority` |  `integer` Optional. Used to resolve conflicts when multiple policies are active for the same extension. Defaults to 0.Larger the number, higher the priority. When the priority is the same, the policy with the newer create time has higher priority.  
`scopedResourceStatus` |  `enum` Output only. The scoped resource status. It's only for tracking the purging status of the policy.  
`rolloutOperation` |  `object` Required. The rollout strategy and status.  
`rolloutOperation.rolloutInput` |  `object` Required. The rollout input which defines the rollout plan.  
`rolloutOperation.rolloutInput.name` |  `string` Optional. The name of the rollout plan. Ex. projects//locations/global/rolloutPlans/.  
`rolloutOperation.rolloutInput.predefinedRolloutPlan` |  `enum` Optional. Specifies the predefined rollout plan for the policy. Valid values are `SLOW_ROLLOUT` and `FAST_ROLLOUT`. The recommended value is `SLOW_ROLLOUT` for progressive rollout. For more information, see [Rollout plans for global policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#rollout-global-policies).  
`rolloutOperation.rolloutInput.retryUuid` |  `string` Optional. The UUID that identifies a policy rollout retry attempt for update and delete operations. Set this field only when retrying a rollout for an existing extension policy.

  * `update` method: Lets you retry policy rollout without changes. An error occurs if you set retryUuid but the policy is modified.
  * `delete` method: Lets you retry policy deletion rollout if the previous deletion rollout is not finished and the policy is in the DELETING state. If you set this field when the policy is not in the DELETING state, an error occurs.

  
`rolloutOperation.rolloutInput.conflictBehavior` |  `string` Optional. Specifies the behavior of the rollout if a conflict is detected in a project during a rollout. This only applies to `insert` and `update` methods.A conflict occurs in the following cases:

  * `insert` method: If the zonal policy already exists when the insert happens.
  * `update` method: If the zonal policy was modified by a zonal API call outside of this rollout.

Possible values are the following:

  * `""` (empty string): If a conflict occurs, the local value is not overwritten. This is the default behavior.
  * `"overwrite"`: If a conflict occurs, the local value is overwritten with the rollout value.

  
`rolloutOperation.rolloutStatus` |  `object` Output only. The rollout status of the policy.  
`rolloutOperation.rolloutStatus.currentRollouts[]` |  `object` Output only. The current rollouts for the latest version of the resource. There should be only one current rollout, but for scalability, we make it repeated.  
`rolloutOperation.rolloutStatus.currentRollouts[].rollout` |  `string` Output only. The name of the rollout. Ex. projects//locations/global/rollouts/.  
`rolloutOperation.rolloutStatus.currentRollouts[].rolloutPlan` |  `string` Output only. The name of the rollout plan. Ex. projects//locations/global/rolloutPlans/.  
`rolloutOperation.rolloutStatus.currentRollouts[].state` |  `enum` Output only. The overall state of the rollout.  
`rolloutOperation.rolloutStatus.currentRollouts[].locationRolloutStatus[]` |  `map (key: string, value: object)` Output only. The rollout status for each location. The list of the locations is the same as the list of locations in the rollout plan.  
`rolloutOperation.rolloutStatus.currentRollouts[].locationRolloutStatus[].state` |  `enum` Output only. The state of the location rollout.  
`rolloutOperation.rolloutStatus.previousRollout` |  `object` Output only. The last completed rollout resource. This field will not be populated until the first rollout is completed.  
`rolloutOperation.rolloutStatus.previousRollout.rollout` |  `string` Output only. The name of the rollout. Ex. projects//locations/global/rollouts/.  
`rolloutOperation.rolloutStatus.previousRollout.rolloutPlan` |  `string` Output only. The name of the rollout plan. Ex. projects//locations/global/rolloutPlans/.  
`rolloutOperation.rolloutStatus.previousRollout.state` |  `enum` Output only. The overall state of the rollout.  
`rolloutOperation.rolloutStatus.previousRollout.locationRolloutStatus[]` |  `map (key: string, value: object)` Output only. The rollout status for each location. The list of the locations is the same as the list of locations in the rollout plan.  
`rolloutOperation.rolloutStatus.previousRollout.locationRolloutStatus[].state` |  `enum` Output only. The state of the location rollout.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.vmExtensionPolicies.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
