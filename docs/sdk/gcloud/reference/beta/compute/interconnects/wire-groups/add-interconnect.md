---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/wire-groups/add-interconnect/
title: gcloud beta compute interconnects wire-groups add-interconnect \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:40:43.848771+00:00
---

# gcloud beta compute interconnects wire-groups add-interconnect  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/wire-groups/add-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute interconnects wire-groups add-interconnect Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute interconnects wire-groups add-interconnect - add interconnect to a Compute Engine wire group 
SYNOPSIS
    

`gcloud beta compute interconnects wire-groups add-interconnect` `NAME` `--cross-site-network`=`CROSS_SITE_NETWORK` `--endpoint-label`=`ENDPOINT_LABEL` `--interconnect`=`INTERCONNECT` `--interconnect-label`=`INTERCONNECT_LABEL` `--vlan-tags`=`VLAN_TAGS` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute interconnects wire-groups add-interconnect` is used to add interconnects to a wire group. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To add an interconnect to a wire group, run: 
    
    
    gcloud beta compute interconnects wire-groups add-interconnect example-wg --cross-site-network=example-csn --endpoint-label=endpoint-1 --interconnect-label=interconnect-1 --interconnect=example-interconnect --vlan-tags=111

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the wire group to update. 
REQUIRED FLAGS
    

`--cross-site-network`=`CROSS_SITE_NETWORK`
     Name of the crossSiteNetwork to operate on. 
`--endpoint-label`=`ENDPOINT_LABEL`
     The endpoint label for the wire group. 
`--interconnect`=`INTERCONNECT`
     The interconnect for the wire group endpoint. 
`--interconnect-label`=`INTERCONNECT_LABEL`
     The interconnect label for the wire group endpoint. 
`--vlan-tags`=`VLAN_TAGS`
     The vlan tags for the interconnect on the wire group endpoint. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute interconnects wire-groups add-interconnect](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-interconnect)
    
    
    [gcloud alpha compute interconnects wire-groups add-interconnect](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/wire-groups/add-interconnect)
    
    
    [gcloud preview compute interconnects wire-groups add-interconnect](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/wire-groups/add-interconnect)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
