---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/attachments/groups/update/
title: gcloud beta compute interconnects attachments groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:51.668761+00:00
---

# gcloud beta compute interconnects attachments groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/attachments/groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute interconnects attachments groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute interconnects attachments groups update - update a Compute Engine interconnect attachment group 
SYNOPSIS
    

`gcloud beta compute interconnects attachments groups update` `NAME` [`--attachments`=[`INTERCONNECT_ATTACHMENT`,…]] [`--description`=`DESCRIPTION`] [`--intended-availability-sla`=`INTENDED_AVAILABILITY_SLA`] [`--update-mask`=`UPDATE_MASK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute interconnects attachments groups update` is used to update interconnect attachment groups. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To update an interconnect attachment group example-attachment-group's intended availability SLA to PRODUCTION_CRITICAL, run: 
    
    
    gcloud beta compute interconnects attachments groups update example-attachment-group --intended-availability-sla=PRODUCTION_CRITICAL

To update an interconnect attachment group example-attachment-group's description to "example attachment group description", run: 
    
    
    gcloud beta compute interconnects attachments groups update example-attachment-group --description="example attachment group description"

To update an interconnect attachment group example-attachment-group's member attachments to attachment-1 and attachment-2, run: 
    
    
    gcloud beta compute interconnects attachments groups update example-attachment-group --attachments=region-1/attachment-1,region-2/attachment-2 --update-mask=attachments

Although you can add or remove member attachments using this command, it is recommended to add or remove member attachments using the `add-members` and `remove-members` commands. 

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect attachment group to update. 
FLAGS
    

`--attachments`=[`INTERCONNECT_ATTACHMENT`,…]
     Member interconnect attachments to add to the interconnect attachment group initially. 
`--description`=`DESCRIPTION`
     An optional, textual description for the interconnect attachment group. 
`--intended-availability-sla`=`INTENDED_AVAILABILITY_SLA`
     The availability SLA that the user intends this group to support. 
`--update-mask`=`UPDATE_MASK`
     Optional update mask to specify which fields to update. Use commas to separate masks. If not specified, all fields present in the command will be updated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute interconnects attachments groups update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/update)
    
    
    [gcloud alpha compute interconnects attachments groups update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups/update)
    
    
    [gcloud preview compute interconnects attachments groups update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
