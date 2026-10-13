---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/subnetworks/list/
title: Method: subnetworks.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:40.117901+00:00
---

# Method: subnetworks.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/subnetworks/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: subnetworks.list Stay organized with collections  Save and categorize content based on your preferences. 

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
        * JSON representation
        * JSON representation
        * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Retrieves a list of subnetworks available to the specified project.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region scoping this request.  
  
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
`views[]` |  `enum` Defines the extra views returned back in the subnetwork resource. Supported values: 

  * `WITH_UTILIZATION`: Utilization data is included in the response. 

  
  
### Request body

The request body must be empty.

### Response body

Contains a list of Subnetwork resources.

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
          "network": string,
          "ipCidrRange": string,
          "reservedInternalRange": string,
          "gatewayAddress": string,
          "region": string,
          "selfLink": string,
          "privateIpGoogleAccess": boolean,
          "secondaryIpRanges": [
            {
              "rangeName": string,
              "ipCidrRange": string,
              "reservedInternalRange": string,
              "ipVersion": enum,
              "ipCollection": string
            }
          ],
          "fingerprint": string,
          "allowSubnetCidrRoutesOverlap": boolean,
          "enableFlowLogs": boolean,
          "privateIpv6GoogleAccess": enum,
          "ipv6CidrRange": string,
          "externalIpv6Prefix": string,
          "internalIpv6Prefix": string,
          "purpose": enum,
          "role": enum,
          "state": enum,
          "logConfig": {
            "enable": boolean,
            "aggregationInterval": enum,
            "flowSampling": number,
            "metadata": enum,
            "metadataFields": [
              string
            ],
            "filterExpr": string
          },
          "stackType": enum,
          "ipv6AccessType": enum,
          "ipCollection": string,
          "ipv6GceEndpoint": enum,
          "params": {
            "resourceManagerTags": {
              string: string,
              ...
            }
          },
          "utilizationDetails": {
            "ipv4Utilizations": [
              {
                "rangeName": string,
                "totalAllocatedIp": string,
                "totalFreeIp": string
              }
            ],
            "externalIpv6InstanceUtilization": {
              "totalAllocatedIp": {
                "high": string,
                "low": string
              },
              "totalFreeIp": {
                "high": string,
                "low": string
              }
            },
            "externalIpv6LbUtilization": {
              "totalAllocatedIp": {
                "high": string,
                "low": string
              },
              "totalFreeIp": {
                "high": string,
                "low": string
              }
            },
            "internalIpv6Utilization": {
              "totalAllocatedIp": {
                "high": string,
                "low": string
              },
              "totalFreeIp": {
                "high": string,
                "low": string
              }
            }
          },
          "systemReservedInternalIpv6Ranges": [
            string
          ],
          "systemReservedExternalIpv6Ranges": [
            string
          ],
          "resolveSubnetMask": enum
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
`kind` |  `string` Output only. Type of resource. Always `compute#subnetworkList` for lists of subnetworks.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of Subnetwork resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#subnetwork` for Subnetwork resources.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time.  
`items[].network` |  `string` The URL of the network to which this subnetwork belongs, provided by the client when initially creating the subnetwork. This field can be set only at resource creation time.  
`items[].ipCidrRange` |  `string` The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, `10.0.0.0/8` or `100.64.0.0/10`. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. This field is set at resource creation time. The range can be any range listed in the [Valid ranges](https://cloud.google.com/vpc/docs/vpc#valid-ranges) list. The range can be expanded after creation using `expandIpCidrRange`.  
`items[].reservedInternalRange` |  `string` The URL of the reserved internal range.  
`items[].gatewayAddress` |  `string` Output only. The gateway address for default routes to reach destination addresses outside this subnetwork.  
`items[].region` |  `string` URL of the region where the Subnetwork resides. This field can be set only at resource creation time.  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].privateIpGoogleAccess` |  `boolean` Whether the VMs in this subnet can access Google services without assigned external IP addresses. This field can be both set at resource creation time and updated using `setPrivateIpGoogleAccess`.  
`items[].secondaryIpRanges[]` |  `object` An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. This field can be updated with a `patch` request. Supports both IPv4 and IPv6 ranges.  
`items[].secondaryIpRanges[].rangeName` |  `string` The name associated with this subnetwork secondary range, used when adding an alias IP/IPv6 range to a VM instance. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). The name must be unique within the subnetwork.  
`items[].secondaryIpRanges[].ipCidrRange` |  `string` The range of IP addresses belonging to this subnetwork secondary range. Provide this property when you create the subnetwork. Ranges must be unique and non-overlapping with all primary and secondary IP ranges within a network. Both IPv4 and IPv6 ranges are supported. For IPv4, the range can be any range listed in the [Valid ranges](https://cloud.google.com/vpc/docs/vpc#valid-ranges) list.For IPv6: The range must have a /64 prefix length. The range must be omitted, for auto-allocation from Google-defined ULA IPv6 range. For BYOGUA internal IPv6 secondary range, the range may be specified along with the `ipCollection` field. If an `ipCollection` is specified, the requested ipCidrRange must lie within the range of the PDP referenced by the `ipCollection` field for allocation. If `ipCollection` field is specified, but ipCidrRange is not, the range is auto-allocated from the PDP referenced by the `ipCollection` field.  
`items[].secondaryIpRanges[].reservedInternalRange` |  `string` The URL of the reserved internal range. Only IPv4 is supported.  
`items[].secondaryIpRanges[].ipVersion` |  `enum`  
`items[].secondaryIpRanges[].ipCollection` |  `string` Reference to a Public Delegated Prefix (PDP) for BYOIP. This field should be specified for configuring BYOGUA internal IPv6 secondary range. When specified along with the ipCidrRange, the ipCidrRange must lie within the PDP referenced by the `ipCollection` field. When specified without the ipCidrRange, the range is auto-allocated from the PDP referenced by the `ipCollection` field.  
`items[].fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a `Subnetwork`. An up-to-date fingerprint must be provided in order to update the `Subnetwork`, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a Subnetwork.A base64-encoded string.  
`items[].allowSubnetCidrRoutesOverlap` |  `boolean` Whether this subnetwork's ranges can conflict with existing custom routes. Setting this to true allows this subnetwork's primary and secondary ranges to overlap with (and contain) custom routes that have already been configured on the corresponding network.For example if a static route has range 10.1.0.0/16, a subnet range 10.0.0.0/8 could only be created if allowConflictingRoutes=true.Overlapping is only allowed on subnetwork operations; routes whose ranges conflict with this subnetwork's ranges won't be allowed unless route.allow_conflicting_subnetworks is set to true.Typically packets destined to IPs within the subnetwork (which may contain private/sensitive data) are prevented from leaving the virtual network. Setting this field to true will disable this feature.The default value is false and applies to all existing subnetworks and automatically created subnetworks.  
`items[].enableFlowLogs` |  `boolean` Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in `get` listings. If not set the default behavior is determined by the org policy, if there is no org policy specified, then it will default to disabled. This field isn't supported if the subnet `purpose` field is set to `REGIONAL_MANAGED_PROXY`. It is recommended to use `logConfig.enable` field instead.  
`items[].privateIpv6GoogleAccess` |  `enum` This field is for internal use.This field can be both set at resource creation time and updated using `patch`.  
`items[].ipv6CidrRange` |  `string` Output only. This field is for internal use.  
`items[].externalIpv6Prefix` |  `string` The external IPv6 address range that is owned by this subnetwork.  
`items[].internalIpv6Prefix` |  `string` The internal IPv6 address range that is owned by this subnetwork.  
`items[].purpose` |  `enum`  
`items[].role` |  `enum` The role of subnetwork. Currently, this field is only used when purpose is set to `GLOBAL_MANAGED_PROXY` or `REGIONAL_MANAGED_PROXY`. The value can be set to `ACTIVE` or `BACKUP`. An `ACTIVE` subnetwork is one that is currently being used for Envoy-based load balancers in a region. A `BACKUP` subnetwork is one that is ready to be promoted to `ACTIVE` or is currently draining. This field can be updated with a `patch` request.  
`items[].state` |  `enum` Output only. The state of the subnetwork, which can be one of the following values: `READY`: Subnetwork is created and ready to use `DRAINING`: only applicable to subnetworks that have the purpose set to `INTERNAL_HTTPS_LOAD_BALANCER` and indicates that connections to the load balancer are being drained. A subnetwork that is draining cannot be used or modified until it reaches a status of `READY`  
`items[].logConfig` |  `object` This field denotes the VPC flow logging options for this subnetwork. If logging is enabled, logs are exported to Cloud Logging.  
`items[].logConfig.enable` |  `boolean` Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in `get` listings. If not set the default behavior is determined by the org policy, if there is no org policy specified, then it will default to disabled. Flow logging isn't supported if the subnet `purpose` field is set to `REGIONAL_MANAGED_PROXY`.  
`items[].logConfig.aggregationInterval` |  `enum` Can only be specified if VPC flow logging for this subnetwork is enabled. Toggles the aggregation interval for collecting flow logs. Increasing the interval time will reduce the amount of generated flow logs for long lasting connections. Default is an interval of 5 seconds per connection.  
`items[].logConfig.flowSampling` |  `number` Can only be specified if VPC flow logging for this subnetwork is enabled. The value of the field must be in [0, 1]. Set the sampling rate of VPC flow logs within the subnetwork where 1.0 means all collected logs are reported and 0.0 means no logs are reported. Default is 0.5 unless otherwise specified by the org policy, which means half of all collected logs are reported.  
`items[].logConfig.metadata` |  `enum` Can only be specified if VPC flow logs for this subnetwork is enabled. Configures whether all, none or a subset of metadata fields should be added to the reported VPC flow logs. Default is `EXCLUDE_ALL_METADATA`.  
`items[].logConfig.metadataFields[]` |  `string` Can only be specified if VPC flow logs for this subnetwork is enabled and "metadata" was set to CUSTOM_METADATA.  
`items[].logConfig.filterExpr` |  `string` Can only be specified if VPC flow logs for this subnetwork is enabled. The filter expression is used to define which VPC flow logs should be exported to Cloud Logging.  
`items[].stackType` |  `enum` The stack type for the subnet. If set to `IPV4_ONLY`, new VMs in the subnet are assigned IPv4 addresses only. If set to `IPV4_IPV6`, new VMs in the subnet can be assigned both IPv4 and IPv6 addresses. If not specified, `IPV4_ONLY` is used.This field can be both set at resource creation time and updated using `patch`.  
`items[].ipv6AccessType` |  `enum` The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack.  
`items[].ipCollection` |  `string` Reference to the source of IP, like a `PublicDelegatedPrefix` (PDP) for BYOIP. The PDP must be a sub-PDP in EXTERNAL_IPV6_SUBNETWORK_CREATION or INTERNAL_IPV6_SUBNETWORK_CREATION mode.Use one of the following formats to specify a sub-PDP when creating a dual stack or IPv6-only subnetwork with external access using BYOIP: 

  * Full resource URL, as in `<https://www.googleapis.com/compute/v1/projects/>projectId/regions/region/publicDelegatedPrefixes/sub-pdp-name`
  * Partial URL, as in 
    * projects/projectId/regions/region/publicDelegatedPrefixes/sub-pdp-name
    * regions/region/publicDelegatedPrefixes/sub-pdp-name

  
`items[].ipv6GceEndpoint` |  `enum` Output only. Possible endpoints of this subnetwork. It can be one of the following: 

  * `VM_ONLY`: The subnetwork can be used for creating instances and IPv6 addresses with VM endpoint type. Such a subnetwork gets external IPv6 ranges from a public delegated prefix and cannot be used to create NetLb. 
  * `VM_AND_FR`: The subnetwork can be used for creating both VM instances and Forwarding Rules. It can also be used to reserve IPv6 addresses with both VM and FR endpoint types. Such a subnetwork gets its IPv6 range from Google IP Pool directly. 

  
`items[].params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`items[].params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid.  
`items[].utilizationDetails` |  `object` Output only. The current IP utilization of all subnetwork ranges. Contains the total number of allocated and free IPs in each range.  
`items[].utilizationDetails.ipv4Utilizations[]` |  `object` Utilizations of all IPV4 IP ranges. For primary ranges, the range name will be empty.  
`items[].utilizationDetails.ipv4Utilizations[].rangeName` |  `string` Will be set for secondary range. Empty for primary IPv4 range.  
`items[].utilizationDetails.ipv4Utilizations[].totalAllocatedIp` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.ipv4Utilizations[].totalFreeIp` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.externalIpv6InstanceUtilization` |  `object` Utilizations of external IPV6 IP range.  
`items[].utilizationDetails.externalIpv6InstanceUtilization.totalAllocatedIp` |  `object`  
`items[].utilizationDetails.externalIpv6InstanceUtilization.totalAllocatedIp.high` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.externalIpv6InstanceUtilization.totalAllocatedIp.low` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.externalIpv6InstanceUtilization.totalFreeIp` |  `object`  
`items[].utilizationDetails.externalIpv6InstanceUtilization.totalFreeIp.high` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.externalIpv6InstanceUtilization.totalFreeIp.low` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.externalIpv6LbUtilization` |  `object` Utilizations of external IPV6 IP range for NetLB.  
`items[].utilizationDetails.externalIpv6LbUtilization.totalAllocatedIp` |  `object`  
`items[].utilizationDetails.externalIpv6LbUtilization.totalAllocatedIp.high` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.externalIpv6LbUtilization.totalAllocatedIp.low` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.externalIpv6LbUtilization.totalFreeIp` |  `object`  
`items[].utilizationDetails.externalIpv6LbUtilization.totalFreeIp.high` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.externalIpv6LbUtilization.totalFreeIp.low` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.internalIpv6Utilization` |  `object` Utilizations of internal IPV6 IP range.  
`items[].utilizationDetails.internalIpv6Utilization.totalAllocatedIp` |  `object`  
`items[].utilizationDetails.internalIpv6Utilization.totalAllocatedIp.high` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.internalIpv6Utilization.totalAllocatedIp.low` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.internalIpv6Utilization.totalFreeIp` |  `object`  
`items[].utilizationDetails.internalIpv6Utilization.totalFreeIp.high` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].utilizationDetails.internalIpv6Utilization.totalFreeIp.low` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].systemReservedInternalIpv6Ranges[]` |  `string` Output only. The array of internal IPv6 network ranges reserved from the subnetwork's internal IPv6 range for system use.  
`items[].systemReservedExternalIpv6Ranges[]` |  `string` Output only. The array of external IPv6 network ranges reserved from the subnetwork's external IPv6 range for system use.  
`items[].resolveSubnetMask` |  `enum` Configures subnet mask resolution for this subnetwork.  
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

  * `compute.subnetworks.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
