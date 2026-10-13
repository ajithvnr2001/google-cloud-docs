---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/list/
title: Method: instanceGroupManagerResizeRequests.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:22.155376+00:00
---

# Method: instanceGroupManagerResizeRequests.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: instanceGroupManagerResizeRequests.list Stay organized with collections  Save and categorize content based on your preferences. 

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
            * JSON representation
      * JSON representation
  * Authorization scopes
  * Try it!



Retrieves a list of resize requests that are contained in the managed instance group.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/resizeRequests`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` The name of the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the managed instance group is located. The name should conform to RFC1035.  
`instanceGroupManager` |  `string` The name of the managed instance group. The name should conform to RFC1035. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `instanceGroupManager`:

  * `compute.instanceGroupManagers.get`

  
  
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
  
### Request body

The request body must be empty.

### Response body

Output only. A list of resize requests.

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
          "name": string,
          "description": string,
          "zone": string,
          "region": string,
          "count": integer,
          "resizeBy": integer,
          "instances": [
            {
              "name": string,
              "preservedState": {
                "disks": {
                  string: {
                    "source": string,
                    "mode": enum,
                    "autoDelete": enum
                  },
                  ...
                },
                "metadata": {
                  string: string,
                  ...
                },
                "internalIPs": {
                  string: {
                    "autoDelete": enum,
                    "ipAddress": {
                      "literal": string,
                      "address": string
                    }
                  },
                  ...
                },
                "externalIPs": {
                  string: {
                    "autoDelete": enum,
                    "ipAddress": {
                      "literal": string,
                      "address": string
                    }
                  },
                  ...
                }
              },
              "status": enum,
              "fingerprint": string
            }
          ],
          "requestedRunDuration": {
            "seconds": string,
            "nanos": integer
          },
          "state": enum,
          "status": {
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
            "lastAttempt": {
              "error": {
                "errors": [
                  {
                    "code": string,
                    "location": string,
                    "message": string,
                    "errorDetails": [
                      {
    
                        // The following is a list of mutually exclusive fields. At most one of the
                        // fields will be set in a response:
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
                        // End of mutually exclusive fields.
                      }
                    ]
                  }
                ]
              }
            }
          },
          "selfLink": string,
          "selfLinkWithId": string
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
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#instanceGroupManagerResizeRequestList` for a list of resize requests.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of resize request resources.  
`items[].kind` |  `string` Output only. The resource type, which is always `compute#instanceGroupManagerResizeRequest` for resize requests.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. A unique identifier for this resource type. The server generates this identifier.  
`items[].creationTimestamp` |  `string` Output only. The creation timestamp for this resize request in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` The name of this resize request. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`items[].description` |  `string` An optional description of this resource.  
`items[].zone` |  `string` Output only. The URL of a [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the resize request is located. Populated only for zonal resize requests.  
`items[].region` |  `string` Output only. The URL of a [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the resize request is located. Populated only for regional resize requests.  
`items[].count  
**(deprecated)**` |  `integer` This field is deprecated, please use resizeBy instead. The count of instances to create as part of this resize request.  
`items[].resizeBy` |  `integer` The number of instances to be created by this resize request. The group's target size will be increased by this number. This field cannot be used together with 'instances'.  
`items[].instances[]` |  `object` The names of instances to be created by this resize request. The number of names specified determines the number of instances to create. The group's target size will be increased by this number. This field cannot be used together with 'resizeBy'.  
`items[].instances[].name` |  `string` The name of a per-instance configuration and its corresponding instance. Serves as a merge key during `UpdatePerInstanceConfigs` operations, that is, if a per-instance configuration with the same name exists then it will be updated, otherwise a new one will be created for the VM instance with the same name. An attempt to create a per-instance configuration for a VM instance that either doesn't exist or is not part of the group will result in an error.  
`items[].instances[].preservedState` |  `object` The intended preserved state for the given instance. Does not contain preserved state generated from a stateful policy.  
`items[].instances[].preservedState.disks[]` |  `map (key: string, value: object)` Preserved disks defined for this instance. This map is keyed with the device names of the disks.  
`items[].instances[].preservedState.disks[].source` |  `string` The URL of the disk resource that is stateful and should be attached to the VM instance.  
`items[].instances[].preservedState.disks[].mode` |  `enum` The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.  
`items[].instances[].preservedState.disks[].autoDelete` |  `enum` These stateful disks will never be deleted during autohealing, update, instance recreate operations. This flag is used to configure if the disk should be deleted after it is no longer used by the group, e.g. when the given instance or the whole MIG is deleted. Note: disks attached in `READ_ONLY` mode cannot be auto-deleted.  
`items[].instances[].preservedState.metadata` |  `map (key: string, value: string)` Preserved metadata defined for this instance.  
`items[].instances[].preservedState.internalIPs[]` |  `map (key: string, value: object)` Preserved internal IPs defined for this instance. This map is keyed with the name of the network interface.  
`items[].instances[].preservedState.internalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`items[].instances[].preservedState.internalIPs[].ipAddress` |  `object` Ip address representation  
`items[].instances[].preservedState.internalIPs[].ipAddress.literal` |  `string` An IPv4 internal network address to assign to the instance for this network interface.  
`items[].instances[].preservedState.internalIPs[].ipAddress.address` |  `string` The URL of the reservation for this IP address.  
`items[].instances[].preservedState.externalIPs[]` |  `map (key: string, value: object)` Preserved external IPs defined for this instance. This map is keyed with the name of the network interface.  
`items[].instances[].preservedState.externalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`items[].instances[].preservedState.externalIPs[].ipAddress` |  `object` Ip address representation  
`items[].instances[].preservedState.externalIPs[].ipAddress.literal` |  `string` An IPv4 internal network address to assign to the instance for this network interface.  
`items[].instances[].preservedState.externalIPs[].ipAddress.address` |  `string` The URL of the reservation for this IP address.  
`items[].instances[].status` |  `enum` The status of applying this per-instance configuration on the corresponding managed instance.  
`items[].instances[].fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this per-instance config. This field can be used in optimistic locking. It is ignored when inserting a per-instance config. An up-to-date fingerprint must be provided in order to update an existing per-instance configuration or the field needs to be unset.A base64-encoded string.  
`items[].requestedRunDuration` |  `object` Requested run duration for instances that will be created by this request. At the end of the run duration instance will be deleted.  
`items[].requestedRunDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].requestedRunDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].state` |  `enum` Output only. Current state of the request.  
`items[].status` |  `object` Output only. Status of the request.  
`items[].status.error` |  `object` Output only. Fatal errors encountered during the queueing or provisioning phases of the ResizeRequest that caused the transition to the FAILED state. Contrary to the lastAttempt errors, this field is final and errors are never removed from here, as the ResizeRequest is not going to retry.  
`items[].status.error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`items[].status.error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`items[].status.error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`items[].status.error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`items[].status.error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`items[].status.error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`items[].status.error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`items[].status.error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`items[].status.error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`items[].status.error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`items[].status.error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`items[].status.error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`items[].status.error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`items[].status.error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`items[].status.error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`items[].status.error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`items[].status.error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`items[].status.error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`items[].status.error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`items[].status.error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`items[].status.error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`items[].status.error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`items[].status.error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`items[].status.lastAttempt` |  `object` Output only. Information about the last attempt to fulfill the request. The value is temporary since the ResizeRequest can retry, as long as it's still active and the last attempt value can either be cleared or replaced with a different error. Since ResizeRequest retries infrequently, the value may be stale and no longer show an active problem. The value is cleared when ResizeRequest transitions to the final state (becomes inactive). If the final state is FAILED the error describing it will be stored in the "error" field only.  
`items[].status.lastAttempt.error` |  `object` Output only. Errors that prevented the ResizeRequest to be fulfilled.  
`items[].status.lastAttempt.error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`items[].status.lastAttempt.error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`items[].status.lastAttempt.error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`items[].status.lastAttempt.error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`items[].status.lastAttempt.error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`items[].status.lastAttempt.error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`items[].status.lastAttempt.error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`items[].status.lastAttempt.error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`items[].status.lastAttempt.error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`items[].status.lastAttempt.error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`items[].status.lastAttempt.error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`items[].status.lastAttempt.error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`items[].status.lastAttempt.error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`items[].status.lastAttempt.error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`items[].status.lastAttempt.error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`items[].status.lastAttempt.error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`items[].status.lastAttempt.error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`items[].status.lastAttempt.error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`items[].status.lastAttempt.error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`items[].status.lastAttempt.error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`items[].status.lastAttempt.error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`items[].status.lastAttempt.error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`items[].status.lastAttempt.error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`items[].selfLink` |  `string` Output only. The URL for this resize request. The server defines this URL.  
`items[].selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
