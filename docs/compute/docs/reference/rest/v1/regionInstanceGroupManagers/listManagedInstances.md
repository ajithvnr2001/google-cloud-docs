---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances/
title: Method: regionInstanceGroupManagers.listManagedInstances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:58.301823+00:00
---

# Method: regionInstanceGroupManagers.listManagedInstances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: regionInstanceGroupManagers.listManagedInstances Stay organized with collections  Save and categorize content based on your preferences. 

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
          * JSON representation
          * JSON representation
      * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
  * Authorization scopes
  * Try it!



Lists the instances in the managed instance group and instances that are scheduled to be created. The list includes any current actions that the group has scheduled for its instances. The `orderBy` query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/listManagedInstances`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region scoping this request.  
`instanceGroupManager` |  `string` The name of the managed instance group. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `instanceGroupManager`:

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

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "managedInstances": [
        {
          "name": string,
          "instance": string,
          "id": string,
          "instanceStatus": enum,
          "targetStatus": enum,
          "version": {
            "name": string,
            "instanceTemplate": string
          },
          "preservedStateFromPolicy": {
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
          "preservedStateFromConfig": {
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
          "currentAction": enum,
          "instanceHealth": [
            {
              "healthCheck": string,
              "detailedHealthState": enum
            }
          ],
          "scheduling": {
            "terminationTimestamp": string,
            "gracefulShutdownTimestamp": string
          },
          "shutdownDetails": {
            "requestTimestamp": string,
            "maxDuration": {
              "seconds": string,
              "nanos": integer
            }
          },
          "lastAttempt": {
            "errors": {
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
          },
          "propertiesFromFlexibilityPolicy": {
            "machineType": string,
            "minCpuPlatform": string,
            "disks": [
              {
                "kind": string,
                "type": enum,
                "mode": enum,
                "savedState": enum,
                "source": string,
                "deviceName": string,
                "index": integer,
                "boot": boolean,
                "initializeParams": {
                  "diskName": string,
                  "sourceImage": string,
                  "diskSizeGb": string,
                  "diskType": string,
                  "sourceImageEncryptionKey": {
                    "rawKey": string,
                    "rsaEncryptedKey": string,
                    "kmsKeyName": string,
                    "sha256": string,
                    "kmsKeyServiceAccount": string
                  },
                  "labels": {
                    string: string,
                    ...
                  },
                  "sourceSnapshot": string,
                  "sourceSnapshotEncryptionKey": {
                    "rawKey": string,
                    "rsaEncryptedKey": string,
                    "kmsKeyName": string,
                    "sha256": string,
                    "kmsKeyServiceAccount": string
                  },
                  "description": string,
                  "replicaZones": [
                    string
                  ],
                  "resourcePolicies": [
                    string
                  ],
                  "onUpdateAction": enum,
                  "provisionedIops": string,
                  "licenses": [
                    string
                  ],
                  "architecture": enum,
                  "resourceManagerTags": {
                    string: string,
                    ...
                  },
                  "provisionedThroughput": string,
                  "enableConfidentialCompute": boolean,
                  "storagePool": string
                },
                "autoDelete": boolean,
                "licenses": [
                  string
                ],
                "interface": enum,
                "guestOsFeatures": [
                  {
                    "type": enum
                  }
                ],
                "diskEncryptionKey": {
                  "sha256": string,
                  "kmsKeyServiceAccount": string,
    
                  // The following is a list of mutually exclusive fields. At most one of the
                  // fields will be set in a response:
                  "rawKey": string,
                  "rsaEncryptedKey": string,
                  "kmsKeyName": string
                  // End of mutually exclusive fields.
                },
                "diskSizeGb": string,
                "shieldedInstanceInitialState": {
                  "pk": {
                    "content": string,
                    "fileType": enum
                  },
                  "keks": [
                    {
                      "content": string,
                      "fileType": enum
                    }
                  ],
                  "dbs": [
                    {
                      "content": string,
                      "fileType": enum
                    }
                  ],
                  "dbxs": [
                    {
                      "content": string,
                      "fileType": enum
                    }
                  ]
                },
                "forceAttach": boolean,
                "architecture": enum
              }
            ]
          }
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`managedInstances[]` |  `object` A list of managed instances.  
`managedInstances[].name` |  `string` Output only. The name of the instance. The name always exists even if the instance has not yet been created.  
`managedInstances[].instance` |  `string` Output only. The URL of the instance. The URL can exist even if the instance has not yet been created.  
`managedInstances[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for this resource. This field is empty when instance does not exist.  
`managedInstances[].instanceStatus` |  `enum` Output only. The status of the instance. This field is empty when the instance does not exist.  
`managedInstances[].targetStatus` |  `enum` Output only. The eventual status of the instance. The instance group manager will not be identified as stable till each managed instance reaches its `targetStatus`.  
`managedInstances[].version` |  `object` Output only. Intended version of this instance.  
`managedInstances[].version.name` |  `string` Output only. Name of the version.  
`managedInstances[].version.instanceTemplate` |  `string` Output only. The intended template of the instance. This field is empty when currentAction is one of { DELETING, ABANDONING }.  
`managedInstances[].preservedStateFromPolicy` |  `object` Output only. Preserved state generated based on stateful policy for this instance.  
`managedInstances[].preservedStateFromPolicy.disks[]` |  `map (key: string, value: object)` Preserved disks defined for this instance. This map is keyed with the device names of the disks.  
`managedInstances[].preservedStateFromPolicy.disks[].source` |  `string` The URL of the disk resource that is stateful and should be attached to the VM instance.  
`managedInstances[].preservedStateFromPolicy.disks[].mode` |  `enum` The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.  
`managedInstances[].preservedStateFromPolicy.disks[].autoDelete` |  `enum` These stateful disks will never be deleted during autohealing, update, instance recreate operations. This flag is used to configure if the disk should be deleted after it is no longer used by the group, e.g. when the given instance or the whole MIG is deleted. Note: disks attached in `READ_ONLY` mode cannot be auto-deleted.  
`managedInstances[].preservedStateFromPolicy.metadata` |  `map (key: string, value: string)` Preserved metadata defined for this instance.  
`managedInstances[].preservedStateFromPolicy.internalIPs[]` |  `map (key: string, value: object)` Preserved internal IPs defined for this instance. This map is keyed with the name of the network interface.  
`managedInstances[].preservedStateFromPolicy.internalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`managedInstances[].preservedStateFromPolicy.internalIPs[].ipAddress` |  `object` Ip address representation  
`managedInstances[].preservedStateFromPolicy.internalIPs[].ipAddress.literal` |  `string` An IPv4 internal network address to assign to the instance for this network interface.  
`managedInstances[].preservedStateFromPolicy.internalIPs[].ipAddress.address` |  `string` The URL of the reservation for this IP address.  
`managedInstances[].preservedStateFromPolicy.externalIPs[]` |  `map (key: string, value: object)` Preserved external IPs defined for this instance. This map is keyed with the name of the network interface.  
`managedInstances[].preservedStateFromPolicy.externalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`managedInstances[].preservedStateFromPolicy.externalIPs[].ipAddress` |  `object` Ip address representation  
`managedInstances[].preservedStateFromPolicy.externalIPs[].ipAddress.literal` |  `string` An IPv4 internal network address to assign to the instance for this network interface.  
`managedInstances[].preservedStateFromPolicy.externalIPs[].ipAddress.address` |  `string` The URL of the reservation for this IP address.  
`managedInstances[].preservedStateFromConfig` |  `object` Output only. Preserved state applied from per-instance config for this instance.  
`managedInstances[].preservedStateFromConfig.disks[]` |  `map (key: string, value: object)` Preserved disks defined for this instance. This map is keyed with the device names of the disks.  
`managedInstances[].preservedStateFromConfig.disks[].source` |  `string` The URL of the disk resource that is stateful and should be attached to the VM instance.  
`managedInstances[].preservedStateFromConfig.disks[].mode` |  `enum` The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.  
`managedInstances[].preservedStateFromConfig.disks[].autoDelete` |  `enum` These stateful disks will never be deleted during autohealing, update, instance recreate operations. This flag is used to configure if the disk should be deleted after it is no longer used by the group, e.g. when the given instance or the whole MIG is deleted. Note: disks attached in `READ_ONLY` mode cannot be auto-deleted.  
`managedInstances[].preservedStateFromConfig.metadata` |  `map (key: string, value: string)` Preserved metadata defined for this instance.  
`managedInstances[].preservedStateFromConfig.internalIPs[]` |  `map (key: string, value: object)` Preserved internal IPs defined for this instance. This map is keyed with the name of the network interface.  
`managedInstances[].preservedStateFromConfig.internalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`managedInstances[].preservedStateFromConfig.internalIPs[].ipAddress` |  `object` Ip address representation  
`managedInstances[].preservedStateFromConfig.internalIPs[].ipAddress.literal` |  `string` An IPv4 internal network address to assign to the instance for this network interface.  
`managedInstances[].preservedStateFromConfig.internalIPs[].ipAddress.address` |  `string` The URL of the reservation for this IP address.  
`managedInstances[].preservedStateFromConfig.externalIPs[]` |  `map (key: string, value: object)` Preserved external IPs defined for this instance. This map is keyed with the name of the network interface.  
`managedInstances[].preservedStateFromConfig.externalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`managedInstances[].preservedStateFromConfig.externalIPs[].ipAddress` |  `object` Ip address representation  
`managedInstances[].preservedStateFromConfig.externalIPs[].ipAddress.literal` |  `string` An IPv4 internal network address to assign to the instance for this network interface.  
`managedInstances[].preservedStateFromConfig.externalIPs[].ipAddress.address` |  `string` The URL of the reservation for this IP address.  
`managedInstances[].currentAction` |  `enum` Output only. The current action that the managed instance group has scheduled for the instance. Possible values: 

  * `NONE` The instance is running, and the managed instance group does not have any scheduled actions for this instance.
  * `CREATING` The managed instance group is creating this instance. If the group fails to create this instance, it will try again until it is successful.
  * `CREATING_WITHOUT_RETRIES` The managed instance group is attempting to create this instance only once. If the group fails to create this instance, it does not try again and the group's `targetSize` value is decreased instead.
  * `RECREATING` The managed instance group is recreating this instance.
  * `DELETING` The managed instance group is permanently deleting this instance.
  * `ABANDONING` The managed instance group is abandoning this instance. The instance will be removed from the instance group and from any target pools that are associated with this group.
  * `RESTARTING` The managed instance group is restarting the instance.
  * `REFRESHING` The managed instance group is applying configuration changes to the instance without stopping it. For example, the group can update the target pool list for an instance without stopping that instance.
  * `VERIFYING` The managed instance group has created the instance and it is in the process of being verified.

  
`managedInstances[].instanceHealth[]` |  `object` Output only. Health state of the instance per health-check.  
`managedInstances[].instanceHealth[].healthCheck` |  `string` Output only. The URL for the health check that verifies whether the instance is healthy.  
`managedInstances[].instanceHealth[].detailedHealthState` |  `enum` Output only. The current detailed instance health state.  
`managedInstances[].scheduling` |  `object` Output only. Information about the termination timestamp of the instance, if applicable.  
`managedInstances[].scheduling.terminationTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the managed instance will be terminated. This is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`managedInstances[].scheduling.gracefulShutdownTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the underlying instance will be triggered for graceful shutdown if it is configured. This is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`managedInstances[].shutdownDetails` |  `object` Output only. Specifies the graceful shutdown details if the instance is in `PENDING_STOP` state or there is a programmed stop scheduled.  
`managedInstances[].shutdownDetails.requestTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Past timestamp indicating the beginning of `PENDING_STOP` state of instance in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`managedInstances[].shutdownDetails.maxDuration` |  `object` Output only. The duration for graceful shutdown. Only applicable when the instance is in `PENDING_STOP` state.  
`managedInstances[].shutdownDetails.maxDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`managedInstances[].shutdownDetails.maxDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`managedInstances[].lastAttempt` |  `object` Output only. Information about the last attempt to create or delete the instance.  
`managedInstances[].lastAttempt.errors` |  `object` Output only. Encountered errors during the last attempt to create or delete the instance.  
`managedInstances[].lastAttempt.errors.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`managedInstances[].lastAttempt.errors.errors[].code` |  `string` Output only. The error type identifier for this error.  
`managedInstances[].lastAttempt.errors.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`managedInstances[].lastAttempt.errors.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`managedInstances[].lastAttempt.errors.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`managedInstances[].propertiesFromFlexibilityPolicy` |  `object` Output only. Instance properties selected for this instance resulting from InstanceFlexibilityPolicy.  
`managedInstances[].propertiesFromFlexibilityPolicy.machineType` |  `string` Output only. The machine type to be used for this instance.  
`managedInstances[].propertiesFromFlexibilityPolicy.minCpuPlatform` |  `string` Name of the minimum CPU platform to be used by this instance. e.g. 'Intel Ice Lake'.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[]` |  `object` regionInstanceGroupManagers.list of disks to be attached to the instance.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].kind` |  `string` Output only. Type of the resource. Always `compute#attachedDisk` for attached disks.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].type` |  `enum` Specifies the type of the disk, either `SCRATCH` or `PERSISTENT`. If not specified, the default is `PERSISTENT`.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].mode` |  `enum` The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].savedState` |  `enum` Output only. For LocalSSD disks on VM Instances in STOPPED or SUSPENDED state, this field is set to `PRESERVED` if the LocalSSD data has been saved to a persistent location by customer request. (see the discardLocalSsd option on Stop/Suspend). Read-only in the api.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].source` |  `string` Specifies a valid partial or full URL to an existing Persistent Disk resource. When creating a new instance boot disk, one of `initializeParams.sourceImage` or `initializeParams.sourceSnapshot` or `disks.source` is required.If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.Note that for InstanceTemplate, specify the disk name for zonal disk, and the URL for regional disk.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].deviceName` |  `string` Specifies a unique device name of your choice that is reflected into the `/dev/disk/by-id/google-*` tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.If not specified, the server chooses a default device name to apply to this disk, in the form `persistent-disk-x`, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].index` |  `integer` Output only. A zero-based index to this disk, where 0 is reserved for the boot disk. If you have many disks attached to an instance, each disk would have a unique index number.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].boot` |  `boolean` Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams` |  `object` [Input Only] Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.This property is mutually exclusive with the `source` property; you can only define one or the other, but not both.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.diskName` |  `string` Specifies the disk name. If not specified, the default is to use the name of the instance. If a disk with the same name already exists in the given region, the existing disk is attached to the new instance and the new disk is not created.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceImage` |  `string` The source image to create this disk. When creating a new instance boot disk, one of `initializeParams.sourceImage` or `initializeParams.sourceSnapshot` or `disks.source` is required.To create a disk with one of the [public operating system images](https://docs.cloud.google.com/compute/docs/images/os-details), specify the image by its family name. For example, specify `family/debian-9` to use the latest Debian 9 image: `projects/debian-cloud/global/images/family/debian-9`Alternatively, use a specific version of a public operating system image: `projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD`To create a disk with a custom image that you created, specify the image name in the following format: `global/images/my-custom-image`You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with `family/family-name`: `global/images/family/my-image-family`If the source image is deleted later, this field will not be set.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB. The size must be at least 10 GB. If you specify a `sourceImage`, which is required for boot disks, the default size is the size of the `sourceImage`. If you do not specify a `sourceImage`, the default disk size is 500 GB.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.diskType` |  `string` Specifies the disk type used for the boot disk or an additional data disk. For valid disk type values, see [ Supported types for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk#hd_disk_types) and [ Persistent Disk type variables](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#hd_disk_types).When creating a single instance, you must provide either the full or partial URL of the disk type. For example, the following values are valid: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/diskTypes/diskType`
  * `projects/project/zones/zone/diskTypes/diskType`
  * `zones/zone/diskTypes/diskType`

When creating an instance template, instance flexibility policy, or when creating or updating an all-instances configuration, you specify the disk type without a URL, for example, `hyperdisk-balanced`.If you omit this field for a disk, the default disk type depends on the instance's machine series, as follows. 

  * For first- and second-generation machine series like N1, N2, T2, and M1, the default disk type is Standard Persistent Disk (`pd-standard`).
  * For C3, C3D, and M3 the default is Balanced Persistent Disk (`pd-balanced`).
  * For other third-generation machine series like A3, H3, Z3, all fourth-generation types like C4, N4, M4, and newer machine series, the default is Hyperdisk Balanced (`hyperdisk-balanced`).

The disk type you specify must be compatible with the instance's machine series. For a list of machine series that support Persistent Disk, see [Machine series support for Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#pd-machine-series).For a list of machine series that support Hyperdisk, see [Machine series support for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceImageEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source image. Required if the source image is protected by a customer-supplied encryption key.InstanceTemplate and InstancePropertiesPatch do not store [customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), so you cannot create disks for instances in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) if the source images are encrypted with your own keys.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceImageEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceImageEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceImageEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceImageEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceImageEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.labels` |  `map (key: string, value: string)` Labels to apply to this disk. These can be later modified by the `disks.setLabels` method. This field is only applicable for persistent disks.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceSnapshot` |  `string` The source snapshot to create this disk. When creating a new instance boot disk, one of `initializeParams.sourceSnapshot` or `initializeParams.sourceImage` or `disks.source` is required.To create a disk with a snapshot that you created, specify the snapshot name in the following format: `global/snapshots/my-backup`If the source snapshot is deleted later, this field will not be set.Note: You cannot create VMs in bulk using a snapshot as the source. Use an image instead when you create VMs using the [bulk insert method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceSnapshotEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source snapshot.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceSnapshotEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceSnapshotEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceSnapshotEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceSnapshotEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.sourceSnapshotEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.description` |  `string` An optional description. Provide this property when creating the disk.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.replicaZones[]` |  `string` Required for each regional disk associated with the instance. Specify the URLs of the zones where the disk should be replicated to. You must provide exactly two replica zones, and one zone must be the same as the instance zone.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.resourcePolicies[]` |  `string` Resource policies applied to this disk for automatic snapshot creations. Specified using the full or partial URL. For instance template, specify only the resource policy name.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.onUpdateAction` |  `enum` Specifies which action to take on instance update with this disk. Default is to use the existing disk.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.provisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see the [Extreme persistent disk documentation](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.licenses[]` |  `string` A list of publicly visible licenses. Reserved for Google's use.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.architecture` |  `enum` The architecture of the attached disk. Valid values are arm64 or x86_64.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the disk. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.provisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must greater than or equal to 1.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.enableConfidentialCompute` |  `boolean` Whether this disk is using confidential compute mode.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].initializeParams.storagePool` |  `string` The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/storagePools/storagePool`
  * `projects/project/zones/zone/storagePools/storagePool`
  * `zones/zone/storagePools/storagePool`

  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].autoDelete` |  `boolean` Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].licenses[]` |  `string` Output only. Any valid publicly visible licenses.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. For most machine types, the default is `SCSI`. Local SSDs can use either NVME or SCSI. In certain configurations, persistent disks can use NVMe. For more information, see [About persistent disks](https://cloud.google.com/compute/docs/disks/persistent-disks).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].guestOsFeatures[]` |  `object` A list of features to enable on the guest operating system. Applicable only for bootable images. Read [ Enabling guest operating system features](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features) to see a list of available options.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].guestOsFeatures[].type` |  `enum` The ID of a supported feature. To add multiple values, use commas to separate values. Set to one or more of the following values: 

  * `VIRTIO_SCSI_MULTIQUEUE`
  * `WINDOWS`
  * `MULTI_IP_SUBNET`
  * `UEFI_COMPATIBLE`
  * `GVNIC`
  * `SEV_CAPABLE`
  * `SUSPEND_RESUME_COMPATIBLE`
  * `SEV_LIVE_MIGRATABLE_V2`
  * `SEV_SNP_CAPABLE`
  * `TDX_CAPABLE`
  * `IDPF`
  * `SNP_SVSM_CAPABLE`
  * `CCA_CAPABLE`
  * `SUSPEND_SAFE_FPR`

For more information, see [ Enabling guest operating system features](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features).   
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].diskEncryptionKey` |  `object` Encrypts or decrypts a disk using a [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption).If you are creating a new disk, this field encrypts the new disk using an encryption key that you provide. If you are attaching an existing disk that is already encrypted, this field decrypts the disk using the customer-supplied encryption key.If you encrypt a disk using a customer-supplied key, you must provide the same key again when you attempt to use this resource at a later time. For example, you must provide the key when you create a snapshot or an image from the disk or when you attach the disk to a virtual machine instance.If you do not provide an encryption key, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later.Note:Instance templates do not store [customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), so you cannot use your own keys to encrypt disks in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups).You cannot create VMs that have disks with customer-supplied keys using the [bulk insert method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].diskEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].diskEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].diskEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].diskEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].diskEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The size of the disk in GB.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState` |  `object` Output only. shielded vm initial state stored on disk  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.pk` |  `object` The Platform Key (PK).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.pk.content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.pk.fileType` |  `enum` The file type of source file.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.keks[]` |  `object` The Key Exchange Key (KEK).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.keks[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.keks[].fileType` |  `enum` The file type of source file.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.dbs[]` |  `object` The Key Database (db).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.dbs[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.dbs[].fileType` |  `enum` The file type of source file.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.dbxs[]` |  `object` The forbidden key database (dbx).  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.dbxs[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].shieldedInstanceInitialState.dbxs[].fileType` |  `enum` The file type of source file.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].forceAttach` |  `boolean` [Input Only] Whether to force attach the regional disk even if it's currently attached to another instance. If you try to force attach a zonal disk to an instance, you will receive an error.  
`managedInstances[].propertiesFromFlexibilityPolicy.disks[].architecture` |  `enum` Output only. The architecture of the attached disk. Valid values are ARM64 or X86_64.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
  
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
