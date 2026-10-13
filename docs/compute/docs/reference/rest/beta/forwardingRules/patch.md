---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/forwardingRules/patch/
title: Method: forwardingRules.patch \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:59.925748+00:00
---

# Method: forwardingRules.patch  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/forwardingRules/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: forwardingRules.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
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



Updates the specified forwarding rule with the data included in the request. This method supports [PATCH](https://tools.ietf.org/html/rfc5789) semantics and uses the [JSON merge patch](https://tools.ietf.org/html/rfc7386) format and processing rules. Currently, you can only patch the networkTier field.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`PATCH https://compute.googleapis.com/compute/beta/projects/{project}/regions/{region}/forwardingRules/{forwardingRule}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region scoping this request.  
`forwardingRule` |  `string` Name of the ForwardingRule resource to patch.  
  
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
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "region": string,
      "IPAddress": string,
      "IPAddresses": [
        string
      ],
      "IPProtocol": enum,
      "portRange": string,
      "ports": [
        string
      ],
      "target": string,
      "selfLink": string,
      "selfLinkWithId": string,
      "loadBalancingScheme": enum,
      "subnetwork": string,
      "network": string,
      "backendService": string,
      "serviceDirectoryRegistrations": [
        {
          "namespace": string,
          "service": string,
          "serviceDirectoryRegion": string
        }
      ],
      "serviceLabel": string,
      "serviceName": string,
      "networkTier": enum,
      "labels": {
        string: string,
        ...
      },
      "labelFingerprint": string,
      "attachedExtensions": [
        {
          "reference": string
        }
      ],
      "ipVersion": enum,
      "fingerprint": string,
      "allPorts": boolean,
      "allowGlobalAccess": boolean,
      "metadataFilters": [
        {
          "filterMatchCriteria": enum,
          "filterLabels": [
            {
              "name": string,
              "value": string
            }
          ]
        }
      ],
      "isMirroringCollector": boolean,
      "sourceIpRanges": [
        string
      ],
      "pscConnectionId": string,
      "pscConnectionStatus": enum,
      "baseForwardingRule": string,
      "allowPscGlobalAccess": boolean,
      "noAutomateDnsZone": boolean,
      "ipCollection": string,
      "externalManagedBackendBucketMigrationState": enum,
      "externalManagedBackendBucketMigrationTestingPercentage": number,
      "availabilityGroup": enum,
      "childForwardingRules": [
        string
      ],
      "parentForwardingRule": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#forwardingRule` for forwarding rule resources.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.For Private Service Connect forwarding rules that forward traffic to Google APIs, the forwarding rule name must be a 1-20 characters string with lowercase letters and numbers and must start with a letter.For global external Passthrough Network Load Balancer forwarding rules, the forwarding rule name must be 1-43 characters long. For each global external Passthrough Network Load Balancer forwarding rule (a parent forwarding rule) that you create, Google Cloud generates two output-only child forwarding rules that are named by concatenating the parent forwarding rule name with the `-ag0` and `-ag1` suffixes, respectively. Refer to the `availabilityGroup` field for further details.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`region` |  `string` Output only. URL of the region where the regional forwarding rule resides. This field is not applicable to global forwarding rules. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`IPAddress` |  `string` IP address for which this forwarding rule accepts traffic. When a client sends traffic to this IP address, the forwarding rule directs the traffic to the referenced `target` or `backendService`. While creating a forwarding rule, specifying an `IPAddress` is required under the following circumstances:

  * When the `target` is set to `targetGrpcProxy` and `validateForProxyless` is set to `true`, the `IPAddress` should be set to `0.0.0.0`.
  * When the `target` is a Private Service Connect Google APIs bundle, you must specify an `IPAddress`.

Otherwise, you can optionally specify an IP address that references an existing static (reserved) IP address resource. When omitted, Google Cloud assigns an ephemeral IP address.Use one of the following formats to specify an IP address while creating a forwarding rule:

  * IP address number, as in `100.1.2.3`
  * IPv6 address range, as in `2600:1234::/96`
  * Full resource URL, as in `<https://www.googleapis.com/compute/v1/projects/>projectId/regions/region/addresses/address-name`
  * Partial URL or by name, as in: 
    * `projects/projectId/regions/region/addresses/address-name`
    * `regions/region/addresses/address-name`
    * `global/addresses/address-name`
    * `address-name`

The IP address can only be set at creation. Once set, it cannot be updated.The forwarding rule's `target` or `backendService`, and in most cases, also the `loadBalancingScheme`, determine the type of IP address that you can use. For detailed information, see [IP address specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications).When reading an `IPAddress`, the API always returns the IP address number.When creating a global external Passthrough Network Load Balancer forwarding rule (a parent forwarding rule), you must use the `IPAddresses` field, but the Google Cloud generated child forwarding rules set the `IPAddress` field instead. Refer to the `availabilityGroup` field for further details.  
`IPAddresses[]` |  `string` IP addresses for which this forwarding rule accepts traffic. All IP addresses must have the same IP version, IPv4 or IPv6. When a client sends traffic that matches one of the specified IP addresses, protocol and ports, the forwarding rule directs the traffic to the referenced `backendService`. All IP addresses are served by the same set of backends, and they share the target capacities specified in the backend service fairly.Global external Passthrough Network Load Balancer requires two IP addresses for each forwarding rule to provide high availability when both IP addresses are used to serve client requests. The two IP addresses must come from global IP pools that belong to two distinct `Availability Groups`, represented by the purpose `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0` and `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1`. The `IPAddresses` field specifies zero, one, or two IP addresses: 

  * If omitted, Google Cloud assigns two ephemeral IP addresses, one from each Availability Group.
  * If you specify one IP address that references an existing static IP address resource from one Availability Group, Google Cloud assigns an ephemeral IP address from the other Availability Group.
  * If you specify two IP addresses that reference existing static IP address resources, they are required to be from different Availability Groups.

For global external Passthrough Network Load Balancer, each IP address can be one of the following: 

  * A static or ephemeral IPv4 address from a Google-owned IP pool.
  * A static IPv4 address from a global public delegated prefix.
  * A static or ephemeral IPv6 /96 prefix from a Google-owned IP pool.

For global external Passthrough Network Load Balancer, the two IP addresses can be of different types. One IP address can be from a BYOIP prefix while the other is from a Google-owned IP pool. One IP address can be static while the other is ephemeral. However, both IP addresses must have the same IP version, IPv4 or IPv6.The IP addresses can only be set at creation and cannot be updated.When creating a global external Passthrough Network Load Balancer forwarding rule (a parent forwarding rule), you must use the `IPAddresses` field, but the Google Cloud-generated child forwarding rules set the `IPAddress` field instead. Refer to the `availabilityGroup` field for further details.Refer to the `IPAddress` field for the formats that can be used to specify IP addresses while creating a forwarding rule.Because Passthrough Network Load Balancers do not terminate or translate traffic, the backend stack types must be compatible with the forwarding rule IP version: 

  * If the forwarding rule IP version is IPv4, backends should be configured as dual-stack or IPv4-only.
  * If the forwarding rule IP version is IPv6, backends should be configured as dual-stack or IPv6-only.

  
`IPProtocol` |  `enum` The IP protocol to which this rule applies.For protocol forwarding, valid options are `TCP`, `UDP`, `ESP`, `AH`, `SCTP`, `ICMP` and `L3_DEFAULT`.The valid IP protocols are different for different load balancing products as described in [Load balancing features](https://cloud.google.com/load-balancing/docs/features#protocols_from_the_load_balancer_to_the_backends).  
`portRange` |  `string` The `ports`, `portRange`, and `allPorts` fields are mutually exclusive. Only packets addressed to ports in the specified range will be forwarded to the backends configured with this forwarding rule.The `portRange` field has the following limitations: 

  * It requires that the forwarding rule `IPProtocol` be TCP, UDP, or SCTP, and
  * It's applicable only to the following products: external passthrough Network Load Balancers, internal and external proxy Network Load Balancers, internal and external Application Load Balancers, external protocol forwarding, and Classic VPN.
  * Some products have restrictions on what ports can be used. See [ port specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications) for details.

For external forwarding rules, two or more forwarding rules cannot use the same `[IPAddress, IPProtocol]` pair (specified in `IPAddress`, `IPAddresses`, `IPProtocol` fields) if they have overlapping `portRange`s.For internal forwarding rules within the same VPC network, two or more forwarding rules cannot use the same `[IPAddress, IPProtocol]` pair, and cannot have overlapping `portRange`s.@pattern: \d+(?:-\d+)?  
`ports[]` |  `string` The `ports`, `portRange`, and `allPorts` fields are mutually exclusive. Only packets addressed to ports in the specified range will be forwarded to the backends configured with this forwarding rule.The `ports` field has the following limitations: 

  * It requires that the forwarding rule `IPProtocol` be TCP, UDP, or SCTP, and
  * It's applicable only to the following products: internal passthrough Network Load Balancers, backend service-based external passthrough Network Load Balancers, and internal protocol forwarding.
  * You can specify a list of up to five ports by number, separated by commas. The ports can be contiguous or discontiguous.

For external forwarding rules, two or more forwarding rules cannot use the same `[IPAddress, IPProtocol]` pair (specified in `IPAddress`, `IPAddresses`, `IPProtocol` fields) if they share at least one port number.For internal forwarding rules within the same VPC network, two or more forwarding rules cannot use the same `[IPAddress, IPProtocol]` pair if they share at least one port number.@pattern: \d+(?:-\d+)?  
`target` |  `string` The URL of the target resource to receive the matched traffic. For regional forwarding rules, this target must be in the same region as the forwarding rule. For global forwarding rules, this target must be a global load balancing resource.The forwarded traffic must be of a type appropriate to the target object. 

  * For load balancers, see the "Target" column in [Port specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications).
  * For Private Service Connect forwarding rules that forward traffic to Google APIs, provide the name of a supported Google API bundle: 
    * `vpc-sc` \- [ APIs that support VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/supported-products). 
    * `all-apis` \- [All supported Google APIs](https://cloud.google.com/vpc/docs/private-service-connect#supported-apis). 
  * For Private Service Connect forwarding rules that forward traffic to managed services, the target must be a service attachment. The target is not mutable once set as a service attachment. 

The following load balancers cannot set the target field (they should set the backendService field instead): 

  * Internal passthrough Network Load Balancers
  * Backend service-based regional external passthrough Network Load Balancers
  * Global external passthrough Network Load Balancers

  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`loadBalancingScheme` |  `enum` Specifies the forwarding rule type.For more information, refer to [ Forwarding rule product and scheme table](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications).  
`subnetwork` |  `string` This field identifies the subnetwork that the load balanced IP should belong to for this forwarding rule, used with internal load balancers and external passthrough Network Load Balancers with IPv6.If the network specified is in auto subnet mode, this field is optional. However, a subnetwork must be specified if the network is in custom subnet mode or when creating external forwarding rule with IPv6.  
`network` |  `string` This field is not used for global external load balancing.For internal passthrough Network Load Balancers, this field identifies the network that the load balanced IP should belong to for this forwarding rule. If the subnetwork is specified, the network of the subnetwork will be used. If neither subnetwork nor this field is specified, the default network will be used.For Private Service Connect forwarding rules that forward traffic to Google APIs, a network must be provided.  
`backendService` |  `string` Identifies the backend service to which the forwarding rule sends traffic.It is a required field for the following load balancers: 

  * Internal passthrough Network Load Balancers
  * Backend service-based regional external passthrough Network Load Balancers
  * Global external passthrough Network Load Balancers

It cannot be set by other load balancer types and protocol forwarding rules.  
`serviceDirectoryRegistrations[]` |  `object` Service Directory resources to register this forwarding rule with. Currently, only supports a single Service Directory resource.  
`serviceDirectoryRegistrations[].namespace` |  `string` Service Directory namespace to register the forwarding rule under.  
`serviceDirectoryRegistrations[].service` |  `string` Service Directory service to register the forwarding rule under.  
`serviceDirectoryRegistrations[].serviceDirectoryRegion` |  `string` [Optional] Service Directory region to register this global forwarding rule under. Default to "us-central1". Only used for PSC for Google APIs. All PSC for Google APIs forwarding rules on the same network should use the same Service Directory region.  
`serviceLabel` |  `string` An optional prefix to the service name for this forwarding rule. If specified, the prefix is the first label of the fully qualified service name.The label must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the label must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.This field is only used for internal load balancing.  
`serviceName` |  `string` Output only. The internal fully qualified service name for this forwarding rule.This field is only used for internal load balancing.  
`networkTier` |  `enum` This signifies the networking tier used for configuring this load balancer and can only take the following values: `PREMIUM`, `STANDARD`.For regional ForwardingRule, the valid values are `PREMIUM` and `STANDARD`. For GlobalForwardingRule, the valid value is `PREMIUM`.If this field is not specified, it is assumed to be `PREMIUM`. If `IPAddress` is specified, this value must be equal to the networkTier of the Address.  
`labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty.  
`labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this resource, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a ForwardingRule.A base64-encoded string.  
`attachedExtensions[]` |  `object` Output only.. The extensions that are attached to this ForwardingRule.  
`attachedExtensions[].reference` |  `string` Output only. The resource name.  
`ipVersion` |  `enum` The IP Version that will be used by this forwarding rule. Valid options are `IPV4` or `IPV6`.  
`fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a ForwardingRule. Include the fingerprint in patch request to ensure that you do not overwrite changes that were applied from another concurrent request.To see the latest fingerprint, make a `get()` request to retrieve a ForwardingRule.A base64-encoded string.  
`allPorts` |  `boolean` The `ports`, `portRange`, and `allPorts` fields are mutually exclusive. Only packets addressed to ports in the specified range will be forwarded to the backends configured with this forwarding rule.The `allPorts` field has the following limitations: 

  * It requires that the forwarding rule `IPProtocol` be TCP, UDP, SCTP, or L3_DEFAULT.
  * It's applicable only to the following products: internal passthrough Network Load Balancers, backend service-based external passthrough Network Load Balancers, and internal and external protocol forwarding.
  * Set this field to true to allow packets addressed to any port or packets lacking destination port information (for example, UDP fragments after the first fragment) to be forwarded to the backends configured with this forwarding rule. The L3_DEFAULT protocol requires `allPorts` be set to true.

  
`allowGlobalAccess` |  `boolean` If set to true, clients can access the internal passthrough Network Load Balancers, the regional internal Application Load Balancer, and the regional internal proxy Network Load Balancer from all regions. If false, only allows access from the local region the load balancer is located at. Note that for INTERNAL_MANAGED forwarding rules, this field cannot be changed after the forwarding rule is created.  
`metadataFilters[]` |  `object` Opaque filter criteria used by load balancer to restrict routing configuration to a limited set of [xDS](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol) compliant clients. In their xDS requests to load balancer, xDS clients present [node metadata](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/base.proto.html#config-core-v3-node). When there is a match, the relevant configuration is made available to those proxies. Otherwise, all the resources (e.g. `TargetHttpProxy`, `UrlMap`) referenced by the `ForwardingRule` are not visible to those proxies. For each `metadataFilter` in this list, if its `filterMatchCriteria` is set to MATCH_ANY, at least one of the `filterLabel`s must match the corresponding label provided in the metadata. If its `filterMatchCriteria` is set to MATCH_ALL, then all of its `filterLabel`s must match with corresponding labels provided in the metadata. If multiple `metadataFilters` are specified, all of them need to be satisfied in order to be considered a match. `metadataFilters` specified here will be applifed before those specified in the `UrlMap` that this `ForwardingRule` references. `metadataFilters` only applies to Loadbalancers that have their `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`.  
`metadataFilters[].filterMatchCriteria` |  `enum` Specifies how individual filter label matches within the list of `filterLabels` and contributes toward the overall `metadataFilter` match.  Supported values are: 

  * `MATCH_ANY`: at least one of the `filterLabels` must have a matching label in the provided metadata.
  * `MATCH_ALL`: all `filterLabels` must have matching labels in the provided metadata.

  
`metadataFilters[].filterLabels[]` |  `object` The list of label value pairs that must match labels in the provided metadata based on `filterMatchCriteria` This list must not be empty and can have at the most 64 entries.  
`metadataFilters[].filterLabels[].name` |  `string` Name of metadata label.  The name can have a maximum length of 1024 characters and must be at least 1 character long.  
`metadataFilters[].filterLabels[].value` |  `string` The value of the label must match the specified value. value can have a maximum length of 1024 characters.  
`isMirroringCollector` |  `boolean` Indicates whether or not this load balancer can be used as a collector for packet mirroring. To prevent mirroring loops, instances behind this load balancer will not have their traffic mirrored even if a `PacketMirroring` rule applies to them. This can only be set to true for load balancers that have their `loadBalancingScheme` set to `INTERNAL`.  
`sourceIpRanges[]` |  `string` If not empty, this forwarding rule will only forward the traffic when the source IP address matches one of the IP addresses or CIDR ranges set here. Note that a forwarding rule can only have up to 64 source IP ranges, and this field can only be used with a regional forwarding rule whose scheme is `EXTERNAL`. Each `sourceIpRange` entry should be either an IP address (for example, 1.2.3.4) or a CIDR range (for example, 1.2.3.0/24).  
`pscConnectionId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The PSC connection id of the PSC forwarding rule.  
`pscConnectionStatus` |  `enum`  
`baseForwardingRule` |  `string` Output only. The URL for the corresponding base forwarding rule. By base forwarding rule, we mean the forwarding rule that has the same IP address, protocol, and port settings with the current forwarding rule, but without sourceIPRanges specified. Always empty if the current forwarding rule does not have sourceIPRanges specified.  
`allowPscGlobalAccess` |  `boolean` This is used in PSC consumer ForwardingRule to control whether the PSC endpoint can be accessed from another region.  
`noAutomateDnsZone` |  `boolean` This is used in PSC consumer ForwardingRule to control whether it should try to auto-generate a DNS zone or not. Non-PSC forwarding rules do not use this field. Once set, this field is not mutable.  
`ipCollection` |  `string` Resource reference of a `PublicDelegatedPrefix`. The PDP must be a sub-PDP in EXTERNAL_IPV6_FORWARDING_RULE_CREATION mode.Use one of the following formats to specify a sub-PDP when creating an IPv6 NetLB forwarding rule using BYOIP: Full resource URL, as in `<https://www.googleapis.com/compute/v1/projects/>projectId/regions/region/publicDelegatedPrefixes/sub-pdp-name` Partial URL, as in: 

  * `projects/projectId/regions/region/publicDelegatedPrefixes/sub-pdp-name`
  * `regions/region/publicDelegatedPrefixes/sub-pdp-name`

  
`externalManagedBackendBucketMigrationState` |  `enum` Specifies the canary migration state for the backend buckets attached to this forwarding rule. Possible values are PREPARE, TEST_BY_PERCENTAGE, and TEST_ALL_TRAFFIC.To begin the migration from EXTERNAL to EXTERNAL_MANAGED, the state must be changed to PREPARE. The state must be changed to TEST_ALL_TRAFFIC before the loadBalancingScheme can be changed to EXTERNAL_MANAGED. Optionally, the TEST_BY_PERCENTAGE state can be used to migrate traffic to backend buckets attached to this forwarding rule by percentage using externalManagedBackendBucketMigrationTestingPercentage.Rolling back a migration requires the states to be set in reverse order. So changing the scheme from EXTERNAL_MANAGED to EXTERNAL requires the state to be set to TEST_ALL_TRAFFIC at the same time. Optionally, the TEST_BY_PERCENTAGE state can be used to migrate some traffic back to EXTERNAL or PREPARE can be used to migrate all traffic back to EXTERNAL.  
`externalManagedBackendBucketMigrationTestingPercentage` |  `number` Determines the fraction of requests to backend buckets that should be processed by the global external Application Load Balancer.The value of this field must be in the range [0, 100].This value can only be set if the loadBalancingScheme in the BackendService is set to EXTERNAL (when using the classic Application Load Balancer) and the migration state is TEST_BY_PERCENTAGE.  
`availabilityGroup` |  `enum` Output only. Specifies the load balancing availability group, one of the two that collectively provide high availability.Specifies the availability group of the forwarding rule. This field is for use by global external passthrough load balancers (load balancing scheme `EXTERNAL_PASSTHROUGH`) and is set for the child forwarding rules only. The possible values are: 

  * `AVAILABILITY_GROUP0`: Set for the child forwarding rule that is programmed on the `AVAILABILITY_GROUP0` load balancing stack. The child forwarding rule has the same IP protocol, port, and backend service settings as the parent forwarding rule, but has only one of the two IP addresses of the parent forwarding rule, the one with the purpose `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0`.
  * `AVAILABILITY_GROUP1`: Set for the child forwarding rule that is programmed on the `AVAILABILITY_GROUP1` load balancing stack. The child forwarding rule has the same IP protocol, port and backend service settings as the parent forwarding rule, but has only one of the two IP addresses of the parent forwarding rule, the one with the purpose `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1`.

For each global external Passthrough Network Load Balancer forwarding rule (a parent forwarding rule) that you create, Google Cloud generates two output-only child forwarding rules, one for `AVAILABILITY_GROUP0` and one for `AVAILABILITY_GROUP1`.  
`childForwardingRules[]` |  `string` Output only. The resource URLs for the child forwarding rules.Applicable only to the parent forwarding rule of global external passthrough load balancers. This field contains the list of child forwarding rule URLs associated with the parent forwarding rule: one for each availability group. AVAILABILITY_GROUP0 will be the first element, and AVAILABILITY_GROUP1 will be the second element. Refer to the `availabilityGroup` field for further details. It cannot be set by any other forwarding rules.  
`parentForwardingRule` |  `string` Output only. The resource URL for the parent forwarding rule.Applicable only to the child forwarding rules of global external passthrough load balancers. This field contains the URL of the parent forwarding rule.  
  
### Response body

Represents an Operation resource.

Google Compute Engine has three Operation resources:

  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalOperations)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionOperations)
  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/beta/zoneOperations)



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

  * `compute.forwardingRules.pscUpdate`
  * `compute.forwardingRules.update`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
