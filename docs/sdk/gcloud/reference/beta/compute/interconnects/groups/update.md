---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/groups/update/
title: gcloud beta compute interconnects groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:27:58.734183+00:00
---

# gcloud beta compute interconnects groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute interconnects groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute interconnects groups update - update a Compute Engine interconnect group 
SYNOPSIS
    

`gcloud beta compute interconnects groups update` `NAME` [`--description`=`DESCRIPTION`] [`--intended-topology-capability`=`INTENDED_TOPOLOGY_CAPABILITY`] [`--interconnects`=[`INTERCONNECT`,…]] [`--update-mask`=`UPDATE_MASK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute interconnects groups update` is used to update interconnect groups. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To update an interconnect group example-interconnect-group's intended topology capability to PRODUCTION_CRITICAL, run: 
    
    
    gcloud beta compute interconnects groups update example-interconnect-group --intended-topology-capability=PRODUCTION_CRITICAL

To update an interconnect group example-interconnect-group's description to "example interconnect group description", run: 
    
    
    gcloud beta compute interconnects groups update example-interconnect-group --description="example interconnect group description"

To update an interconnect group example-interconnect-group's member interconnects to interconnect-1 and interconnect-2, run: 
    
    
    gcloud beta compute interconnects groups update example-interconnect-group --interconnects=interconnect-1,interconnect-2 --update-mask=interconnects

Although you can add or remove member interconnects using this command, it is recommended to add or remove member interconnects using the `add-members` and `remove-members` commands. 

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect group to update. 
FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the interconnect group. 
`--intended-topology-capability`=`INTENDED_TOPOLOGY_CAPABILITY`
     The reliability the user intends this group to be capable of, in terms of the Interconnect product SLAs. 
`--interconnects`=[`INTERCONNECT`,…]
     Member interconnects to set the interconnect group to contain. 
`--update-mask`=`UPDATE_MASK`
     Optional update mask to specify which fields to update. Use commas to separate masks. If not specified, all fields present in the command will be updated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute interconnects groups update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/update)
    
    
    [gcloud alpha compute interconnects groups update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/update)
    
    
    [gcloud preview compute interconnects groups update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
