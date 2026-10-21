---
url: https://docs.cloud.google.com/sdk/gcloud/reference/services/disable/
title: gcloud services disable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:44.499142+00:00
---

# gcloud services disable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/services/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud services disable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud services disable - disable a service for consumption for a project 
SYNOPSIS
    

`gcloud services disable` `SERVICE` [`SERVICE` …] [`--async`] [`--force`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command disables one or more previously-enabled services for consumption. 

To see a list of the enabled services for a project, run: 
    
    
    [gcloud services list](https://docs.cloud.google.com/sdk/gcloud/reference/services/list)

More information on listing services can be found at: <https://cloud.google.com/service-usage/docs/list-services> and on disabling a service at: <https://cloud.google.com/service-usage/docs/enable-disable>

EXAMPLES
     To disable a service called `my-consumed-service` for the active project, run: 
    
    
    gcloud services disable my-consumed-service

To run the same command asynchronously (non-blocking), run: 
    
    
    gcloud services disable my-consumed-service --async

POSITIONAL ARGUMENTS
    

`SERVICE` [`SERVICE` …]
     The name of the service(s) to disable. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--force`
     If specified, the disable call will proceed even if there are enabled services which depend on the service to be disabled or disable the service used in last 30 days or was enabled in recent 3 days. Forcing the call means that the services which depend on the service to be disabled will also be disabled. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha services disable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/disable)
    
    
    [gcloud beta services disable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/disable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
