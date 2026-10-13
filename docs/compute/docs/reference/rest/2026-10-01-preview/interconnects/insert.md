---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/insert/
title: Method: interconnects.insert \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:15.571985+00:00
---

# Method: interconnects.insert  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: interconnects.insert Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
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



API Version : 2026-10-01-preview

Creates an Interconnect in the specified project using the data included in the request.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/global/interconnects?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
  
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
      "description": string,
      "selfLink": string,
      "selfLinkWithId": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "location": string,
      "subzone": enum,
      "linkType": enum,
      "requestedLinkCount": integer,
      "interconnectType": enum,
      "adminEnabled": boolean,
      "nocContactEmail": string,
      "customerName": string,
      "operationalStatus": enum,
      "provisionedLinkCount": integer,
      "interconnectAttachments": [
        string
      ],
      "peerIpAddress": string,
      "googleIpAddress": string,
      "googleReferenceId": string,
      "expectedOutages": [
        {
          "name": string,
          "description": string,
          "source": enum,
          "state": enum,
          "issueType": enum,
          "affectedCircuits": [
            string
          ],
          "startTime": string,
          "endTime": string
        }
      ],
      "circuitInfos": [
        {
          "googleCircuitId": string,
          "googleDemarcId": string,
          "customerDemarcId": string
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "labelFingerprint": string,
      "state": enum,
      "satisfiesPzs": boolean,
      "macsec": {
        "preSharedKeys": [
          {
            "name": string,
            "startTime": string
          }
        ],
        "failOpen": boolean
      },
      "macsecEnabled": boolean,
      "remoteLocation": string,
      "requestedFeatures": [
        enum
      ],
      "availableFeatures": [
        enum
      ],
      "applicationAwareInterconnect": {
        "strictPriorityPolicy": ,
        "bandwidthPercentagePolicy": {
          "bandwidthPercentages": [
            {
              "trafficClass": enum,
              "percentage": integer
            }
          ]
        },
        "profileDescription": string,
        "shapeAveragePercentages": [
          {
            "trafficClass": enum,
            "percentage": integer
          }
        ]
      },
      "aaiEnabled": boolean,
      "interconnectGroups": [
        string
      ],
      "wireGroups": [
        string
      ],
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      },
      "effectiveLocation": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#interconnect` for interconnects.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` [REQUIRED] Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`location` |  `string` URL of the InterconnectLocation object that represents where this connection is to be provisioned.  
`subzone` |  `enum` To be deprecated.  
`linkType` |  `enum` Type of link requested, which can take one of the following values: 

  * LINK_TYPE_ETHERNET_10G_LR: A 10G Ethernet with LR optics
  * LINK_TYPE_ETHERNET_100G_LR: A 100G Ethernet with LR optics.
  * LINK_TYPE_ETHERNET_400G_LR4: A 400G Ethernet with LR4 optics.

Note that this field indicates the speed of each of the links in the bundle, not the speed of the entire bundle.   
`requestedLinkCount` |  `integer` Target number of physical links in the link bundle, as requested by the customer.  
`interconnectType` |  `enum` Type of interconnect, which can take one of the following values: 

  * PARTNER: A partner-managed interconnection shared between customers though a partner.
  * DEDICATED: A dedicated physical interconnection with the customer.

Note that a value IT_PRIVATE has been deprecated in favor of DEDICATED.   
`adminEnabled` |  `boolean` Administrative status of the interconnect. When this is set to true, the Interconnect is functional and can carry traffic. When set to false, no packets can be carried over the interconnect and no BGP routes are exchanged over it. By default, the status is set to true.  
`nocContactEmail` |  `string` Email address to contact the customer NOC for operations and maintenance notifications regarding this Interconnect. If specified, this will be used for notifications in addition to all other forms described, such as Cloud Monitoring logs alerting and Cloud Notifications. This field is required for users who sign up for Cloud Interconnect using [ workforce identity federation](https://cloud.google.com/iam/docs/workforce-identity-federation).  
`customerName` |  `string` Customer name, to put in the Letter of Authorization as the party authorized to request a crossconnect.  
`operationalStatus` |  `enum` Output only. The current status of this Interconnect's functionality, which can take one of the following values: 

  * OS_ACTIVE: A valid Interconnect, which is turned up and is ready to use. Attachments may be provisioned on this Interconnect.


* OS_UNPROVISIONED: An Interconnect that has not completed turnup. No attachments may be provisioned on this Interconnect.
* OS_UNDER_MAINTENANCE: An Interconnect that is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.  
`provisionedLinkCount` |  `integer` Output only. Number of links actually provisioned in this interconnect.  
`interconnectAttachments[]` |  `string` Output only. A list of the URLs of all InterconnectAttachments configured to use this Interconnect.  
`peerIpAddress` |  `string` Output only. IP address configured on the customer side of the Interconnect link. The customer should configure this IP address during turnup when prompted by Google NOC. This can be used only for ping tests.  
`googleIpAddress` |  `string` Output only. IP address configured on the Google side of the Interconnect link. This can be used only for ping tests.  
`googleReferenceId` |  `string` Output only. Google reference ID to be used when raising support tickets with Google or otherwise to debug backend connectivity issues.  
`expectedOutages[]` |  `object` Output only. A list of outages expected for this Interconnect.  
`expectedOutages[].name` |  `string` Unique identifier for this outage notification.  
`expectedOutages[].description` |  `string` A description about the purpose of the outage.  
`expectedOutages[].source` |  `enum` The party that generated this notification, which can take the following value: 

  * GOOGLE: this notification as generated by Google.

Note that the value of NSRC_GOOGLE has been deprecated in favor of GOOGLE.   
`expectedOutages[].state` |  `enum` State of this notification, which can take one of the following values: 

  * ACTIVE: This outage notification is active. The event could be in the past, present, or future. See startTime and endTime for scheduling.
  * CANCELLED: The outage associated with this notification was cancelled before the outage was due to start.
  * COMPLETED: The outage associated with this notification is complete. 

Note that the versions of this enum prefixed with "NS_" have been deprecated in favor of the unprefixed values.   
`expectedOutages[].issueType` |  `enum` Form this outage is expected to take, which can take one of the following values: 

  * OUTAGE: The Interconnect may be completely out of service for some or all of the specified window.
  * PARTIAL_OUTAGE: Some circuits comprising the Interconnect as a whole should remain up, but with reduced bandwidth.

Note that the versions of this enum prefixed with "IT_" have been deprecated in favor of the unprefixed values.   
`expectedOutages[].affectedCircuits[]` |  `string` If issueType is IT_PARTIAL_OUTAGE, a list of the Google-side circuit IDs that will be affected.  
`expectedOutages[].startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Scheduled start time for the outage (milliseconds since Unix epoch).  
`expectedOutages[].endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Scheduled end time for the outage (milliseconds since Unix epoch).  
`circuitInfos[]` |  `object` Output only. A list of CircuitInfo objects, that describe the individual circuits in this LAG.  
`circuitInfos[].googleCircuitId` |  `string` Google-assigned unique ID for this circuit. Assigned at circuit turn-up.  
`circuitInfos[].googleDemarcId` |  `string` Google-side demarc ID for this circuit. Assigned at circuit turn-up and provided by Google to the customer in the LOA.  
`circuitInfos[].customerDemarcId` |  `string` Customer-side demarc ID for this circuit.  
`labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `labels`:

  * `compute.interconnects.setLabels`

  
`labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this Interconnect, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve an Interconnect.A base64-encoded string.  
`state` |  `enum` Output only. The current state of Interconnect functionality, which can take one of the following values: 

  * ACTIVE: The Interconnect is valid, turned up and ready to use. Attachments may be provisioned on this Interconnect.
  * UNPROVISIONED: The Interconnect has not completed turnup. No attachments may be provisioned on this Interconnect.
  * UNDER_MAINTENANCE: The Interconnect is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.

  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`macsec` |  `object` Configuration that enables Media Access Control security (MACsec) on the Cloud Interconnect connection between Google and your on-premises router.  
`macsec.preSharedKeys[]` |  `object` Required. A keychain placeholder describing a set of named key objects along with their start times. A MACsec CKN/CAK is generated for each key in the key chain. Google router automatically picks the key with the most recent startTime when establishing or re-establishing a MACsec secure link.  
`macsec.preSharedKeys[].name` |  `string` Required. A name for this pre-shared key. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`macsec.preSharedKeys[].startTime` |  `string` A [RFC3339](http://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the key is valid. startTime can be in the future. If the keychain has a single key, startTime can be omitted. If the keychain has multiple keys, startTime is mandatory for each key. The start times of keys must be in increasing order. The start times of two consecutive keys must be at least 6 hours apart.  
`macsec.failOpen` |  `boolean` If set to true, the Interconnect connection is configured with a `should-secure` MACsec security policy, that allows the Google router to fallback to cleartext traffic if the MKA session cannot be established. By default, the Interconnect connection is configured with a `must-secure` security policy that drops all traffic if the MKA session cannot be established with your router.  
`macsecEnabled` |  `boolean` Enable or disable MACsec on this Interconnect connection. MACsec enablement fails if the MACsec object is not specified.  
`remoteLocation` |  `string` Indicates that this is a Cross-Cloud Interconnect. This field specifies the location outside of Google's network that the interconnect is connected to.  
`requestedFeatures[]` |  `enum` Optional. This parameter can be provided only with Interconnect INSERT. It isn't valid for Interconnect PATCH. interconnects.list of features requested for this Interconnect connection, which can take one of the following values: 

  * IF_MACSEC: If specified, then the connection is created on MACsec capable hardware ports. If not specified, non-MACsec capable ports will also be considered.
  * IF_CROSS_SITE_NETWORK: If specified, then the connection is created exclusively for Cross-Site Networking. The connection can not be used for Cross-Site Networking unless this feature is specified.

  
`availableFeatures[]` |  `enum` Output only. interconnects.list of features available for this Interconnect connection, which can take one of the following values: 

  * IF_MACSEC: If present, then the Interconnect connection is provisioned on MACsec capable hardware ports. If not present, then the Interconnect connection is provisioned on non-MACsec capable ports. Any attempt to enable MACsec will fail.
  * IF_CROSS_SITE_NETWORK: If present, then the Interconnect connection is provisioned exclusively for Cross-Site Networking. Any attempt to configure VLAN attachments will fail. If not present, then the Interconnect connection is not provisioned for Cross-Site Networking. Any attempt to use it for Cross-Site Networking will fail.

  
`applicationAwareInterconnect` |  `object` Configuration information for application awareness on this Cloud Interconnect.  
`applicationAwareInterconnect.strictPriorityPolicy` |  `object`  
`applicationAwareInterconnect.bandwidthPercentagePolicy` |  `object`  
`applicationAwareInterconnect.bandwidthPercentagePolicy.bandwidthPercentages[]` |  `object` Specify bandwidth percentages for various traffic classes for queuing type Bandwidth Percent.  
`applicationAwareInterconnect.bandwidthPercentagePolicy.bandwidthPercentages[].trafficClass` |  `enum` TrafficClass whose bandwidth percentage is being specified.  
`applicationAwareInterconnect.bandwidthPercentagePolicy.bandwidthPercentages[].percentage` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Bandwidth percentage for a specific traffic class.  
`applicationAwareInterconnect.profileDescription` |  `string` Description for the application awareness profile on this Cloud Interconnect.  
`applicationAwareInterconnect.shapeAveragePercentages[]` |  `object` Optional field to specify a list of shape average percentages to be applied in conjunction with StrictPriorityPolicy or BandwidthPercentagePolicy.  
`applicationAwareInterconnect.shapeAveragePercentages[].trafficClass` |  `enum` TrafficClass whose bandwidth percentage is being specified.  
`applicationAwareInterconnect.shapeAveragePercentages[].percentage` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Bandwidth percentage for a specific traffic class.  
`aaiEnabled` |  `boolean` Enable or disable the application awareness feature on this Cloud Interconnect.  
`interconnectGroups[]` |  `string` Output only. URLs of InterconnectGroups that include this Interconnect. Order is arbitrary and items are unique.  
`wireGroups[]` |  `string` Output only. A list of the URLs of all CrossSiteNetwork WireGroups configured to use this Interconnect. The Interconnect cannot be deleted if this list is non-empty.  
`params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid. * Inconsistent format is not supported. For instance: {"tagKeys/333" : "tagValues/444", "123/env" : "prod"} is invalid.  
`effectiveLocation` |  `string` Output only. URL of the InterconnectLocation object that represents where this connection is to be provisioned. By default it will be the same as the location field.  
  
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

  * `compute.interconnects.create`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
