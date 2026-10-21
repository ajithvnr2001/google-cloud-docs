---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/associations/delete/
title: gcloud alpha compute network-firewall-policies associations delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:19:56.406594+00:00
---

# gcloud alpha compute network-firewall-policies associations delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/associations/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute network-firewall-policies associations delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute network-firewall-policies associations delete - delete a new association between a firewall policy and an network or folder resource 
SYNOPSIS
    

`gcloud alpha compute network-firewall-policies associations delete` `--firewall-policy`=`FIREWALL_POLICY` `--name`=`NAME` [`--firewall-policy-region`=`FIREWALL_POLICY_REGION` | `--global-firewall-policy`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute network-firewall-policies associations delete` is used to delete network firewall policy associations. An network firewall policy is a set of rules that controls access to various resources. 
EXAMPLES
     To delete an association from a global network firewall policy with NAME ``my-policy`` and association name ``my-association``, run: 
    
    
    [gcloud alpha compute network-firewall-policies associations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/associations) delete --firewall-policy=my-policy --name=my-association --global-firewall-policy

To delete an association from a regional network firewall policy with NAME ``my-policy`` in region ``region-a`` and association name ``my-association``, run: 
    
    
    [gcloud alpha compute network-firewall-policies associations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/associations) delete --firewall-policy=my-policy --name=my-association --firewall-policy-region=region-a

REQUIRED FLAGS
    

`--firewall-policy`=`FIREWALL_POLICY`
     Firewall policy ID with which to delete association. 
`--name`=`NAME`
     Name of the association to delete. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--firewall-policy-region`=`FIREWALL_POLICY_REGION`
     Region of the firewall policy to delete. Overrides the default `compute/region` property value for this command invocation. 
`--global-firewall-policy`
     If set, the firewall policy is global. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute network-firewall-policies associations delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/delete)
    
    
    [gcloud beta compute network-firewall-policies associations delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/associations/delete)
    
    
    [gcloud preview compute network-firewall-policies associations](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/associations) delete

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
