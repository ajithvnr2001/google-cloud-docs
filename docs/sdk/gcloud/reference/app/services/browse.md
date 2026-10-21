---
url: https://docs.cloud.google.com/sdk/gcloud/reference/app/services/browse/
title: gcloud app services browse \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:51:34.073646+00:00
---

# gcloud app services browse  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/app/services/browse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud app services browse Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud app services browse - open the specified service(s) in a browser 
SYNOPSIS
    

`gcloud app services browse` `SERVICES` [`SERVICES` …] [`--no-launch-browser`] [`--version`=`VERSION`, `-v` `VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Open the specified service(s) in a browser. 
EXAMPLES
     To show the url for the default service in the browser, run: 
    
    
    gcloud app services browse default

To show version `v1` of service `myService` in the browser, run: 
    
    
    gcloud app services browse myService --version="v1"

To show multiple services side-by-side, run: 
    
    
    gcloud app services browse default otherService

To show multiple services side-by-side with a specific version, run: 
    
    
    gcloud app services browse s1 s2 --version=v1

POSITIONAL ARGUMENTS
    

`SERVICES` [`SERVICES` …]
     The services to open (optionally filtered by the --version flag). 
FLAGS
    

`--launch-browser`
     Launch a browser if possible. When disabled, only displays the URL. Enabled by default, use `--no-launch-browser` to disable. 
`--version`=`VERSION`, `-v` `VERSION`
     If specified, open services with a given version. If not specified, use a version based on the service's traffic split . 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta app services browse](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/services/browse)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
