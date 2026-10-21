---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/
title: gcloud apigee deployments \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:45.039322+00:00
---

# gcloud apigee deployments  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apigee deployments Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apigee deployments - manage deployments of Apigee API proxies in runtime environments 
SYNOPSIS
    

`gcloud apigee deployments` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage deployments of Apigee API proxies in runtime environments. 

`gcloud apigee deployments` contains commands for enumerating and checking the status of deployments of proxies to runtime environments. 

EXAMPLES
     To list all deployments for the active Cloud Platform project, run: 
    
    
    [gcloud apigee deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/list)

To list all deployments in a particular environment of a particular Apigee organization, run: 
    
    
    [gcloud apigee deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/list) --environment=ENVIRONMENT --organization=ORG_NAME

To get the status of a specific deployment as a JSON object, run: 
    
    
    [gcloud apigee deployments describe](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/describe) --api=API_NAME --environment=ENVIRONMENT --format=json

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/describe)`
     Describe an Apigee API proxy deployment. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/list)`
     List Apigee API proxy deployments. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha apigee deployments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments)
    
    
    [gcloud beta apigee deployments](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
