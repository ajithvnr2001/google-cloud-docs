---
url: https://docs.cloud.google.com/sdk/gcloud/reference/app/versions/stop/
title: gcloud app versions stop \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:40:54.972602+00:00
---

# gcloud app versions stop  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/app/versions/stop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud app versions stop Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud app versions stop - stop serving specified versions 
SYNOPSIS
    

`gcloud app versions stop` `VERSIONS` [`VERSIONS` …] [`--service`=`SERVICE`, `-s` `SERVICE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command stops serving the specified versions. It may only be used if the scaling module for your service has been set to manual. 
EXAMPLES
     To stop a specific version across all services, run: 
    
    
    gcloud app versions stop v1

To stop multiple named versions across all services, run: 
    
    
    gcloud app versions stop v1 v2

To stop a single version on a single service, run: 
    
    
    gcloud app versions stop --service=servicename v1

To stop multiple versions in a single service, run: 
    
    
    gcloud app versions stop --service=servicename v1 v2

Note that that last example may be more simply written using the `services stop` command (see its documentation for details). 

POSITIONAL ARGUMENTS
    

`VERSIONS` [`VERSIONS` …]
     The versions to stop (optionally filtered by the --service flag). 
FLAGS
    

`--service`=`SERVICE`, `-s` `SERVICE`
     If specified, only stop versions from the given service. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta app versions stop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/versions/stop)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
