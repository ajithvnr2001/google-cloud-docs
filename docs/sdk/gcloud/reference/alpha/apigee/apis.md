---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/
title: gcloud alpha apigee apis \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:48.280605+00:00
---

# gcloud alpha apigee apis  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apigee apis Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apigee apis - manage Apigee API proxies 
SYNOPSIS
    

`gcloud alpha apigee apis` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage Apigee API proxies. 
EXAMPLES
     To list all the API proxies in the active Cloud Platform project, run: 
    
    
    [gcloud alpha apigee apis list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/list)

To get details about a specific API proxy in a specific Apigee organization, run: 
    
    
    [gcloud alpha apigee apis describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/describe) PROXY_NAME --organization=ORG_NAME

To get a JSON object containing revision-level details about an API proxy, run: 
    
    
    [gcloud alpha apigee apis describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/describe) PROXY_NAME --verbose --format=json

To deploy the most recent revision of an API proxy into the ``eval`` deployment environment, run: 
    
    
    [gcloud alpha apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/deploy) --api=PROXY_NAME --environment=eval

To deploy the first revision of that API proxy into the ``release`` deployment environment, run: 
    
    
    [gcloud alpha apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/deploy) 1 --api=PROXY_NAME --environment=release

To undeploy whatever revision of PROXY_NAME is currently deployed in ENVIRONMENT, run: 
    
    
    [gcloud alpha apigee apis undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/undeploy) --api=PROXY_NAME --environment=ENVIRONMENT

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/delete)`
     `(ALPHA)` Delete an Apigee API proxy. 
`[deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/deploy)`
     `(ALPHA)` Deploy an Apigee API proxy to an environment. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/describe)`
     `(ALPHA)` Describe an Apigee API proxy. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/import)`
     `(ALPHA)` Import an Apigee API proxy from local files. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/list)`
     `(ALPHA)` List Apigee API proxies. 
`[undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/undeploy)`
     `(ALPHA)` Undeploy an Apigee API proxy from an environment. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud apigee apis](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis)
    
    
    [gcloud beta apigee apis](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
