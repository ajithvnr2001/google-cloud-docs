---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes
title: REST Resource: projects.locations.global.policyBasedRoutes \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:02.859854+00:00
---

# REST Resource: projects.locations.global.policyBasedRoutes  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  REST Resource: projects.locations.global.policyBasedRoutes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PolicyBasedRoute
    * JSON representation
  * VirtualMachine
    * JSON representation
  * InterconnectAttachment
    * JSON representation
  * OtherRoutes
  * Filter
    * JSON representation
  * ProtocolVersion
  * Warnings
    * JSON representation
  * Code
  * Methods



## Resource: PolicyBasedRoute

Policy-based routes route L4 network traffic based on not just destination IP address, but also source IP address, protocol, and more. If a policy-based route conflicts with other types of routes, the policy-based route always takes precedence.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "network": string,
      "filter": {
        object ([Filter](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#Filter))
      },
      "priority": integer,
      "warnings": [
        {
          object ([Warnings](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#Warnings))
        }
      ],
      "selfLink": string,
      "kind": string,
    
      // Union field target can be only one of the following:
      "virtualMachine": {
        object ([VirtualMachine](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#VirtualMachine))
      },
      "interconnectAttachment": {
        object ([InterconnectAttachment](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#InterconnectAttachment))
      }
      // End of list of possible types for union field target.
    
      // Union field next_hop can be only one of the following:
      "nextHopIlbIp": string,
      "nextHopOtherRoutes": enum ([OtherRoutes](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#OtherRoutes))
      // End of list of possible types for union field next_hop.
    }  
  
Fields  
---  
`name` |  `string` Immutable. A unique name of the resource in the form of `projects/{projectNumber}/locations/global/PolicyBasedRoutes/{policyBasedRouteId}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the policy-based route was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the policy-based route was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` User-defined labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. An optional description of this resource. Provide this field when you create the resource.  
`network` |  `string` Required. Fully-qualified URL of the network that this route applies to, for example: projects/my-project/global/networks/my-network.  
`filter` |  `object (`[Filter](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#Filter)`)` Required. The filter to match L4 traffic.  
`priority` |  `integer` Optional. The priority of this policy-based route. Priority is used to break ties in cases where there are more than one matching policy-based routes found. In cases where multiple policy-based routes are matched, the one with the lowest-numbered priority value wins. The default value is 1000. The priority value must be from 1 to 65535, inclusive.  
`warnings[]` |  `object (`[Warnings](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#Warnings)`)` Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.  
`selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`kind` |  `string` Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for policy-based Route resources.  
Union field `target`. Target specifies network endpoints that this policy-based route applies to. If no target is specified, the PBR will be installed on all network endpoints (e.g. VMs, VPNs, and Interconnects) in the VPC. `target` can be only one of the following:  
`virtualMachine` |  `object (`[VirtualMachine](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#VirtualMachine)`)` Optional. VM instances that this policy-based route applies to.  
`interconnectAttachment` |  `object (`[InterconnectAttachment](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#InterconnectAttachment)`)` Optional. The interconnect attachments that this policy-based route applies to.  
Union field `next_hop`.`next_hop` can be only one of the following:  
`nextHopIlbIp` |  `string` Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported.  
`nextHopOtherRoutes` |  `enum (`[OtherRoutes](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#OtherRoutes)`)` Optional. Other routes that will be referenced to determine the next hop of the packet.  
  
## VirtualMachine

VM instances that this policy-based route applies to.

JSON representation  
---  
      
    
    {
      "tags": [
        string
      ]
    }  
  
Fields  
---  
`tags[]` |  `string` Optional. A list of VM instance tags that this policy-based route applies to. VM instances that have ANY of tags specified here installs this PBR.  
  
## InterconnectAttachment

InterconnectAttachment that this route applies to.

JSON representation  
---  
      
    
    {
      "region": string
    }  
  
Fields  
---  
`region` |  `string` Optional. Cloud region to install this policy-based route on interconnect attachment. Use `all` to install it on all interconnect attachments.  
  
## OtherRoutes

The other routing cases.

Enums  
---  
`OTHER_ROUTES_UNSPECIFIED` | Default value.  
`DEFAULT_ROUTING` | Use the routes from the default routing tables (system-generated routes, custom routes, peering route) to determine the next hop. This effectively excludes matching packets being applied on other PBRs with a lower priority.  
  
## Filter

Filter matches L4 traffic.

JSON representation  
---  
      
    
    {
      "ipProtocol": string,
      "srcRange": string,
      "destRange": string,
      "protocolVersion": enum ([ProtocolVersion](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#ProtocolVersion))
    }  
  
Fields  
---  
`ipProtocol` |  `string` Optional. The IP protocol that this policy-based route applies to. Valid values are 'TCP', 'UDP', and 'ALL'. Default is 'ALL'.  
`srcRange` |  `string` Optional. The source IP range of outgoing packets that this policy-based route applies to. Default is "0.0.0.0/0" if protocol version is IPv4 and "::/0" if protocol version is IPv6.  
`destRange` |  `string` Optional. The destination IP range of outgoing packets that this policy-based route applies to. Default is "0.0.0.0/0" if protocol version is IPv4 and "::/0" if protocol version is IPv6.  
`protocolVersion` |  `enum (`[ProtocolVersion](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#ProtocolVersion)`)` Required. Internet protocol versions this policy-based route applies to. IPV4 and IPV6 is supported.  
  
## ProtocolVersion

The internet protocol version.

Enums  
---  
`PROTOCOL_VERSION_UNSPECIFIED` | Default value.  
`IPV4` | The PBR is for IPv4 internet protocol traffic.  
`IPV6` | The PBR is for IPv6 internet protocol traffic.  
  
## Warnings

Informational warning message.

JSON representation  
---  
      
    
    {
      "code": enum ([Code](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#Code)),
      "data": {
        string: string,
        ...
      },
      "warningMessage": string
    }  
  
Fields  
---  
`code` |  `enum (`[Code](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#Code)`)` Output only. A warning code, if applicable.  
`data` |  `map (key: string, value: string)` Output only. Metadata about this warning in key: value format. The key should provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be scope and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`warningMessage` |  `string` Output only. A human-readable description of the warning code.  
  
## Code

Warning code for policy-based routing. Expect to add values in the future.

Enums  
---  
`WARNING_UNSPECIFIED` | Default value.  
`RESOURCE_NOT_ACTIVE` | The policy-based route is not active and functioning. Common causes are that the dependent network was deleted or the resource project was turned off.  
`RESOURCE_BEING_MODIFIED` | The policy-based route is being modified (e.g. created/deleted) at this time.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/create)`

|  Creates a new policy-based route in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/delete)`

|  Deletes a single policy-based route.  
  
### `[get](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/get)`

|  Gets details of a single policy-based route.  
  
### `[getIamPolicy](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/list)`

|  Lists policy-based routes in a given project and location.  
  
### `[setIamPolicy](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
