---
url: https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/create/
title: gcloud config configurations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:35.975374+00:00
---

# gcloud config configurations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud config configurations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud config configurations create - creates a new named configuration 
SYNOPSIS
    

`gcloud config configurations create` `CONFIGURATION_NAME` [`--no-activate`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a new named configuration. 

Except for special cases (NONE), configuration names start with a lower case letter and contain only lower case letters a-z, digits 0-9, and hyphens '-'. 

See `[gcloud topic configurations](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations. 

EXAMPLES
     To create a new named configuration, run: 
    
    
    gcloud config configurations create my-config

POSITIONAL ARGUMENTS
    

`CONFIGURATION_NAME`
     Name of the configuration to create 
FLAGS
    

`--activate`
     If true, activate this configuration upon create. Enabled by default, use `--no-activate` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha config configurations create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/config/configurations/create)
    
    
    [gcloud beta config configurations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/config/configurations/create)
    
    
    [gcloud preview config configurations create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/config/configurations/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
