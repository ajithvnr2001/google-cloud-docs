---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/test-iam-permissions/
title: gcloud beta compute firewall-policies test-iam-permissions \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:57.659356+00:00
---

# gcloud beta compute firewall-policies test-iam-permissions  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/test-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute firewall-policies test-iam-permissions Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute firewall-policies test-iam-permissions - test IAM permissions for a Compute Engine organization firewall policy 
SYNOPSIS
    

`gcloud beta compute firewall-policies test-iam-permissions` `FIREWALL_POLICY` `--permissions`=[`PERMISSION`,…] [`--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Returns permissions that a caller has on the specified organization firewall policy. 
EXAMPLES
     To test if the caller has `compute.firewallPolicies.get` permission on the organization firewall policy `my-policy` (under organization `123456789`), run: 
    
    
    gcloud beta compute firewall-policies test-iam-permissions my-policy --organization=123456789 --permissions=compute.firewallPolicies.get

To test if the caller has `compute.firewallPolicies.get` permission on the organization firewall policy with numeric ID `987654321`, run: 
    
    
    gcloud beta compute firewall-policies test-iam-permissions 987654321 --permissions=compute.firewallPolicies.get

POSITIONAL ARGUMENTS
    

`FIREWALL_POLICY`
     Short name or ID of the firewall policy to test IAM permissions. 
REQUIRED FLAGS
    

`--permissions`=[`PERMISSION`,…]
     The permissions to test. 
OPTIONAL FLAGS
    

`--organization`=`ORGANIZATION`
     Organization ID in which the organization firewall policy is to be described. Must be set if FIREWALL_POLICY is short name. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute firewall-policies test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/test-iam-permissions)
    
    
    [gcloud alpha compute firewall-policies test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/test-iam-permissions)
    
    
    [gcloud preview compute firewall-policies test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies/test-iam-permissions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
