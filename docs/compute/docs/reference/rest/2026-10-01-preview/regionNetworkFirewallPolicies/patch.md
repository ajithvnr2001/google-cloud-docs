---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/regionNetworkFirewallPolicies/patch/
title: Method: regionNetworkFirewallPolicies.patch \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:15.676482+00:00
---

# Method: regionNetworkFirewallPolicies.patch  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/regionNetworkFirewallPolicies/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: regionNetworkFirewallPolicies.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
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



API Version : 2026-10-01-preview

Patches the specified network firewall policy.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`PATCH https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/firewallPolicies/{firewallPolicy}?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region scoping this request.  
`firewallPolicy` |  `string` Name of the firewall policy to update.  
  
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
`rules[].match.srcSecureTags[]` |  `object` regionNetworkFirewallPolicies.list of secure tag values, which should be matched at the source of the traffic. For INGRESS rule, if all the `srcSecureTag` are INEFFECTIVE, and there is no `srcIpRange`, this rule will be ignored. Maximum number of source tag values allowed is 256.  
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
`packetMirroringRules[].match.srcSecureTags[]` |  `object` regionNetworkFirewallPolicies.list of secure tag values, which should be matched at the source of the traffic. For INGRESS rule, if all the `srcSecureTag` are INEFFECTIVE, and there is no `srcIpRange`, this rule will be ignored. Maximum number of source tag values allowed is 256.  
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
**(deprecated)**` |  `string` Deprecated, please use short name instead. User-provided name of the Organization firewall policy. The name should be unique in the organization in which the firewall policy is created. This field is not applicable to network firewall policies. This name must be set on creation and cannot be changed. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`parent` |  `string` Output only. The parent of the firewall policy. This field is not applicable to network firewall policies.  
`region` |  `string` Output only. URL of the region where the regional firewall policy resides. This field is not applicable to global firewall policies. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`policyType` |  `enum` The type of the firewall policy. This field can be one of VPC_POLICY, RDMA_ROCE_POLICY or ULL_POLICY.Note: if not specified then `VPC_POLICY` will be used.  
  
### Response body

Represents an Operation resource.

Google Compute Engine has three Operation resources:

  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations)
  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations)



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

  * `compute.regionFirewallPolicies.get`
  * `compute.regionFirewallPolicies.update`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
