---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/groups/create/
title: gcloud preview compute interconnects groups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:37.191364+00:00
---

# gcloud preview compute interconnects groups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute interconnects groups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute interconnects groups create - create a Compute Engine interconnect group 
SYNOPSIS
    

`gcloud preview compute interconnects groups create` `NAME` `--intended-topology-capability`=`INTENDED_TOPOLOGY_CAPABILITY` [`--description`=`DESCRIPTION`] [`--interconnects`=[`INTERCONNECT`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute interconnects groups create` is used to create interconnect groups. An interconnect group connects a set of redundant interconnects between Google and the customer. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To create an interconnect group capable of PRODUCTION_CRITICAL, run: 
    
    
    gcloud preview compute interconnects groups create example-interconnect-group --intended-topology-capability=PRODUCTION_CRITICAL --description="Example interconnect group"

It is easy to add members to an existing interconnect group after creation using the `add-members` command. 

To create an interconnect group capable of PRODUCTION_NON_CRITICAL, with two members at creation time, run: 
    
    
    gcloud preview compute interconnects groups create example-interconnect-group --intended-topology-capability=PRODUCTION_NON_CRITICAL --interconnects=interconnect-1,interconnect-2

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect group to create. 
REQUIRED FLAGS
    

`--intended-topology-capability`=`INTENDED_TOPOLOGY_CAPABILITY`
     The reliability the user intends this group to be capable of, in terms of the Interconnect product SLAs. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the interconnect group. 
`--interconnects`=[`INTERCONNECT`,…]
     Member interconnects to add to the interconnect group initially. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute interconnects groups create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create)
    
    
    [gcloud alpha compute interconnects groups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create)
    
    
    [gcloud beta compute interconnects groups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/groups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
