---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/
title: REST Resource: firewalls \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:40.926737+00:00
---

# REST Resource: firewalls  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: firewalls Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Firewall
    * JSON representation
  * Methods



## Resource: Firewall

Represents a Firewall Rule resource.

Firewall rules allow or deny ingress traffic to, and egress traffic from your instances. For more information, read [Firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "network": string,
      "priority": integer,
      "sourceRanges": [
        string
      ],
      "destinationRanges": [
        string
      ],
      "sourceTags": [
        string
      ],
      "targetTags": [
        string
      ],
      "sourceServiceAccounts": [
        string
      ],
      "targetServiceAccounts": [
        string
      ],
      "allowed": [
        {
          "IPProtocol": string,
          "ports": [
            string
          ]
        }
      ],
      "denied": [
        {
          "IPProtocol": string,
          "ports": [
            string
          ]
        }
      ],
      "direction": enum,
      "logConfig": {
        "enable": boolean,
        "metadata": enum
      },
      "disabled": boolean,
      "selfLink": string,
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#firewall` for firewall rules.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.  
`description` |  `string` An optional description of this resource. Provide this field when you create the resource.  
`network` |  `string` URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the `default` network is used: 
    
    
    global/networks/default

If you choose to specify this field, you can specify the network as a full or partial URL. For example, the following are all valid URLs: 

  * `<https://www.googleapis.com/compute/v1/projects/myproject/global/networks/my-network>`
  * `projects/myproject/global/networks/my-network`
  * `global/networks/default`

  
`priority` |  `integer` Priority for this rule. This is an integer between `0` and `65535`, both inclusive. The default value is `1000`. Relative priorities determine which rule takes effect if multiple rules apply. Lower values indicate higher priority. For example, a rule with priority `0` has higher precedence than a rule with priority `1`. DENY rules take precedence over ALLOW rules if they have equal priority. Note that VPC networks have [implied](https://cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rules with a priority of `65535`. To avoid conflicts with the implied rules, use a priority number less than `65535`.  
`sourceRanges[]` |  `string` If source ranges are specified, the firewall rule applies only to traffic that has a source IP address in these ranges. These ranges must be expressed in [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) format. One or both of `sourceRanges` and `sourceTags` may be set. If both fields are set, the rule applies to traffic that has a source IP address within `sourceRanges` OR a source IP from a resource with a matching tag listed in the `sourceTags` field. The connection does not need to match both fields for the rule to apply. Both IPv4 and IPv6 are supported.  
`destinationRanges[]` |  `string` If destination ranges are specified, the firewall rule applies only to traffic that has destination IP address in these ranges. These ranges must be expressed in [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) format. Both IPv4 and IPv6 are supported.  
`sourceTags[]` |  `string` If source tags are specified, the firewall rule applies only to traffic with source IPs that match the primary network interfaces of VM instances that have the tag and are in the same VPC network. Source tags cannot be used to control traffic to an instance's external IP address, it only applies to traffic between instances in the same virtual network. Because tags are associated with instances, not IP addresses. One or both of `sourceRanges` and `sourceTags` may be set. If both fields are set, the firewall applies to traffic that has a source IP address within `sourceRanges` OR a source IP from a resource with a matching tag listed in the `sourceTags` field. The connection does not need to match both fields for the firewall to apply.  
`targetTags[]` |  `string` A list of tags that controls which instances the firewall rule applies to. If `targetTags` are specified, then the firewall rule applies only to instances in the VPC network that have one of those tags. If no `targetTags` are specified, the firewall rule applies to all instances on the specified network.  
`sourceServiceAccounts[]` |  `string` If source service accounts are specified, the firewall rules apply only to traffic originating from an instance with a service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP address because service accounts are associated with an instance, not an IP address. `sourceRanges` can be set at the same time as `sourceServiceAccounts`. If both are set, the firewall applies to traffic that has a source IP address within the `sourceRanges` OR a source IP that belongs to an instance with service account listed in `sourceServiceAccount`. The connection does not need to match both fields for the firewall to apply. `sourceServiceAccounts` cannot be used at the same time as `sourceTags` or `targetTags`.  
`targetServiceAccounts[]` |  `string` A list of service accounts indicating sets of instances located in the network that may make network connections as specified in `allowed[]`. `targetServiceAccounts` cannot be used at the same time as `targetTags` or `sourceTags`. If neither `targetServiceAccounts` nor `targetTags` are specified, the firewall rule applies to all instances on the specified network.  
`allowed[]` |  `object` The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection.  
`allowed[].IPProtocol` |  `string` The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (`tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`) or the IP protocol number.  
`allowed[].ports[]` |  `string` An optional list of ports to which this rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.Example inputs include: `["22"]`, `["80","443"]`, and `["12345-12349"]`.  
`denied[]` |  `object` The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a denied connection.  
`denied[].IPProtocol` |  `string` The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (`tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`) or the IP protocol number.  
`denied[].ports[]` |  `string` An optional list of ports to which this rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.Example inputs include: `["22"]`, `["80","443"]`, and `["12345-12349"]`.  
`direction` |  `enum` Direction of traffic to which this firewall applies, either `INGRESS` or `EGRESS`. The default is `INGRESS`. For `EGRESS` traffic, you cannot specify the `sourceTags` fields.  
`logConfig` |  `object` This field denotes the logging options for a particular firewall rule. If logging is enabled, logs will be exported to Cloud Logging.  
`logConfig.enable` |  `boolean` This field denotes whether to enable logging for a particular firewall rule.  
`logConfig.metadata` |  `enum` This field can only be specified for a particular firewall rule if logging is enabled for that rule. This field denotes whether to include or exclude metadata for firewall logs.  
`disabled` |  `boolean` Denotes whether the firewall rule is disabled. When set to true, the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall rule will be enabled.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/delete)`

|  Deletes the specified firewall.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/get)`

|  Returns the specified firewall.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert)`

|  Creates a firewall rule in the specified project using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/list)`

|  Retrieves the list of firewall rules available to the specified project.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/patch)`

|  Updates the specified firewall rule with the data included in the request.  
  
### `[testIamPermissions](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/update)`

|  Updates the specified firewall rule with the data included in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
