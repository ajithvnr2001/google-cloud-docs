---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionInstanceGroupManagerResizeRequests/get/
title: Method: regionInstanceGroupManagerResizeRequests.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:58.648646+00:00
---

# Method: regionInstanceGroupManagerResizeRequests.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionInstanceGroupManagerResizeRequests/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: regionInstanceGroupManagerResizeRequests.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
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
  * Try it!



API Version : 2026-09-01

Returns all of the details about the specified resize request.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/resizeRequests/{resizeRequest}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` The name of the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) scoping this request. Name should conform to RFC1035.  
`instanceGroupManager` |  `string` The name of the managed instance group. Name should conform to RFC1035 or be a resource ID. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `instanceGroupManager`:

  * `compute.instanceGroupManagers.get`

  
`resizeRequest` |  `string` The name of the resize request. Name should conform to RFC1035 or be a resource ID.  
  
### Request body

The request body must be empty.

### Response body

InstanceGroupManagerResizeRequest represents a request to create a number of VMs: either immediately or by queuing the request for the specified time. This resize request is nested under InstanceGroupManager and the VMs created by this request are added to the owning InstanceGroupManager.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "zone": string,
      "region": string,
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
          }
        }
      },
      "selfLink": string,
      "selfLinkWithId": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. The resource type, which is always `compute#instanceGroupManagerResizeRequest` for resize requests.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. A unique identifier for this resource type. The server generates this identifier.  
`creationTimestamp` |  `string` Output only. The creation timestamp for this resize request in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` The name of this resize request. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`description` |  `string` An optional description of this resource.  
`zone` |  `string` Output only. The URL of a [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the resize request is located. Populated only for zonal resize requests.  
`region` |  `string` Output only. The URL of a [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the resize request is located. Populated only for regional resize requests.  
`resizeBy` |  `integer` The number of instances to be created by this resize request. The group's target size will be increased by this number. This field cannot be used together with 'instances'.  
`instances[]` |  `object` The names of instances to be created by this resize request. The number of names specified determines the number of instances to create. The group's target size will be increased by this number. This field cannot be used together with 'resizeBy'.  
`instances[].name` |  `string` The name of a per-instance configuration and its corresponding instance. Serves as a merge key during `UpdatePerInstanceConfigs` operations, that is, if a per-instance configuration with the same name exists then it will be updated, otherwise a new one will be created for the VM instance with the same name. An attempt to create a per-instance configuration for a VM instance that either doesn't exist or is not part of the group will result in an error.  
`instances[].preservedState` |  `object` The intended preserved state for the given instance. Does not contain preserved state generated from a stateful policy.  
`instances[].preservedState.disks[]` |  `map (key: string, value: object)` Preserved disks defined for this instance. This map is keyed with the device names of the disks.  
`instances[].preservedState.disks[].source` |  `string` The URL of the disk resource that is stateful and should be attached to the VM instance.  
`instances[].preservedState.disks[].mode` |  `enum` The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.  
`instances[].preservedState.disks[].autoDelete` |  `enum` These stateful disks will never be deleted during autohealing, update, instance recreate operations. This flag is used to configure if the disk should be deleted after it is no longer used by the group, e.g. when the given instance or the whole MIG is deleted. Note: disks attached in `READ_ONLY` mode cannot be auto-deleted.  
`instances[].preservedState.metadata` |  `map (key: string, value: string)` Preserved metadata defined for this instance.  
`instances[].preservedState.internalIPs[]` |  `map (key: string, value: object)` Preserved internal IPs defined for this instance. This map is keyed with the name of the network interface.  
`instances[].preservedState.internalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`instances[].preservedState.internalIPs[].ipAddress` |  `object` Ip address representation  
`instances[].preservedState.internalIPs[].ipAddress.literal` |  `string` An IPv4 internal network address to assign to the instance for this network interface.  
`instances[].preservedState.internalIPs[].ipAddress.address` |  `string` The URL of the reservation for this IP address.  
`instances[].preservedState.externalIPs[]` |  `map (key: string, value: object)` Preserved external IPs defined for this instance. This map is keyed with the name of the network interface.  
`instances[].preservedState.externalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`instances[].preservedState.externalIPs[].ipAddress` |  `object` Ip address representation  
`instances[].preservedState.externalIPs[].ipAddress.literal` |  `string` An IPv4 internal network address to assign to the instance for this network interface.  
`instances[].preservedState.externalIPs[].ipAddress.address` |  `string` The URL of the reservation for this IP address.  
`instances[].status` |  `enum` The status of applying this per-instance configuration on the corresponding managed instance.  
`instances[].fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this per-instance config. This field can be used in optimistic locking. It is ignored when inserting a per-instance config. An up-to-date fingerprint must be provided in order to update an existing per-instance configuration or the field needs to be unset.A base64-encoded string.  
`requestedRunDuration` |  `object` Requested run duration for instances that will be created by this request. At the end of the run duration instance will be deleted.  
`requestedRunDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`requestedRunDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`state` |  `enum` Output only. Current state of the request.  
`status` |  `object` Output only. Status of the request.  
`status.error` |  `object` Output only. Fatal errors encountered during the queueing or provisioning phases of the ResizeRequest that caused the transition to the FAILED state. Contrary to the lastAttempt errors, this field is final and errors are never removed from here, as the ResizeRequest is not going to retry.  
`status.error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`status.error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`status.error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`status.error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`status.error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`status.error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`status.error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`status.error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`status.error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`status.error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`status.error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`status.error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`status.error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`status.error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`status.error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`status.error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`status.error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`status.error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`status.error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`status.error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`status.error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`status.error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`status.error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`status.lastAttempt` |  `object` Output only. Information about the last attempt to fulfill the request. The value is temporary since the ResizeRequest can retry, as long as it's still active and the last attempt value can either be cleared or replaced with a different error. Since ResizeRequest retries infrequently, the value may be stale and no longer show an active problem. The value is cleared when ResizeRequest transitions to the final state (becomes inactive). If the final state is FAILED the error describing it will be stored in the "error" field only.  
`status.lastAttempt.error` |  `object` Output only. Errors that prevented the ResizeRequest to be fulfilled.  
`status.lastAttempt.error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`status.lastAttempt.error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`status.lastAttempt.error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`status.lastAttempt.error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`status.lastAttempt.error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`status.lastAttempt.error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`status.lastAttempt.error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`status.lastAttempt.error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`status.lastAttempt.error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`status.lastAttempt.error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`status.lastAttempt.error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`status.lastAttempt.error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`status.lastAttempt.error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`status.lastAttempt.error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`status.lastAttempt.error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`status.lastAttempt.error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`status.lastAttempt.error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`status.lastAttempt.error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`status.lastAttempt.error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`status.lastAttempt.error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`status.lastAttempt.error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`status.lastAttempt.error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`status.lastAttempt.error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`selfLink` |  `string` Output only. The URL for this resize request. The server defines this URL.  
`selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
  
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
