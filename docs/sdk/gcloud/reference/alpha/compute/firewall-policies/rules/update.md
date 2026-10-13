---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/update/
title: gcloud alpha compute firewall-policies rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:14.539425+00:00
---

# gcloud alpha compute firewall-policies rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute firewall-policies rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute firewall-policies rules update - updates a Compute Engine firewall policy rule 
SYNOPSIS
    

`gcloud alpha compute firewall-policies rules update` `PRIORITY` `--firewall-policy`=`FIREWALL_POLICY` [`--action`=`ACTION`] [`--description`=`DESCRIPTION`] [`--dest-address-groups`=[`DEST_ADDRESS_GROUPS`,…]] [`--dest-fqdns`=[`DEST_FQDNS`,…]] [`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]] [`--dest-network-context`=`DEST_NETWORK_CONTEXT`] [`--dest-network-type`=`DEST_NETWORK_TYPE`] [`--dest-region-codes`=[`DEST_REGION_CODES`,…]] [`--dest-threat-intelligence`=[`DEST_THREAT_INTELLIGENCE_LISTS`,…]] [`--direction`=`DIRECTION`] [`--[no-]disabled`] [`--[no-]enable-logging`] [`--layer4-configs`=[`LAYER4_CONFIG`,…]] [`--new-priority`=`NEW_PRIORITY`] [`--organization`=`ORGANIZATION`] [`--security-profile-group`=`SECURITY_PROFILE_GROUP`] [`--src-address-groups`=[`SOURCE_ADDRESS_GROUPS`,…]] [`--src-fqdns`=[`SOURCE_FQDNS`,…]] [`--src-ip-ranges`=[`SRC_IP_RANGE`,…]] [`--src-network-context`=`SRC_NETWORK_CONTEXT`] [`--src-network-type`=`SRC_NETWORK_TYPE`] [`--src-networks`=[`SRC_NETWORKS`,…]] [`--src-region-codes`=[`SOURCE_REGION_CODES`,…]] [`--src-secure-tags`=[`SOURCE_SECURE_TAGS`,…]] [`--src-threat-intelligence`=[`SOURCE_THREAT_INTELLIGENCE_LISTS`,…]] [`--target-resources`=[`TARGET_RESOURCES`,…]] [`--target-secure-tags`=[`TARGET_SECURE_TAGS`,…]] [`--target-service-accounts`=[`TARGET_SERVICE_ACCOUNTS`,…]] [`--[no-]tls-inspect`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute firewall-policies rules update` is used to update organization firewall policy rules. 
EXAMPLES
     To update a rule with priority ``10" in an organization firewall policy with ID ``123456789" to change the action to ``allow" and description to ``new-example-rule", run: 
    
    
    gcloud alpha compute firewall-policies rules update 10 --firewall-policy=123456789 --action=allow --description=new-example-rule

POSITIONAL ARGUMENTS
    

`PRIORITY`
     Priority of the firewall policy rule to update. 
REQUIRED FLAGS
    

`--firewall-policy`=`FIREWALL_POLICY`
     Short name of the firewall policy into which the rule should be updated. 
OPTIONAL FLAGS
    

`--action`=`ACTION`
     Action to take if the request matches the match condition. `ACTION` must be one of: `allow`, `deny`, `goto_next`, `apply_security_profile_group`. 
`--description`=`DESCRIPTION`
     An optional, textual description for the rule. 
`--dest-address-groups`=[`DEST_ADDRESS_GROUPS`,…]
     Destination address groups to match for this rule. Can only be specified if DIRECTION is egress. 
`--dest-fqdns`=[`DEST_FQDNS`,…]
     Destination FQDNs to match for this rule. Can only be specified if DIRECTION is `egress`. 
`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]
     Destination IP ranges to match for this rule. 
`--dest-network-context`=`DEST_NETWORK_CONTEXT`
     Use this flag to indicate that the rule should match internet or non-internet traffic. It applies to destination traffic for egress rules. Valid values are INTERNET and NON_INTERNET. Use empty string to clear the field. 
`--dest-network-type`=`DEST_NETWORK_TYPE`
     Use this flag to indicate that the rule should match internet or non-internet traffic. It applies to destination traffic for egress rules. Valid values are INTERNET and NON_INTERNET. Use empty string to clear the field. 
`--dest-region-codes`=[`DEST_REGION_CODES`,…]
     Destination Region Code to match for this rule. Can only be specified if DIRECTION is `egress`. Cannot be specified when the source network context is NON_INTERNET. 
`--dest-threat-intelligence`=[`DEST_THREAT_INTELLIGENCE_LISTS`,…]
     Destination Threat Intelligence lists to match for this rule. Can only be specified if DIRECTION is `egress`. Cannot be specified when source network context is NON_INTERNET. The available lists can be found here: <https://cloud.google.com/vpc/docs/firewall-policies-rule-details#threat-intelligence-fw-policy>. 
`--direction`=`DIRECTION`
     Direction of the traffic the rule is applied. The default is to apply on incoming traffic. `DIRECTION` must be one of: `INGRESS`, `EGRESS`. 
`--[no-]disabled`
     Use this flag to disable the rule. Disabled rules will not affect traffic. Use `--disabled` to disable and `--no-disabled` to enable. 
`--[no-]enable-logging`
     Use this flag to enable logging of connections that allowed or denied by this rule. Use `--enable-logging` to enable and `--no-enable-logging` to disable. 
`--layer4-configs`=[`LAYER4_CONFIG`,…]
     A list of destination protocols and ports to which the firewall rule will apply. 
`--new-priority`=`NEW_PRIORITY`
     New priority for the rule to update. Valid in [0, 65535]. 
`--organization`=`ORGANIZATION`
     Organization which the organization firewall policy belongs to. Must be set if FIREWALL_POLICY is short name. 
`--security-profile-group`=`SECURITY_PROFILE_GROUP`
     An org-based security profile group to be used with apply_security_profile_group action. Allowed formats are: a) http(s)://<namespace>/<api>/organizations/<org_id>/locations/global/securityProfileGroups/<profile> b) (//)<namespace>/organizations/<org_id>/locations/global/securityProfileGroups/<profile> c) <profile>. In case "c" `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI will create a reference matching format "a", but to make it work CLOUDSDK_API_ENDPOINT_OVERRIDES_NETWORKSECURITY property must be set. In order to set this property, please run the command `gcloud config set api_endpoint_overrides/networksecurity https://<namespace>/`. 
`--src-address-groups`=[`SOURCE_ADDRESS_GROUPS`,…]
     Source address groups to match for this rule. Can only be specified if DIRECTION is ingress. 
`--src-fqdns`=[`SOURCE_FQDNS`,…]
     Source FQDNs to match for this rule. Can only be specified if DIRECTION is `ingress`. 
`--src-ip-ranges`=[`SRC_IP_RANGE`,…]
     Source IP ranges to match for this rule. 
`--src-network-context`=`SRC_NETWORK_CONTEXT`
     Use this flag to indicate that the rule should match internet, non-internet traffic or traffic coming from the network specified by --src-network. It applies to ingress rules. Valid values are INTERNET, NON_INTERNET, VPC_NETWORKS and INTRA_VPC. Use empty string to clear the field. 
`--src-network-type`=`SRC_NETWORK_TYPE`
     Use this flag to indicate that the rule should match internet, non-internet traffic or traffic coming from the network specified by --src-network. It applies to ingress rules. Valid values are INTERNET, NON_INTERNET, VPC_NETWORKS and INTRA_VPC. Use empty string to clear the field. 
`--src-networks`=[`SRC_NETWORKS`,…]
     The source VPC networks to match for this rule. It can only be specified when \--src-network-type is VPC_NETWORKS. It applies to ingress rules. It accepts full or partial URLs. 
`--src-region-codes`=[`SOURCE_REGION_CODES`,…]
     Source Region Code to match for this rule. Can only be specified if DIRECTION is `ingress`. Cannot be specified when the source network context is NON_INTERNET, VPC_NETWORK or INTRA_VPC. 
`--src-secure-tags`=[`SOURCE_SECURE_TAGS`,…]
     A list of instance secure tags indicating the set of instances on the network to which the rule applies if all other fields match. Either --src-ip-ranges or \--src-secure-tags must be specified for ingress traffic. If both --src-ip-ranges and --src-secure-tags are specified, an inbound connection is allowed if either the range of the source matches --src-ip-ranges or the tag of the source matches \--src-secure-tags. Secure Tags can be assigned to instances during instance creation. 
`--src-threat-intelligence`=[`SOURCE_THREAT_INTELLIGENCE_LISTS`,…]
     Source Threat Intelligence lists to match for this rule. Can only be specified if DIRECTION is `ingress`. Cannot be specified when the source network context is NON_INTERNET, VPC_NETWORK or INTRA_VPC. The available lists can be found here: <https://cloud.google.com/vpc/docs/firewall-policies-rule-details#threat-intelligence-fw-policy>. 
`--target-resources`=[`TARGET_RESOURCES`,…]
     List of URLs of target resources to which the rule is applied. 
`--target-secure-tags`=[`TARGET_SECURE_TAGS`,…]
     An optional, list of target secure tags with a name of the format tagValues/ or full namespaced name 
`--target-service-accounts`=[`TARGET_SERVICE_ACCOUNTS`,…]
     List of target service accounts for the rule. 
`--[no-]tls-inspect`
     Use this flag to indicate whether TLS traffic should be inspected using the TLS inspection policy when the security profile group is applied. Default: no TLS inspection. Use `--tls-inspect` to enable and `--no-tls-inspect` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute firewall-policies rules update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/update)
    
    
    [gcloud beta compute firewall-policies rules update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/rules/update)
    
    
    [gcloud preview compute firewall-policies rules update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies/rules/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
