---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/
title: gcloud alpha apigee applications \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:49.048179+00:00
---

# gcloud alpha apigee applications  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apigee applications Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apigee applications - manage third-party applications which call Apigee API proxies 
SYNOPSIS
    

`gcloud alpha apigee applications` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage third-party applications which call Apigee API proxies. 

`gcloud alpha apigee applications` manages applications that want to use APIs exposed via Apigee. 

EXAMPLES
     To get the names and UUIDs of all applications in the active Cloud Platform project, run: 
    
    
    [gcloud alpha apigee applications list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list)

To get a JSON representation of an application in the active Cloud Platform project, including its API keys, run: 
    
    
    [gcloud alpha apigee applications describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe) APP_UUID --format=json

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe)`
     `(ALPHA)` Describe an Apigee application. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list)`
     `(ALPHA)` List Apigee applications. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud apigee applications](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/applications)
    
    
    [gcloud beta apigee applications](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/applications)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
