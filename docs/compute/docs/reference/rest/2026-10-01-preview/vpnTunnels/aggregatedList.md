---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/vpnTunnels/aggregatedList/
title: Method: vpnTunnels.aggregatedList \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:53.507408+00:00
---

# Method: vpnTunnels.aggregatedList  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/vpnTunnels/aggregatedList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: vpnTunnels.aggregatedList Stay organized with collections  Save and categorize content based on your preferences. 

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
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-10-01-preview

Retrieves an aggregated list of VPN tunnels.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/aggregated/vpnTunnels?$apiVersion=2026-10-01-preview`

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
`includeAllScopes` |  `boolean` Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included.  
`serviceProjectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": {
        string: {
          "vpnTunnels": [
            {
              "kind": string,
              "id": string,
              "creationTimestamp": string,
              "name": string,
              "description": string,
              "region": string,
              "targetVpnGateway": string,
              "vpnGateway": string,
              "vpnGatewayInterface": integer,
              "peerExternalGateway": string,
              "peerExternalGatewayInterface": integer,
              "peerGcpGateway": string,
              "router": string,
              "peerIp": string,
              "sharedSecret": string,
              "sharedSecretHash": string,
              "status": enum,
              "selfLink": string,
              "ikeVersion": integer,
              "detailedStatus": string,
              "localTrafficSelector": [
                string
              ],
              "remoteTrafficSelector": [
                string
              ],
              "labels": {
                string: string,
                ...
              },
              "labelFingerprint": string,
              "cipherSuite": {
                "phase1": {
                  "encryption": [
                    string
                  ],
                  "integrity": [
                    string
                  ],
                  "prf": [
                    string
                  ],
                  "dh": [
                    string
                  ]
                },
                "phase2": {
                  "encryption": [
                    string
                  ],
                  "integrity": [
                    string
                  ],
                  "pfs": [
                    string
                  ]
                }
              },
              "params": {
                "resourceManagerTags": {
                  string: string,
                  ...
                }
              }
            }
          ],
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
        },
        ...
      },
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
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#vpnTunnel` for VPN tunnels.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items` |  `map (key: string, value: object)` A list of VpnTunnelsScopedList resources.**Key:** Name of the scope containing this set of VPN tunnels.  
`items.vpnTunnels[]` |  `object` A list of VPN tunnels contained in this scope.  
`items.vpnTunnels[].kind` |  `string` Output only. Type of resource. Always `compute#vpnTunnel` for VPN tunnels.  
`items.vpnTunnels[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items.vpnTunnels[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.vpnTunnels[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items.vpnTunnels[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items.vpnTunnels[].region` |  `string` Output only. URL of the region where the VPN tunnel resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`items.vpnTunnels[].targetVpnGateway` |  `string` URL of the Target VPN gateway with which this VPN tunnel is associated. Provided by the client when the VPN tunnel is created. This field can be set only for Classic VPN tunnels.  
`items.vpnTunnels[].vpnGateway` |  `string` URL of the VPN gateway with which this VPN tunnel is associated. Provided by the client when the VPN tunnel is created. This must be used (instead of targetVpnGateway) if a High Availability VPN gateway resource is created.  
`items.vpnTunnels[].vpnGatewayInterface` |  `integer` The interface ID of the VPN gateway with which this VPN tunnel is associated. Possible values are: `0`, `1`.  
`items.vpnTunnels[].peerExternalGateway` |  `string` URL of the peer side external VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. This field is exclusive with the field peerGcpGateway.  
`items.vpnTunnels[].peerExternalGatewayInterface` |  `integer` The interface ID of the external VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. Possible values are: `0`, `1`, `2`, `3`. The number of IDs in use depends on the external VPN gateway redundancy type.  
`items.vpnTunnels[].peerGcpGateway` |  `string` URL of the peer side HA VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. This field can be used when creating highly available VPN from VPC network to VPC network, the field is exclusive with the field peerExternalGateway. If provided, the VPN tunnel will automatically use the same vpnGatewayInterface ID in the peer Google Cloud VPN gateway.  
`items.vpnTunnels[].router` |  `string` URL of the router resource to be used for dynamic routing.  
`items.vpnTunnels[].peerIp` |  `string` IP address of the peer VPN gateway. Only IPv4 is supported. This field can be set only for Classic VPN tunnels.  
`items.vpnTunnels[].sharedSecret` |  `string` Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway.  
`items.vpnTunnels[].sharedSecretHash` |  `string` Hash of the shared secret.  
`items.vpnTunnels[].status` |  `enum` Output only. The status of the VPN tunnel, which can be one of the following: 

  * PROVISIONING: Resource is being allocated for the VPN tunnel.
  * WAITING_FOR_FULL_CONFIG: Waiting to receive all VPN-related configs from the user. Network, TargetVpnGateway, VpnTunnel, ForwardingRule, and Route resources are needed to setup the VPN tunnel.
  * FIRST_HANDSHAKE: Successful first handshake with the peer VPN.
  * ESTABLISHED: Secure session is successfully established with the peer VPN.
  * NETWORK_ERROR: Deprecated, replaced by NO_INCOMING_PACKETS
  * AUTHORIZATION_ERROR: Auth error (for example, bad shared secret).
  * NEGOTIATION_FAILURE: Handshake failed.
  * DEPROVISIONING: Resources are being deallocated for the VPN tunnel.
  * FAILED: Tunnel creation has failed and the tunnel is not ready to be used.
  * NO_INCOMING_PACKETS: No incoming packets from peer.
  * REJECTED: Tunnel configuration was rejected, can be result of being denied access.
  * ALLOCATING_RESOURCES: Cloud VPN is in the process of allocating all required resources.
  * STOPPED: Tunnel is stopped due to its Forwarding Rules being deleted for Classic VPN tunnels or the project is in frozen state.
  * PEER_IDENTITY_MISMATCH: Peer identity does not match peer IP, probably behind NAT.
  * TS_NARROWING_NOT_ALLOWED: Traffic selector narrowing not allowed for an HA-VPN tunnel.

  
`items.vpnTunnels[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items.vpnTunnels[].ikeVersion` |  `integer` IKE protocol version to use when establishing the VPN tunnel with the peer VPN gateway. Acceptable IKE versions are `1` or `2`. The default version is `2`.  
`items.vpnTunnels[].detailedStatus` |  `string` Output only. Detailed status message for the VPN tunnel.  
`items.vpnTunnels[].localTrafficSelector[]` |  `string` Local traffic selector to use when establishing the VPN tunnel with the peer VPN gateway. The value should be a CIDR formatted string, for example: `192.168.0.0/16`. The ranges must be disjoint. Only IPv4 is supported for Classic VPN tunnels. This field is output only for HA VPN tunnels.  
`items.vpnTunnels[].remoteTrafficSelector[]` |  `string` Remote traffic selectors to use when establishing the VPN tunnel with the peer VPN gateway. The value should be a CIDR formatted string, for example: 192.168.0.0/16. The ranges should be disjoint. Only IPv4 is supported for Classic VPN tunnels. This field is output only for HA VPN tunnels.  
`items.vpnTunnels[].labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty.  
`items.vpnTunnels[].labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this VpnTunnel, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a VpnTunnel.A base64-encoded string.  
`items.vpnTunnels[].cipherSuite` |  `object` User specified list of ciphers to use for the phase 1 and phase 2 of the IKE protocol.  
`items.vpnTunnels[].cipherSuite.phase1` |  `object`  
`items.vpnTunnels[].cipherSuite.phase1.encryption[]` |  `string`  
`items.vpnTunnels[].cipherSuite.phase1.integrity[]` |  `string`  
`items.vpnTunnels[].cipherSuite.phase1.prf[]` |  `string`  
`items.vpnTunnels[].cipherSuite.phase1.dh[]` |  `string`  
`items.vpnTunnels[].cipherSuite.phase2` |  `object`  
`items.vpnTunnels[].cipherSuite.phase2.encryption[]` |  `string`  
`items.vpnTunnels[].cipherSuite.phase2.integrity[]` |  `string`  
`items.vpnTunnels[].cipherSuite.phase2.pfs[]` |  `string`  
`items.vpnTunnels[].params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`items.vpnTunnels[].params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as resource manager tags. The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid. * Inconsistent format is not supported. For instance: {"tagKeys/333" : "tagValues/444", "123/env" : "prod"} is invalid.  
`items.warning` |  `object` Informational warning which replaces the list of addresses when the list is empty.  
`items.warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`items.warning.message` |  `string` Output only. A human-readable description of the warning code.  
`items.warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`items.warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`items.warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`unreachables[]` |  `string` Output only. Unreachable resources.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.vpnTunnels.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
