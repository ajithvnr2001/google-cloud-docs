---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/config/configurations/describe/
title: gcloud alpha config configurations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:47:47.278571+00:00
---

# gcloud alpha config configurations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/config/configurations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha config configurations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha config configurations describe - describes a named configuration by listing its properties 
SYNOPSIS
    

`gcloud alpha config configurations describe` `CONFIGURATION_NAME` [`--all`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describes a named configuration by listing its properties. 

See `[gcloud topic configurations](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations. 

EXAMPLES
     To describe an existing configuration named `my-config`, run: 
    
    
    gcloud alpha config configurations describe my-config

This is similar to: 
    
    
    [gcloud config configurations activate](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/activate) my-config
    
    
    [gcloud config list](https://docs.cloud.google.com/sdk/gcloud/reference/config/list)

POSITIONAL ARGUMENTS
    

`CONFIGURATION_NAME`
     Name of the configuration to describe 
FLAGS
    

`--all`
     Include unset properties in output. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud config configurations describe](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/describe)
    
    
    [gcloud beta config configurations describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/config/configurations/describe)
    
    
    [gcloud preview config configurations describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/config/configurations/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
