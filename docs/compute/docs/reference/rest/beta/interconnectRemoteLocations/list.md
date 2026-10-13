---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/interconnectRemoteLocations/list/
title: Method: interconnectRemoteLocations.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:08.699547+00:00
---

# Method: interconnectRemoteLocations.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/interconnectRemoteLocations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: interconnectRemoteLocations.list Stay organized with collections  Save and categorize content based on your preferences. 

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



Retrieves the list of interconnect remote locations available to the specified project.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/projects/{project}/global/interconnectRemoteLocations`

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

Response to the list request, and contains a list of interconnect remote locations.

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
          "id": string,
          "creationTimestamp": string,
          "name": string,
          "peeringdbFacilityId": string,
          "address": string,
          "facilityProvider": string,
          "facilityProviderFacilityId": string,
          "continent": enum,
          "city": string,
          "status": enum,
          "remoteService": string,
          "permittedConnections": [
            {
              "interconnectLocation": string
            }
          ],
          "constraints": {
            "subnetLengthRange": {
              "min": integer,
              "max": integer
            },
            "portPairVlan": enum,
            "portPairRemoteLocation": enum
          },
          "attachmentConfigurationConstraints": {
            "bgpMd5": enum,
            "bgpPeerAsnRanges": [
              {
                "min": integer,
                "max": integer
              }
            ]
          },
          "lacp": enum,
          "maxLagSize100Gbps": integer,
          "maxLagSize10Gbps": integer,
          "maxLagSize400Gbps": integer
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
`kind` |  `string` Output only. Type of resource. Always `compute#interconnectRemoteLocationList` for lists of interconnect remote locations.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of InterconnectRemoteLocation resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#interconnectRemoteLocation` for interconnect remote locations.  
`items[].description` |  `string` Output only. An optional description of the resource.  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Output only. Name of the resource.  
`items[].peeringdbFacilityId` |  `string` Output only. The peeringdb identifier for this facility (corresponding with a netfac type in peeringdb).  
`items[].address` |  `string` Output only. The postal address of the Point of Presence, each line in the address is separated by a newline character.  
`items[].facilityProvider` |  `string` Output only. The name of the provider for this facility (e.g., EQUINIX).  
`items[].facilityProviderFacilityId` |  `string` Output only. A provider-assigned Identifier for this facility (e.g., Ashburn-DC1).  
`items[].continent` |  `enum` Output only. Continent for this location, which can take one of the following values: 

  * AFRICA
  * ASIA_PAC
  * EUROPE
  * NORTH_AMERICA
  * SOUTH_AMERICA

  
`items[].city` |  `string` Output only. Metropolitan area designator that indicates which city an interconnect is located. For example: "Chicago, IL", "Amsterdam, Netherlands".  
`items[].status` |  `enum` Output only. The status of this InterconnectRemoteLocation, which can take one of the following values: 

  * CLOSED: The InterconnectRemoteLocation is closed and is unavailable for provisioning new Cross-Cloud Interconnects.
  * AVAILABLE: The InterconnectRemoteLocation is available for provisioning new Cross-Cloud Interconnects.

  
`items[].remoteService` |  `string` Output only. Indicates the service provider present at the remote location. Example values: "Amazon Web Services", "Microsoft Azure".  
`items[].permittedConnections[]` |  `object` Output only. Permitted connections.  
`items[].permittedConnections[].interconnectLocation` |  `string` Output only. URL of an Interconnect location that is permitted to connect to this Interconnect remote location.  
`items[].constraints` |  `object` Output only. Constraints on the parameters for creating Cross-Cloud Interconnect and associated InterconnectAttachments.  
`items[].constraints.subnetLengthRange` |  `object` Output only. [min-length, max-length]  The minimum and maximum value (inclusive) for the IPv4 subnet length. For example, an interconnectRemoteLocation for Azure has {min: 30, max: 30} because Azure requires /30 subnets.  This range specifies the values supported by both cloud providers. Interconnect currently supports /29 and /30 IPv4 subnet lengths. If a remote cloud has no constraint on IPv4 subnet length, the range would thus be {min: 29, max: 30}.  
`items[].constraints.subnetLengthRange.min` |  `integer`  
`items[].constraints.subnetLengthRange.max` |  `integer`  
`items[].constraints.portPairVlan` |  `enum` Output only. Port pair VLAN constraints, which can take one of the following values: PORT_PAIR_UNCONSTRAINED_VLAN, PORT_PAIR_MATCHING_VLAN  
`items[].constraints.portPairRemoteLocation` |  `enum` Output only. Port pair remote location constraints, which can take one of the following values: PORT_PAIR_UNCONSTRAINED_REMOTE_LOCATION, PORT_PAIR_MATCHING_REMOTE_LOCATION.Google Cloud API refers only to individual ports, but the UI uses this field when ordering a pair of ports, to prevent users from accidentally ordering something that is incompatible with their cloud provider. Specifically, when ordering a redundant pair of Cross-Cloud Interconnect ports, and one of them uses a remote location with portPairMatchingRemoteLocation set to matching, the UI requires that both ports use the same remote location.  
`items[].attachmentConfigurationConstraints` |  `object` Output only. Subset of fields from InterconnectAttachment's |configurationConstraints| field that apply to all attachments for this remote location.  
`items[].attachmentConfigurationConstraints.bgpMd5` |  `enum` Output only. Whether the attachment's BGP session requires/allows/disallows BGP MD5 authentication. This can take one of the following values: MD5_OPTIONAL, MD5_REQUIRED, MD5_UNSUPPORTED.For example, a Cross-Cloud Interconnect connection to a remote cloud provider that requires BGP MD5 authentication has the interconnectRemoteLocation attachmentConfigurationConstraints.bgp_md5 field set to MD5_REQUIRED, and that property is propagated to the attachment. Similarly, if BGP MD5 is MD5_UNSUPPORTED, an error is returned if MD5 is requested.  
`items[].attachmentConfigurationConstraints.bgpPeerAsnRanges[]` |  `object` Output only. interconnectRemoteLocations.list of ASN ranges that the remote location is known to support. Formatted as an array of inclusive ranges {min: min-value, max: max-value}. For example, [{min: 123, max: 123}, {min: 64512, max: 65534}] allows the peer ASN to be 123 or anything in the range 64512-65534.This field is only advisory. Although the API accepts other ranges, these are the ranges that we recommend.  
`items[].attachmentConfigurationConstraints.bgpPeerAsnRanges[].min` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].attachmentConfigurationConstraints.bgpPeerAsnRanges[].max` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].lacp` |  `enum` Output only. Link Aggregation Control Protocol (LACP) constraints, which can take one of the following values: LACP_SUPPORTED, LACP_UNSUPPORTED  
`items[].maxLagSize100Gbps` |  `integer` Output only. The maximum number of 100 Gbps ports supported in a link aggregation group (LAG). When linkType is 100 Gbps, requestedLinkCount cannot exceed maxLagSize100Gbps.  
`items[].maxLagSize10Gbps` |  `integer` Output only. The maximum number of 10 Gbps ports supported in a link aggregation group (LAG). When linkType is 10 Gbps, requestedLinkCount cannot exceed maxLagSize10Gbps.  
`items[].maxLagSize400Gbps` |  `integer` Output only. The maximum number of 400 Gbps ports supported in a link aggregation group (LAG). When linkType is 400 Gbps, requestedLinkCount cannot exceed maxLagSize400Gbps.  
`nextPageToken` |  `string` Output only. This token lets you get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
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

  * `compute.interconnectRemoteLocations.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
