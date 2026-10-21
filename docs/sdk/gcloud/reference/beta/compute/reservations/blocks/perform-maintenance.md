---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/blocks/perform-maintenance/
title: gcloud beta compute reservations blocks perform-maintenance \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:12:22.863112+00:00
---

# gcloud beta compute reservations blocks perform-maintenance  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/blocks/perform-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute reservations blocks perform-maintenance Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute reservations blocks perform-maintenance - perform maintenance on a reservation block within a reservation 
SYNOPSIS
    

`gcloud beta compute reservations blocks perform-maintenance` `RESERVATION` `--block-name`=`BLOCK_NAME` [`--scope`=`SCOPE`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Perform maintenance on a reservation block within a reservation. 
EXAMPLES
     To perform maintenance on a reservation block in reservation my-reservation in my-zone with block name my-reservation-block-0001 with scope all, run: 
    
    
    gcloud beta compute reservations blocks perform-maintenance my-reservation --zone=my-zone --block-name=my-reservation-block-0001 --scope=all

POSITIONAL ARGUMENTS
    

`RESERVATION`
     Name of the reservation to perform-maintenance. 
REQUIRED FLAGS
    

`--block-name`=`BLOCK_NAME`
     The name of the reservation block. 
OPTIONAL FLAGS
    

`--scope`=`SCOPE`
     The maintenance scope to set for the reservation block. `SCOPE` must be one of: 

`all`
     Perform maintenance on all hosts in the reservation block. 
`running`
     Perform maintenance only on the hosts in the reservation block that have running VMs. 
`unused`
     Perform maintenance only on the hosts in the reservation block that don't have running VMs. 
`--zone`=`ZONE`
     Zone of the reservation to perform-maintenance. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute reservations blocks perform-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance)
    
    
    [gcloud alpha compute reservations blocks perform-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations/blocks/perform-maintenance)
    
    
    [gcloud preview compute reservations blocks perform-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reservations/blocks/perform-maintenance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
