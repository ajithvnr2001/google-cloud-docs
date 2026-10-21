---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/applications/describe/
title: gcloud apigee applications describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:44.896461+00:00
---

# gcloud apigee applications describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/applications/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apigee applications describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apigee applications describe - describe an Apigee application 
SYNOPSIS
    

`gcloud apigee applications describe` (`APPLICATION` : `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe an Apigee application. 

`gcloud apigee applications describe` retrieves the application's details, including its developer, credentials, API products, and other information. 

EXAMPLES
     To describe an application for the active Cloud Platform project whose UUID is ``46d6151e-0000-4dfa-b9c7-c03b8b58bb2f``, run: 
    
    
    gcloud apigee applications describe 46d6151e-0000-4dfa-b9c7-c03b8b58bb2f

To describe that application in the Apigee organization ``my-org``, formatted as a JSON object, run: 
    
    
    gcloud apigee applications describe 46d6151e-0000-4dfa-b9c7-c03b8b58bb2f --organization=my-org --format=json

POSITIONAL ARGUMENTS
    

Application resource - Application to be described. To get a list of available applications, run `[gcloud apigee applications list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/applications/list)`. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`APPLICATION`
     ID of the application or fully qualified identifier for the application. 

To set the `app` attribute: 

  * provide the argument `APPLICATION` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     Apigee organization containing the application. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `APPLICATION` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha apigee applications describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe)
    
    
    [gcloud beta apigee applications describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/applications/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
