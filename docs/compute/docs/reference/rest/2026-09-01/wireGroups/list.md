---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/wireGroups/list/
title: Method: wireGroups.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:31.215427+00:00
---

# Method: wireGroups.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/wireGroups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: wireGroups.list Stay organized with collections  Save and categorize content based on your preferences. 

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



API Version : 2026-09-01

Lists the wire groups for a project in the given scope.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/crossSiteNetworks/{crossSiteNetwork}/wireGroups?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`crossSiteNetwork` |  `string`  
  
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
  
### Request body

The request body must be empty.

### Response body

Response for the list request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
        {
          "kind": string,
          "selfLink": string,
          "id": string,
          "creationTimestamp": string,
          "name": string,
          "description": string,
          "endpoints": {
            string: {
              "interconnects": {
                string: {
                  "interconnect": string,
                  "vlanTags": [
                    integer
                  ]
                },
                ...
              }
            },
            ...
          },
          "wireProperties": {
            "bandwidthUnmetered": string,
            "bandwidthAllocation": enum,
            "faultResponse": enum
          },
          "adminEnabled": boolean,
          "wires": [
            {
              "label": string,
              "endpoints": [
                {
                  "interconnect": string,
                  "vlanTag": integer
                }
              ],
              "wireProperties": {
                "bandwidthUnmetered": string,
                "bandwidthAllocation": enum,
                "faultResponse": enum
              },
              "adminEnabled": boolean
            }
          ],
          "topology": {
            "endpoints": [
              {
                "label": string,
                "city": string
              }
            ]
          },
          "reconciling": boolean
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
      },
      "etag": string,
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#wireGroups` for wire groups.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of wire group resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#wireGroups` for wire groups.  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource type. The server generates this identifier.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].description` |  `string` An optional description of the wire group.  
`items[].endpoints[]` |  `map (key: string, value: object)` A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows: 

  * Key: an RFC1035 user-specified label.
  * Value: an `Endpoint` object.

  
`items[].endpoints[].interconnects[]` |  `map (key: string, value: object)` A map that contains the redundant Interconnect connections. Specify key-value pairs for the map as follows: 

  * Key: an RFC1035 user-specified label.
  * Value: an `Interconnect` object.

  
`items[].endpoints[].interconnects[].interconnect` |  `string` Required. An Interconnect connection. You can specify the connection as a partial or full URL. If the connection is in a different project from the cross-site network, use a format that specifies the project. See the following examples of partial and full URLs: 

`global/interconnects/NAME` `projects/PROJECT_ID/global/interconnects/NAME`
  * `<https://compute.googleapis.com/compute/projects/>PROJECT_ID/global/interconnects/NAME`

  
`items[].endpoints[].interconnects[].vlanTags[]` |  `integer` Required. To configure the wire group for VLAN mode, enter a VLAN tag, which is a number from `2` to `4093`. You can autoallocate a tag by entering `0`. To configure the wire group for port mode, enter `-1`. Review the following guidelines: 

  * A VLAN tag must be unique for an Interconnect connection across all attachments and wire groups.
  * Both endpoints of a wire must use the same VLAN tag value.
  * Single wire and redundant type wire groups must have only one VLAN tag.
  * Port mode pseudowires must have a single VLAN tag with a value of `-1` for both endpoints.
  * Box and cross type wire groups must have two VLAN tags. The first is for the same-zone pseudowire, and the second is for the cross-zone pseudowire.

  
`items[].wireProperties` |  `object` Properties for all wires in the wire group.  
`items[].wireProperties.bandwidthUnmetered` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The unmetered bandwidth in Gigabits per second, using decimal units. `10` is 10 Gbps, `100` is 100 Gbps. The bandwidth must be greater than 0.  
`items[].wireProperties.bandwidthAllocation` |  `enum` The configuration of the bandwidth allocation, one of the following: 

  * ALLOCATE_PER_WIRE: configures a separate unmetered bandwidth allocation (and associated charges) for each wire in the group.
  * SHARED_WITH_WIRE_GROUP: this is the default behavior, which configures one unmetered bandwidth allocation for the wire group. The unmetered bandwidth is divided equally across each wire in the group, but dynamic throttling reallocates unused unmetered bandwidth from unused or underused wires to other wires in the group.

  
`items[].wireProperties.faultResponse` |  `enum` Response when a fault is detected in a pseudowire: 

  * NONE: default.
  * DISABLE_PORT: set the port line protocol down when inline probes detect a fault. This setting is only permitted on port mode pseudowires.

  
`items[].adminEnabled` |  `boolean` Indicates whether the wires in the wire group are enabled. When false, the wires in the wire group are disabled. When true and when there is simultaneously no wire-specific override of `adminEnabled` to false, a given wire is enabled. Defaults to true.  
`items[].wires[]` |  `object` Output only. The single/redundant wire(s) managed by the wire group.  
`items[].wires[].label` |  `string` Output only. A label that identifies the wire. The format of this label combines the existing labels of the wire group endpoints and Interconnect connections used by this wire in alphabetical order as follows: `ENDPOINT_A+CONNECTION_A1,ENDPOINT_B+CONNECTION_B1`, where: 

  * `ENDPOINT_A` and `ENDPOINT_B`: are the labels that you entered as map keys when you specified the wire group endpoint objects.
  * `CONNECTION_A1` and `CONNECTION_B1`: are the labels that you entered as map keys when you specified the wire group Interconnect objects.

  
`items[].wires[].endpoints[]` |  `object` Output only. Wire endpoints are specific Interconnect connections.  
`items[].wires[].endpoints[].interconnect` |  `string`  
`items[].wires[].endpoints[].vlanTag` |  `integer`  
`items[].wires[].wireProperties` |  `object` Output only. Properties of the wire.  
`items[].wires[].wireProperties.bandwidthUnmetered` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The unmetered bandwidth in Gigabits per second, using decimal units. `10` is 10 Gbps, `100` is 100 Gbps. The bandwidth must be greater than 0.  
`items[].wires[].wireProperties.bandwidthAllocation` |  `enum` The configuration of the bandwidth allocation, one of the following: 

  * ALLOCATE_PER_WIRE: configures a separate unmetered bandwidth allocation (and associated charges) for each wire in the group.
  * SHARED_WITH_WIRE_GROUP: this is the default behavior, which configures one unmetered bandwidth allocation for the wire group. The unmetered bandwidth is divided equally across each wire in the group, but dynamic throttling reallocates unused unmetered bandwidth from unused or underused wires to other wires in the group.

  
`items[].wires[].wireProperties.faultResponse` |  `enum` Response when a fault is detected in a pseudowire: 

  * NONE: default.
  * DISABLE_PORT: set the port line protocol down when inline probes detect a fault. This setting is only permitted on port mode pseudowires.

  
`items[].wires[].adminEnabled` |  `boolean` Output only. Indicates whether the wire is enabled. When false, the wire is disabled. When true and when the wire group of the wire is also enabled, the wire is enabled. Defaults to true.  
`items[].topology` |  `object` Output only. Topology details for the wire group configuration.  
`items[].topology.endpoints[]` |  `object` Output only. Topology details for all endpoints in the wire group.  
`items[].topology.endpoints[].label` |  `string` Output only. Endpoint label from the wire group.  
`items[].topology.endpoints[].city` |  `string` Output only. The InterconnectLocation.city (metropolitan area designator) that all interconnects are located in.  
`items[].reconciling` |  `boolean` Output only. Indicates whether there are wire changes yet to be processed.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`etag` |  `string`  
`unreachables[]` |  `string` Output only. Unreachable resources. end_interface: MixerListResponseWithEtagBuilder  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.wireGroups.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
