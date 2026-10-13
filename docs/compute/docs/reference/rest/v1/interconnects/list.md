---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/list/
title: Method: interconnects.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:21.280319+00:00
---

# Method: interconnects.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: interconnects.list Stay organized with collections  Save and categorize content based on your preferences. 

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
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieves the list of Interconnects available to the specified project.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/interconnects`

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
  
### Request body

The request body must be empty.

### Response body

Response to the list request, and contains a list of interconnects.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
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
            "profileDescription": string,
            "shapeAveragePercentages": [
              {
                "trafficClass": enum,
                "percentage": integer
              }
            ],
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "strictPriorityPolicy": ,
            "bandwidthPercentagePolicy": {
              "bandwidthPercentages": [
                {
                  "trafficClass": enum,
                  "percentage": integer
                }
              ]
            }
            // End of mutually exclusive fields.
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
`kind` |  `string` Output only. Type of resource. Always `compute#interconnectList` for lists of interconnects.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of Interconnect resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#interconnect` for interconnects.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].location` |  `string` URL of the InterconnectLocation object that represents where this connection is to be provisioned.  
`items[].subzone` |  `enum` To be deprecated.  
`items[].linkType` |  `enum` Type of link requested, which can take one of the following values: 

  * LINK_TYPE_ETHERNET_10G_LR: A 10G Ethernet with LR optics
  * LINK_TYPE_ETHERNET_100G_LR: A 100G Ethernet with LR optics.
  * LINK_TYPE_ETHERNET_400G_LR4: A 400G Ethernet with LR4 optics.

Note that this field indicates the speed of each of the links in the bundle, not the speed of the entire bundle.   
`items[].requestedLinkCount` |  `integer` Target number of physical links in the link bundle, as requested by the customer.  
`items[].interconnectType` |  `enum` Type of interconnect, which can take one of the following values: 

  * PARTNER: A partner-managed interconnection shared between customers though a partner.
  * DEDICATED: A dedicated physical interconnection with the customer.

Note that a value IT_PRIVATE has been deprecated in favor of DEDICATED.   
`items[].adminEnabled` |  `boolean` Administrative status of the interconnect. When this is set to true, the Interconnect is functional and can carry traffic. When set to false, no packets can be carried over the interconnect and no BGP routes are exchanged over it. By default, the status is set to true.  
`items[].nocContactEmail` |  `string` Email address to contact the customer NOC for operations and maintenance notifications regarding this Interconnect. If specified, this will be used for notifications in addition to all other forms described, such as Cloud Monitoring logs alerting and Cloud Notifications. This field is required for users who sign up for Cloud Interconnect using [ workforce identity federation](https://cloud.google.com/iam/docs/workforce-identity-federation).  
`items[].customerName` |  `string` Customer name, to put in the Letter of Authorization as the party authorized to request a crossconnect.  
`items[].operationalStatus` |  `enum` Output only. The current status of this Interconnect's functionality, which can take one of the following values: 

  * OS_ACTIVE: A valid Interconnect, which is turned up and is ready to use. Attachments may be provisioned on this Interconnect.


* OS_UNPROVISIONED: An Interconnect that has not completed turnup. No attachments may be provisioned on this Interconnect.
* OS_UNDER_MAINTENANCE: An Interconnect that is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.  
`items[].provisionedLinkCount` |  `integer` Output only. Number of links actually provisioned in this interconnect.  
`items[].interconnectAttachments[]` |  `string` Output only. A list of the URLs of all InterconnectAttachments configured to use this Interconnect.  
`items[].peerIpAddress` |  `string` Output only. IP address configured on the customer side of the Interconnect link. The customer should configure this IP address during turnup when prompted by Google NOC. This can be used only for ping tests.  
`items[].googleIpAddress` |  `string` Output only. IP address configured on the Google side of the Interconnect link. This can be used only for ping tests.  
`items[].googleReferenceId` |  `string` Output only. Google reference ID to be used when raising support tickets with Google or otherwise to debug backend connectivity issues.  
`items[].expectedOutages[]` |  `object` Output only. A list of outages expected for this Interconnect.  
`items[].expectedOutages[].name` |  `string` Unique identifier for this outage notification.  
`items[].expectedOutages[].description` |  `string` A description about the purpose of the outage.  
`items[].expectedOutages[].source` |  `enum` The party that generated this notification, which can take the following value: 

  * GOOGLE: this notification as generated by Google.

Note that the value of NSRC_GOOGLE has been deprecated in favor of GOOGLE.   
`items[].expectedOutages[].state` |  `enum` State of this notification, which can take one of the following values: 

  * ACTIVE: This outage notification is active. The event could be in the past, present, or future. See startTime and endTime for scheduling.
  * CANCELLED: The outage associated with this notification was cancelled before the outage was due to start.
  * COMPLETED: The outage associated with this notification is complete. 

Note that the versions of this enum prefixed with "NS_" have been deprecated in favor of the unprefixed values.   
`items[].expectedOutages[].issueType` |  `enum` Form this outage is expected to take, which can take one of the following values: 

  * OUTAGE: The Interconnect may be completely out of service for some or all of the specified window.
  * PARTIAL_OUTAGE: Some circuits comprising the Interconnect as a whole should remain up, but with reduced bandwidth.

Note that the versions of this enum prefixed with "IT_" have been deprecated in favor of the unprefixed values.   
`items[].expectedOutages[].affectedCircuits[]` |  `string` If issueType is IT_PARTIAL_OUTAGE, a list of the Google-side circuit IDs that will be affected.  
`items[].expectedOutages[].startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Scheduled start time for the outage (milliseconds since Unix epoch).  
`items[].expectedOutages[].endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Scheduled end time for the outage (milliseconds since Unix epoch).  
`items[].circuitInfos[]` |  `object` Output only. A list of CircuitInfo objects, that describe the individual circuits in this LAG.  
`items[].circuitInfos[].googleCircuitId` |  `string` Google-assigned unique ID for this circuit. Assigned at circuit turn-up.  
`items[].circuitInfos[].googleDemarcId` |  `string` Google-side demarc ID for this circuit. Assigned at circuit turn-up and provided by Google to the customer in the LOA.  
`items[].circuitInfos[].customerDemarcId` |  `string` Customer-side demarc ID for this circuit.  
`items[].labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty.  
`items[].labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this Interconnect, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve an Interconnect.A base64-encoded string.  
`items[].state` |  `enum` Output only. The current state of Interconnect functionality, which can take one of the following values: 

  * ACTIVE: The Interconnect is valid, turned up and ready to use. Attachments may be provisioned on this Interconnect.
  * UNPROVISIONED: The Interconnect has not completed turnup. No attachments may be provisioned on this Interconnect.
  * UNDER_MAINTENANCE: The Interconnect is undergoing internal maintenance. No attachments may be provisioned or updated on this Interconnect.

  
`items[].satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`items[].macsec` |  `object` Configuration that enables Media Access Control security (MACsec) on the Cloud Interconnect connection between Google and your on-premises router.  
`items[].macsec.preSharedKeys[]` |  `object` Required. A keychain placeholder describing a set of named key objects along with their start times. A MACsec CKN/CAK is generated for each key in the key chain. Google router automatically picks the key with the most recent startTime when establishing or re-establishing a MACsec secure link.  
`items[].macsec.preSharedKeys[].name` |  `string` Required. A name for this pre-shared key. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].macsec.preSharedKeys[].startTime` |  `string` A [RFC3339](http://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the key is valid. startTime can be in the future. If the keychain has a single key, startTime can be omitted. If the keychain has multiple keys, startTime is mandatory for each key. The start times of keys must be in increasing order. The start times of two consecutive keys must be at least 6 hours apart.  
`items[].macsec.failOpen` |  `boolean` If set to true, the Interconnect connection is configured with a `should-secure` MACsec security policy, that allows the Google router to fallback to cleartext traffic if the MKA session cannot be established. By default, the Interconnect connection is configured with a `must-secure` security policy that drops all traffic if the MKA session cannot be established with your router.  
`items[].macsecEnabled` |  `boolean` Enable or disable MACsec on this Interconnect connection. MACsec enablement fails if the MACsec object is not specified.  
`items[].remoteLocation` |  `string` Indicates that this is a Cross-Cloud Interconnect. This field specifies the location outside of Google's network that the interconnect is connected to.  
`items[].requestedFeatures[]` |  `enum` Optional. This parameter can be provided only with Interconnect INSERT. It isn't valid for Interconnect PATCH. interconnects.list of features requested for this Interconnect connection, which can take one of the following values: 

  * IF_MACSEC: If specified, then the connection is created on MACsec capable hardware ports. If not specified, non-MACsec capable ports will also be considered.
  * IF_CROSS_SITE_NETWORK: If specified, then the connection is created exclusively for Cross-Site Networking. The connection can not be used for Cross-Site Networking unless this feature is specified.

  
`items[].availableFeatures[]` |  `enum` Output only. interconnects.list of features available for this Interconnect connection, which can take one of the following values: 

  * IF_MACSEC: If present, then the Interconnect connection is provisioned on MACsec capable hardware ports. If not present, then the Interconnect connection is provisioned on non-MACsec capable ports. Any attempt to enable MACsec will fail.
  * IF_CROSS_SITE_NETWORK: If present, then the Interconnect connection is provisioned exclusively for Cross-Site Networking. Any attempt to configure VLAN attachments will fail. If not present, then the Interconnect connection is not provisioned for Cross-Site Networking. Any attempt to use it for Cross-Site Networking will fail.

  
`items[].applicationAwareInterconnect` |  `object` Configuration information for application awareness on this Cloud Interconnect.  
`items[].applicationAwareInterconnect.strictPriorityPolicy` |  `object`  
`items[].applicationAwareInterconnect.bandwidthPercentagePolicy` |  `object`  
`items[].applicationAwareInterconnect.bandwidthPercentagePolicy.bandwidthPercentages[]` |  `object` Specify bandwidth percentages for various traffic classes for queuing type Bandwidth Percent.  
`items[].applicationAwareInterconnect.bandwidthPercentagePolicy.bandwidthPercentages[].trafficClass` |  `enum` TrafficClass whose bandwidth percentage is being specified.  
`items[].applicationAwareInterconnect.bandwidthPercentagePolicy.bandwidthPercentages[].percentage` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Bandwidth percentage for a specific traffic class.  
`items[].applicationAwareInterconnect.profileDescription` |  `string` Description for the application awareness profile on this Cloud Interconnect.  
`items[].applicationAwareInterconnect.shapeAveragePercentages[]` |  `object` Optional field to specify a list of shape average percentages to be applied in conjunction with StrictPriorityPolicy or BandwidthPercentagePolicy.  
`items[].applicationAwareInterconnect.shapeAveragePercentages[].trafficClass` |  `enum` TrafficClass whose bandwidth percentage is being specified.  
`items[].applicationAwareInterconnect.shapeAveragePercentages[].percentage` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Bandwidth percentage for a specific traffic class.  
`items[].aaiEnabled` |  `boolean` Enable or disable the application awareness feature on this Cloud Interconnect.  
`items[].interconnectGroups[]` |  `string` Output only. URLs of InterconnectGroups that include this Interconnect. Order is arbitrary and items are unique.  
`items[].wireGroups[]` |  `string` Output only. A list of the URLs of all CrossSiteNetwork WireGroups configured to use this Interconnect. The Interconnect cannot be deleted if this list is non-empty.  
`items[].params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`items[].params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid. * Inconsistent format is not supported. For instance: {"tagKeys/333" : "tagValues/444", "123/env" : "prod"} is invalid.  
`items[].effectiveLocation` |  `string` Output only. URL of the InterconnectLocation object that represents where this connection is to be provisioned. By default it will be the same as the location field.  
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

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.interconnects.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
