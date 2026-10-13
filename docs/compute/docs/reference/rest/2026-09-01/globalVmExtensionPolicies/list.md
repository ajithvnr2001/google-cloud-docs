---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalVmExtensionPolicies/list/
title: Method: globalVmExtensionPolicies.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:14.970458+00:00
---

# Method: globalVmExtensionPolicies.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalVmExtensionPolicies/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: globalVmExtensionPolicies.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
        * JSON representation
        * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Lists global VM extension policies.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/vmExtensionPolicies?$apiVersion=2026-09-01`

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

Response to list global VM extension policy resources.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
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
    
              // The following is a list of mutually exclusive fields. At most one of the
              // fields will be set in a response:
              "labelSelector": {
                "inclusionLabels": {
                  string: string,
                  ...
                }
              }
              // End of mutually exclusive fields.
            }
          ],
          "priority": integer,
          "scopedResourceStatus": enum,
          "rolloutOperation": {
            "rolloutInput": {
              "name": string,
              "predefinedRolloutPlan": enum,
              "retryUuid": string,
              "conflictBehavior": string
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
`kind` |  `string` Output only. Type of resource.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of GlobalVmExtensionPolicy resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#globalVmExtensionPolicy` for globalVmExtensionPolicies.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].updateTimestamp` |  `string` Output only. globalVmExtensionPolicies.update timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`items[].selfLinkWithId` |  `string` Output only. Server-defined URL for this resource's resource id.  
`items[].extensionPolicies[]` |  `map (key: string, value: object)` Required. Map from extension (eg: "cloudops") to its policy configuration. The key is the name of the extension.  
`items[].extensionPolicies[].stringConfig` |  `string` Optional. String configuration. Any string payload that the extension understands.  
`items[].extensionPolicies[].pinnedVersion` |  `string` Optional. The version pinning for the extension. If empty, the extension will be installed with the latest version released by the extension producer.  
`items[].instanceSelectors[]` |  `object` Optional. Selector to target VMs for a policy. There is a logical "AND" between instanceSelectors.  
`items[].instanceSelectors[].labelSelector` |  `object` Optional. Labels within the LabelSelector are OR'd.  
`items[].instanceSelectors[].labelSelector.inclusionLabels` |  `map (key: string, value: string)` Optional. Labels as key value pairs. A VM should contain all the pairs specified in this map to be selected; Labels within the LabelSelector are OR'ed.  
`items[].priority` |  `integer` Optional. Used to resolve conflicts when multiple policies are active for the same extension. Defaults to 0.Larger the number, higher the priority. When the priority is the same, the policy with the newer create time has higher priority.  
`items[].scopedResourceStatus` |  `enum` Output only. The scoped resource status. It's only for tracking the purging status of the policy.  
`items[].rolloutOperation` |  `object` Required. The rollout strategy and status.  
`items[].rolloutOperation.rolloutInput` |  `object` Required. The rollout input which defines the rollout plan.  
`items[].rolloutOperation.rolloutInput.name` |  `string` Optional. The name of the rollout plan. Ex. projects//locations/global/rolloutPlans/.  
`items[].rolloutOperation.rolloutInput.predefinedRolloutPlan` |  `enum` Optional. Specifies the predefined rollout plan for the policy. Valid values are `SLOW_ROLLOUT` and `FAST_ROLLOUT`. The recommended value is `SLOW_ROLLOUT` for progressive rollout. For more information, see [Rollout plans for global policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#rollout-global-policies).  
`items[].rolloutOperation.rolloutInput.retryUuid` |  `string` Optional. The UUID that identifies a policy rollout retry attempt for update and delete operations. Set this field only when retrying a rollout for an existing extension policy.

  * `update` method: Lets you retry policy rollout without changes. An error occurs if you set retryUuid but the policy is modified.
  * `delete` method: Lets you retry policy deletion rollout if the previous deletion rollout is not finished and the policy is in the DELETING state. If you set this field when the policy is not in the DELETING state, an error occurs.

  
`items[].rolloutOperation.rolloutInput.conflictBehavior` |  `string` Optional. Specifies the behavior of the rollout if a conflict is detected in a project during a rollout. This only applies to `insert` and `update` methods.A conflict occurs in the following cases:

  * `insert` method: If the zonal policy already exists when the insert happens.
  * `update` method: If the zonal policy was modified by a zonal API call outside of this rollout.

Possible values are the following:

  * `""` (empty string): If a conflict occurs, the local value is not overwritten. This is the default behavior.
  * `"overwrite"`: If a conflict occurs, the local value is overwritten with the rollout value.

  
`items[].rolloutOperation.rolloutStatus` |  `object` Output only. The rollout status of the policy.  
`items[].rolloutOperation.rolloutStatus.currentRollouts[]` |  `object` Output only. The current rollouts for the latest version of the resource. There should be only one current rollout, but for scalability, we make it repeated.  
`items[].rolloutOperation.rolloutStatus.currentRollouts[].rollout` |  `string` Output only. The name of the rollout. Ex. projects//locations/global/rollouts/.  
`items[].rolloutOperation.rolloutStatus.currentRollouts[].rolloutPlan` |  `string` Output only. The name of the rollout plan. Ex. projects//locations/global/rolloutPlans/.  
`items[].rolloutOperation.rolloutStatus.currentRollouts[].state` |  `enum` Output only. The overall state of the rollout.  
`items[].rolloutOperation.rolloutStatus.currentRollouts[].locationRolloutStatus[]` |  `map (key: string, value: object)` Output only. The rollout status for each location. The list of the locations is the same as the list of locations in the rollout plan.  
`items[].rolloutOperation.rolloutStatus.currentRollouts[].locationRolloutStatus[].state` |  `enum` Output only. The state of the location rollout.  
`items[].rolloutOperation.rolloutStatus.previousRollout` |  `object` Output only. The last completed rollout resource. This field will not be populated until the first rollout is completed.  
`items[].rolloutOperation.rolloutStatus.previousRollout.rollout` |  `string` Output only. The name of the rollout. Ex. projects//locations/global/rollouts/.  
`items[].rolloutOperation.rolloutStatus.previousRollout.rolloutPlan` |  `string` Output only. The name of the rollout plan. Ex. projects//locations/global/rolloutPlans/.  
`items[].rolloutOperation.rolloutStatus.previousRollout.state` |  `enum` Output only. The overall state of the rollout.  
`items[].rolloutOperation.rolloutStatus.previousRollout.locationRolloutStatus[]` |  `map (key: string, value: object)` Output only. The rollout status for each location. The list of the locations is the same as the list of locations in the rollout plan.  
`items[].rolloutOperation.rolloutStatus.previousRollout.locationRolloutStatus[].state` |  `enum` Output only. The state of the location rollout.  
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
`unreachables[]` |  `string` Output only. Unreachable resources.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.vmExtensionPolicies.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
