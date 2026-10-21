---
url: https://docs.cloud.google.com/sdk/gcloud/reference/run/compose/up/
title: gcloud run compose up \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:07:57.543687+00:00
---

# gcloud run compose up  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/run/compose/up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud run compose up Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud run compose up - deploy to Cloud Run from compose specification 
SYNOPSIS
    

`gcloud run compose up` [`COMPOSE_FILE`] [`--[no-]allow-unauthenticated`] [`--dry-run`] [`--region`=`REGION`] [`--build` | `--no-build`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Deploy to Cloud Run from compose specification. 

The below attribute in the Compose file specifies the service to be used as the ingress container in Cloud Run. Only one service can be designated as the ingress container. 
    
    
    x-google-cloudrun:
      ingress-container: true

EXAMPLES
     To deploy a container from the source Compose file on Cloud Run: 
    
    
    gcloud run compose up compose.yaml

To deploy to Cloud Run with unauthenticated access: 
    
    
    gcloud run compose up compose.yaml --allow-unauthenticated

POSITIONAL ARGUMENTS
    

[`COMPOSE_FILE`]
     The compose yaml file to deploy from a Compose directory to Cloud Run. 
FLAGS
    

`--[no-]allow-unauthenticated`
     Whether to enable allowing unauthenticated access to the service. This may take a few moments to take effect. Use `--allow-unauthenticated` to enable and `--no-allow-unauthenticated` to disable. 
`--dry-run`
     If set to true, only validates the configuration. The configuration is not applied. 
`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
At most one of these can be specified: 

`--build`
     Force build of images. 
`--no-build`
     Skip building from source if applicable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha run compose up](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/compose/up)
    
    
    [gcloud beta run compose up](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/compose/up)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
