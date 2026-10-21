---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/set-iam-policy/
title: gcloud preview compute network-firewall-policies set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:28:09.206844+00:00
---

# gcloud preview compute network-firewall-policies set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute network-firewall-policies set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute network-firewall-policies set-iam-policy - set the IAM policy binding for a Compute Engine network firewall policy 
SYNOPSIS
    

`gcloud preview compute network-firewall-policies set-iam-policy` `FIREWALL_POLICY` `POLICY_FILE` [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Sets the IAM policy for the given network firewall policy as defined in a JSON or YAML file. 
EXAMPLES
     The following command will read an IAM policy defined in a JSON file 'policy.json' and set it for the global network firewall policy `my-policy`: 
    
    
    gcloud preview compute network-firewall-policies set-iam-policy my-policy policy.json --global

The following command will read an IAM policy defined in a JSON file 'policy.json' and set it for the regional network firewall policy `my-policy` (in region `REGION`): 
    
    
    gcloud preview compute network-firewall-policies set-iam-policy my-policy policy.json --region=REGION

See <https://cloud.google.com/iam/docs/managing-policies> for details of the policy file format and contents. 

POSITIONAL ARGUMENTS
    

`FIREWALL_POLICY`
     name of the network firewall policy to set IAM policy. 
`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

FLAGS
    

At most one of these can be specified: 

`--global`
     If set, the firewall policy is global. 
`--region`=`REGION`
     Region of the firewall policy to get. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute network-firewall-policies set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/set-iam-policy)
    
    
    [gcloud alpha compute network-firewall-policies set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/set-iam-policy)
    
    
    [gcloud beta compute network-firewall-policies set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
