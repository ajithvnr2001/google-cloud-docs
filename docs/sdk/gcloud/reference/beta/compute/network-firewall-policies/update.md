---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/update/
title: gcloud beta compute network-firewall-policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:54:13.554633+00:00
---

# gcloud beta compute network-firewall-policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute network-firewall-policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute network-firewall-policies update - update a Compute Engine network firewall policy 
SYNOPSIS
    

`gcloud beta compute network-firewall-policies update` `FIREWALL_POLICY` [`--description`=`DESCRIPTION`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute network-firewall-policies update` is used to update network firewall policies. A network firewall policy is a set of rules that controls access to various resources. 
EXAMPLES
     To update a global network firewall policy with name ``my-policy``, to change the description to ``New description``, run: 
    
    
    gcloud beta compute network-firewall-policies update my-policy --description='New description' --global

To update a regional network firewall policy with name ``my-policy``, in region ``my-region``, to change the description to ``New description``, run: 
    
    
    gcloud beta compute network-firewall-policies update my-policy --description='New description' --region=my-region

POSITIONAL ARGUMENTS
    

`FIREWALL_POLICY`
     name of the network firewall policy to update. 
FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the network firewall policy. 
At most one of these can be specified: 

`--global`
     If set, the firewall policy is global. 
`--region`=`REGION`
     Region of the firewall policy to update. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute network-firewall-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/update)
    
    
    [gcloud alpha compute network-firewall-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/update)
    
    
    [gcloud preview compute network-firewall-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
