---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/config/configurations/delete/
title: gcloud beta config configurations delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:57.331391+00:00
---

# gcloud beta config configurations delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/config/configurations/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta config configurations delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta config configurations delete - deletes a named configuration 
SYNOPSIS
    

`gcloud beta config configurations delete` `CONFIGURATION_NAMES` [`CONFIGURATION_NAMES` …] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Deletes a named configuration. You cannot delete a configuration that is active, even when overridden with the --configuration flag. To delete the current active configuration, first `[gcloud config configurations activate](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/activate)` another one. 

See `[gcloud topic configurations](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations. 

EXAMPLES
     To delete an existing configuration named `my-config`, run: 
    
    
    gcloud beta config configurations delete my-config

To delete more than one configuration, run: 
    
    
    gcloud beta config configurations delete my-config1 my-config2

To list existing configurations, run: 
    
    
    [gcloud config configurations list](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/list)

POSITIONAL ARGUMENTS
    

`CONFIGURATION_NAMES` [`CONFIGURATION_NAMES` …]
     Name of the configuration to delete. Cannot be currently active configuration. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud config configurations delete](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/delete)
    
    
    [gcloud alpha config configurations delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/config/configurations/delete)
    
    
    [gcloud preview config configurations delete](https://docs.cloud.google.com/sdk/gcloud/reference/preview/config/configurations/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
