---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/datalineage/processes/create/
title: gcloud alpha datalineage processes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:16:24.064178+00:00
---

# gcloud alpha datalineage processes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/datalineage/processes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha datalineage processes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha datalineage processes create - create a Data Lineage process 
SYNOPSIS
    

`gcloud alpha datalineage processes create` (`PROCESS` : `--location`=`LOCATION`) [`--attributes`=[`ATTRIBUTES`,…]] [`--display-name`=`DISPLAY_NAME`] [`--origin-name`=`ORIGIN_NAME`] [`--origin-source-type`=`ORIGIN_SOURCE_TYPE`; default="custom"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Data Lineage process. 
EXAMPLES
     To create a process with ID `my-process` in location `us-central1` with display name `My Process` and origin `custom`, run: 
    
    
    gcloud alpha datalineage processes create my-process --location=us-central1 --display-name="My Process" --origin-source-type=custom --origin-name="my-app"

POSITIONAL ARGUMENTS
    

Process resource - The process to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `process` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`PROCESS`
     ID of the process or fully qualified identifier for the process. 

To set the `process` attribute: 

  * provide the argument `process` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the process. To set the `location` attribute: 

  * provide the argument `process` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--attributes`=[`ATTRIBUTES`,…]
     Additional attributes for the process. 
`--display-name`=`DISPLAY_NAME`
     A human-readable name for the process. 
`--origin-name`=`ORIGIN_NAME`
     The name of the origin (e.g. the application or pipeline name). 
`--origin-source-type`=`ORIGIN_SOURCE_TYPE`; default="custom"
     Type of the source. Use of a source type other than `custom` for process creation or updating is highly discouraged. It might be restricted in the future without notice. There will be increase in cost if you use any of the source types other than `custom`. `ORIGIN_SOURCE_TYPE` must be one of: `bigquery`, `composer`, `custom`, `dataflow`, `dataproc`, `data-fusion`, `looker-core`, `looker-studio`, `source-type-unspecified`, `vertex-ai`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datalineage/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud datalineage processes create](https://docs.cloud.google.com/sdk/gcloud/reference/datalineage/processes/create)
    
    
    [gcloud beta datalineage processes create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datalineage/processes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
