---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/describe/
title: gcloud apigee apis describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:44.776748+00:00
---

# gcloud apigee apis describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apigee apis describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apigee apis describe - describe an Apigee API proxy 
SYNOPSIS
    

`gcloud apigee apis describe` (`API` : `--organization`=`ORGANIZATION`) [`--verbose`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe an Apigee API proxy. 

`gcloud apigee apis describe` shows metadata about an API proxy and its revisions. 

EXAMPLES
     To describe an API proxy called ``proxy-name`` given that its matching Cloud Platform project has been set in gcloud settings, run: 
    
    
    gcloud apigee apis describe proxy-name

To describe an API proxy called ``other-proxy-name`` in another project whose Apigee organization is named ``org-name``, run: 
    
    
    gcloud apigee apis describe other-proxy-name --organization=org-name

To describe an API proxy called ``proxy-name`` and include details on its revisions, run: 
    
    
    gcloud apigee apis describe proxy-name --verbose

To describe an API proxy called ``proxy-name`` as a JSON object, run: 
    
    
    gcloud apigee apis describe proxy-name --format=json

POSITIONAL ARGUMENTS
    

API proxy resource - API proxy to be described. To get a list of available API proxies, run `[gcloud apigee apis list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/list)`. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`API`
     ID of the API proxy or fully qualified identifier for the API proxy. 

To set the `api` attribute: 

  * provide the argument `API` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     Apigee organization containing the API proxy. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `API` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


FLAGS
    

`--verbose`
     Include proxy revision info in the description. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha apigee apis describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/describe)
    
    
    [gcloud beta apigee apis describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
