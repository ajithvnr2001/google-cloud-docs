---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/update/
title: gcloud alpha compute firewall-policies mirroring-rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:13.167273+00:00
---

# gcloud alpha compute firewall-policies mirroring-rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute firewall-policies mirroring-rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute firewall-policies mirroring-rules update - updates a Compute Engine firewall policy packet mirroring rule 
SYNOPSIS
    

`gcloud alpha compute firewall-policies mirroring-rules update` `PRIORITY` `--firewall-policy`=`FIREWALL_POLICY` [`--action`=`ACTION`] [`--description`=`DESCRIPTION`] [`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]] [`--direction`=`DIRECTION`] [`--[no-]disabled`] [`--layer4-configs`=[`LAYER4_CONFIG`,…]] [`--new-priority`=`NEW_PRIORITY`] [`--organization`=`ORGANIZATION`] [`--security-profile-group`=`SECURITY_PROFILE_GROUP`] [`--src-ip-ranges`=[`SRC_IP_RANGE`,…]] [`--target-resources`=[`TARGET_RESOURCES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute firewall-policies mirroring-rules update` is used to update organization firewall policy packet mirroring rules. 
EXAMPLES
     To update a rule with priority ``10" in an organization firewall policy with ID ``123456789" to change the action to ``allow" and description to ``new-example-rule", run: 
    
    
    gcloud alpha compute firewall-policies mirroring-rules update 10 --firewall-policy=123456789 --action=do_not_mirror --description=new-example-rule

POSITIONAL ARGUMENTS
    

`PRIORITY`
     Priority of the firewall policy rule to update. 
REQUIRED FLAGS
    

`--firewall-policy`=`FIREWALL_POLICY`
     Short name of the firewall policy into which the rule should be updated. 
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
     Use this flag to disable the rule. Disabled rules will not affect traffic. Use `--disabled` to disable and `--no-disabled` to enable. 
`--layer4-configs`=[`LAYER4_CONFIG`,…]
     A list of destination protocols and ports to which the firewall rule will apply. 
`--new-priority`=`NEW_PRIORITY`
     New priority for the rule to update. Valid in [0, 65535]. 
`--organization`=`ORGANIZATION`
     Organization which the organization firewall policy belongs to. Must be set if FIREWALL_POLICY is short name. 
`--security-profile-group`=`SECURITY_PROFILE_GROUP`
     An org-based security profile group to be used with mirror action. Allowed formats are: a) http(s)://<namespace>/<api>/organizations/<org_id>/locations/global/securityProfileGroups/<profile> b) (//)<namespace>/organizations/<org_id>/locations/global/securityProfileGroups/<profile> c) <profile>. In case "c" `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI will create a reference matching format "a", but to make it work CLOUDSDK_API_ENDPOINT_OVERRIDES_NETWORKSECURITY property must be set. In order to set this property, please run the command `gcloud config set api_endpoint_overrides/networksecurity https://<namespace>/`. 
`--src-ip-ranges`=[`SRC_IP_RANGE`,…]
     Source IP ranges to match for this rule. 
`--target-resources`=[`TARGET_RESOURCES`,…]
     List of URLs of target resources to which the rule is applied. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta compute firewall-policies mirroring-rules update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/mirroring-rules/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
