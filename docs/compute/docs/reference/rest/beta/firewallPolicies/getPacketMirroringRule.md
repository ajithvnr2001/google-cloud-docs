---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/firewallPolicies/getPacketMirroringRule/
title: Method: firewallPolicies.getPacketMirroringRule \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:55.595893+00:00
---

# Method: firewallPolicies.getPacketMirroringRule  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/firewallPolicies/getPacketMirroringRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: firewallPolicies.getPacketMirroringRule Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Gets a packet mirroring rule of the specified priority.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/locations/global/firewallPolicies/{firewallPolicy}/getPacketMirroringRule`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`firewallPolicy` |  `string` Name of the firewall policy to which the queried rule belongs.  
  
### Query parameters

Parameters  
---  
`priority` |  `integer` The priority of the rule to get from the firewall policy.  
  
### Request body

The request body must be empty.

### Response body

Represents a rule that describes one or more match conditions along with the action to be taken when traffic matches this condition (allow or deny).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
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
        "srcNetworkScope": enum,
        "srcNetworkType": enum,
        "srcNetworkContext": enum,
        "srcNetworks": [
          string
        ],
        "destNetworkScope": enum,
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
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Returns `compute#firewallPolicyRule` for firewall rules and `compute#packetMirroringRule` for packet mirroring rules.  
`ruleName` |  `string` An optional name for the rule. This field is not a unique identifier and can be updated.  
`description` |  `string` An optional description for this resource.  
`priority` |  `integer` An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.  
`match` |  `object` A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.  
`match.srcIpRanges[]` |  `string` CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 5000.  
`match.destIpRanges[]` |  `string` CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 5000.  
`match.layer4Configs[]` |  `object` Pairs of IP protocols and ports that the rule should match.  
`match.layer4Configs[].ipProtocol` |  `string` The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (`tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`), or the IP protocol number.  
`match.layer4Configs[].ports[]` |  `string` An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port.Example inputs include: `["22"]`, `["80","443"]`, and `["12345-12349"]`.  
`match.srcSecureTags[]` |  `object` firewallPolicies.list of secure tag values, which should be matched at the source of the traffic. For INGRESS rule, if all the `srcSecureTag` are INEFFECTIVE, and there is no `srcIpRange`, this rule will be ignored. Maximum number of source tag values allowed is 256.  
`match.srcSecureTags[].name` |  `string` Name of the secure tag, created with TagManager's TagValue API.  
`match.srcSecureTags[].state` |  `enum` Output only. State of the secure tag, either `EFFECTIVE` or `INEFFECTIVE`. A secure tag is `INEFFECTIVE` when it is deleted or its network is deleted.  
`match.destAddressGroups[]` |  `string` Address groups which should be matched against the traffic destination. Maximum number of destination address groups is 10.  
`match.srcAddressGroups[]` |  `string` Address groups which should be matched against the traffic source. Maximum number of source address groups is 10.  
`match.srcFqdns[]` |  `string` Fully Qualified Domain Name (FQDN) which should be matched against traffic source. Maximum number of source fqdn allowed is 100.  
`match.destFqdns[]` |  `string` Fully Qualified Domain Name (FQDN) which should be matched against traffic destination. Maximum number of destination fqdn allowed is 100.  
`match.srcRegionCodes[]` |  `string` Region codes whose IP addresses will be used to match for source of traffic. Should be specified as 2 letter country code defined as per ISO 3166 alpha-2 country codes. ex."US" Maximum number of source region codes allowed is 5000.  
`match.destRegionCodes[]` |  `string` Region codes whose IP addresses will be used to match for destination of traffic. Should be specified as 2 letter country code defined as per ISO 3166 alpha-2 country codes. ex."US" Maximum number of dest region codes allowed is 5000.  
`match.destThreatIntelligences[]` |  `string` Names of Network Threat Intelligence lists. The IPs in these lists will be matched against traffic destination.  
`match.srcThreatIntelligences[]` |  `string` Names of Network Threat Intelligence lists. The IPs in these lists will be matched against traffic source.  
`match.srcNetworkScope` |  `enum` Network scope of the traffic source.  
`match.srcNetworkType` |  `enum` Network type of the traffic source. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `INTRA_VPC`
  * `NON_INTERNET`
  * `VPC_NETWORKS`

  
`match.srcNetworkContext` |  `enum` Network context of the traffic source. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `INTRA_VPC`
  * `NON_INTERNET`
  * `VPC_NETWORKS`

  
`match.srcNetworks[]` |  `string` Networks of the traffic source. It can be either a full or partial url.  
`match.destNetworkScope` |  `enum` Network scope of the traffic destination.  
`match.destNetworkType` |  `enum` Network type of the traffic destination. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `NON_INTERNET`

  
`match.destNetworkContext` |  `enum` Network context of the traffic destination. Allowed values are: 

  * `UNSPECIFIED`
  * `INTERNET`
  * `NON_INTERNET`

  
`action` |  `string` The Action to perform when the client connection triggers the rule. Valid actions for firewall rules are: "allow", "deny", "apply_security_profile_group" and "goto_next" ( "apply_security_profile_group" can be specified only for global network firewall policies or hierarchical firewall policies). Valid actions for packet mirroring rules are: "mirror", "do_not_mirror" and "goto_next".  
`securityProfileGroup` |  `string` A fully-qualified URL of a SecurityProfileGroup resource instance. Example: <https://networksecurity.googleapis.com/v1/projects/{project}/locations/{location}/securityProfileGroups/my-security-profile-group> Must be specified if action is one of 'apply_security_profile_group' or 'mirror'. Cannot be specified for other actions. Can be specified only for global network firewall policies or hierarchical firewall policies.  
`tlsInspect` |  `boolean` Boolean flag indicating if the traffic should be TLS decrypted. Can be set only if action = 'apply_security_profile_group' and cannot be set for other actions.  
`direction` |  `enum` The direction in which this rule applies.  
`targetResources[]` |  `string` A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule.  
`enableLogging` |  `boolean` Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules.  
`ruleTupleCount` |  `integer` Output only. Calculation of the complexity of a single firewall policy rule.  
`targetServiceAccounts[]` |  `string` A list of service accounts indicating the sets of instances that are applied with this rule.  
`targetSecureTags[]` |  `object` A list of secure tags that controls which instances the firewall rule applies to. If `targetSecureTag` are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the targetSecureTag are in INEFFECTIVE state, then this rule will be ignored. `targetSecureTag` may not be set at the same time as `targetServiceAccounts`. If neither `targetServiceAccounts` nor `targetSecureTag` are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256.  
`targetSecureTags[].name` |  `string` Name of the secure tag, created with TagManager's TagValue API.  
`targetSecureTags[].state` |  `enum` Output only. State of the secure tag, either `EFFECTIVE` or `INEFFECTIVE`. A secure tag is `INEFFECTIVE` when it is deleted or its network is deleted.  
`disabled` |  `boolean` Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled.  
`targetType` |  `enum` Target types of the firewall policy rule. Default value is INSTANCES.  
`targetForwardingRules[]` |  `string` A list of forwarding rules to which this rule applies. This field allows you to control which load balancers get this rule. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/forwardingRules/forwardingRule`
  * `<https://www.googleapis.com/compute/v1/projects/>project/regions/region/forwardingRules/forwardingRule`
  * `projects/project/global/ forwardingRules/forwardingRule`
  * `projects/project/regions/region/forwardingRules/ forwardingRule`

  
  
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

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
