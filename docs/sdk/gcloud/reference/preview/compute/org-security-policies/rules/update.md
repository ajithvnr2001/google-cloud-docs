---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/rules/update/
title: gcloud preview compute org-security-policies rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:06:11.611045+00:00
---

# gcloud preview compute org-security-policies rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute org-security-policies rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute org-security-policies rules update - update a Compute Engine security policy rule 
SYNOPSIS
    

`gcloud preview compute org-security-policies rules update` `PRIORITY` `--security-policy`=`SECURITY_POLICY` [`--action`=`ACTION`] [`--cloud-armor`] [`--description`=`DESCRIPTION`] [`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]] [`--direction`=`DIRECTION`] [`--[no-]enable-logging`] [`--layer4-configs`=[`LAYER4_CONFIG`,…]] [`--new-priority`=`NEW_PRIORITY`] [`--organization`=`ORGANIZATION`] [`--[no-]preview`] [`--target-resources`=[`TARGET_RESOURCES`,…]] [`--target-service-accounts`=[`TARGET_SERVICE_ACCOUNTS`,…]] [`--expression`=`EXPRESSION` | `--src-ip-ranges`=[`SRC_IP_RANGE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute org-security-policies rules update` is used to update organization security policy rules. 
EXAMPLES
     To update a rule with priority ``10`` in an organization security policy with ID ``123456789`` to change the action to ``allow`` and description to ``new-example-rule``, run: 
    
    
    gcloud preview compute org-security-policies rules update 10 --security-policy=123456789 --action=allow --description=new-example-rule

POSITIONAL ARGUMENTS
    

`PRIORITY`
     Priority of the security policy rule to update. 
REQUIRED FLAGS
    

`--security-policy`=`SECURITY_POLICY`
     short name of the security policy into which the rule should be updated. 
OPTIONAL FLAGS
    

`--action`=`ACTION`
     Action to take if the request matches the match condition. `ACTION` must be one of: 

`allow`
     Allows the request from HTTP(S) Load Balancing. 
`deny`
     (DEPRECATED) Only used for Hierarchical Firewalls. 
`deny-403`
     Denies the request from HTTP(S) Load Balancing, with an HTTP response status code of 403. 
`deny-404`
     Denies the request from HTTP(S) Load Balancing, with an HTTP response status code of 404. 
`deny-502`
     Denies the request from HTTP(S) Load Balancing, with an HTTP response status code of 502. 
`goto-next`
     Defers enforcement to the next policy in the hierarchy. 
`redirect`
     Redirects the request from HTTP(S) Load Balancing, based on redirect options. 
`--cloud-armor`
     Specified for Hierarchical Cloud Armor rules. 
`--description`=`DESCRIPTION`
     An optional, textual description for the rule. 
`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]
     Destination IP ranges to match for this rule. Can only be specified if DIRECTION is egress. 
`--direction`=`DIRECTION`
     Direction of the traffic the rule is applied. The default is to apply on incoming traffic. `DIRECTION` must be one of: `INGRESS`, `EGRESS`. 
`--[no-]enable-logging`
     Use this flag to enable logging of connections that allowed or denied by this rule. Use `--enable-logging` to enable and `--no-enable-logging` to disable. 
`--layer4-configs`=[`LAYER4_CONFIG`,…]
     A list of destination protocols and ports to which the firewall rule will apply. 
`--new-priority`=`NEW_PRIORITY`
     New priority for the rule to update. Valid in [0, 65535]. 
`--organization`=`ORGANIZATION`
     Organization which the organization security policy belongs to. Must be set if SECURITY_POLICY is short name. 
`--[no-]preview`
     If specified, the action will not be enforced. Use `--preview` to enable and `--no-preview` to disable. 
`--target-resources`=[`TARGET_RESOURCES`,…]
     List of URLs of target resources to which the rule is applied. 
`--target-service-accounts`=[`TARGET_SERVICE_ACCOUNTS`,…]
     List of target service accounts for the rule. 
Security policy rule matcher. 

At most one of these can be specified: 

`--expression`=`EXPRESSION`
     The Cloud Armor rules language expression to match for this rule. 
`--src-ip-ranges`=[`SRC_IP_RANGE`,…]
     The source IPs/IP ranges to match for this rule. To match all IPs specify *. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute org-security-policies rules update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/rules/update)
    
    
    [gcloud alpha compute org-security-policies rules update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies/rules/update)
    
    
    [gcloud beta compute org-security-policies rules update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/org-security-policies/rules/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
