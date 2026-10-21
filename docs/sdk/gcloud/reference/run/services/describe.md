---
url: https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe/
title: gcloud run services describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:08:00.924931+00:00
---

# gcloud run services describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud run services describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud run services describe - obtain details about a given service 
SYNOPSIS
    

`gcloud run services describe` (`SERVICE` : `--namespace`=`NAMESPACE`) [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Obtain details about a given service. 
EXAMPLES
     To obtain details about a given service: 
    
    
    gcloud run services describe <service-name>

To get those details in the YAML format: 
    
    
    gcloud run services describe <service-name> --format=yaml

To get them in YAML format suited to export (omitting metadata specific to this deployment and status info): 
    
    
    gcloud run services describe <service-name> --format=export

POSITIONAL ARGUMENTS
    

Service resource - Service to describe. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`SERVICE`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `SERVICE` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--namespace`=`NAMESPACE`
     Specific to Cloud Run for Anthos: Kubernetes namespace for the service. 

To set the `namespace` attribute: 

  * provide the argument `SERVICE` on the command line with a fully specified name; 
  * provide the argument `--namespace` on the command line; 
  * set the property `run/namespace`; 
  * For Cloud Run on Kubernetes Engine, defaults to "default". Otherwise, defaults to project ID.; 
  * provide the argument `project` on the command line; 
  * set the property `core/project`. 


FLAGS
    

`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha run services describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/describe)
    
    
    [gcloud beta run services describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/services/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
