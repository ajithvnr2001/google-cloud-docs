---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/set-iam-policy/
title: gcloud beta compute firewall-policies set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:18.277042+00:00
---

# gcloud beta compute firewall-policies set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute firewall-policies set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute firewall-policies set-iam-policy - set the IAM policy for a Compute Engine organization firewall policy 
SYNOPSIS
    

`gcloud beta compute firewall-policies set-iam-policy` `FIREWALL_POLICY` `POLICY_FILE` [`--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Sets the IAM policy for the given organization firewall policy as defined in a JSON or YAML file. 
EXAMPLES
     The following command will read an IAM policy defined in a JSON file 'policy.json' and set it for the organization firewall policy `my-policy`: 
    
    
    gcloud beta compute firewall-policies set-iam-policy my-policy policy.json --organization=123456789

To set the IAM policy for the organization firewall policy with numeric ID `987654321`, run: 
    
    
    gcloud beta compute firewall-policies set-iam-policy 987654321 policy.json

See <https://cloud.google.com/iam/docs/managing-policies> for details of the policy file format and contents. 

POSITIONAL ARGUMENTS
    

`FIREWALL_POLICY`
     Short name or ID of the firewall policy to set IAM policy. 
`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

FLAGS
    

`--organization`=`ORGANIZATION`
     Organization ID in which the organization firewall policy is to be set. Must be set if FIREWALL_POLICY is short name. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute firewall-policies set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/set-iam-policy)
    
    
    [gcloud alpha compute firewall-policies set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/set-iam-policy)
    
    
    [gcloud preview compute firewall-policies set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
