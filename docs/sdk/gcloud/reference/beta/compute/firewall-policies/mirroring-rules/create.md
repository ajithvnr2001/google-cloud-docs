---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/mirroring-rules/create/
title: gcloud beta compute firewall-policies mirroring-rules create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:55.536623+00:00
---

# gcloud beta compute firewall-policies mirroring-rules create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/mirroring-rules/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute firewall-policies mirroring-rules create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute firewall-policies mirroring-rules create - creates a Compute Engine firewall policy packet mirroring rule 
SYNOPSIS
    

`gcloud beta compute firewall-policies mirroring-rules create` `PRIORITY` `--action`=`ACTION` `--firewall-policy`=`FIREWALL_POLICY` `--layer4-configs`=[`LAYER4_CONFIG`,…] [`--description`=`DESCRIPTION`] [`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]] [`--direction`=`DIRECTION`] [`--[no-]disabled`] [`--organization`=`ORGANIZATION`] [`--security-profile-group`=`SECURITY_PROFILE_GROUP`] [`--src-ip-ranges`=[`SRC_IP_RANGE`,…]] [`--target-resources`=[`TARGET_RESOURCES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute firewall-policies mirroring-rules create` is used to create organization firewall policy packet mirroring rules. 
EXAMPLES
     To create a packet mirroring rule with priority ``10" in an organization firewall policy with ID ``123456789", run: 
    
    
    gcloud beta compute firewall-policies mirroring-rules create 10 --firewall-policy=123456789 --action=mirror --security-profile-group=organizations/123/locations/global/securityProfileGroups/custom-security-profile-group --description=example-rule

POSITIONAL ARGUMENTS
    

`PRIORITY`
     Priority of the firewall policy rule to create. 
REQUIRED FLAGS
    

`--action`=`ACTION`
     Action to take if the request matches the match condition. `ACTION` must be one of: `mirror`, `do_not_mirror`, `goto_next`. 
`--firewall-policy`=`FIREWALL_POLICY`
     Short name of the firewall policy into which the rule should be inserted. 
`--layer4-configs`=[`LAYER4_CONFIG`,…]
     A list of destination protocols and ports to which the firewall rule will apply. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the rule. 
`--dest-ip-ranges`=[`DEST_IP_RANGE`,…]
     Destination IP ranges to match for this rule. 
`--direction`=`DIRECTION`
     Direction of the traffic the rule is applied. The default is to apply on incoming traffic. `DIRECTION` must be one of: `INGRESS`, `EGRESS`. 
`--[no-]disabled`
     Use this flag to disable the rule. Disabled rules will not affect traffic. Use `--disabled` to disable and `--no-disabled` to enable. 
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
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha compute firewall-policies mirroring-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/mirroring-rules/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
