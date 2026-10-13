---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/addresses/list/
title: Method: addresses.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:35.769161+00:00
---

# Method: addresses.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/addresses/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: addresses.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Retrieves a list of addresses contained within the specified region.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/addresses?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region for this request.  
  
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

Contains a list of addresses.

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
          "address": string,
          "prefixLength": integer,
          "status": enum,
          "region": string,
          "selfLink": string,
          "users": [
            string
          ],
          "networkTier": enum,
          "labels": {
            string: string,
            ...
          },
          "labelFingerprint": string,
          "ipVersion": enum,
          "addressType": enum,
          "purpose": enum,
          "subnetwork": string,
          "network": string,
          "ipv6EndpointType": enum,
          "ipCollection": string
        }
      ],
      "nextPageToken": string,
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
      "selfLink": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#addressList` for lists of addresses.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of Address resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#address` for addresses.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.  
`items[].description` |  `string` An optional description of this resource. Provide this field when you create the resource.  
`items[].address` |  `string` The static IP address represented by this resource.  
`items[].prefixLength` |  `integer` The prefix length if the resource represents an IP range.  
`items[].status` |  `enum` Output only. The status of the address, which can be one of `RESERVING`, `RESERVED`, or `IN_USE`. An address that is `RESERVING` is currently in the process of being reserved. A `RESERVED` address is currently reserved and available to use. An `IN_USE` address is currently being used by another resource and is not available.  
`items[].region` |  `string` Output only. The URL of the region where a regional address resides. For regional addresses, you must specify the region as a path parameter in the HTTP request URL. **This field is not applicable to global addresses.**  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].users[]` |  `string` Output only. The URLs of the resources that are using this address.  
`items[].networkTier` |  `enum` This signifies the networking tier used for configuring this address and can only take the following values: `PREMIUM` or `STANDARD`. Internal IP addresses are always Premium Tier; global external IP addresses are always Premium Tier; regional external IP addresses can be either Standard or Premium Tier.If this field is not specified, it is assumed to be `PREMIUM`.  
`items[].labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty.  
`items[].labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this Address, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve an Address.A base64-encoded string.  
`items[].ipVersion` |  `enum` The IP version that will be used by this address. Valid options are `IPV4` or `IPV6`.  
`items[].addressType` |  `enum` The type of address to reserve, either `INTERNAL` or `EXTERNAL`. If unspecified, defaults to `EXTERNAL`.  
`items[].purpose` |  `enum` The purpose of this resource, which can be one of the following values: 

  * `GCE_ENDPOINT` for addresses that are used by VM instances, alias IP ranges, load balancers, and similar resources.
  * `DNS_RESOLVER` for a DNS resolver address in a subnetwork for a Cloud DNS [ inbound forwarder IP addresses](https://cloud.google.com/dns/docs/policies#create-in) (regional internal IP address in a subnet of a VPC network)
  * `VPC_PEERING` for global internal IP addresses used for [ private services access allocated ranges](https://cloud.google.com/vpc/docs/configure-private-services-access#allocating-range).
  * `NAT_AUTO` for the regional external IP addresses used by Cloud NAT when allocating addresses using [ automatic NAT IP address allocation](https://cloud.google.com/nat/docs/ports-and-addresses#addresses).
  * `IPSEC_INTERCONNECT` for addresses created from a private IP range that are reserved for a VLAN attachment in an _HA VPN over Cloud Interconnect_ configuration. These addresses are regional resources.
  * `SHARED_LOADBALANCER_VIP` for an internal IP address that is assigned to multiple internal forwarding rules.
  * `PRIVATE_SERVICE_CONNECT` for a private network address that is used to configure Private Service Connect. Only global internal addresses can use this purpose.
  * `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0` for addresses that can only be assigned to global external Passthrough Network Load Balancer forwarding rules, as an Availability Group 0 address.
  * `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1` for addresses that can only be assigned to global external Passthrough Network Load Balancer forwarding rules, as an Availability Group 1 address.

  
`items[].subnetwork` |  `string` The URL of the subnetwork in which to reserve the address. If an IP address is specified, it must be within the subnetwork's IP range. This field can only be used with `INTERNAL` type with a `GCE_ENDPOINT` or `DNS_RESOLVER` purpose.  
`items[].network` |  `string` The URL of the network in which to reserve the address. This field can only be used with `INTERNAL` type with the `VPC_PEERING` purpose.  
`items[].ipv6EndpointType` |  `enum` The endpoint type of this address, which should be `VM` or `NETLB`. This is used for deciding which type of endpoint this address can be used after the external IPv6 address reservation.  
`items[].ipCollection` |  `string` Reference to the source of IP addresses.It supports the following cases: 

  * Case 1: `PublicDelegatedPrefix` (PDP) for BYOIP external addresses. If an IPv4 PDP is used, the PDP must support enhanced IPv4 allocations. If an IPv6 PDP is used, the PDP must be in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode. 
  * Case 2: `Internal Range` for global internal addresses. 

Use one of the following formats to specify the resource:For a Public Delegated Prefix: 

  * Full resource URL: `<https://www.googleapis.com/compute/v1/projects/>projectId/regions/region/publicDelegatedPrefixes/pdp`
  * Partial URL: 
    * projects/projectId/regions/region/publicDelegatedPrefixes/pdp-name
    * regions/region/publicDelegatedPrefixes/pdp-name

For an Internal Range: 

  * Full URL: `<https://networkconnectivity.googleapis.com/v1/projects/>project/locations/global/internalRanges/internal-range`
  * Partial URL: `projects/project/locations/global/internalRanges/internal-range`

  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.addresses.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
