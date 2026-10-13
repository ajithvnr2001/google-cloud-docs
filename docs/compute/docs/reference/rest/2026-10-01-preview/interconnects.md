---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/
title: REST Resource: interconnects \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:49.017380+00:00
---

# REST Resource: interconnects  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: interconnects Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Interconnect
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Methods



## Resource: Interconnect

Represents an Interconnect resource.

An Interconnect resource is a dedicated connection between the Google Cloud network and your on-premises network. For more information, read the [ Dedicated Interconnect Overview](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview).

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
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
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
`labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty.  
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
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/delete)`

|  Deletes the specified Interconnect.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/get)`

|  Returns the specified Interconnect.  
  
### `[getDiagnostics](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/getDiagnostics)`

|  Returns the `interconnectDiagnostics` for the specified Interconnect.  
  
### `[getMacsecConfig](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/getMacsecConfig)`

|  Returns the `interconnectMacsecConfig` for the specified Interconnect.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/insert)`

|  Creates an Interconnect in the specified project using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/list)`

|  Retrieves the list of Interconnects available to the specified project.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/patch)`

|  Updates the specified Interconnect with the data included in the request.  
  
### `[setLabels](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/interconnects/setLabels)`

|  Sets the labels on an Interconnect.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
