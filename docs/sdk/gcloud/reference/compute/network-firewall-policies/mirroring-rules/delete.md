---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete/
title: gcloud compute network-firewall-policies mirroring-rules delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:47:23.757545+00:00
---

# gcloud compute network-firewall-policies mirroring-rules delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute network-firewall-policies mirroring-rules delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute network-firewall-policies mirroring-rules delete - deletes a Compute Engine network firewall policy packet mirroirng rule 
SYNOPSIS
    

`gcloud compute network-firewall-policies mirroring-rules delete` `PRIORITY` `--firewall-policy`=`FIREWALL_POLICY` `--global-firewall-policy` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute network-firewall-policies mirroring-rules delete` is used to delete network firewall policy packet mirroring rules. 
EXAMPLES
     To delete a rule with priority ``10`` in a global network firewall policy with name ``my-policy``, run: 
    
    
    gcloud compute network-firewall-policies mirroring-rules delete 10 --firewall-policy=my-policy --global-firewall-policy

POSITIONAL ARGUMENTS
    

`PRIORITY`
     Priority of the rule to be deleted. Valid in [0, 2147483547]. 
REQUIRED FLAGS
    

`--firewall-policy`=`FIREWALL_POLICY`
     Firewall policy ID with which to delete rule. 
`--global-firewall-policy`
     Use this flag to indicate that firewall policy is global. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute network-firewall-policies mirroring-rules](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/mirroring-rules) delete
    
    
    [gcloud beta compute network-firewall-policies mirroring-rules](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/mirroring-rules) delete
    
    
    [gcloud preview compute network-firewall-policies mirroring-rules](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/mirroring-rules) delete

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
