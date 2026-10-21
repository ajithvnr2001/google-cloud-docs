---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/clone-rules/
title: gcloud alpha compute firewall-policies clone-rules \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:09.667651+00:00
---

# gcloud alpha compute firewall-policies clone-rules  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/clone-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute firewall-policies clone-rules Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute firewall-policies clone-rules - replace the rules of a Compute Engine organization firewall policy with rules from another policy 
SYNOPSIS
    

`gcloud alpha compute firewall-policies clone-rules` `FIREWALL_POLICY` `--source-firewall-policy`=`SOURCE_FIREWALL_POLICY` [`--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute firewall-policies clone-rules` is used to replace the rules of organization firewall policies. An organization firewall policy is a set of rules that controls access to various resources. 
EXAMPLES
     To clone the rules of an organization firewall policy with ID ``123456789", from another organization firewall policy with ID ``987654321", run: 
    
    
    gcloud alpha compute firewall-policies clone-rules 123456789 --source-firewall-policy=987654321

POSITIONAL ARGUMENTS
    

`FIREWALL_POLICY`
     Short name or ID of the firewall policy to clone the rules to. 
REQUIRED FLAGS
    

`--source-firewall-policy`=`SOURCE_FIREWALL_POLICY`
     The URL of the source firewall policy to copy the rules from. 
OPTIONAL FLAGS
    

`--organization`=`ORGANIZATION`
     Organization in which the organization firewall policy to copy the rules to. Must be set if firewall-policy is short name. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

IAM PERMISSIONS
     To clone rules to a firewall policy, the user must have the following permission: ``compute.firewallPolicies.cloneRules`. 

To find predefined roles that contain those permissions, see the [Compute Engine IAM roles](https://cloud.google.com/compute/docs/access/iam). 

`
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute firewall-policies clone-rules](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/clone-rules)
    
    
    [gcloud beta compute firewall-policies clone-rules](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/clone-rules)
    
    
    [gcloud preview compute firewall-policies clone-rules](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies/clone-rules)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
