---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-policies/traffic-classification-rules/describe/
title: gcloud alpha compute network-policies traffic-classification-rules describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:09:48.349285+00:00
---

# gcloud alpha compute network-policies traffic-classification-rules describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-policies/traffic-classification-rules/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute network-policies traffic-classification-rules describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute network-policies traffic-classification-rules describe - describes a Compute Engine network policy rule 
SYNOPSIS
    

`gcloud alpha compute network-policies traffic-classification-rules describe` `--network-policy`=`NETWORK_POLICY` `--priority`=`PRIORITY` [`--network-policy-region`=`NETWORK_POLICY_REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute network-policies traffic-classification-rules describe` is used to describe network policy rules. 
EXAMPLES
     To describe a rule with priority ``10`` in a network policy with name ``my-policy``, in region ``region-a``, run: 
    
    
    [gcloud alpha compute network-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-policies) traffic-classification-rules describe --priority=10 --network-policy=my-policy --network-policy-region=region-a

REQUIRED FLAGS
    

`--network-policy`=`NETWORK_POLICY`
     Network policy ID with which to describe rule. 
`--priority`=`PRIORITY`
     Priority of the rule to be described. Valid in [1, 2147483647]. 
OPTIONAL FLAGS
    

`--network-policy-region`=`NETWORK_POLICY_REGION`
     Region of the network policy to describe. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta compute network-policies](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-policies) traffic-classification-rules describe

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
