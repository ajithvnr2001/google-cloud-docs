---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reservations/blocks/describe/
title: gcloud preview compute reservations blocks describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:28:50.022716+00:00
---

# gcloud preview compute reservations blocks describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reservations/blocks/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute reservations blocks describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute reservations blocks describe - describe a Compute Engine reservation block 
SYNOPSIS
    

`gcloud preview compute reservations blocks describe` `RESERVATION` `--block-name`=`BLOCK_NAME` [`--full-view`=`FULL_VIEW`; default=`"BLOCK_VIEW_UNSPECIFIED"`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Describe a Compute Engine reservation block. 
EXAMPLES
     To describe a reservation block in reservation my-reservation in my-zone with block name my-reservation-block-0001, run: 
    
    
    gcloud preview compute reservations blocks describe my-reservation --zone=my-zone --block-name=my-reservation-block-0001

POSITIONAL ARGUMENTS
    

`RESERVATION`
     Name of the reservation to describe. 
REQUIRED FLAGS
    

`--block-name`=`BLOCK_NAME`
     The name of the reservation block. 
OPTIONAL FLAGS
    

`--full-view`=`FULL_VIEW`; default=`"BLOCK_VIEW_UNSPECIFIED"`
     The view type for the reservation block. `FULL_VIEW` must be one of: 

`BLOCK_VIEW_BASIC`
     Basic default view of the reservation block. 
`BLOCK_VIEW_FULL`
     Full detailed view of the reservation block. 
`--zone`=`ZONE`
     Zone of the reservation to describe. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute reservations blocks describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/describe)
    
    
    [gcloud alpha compute reservations blocks describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations/blocks/describe)
    
    
    [gcloud beta compute reservations blocks describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/blocks/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
