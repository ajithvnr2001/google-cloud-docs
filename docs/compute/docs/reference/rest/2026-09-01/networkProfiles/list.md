---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/networkProfiles/list/
title: Method: networkProfiles.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:40.137014+00:00
---

# Method: networkProfiles.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/networkProfiles/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: networkProfiles.list Stay organized with collections  Save and categorize content based on your preferences. 

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

Retrieves a list of network profiles available to the specified project.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/networkProfiles?$apiVersion=2026-09-01`

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
  
### Request body

The request body must be empty.

### Response body

Contains a list of network profiles.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
        {
          "kind": string,
          "id": string,
          "creationTimestamp": string,
          "name": string,
          "description": string,
          "selfLink": string,
          "selfLinkWithId": string,
          "location": {
            "scope": enum,
            "name": string
          },
          "profileType": {
            "networkType": enum,
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "rdmaSubtype": enum,
            "vpcSubtype": enum,
            "ullSubtype": enum
            // End of mutually exclusive fields.
          },
          "features": {
            "allowSameNetworkUnicast": enum,
            "unicast": enum,
            "multicast": enum,
            "allowMulticast": enum,
            "allowAutoModeSubnet": enum,
            "allowVpcPeering": enum,
            "allowMultiNicInSameNetwork": enum,
            "allowLoadBalancing": enum,
            "allowStaticRoutes": enum,
            "allowPsc": enum,
            "allowCloudRouter": enum,
            "allowCloudNat": enum,
            "allowVpn": enum,
            "allowInterconnect": enum,
            "allowPacketMirroring": enum,
            "subnetworkPurposes": [
              enum
            ],
            "subnetworkStackTypes": [
              enum
            ],
            "subnetPurposes": [
              enum
            ],
            "subnetStackTypes": [
              enum
            ],
            "allowPrivateGoogleAccess": enum,
            "interfaceTypes": [
              enum
            ],
            "allowClassDFirewalls": enum,
            "allowSubInterfaces": enum,
            "allowExternalIpAccess": enum,
            "addressPurposes": [
              enum
            ],
            "allowAliasIpRanges": enum,
            "allowDefaultNicAttachment": enum,
            "allowNcc": enum,
            "allowIpForwarding": enum,
            "allowNetworkMigration": enum,
            "allowFirewallPolicy": enum,
            "firewallPolicyTypes": [
              enum
            ],
            "allowVpcFirewallRules": enum,
            "allowMultiNicInSameSubnetwork": enum,
            "predefinedNetworkInternalIpv6Range": string,
            "predefinedSubnetworkRanges": [
              {
                "namePrefix": string,
                "ipv6Range": string
              }
            ],
            "allowSubnetworkCreation": enum,
            "allowAddressCreation": enum
          }
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
`kind` |  `string` Output only. Type of resource. Always `compute#networkProfileList` for network profiles.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of NetworkProfile resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#networkProfile` for network profiles.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Output only. Name of the resource.  
`items[].description` |  `string` Output only. An optional description of this resource.  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`items[].location` |  `object` Output only. Location to which the network is restricted.  
`items[].location.scope` |  `enum`  
`items[].location.name` |  `string`  
`items[].profileType` |  `object` Output only. Type of the network profile.  
`items[].profileType.rdmaSubtype` |  `enum`  
`items[].profileType.vpcSubtype` |  `enum`  
`items[].profileType.ullSubtype` |  `enum`  
`items[].profileType.networkType` |  `enum`  
`items[].features` |  `object` Output only. Features supported by the network.  
`items[].features.allowSameNetworkUnicast` |  `enum` Specifies whether unicast within the same network is allowed.  
`items[].features.unicast` |  `enum` Specifies which type of unicast is supported.  
`items[].features.multicast` |  `enum` Specifies which type of multicast is supported.  
`items[].features.allowMulticast` |  `enum` Specifies whether multicast is allowed.  
`items[].features.allowAutoModeSubnet` |  `enum` Specifies whether auto mode subnet creation is allowed.  
`items[].features.allowVpcPeering` |  `enum` Specifies whether VPC peering is allowed.  
`items[].features.allowMultiNicInSameNetwork` |  `enum` Specifies whether multi-nic in the same network is allowed.  
`items[].features.allowLoadBalancing` |  `enum` Specifies whether cloud load balancing is allowed.  
`items[].features.allowStaticRoutes` |  `enum` Specifies whether static route creation is allowed.  
`items[].features.allowPsc` |  `enum` Specifies whether PSC creation is allowed.  
`items[].features.allowCloudRouter` |  `enum` Specifies whether cloud router creation is allowed.  
`items[].features.allowCloudNat` |  `enum` Specifies whether cloud NAT creation is allowed.  
`items[].features.allowVpn` |  `enum` Specifies whether VPN creation is allowed.  
`items[].features.allowInterconnect` |  `enum` Specifies whether Cloud Interconnect creation is allowed.  
`items[].features.allowPacketMirroring` |  `enum` Specifies whether Packet Mirroring 1.0 is supported.  
`items[].features.subnetworkPurposes[]` |  `enum` Output only. Specifies which subnetwork purposes are supported.  
`items[].features.subnetworkStackTypes[]` |  `enum` Output only. Specifies which subnetwork stack types are supported.  
`items[].features.subnetPurposes[]` |  `enum` Specifies which subnetwork purposes are supported.  
`items[].features.subnetStackTypes[]` |  `enum` Specifies which subnetwork stack types are supported.  
`items[].features.allowPrivateGoogleAccess` |  `enum` Specifies whether private Google access is allowed.  
`items[].features.interfaceTypes[]` |  `enum` If set, limits the interface types that the network supports. If empty, all interface types are supported.  
`items[].features.allowClassDFirewalls` |  `enum` Specifies whether firewalls for Class D address ranges are supported.  
`items[].features.allowSubInterfaces` |  `enum` Specifies whether sub interfaces are allowed.  
`items[].features.allowExternalIpAccess` |  `enum` Specifies whether VMs are allowed to have external IP access on network interfaces connected to this VPC.  
`items[].features.addressPurposes[]` |  `enum` Specifies what address purposes are supported. If empty, all address purposes are supported.  
`items[].features.allowAliasIpRanges` |  `enum` Specifies whether alias IP ranges (and secondary address ranges) are allowed.  
`items[].features.allowDefaultNicAttachment` |  `enum` Specifies whether default NIC attachment is allowed.  
`items[].features.allowNcc` |  `enum` Specifies whether NCC is allowed.  
`items[].features.allowIpForwarding` |  `enum` Specifies whether IP forwarding is allowed.  
`items[].features.allowNetworkMigration` |  `enum` Specifies whether VM network migration is allowed.  
`items[].features.allowFirewallPolicy` |  `enum` Specifies whether firewall policy can be attached to the network.  
`items[].features.firewallPolicyTypes[]` |  `enum`  
`items[].features.allowVpcFirewallRules` |  `enum` Specifies whether VPC firewall rules can be created under the network.  
`items[].features.allowMultiNicInSameSubnetwork` |  `enum` Specifies whether multi-nic in the same subnetwork is allowed.  
`items[].features.predefinedNetworkInternalIpv6Range` |  `string` Specifies a predefined internal IPv6 range for the network.  
`items[].features.predefinedSubnetworkRanges[]` |  `object` Predefined subnetwork ranges for the network.  
`items[].features.predefinedSubnetworkRanges[].namePrefix` |  `string` The naming prefix of the predefined subnetwork.  
`items[].features.predefinedSubnetworkRanges[].ipv6Range` |  `string` The IPv6 range of the predefined subnetwork.  
`items[].features.allowSubnetworkCreation` |  `enum` Specifies whether subnetwork creation is allowed.  
`items[].features.allowAddressCreation` |  `enum` Specifies whether address creation is allowed.  
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

  * `compute.networkProfiles.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
