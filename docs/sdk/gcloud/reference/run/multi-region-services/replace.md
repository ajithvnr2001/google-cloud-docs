---
url: https://docs.cloud.google.com/sdk/gcloud/reference/run/multi-region-services/replace/
title: gcloud run multi-region-services replace \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:04.089162+00:00
---

# gcloud run multi-region-services replace  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/run/multi-region-services/replace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud run multi-region-services replace Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud run multi-region-services replace - create or Update multi-region service from YAML 
SYNOPSIS
    

`gcloud run multi-region-services replace` [`FILE`] [`--async`] [`--dry-run`] [`--region`=`REGION`] [`--regions`=`REGIONS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates or replaces a service from a YAML service specification. 
EXAMPLES
     To replace the specification for a service defined in myservice.yaml 
    
    
    gcloud run multi-region-services replace myservice.yaml

POSITIONAL ARGUMENTS
    

[`FILE`]
     The absolute path to the YAML file with a Knative service definition for the service to update or deploy. Defaults to `service.yaml` if not specified. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--dry-run`
     If set to true, only validates the configuration. The configuration is not applied. 
`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
`--regions`=`REGIONS`
     Comma-separated list of regions in which the multi-region Service can be found. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha run multi-region-services replace](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/replace)
    
    
    [gcloud beta run multi-region-services replace](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/multi-region-services/replace)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
