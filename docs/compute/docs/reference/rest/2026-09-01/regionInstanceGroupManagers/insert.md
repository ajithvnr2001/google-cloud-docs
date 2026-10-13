---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionInstanceGroupManagers/insert/
title: Method: regionInstanceGroupManagers.insert \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:07.432261+00:00
---

# Method: regionInstanceGroupManagers.insert  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/regionInstanceGroupManagers/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: regionInstanceGroupManagers.insert Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
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
        * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
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
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as `DONE` when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with the [listmanagedinstances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances) method.

A regional managed instance group can contain up to 2000 instances.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/instanceGroupManagers?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region scoping this request.  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`).  
  
### Request body

The request body contains data with the following structure:

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
      "distributionPolicy": {
        "zones": [
          {
            "zone": string
          }
        ],
        "targetShape": enum
      },
      "instanceTemplate": string,
      "versions": [
        {
          "name": string,
          "instanceTemplate": string,
          "targetSize": {
            "fixed": integer,
            "percent": integer,
            "calculated": integer
          }
        }
      ],
      "allInstancesConfig": {
        "properties": {
          "metadata": {
            string: string,
            ...
          },
          "labels": {
            string: string,
            ...
          },
          "exposeHostTopology": boolean
        }
      },
      "instanceGroup": string,
      "targetPools": [
        string
      ],
      "baseInstanceName": string,
      "fingerprint": string,
      "currentActions": {
        "none": integer,
        "creating": integer,
        "creatingWithoutRetries": integer,
        "verifying": integer,
        "recreating": integer,
        "deleting": integer,
        "abandoning": integer,
        "restarting": integer,
        "refreshing": integer,
        "suspending": integer,
        "resuming": integer,
        "stopping": integer,
        "starting": integer
      },
      "status": {
        "isStable": boolean,
        "allInstancesConfig": {
          "effective": boolean,
          "currentRevision": string
        },
        "versionTarget": {
          "isReached": boolean
        },
        "stateful": {
          "hasStatefulConfig": boolean,
          "perInstanceConfigs": {
            "allEffective": boolean
          }
        },
        "autoscaler": string,
        "bulkInstanceOperation": {
          "inProgress": boolean,
          "lastProgressCheck": {
            "timestamp": string,
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
        "appliedAcceleratorTopologies": [
          {
            "acceleratorTopology": string,
            "state": enum,
            "stateDetails": {
              "timestamp": string,
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
          }
        ],
        "currentInstanceStatuses": {
          "nonExistent": integer,
          "provisioning": integer,
          "staging": integer,
          "running": integer,
          "stopping": integer,
          "stopped": integer,
          "terminated": integer,
          "suspending": integer,
          "suspended": integer,
          "repairing": integer,
          "deprovisioning": integer,
          "pendingStop": integer,
          "pending": integer
        }
      },
      "targetSize": integer,
      "targetSizePolicy": {
        "mode": enum
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          string: {
            "machineTypes": [
              string
            ],
            "rank": integer,
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
                    "sha256": string,
                    "kmsKeyServiceAccount": string,
    
                    // The following is a list of mutually exclusive fields. At most one of the
                    // fields will be set in a response:
                    "rawKey": string,
                    "rsaEncryptedKey": string,
                    "kmsKeyName": string
                    // End of mutually exclusive fields.
                  },
                  "labels": {
                    string: string,
                    ...
                  },
                  "sourceSnapshot": string,
                  "sourceSnapshotEncryptionKey": {
                    "sha256": string,
                    "kmsKeyServiceAccount": string,
    
                    // The following is a list of mutually exclusive fields. At most one of the
                    // fields will be set in a response:
                    "rawKey": string,
                    "rsaEncryptedKey": string,
                    "kmsKeyName": string
                    // End of mutually exclusive fields.
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
                  "rawKey": string,
                  "rsaEncryptedKey": string,
                  "kmsKeyName": string,
                  "sha256": string,
                  "kmsKeyServiceAccount": string
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
          },
          ...
        }
      },
      "targetStoppedSize": integer,
      "targetSuspendedSize": integer,
      "listManagedInstancesResults": enum,
      "standbyPolicy": {
        "initialDelaySec": integer,
        "mode": enum
      },
      "selfLink": string,
      "autoHealingPolicies": [
        {
          "healthCheck": string,
          "initialDelaySec": integer
        }
      ],
      "updatePolicy": {
        "type": enum,
        "instanceRedistributionType": enum,
        "minimalAction": enum,
        "mostDisruptiveAllowedAction": enum,
        "maxSurge": {
          "fixed": integer,
          "percent": integer,
          "calculated": integer
        },
        "maxUnavailable": {
          "fixed": integer,
          "percent": integer,
          "calculated": integer
        },
        "replacementMethod": enum
      },
      "namedPorts": [
        {
          "name": string,
          "port": integer
        }
      ],
      "statefulPolicy": {
        "preservedState": {
          "disks": {
            string: {
              "autoDelete": enum
            },
            ...
          },
          "internalIPs": {
            string: {
              "autoDelete": enum
            },
            ...
          },
          "externalIPs": {
            string: {
              "autoDelete": enum
            },
            ...
          }
        }
      },
      "instanceLifecyclePolicy": {
        "forceUpdateOnRepair": enum,
        "defaultActionOnFailure": enum,
        "onFailedHealthCheck": enum,
        "onRepair": {
          "allowChangingZone": enum
        }
      },
      "satisfiesPzi": boolean,
      "satisfiesPzs": boolean,
      "resourcePolicies": {
        "workloadPolicy": string
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. The resource type, which is always `compute#instanceGroupManager` for managed instance groups.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. A unique identifier for this resource type. The server generates this identifier.  
`creationTimestamp` |  `string` Output only. The creation timestamp for this managed instance group in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` [REQUIRED] The name of the managed instance group. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`description` |  `string` An optional description of this resource.  
`zone` |  `string` Output only. The URL of a [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the managed instance group is located (for zonal resources).  
`region` |  `string` Output only. The URL of the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the managed instance group resides (for regional resources).  
`distributionPolicy` |  `object` Policy specifying the intended distribution of managed instances across zones in a regional managed instance group.  
`distributionPolicy.zones[]` |  `object` Zones where the regional managed instance group will create and manage its instances. By default, a regional MIG doesn't automatically select an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) to create instances, even if an AI zone is available in the specified region. To create instances in an AI zone in the selected region, you must explicitly specify it in the distribution policy together with the other preferred zones.  
`distributionPolicy.zones[].zone` |  `string` [REQUIRED] The URL of the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available). The zone must exist in the region where the managed instance group is located.  
`distributionPolicy.targetShape` |  `enum` The distribution shape to which the group converges either proactively or on resize events (depending on the value set in `updatePolicy.instanceRedistributionType`).  
`instanceTemplate` |  `string` The URL of the instance template that is specified for this managed instance group. The group uses this template to create all new instances in the managed instance group. The templates for existing instances in the group do not change unless you run `recreateInstances`, run `applyUpdatesToInstances`, or set the group's `updatePolicy.type` to `PROACTIVE`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `instanceTemplate`:

  * `compute.instanceTemplates.get`
  * `compute.instanceTemplates.useReadOnly`

  
`versions[]` |  `object` Specifies the instance templates used by this managed instance group to create instances.Each version is defined by an `instanceTemplate` and a `name`. Every version can appear at most once per instance group. This field overrides the top-level `instanceTemplate` field. Read more about the [relationships between these fields](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#relationship_between_versions_and_instancetemplate_properties_for_a_managed_instance_group). Exactly one `version` must leave the `targetSize` field unset. That version will be applied to all remaining instances. For more information, read about [canary updates](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#starting_a_canary_update).  
`versions[].name` |  `string` Name of the version. Unique among all versions in the scope of this managed instance group.  
`versions[].instanceTemplate` |  `string` The URL of the instance template that is specified for this managed instance group. The group uses this template to create new instances in the managed instance group until the `targetSize` for this version is reached. The templates for existing instances in the group do not change unless you run `recreateInstances`, run `applyUpdatesToInstances`, or set the group's `updatePolicy.type` to `PROACTIVE`; in those cases, existing instances are updated until the `targetSize` for this version is reached. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `instanceTemplate`:

  * `compute.instanceTemplates.get`
  * `compute.instanceTemplates.useReadOnly`

  
`versions[].targetSize` |  `object` Specifies the intended number of instances to be created from the `instanceTemplate`. The final number of instances created from the template will be equal to: 

  * If expressed as a fixed number, the minimum of either `targetSize.fixed` or `instanceGroupManager.targetSize` is used.
  * if expressed as a `percent`, the `targetSize` would be `(targetSize.percent/100 * InstanceGroupManager.targetSize)` If there is a remainder, the number is rounded.

If unset, this version will update any remaining instances not updated by another `version`. Read [Starting a canary update](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#starting_a_canary_update) for more information.   
`versions[].targetSize.fixed` |  `integer` Specifies a fixed number of VM instances. This must be a positive integer.  
`versions[].targetSize.percent` |  `integer` Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify `80` for 80%.  
`versions[].targetSize.calculated` |  `integer` Output only. Absolute value of VM instances calculated based on the specific mode.

  * If the value is `fixed`, then the `calculated` value is equal to the `fixed` value.
  * If the value is a `percent`, then the `calculated` value is `percent`/100 * `targetSize`. For example, the `calculated` value of a 80% of a managed instance group with 150 instances would be (80/100 * 150) = 120 VM instances. If there is a remainder, the number is rounded.

  
`allInstancesConfig` |  `object` Specifies configuration that overrides the instance template configuration for the group.  
`allInstancesConfig.properties` |  `object` Properties to set on all instances in the group.You can add or modify properties using the `instanceGroupManagers.patch` or `regionInstanceGroupManagers.patch`. After setting `allInstancesConfig` on the group, you must update the group's instances to apply the configuration. To apply the configuration, set the group's `updatePolicy.type` field to use proactive updates or use the `applyUpdatesToInstances` method.  
`allInstancesConfig.properties.metadata` |  `map (key: string, value: string)` The metadata key-value pairs that you want to patch onto the instance. For more information, see [Project and instance metadata](https://docs.cloud.google.com/compute/docs/metadata#project_and_instance_metadata).  
`allInstancesConfig.properties.labels` |  `map (key: string, value: string)` The label key-value pairs that you want to patch onto the instance.  
`allInstancesConfig.properties.exposeHostTopology` |  `boolean` This optional flag exposes the hashed physical host ID.  
`instanceGroup` |  `string` Output only. The URL of the Instance Group resource.  
`targetPools[]` |  `string` The URLs for all TargetPool resources to which instances in the `instanceGroup` field are added. The target pools automatically apply to all of the instances in the managed instance group. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `targetPools`:

  * `compute.targetPools.get`

  
`baseInstanceName` |  `string` The base instance name is a prefix that you want to attach to the names of all VMs in a MIG. The maximum character length is 58 and the name must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) format.When a VM is created in the group, the MIG appends a hyphen and a random four-character string to the base instance name. If you want the MIG to assign sequential numbers instead of a random string, then end the base instance name with a hyphen followed by one or more hash symbols. The hash symbols indicate the number of digits. For example, a base instance name of "vm-###" results in "vm-001" as a VM name. @pattern [a-z](([-a-z0-9]{0,57})|([-a-z0-9]{0,51}-#{1,10}(\\[[0-9]{1,10}\\])?))  
`fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. This field may be used in optimistic locking. It will be ignored when inserting an InstanceGroupManager. An up-to-date fingerprint must be provided in order to update the InstanceGroupManager, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve an InstanceGroupManager.A base64-encoded string.  
`currentActions` |  `object` Output only. The list of instance actions and the number of instances in this managed instance group that are scheduled for each of those actions.  
`currentActions.none` |  `integer` Output only. The number of instances in the managed instance group that are running and have no scheduled actions.  
`currentActions.creating` |  `integer` Output only. The number of instances in the managed instance group that are scheduled to be created or are currently being created. If the group fails to create any of these instances, it tries again until it creates the instance successfully.If you have disabled creation retries, this field will not be populated; instead, the `creatingWithoutRetries` field will be populated.  
`currentActions.creatingWithoutRetries` |  `integer` Output only. The number of instances that the managed instance group will attempt to create. The group attempts to create each instance only once. If the group fails to create any of these instances, it decreases the group's `targetSize` value accordingly.  
`currentActions.verifying` |  `integer` Output only. The number of instances in the managed instance group that are being verified. See the `managedInstances[].currentAction` property in the `listManagedInstances` method documentation.  
`currentActions.recreating` |  `integer` Output only. The number of instances in the managed instance group that are scheduled to be recreated or are currently being being recreated. Recreating an instance deletes the existing root persistent disk and creates a new disk from the image that is defined in the instance template.  
`currentActions.deleting` |  `integer` Output only. The number of instances in the managed instance group that are scheduled to be deleted or are currently being deleted.  
`currentActions.abandoning` |  `integer` Output only. The total number of instances in the managed instance group that are scheduled to be abandoned. Abandoning an instance removes it from the managed instance group without deleting it.  
`currentActions.restarting` |  `integer` Output only. The number of instances in the managed instance group that are scheduled to be restarted or are currently being restarted.  
`currentActions.refreshing` |  `integer` Output only. The number of instances in the managed instance group that are being reconfigured with properties that do not require a restart or a recreate action. For example, setting or removing target pools for the instance.  
`currentActions.suspending` |  `integer` Output only. The number of instances in the managed instance group that are scheduled to be suspended or are currently being suspended.  
`currentActions.resuming` |  `integer` Output only. The number of instances in the managed instance group that are scheduled to be resumed or are currently being resumed.  
`currentActions.stopping` |  `integer` Output only. The number of instances in the managed instance group that are scheduled to be stopped or are currently being stopped.  
`currentActions.starting` |  `integer` Output only. The number of instances in the managed instance group that are scheduled to be started or are currently being started.  
`status` |  `object` Output only. The status of this managed instance group.  
`status.isStable` |  `boolean` Output only. A bit indicating whether the managed instance group is in a stable state. A stable state means that: none of the instances in the managed instance group is currently undergoing any type of change (for example, creation, restart, or deletion); no future changes are scheduled for instances in the managed instance group; and the managed instance group itself is not being modified.  
`status.allInstancesConfig` |  `object` Output only. Status of all-instances configuration on the group.  
`status.allInstancesConfig.effective` |  `boolean` Output only. A bit indicating whether this configuration has been applied to all managed instances in the group.  
`status.allInstancesConfig.currentRevision` |  `string` Output only. Current all-instances configuration revision. This value is in RFC3339 text format.  
`status.versionTarget` |  `object` Output only. A status of consistency of Instances' versions with their target version specified by `version` field on Instance Group Manager.  
`status.versionTarget.isReached` |  `boolean` Output only. A bit indicating whether version target has been reached in this managed instance group, i.e. all instances are in their target version. Instances' target version are specified by `version` field on Instance Group Manager.  
`status.stateful` |  `object` Output only. Stateful status of the given Instance Group Manager.  
`status.stateful.hasStatefulConfig` |  `boolean` Output only. A bit indicating whether the managed instance group has stateful configuration, that is, if you have configured any items in a stateful policy or in per-instance configs. The group might report that it has no stateful configuration even when there is still some preserved state on a managed instance, for example, if you have deleted all PICs but not yet applied those deletions.  
`status.stateful.perInstanceConfigs` |  `object` Output only. Status of per-instance configurations on the instances.  
`status.stateful.perInstanceConfigs.allEffective` |  `boolean` Output only. A bit indicating if all of the group's per-instance configurations (listed in the output of a listPerInstanceConfigs API call) have status `EFFECTIVE` or there are no per-instance-configs.  
`status.autoscaler` |  `string` Output only. The URL of the [Autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler) that targets this instance group manager.  
`status.bulkInstanceOperation` |  `object` Output only. The status of bulk instance operation.  
`status.bulkInstanceOperation.inProgress` |  `boolean` Output only. Informs whether bulk instance operation is in progress.  
`status.bulkInstanceOperation.lastProgressCheck` |  `object` Output only. Information from the last progress check of bulk instance operation.  
`status.bulkInstanceOperation.lastProgressCheck.timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the last progress check of bulk instance operation. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status.bulkInstanceOperation.lastProgressCheck.error` |  `object` Output only. Errors encountered during bulk instance operation.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`status.bulkInstanceOperation.lastProgressCheck.error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`status.appliedAcceleratorTopologies[]` |  `object` Output only. The accelerator topology applied to this MIG. Currently only one accelerator topology is supported.  
`status.appliedAcceleratorTopologies[].acceleratorTopology` |  `string` Output only. Topology in the format of: "16x16", "4x4x4", etc. The value is the same as configured in the WorkloadPolicy.  
`status.appliedAcceleratorTopologies[].state` |  `enum` Output only. The state of the accelerator topology.  
`status.appliedAcceleratorTopologies[].stateDetails` |  `object` Output only. The result of the latest accelerator topology state check.  
`status.appliedAcceleratorTopologies[].stateDetails.timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp is shown only if there is an error. The field has // [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) // text format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status.appliedAcceleratorTopologies[].stateDetails.error` |  `object` Output only. Encountered errors.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`status.appliedAcceleratorTopologies[].stateDetails.error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`status.currentInstanceStatuses` |  `object` Output only. The list of instance statuses and the number of instances in this managed instance group that have the status. Currently only shown for TPU MIGs  
`status.currentInstanceStatuses.nonExistent` |  `integer` Output only. The number of instances that have not been created yet or have been deleted. Includes only instances that would be shown in the listManagedInstances method and not all instances that have been deleted in the lifetime of the MIG. Does not include FlexStart instances that are waiting for the resources availability, they are considered as 'pending'.  
`status.currentInstanceStatuses.provisioning` |  `integer` Output only. The number of instances in the managed instance group that have PROVISIONING status.  
`status.currentInstanceStatuses.staging` |  `integer` Output only. The number of instances in the managed instance group that have STAGING status.  
`status.currentInstanceStatuses.running` |  `integer` Output only. The number of instances in the managed instance group that have RUNNING status.  
`status.currentInstanceStatuses.stopping` |  `integer` Output only. The number of instances in the managed instance group that have STOPPING status.  
`status.currentInstanceStatuses.stopped` |  `integer` Output only. The number of instances in the managed instance group that have STOPPED status.  
`status.currentInstanceStatuses.terminated` |  `integer` Output only. The number of instances in the managed instance group that have TERMINATED status.  
`status.currentInstanceStatuses.suspending` |  `integer` Output only. The number of instances in the managed instance group that have SUSPENDING status.  
`status.currentInstanceStatuses.suspended` |  `integer` Output only. The number of instances in the managed instance group that have SUSPENDED status.  
`status.currentInstanceStatuses.repairing` |  `integer` Output only. The number of instances in the managed instance group that have REPAIRING status.  
`status.currentInstanceStatuses.deprovisioning` |  `integer` Output only. The number of instances in the managed instance group that have DEPROVISIONING status.  
`status.currentInstanceStatuses.pendingStop` |  `integer` Output only. The number of instances in the managed instance group that have PENDING_STOP status.  
`status.currentInstanceStatuses.pending` |  `integer` Output only. The number of instances in the managed instance group that have PENDING status, that is FlexStart instances that are waiting for resources. Instances that do not exist because of the other reasons are counted as 'nonExistent'.  
`targetSize` |  `integer` [REQUIRED] The target number of running instances for this managed instance group. You can reduce this number by using the instanceGroupManager deleteInstances or abandonInstances methods. Resizing the group also changes this number.  
`targetSizePolicy` |  `object` The policy that specifies how the MIG creates its VMs to achieve the target size.  
`targetSizePolicy.mode` |  `enum` The mode of target size policy based on which the MIG creates its VMs individually or all at once.  
`instanceFlexibilityPolicy` |  `object` Instance flexibility allowing MIG to create VMs from multiple types of machines. Instance flexibility configuration on MIG overrides instance template configuration.  
`instanceFlexibilityPolicy.instanceSelections[]` |  `map (key: string, value: object)` Named instance selections configuring properties that the group will use when creating new VMs.  
`instanceFlexibilityPolicy.instanceSelections[].machineTypes[]` |  `string` Full machine-type names, e.g. "n1-standard-16".  
`instanceFlexibilityPolicy.instanceSelections[].rank` |  `integer` Preference of this instance selection. Lower number means higher preference. MIG will first try to create a VM based on the machine-type with lowest rank and fallback to next rank based on availability. Machine types and instance selections with the same rank have the same preference.  
`instanceFlexibilityPolicy.instanceSelections[].minCpuPlatform` |  `string` Name of the minimum CPU platform to be used by this instance selection. e.g. 'Intel Ice Lake'.  
`instanceFlexibilityPolicy.instanceSelections[].disks[]` |  `object` regionInstanceGroupManagers.list of disks to be attached to the instances created from this selection.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].kind` |  `string` Output only. Type of the resource. Always `compute#attachedDisk` for attached disks.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].type` |  `enum` Specifies the type of the disk, either `SCRATCH` or `PERSISTENT`. If not specified, the default is `PERSISTENT`.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].mode` |  `enum` The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].savedState` |  `enum` Output only. For LocalSSD disks on VM Instances in STOPPED or SUSPENDED state, this field is set to `PRESERVED` if the LocalSSD data has been saved to a persistent location by customer request. (see the discardLocalSsd option on Stop/Suspend). Read-only in the api.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].source` |  `string` Specifies a valid partial or full URL to an existing Persistent Disk resource. When creating a new instance boot disk, one of `initializeParams.sourceImage` or `initializeParams.sourceSnapshot` or `disks.source` is required.If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.Note that for InstanceTemplate, specify the disk name for zonal disk, and the URL for regional disk.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].deviceName` |  `string` Specifies a unique device name of your choice that is reflected into the `/dev/disk/by-id/google-*` tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.If not specified, the server chooses a default device name to apply to this disk, in the form `persistent-disk-x`, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].index` |  `integer` Output only. A zero-based index to this disk, where 0 is reserved for the boot disk. If you have many disks attached to an instance, each disk would have a unique index number.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].boot` |  `boolean` Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams` |  `object` [Input Only] Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.This property is mutually exclusive with the `source` property; you can only define one or the other, but not both.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.diskName` |  `string` Specifies the disk name. If not specified, the default is to use the name of the instance. If a disk with the same name already exists in the given region, the existing disk is attached to the new instance and the new disk is not created.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceImage` |  `string` The source image to create this disk. When creating a new instance boot disk, one of `initializeParams.sourceImage` or `initializeParams.sourceSnapshot` or `disks.source` is required.To create a disk with one of the [public operating system images](https://docs.cloud.google.com/compute/docs/images/os-details), specify the image by its family name. For example, specify `family/debian-9` to use the latest Debian 9 image: `projects/debian-cloud/global/images/family/debian-9`Alternatively, use a specific version of a public operating system image: `projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD`To create a disk with a custom image that you created, specify the image name in the following format: `global/images/my-custom-image`You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with `family/family-name`: `global/images/family/my-image-family`If the source image is deleted later, this field will not be set.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB. The size must be at least 10 GB. If you specify a `sourceImage`, which is required for boot disks, the default size is the size of the `sourceImage`. If you do not specify a `sourceImage`, the default disk size is 500 GB.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.diskType` |  `string` Specifies the disk type used for the boot disk or an additional data disk. For valid disk type values, see [ Supported types for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk#hd_disk_types) and [ Persistent Disk type variables](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#hd_disk_types).When creating a single instance, you must provide either the full or partial URL of the disk type. For example, the following values are valid: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/diskTypes/diskType`
  * `projects/project/zones/zone/diskTypes/diskType`
  * `zones/zone/diskTypes/diskType`

When creating an instance template, instance flexibility policy, or when creating or updating an all-instances configuration, you specify the disk type without a URL, for example, `hyperdisk-balanced`.If you omit this field for a disk, the default disk type depends on the instance's machine series, as follows. 

  * For first- and second-generation machine series like N1, N2, T2, and M1, the default disk type is Standard Persistent Disk (`pd-standard`).
  * For C3, C3D, and M3 the default is Balanced Persistent Disk (`pd-balanced`).
  * For other third-generation machine series like A3, H3, Z3, all fourth-generation types like C4, N4, M4, and newer machine series, the default is Hyperdisk Balanced (`hyperdisk-balanced`).

The disk type you specify must be compatible with the instance's machine series. For a list of machine series that support Persistent Disk, see [Machine series support for Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#pd-machine-series).For a list of machine series that support Hyperdisk, see [Machine series support for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceImageEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source image. Required if the source image is protected by a customer-supplied encryption key.InstanceTemplate and InstancePropertiesPatch do not store [customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), so you cannot create disks for instances in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) if the source images are encrypted with your own keys.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceImageEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceImageEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceImageEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceImageEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceImageEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.labels` |  `map (key: string, value: string)` Labels to apply to this disk. These can be later modified by the `disks.setLabels` method. This field is only applicable for persistent disks.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceSnapshot` |  `string` The source snapshot to create this disk. When creating a new instance boot disk, one of `initializeParams.sourceSnapshot` or `initializeParams.sourceImage` or `disks.source` is required.To create a disk with a snapshot that you created, specify the snapshot name in the following format: `global/snapshots/my-backup`If the source snapshot is deleted later, this field will not be set.Note: You cannot create VMs in bulk using a snapshot as the source. Use an image instead when you create VMs using the [bulk insert method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceSnapshotEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source snapshot.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceSnapshotEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceSnapshotEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceSnapshotEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceSnapshotEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceSnapshotEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.description` |  `string` An optional description. Provide this property when creating the disk.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.replicaZones[]` |  `string` Required for each regional disk associated with the instance. Specify the URLs of the zones where the disk should be replicated to. You must provide exactly two replica zones, and one zone must be the same as the instance zone.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.resourcePolicies[]` |  `string` Resource policies applied to this disk for automatic snapshot creations. Specified using the full or partial URL. For instance template, specify only the resource policy name.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.onUpdateAction` |  `enum` Specifies which action to take on instance update with this disk. Default is to use the existing disk.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.provisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see the [Extreme persistent disk documentation](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.licenses[]` |  `string` A list of publicly visible licenses. Reserved for Google's use.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.architecture` |  `enum` The architecture of the attached disk. Valid values are arm64 or x86_64.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the disk. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.provisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must greater than or equal to 1.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.enableConfidentialCompute` |  `boolean` Whether this disk is using confidential compute mode.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.storagePool` |  `string` The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/storagePools/storagePool`
  * `projects/project/zones/zone/storagePools/storagePool`
  * `zones/zone/storagePools/storagePool`

  
`instanceFlexibilityPolicy.instanceSelections[].disks[].autoDelete` |  `boolean` Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].licenses[]` |  `string` Output only. Any valid publicly visible licenses.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. For most machine types, the default is `SCSI`. Local SSDs can use either NVME or SCSI. In certain configurations, persistent disks can use NVMe. For more information, see [About persistent disks](https://cloud.google.com/compute/docs/disks/persistent-disks).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].guestOsFeatures[]` |  `object` A list of features to enable on the guest operating system. Applicable only for bootable images. Read [ Enabling guest operating system features](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features) to see a list of available options.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].guestOsFeatures[].type` |  `enum` The ID of a supported feature. To add multiple values, use commas to separate values. Set to one or more of the following values: 

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
`instanceFlexibilityPolicy.instanceSelections[].disks[].diskEncryptionKey` |  `object` Encrypts or decrypts a disk using a [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption).If you are creating a new disk, this field encrypts the new disk using an encryption key that you provide. If you are attaching an existing disk that is already encrypted, this field decrypts the disk using the customer-supplied encryption key.If you encrypt a disk using a customer-supplied key, you must provide the same key again when you attempt to use this resource at a later time. For example, you must provide the key when you create a snapshot or an image from the disk or when you attach the disk to a virtual machine instance.If you do not provide an encryption key, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later.Note:Instance templates do not store [customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), so you cannot use your own keys to encrypt disks in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups).You cannot create VMs that have disks with customer-supplied keys using the [bulk insert method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].diskEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].diskEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].diskEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].diskEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].diskEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The size of the disk in GB.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState` |  `object` Output only. shielded vm initial state stored on disk  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.pk` |  `object` The Platform Key (PK).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.pk.content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.pk.fileType` |  `enum` The file type of source file.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.keks[]` |  `object` The Key Exchange Key (KEK).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.keks[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.keks[].fileType` |  `enum` The file type of source file.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.dbs[]` |  `object` The Key Database (db).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.dbs[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.dbs[].fileType` |  `enum` The file type of source file.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.dbxs[]` |  `object` The forbidden key database (dbx).  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.dbxs[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].shieldedInstanceInitialState.dbxs[].fileType` |  `enum` The file type of source file.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].forceAttach` |  `boolean` [Input Only] Whether to force attach the regional disk even if it's currently attached to another instance. If you try to force attach a zonal disk to an instance, you will receive an error.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].architecture` |  `enum` Output only. The architecture of the attached disk. Valid values are ARM64 or X86_64.  
`targetStoppedSize` |  `integer` The target number of stopped instances for this managed instance group. This number changes when you: 

  * Stop instance using the [stopInstances](https://docs.cloud.google.com/compute/docs/reference/v1/instanceGroupManagers/stopInstances) method or start instances using the [startInstances](https://docs.cloud.google.com/compute/docs/reference/v1/instanceGroupManagers/startInstances) method.
  * Manually change the `targetStoppedSize` using the [update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/update) method.

  
`targetSuspendedSize` |  `integer` The target number of suspended instances for this managed instance group. This number changes when you: 

  * Suspend instance using the [suspendInstances](https://docs.cloud.google.com/compute/docs/reference/v1/instanceGroupManagers/suspendInstances) method or resume instances using the [resumeInstances](https://docs.cloud.google.com/compute/docs/reference/v1/instanceGroupManagers/resumeInstances) method.
  * Manually change the `targetSuspendedSize` using the [update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/update) method.

  
`listManagedInstancesResults` |  `enum` Pagination behavior of the `listManagedInstances` API method for this managed instance group.  
`standbyPolicy` |  `object` Standby policy for stopped and suspended instances.  
`standbyPolicy.initialDelaySec` |  `integer` Specifies the number of seconds that the MIG should wait to suspend or stop a VM after that VM was created. The initial delay gives the initialization script the time to prepare your VM for a quick scale out. The value of initial delay must be between 0 and 3600 seconds. The default value is 0.  
`standbyPolicy.mode` |  `enum` Defines how a MIG resumes or starts VMs from a standby pool when the group scales out. The default mode is `MANUAL`.  
`selfLink` |  `string` Output only. The URL for this managed instance group. The server defines this URL.  
`autoHealingPolicies[]` |  `object` The autohealing policy for this managed instance group. You can specify only one value.  
`autoHealingPolicies[].healthCheck` |  `string` The URL for the health check that signals autohealing. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `healthCheck`:

  * `compute.httpsHealthChecks.use`

  
`autoHealingPolicies[].initialDelaySec` |  `integer` The initial delay is the number of seconds that a new VM takes to initialize and run its startup script. During a VM's initial delay period, the MIG ignores unsuccessful health checks because the VM might be in the startup process. This prevents the MIG from prematurely recreating a VM. If the health check receives a healthy response during the initial delay, it indicates that the startup process is complete and the VM is ready. The value of initial delay must be between 0 and 3600 seconds. The default value is 0.  
`updatePolicy` |  `object` The update policy for this managed instance group.  
`updatePolicy.type` |  `enum` The [type of update process](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#choosing_between_automated_and_selective_updates). You can specify either `PROACTIVE` so that the MIG automatically updates VMs to the latest configurations or `OPPORTUNISTIC` so that you can select the VMs that you want to update.  
`updatePolicy.instanceRedistributionType` |  `enum` The [ instance redistribution policy](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution) for regional managed instance groups. Valid values are: 

  * `PROACTIVE` (default): The group attempts to maintain an even distribution of VM instances across zones in the region.
  * `NONE`: For non-autoscaled groups, proactive redistribution is disabled.

  
`updatePolicy.minimalAction` |  `enum` Minimal action to be taken on an instance. Use this option to minimize disruption as much as possible or to apply a more disruptive action than is necessary.

  * To limit disruption as much as possible, set the minimal action to `REFRESH`. If your update requires a more disruptive action, Compute Engine performs the necessary action to execute the update.
  * To apply a more disruptive action than is strictly necessary, set the minimal action to `RESTART` or `REPLACE`. For example, Compute Engine does not need to restart a VM to change its metadata. But if your application reads instance metadata only when a VM is restarted, you can set the minimal action to `RESTART` in order to pick up metadata changes.

  
`updatePolicy.mostDisruptiveAllowedAction` |  `enum` Most disruptive action that is allowed to be taken on an instance. You can specify either `NONE` to forbid any actions, `REFRESH` to avoid restarting the VM and to limit disruption as much as possible. `RESTART` to allow actions that can be applied without instance replacing or `REPLACE` to allow all possible actions. If the Updater determines that the minimal update action needed is more disruptive than most disruptive allowed action you specify it will not perform the update at all.  
`updatePolicy.maxSurge` |  `object` The maximum number of instances that can be created above the specified `targetSize` during the update process. This value can be either a fixed number or, if the group has 10 or more instances, a percentage. If you set a percentage, the number of instances is rounded if necessary. The default value for `maxSurge` is a fixed value equal to the number of zones in which the managed instance group operates.At least one of either `maxSurge` or `maxUnavailable` must be greater than 0. Learn more about [`maxSurge`](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#maxSurge).  
`updatePolicy.maxSurge.fixed` |  `integer` Specifies a fixed number of VM instances. This must be a positive integer.  
`updatePolicy.maxSurge.percent` |  `integer` Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify `80` for 80%.  
`updatePolicy.maxSurge.calculated` |  `integer` Output only. Absolute value of VM instances calculated based on the specific mode.

  * If the value is `fixed`, then the `calculated` value is equal to the `fixed` value.
  * If the value is a `percent`, then the `calculated` value is `percent`/100 * `targetSize`. For example, the `calculated` value of a 80% of a managed instance group with 150 instances would be (80/100 * 150) = 120 VM instances. If there is a remainder, the number is rounded.

  
`updatePolicy.maxUnavailable` |  `object` The maximum number of instances that can be unavailable during the update process. An instance is considered available if all of the following conditions are satisfied:

  * The instance's [status](https://docs.cloud.google.com/compute/docs/instances/checking-instance-status) is `RUNNING`.
  * If there is a [health check](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) on the instance group, the instance's health check status must be `HEALTHY` at least once. If there is no health check on the group, then the instance only needs to have a status of `RUNNING` to be considered available.

This value can be either a fixed number or, if the group has 10 or more instances, a percentage. If you set a percentage, the number of instances is rounded if necessary. The default value for `maxUnavailable` is a fixed value equal to the number of zones in which the managed instance group operates.At least one of either `maxSurge` or `maxUnavailable` must be greater than 0. Learn more about [`maxUnavailable`](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#maxUnavailable).  
`updatePolicy.maxUnavailable.fixed` |  `integer` Specifies a fixed number of VM instances. This must be a positive integer.  
`updatePolicy.maxUnavailable.percent` |  `integer` Specifies a percentage of instances between 0 to 100%, inclusive. For example, specify `80` for 80%.  
`updatePolicy.maxUnavailable.calculated` |  `integer` Output only. Absolute value of VM instances calculated based on the specific mode.

  * If the value is `fixed`, then the `calculated` value is equal to the `fixed` value.
  * If the value is a `percent`, then the `calculated` value is `percent`/100 * `targetSize`. For example, the `calculated` value of a 80% of a managed instance group with 150 instances would be (80/100 * 150) = 120 VM instances. If there is a remainder, the number is rounded.

  
`updatePolicy.replacementMethod` |  `enum` What action should be used to replace instances. See minimalAction.REPLACE  
`namedPorts[]` |  `object` Output only. Named ports configured on the Instance Groups complementary to this Instance Group Manager.  
`namedPorts[].name` |  `string` The name for this named port. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`namedPorts[].port` |  `integer` The port number, which can be a value between 1 and 65535.  
`statefulPolicy` |  `object` Stateful configuration for this Instanced Group Manager  
`statefulPolicy.preservedState` |  `object`  
`statefulPolicy.preservedState.disks[]` |  `map (key: string, value: object)` Disks created on the instances that will be preserved on instance delete, update, etc. This map is keyed with the device names of the disks.  
`statefulPolicy.preservedState.disks[].autoDelete` |  `enum` These stateful disks will never be deleted during autohealing, update or VM instance recreate operations. This flag is used to configure if the disk should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted. Note: disks attached in `READ_ONLY` mode cannot be auto-deleted.  
`statefulPolicy.preservedState.internalIPs[]` |  `map (key: string, value: object)` Internal network IPs assigned to the instances that will be preserved on instance delete, update, etc. This map is keyed with the network interface name. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `internalIPs`:

  * `compute.addresses.createInternal`
  * `compute.addresses.deleteInternal`
  * `compute.addresses.get`
  * `compute.addresses.useInternal`

  
`statefulPolicy.preservedState.internalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`statefulPolicy.preservedState.externalIPs[]` |  `map (key: string, value: object)` External network IPs assigned to the instances that will be preserved on instance delete, update, etc. This map is keyed with the network interface name. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `externalIPs`:

  * `compute.addresses.create`
  * `compute.addresses.delete`
  * `compute.addresses.get`
  * `compute.addresses.use`

  
`statefulPolicy.preservedState.externalIPs[].autoDelete` |  `enum` These stateful IPs will never be released during autohealing, update or VM instance recreate operations. This flag is used to configure if the IP reservation should be deleted after it is no longer used by the group, e.g. when the given instance or the whole group is deleted.  
`instanceLifecyclePolicy` |  `object` The repair policy for this managed instance group.  
`instanceLifecyclePolicy.forceUpdateOnRepair` |  `enum` A bit indicating whether to forcefully apply the group's latest configuration when repairing a VM. Valid options are:

  * NO (default): If configuration updates are available, they are not forcefully applied during repair. Instead, configuration updates are applied according to the group's update policy.
  * YES: If configuration updates are available, they are applied during repair.

  
`instanceLifecyclePolicy.defaultActionOnFailure` |  `enum` The action that a MIG performs on a failed VM. If the value of the onFailedHealthCheck field is `DEFAULT_ACTION`, then the same action also applies to the VMs on which your application fails a health check. Valid values are 

  * `REPAIR` (default): MIG automatically repairs a failed VM by recreating it. For more information, see [About repairing VMs in a MIG](https://cloud.google.com/compute/docs/instance-groups/about-repair).
  * `DO_NOTHING`: MIG does not repair a failed VM.

  
`instanceLifecyclePolicy.onFailedHealthCheck` |  `enum` The action that a MIG performs on an unhealthy VM. A VM is marked as unhealthy when the application running on that VM fails a health check. Valid values are:

  * `DEFAULT_ACTION (default)`: MIG uses the same action configured for instanceLifecyclePolicy.defaultActionOnFailure field.
  * `REPAIR`: MIG automatically repairs an unhealthy VM by recreating it.
  * `DO_NOTHING`: MIG doesn't repair an unhealthy VM.
For more information, see [ About repairing VMs in a MIG](https://cloud.google.com/compute/docs/instance-groups/about-repair). 
  
`instanceLifecyclePolicy.onRepair` |  `object` Configuration for VM repairs in the MIG.  
`instanceLifecyclePolicy.onRepair.allowChangingZone` |  `enum` Specifies whether the MIG can change a VM's zone during a repair. Valid values are:

  * `NO (default)`: MIG cannot change a VM's zone during a repair.
  * `YES`: MIG can select a different zone for the VM during a repair.

  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`resourcePolicies` |  `object` Resource policies for this managed instance group.  
`resourcePolicies.workloadPolicy` |  `string` The URL of the workload policy that is specified for this managed instance group. It can be a full or partial URL. For example, the following are all valid URLs to a workload policy: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/regions/region/resourcePolicies/resourcePolicy`
  * `projects/project/regions/region/resourcePolicies/resourcePolicy`
  * `regions/region/resourcePolicies/resourcePolicy`

  
  
### Response body

Represents an Operation resource.

Google Compute Engine has three Operation resources:

  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations)
  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations)



You can use an operation resource to manage asynchronous API requests. For more information, read [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses).

Operations can be global, regional or zonal. 

  * For global operations, use the `globalOperations` resource.
  * For regional operations, use the `regionOperations` resource.
  * For zonal operations, use the `zoneOperations` resource.



For more information, read [ Global, Regional, and Zonal Resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

Note that completed Operation resources have a limited [ retention period.](https://cloud.google.com/compute/docs/instances/viewing-compute-operations#operation-retention-period)

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
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
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#operation` for Operation resources.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the operation. This identifier is defined by the server.  
`creationTimestamp` |  `string` [Deprecated] This field is deprecated.  
`name` |  `string` Output only. Name of the operation.  
`zone` |  `string` Output only. The URL of the zone where the operation resides. Only applicable when performing per-zone operations.  
`clientOperationId` |  `string` Output only. The value of `requestId` if you provided it in the request. Not present otherwise.  
`operationType` |  `string` Output only. The type of operation, such as `insert`, `update`, or `delete`, and so on.  
`targetLink` |  `string` Output only. The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the disk that the snapshot was created from.  
`targetId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique target ID, which identifies a specific incarnation of the target resource.  
`status` |  `enum` Output only. The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`.  
`statusMessage` |  `string` Output only. An optional textual description of the current status of the operation.  
`user` |  `string` Output only. User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`.  
`progress` |  `integer` Output only. An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses.  
`insertTime` |  `string` Output only. The time that this operation was requested. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`startTime` |  `string` Output only. The time that this operation was started by the server. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`endTime` |  `string` Output only. The time that this operation was completed. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`error` |  `object` Output only. If errors are generated during processing of the operation, this field will be populated.  
`error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`warnings[]` |  `object` Output only. If warning messages are generated during processing of the operation, this field will be populated.  
`warnings[].code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warnings[].message` |  `string` Output only. A human-readable description of the warning code.  
`warnings[].data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warnings[].data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warnings[].data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`httpErrorStatusCode` |  `integer` Output only. If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found.  
`httpErrorMessage` |  `string` Output only. If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`region` |  `string` Output only. The URL of the region where the operation resides. Only applicable when performing regional operations.  
`description` |  `string` Output only. A textual description of the operation, which is set when the operation is created.  
`operationGroupId` |  `string` Output only. An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request.  
Output only. Service-specific metadata attached to this operation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`setCommonInstanceMetadataOperationMetadata` |  `object` Output only. If the operation is for projects.setCommonInstanceMetadata, this field will contain information on all underlying zonal actions and their state.  
`setCommonInstanceMetadataOperationMetadata.clientOperationId` |  `string` Output only. The client operation id.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[]` |  `map (key: string, value: object)` Output only. Status information per location (location name is key). Example key: zones/us-central1-a  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].state` |  `enum` Output only. Status of the action, which can be one of the following: `PROPAGATING`, `PROPAGATED`, `ABANDONED`, `FAILED`, or `DONE`.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error` |  `object` Output only. If state is `ABANDONED` or `FAILED`, this field is populated.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`instancesBulkInsertOperationMetadata` |  `object`  
`instancesBulkInsertOperationMetadata.perLocationStatus[]` |  `map (key: string, value: object)` Status information per location (location name is key). Example key: zones/us-central1-a  
`instancesBulkInsertOperationMetadata.perLocationStatus[].status` |  `enum` Output only. Creation status of BulkInsert operation - information if the flow is rolling forward or rolling back.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].targetVmCount` |  `integer` Output only. Count of VMs originally planned to be created.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].createdVmCount` |  `integer` Output only. Count of VMs successfully created so far.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].failedToCreateVmCount` |  `integer` Output only. Count of VMs that started creating but encountered an error.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].deletedVmCount` |  `integer` Output only. Count of VMs that got deleted during rollback.  
`getVersionOperationMetadata` |  `object`  
`getVersionOperationMetadata.inlineSbomInfo` |  `object`  
`getVersionOperationMetadata.inlineSbomInfo.currentComponentVersions` |  `map (key: string, value: string)` A mapping of components to their currently-applied versions or other appropriate identifiers.  
`getVersionOperationMetadata.inlineSbomInfo.targetComponentVersions` |  `map (key: string, value: string)` A mapping of components to their target versions or other appropriate identifiers.  
`getHealthOperationMetadata` |  `object` Output only. Metadata for GetHealth operations.  
`getHealthOperationMetadata.healthInfo` |  `object` Output only. The health information.  
`getHealthOperationMetadata.healthInfo.healthStatus` |  `enum` Output only. The health status.  
`getHealthOperationMetadata.healthInfo.unhealthyReason` |  `enum` Output only. The reason for unhealthy status.  
`getHealthOperationMetadata.healthInfo.repairCategory` |  `enum` Output only. The repair category.  
`getHealthOperationMetadata.healthInfo.availabilitySloStatus` |  `enum` Output only. The availability SLO status.  
`getHealthOperationMetadata.healthInfo.updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when health info was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.disks.create`
  * `compute.images.useReadOnly`
  * `compute.instanceGroupManagers.create`
  * `compute.instances.create`
  * `compute.instances.setMetadata`
  * `compute.subnetworks.use`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
