---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/mirroring-rules/update/
title: gcloud beta compute network-firewall-policies mirroring-rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:15:16.090073+00:00
---

# gcloud beta compute network-firewall-policies mirroring-rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/mirroring-rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute network-firewall-policies mirroring-rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute network-firewall-policies mirroring-rules update - updates a Compute Engine network firewall policy packet mirroring rule 
SYNOPSIS
    

`gcloud beta compute network-firewall-policies mirroring-rules update` `PRIORITY` `--firewall-policy`=`FIREWALL_POLICY` `--global-firewall-policy` [`--action`=`ACTION`] [`--description`=`DESCRIPTION`] [`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]] [`--direction`=`DIRECTION`] [`--[no-]disabled`] [`--layer4-configs`=[`LAYER4_CONFIG`,…]] [`--new-priority`=`NEW_PRIORITY`] [`--security-profile-group`=`SECURITY_PROFILE_GROUP`] [`--src-ip-ranges`=[`SRC_IP_RANGE`,…]] [`--target-secure-tags`=[`TARGET_SECURE_TAGS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute network-firewall-policies mirroring-rules update` is used to update network firewall policy packet mirroring rules. 
EXAMPLES
     To update a rule with priority ``10`` in a global network firewall policy with name ``my-policy`` to change the action to ``mirror`` and description to ``new example rule``, run: 
    
    
    [gcloud beta compute network-firewall-policies mirroring-rules](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/mirroring-rules) update 10 --firewall-policy=my-policy --action=mirror --description="new example rule"

POSITIONAL ARGUMENTS
    

`PRIORITY`
     Priority of the rule to be updated. Valid in [0, 2147483547]. 
REQUIRED FLAGS
    

`--firewall-policy`=`FIREWALL_POLICY`
     Firewall policy ID with which to update rule. 
`--global-firewall-policy`
     Use this flag to indicate that firewall policy is global. 
OPTIONAL FLAGS
    

`--action`=`ACTION`
     Action to take if the request matches the match condition. `ACTION` must be one of: `mirror`, `do_not_mirror`, `goto_next`. 
`--description`=`DESCRIPTION`
     An optional, textual description for the rule. 
`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]
     Destination IP ranges to match for this rule. 
`--direction`=`DIRECTION`
     Direction of the traffic the rule is applied. The default is to apply on incoming traffic. `DIRECTION` must be one of: `INGRESS`, `EGRESS`. 
`--[no-]disabled`
     Use this flag to disable the rule. Disabled rules will not affect traffic. Use `--disabled` to enable and `--no-disabled` to disable. 
`--layer4-configs`=[`LAYER4_CONFIG`,…]
     A list of destination protocols and ports to which the firewall rule will apply. 
`--new-priority`=`NEW_PRIORITY`
     New priority for the rule to update. Valid in [0, 65535]. 
`--security-profile-group`=`SECURITY_PROFILE_GROUP`
     A security profile group to be used with mirror action. 
`--src-ip-ranges`=[`SRC_IP_RANGE`,…]
     A list of IP address blocks that are allowed to make inbound connections that match the firewall rule to the instances on the network. The IP address blocks must be specified in CIDR format: <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing.Either> \--src-ip-ranges or --src-secure-tags must be specified for INGRESS traffic. If both --src-ip-ranges and --src-secure-tags are specified, the rule matches if either the range of the source matches --src-ip-ranges or the secure tag of the source matches --src-secure-tags.Multiple IP address blocks can be specified if they are separated by commas. 
`--target-secure-tags`=[`TARGET_SECURE_TAGS`,…]
     An optional, list of target secure tags with a name of the format tagValues/ or full namespaced name 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute network-firewall-policies mirroring-rules update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update)
    
    
    [gcloud alpha compute network-firewall-policies mirroring-rules](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/mirroring-rules) update
    
    
    [gcloud preview compute network-firewall-policies mirroring-rules](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/mirroring-rules) update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
