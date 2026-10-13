---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalVmExtensionPolicies/aggregatedList/
title: Method: globalVmExtensionPolicies.aggregatedList \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:09.511132+00:00
---

# Method: globalVmExtensionPolicies.aggregatedList  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalVmExtensionPolicies/aggregatedList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: globalVmExtensionPolicies.aggregatedList Stay organized with collections  Save and categorize content based on your preferences. 

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
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Retrieves the list of all VM Extension Policy resources available to the specified project.

To prevent failure, it's recommended that you set the `returnPartialSuccess` parameter to `true`.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/aggregated/vmExtensionPolicies?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Name of the project scoping this request.  
  
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
`includeAllScopes` |  `boolean` Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included.  
`serviceProjectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api.  
  
### Request body

The request body must be empty.

### Response body

Response for the aggregated list of VM extension policies.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": {
        string: {
          "vmExtensionPolicies": [
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
              "managedByGlobal": boolean,
              "globalResourceLink": string,
              "state": enum
            }
          ],
          "warning": {
            "code": enum,
            "message": string,
            "data": [
              {
                "key": string,
                "value": string
              }
            ]
          }
        },
        ...
      },
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
`kind` |  `string` Output only. Type of resource. Always `compute#VmExtensionPolicyAggregatedList` for lists of VmExtensionPolicies.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items` |  `map (key: string, value: object)` A list of VmExtensionPoliciesScopedList resources.**Key:** Name of the scope containing this set of VmExtensionPolicies.  
`items.vmExtensionPolicies[]` |  `object` globalVmExtensionPolicies.list of VmExtensionPolicy resources contained in this scope.  
`items.vmExtensionPolicies[].kind` |  `string` Output only. Type of the resource. Always `compute#vmExtensionPolicy`.  
`items.vmExtensionPolicies[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items.vmExtensionPolicies[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.vmExtensionPolicies[].updateTimestamp` |  `string` Output only. globalVmExtensionPolicies.update timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.vmExtensionPolicies[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items.vmExtensionPolicies[].description` |  `string` An optional description of this resource.  
`items.vmExtensionPolicies[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`items.vmExtensionPolicies[].selfLinkWithId` |  `string` Output only. Server-defined URL for this resource's resource id.  
`items.vmExtensionPolicies[].extensionPolicies[]` |  `map (key: string, value: object)` Required. A map of extension names (for example, "ops-agent") to their corresponding policy configurations.  
`items.vmExtensionPolicies[].extensionPolicies[].stringConfig` |  `string` Optional. String-based configuration data for the extension.  
`items.vmExtensionPolicies[].extensionPolicies[].pinnedVersion` |  `string` Optional. The specific version of the extension to install. If not set, the latest version is used.  
`items.vmExtensionPolicies[].instanceSelectors[]` |  `object` Optional. Selectors to target VMs for this policy. VMs are selected if they match _any_ of the provided selectors (logical OR). If this list is empty, the policy applies to all VMs.  
`items.vmExtensionPolicies[].instanceSelectors[].labelSelector` |  `object` Optional. LabelSelector selects VMs based on their labels.  
`items.vmExtensionPolicies[].instanceSelectors[].labelSelector.inclusionLabels` |  `map (key: string, value: string)` Optional. A map of key-value pairs representing VM labels. VMs must have all of the labels specified in this map to be selected (logical AND).e.g. If the `inclusionLabels` are {("key1", "value1"), ("key2", "value2")}, the VM labels must contain both ("key1", "value1") and ("key2", "value2") to be selected. If the VM labels are ("key1", "value1") and ("something", "else"), it will not be selected.If the map is empty, it's considered a match.  
`items.vmExtensionPolicies[].priority` |  `integer` Optional. Priority of this policy. Used to resolve conflicts when multiple policies apply to the same extension. The policy priority is an integer from 0 to 65535, inclusive. Lower integers indicate higher priorities. If you do not specify a priority when creating a rule, it is assigned a priority of 1000. If priorities are equal, the policy with the most recent creation timestamp takes precedence.  
`items.vmExtensionPolicies[].managedByGlobal` |  `boolean` Optional. Output only. Indicates if this policy is managed by a global policy.  
`items.vmExtensionPolicies[].globalResourceLink` |  `string` Optional. Output only. Link to the global policy that manages this zone policy, if applicable.  
`items.vmExtensionPolicies[].state` |  `enum` Optional. Output only. Current state of the policy: ACTIVE or DELETING.  
`items.warning` |  `object` Informational warning which replaces the list of backend services when the list is empty.  
`items.warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`items.warning.message` |  `string` Output only. A human-readable description of the warning code.  
`items.warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`items.warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`items.warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
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
