---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/nodeGroups/aggregatedList/
title: Method: nodeGroups.aggregatedList \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:50.691746+00:00
---

# Method: nodeGroups.aggregatedList  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/nodeGroups/aggregatedList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: nodeGroups.aggregatedList Stay organized with collections  Save and categorize content based on your preferences. 

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



Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/projects/{project}/aggregated/nodeGroups`

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
`returnPartialSuccess` |  `boolean` Opt-in for partial success behavior which provides partial results in case of failure. The default value is false.For example, when partial success behavior is enabled, aggregatedList for a single zone scope either returns all resources in the zone or no resources, with an error code.  
`includeAllScopes` |  `boolean` Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included.  
`serviceProjectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": {
        string: {
          "nodeGroups": [
            {
              "kind": string,
              "id": string,
              "creationTimestamp": string,
              "name": string,
              "description": string,
              "nodeTemplate": string,
              "zone": string,
              "selfLink": string,
              "status": enum,
              "size": integer,
              "autoscalingPolicy": {
                "mode": enum,
                "minNodes": integer,
                "maxNodes": integer
              },
              "maintenancePolicy": enum,
              "locationHint": string,
              "fingerprint": string,
              "maintenanceWindow": {
                "startTime": string,
                "maintenanceDuration": {
                  "seconds": string,
                  "nanos": integer
                }
              },
              "shareSettings": {
                "shareType": enum,
                "projects": [
                  string
                ],
                "projectMap": {
                  string: {
                    "projectId": string
                  },
                  ...
                },
                "folderMap": {
                  string: {
                    "folderId": string
                  },
                  ...
                }
              },
              "maintenanceInterval": enum
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
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource.Always `compute#nodeGroupAggregatedList` for aggregated lists of node groups.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items` |  `map (key: string, value: object)` A list of NodeGroupsScopedList resources.**Key:** Output only. Name of the scope containing this set of node groups.  
`items.nodeGroups[]` |  `object` Output only. A list of node groups contained in this scope.  
`items.nodeGroups[].kind` |  `string` Output only. The type of the resource. Always `compute#nodeGroup` for node group.  
`items.nodeGroups[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items.nodeGroups[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.nodeGroups[].name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items.nodeGroups[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items.nodeGroups[].nodeTemplate` |  `string` URL of the node template to create the node group from.  
`items.nodeGroups[].zone` |  `string` Output only. The name of the zone where the node group resides, such as us-central1-a.  
`items.nodeGroups[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items.nodeGroups[].status` |  `enum`  
`items.nodeGroups[].size` |  `integer` Output only. The total number of nodes in the node group.  
`items.nodeGroups[].autoscalingPolicy` |  `object` Specifies how autoscaling should behave.  
`items.nodeGroups[].autoscalingPolicy.mode` |  `enum` The autoscaling mode. Set to one of: `ON`, `OFF`, or `ONLY_SCALE_OUT`. For more information, see [ Autoscaler modes](https://cloud.google.com/compute/docs/nodes/autoscaling-node-groups#modes).  
`items.nodeGroups[].autoscalingPolicy.minNodes` |  `integer` The minimum number of nodes that the group should have.  
`items.nodeGroups[].autoscalingPolicy.maxNodes` |  `integer` The maximum number of nodes that the group should have. Must be set if autoscaling is enabled. Maximum value allowed is 100.  
`items.nodeGroups[].maintenancePolicy` |  `enum` Specifies how to handle instances when a node in the group undergoes maintenance. Set to one of: `DEFAULT`, `RESTART_IN_PLACE`, or `MIGRATE_WITHIN_NODE_GROUP`. The default value is `DEFAULT`. For more information, see [ Maintenance policies](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes#maintenance_policies).  
`items.nodeGroups[].locationHint` |  `string` An opaque location hint used to place the Node close to other resources. This field is for use by internal tools that use the public API. The location hint here on the NodeGroup overrides any locationHint present in the NodeTemplate.  
`items.nodeGroups[].fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A base64-encoded string.  
`items.nodeGroups[].maintenanceWindow` |  `object`  
`items.nodeGroups[].maintenanceWindow.startTime` |  `string` Start time of the window. This must be in UTC format that resolves to one of `00:00`, `04:00`, `08:00`, `12:00`, `16:00`, or `20:00`. For example, both `13:00-5` and `08:00` are valid.  
`items.nodeGroups[].maintenanceWindow.maintenanceDuration` |  `object` Output only. A predetermined duration for the window, automatically chosen to be the smallest possible in the given scenario.  
`items.nodeGroups[].maintenanceWindow.maintenanceDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items.nodeGroups[].maintenanceWindow.maintenanceDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items.nodeGroups[].shareSettings` |  `object` Share-settings for the node group  
`items.nodeGroups[].shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`items.nodeGroups[].shareSettings.projects[]` |  `string` A nodeGroups.list of Project names to specify consumer projects for this shared-reservation. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`items.nodeGroups[].shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`items.nodeGroups[].shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`items.nodeGroups[].shareSettings.folderMap[]` |  `map (key: string, value: object)` A map of folder id and folder config to specify consumer projects for this shared-reservation. This is only valid when shareType's value is DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS. Folder id should be a string of number, and without "folders/" prefix.  
`items.nodeGroups[].shareSettings.folderMap[].folderId` |  `string` The folder ID, should be same as the key of this folder config in the parent map. Folder id should be a string of number, and without "folders/" prefix.  
`items.nodeGroups[].maintenanceInterval` |  `enum` Specifies the frequency of planned maintenance events. The accepted values are: `AS_NEEDED` and `RECURRENT`.  
`items.warning` |  `object` Output only. An informational warning that appears when the nodeGroup list is empty.  
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
`unreachables[]` |  `string` Output only. Unreachable resources.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.nodeGroups.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
