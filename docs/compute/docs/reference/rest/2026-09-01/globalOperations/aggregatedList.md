---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalOperations/aggregatedList/
title: Method: globalOperations.aggregatedList \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:04:50.377843+00:00
---

# Method: globalOperations.aggregatedList  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalOperations/aggregatedList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: globalOperations.aggregatedList Stay organized with collections  Save and categorize content based on your preferences. 

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
          * JSON representation
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

Retrieves an aggregated list of all operations.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/aggregated/operations?$apiVersion=2026-09-01`

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
          "operations": [
            {
              "kind": string,
              "id": string,
              "creationTimestamp": string,
              "name": string,
              "zone": string,
              "clientOperationId": string,
              "operationType": string,
              "targetLink": string,
              "targetId": string,
              "status": enum,
              "statusMessage": string,
              "user": string,
              "progress": integer,
              "insertTime": string,
              "startTime": string,
              "endTime": string,
              "error": {
                "errors": [
                  {
                    "code": string,
                    "location": string,
                    "message": string,
                    "errorDetails": [
                      {
                        "errorInfo": {
                          "reason": string,
                          "domain": string,
                          "metadatas": {
                            string: string,
                            ...
                          }
                        },
                        "quotaInfo": {
                          "metricName": string,
                          "limitName": string,
                          "dimensions": {
                            string: string,
                            ...
                          },
                          "limit": number,
                          "futureLimit": number,
                          "rolloutStatus": enum
                        },
                        "help": {
                          "links": [
                            {
                              "description": string,
                              "url": string
                            }
                          ]
                        },
                        "localizedMessage": {
                          "locale": string,
                          "message": string
                        }
                      }
                    ]
                  }
                ]
              },
              "warnings": [
                {
                  "code": enum,
                  "message": string,
                  "data": [
                    {
                      "key": string,
                      "value": string
                    }
                  ]
                }
              ],
              "httpErrorStatusCode": integer,
              "httpErrorMessage": string,
              "selfLink": string,
              "region": string,
              "description": string,
              "operationGroupId": string,
    
              // The following is a list of mutually exclusive fields. At most one of the
              // fields will be set in a response:
              "setCommonInstanceMetadataOperationMetadata": {
                "clientOperationId": string,
                "perLocationOperations": {
                  string: {
                    "state": enum,
                    "error": {
                      "code": integer,
                      "message": string,
                      "details": [
                        {
                          "@type": string,
                          field1: ...,
                          ...
                        }
                      ]
                    }
                  },
                  ...
                }
              },
              "instancesBulkInsertOperationMetadata": {
                "perLocationStatus": {
                  string: {
                    "status": enum,
                    "targetVmCount": integer,
                    "createdVmCount": integer,
                    "failedToCreateVmCount": integer,
                    "deletedVmCount": integer
                  },
                  ...
                }
              },
              "getVersionOperationMetadata": {
                "inlineSbomInfo": {
                  "currentComponentVersions": {
                    string: string,
                    ...
                  },
                  "targetComponentVersions": {
                    string: string,
                    ...
                  }
                }
              },
              "getHealthOperationMetadata": {
                "healthInfo": {
                  "healthStatus": enum,
                  "unhealthyReason": enum,
                  "repairCategory": enum,
                  "availabilitySloStatus": enum,
                  "updateTime": string
                }
              }
              // End of mutually exclusive fields.
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
`kind` |  `string` Output only. Type of resource. Always `compute#operationAggregatedList` for aggregated lists of operations.  
`id` |  `string` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items` |  `map (key: string, value: object)` Output only. A map of scoped operation lists.**Key:** Output only. Name of the scope containing this set of operations.  
`items.operations[]` |  `object` Output only. A list of operations contained in this scope.  
`items.operations[].setCommonInstanceMetadataOperationMetadata` |  `object` Output only. If the operation is for projects.setCommonInstanceMetadata, this field will contain information on all underlying zonal actions and their state.  
`items.operations[].setCommonInstanceMetadataOperationMetadata.clientOperationId` |  `string` Output only. The client operation id.  
`items.operations[].setCommonInstanceMetadataOperationMetadata.perLocationOperations[]` |  `map (key: string, value: object)` Output only. Status information per location (location name is key). Example key: zones/us-central1-a  
`items.operations[].setCommonInstanceMetadataOperationMetadata.perLocationOperations[].state` |  `enum` Output only. Status of the action, which can be one of the following: `PROPAGATING`, `PROPAGATED`, `ABANDONED`, `FAILED`, or `DONE`.  
`items.operations[].setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error` |  `object` Output only. If state is `ABANDONED` or `FAILED`, this field is populated.  
`items.operations[].setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`items.operations[].setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`items.operations[].setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`items.operations[].instancesBulkInsertOperationMetadata` |  `object`  
`items.operations[].instancesBulkInsertOperationMetadata.perLocationStatus[]` |  `map (key: string, value: object)` Status information per location (location name is key). Example key: zones/us-central1-a  
`items.operations[].instancesBulkInsertOperationMetadata.perLocationStatus[].status` |  `enum` Output only. Creation status of BulkInsert operation - information if the flow is rolling forward or rolling back.  
`items.operations[].instancesBulkInsertOperationMetadata.perLocationStatus[].targetVmCount` |  `integer` Output only. Count of VMs originally planned to be created.  
`items.operations[].instancesBulkInsertOperationMetadata.perLocationStatus[].createdVmCount` |  `integer` Output only. Count of VMs successfully created so far.  
`items.operations[].instancesBulkInsertOperationMetadata.perLocationStatus[].failedToCreateVmCount` |  `integer` Output only. Count of VMs that started creating but encountered an error.  
`items.operations[].instancesBulkInsertOperationMetadata.perLocationStatus[].deletedVmCount` |  `integer` Output only. Count of VMs that got deleted during rollback.  
`items.operations[].getVersionOperationMetadata` |  `object`  
`items.operations[].getVersionOperationMetadata.inlineSbomInfo` |  `object`  
`items.operations[].getVersionOperationMetadata.inlineSbomInfo.currentComponentVersions` |  `map (key: string, value: string)` A mapping of components to their currently-applied versions or other appropriate identifiers.  
`items.operations[].getVersionOperationMetadata.inlineSbomInfo.targetComponentVersions` |  `map (key: string, value: string)` A mapping of components to their target versions or other appropriate identifiers.  
`items.operations[].getHealthOperationMetadata` |  `object` Output only. Metadata for GetHealth operations.  
`items.operations[].getHealthOperationMetadata.healthInfo` |  `object` Output only. The health information.  
`items.operations[].getHealthOperationMetadata.healthInfo.healthStatus` |  `enum` Output only. The health status.  
`items.operations[].getHealthOperationMetadata.healthInfo.unhealthyReason` |  `enum` Output only. The reason for unhealthy status.  
`items.operations[].getHealthOperationMetadata.healthInfo.repairCategory` |  `enum` Output only. The repair category.  
`items.operations[].getHealthOperationMetadata.healthInfo.availabilitySloStatus` |  `enum` Output only. The availability SLO status.  
`items.operations[].getHealthOperationMetadata.healthInfo.updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when health info was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`items.operations[].kind` |  `string` Output only. Type of the resource. Always `compute#operation` for Operation resources.  
`items.operations[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the operation. This identifier is defined by the server.  
`items.operations[].creationTimestamp` |  `string` [Deprecated] This field is deprecated.  
`items.operations[].name` |  `string` Output only. Name of the operation.  
`items.operations[].zone` |  `string` Output only. The URL of the zone where the operation resides. Only applicable when performing per-zone operations.  
`items.operations[].clientOperationId` |  `string` Output only. The value of `requestId` if you provided it in the request. Not present otherwise.  
`items.operations[].operationType` |  `string` Output only. The type of operation, such as `insert`, `update`, or `delete`, and so on.  
`items.operations[].targetLink` |  `string` Output only. The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the disk that the snapshot was created from.  
`items.operations[].targetId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique target ID, which identifies a specific incarnation of the target resource.  
`items.operations[].status` |  `enum` Output only. The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`.  
`items.operations[].statusMessage` |  `string` Output only. An optional textual description of the current status of the operation.  
`items.operations[].user` |  `string` Output only. User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`.  
`items.operations[].progress` |  `integer` Output only. An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses.  
`items.operations[].insertTime` |  `string` Output only. The time that this operation was requested. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.operations[].startTime` |  `string` Output only. The time that this operation was started by the server. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.operations[].endTime` |  `string` Output only. The time that this operation was completed. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.operations[].error` |  `object` Output only. If errors are generated during processing of the operation, this field will be populated.  
`items.operations[].error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`items.operations[].error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`items.operations[].error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`items.operations[].error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`items.operations[].error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`items.operations[].error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`items.operations[].error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`items.operations[].error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`items.operations[].error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`items.operations[].error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`items.operations[].error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`items.operations[].error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`items.operations[].error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`items.operations[].error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`items.operations[].error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`items.operations[].error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`items.operations[].error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`items.operations[].error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`items.operations[].error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`items.operations[].error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`items.operations[].error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`items.operations[].error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`items.operations[].error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`items.operations[].warnings[]` |  `object` Output only. If warning messages are generated during processing of the operation, this field will be populated.  
`items.operations[].warnings[].code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`items.operations[].warnings[].message` |  `string` Output only. A human-readable description of the warning code.  
`items.operations[].warnings[].data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`items.operations[].warnings[].data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`items.operations[].warnings[].data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`items.operations[].httpErrorStatusCode` |  `integer` Output only. If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found.  
`items.operations[].httpErrorMessage` |  `string` Output only. If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`.  
`items.operations[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items.operations[].region` |  `string` Output only. The URL of the region where the operation resides. Only applicable when performing regional operations.  
`items.operations[].description` |  `string` Output only. A textual description of the operation, which is set when the operation is created.  
`items.operations[].operationGroupId` |  `string` Output only. An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request.  
`items.warning` |  `object` Output only. Informational warning which replaces the list of operations when the list is empty.  
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

  * `compute.globalOperations.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
