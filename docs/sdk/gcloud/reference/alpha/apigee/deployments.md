---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/
title: gcloud alpha apigee deployments \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:49.941837+00:00
---

# gcloud alpha apigee deployments  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apigee deployments Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apigee deployments - manage deployments of Apigee API proxies in runtime environments 
SYNOPSIS
    

`gcloud alpha apigee deployments` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage deployments of Apigee API proxies in runtime environments. 

`gcloud alpha apigee deployments` contains commands for enumerating and checking the status of deployments of proxies to runtime environments. 

EXAMPLES
     To list all deployments for the active Cloud Platform project, run: 
    
    
    [gcloud alpha apigee deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/list)

To list all deployments in a particular environment of a particular Apigee organization, run: 
    
    
    [gcloud alpha apigee deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/list) --environment=ENVIRONMENT --organization=ORG_NAME

To get the status of a specific deployment as a JSON object, run: 
    
    
    [gcloud alpha apigee deployments describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe) --api=API_NAME --environment=ENVIRONMENT --format=json

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe)`
     `(ALPHA)` Describe an Apigee API proxy deployment. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/list)`
     `(ALPHA)` List Apigee API proxy deployments. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud apigee deployments](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments)
    
    
    [gcloud beta apigee deployments](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
