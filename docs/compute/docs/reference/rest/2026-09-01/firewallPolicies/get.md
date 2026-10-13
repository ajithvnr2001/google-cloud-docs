---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/firewallPolicies/get/
title: Method: firewallPolicies.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:03:29.570139+00:00
---

# Method: firewallPolicies.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/firewallPolicies/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: firewallPolicies.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
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

Returns the specified firewall policy.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/locations/global/{firewallPolicy=firewallPolicies/*}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`firewallPolicy` |  `string` Name of the firewall policy to get.  
  
### Request body

The request body must be empty.

### Response body

Represents a Firewall Policy resource.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "rules": [
        {
          "kind": string,
          "ruleName": string,
          "description": string,
          "priority": integer,
          "match": {
            "srcIpRanges": [
              string
            ],
            "destIpRanges": [
              string
            ],
            "layer4Configs": [
              {
                "ipProtocol": string,
                "ports": [
                  string
                ]
              }
            ],
            "srcSecureTags": [
              {
                "name": string,
                "state": enum
              }
            ],
            "destAddressGroups": [
              string
            ],
            "srcAddressGroups": [
              string
            ],
            "srcFqdns": [
              string
            ],
            "destFqdns": [
              string
            ],
            "srcRegionCodes": [
              string
            ],
            "destRegionCodes": [
              string
            ],
            "destThreatIntelligences": [
              string
            ],
            "srcThreatIntelligences": [
              string
            ],
            "srcNetworkType": enum,
            "srcNetworkContext": enum,
            "srcNetworks": [
              string
            ],
            "destNetworkType": enum,
            "destNetworkContext": enum
          },
          "action": string,
          "securityProfileGroup": string,
          "tlsInspect": boolean,
          "direction": enum,
          "targetResources": [
            string
          ],
          "enableLogging": boolean,
          "ruleTupleCount": integer,
          "targetServiceAccounts": [
            string
          ],
          "targetSecureTags": [
            {
              "name": string,
              "state": enum
            }
          ],
          "disabled": boolean,
          "targetType": enum,
          "targetForwardingRules": [
            string
          ]
        }
      ],
      "packetMirroringRules": [
        {
          "kind": string,
          "ruleName": string,
          "description": string,
          "priority": integer,
          "match": {
            "srcIpRanges": [
              string
            ],
            "destIpRanges": [
              string
            ],
            "layer4Configs": [
              {
                "ipProtocol": string,
                "ports": [
                  string
                ]
              }
            ],
            "srcSecureTags": [
              {
                "name": string,
                "state": enum
              }
            ],
            "destAddressGroups": [
              string
            ],
            "srcAddressGroups": [
              string
            ],
            "srcFqdns": [
              string
            ],
            "destFqdns": [
              string
            ],
            "srcRegionCodes": [
              string
            ],
            "destRegionCodes": [
              string
            ],
            "destThreatIntelligences": [
              string
            ],
            "srcThreatIntelligences": [
              string
            ],
            "srcNetworkType": enum,
            "srcNetworkContext": enum,
            "srcNetworks": [
              string
            ],
            "destNetworkType": enum,
            "destNetworkContext": enum
          },
          "action": string,
          "securityProfileGroup": string,
          "tlsInspect": boolean,
          "direction": enum,
          "targetResources": [
            string
          ],
          "enableLogging": boolean,
          "ruleTupleCount": integer,
          "targetServiceAccounts": [
            string
          ],
          "targetSecureTags": [
            {
              "name": string,
              "state": enum
            }
          ],
          "disabled": boolean,
          "targetType": enum,
          "targetForwardingRules": [
            string
          ]
        }
      ],
      "fingerprint": string,
      "selfLink": string,
      "selfLinkWithId": string,
      "associations": [
        {
          "name": string,
          "attachmentTarget": string,
          "firewallPolicyId": string,
          "shortName": string,
          "displayName": string,
          "priority": integer
        }
      ],
      "ruleTupleCount": integer,
      "shortName": string,
      "displayName": string,
      "parent": string,
      "region": string,
      "policyType": enum
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#firewallPolicy`for firewall policies  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. For Organization Firewall Policies it's a Output only. numeric ID allocated by Google Cloud which uniquely identifies the Organization Firewall Policy.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`rules[]` |  `object` A list of rules that belong to this policy. There must always be a default rule (rule with priority 2147483647 and match "*"). If no rules are provided when creating a firewall policy, a default rule with action "allow" will be added.  
`rules[].kind` |  `string` Output only. Type of the resource. Returns `compute#firewallPolicyRule` for firewall rules and `compute#packetMirroringRule` for packet mirroring rules.  
`rules[].ruleName` |  `string` An optional name for the rule. This field is not a unique identifier and can be updated.  
`rules[].description` |  `string` An optional description for this resource.  
`rules[].priority` |  `integer` An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.  
`rules[].match` |  `object` A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.  
`rules[].match.srcIpRanges[]` |  `string` CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 5000.  
`rules[].match.destIpRanges[]` |  `string` CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 5000.  
`rules[].match.layer4Configs[]` |  `object` Pairs of IP protocols and ports that the rule should match.  
`rules[].match.layer4Configs[].ipProtocol` |  `string` The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (`tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`), or the IP protocol number.  
`rules[].match.layer4Configs[].ports[]` |  `string` An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.Example inputs include: `["22"]`, `["80","443"]`, and `["12345-12349"]`.  
`rules[].match.srcSecureTags[]` |  `object` firewallPolicies.list of secure tag values, which should be matched at the source of the traffic. For INGRESS rule, if all the `srcSecureTag` are INEFFECTIVE, and there is no `srcIpRange`, this rule will be ignored. Maximum number of source tag values allowed is 256.  
`rules[].match.srcSecureTags[].name` |  `string` Name of the secure tag, created with TagManager's TagValue API.  
`rules[].match.srcSecureTags[].state` |  `enum` Output only. State of the secure tag, either `EFFECTIVE` or `INEFFECTIVE`. A secure tag is `INEFFECTIVE` when it is deleted or its network is deleted.  
`rules[].match.destAddressGroups[]` |  `string` Address groups which should be matched against the traffic destination. Maximum number of destination address groups is 10.  
`rules[].match.srcAddressGroups[]` |  `string` Address groups which should be matched against the traffic source. Maximum number of source address groups is 10.  
`rules[].match.srcFqdns[]` |  `string` Fully Qualified Domain Name (FQDN) which should be matched against traffic source. Maximum number of source fqdn allowed is 100.  
`rules[].match.destFqdns[]` |  `string` Fully Qualified Domain Name (FQDN) which should be matched against traffic destination. Maximum number of destination fqdn allowed is 100.  
`rules[].match.srcRegionCodes[]` |  `string` Region codes whose IP addresses will be used to match for source of traffic. Should be specified as 2 letter country code defined as per ISO 3166 alpha-2 country codes. ex."US" Maximum number of source region codes allowed is 5000.  
`rules[].match.destRegionCodes[]` |  `string` Region codes whose IP addresses will be used to match for destination of traffic. Should be specified as 2 letter country code defined as per ISO 3166 alpha-2 country codes. ex."US" Maximum number of dest region codes allowed is 5000.  
`rules[].match.destThreatIntelligences[]` |  `string` Names of Network Threat Intelligence lists. The IPs in these lists will be matched against traffic destination.  
`rules[].match.srcThreatIntelligences[]` |  `string` Names of Network Threat Intelligence lists. The IPs in these lists will be matched against traffic source.  
`rules[].match.srcNetworkType` |  `enum` Network type of the traffic source. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `INTRA_VPC`
  * `NON_INTERNET`
  * `VPC_NETWORKS`

  
`rules[].match.srcNetworkContext` |  `enum` Network context of the traffic source. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `INTRA_VPC`
  * `NON_INTERNET`
  * `VPC_NETWORKS`

  
`rules[].match.srcNetworks[]` |  `string` Networks of the traffic source. It can be either a full or partial url.  
`rules[].match.destNetworkType` |  `enum` Network type of the traffic destination. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `NON_INTERNET`

  
`rules[].match.destNetworkContext` |  `enum` Network context of the traffic destination. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `NON_INTERNET`

  
`rules[].action` |  `string` The Action to perform when the client connection triggers the rule. Valid actions for firewall rules are: "allow", "deny", "apply_security_profile_group" and "goto_next" ( "apply_security_profile_group" can be specified only for global network firewall policies or hierarchical firewall policies). Valid actions for packet mirroring rules are: "mirror", "do_not_mirror" and "goto_next".  
`rules[].securityProfileGroup` |  `string` A fully-qualified URL of a SecurityProfileGroup resource instance. Example: <https://networksecurity.googleapis.com/v1/projects/{project}/locations/{location}/securityProfileGroups/my-security-profile-group> Must be specified if action is one of 'apply_security_profile_group' or 'mirror'. Cannot be specified for other actions. Can be specified only for global network firewall policies or hierarchical firewall policies.  
`rules[].tlsInspect` |  `boolean` Boolean flag indicating if the traffic should be TLS decrypted. Can be set only if action = 'apply_security_profile_group' and cannot be set for other actions.  
`rules[].direction` |  `enum` The direction in which this rule applies.  
`rules[].targetResources[]` |  `string` A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule.  
`rules[].enableLogging` |  `boolean` Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules.  
`rules[].ruleTupleCount` |  `integer` Output only. Calculation of the complexity of a single firewall policy rule.  
`rules[].targetServiceAccounts[]` |  `string` A list of service accounts indicating the sets of instances that are applied with this rule.  
`rules[].targetSecureTags[]` |  `object` A list of secure tags that controls which instances the firewall rule applies to. If `targetSecureTag` are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the targetSecureTag are in INEFFECTIVE state, then this rule will be ignored. `targetSecureTag` may not be set at the same time as `targetServiceAccounts`. If neither `targetServiceAccounts` nor `targetSecureTag` are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256.  
`rules[].targetSecureTags[].name` |  `string` Name of the secure tag, created with TagManager's TagValue API.  
`rules[].targetSecureTags[].state` |  `enum` Output only. State of the secure tag, either `EFFECTIVE` or `INEFFECTIVE`. A secure tag is `INEFFECTIVE` when it is deleted or its network is deleted.  
`rules[].disabled` |  `boolean` Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled.  
`rules[].targetType` |  `enum` Target types of the firewall policy rule. Default value is INSTANCES.  
`rules[].targetForwardingRules[]` |  `string` A list of forwarding rules to which this rule applies. This field allows you to control which load balancers get this rule. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/forwardingRules/forwardingRule`
  * `<https://www.googleapis.com/compute/v1/projects/>project/regions/region/forwardingRules/forwardingRule`
  * `projects/project/global/ forwardingRules/forwardingRule`
  * `projects/project/regions/region/forwardingRules/ forwardingRule`

  
`packetMirroringRules[]` |  `object` A list of packet mirroring rules that belong to this policy.  
`packetMirroringRules[].kind` |  `string` Output only. Type of the resource. Returns `compute#firewallPolicyRule` for firewall rules and `compute#packetMirroringRule` for packet mirroring rules.  
`packetMirroringRules[].ruleName` |  `string` An optional name for the rule. This field is not a unique identifier and can be updated.  
`packetMirroringRules[].description` |  `string` An optional description for this resource.  
`packetMirroringRules[].priority` |  `integer` An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.  
`packetMirroringRules[].match` |  `object` A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.  
`packetMirroringRules[].match.srcIpRanges[]` |  `string` CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 5000.  
`packetMirroringRules[].match.destIpRanges[]` |  `string` CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 5000.  
`packetMirroringRules[].match.layer4Configs[]` |  `object` Pairs of IP protocols and ports that the rule should match.  
`packetMirroringRules[].match.layer4Configs[].ipProtocol` |  `string` The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (`tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`), or the IP protocol number.  
`packetMirroringRules[].match.layer4Configs[].ports[]` |  `string` An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.Example inputs include: `["22"]`, `["80","443"]`, and `["12345-12349"]`.  
`packetMirroringRules[].match.srcSecureTags[]` |  `object` firewallPolicies.list of secure tag values, which should be matched at the source of the traffic. For INGRESS rule, if all the `srcSecureTag` are INEFFECTIVE, and there is no `srcIpRange`, this rule will be ignored. Maximum number of source tag values allowed is 256.  
`packetMirroringRules[].match.srcSecureTags[].name` |  `string` Name of the secure tag, created with TagManager's TagValue API.  
`packetMirroringRules[].match.srcSecureTags[].state` |  `enum` Output only. State of the secure tag, either `EFFECTIVE` or `INEFFECTIVE`. A secure tag is `INEFFECTIVE` when it is deleted or its network is deleted.  
`packetMirroringRules[].match.destAddressGroups[]` |  `string` Address groups which should be matched against the traffic destination. Maximum number of destination address groups is 10.  
`packetMirroringRules[].match.srcAddressGroups[]` |  `string` Address groups which should be matched against the traffic source. Maximum number of source address groups is 10.  
`packetMirroringRules[].match.srcFqdns[]` |  `string` Fully Qualified Domain Name (FQDN) which should be matched against traffic source. Maximum number of source fqdn allowed is 100.  
`packetMirroringRules[].match.destFqdns[]` |  `string` Fully Qualified Domain Name (FQDN) which should be matched against traffic destination. Maximum number of destination fqdn allowed is 100.  
`packetMirroringRules[].match.srcRegionCodes[]` |  `string` Region codes whose IP addresses will be used to match for source of traffic. Should be specified as 2 letter country code defined as per ISO 3166 alpha-2 country codes. ex."US" Maximum number of source region codes allowed is 5000.  
`packetMirroringRules[].match.destRegionCodes[]` |  `string` Region codes whose IP addresses will be used to match for destination of traffic. Should be specified as 2 letter country code defined as per ISO 3166 alpha-2 country codes. ex."US" Maximum number of dest region codes allowed is 5000.  
`packetMirroringRules[].match.destThreatIntelligences[]` |  `string` Names of Network Threat Intelligence lists. The IPs in these lists will be matched against traffic destination.  
`packetMirroringRules[].match.srcThreatIntelligences[]` |  `string` Names of Network Threat Intelligence lists. The IPs in these lists will be matched against traffic source.  
`packetMirroringRules[].match.srcNetworkType` |  `enum` Network type of the traffic source. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `INTRA_VPC`
  * `NON_INTERNET`
  * `VPC_NETWORKS`

  
`packetMirroringRules[].match.srcNetworkContext` |  `enum` Network context of the traffic source. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `INTRA_VPC`
  * `NON_INTERNET`
  * `VPC_NETWORKS`

  
`packetMirroringRules[].match.srcNetworks[]` |  `string` Networks of the traffic source. It can be either a full or partial url.  
`packetMirroringRules[].match.destNetworkType` |  `enum` Network type of the traffic destination. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `NON_INTERNET`

  
`packetMirroringRules[].match.destNetworkContext` |  `enum` Network context of the traffic destination. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `NON_INTERNET`

  
`packetMirroringRules[].action` |  `string` The Action to perform when the client connection triggers the rule. Valid actions for firewall rules are: "allow", "deny", "apply_security_profile_group" and "goto_next" ( "apply_security_profile_group" can be specified only for global network firewall policies or hierarchical firewall policies). Valid actions for packet mirroring rules are: "mirror", "do_not_mirror" and "goto_next".  
`packetMirroringRules[].securityProfileGroup` |  `string` A fully-qualified URL of a SecurityProfileGroup resource instance. Example: <https://networksecurity.googleapis.com/v1/projects/{project}/locations/{location}/securityProfileGroups/my-security-profile-group> Must be specified if action is one of 'apply_security_profile_group' or 'mirror'. Cannot be specified for other actions. Can be specified only for global network firewall policies or hierarchical firewall policies.  
`packetMirroringRules[].tlsInspect` |  `boolean` Boolean flag indicating if the traffic should be TLS decrypted. Can be set only if action = 'apply_security_profile_group' and cannot be set for other actions.  
`packetMirroringRules[].direction` |  `enum` The direction in which this rule applies.  
`packetMirroringRules[].targetResources[]` |  `string` A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule.  
`packetMirroringRules[].enableLogging` |  `boolean` Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules.  
`packetMirroringRules[].ruleTupleCount` |  `integer` Output only. Calculation of the complexity of a single firewall policy rule.  
`packetMirroringRules[].targetServiceAccounts[]` |  `string` A list of service accounts indicating the sets of instances that are applied with this rule.  
`packetMirroringRules[].targetSecureTags[]` |  `object` A list of secure tags that controls which instances the firewall rule applies to. If `targetSecureTag` are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the targetSecureTag are in INEFFECTIVE state, then this rule will be ignored. `targetSecureTag` may not be set at the same time as `targetServiceAccounts`. If neither `targetServiceAccounts` nor `targetSecureTag` are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256.  
`packetMirroringRules[].targetSecureTags[].name` |  `string` Name of the secure tag, created with TagManager's TagValue API.  
`packetMirroringRules[].targetSecureTags[].state` |  `enum` Output only. State of the secure tag, either `EFFECTIVE` or `INEFFECTIVE`. A secure tag is `INEFFECTIVE` when it is deleted or its network is deleted.  
`packetMirroringRules[].disabled` |  `boolean` Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled.  
`packetMirroringRules[].targetType` |  `enum` Target types of the firewall policy rule. Default value is INSTANCES.  
`packetMirroringRules[].targetForwardingRules[]` |  `string` A list of forwarding rules to which this rule applies. This field allows you to control which load balancers get this rule. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/forwardingRules/forwardingRule`
  * `<https://www.googleapis.com/compute/v1/projects/>project/regions/region/forwardingRules/forwardingRule`
  * `projects/project/global/ forwardingRules/forwardingRule`
  * `projects/project/regions/region/forwardingRules/ forwardingRule`

  
`fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Specifies a fingerprint for this resource, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make `get()` request to the firewall policy.A base64-encoded string.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`associations[]` |  `object` A list of associations that belong to this firewall policy.  
`associations[].name` |  `string` The name for an association.  
`associations[].attachmentTarget` |  `string` The target that the firewall policy is attached to.  
`associations[].firewallPolicyId` |  `string` Output only. The firewall policy ID of the association.  
`associations[].shortName` |  `string` Output only. The short name of the firewall policy of the association.  
`associations[].displayName  
**(deprecated)**` |  `string` Output only. Deprecated, please use short name instead. The display name of the firewall policy of the association.  
`associations[].priority` |  `integer` An integer indicating the priority of an association. The priority must be a positive value between 1 and 2147483647. Firewall Policies are evaluated from highest to lowest priority where 1 is the highest priority and 2147483647 is the lowest priority. The default value is `1000`. If two associations have the same priority then lexicographical order on association names is applied.  
`ruleTupleCount` |  `integer` Output only. Total count of all firewall policy rule tuples. A firewall policy can not exceed a set number of tuples.  
`shortName` |  `string` User-provided name of the Organization firewall policy. The name should be unique in the organization in which the firewall policy is created. This field is not applicable to network firewall policies. This name must be set on creation and cannot be changed. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`displayName  
**(deprecated)**` |  `string` This item is deprecated!Deprecated, please use short name instead. User-provided name of the Organization firewall policy. The name should be unique in the organization in which the firewall policy is created. This field is not applicable to network firewall policies. This name must be set on creation and cannot be changed. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`parent` |  `string` Output only. The parent of the firewall policy. This field is not applicable to network firewall policies.  
`region` |  `string` Output only. URL of the region where the regional firewall policy resides. This field is not applicable to global firewall policies. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`policyType` |  `enum` The type of the firewall policy. This field can be one of VPC_POLICY, RDMA_ROCE_POLICY or ULL_POLICY.Note: if not specified then `VPC_POLICY` will be used.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.firewallPolicies.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
