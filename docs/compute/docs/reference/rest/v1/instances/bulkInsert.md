---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert/
title: Method: instances.bulkInsert \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:33.778852+00:00
---

# Method: instances.bulkInsert  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: instances.bulkInsert Stay organized with collections  Save and categorize content based on your preferences. 

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



Creates multiple instances. Count specifies the number of instances to create. For more information, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation).

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances/bulkInsert`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` The name of the zone for this request.  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`).  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "count": string,
      "minCount": string,
      "namePattern": string,
      "perInstanceProperties": {
        string: {
          "name": string,
          "hostname": string
        },
        ...
      },
      "sourceInstanceTemplate": string,
      "instanceProperties": {
        "description": string,
        "tags": {
          "items": [
            string
          ],
          "fingerprint": string
        },
        "resourceManagerTags": {
          string: string,
          ...
        },
        "machineType": string,
        "canIpForward": boolean,
        "networkInterfaces": [
          {
            "kind": string,
            "network": string,
            "subnetwork": string,
            "networkIP": string,
            "ipv6Address": string,
            "internalIpv6PrefixLength": integer,
            "name": string,
            "accessConfigs": [
              {
                "kind": string,
                "type": enum,
                "name": string,
                "natIP": string,
                "externalIpv6": string,
                "externalIpv6PrefixLength": integer,
                "setPublicPtr": boolean,
                "publicPtrDomainName": string,
                "networkTier": enum,
                "securityPolicy": string
              }
            ],
            "ipv6AccessConfigs": [
              {
                "kind": string,
                "type": enum,
                "name": string,
                "natIP": string,
                "externalIpv6": string,
                "externalIpv6PrefixLength": integer,
                "setPublicPtr": boolean,
                "publicPtrDomainName": string,
                "networkTier": enum,
                "securityPolicy": string
              }
            ],
            "aliasIpRanges": [
              {
                "ipCidrRange": string,
                "subnetworkRangeName": string
              }
            ],
            "aliasIpv6Ranges": [
              {
                "ipCidrRange": string,
                "subnetworkRangeName": string
              }
            ],
            "fingerprint": string,
            "stackType": enum,
            "ipv6AccessType": enum,
            "queueCount": integer,
            "nicType": enum,
            "networkAttachment": string,
            "parentNicName": string,
            "vlan": integer,
            "igmpQuery": enum,
            "serviceClassId": string,
            "enableVpcScopedDns": boolean
          }
        ],
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
        ],
        "metadata": {
          "kind": string,
          "fingerprint": string,
          "items": [
            {
              "key": string,
              "value": string
            }
          ]
        },
        "serviceAccounts": [
          {
            "email": string,
            "scopes": [
              string
            ]
          }
        ],
        "scheduling": {
          "onHostMaintenance": enum,
          "automaticRestart": boolean,
          "preemptible": boolean,
          "nodeAffinities": [
            {
              "key": string,
              "operator": enum,
              "values": [
                string
              ]
            }
          ],
          "minNodeCpus": integer,
          "locationHint": string,
          "availabilityDomain": integer,
          "provisioningModel": enum,
          "instanceTerminationAction": enum,
          "hostErrorTimeoutSeconds": integer,
          "gracefulShutdown": {
            "enabled": boolean,
            "maxDuration": {
              "seconds": string,
              "nanos": integer
            }
          },
          "localSsdRecoveryTimeout": {
            "seconds": string,
            "nanos": integer
          },
          "skipGuestOsShutdown": boolean,
          "preemptionNoticeDuration": {
            "seconds": string,
            "nanos": integer
          },
          "exposeHostTopology": boolean,
          "protectionTier": enum,
    
          // The following is a list of mutually exclusive fields. At most one of the
          // fields will be set in a response:
          "maxRunDuration": {
            "seconds": string,
            "nanos": integer
          },
          "terminationTime": string
          // End of mutually exclusive fields.,
    
          // The following is a list of mutually exclusive fields. At most one of the
          // fields will be set in a response:
          "onInstanceStopAction": {
            "discardLocalSsd": boolean
          }
          // End of mutually exclusive fields.
        },
        "labels": {
          string: string,
          ...
        },
        "guestAccelerators": [
          {
            "acceleratorType": string,
            "acceleratorCount": integer
          }
        ],
        "minCpuPlatform": string,
        "reservationAffinity": {
          "consumeReservationType": enum,
          "key": string,
          "values": [
            string
          ]
        },
        "shieldedInstanceConfig": {
          "enableSecureBoot": boolean,
          "enableVtpm": boolean,
          "enableIntegrityMonitoring": boolean
        },
        "resourcePolicies": [
          string
        ],
        "confidentialInstanceConfig": {
          "enableConfidentialCompute": boolean,
          "confidentialInstanceType": enum
        },
        "privateIpv6GoogleAccess": enum,
        "advancedMachineFeatures": {
          "enableNestedVirtualization": boolean,
          "threadsPerCore": integer,
          "visibleCoreCount": integer,
          "enableUefiNetworking": boolean,
          "performanceMonitoringUnit": enum,
          "turboMode": string
        },
        "networkPerformanceConfig": {
          "totalEgressBandwidthTier": enum
        },
        "keyRevocationActionType": enum,
        "localSsdEncryptionMode": enum,
        "workloadIdentityConfig": {
          "identity": string,
          "identityCertificateEnabled": boolean
        }
      },
      "locationPolicy": {
        "locations": {
          string: {
            "preference": enum,
            "constraints": {
              "maxCount": integer
            }
          },
          ...
        },
        "targetShape": enum,
        "zones": [
          {
            "zone": string
          }
        ]
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          string: {
            "machineTypes": [
              string
            ],
            "rank": string,
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
            ],
            "minCpuPlatform": string
          },
          ...
        }
      }
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of instances to create.  
`minCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The minimum number of instances to create. If no `minCount` is specified then `count` is used as the default value. If `minCount` instances cannot be created, then no instances will be created and instances already created will be deleted.  
`namePattern` |  `string` The string pattern used for the names of the VMs. Either `namePattern` or `perInstanceProperties` must be set. The pattern must contain one continuous sequence of placeholder hash characters (#) with each character corresponding to one digit of the generated instance name. Example: a `namePattern` of `inst-####` generates instance names such as `inst-0001` and `inst-0002`. If existing instances in the same project and zone have names that match the name pattern then the generated instance numbers start after the biggest existing number. For example, if there exists an instance with name `inst-0050`, then instance names generated using the pattern `inst-####` begin with `inst-0051`. The name pattern placeholder `#...#` can contain up to 18 characters.  
`perInstanceProperties[]` |  `map (key: string, value: object)` Per-instance properties to be set on individual instances. Keys of this map specify requested instance names. Can be empty if `namePattern` is used.  
`perInstanceProperties[].name` |  `string` Output only. This field is only temporary. It will be removed. Do not use it.  
`perInstanceProperties[].hostname` |  `string` Specifies the hostname of the instance. More details in: <https://cloud.google.com/compute/docs/instances/custom-hostname-vm#naming_convention>  
`sourceInstanceTemplate` |  `string` Specifies the instance template from which to create instances. You may combine `sourceInstanceTemplate` with `instanceProperties` to override specific values from an existing instance template. Bulk API follows the semantics of JSON Merge Patch [described by RFC 7396](https://www.ietf.org/rfc/rfc7396.txt).It can be a full or partial URL. For example, the following are all valid URLs to an instance template: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/instanceTemplates/instanceTemplate`
  * `projects/project/global/instanceTemplates/instanceTemplate`
  * `global/instanceTemplates/instanceTemplate`

This field is optional. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sourceInstanceTemplate`:

  * `compute.instanceTemplates.useReadOnly`

  
`instanceProperties` |  `object` The instance properties defining the VM instances to be created. Required if `sourceInstanceTemplate` is not provided.  
`instanceProperties.description` |  `string` An optional text description for the instances that are created from these properties.  
`instanceProperties.tags` |  `object` A list of tags to apply to the instances that are created from these properties. The tags identify valid sources or targets for network firewalls. The setTags method can modify this list of tags. Each tag within the list must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `tags`:

  * `compute.instances.setTags`

  
`instanceProperties.tags.items[]` |  `string` An array of tags. Each tag must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`instanceProperties.tags.fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Specifies a fingerprint for this request, which is essentially a hash of the tags' contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update tags. You must always provide an up-to-date fingerprint hash in order to update or change tags.To see the latest fingerprint, make `get()` request to the instance.A base64-encoded string.  
`instanceProperties.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the instance. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`instanceProperties.machineType` |  `string` The machine type to use for instances that are created from these properties. This field only accepts a machine type name, for example `n2-standard-4`. If you use the machine type full or partial URL, for example `projects/my-l7ilb-project/zones/us-central1-a/machineTypes/n2-standard-4`, the request will result in an `INTERNAL_ERROR`.  
`instanceProperties.canIpForward` |  `boolean` Enables instances created based on these properties to send packets with source IP addresses other than their own and receive packets with destination IP addresses other than their own. If these instances will be used as an IP gateway or it will be set as the next-hop in a Route resource, specify `true`. If unsure, leave this set to `false`. See the [Enable IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) documentation for more information.  
`instanceProperties.networkInterfaces[]` |  `object` An array of network access configurations for this interface.  
`instanceProperties.networkInterfaces[].kind` |  `string` Output only. Type of the resource. Always `compute#networkInterface` for network interfaces.  
`instanceProperties.networkInterfaces[].network` |  `string` URL of the VPC network resource for this instance. When creating an instance, if neither the network nor the subnetwork is specified, the default network `global/networks/default` is used. If the selected project doesn't have the default network, you must specify a network or subnet. If the network is not specified but the subnetwork is specified, the network is inferred.If you specify this property, you can specify the network as a full or partial URL. For example, the following are all valid URLs: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/networks/network`
  * `projects/project/global/networks/network`
  * `global/networks/default`

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `network`:

  * `compute.networks.use`
  * `compute.networks.useExternalIp`

  
`instanceProperties.networkInterfaces[].subnetwork` |  `string` The URL of the Subnetwork resource for this instance. If the network resource is in [legacy](https://docs.cloud.google.com/vpc/docs/legacy) mode, do not specify this field. If the network is in auto subnet mode, specifying the subnetwork is optional. If the network is in custom subnet mode, specifying the subnetwork is required. If you specify this field, you can specify the subnetwork as a full or partial URL. For example, the following are all valid URLs: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/regions/region/subnetworks/subnetwork`
  * `regions/region/subnetworks/subnetwork`

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `subnetwork`:

  * `compute.subnetworks.use`
  * `compute.subnetworks.useExternalIp`

  
`instanceProperties.networkInterfaces[].networkIP` |  `string` An IPv4 internal IP address to assign to the instance for this network interface. If not specified by the user, an unused internal IP is assigned by the system.  
`instanceProperties.networkInterfaces[].ipv6Address` |  `string` An IPv6 internal network address for this network interface. To use a static internal IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an internal IPv6 address from the instance's subnetwork.  
`instanceProperties.networkInterfaces[].internalIpv6PrefixLength` |  `integer` The prefix length of the primary internal IPv6 range.  
`instanceProperties.networkInterfaces[].name` |  `string` Output only. The name of the network interface, which is generated by the server. For a VM, the network interface uses the `nicN` naming format. Where `N` is a value between `0` and `7`. The default interface value is `nic0`.  
`instanceProperties.networkInterfaces[].accessConfigs[]` |  `object` An array of configurations for this interface. Currently, only one access config, `ONE_TO_ONE_NAT`, is supported. If there are no `accessConfigs` specified, then this instance will have no external internet access.  
`instanceProperties.networkInterfaces[].accessConfigs[].kind` |  `string` Output only. Type of the resource. Always `compute#accessConfig` for access configs.  
`instanceProperties.networkInterfaces[].accessConfigs[].type` |  `enum` The type of configuration. In `accessConfigs` (IPv4), the default and only option is `ONE_TO_ONE_NAT`. In `ipv6AccessConfigs`, the default and only option is `DIRECT_IPV6`.  
`instanceProperties.networkInterfaces[].accessConfigs[].name` |  `string` The name of this access configuration. In `accessConfigs` (IPv4), the default and recommended name is `External NAT`, but you can use any arbitrary string, such as `My external IP` or `Network Access`. In `ipv6AccessConfigs`, the recommend name is `External IPv6`.  
`instanceProperties.networkInterfaces[].accessConfigs[].natIP` |  `string` Applies to `accessConfigs` (IPv4) only. An [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) associated with this instance. Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `natIP`:

  * `compute.addresses.use`

  
`instanceProperties.networkInterfaces[].accessConfigs[].externalIpv6` |  `string` Applies to `ipv6AccessConfigs` only. The first IPv6 address of the external IPv6 range associated with this instance, prefix length is stored in `externalIpv6PrefixLength` in `ipv6AccessConfig`. To use a static external IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an external IPv6 address from the instance's subnetwork.  
`instanceProperties.networkInterfaces[].accessConfigs[].externalIpv6PrefixLength` |  `integer` Applies to `ipv6AccessConfigs` only. The prefix length of the external IPv6 range.  
`instanceProperties.networkInterfaces[].accessConfigs[].setPublicPtr` |  `boolean` Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.This field is not used in `ipv6AccessConfig`. A default PTR record will be created if the VM has external IPv6 range associated.  
`instanceProperties.networkInterfaces[].accessConfigs[].publicPtrDomainName` |  `string` The DNS domain name for the public PTR record.You can set this field only if the `setPublicPtr` field is enabled in `accessConfig`. If this field is unspecified in `ipv6AccessConfig`, a default PTR record will be created for first IP in associated external IPv6 range.  
`instanceProperties.networkInterfaces[].accessConfigs[].networkTier` |  `enum` This signifies the networking tier used for configuring this access configuration and can only take the following values: `PREMIUM`, `STANDARD`.If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier.If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP.  
`instanceProperties.networkInterfaces[].accessConfigs[].securityPolicy` |  `string` The resource URL for the security policy associated with this access config.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[]` |  `object` An array of IPv6 access configurations for this interface. Currently, only one IPv6 access config, `DIRECT_IPV6`, is supported. If there is no `ipv6AccessConfig` specified, then this instance will have no external IPv6 Internet access.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].kind` |  `string` Output only. Type of the resource. Always `compute#accessConfig` for access configs.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].type` |  `enum` The type of configuration. In `accessConfigs` (IPv4), the default and only option is `ONE_TO_ONE_NAT`. In `ipv6AccessConfigs`, the default and only option is `DIRECT_IPV6`.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].name` |  `string` The name of this access configuration. In `accessConfigs` (IPv4), the default and recommended name is `External NAT`, but you can use any arbitrary string, such as `My external IP` or `Network Access`. In `ipv6AccessConfigs`, the recommend name is `External IPv6`.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].natIP` |  `string` Applies to `accessConfigs` (IPv4) only. An [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) associated with this instance. Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `natIP`:

  * `compute.addresses.use`

  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].externalIpv6` |  `string` Applies to `ipv6AccessConfigs` only. The first IPv6 address of the external IPv6 range associated with this instance, prefix length is stored in `externalIpv6PrefixLength` in `ipv6AccessConfig`. To use a static external IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an external IPv6 address from the instance's subnetwork.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].externalIpv6PrefixLength` |  `integer` Applies to `ipv6AccessConfigs` only. The prefix length of the external IPv6 range.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].setPublicPtr` |  `boolean` Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.This field is not used in `ipv6AccessConfig`. A default PTR record will be created if the VM has external IPv6 range associated.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].publicPtrDomainName` |  `string` The DNS domain name for the public PTR record.You can set this field only if the `setPublicPtr` field is enabled in `accessConfig`. If this field is unspecified in `ipv6AccessConfig`, a default PTR record will be created for first IP in associated external IPv6 range.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].networkTier` |  `enum` This signifies the networking tier used for configuring this access configuration and can only take the following values: `PREMIUM`, `STANDARD`.If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier.If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP.  
`instanceProperties.networkInterfaces[].ipv6AccessConfigs[].securityPolicy` |  `string` The resource URL for the security policy associated with this access config.  
`instanceProperties.networkInterfaces[].aliasIpRanges[]` |  `object` An array of alias IP ranges for this network interface. You can only specify this field for network interfaces in VPC networks.  
`instanceProperties.networkInterfaces[].aliasIpRanges[].ipCidrRange` |  `string` The IP alias ranges to allocate for this interface. This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. This range may be a single IP address (such as `10.2.3.4`), a netmask (such as `/24`) or a CIDR-formatted string (such as `10.1.2.0/24`).  
`instanceProperties.networkInterfaces[].aliasIpRanges[].subnetworkRangeName` |  `string` The name of a subnetwork secondary IP range from which to allocate an IP alias range. If not specified, the primary range of the subnetwork is used.  
`instanceProperties.networkInterfaces[].aliasIpv6Ranges[]` |  `object` An array of alias IPv6 ranges for this network interface. You can only specify this field for network interfaces in VPC networks.  
`instanceProperties.networkInterfaces[].aliasIpv6Ranges[].ipCidrRange` |  `string` The IP alias ranges to allocate for this interface. This IP CIDR range must belong to the specified subnetwork and cannot contain IP addresses reserved by system or used by other network interfaces. This range may be a single IP address (such as `10.2.3.4`), a netmask (such as `/24`) or a CIDR-formatted string (such as `10.1.2.0/24`).  
`instanceProperties.networkInterfaces[].aliasIpv6Ranges[].subnetworkRangeName` |  `string` The name of a subnetwork secondary IP range from which to allocate an IP alias range. If not specified, the primary range of the subnetwork is used.  
`instanceProperties.networkInterfaces[].fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint hash of contents stored in this network interface. This field will be ignored when inserting an `Instance` or adding a `NetworkInterface`. An up-to-date fingerprint must be provided in order to update the `NetworkInterface`. The request will fail with error `400 Bad Request` if the fingerprint is not provided, or `412 Precondition Failed` if the fingerprint is out of date.A base64-encoded string.  
`instanceProperties.networkInterfaces[].stackType` |  `enum` The stack type for this network interface. To assign only IPv4 addresses, use IPV4_ONLY. To assign both IPv4 and IPv6 addresses, use `IPV4_IPV6`. If not specified, `IPV4_ONLY` is used.This field can be both set at instance creation and update network interface operations.  
`instanceProperties.networkInterfaces[].ipv6AccessType` |  `enum` Output only. One of EXTERNAL, INTERNAL to indicate whether the IP can be accessed from the Internet. This field is always inherited from its subnetwork.Valid only if `stackType` is `IPV4_IPV6`.  
`instanceProperties.networkInterfaces[].queueCount` |  `integer` The networking queue count that's specified by users for the network interface. Both Rx and Tx queues will be set to this number. It'll be empty if not specified by the users.  
`instanceProperties.networkInterfaces[].nicType` |  `enum` The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.  
`instanceProperties.networkInterfaces[].networkAttachment` |  `string` The URL of the network attachment that this interface should connect to in the following format: projects/{projectNumber}/regions/{region_name}/networkAttachments/{network_attachment_name}.  
`instanceProperties.networkInterfaces[].parentNicName` |  `string` Name of the parent network interface of a dynamic network interface.  
`instanceProperties.networkInterfaces[].vlan` |  `integer` VLAN tag of a dynamic network interface, must be an integer in the range from 2 to 255 inclusively.  
`instanceProperties.networkInterfaces[].igmpQuery` |  `enum` Indicate whether igmp query is enabled on the network interface or not. If enabled, also indicates the version of IGMP supported.  
`instanceProperties.networkInterfaces[].serviceClassId` |  `string` Optional. Producer Service's Service class Id for the region of this network interface. Can only be used with networkAttachment. It is not possible to use on its own however, networkAttachment can be used without serviceClassId.  
`instanceProperties.networkInterfaces[].enableVpcScopedDns` |  `boolean` Optional. If true, DNS resolution will be enabled over this interface. Only valid with networkAttachment.  
`instanceProperties.disks[]` |  `object` An array of disks that are associated with the instances that are created from these properties.  
`instanceProperties.disks[].kind` |  `string` Output only. Type of the resource. Always `compute#attachedDisk` for attached disks.  
`instanceProperties.disks[].type` |  `enum` Specifies the type of the disk, either `SCRATCH` or `PERSISTENT`. If not specified, the default is `PERSISTENT`.  
`instanceProperties.disks[].mode` |  `enum` The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.  
`instanceProperties.disks[].savedState` |  `enum` Output only. For LocalSSD disks on VM Instances in STOPPED or SUSPENDED state, this field is set to `PRESERVED` if the LocalSSD data has been saved to a persistent location by customer request. (see the discardLocalSsd option on instances.stop/instances.suspend). Read-only in the api.  
`instanceProperties.disks[].source` |  `string` Specifies a valid partial or full URL to an existing Persistent Disk resource. When creating a new instance boot disk, one of `initializeParams.sourceImage` or `initializeParams.sourceSnapshot` or `disks.source` is required.If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.Note that for InstanceTemplate, specify the disk name for zonal disk, and the URL for regional disk. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `source`:

  * `compute.disks.use`
  * `compute.disks.useReadOnly`

  
`instanceProperties.disks[].deviceName` |  `string` Specifies a unique device name of your choice that is reflected into the `/dev/disk/by-id/google-*` tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.If not specified, the server chooses a default device name to apply to this disk, in the form `persistent-disk-x`, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks.  
`instanceProperties.disks[].index` |  `integer` Output only. A zero-based index to this disk, where 0 is reserved for the boot disk. If you have many disks attached to an instance, each disk would have a unique index number.  
`instanceProperties.disks[].boot` |  `boolean` Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.  
`instanceProperties.disks[].initializeParams` |  `object` [Input Only] Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.This property is mutually exclusive with the `source` property; you can only define one or the other, but not both.  
`instanceProperties.disks[].initializeParams.diskName` |  `string` Specifies the disk name. If not specified, the default is to use the name of the instance. If a disk with the same name already exists in the given region, the existing disk is attached to the new instance and the new disk is not created.  
`instanceProperties.disks[].initializeParams.sourceImage` |  `string` The source image to create this disk. When creating a new instance boot disk, one of `initializeParams.sourceImage` or `initializeParams.sourceSnapshot` or `disks.source` is required.To create a disk with one of the [public operating system images](https://docs.cloud.google.com/compute/docs/images/os-details), specify the image by its family name. For example, specify `family/debian-9` to use the latest Debian 9 image: `projects/debian-cloud/global/images/family/debian-9`Alternatively, use a specific version of a public operating system image: `projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD`To create a disk with a custom image that you created, specify the image name in the following format: `global/images/my-custom-image`You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with `family/family-name`: `global/images/family/my-image-family`If the source image is deleted later, this field will not be set. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sourceImage`:

  * `compute.images.useReadOnly`

  
`instanceProperties.disks[].initializeParams.diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB. The size must be at least 10 GB. If you specify a `sourceImage`, which is required for boot disks, the default size is the size of the `sourceImage`. If you do not specify a `sourceImage`, the default disk size is 500 GB.  
`instanceProperties.disks[].initializeParams.diskType` |  `string` Specifies the disk type used for the boot disk or an additional data disk. For valid disk type values, see [ Supported types for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk#hd_disk_types) and [ Persistent Disk type variables](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#hd_disk_types).When creating a single instance, you must provide either the full or partial URL of the disk type. For example, the following values are valid: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/diskTypes/diskType`
  * `projects/project/zones/zone/diskTypes/diskType`
  * `zones/zone/diskTypes/diskType`

When creating an instance template, instance flexibility policy, or when creating or updating an all-instances configuration, you specify the disk type without a URL, for example, `hyperdisk-balanced`.If you omit this field for a disk, the default disk type depends on the instance's machine series, as follows. 

  * For first- and second-generation machine series like N1, N2, T2, and M1, the default disk type is Standard Persistent Disk (`pd-standard`).
  * For C3, C3D, and M3 the default is Balanced Persistent Disk (`pd-balanced`).
  * For other third-generation machine series like A3, H3, Z3, all fourth-generation types like C4, N4, M4, and newer machine series, the default is Hyperdisk Balanced (`hyperdisk-balanced`).

The disk type you specify must be compatible with the instance's machine series. For a list of machine series that support Persistent Disk, see [Machine series support for Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#pd-machine-series).For a list of machine series that support Hyperdisk, see [Machine series support for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).  
`instanceProperties.disks[].initializeParams.sourceImageEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source image. Required if the source image is protected by a customer-supplied encryption key.InstanceTemplate and InstancePropertiesPatch do not store [customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), so you cannot create disks for instances in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) if the source images are encrypted with your own keys.  
`instanceProperties.disks[].initializeParams.sourceImageEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`instanceProperties.disks[].initializeParams.sourceImageEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`instanceProperties.disks[].initializeParams.sourceImageEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`instanceProperties.disks[].initializeParams.sourceImageEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`instanceProperties.disks[].initializeParams.sourceImageEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`instanceProperties.disks[].initializeParams.labels` |  `map (key: string, value: string)` Labels to apply to this disk. These can be later modified by the `disks.setLabels` method. This field is only applicable for persistent disks. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `labels`:

  * `compute.disks.setLabels`

  
`instanceProperties.disks[].initializeParams.sourceSnapshot` |  `string` The source snapshot to create this disk. When creating a new instance boot disk, one of `initializeParams.sourceSnapshot` or `initializeParams.sourceImage` or `disks.source` is required.To create a disk with a snapshot that you created, specify the snapshot name in the following format: `global/snapshots/my-backup`If the source snapshot is deleted later, this field will not be set.Note: You cannot create VMs in bulk using a snapshot as the source. Use an image instead when you create VMs using the [bulk insert method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sourceSnapshot`:

  * `compute.snapshots.useReadOnly`

  
`instanceProperties.disks[].initializeParams.sourceSnapshotEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source snapshot.  
`instanceProperties.disks[].initializeParams.sourceSnapshotEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`instanceProperties.disks[].initializeParams.sourceSnapshotEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`instanceProperties.disks[].initializeParams.sourceSnapshotEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`instanceProperties.disks[].initializeParams.sourceSnapshotEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`instanceProperties.disks[].initializeParams.sourceSnapshotEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`instanceProperties.disks[].initializeParams.description` |  `string` An optional description. Provide this property when creating the disk.  
`instanceProperties.disks[].initializeParams.replicaZones[]` |  `string` Required for each regional disk associated with the instance. Specify the URLs of the zones where the disk should be replicated to. You must provide exactly two replica zones, and one zone must be the same as the instance zone.  
`instanceProperties.disks[].initializeParams.resourcePolicies[]` |  `string` Resource policies applied to this disk for automatic snapshot creations. Specified using the full or partial URL. For instance template, specify only the resource policy name.  
`instanceProperties.disks[].initializeParams.onUpdateAction` |  `enum` Specifies which action to take on instance update with this disk. Default is to use the existing disk.  
`instanceProperties.disks[].initializeParams.provisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see the [Extreme persistent disk documentation](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk).  
`instanceProperties.disks[].initializeParams.licenses[]` |  `string` A list of publicly visible licenses. Reserved for Google's use.  
`instanceProperties.disks[].initializeParams.architecture` |  `enum` The architecture of the attached disk. Valid values are arm64 or x86_64.  
`instanceProperties.disks[].initializeParams.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the disk. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`instanceProperties.disks[].initializeParams.provisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must greater than or equal to 1.  
`instanceProperties.disks[].initializeParams.enableConfidentialCompute` |  `boolean` Whether this disk is using confidential compute mode.  
`instanceProperties.disks[].initializeParams.storagePool` |  `string` The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/storagePools/storagePool`
  * `projects/project/zones/zone/storagePools/storagePool`
  * `zones/zone/storagePools/storagePool`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `storagePool`:

  * `compute.storagePools.use`

  
`instanceProperties.disks[].autoDelete` |  `boolean` Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).  
`instanceProperties.disks[].licenses[]` |  `string` Output only. Any valid publicly visible licenses.  
`instanceProperties.disks[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. For most machine types, the default is `SCSI`. Local SSDs can use either NVME or SCSI. In certain configurations, persistent disks can use NVMe. For more information, see [About persistent disks](https://cloud.google.com/compute/docs/disks/persistent-disks).  
`instanceProperties.disks[].guestOsFeatures[]` |  `object` A list of features to enable on the guest operating system. Applicable only for bootable images. Read [ Enabling guest operating system features](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features) to see a list of available options.  
`instanceProperties.disks[].guestOsFeatures[].type` |  `enum` The ID of a supported feature. To add multiple values, use commas to separate values. Set to one or more of the following values: 

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
`instanceProperties.disks[].diskEncryptionKey` |  `object` Encrypts or decrypts a disk using a [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption).If you are creating a new disk, this field encrypts the new disk using an encryption key that you provide. If you are attaching an existing disk that is already encrypted, this field decrypts the disk using the customer-supplied encryption key.If you encrypt a disk using a customer-supplied key, you must provide the same key again when you attempt to use this resource at a later time. For example, you must provide the key when you create a snapshot or an image from the disk or when you attach the disk to a virtual machine instance.If you do not provide an encryption key, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later.Note:Instance templates do not store [customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), so you cannot use your own keys to encrypt disks in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups).You cannot create VMs that have disks with customer-supplied keys using the [bulk insert method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).  
`instanceProperties.disks[].diskEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`instanceProperties.disks[].diskEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`instanceProperties.disks[].diskEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`instanceProperties.disks[].diskEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`instanceProperties.disks[].diskEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`instanceProperties.disks[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The size of the disk in GB.  
`instanceProperties.disks[].shieldedInstanceInitialState` |  `object` Output only. shielded vm initial state stored on disk  
`instanceProperties.disks[].shieldedInstanceInitialState.pk` |  `object` The Platform Key (PK).  
`instanceProperties.disks[].shieldedInstanceInitialState.pk.content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`instanceProperties.disks[].shieldedInstanceInitialState.pk.fileType` |  `enum` The file type of source file.  
`instanceProperties.disks[].shieldedInstanceInitialState.keks[]` |  `object` The Key Exchange Key (KEK).  
`instanceProperties.disks[].shieldedInstanceInitialState.keks[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`instanceProperties.disks[].shieldedInstanceInitialState.keks[].fileType` |  `enum` The file type of source file.  
`instanceProperties.disks[].shieldedInstanceInitialState.dbs[]` |  `object` The Key Database (db).  
`instanceProperties.disks[].shieldedInstanceInitialState.dbs[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`instanceProperties.disks[].shieldedInstanceInitialState.dbs[].fileType` |  `enum` The file type of source file.  
`instanceProperties.disks[].shieldedInstanceInitialState.dbxs[]` |  `object` The forbidden key database (dbx).  
`instanceProperties.disks[].shieldedInstanceInitialState.dbxs[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`instanceProperties.disks[].shieldedInstanceInitialState.dbxs[].fileType` |  `enum` The file type of source file.  
`instanceProperties.disks[].forceAttach` |  `boolean` [Input Only] Whether to force attach the regional disk even if it's currently attached to another instance. If you try to force attach a zonal disk to an instance, you will receive an error.  
`instanceProperties.disks[].architecture` |  `enum` Output only. The architecture of the attached disk. Valid values are ARM64 or X86_64.  
`instanceProperties.metadata` |  `object` The metadata key/value pairs to assign to instances that are created from these properties. These pairs can consist of custom metadata or predefined keys. See [Project and instance metadata](https://docs.cloud.google.com/compute/docs/metadata#project_and_instance_metadata) for more information. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `metadata`:

  * `compute.instances.setMetadata`

  
`instanceProperties.metadata.kind` |  `string` Output only. Type of the resource. Always `compute#metadata` for metadata.  
`instanceProperties.metadata.fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Specifies a fingerprint for this request, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve the resource.A base64-encoded string.  
`instanceProperties.metadata.items[]` |  `object` Array of key/value pairs. The total size of all keys and values must be less than 512 KB.  
`instanceProperties.metadata.items[].key` |  `string` Key for the metadata entry. Keys must conform to the following regexp: `[a-zA-Z0-9-_]+`, and be less than 128 bytes in length. This is reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project.  
`instanceProperties.metadata.items[].value` |  `string` Value for the metadata entry. These are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on values is that their size must be less than or equal to 262144 bytes (256 KiB).  
`instanceProperties.serviceAccounts[]` |  `object` A list of service accounts with specified scopes. Access tokens for these service accounts are available to the instances that are created from these properties. Use metadata queries to obtain the access tokens for these instances. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceAccounts`:

  * `compute.instances.setServiceAccount`

  
`instanceProperties.serviceAccounts[].email` |  `string` Email address of the service account. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `email`:

  * `iam.serviceAccounts.actAs`

  
`instanceProperties.serviceAccounts[].scopes[]` |  `string` The list of scopes to be made available for this service account.  
`instanceProperties.scheduling` |  `object` Specifies the scheduling options for the instances that are created from these properties.  
`instanceProperties.scheduling.maxRunDuration` |  `object` Specifies the max run duration for the given instance. If specified, the instance termination action will be performed at the end of the run duration.  
`instanceProperties.scheduling.maxRunDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`instanceProperties.scheduling.maxRunDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`instanceProperties.scheduling.terminationTime` |  `string` Specifies the timestamp, when the instance will be terminated, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. If specified, the instance termination action will be performed at the termination time.  
`instanceProperties.scheduling.onInstanceStopAction` |  `object`  
`instanceProperties.scheduling.onInstanceStopAction.discardLocalSsd` |  `boolean` If true, the contents of any attached Local SSD disks will be discarded else, the Local SSD data will be preserved when the instance is stopped at the end of the run duration/termination time.  
`instanceProperties.scheduling.onHostMaintenance` |  `enum` Defines the maintenance behavior for this instance. For standard instances, the default behavior is `MIGRATE`. For [preemptible instances](https://docs.cloud.google.com/compute/docs/instances/preemptible), the default and only possible behavior is `TERMINATE`. For more information, see [Set VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-options).  
`instanceProperties.scheduling.automaticRestart` |  `boolean` Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user). You can only set the automatic restart option for standard instances. [Preemptible instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) cannot be automatically restarted.By default, this is set to `true` so an instance is automatically restarted if it is terminated by Compute Engine.  
`instanceProperties.scheduling.preemptible` |  `boolean` Defines whether the instance is preemptible. This can only be set during instance creation or while the instance is [stopped](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) and therefore, in a `TERMINATED` state. See [Instance Life Cycle](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle) for more information on the possible instance states.  
`instanceProperties.scheduling.nodeAffinities[]` |  `object` A set of node affinity and anti-affinity configurations. Refer to [Configuring node affinity](https://docs.cloud.google.com/compute/docs/nodes/create-nodes#affinity) for more information. Overrides reservationAffinity.  
`instanceProperties.scheduling.nodeAffinities[].key` |  `string` Corresponds to the label key of Node resource.  
`instanceProperties.scheduling.nodeAffinities[].operator` |  `enum` Defines the operation of node selection. Valid operators are `IN` for affinity and `NOT_IN` for anti-affinity.  
`instanceProperties.scheduling.nodeAffinities[].values[]` |  `string` Corresponds to the label values of Node resource.  
`instanceProperties.scheduling.minNodeCpus` |  `integer` The minimum number of virtual CPUs this instance will consume when running on a sole-tenant node.  
`instanceProperties.scheduling.locationHint` |  `string` An opaque location hint used to place the instance close to other resources. This field is for use by internal tools that use the public API.  
`instanceProperties.scheduling.availabilityDomain` |  `integer` Specifies the availability domain to place the instance in. The value must be a number between 1 and the number of availability domains specified in the spread placement policy attached to the instance.  
`instanceProperties.scheduling.provisioningModel` |  `enum` Specifies the provisioning model of the instance.  
`instanceProperties.scheduling.instanceTerminationAction` |  `enum` Specifies the termination action for the instance.  
`instanceProperties.scheduling.hostErrorTimeoutSeconds` |  `integer` Specify the time in seconds for host error detection, the value must be within the range of [90, 330] with the increment of 30, if unset, the default behavior of host error recovery will be used.  
`instanceProperties.scheduling.gracefulShutdown` |  `object`  
`instanceProperties.scheduling.gracefulShutdown.enabled` |  `boolean` Opts-in for graceful shutdown.  
`instanceProperties.scheduling.gracefulShutdown.maxDuration` |  `object` The time allotted for the instance to gracefully shut down. If the graceful shutdown isn't complete after this time, then the instance transitions to the STOPPING state.  
`instanceProperties.scheduling.gracefulShutdown.maxDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`instanceProperties.scheduling.gracefulShutdown.maxDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`instanceProperties.scheduling.localSsdRecoveryTimeout` |  `object` Specifies the maximum amount of time a Local Ssd Vm should wait while recovery of the Local Ssd state is attempted. Its value should be in between 0 and 168 hours with hour granularity and the default value being 1 hour.  
`instanceProperties.scheduling.localSsdRecoveryTimeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`instanceProperties.scheduling.localSsdRecoveryTimeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`instanceProperties.scheduling.skipGuestOsShutdown` |  `boolean` Default is false and there will be 120 seconds between [GCE ACPI G2 Soft Off](https://en.wikipedia.org/wiki/ACPI#Power_states) and [ACPI G3 Mechanical Off](https://en.wikipedia.org/wiki/ACPI#Power_states) for Standard VMs and 30 seconds for Spot VMs.  
`instanceProperties.scheduling.preemptionNoticeDuration` |  `object` Specifies the Metadata Service preemption notice duration before the [GCE ACPI G2 Soft Off](https://en.wikipedia.org/wiki/ACPI#Power_states) signal is triggered for [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) only. If not specified, there will be no wait before the G2 Soft Off signal is triggered.  
`instanceProperties.scheduling.preemptionNoticeDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`instanceProperties.scheduling.preemptionNoticeDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`instanceProperties.scheduling.exposeHostTopology` |  `boolean` This optional flag exposes the hashed physical host ID in the ResourceStatus resource of the VM.  
`instanceProperties.scheduling.protectionTier` |  `enum` Protection tier for the workload which specifies the workload expectations in the event of infrastructure failures at data center (e.g. power and/or cooling failures).  
`instanceProperties.labels` |  `map (key: string, value: string)` Labels to apply to instances that are created from these properties. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `labels`:

  * `compute.instances.setLabels`

  
`instanceProperties.guestAccelerators[]` |  `object` A list of guest accelerator cards' type and count to use for instances created from these properties.  
`instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`instanceProperties.minCpuPlatform` |  `string` Minimum cpu/platform to be used by instances. The instance may be scheduled on the specified or newer cpu/platform. Applicable values are the friendly names of CPU platforms, such as `minCpuPlatform: "Intel Haswell"` or `minCpuPlatform: "Intel Sandy Bridge"`. For more information, read [Specifying a Minimum CPU Platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform).  
`instanceProperties.reservationAffinity` |  `object` Specifies the reservations that instances can consume from. Note that for MachineImage, this is not supported yet.  
`instanceProperties.reservationAffinity.consumeReservationType` |  `enum` Specifies the type of reservation from which this instance can consume resources: `ANY_RESERVATION` (default), `SPECIFIC_RESERVATION`, or `NO_RESERVATION`. See [ Consuming reserved instances](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources#consuming_reserved_instances) for examples.  
`instanceProperties.reservationAffinity.key` |  `string` Corresponds to the label key of a reservation resource. To target a `SPECIFIC_RESERVATION` by name, specify `googleapis.com/reservation-name` as the key and specify the name of your reservation as its value.  
`instanceProperties.reservationAffinity.values[]` |  `string` Corresponds to the label values of a reservation resource. This can be either a name to a reservation in the same project or "projects/different-project/reservations/some-reservation-name" to target a shared reservation in the same zone but in a different project.  
`instanceProperties.shieldedInstanceConfig` |  `object` Note that for MachineImage, this is not supported yet.  
`instanceProperties.shieldedInstanceConfig.enableSecureBoot` |  `boolean` Defines whether the instance has Secure Boot enabled. [Disabled by default](https://docs.cloud.google.com/compute/docs/instances/modifying-shielded-vm).  
`instanceProperties.shieldedInstanceConfig.enableVtpm` |  `boolean` Defines whether the instance has the vTPM enabled. [Enabled by default](https://docs.cloud.google.com/compute/docs/instances/modifying-shielded-vm).  
`instanceProperties.shieldedInstanceConfig.enableIntegrityMonitoring` |  `boolean` Defines whether the instance has integrity monitoring enabled. [Enabled by default](https://docs.cloud.google.com/compute/docs/instances/modifying-shielded-vm).  
`instanceProperties.resourcePolicies[]` |  `string` Resource policies (names, not URLs) applied to instances created from these properties. Note that for MachineImage, this is not supported yet. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `resourcePolicies`:

  * `compute.resourcePolicies.use`

  
`instanceProperties.confidentialInstanceConfig` |  `object` Specifies the Confidential Instance options. Note that for MachineImage, this is not supported yet.  
`instanceProperties.confidentialInstanceConfig.enableConfidentialCompute` |  `boolean` Defines whether the instance should have confidential compute enabled.  
`instanceProperties.confidentialInstanceConfig.confidentialInstanceType` |  `enum` Defines the type of technology used by the confidential instance.  
`instanceProperties.privateIpv6GoogleAccess` |  `enum` The private IPv6 google access type for VMs. If not specified, use ` INHERIT_FROM_SUBNETWORK` as default. Note that for MachineImage, this is not supported yet.  
`instanceProperties.advancedMachineFeatures` |  `object` Controls for advanced machine-related behavior features. Note that for MachineImage, this is not supported yet.  
`instanceProperties.advancedMachineFeatures.enableNestedVirtualization` |  `boolean` Whether to enable nested virtualization or not (default is false).  
`instanceProperties.advancedMachineFeatures.threadsPerCore` |  `integer` The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed.  
`instanceProperties.advancedMachineFeatures.visibleCoreCount` |  `integer` The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width.  
`instanceProperties.advancedMachineFeatures.enableUefiNetworking` |  `boolean` Whether to enable UEFI networking for instance creation.  
`instanceProperties.advancedMachineFeatures.performanceMonitoringUnit` |  `enum` Type of Performance Monitoring Unit requested on instance.  
`instanceProperties.advancedMachineFeatures.turboMode` |  `string` Turbo frequency mode to use for the instance. Supported modes include: * ALL_CORE_MAXUsing empty string or not setting this field will use the platform-specific default turbo mode.  
`instanceProperties.networkPerformanceConfig` |  `object` Note that for MachineImage, this is not supported yet.  
`instanceProperties.networkPerformanceConfig.totalEgressBandwidthTier` |  `enum`  
`instanceProperties.keyRevocationActionType` |  `enum` KeyRevocationActionType of the instance. Supported options are "STOP" and "NONE". The default value is "NONE" if it is not specified.  
`instanceProperties.localSsdEncryptionMode` |  `enum` Specifies which method should be used for encrypting the Local SSDs attached to the VM.  
`instanceProperties.workloadIdentityConfig` |  `object`  
`instanceProperties.workloadIdentityConfig.identity` |  `string`  
`instanceProperties.workloadIdentityConfig.identityCertificateEnabled` |  `boolean`  
`locationPolicy` |  `object` Policy for choosing target zone. For more information, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).  
`locationPolicy.locations[]` |  `map (key: string, value: object)` Location configurations mapped by location name. Currently only zone names are supported and must be represented as valid internal URLs, such as `zones/us-central1-a`. The bulkInsert operation doesn't create instances in an AI zone, even if an AI zone is available in the specified region. For example, if you set a DENY preference for us-central1-a, Compute Engine will consider us-central1-b and us-central1-c for instance creation, but not us-central1-ai1a. Also, you can't use the locations[] configuration to allow instance creation in an AI zone. To include an AI zone in bulkInsert operations, use the locationPolicy.zones[] field.  
`locationPolicy.locations[].preference` |  `enum` Preference for a given location. Set to either `ALLOW` or `DENY`.  
`locationPolicy.locations[].constraints` |  `object` Constraints that the caller requires on the result distribution in this zone.  
`locationPolicy.locations[].constraints.maxCount` |  `integer` Maximum number of items that are allowed to be placed in this zone. The value must be non-negative.  
`locationPolicy.targetShape` |  `enum` Strategy for distributing VMs across zones in a region.  
`locationPolicy.zones[]` |  `object` The bulkInsert operation applies any preferences set in the locations field to the specific zones listed in the zones field if the same zones are specified in both fields.  
`locationPolicy.zones[].zone` |  `string` The URL of the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available). The zone must exist in the region where the request is called. Zones must be represented as valid partial URLs, such as `zones/us-central1-a`.  
`instanceFlexibilityPolicy` |  `object` A flexible specification of machine type of instances to create.  
`instanceFlexibilityPolicy.instanceSelections[]` |  `map (key: string, value: object)` Specification of alternative, flexible instance subsets. One of them will be selected to create the instances based on various criteria, like: - ranks, - location policy, - current capacity, - available reservations (you can specify affinity in InstanceProperties), - SWAN/GOOSE limitations. Key is an arbitrary, unique RFC1035 string that identifies the instance selection.  
`instanceFlexibilityPolicy.instanceSelections[].machineTypes[]` |  `string` Alternative machine types to use for instances that are created from these properties. This field only accepts a machine type names, for example `n2-standard-4` and not URLs or partial URLs.  
`instanceFlexibilityPolicy.instanceSelections[].rank` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Rank when prioritizing the shape flexibilities. The instance selections with rank are considered first, in the ascending order of the rank. If not set, defaults to 0.  
`instanceFlexibilityPolicy.instanceSelections[].disks[]` |  `object` Disks to be attached to the instances created from in this selection. They override the disks specified in the instance properties.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].kind` |  `string` Output only. Type of the resource. Always `compute#attachedDisk` for attached disks.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].type` |  `enum` Specifies the type of the disk, either `SCRATCH` or `PERSISTENT`. If not specified, the default is `PERSISTENT`.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].mode` |  `enum` The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].savedState` |  `enum` Output only. For LocalSSD disks on VM Instances in STOPPED or SUSPENDED state, this field is set to `PRESERVED` if the LocalSSD data has been saved to a persistent location by customer request. (see the discardLocalSsd option on instances.stop/instances.suspend). Read-only in the api.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].source` |  `string` Specifies a valid partial or full URL to an existing Persistent Disk resource. When creating a new instance boot disk, one of `initializeParams.sourceImage` or `initializeParams.sourceSnapshot` or `disks.source` is required.If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.Note that for InstanceTemplate, specify the disk name for zonal disk, and the URL for regional disk. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `source`:

  * `compute.disks.use`
  * `compute.disks.useReadOnly`

  
`instanceFlexibilityPolicy.instanceSelections[].disks[].deviceName` |  `string` Specifies a unique device name of your choice that is reflected into the `/dev/disk/by-id/google-*` tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.If not specified, the server chooses a default device name to apply to this disk, in the form `persistent-disk-x`, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].index` |  `integer` Output only. A zero-based index to this disk, where 0 is reserved for the boot disk. If you have many disks attached to an instance, each disk would have a unique index number.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].boot` |  `boolean` Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams` |  `object` [Input Only] Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.This property is mutually exclusive with the `source` property; you can only define one or the other, but not both.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.diskName` |  `string` Specifies the disk name. If not specified, the default is to use the name of the instance. If a disk with the same name already exists in the given region, the existing disk is attached to the new instance and the new disk is not created.  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceImage` |  `string` The source image to create this disk. When creating a new instance boot disk, one of `initializeParams.sourceImage` or `initializeParams.sourceSnapshot` or `disks.source` is required.To create a disk with one of the [public operating system images](https://docs.cloud.google.com/compute/docs/images/os-details), specify the image by its family name. For example, specify `family/debian-9` to use the latest Debian 9 image: `projects/debian-cloud/global/images/family/debian-9`Alternatively, use a specific version of a public operating system image: `projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD`To create a disk with a custom image that you created, specify the image name in the following format: `global/images/my-custom-image`You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with `family/family-name`: `global/images/family/my-image-family`If the source image is deleted later, this field will not be set. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sourceImage`:

  * `compute.images.useReadOnly`

  
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
  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.labels` |  `map (key: string, value: string)` Labels to apply to this disk. These can be later modified by the `disks.setLabels` method. This field is only applicable for persistent disks. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `labels`:

  * `compute.disks.setLabels`

  
`instanceFlexibilityPolicy.instanceSelections[].disks[].initializeParams.sourceSnapshot` |  `string` The source snapshot to create this disk. When creating a new instance boot disk, one of `initializeParams.sourceSnapshot` or `initializeParams.sourceImage` or `disks.source` is required.To create a disk with a snapshot that you created, specify the snapshot name in the following format: `global/snapshots/my-backup`If the source snapshot is deleted later, this field will not be set.Note: You cannot create VMs in bulk using a snapshot as the source. Use an image instead when you create VMs using the [bulk insert method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sourceSnapshot`:

  * `compute.snapshots.useReadOnly`

  
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

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `storagePool`:

  * `compute.storagePools.use`

  
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
`instanceFlexibilityPolicy.instanceSelections[].minCpuPlatform` |  `string` Name of the minimum CPU platform to be used by this instance selection. e.g. 'Intel Ice Lake'.  
  
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
`instancesBulkInsertOperationMetadata.perLocationStatus[].status` |  `enum` Output only. Creation status of instances.bulkInsert operation - information if the flow is rolling forward or rolling back.  
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
  * `compute.instances.create`
  * `compute.instances.pscInterfaceCreate`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
