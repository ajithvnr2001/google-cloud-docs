---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules
title: REST Resource: projects.locations.networkPolicies.externalAccessRules \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:08.699541+00:00
---

# REST Resource: projects.locations.networkPolicies.externalAccessRules  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.networkPolicies.externalAccessRules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ExternalAccessRule
    * JSON representation
  * Action
  * IpRange
    * JSON representation
  * State
  * Methods



## Resource: ExternalAccessRule

External access firewall rules for filtering incoming traffic destined to `ExternalAddress` resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "priority": integer,
      "action": enum ([Action](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules#Action)),
      "ipProtocol": string,
      "sourceIpRanges": [
        {
          object ([IpRange](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules#IpRange))
        }
      ],
      "sourcePorts": [
        string
      ],
      "destinationIpRanges": [
        {
          object ([IpRange](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules#IpRange))
        }
      ],
      "destinationPorts": [
        string
      ],
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules#State)),
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of this external access rule. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` User-provided description for this external access rule.  
`priority` |  `integer` External access rule priority, which determines the external access rule to use when multiple rules apply. If multiple rules have the same priority, their ordering is non-deterministic. If specific ordering is required, assign unique priorities to enforce such ordering. The external access rule priority is an integer from 100 to 4096, both inclusive. Lower integers indicate higher precedence. For example, a rule with priority `100` has higher precedence than a rule with priority `101`.  
`action` |  `enum (`[Action](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules#Action)`)` The action that the external access rule performs.  
`ipProtocol` |  `string` The IP protocol to which the external access rule applies. This value can be one of the following three protocol strings (not case-sensitive): `tcp`, `udp`, or `icmp`.  
`sourceIpRanges[]` |  `object (`[IpRange](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules#IpRange)`)` If source ranges are specified, the external access rule applies only to traffic that has a source IP address in these ranges. These ranges can either be expressed in the CIDR format or as an IP address. As only inbound rules are supported, `ExternalAddress` resources cannot be the source IP addresses of an external access rule. To match all source addresses, specify `0.0.0.0/0`.  
`sourcePorts[]` |  `string` A list of source ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all source ports, specify `["0-65535"]`.  
`destinationIpRanges[]` |  `object (`[IpRange](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules#IpRange)`)` If destination ranges are specified, the external access rule applies only to the traffic that has a destination IP address in these ranges. The specified IP addresses must have reserved external IP addresses in the scope of the parent network policy. To match all external IP addresses in the scope of the parent network policy, specify `0.0.0.0/0`. To match a specific external IP address, specify it using the `IpRange.external_address` property.  
`destinationPorts[]` |  `string` A list of destination ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all destination ports, specify `["0-65535"]`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules#State)`)` Output only. The state of the resource.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
  
## Action

Action determines whether the external access rule permits or blocks traffic, subject to the other components of the rule matching the traffic.

Enums  
---  
`ACTION_UNSPECIFIED` | Defaults to allow.  
`ALLOW` | Allows connections that match the other specified components.  
`DENY` | Blocks connections that match the other specified components.  
  
## IpRange

An IP range provided in any one of the supported formats.

JSON representation  
---  
      
    
    {
    
      // Union field ip_range can be only one of the following:
      "ipAddress": string,
      "ipAddressRange": string,
      "externalAddress": string
      // End of list of possible types for union field ip_range.
    }  
  
Fields  
---  
Union field `ip_range`.`ip_range` can be only one of the following:  
`ipAddress` |  `string` A single IP address. For example: `10.0.0.5`.  
`ipAddressRange` |  `string` An IP address range in the CIDR format. For example: `10.0.0.0/24`.  
`externalAddress` |  `string` The name of an `ExternalAddress` resource. The external address must have been reserved in the scope of this external access rule's parent network policy. Provide the external address name in the form of `projects/{project}/locations/{location}/privateClouds/{privateCloud}/externalAddresses/{externalAddress}`. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address`.  
  
## State

Defines possible states of external access firewall rules.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the state is omitted.  
`ACTIVE` | The rule is ready.  
`CREATING` | The rule is being created.  
`UPDATING` | The rule is being updated.  
`DELETING` | The rule is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/create)`

|  Creates a new external access rule in a given network policy.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/delete)`

|  Deletes a single external access rule.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/get)`

|  Gets details of a single external access rule.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/list)`

|  Lists `ExternalAccessRule` resources in the specified network policy.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules/patch)`

|  Updates the parameters of a single external access rule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
