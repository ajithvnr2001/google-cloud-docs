---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-policies/traffic-classification-rules/update/
title: gcloud alpha compute network-policies traffic-classification-rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:26:25.501460+00:00
---

# gcloud alpha compute network-policies traffic-classification-rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-policies/traffic-classification-rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute network-policies traffic-classification-rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute network-policies traffic-classification-rules update - updates a Compute Engine network policy rule 
SYNOPSIS
    

`gcloud alpha compute network-policies traffic-classification-rules update` `--network-policy`=`NETWORK_POLICY` `--priority`=`PRIORITY` [`--action`=`ACTION`] [`--description`=`DESCRIPTION`] [`--dest-address-groups`=[`DEST_ADDRESS_GROUP`,…]] [`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]] [`--[no-]disabled`] [`--dscp-mode`=`DSCP_MODE`] [`--dscp-value`=`DSCP_VALUE`] [`--layer4-configs`=[`LAYER4_CONFIG`,…]] [`--network-policy-region`=`NETWORK_POLICY_REGION`] [`--new-priority`=`NEW_PRIORITY`] [`--src-ip-ranges`=[`SRC_IP_RANGE`,…]] [`--target-secure-tags`=[`TARGET_SECURE_TAGS`,…]] [`--target-service-accounts`=[`TARGET_SERVICE_ACCOUNTS`,…]] [`--traffic-class`=`TRAFFIC_CLASS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute network-policies traffic-classification-rules update` is used to update network policy rules. 
EXAMPLES
     To update a rule with priority ``10`` in a network policy with name ``my-policy`` to change the description to ``new example rule``, run: 
    
    
    [gcloud alpha compute network-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-policies) traffic-classification-rules update --priority=10 --network-policy=my-policy --description="new example rule"

REQUIRED FLAGS
    

`--network-policy`=`NETWORK_POLICY`
     Network policy ID with which to update rule. 
`--priority`=`PRIORITY`
     Priority of the rule to be updated. Valid in [1, 2147482647]. 
OPTIONAL FLAGS
    

`--action`=`ACTION`
     Action to take if the request matches the match condition. `ACTION` must be (only one value is supported): `apply_traffic_classification`. 
`--description`=`DESCRIPTION`
     An optional, textual description for the rule. 
`--dest-address-groups`=[`DEST_ADDRESS_GROUP`,…]
     Destination address groups to match for this rule. 
`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]
     Destination IP ranges to match for this rule. 
`--[no-]disabled`
     Use this flag to disable the rule. Disabled rules will not affect traffic. Use `--disabled` to enable and `--no-disabled` to disable. 
`--dscp-mode`=`DSCP_MODE`
     When set to AUTO, the DSCP value will be picked automatically based on selected traffic class. Otherwise, DSCP value must be specified. `DSCP_MODE` must be one of: `auto`, `custom`. 
`--dscp-value`=`DSCP_VALUE`
     Custom DSCP value from 0-63 range. 
`--layer4-configs`=[`LAYER4_CONFIG`,…]
     A list of destination protocols and ports to which the network policy rule will apply. 
`--network-policy-region`=`NETWORK_POLICY_REGION`
     Region of the network policy to operate on. Overrides the default `compute/region` property value for this command invocation. 
`--new-priority`=`NEW_PRIORITY`
     New priority for the rule to update. Valid priority range: [1, 2147482647]. 
`--src-ip-ranges`=[`SRC_IP_RANGE`,…]
     CIDR IP address range. 
`--target-secure-tags`=[`TARGET_SECURE_TAGS`,…]
     An optional, list of target secure tags with a name of the format tagValues/ or full namespaced name 
`--target-service-accounts`=[`TARGET_SERVICE_ACCOUNTS`,…]
     List of target service accounts for the rule. 
`--traffic-class`=`TRAFFIC_CLASS`
     The traffic class that be applied to matching packet. `TRAFFIC_CLASS` must be one of: `tc1`, `tc2`, `tc3`, `tc4`, `tc5`, `tc6`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta compute network-policies](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-policies) traffic-classification-rules update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
