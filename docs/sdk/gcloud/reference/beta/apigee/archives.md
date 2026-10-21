---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/
title: gcloud beta apigee archives \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:31:22.879045+00:00
---

# gcloud beta apigee archives  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta apigee archives Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta apigee archives - manage Apigee archive deployments 
SYNOPSIS
    

`gcloud beta apigee archives` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Manage Apigee archive deployments. 
EXAMPLES
     To deploy a local archive deployment remotely to the management plane in the ``test`` environment, run: 
    
    
    [gcloud beta apigee archives deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/deploy) --environment=test

To list all archive deployments in the ``dev`` environment, run: 
    
    
    [gcloud beta apigee archives list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/list) --environment=dev

To describe the archive deployment with id ``abcdef01234`` in the ``demo`` environment of the ``my-org`` Apigee organization, run: 
    
    
    [gcloud beta apigee archives describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/describe) abcdef01234 --environment=demo --organization=my-org

To update the labels of the archive deployment with id ``uvxwzy56789`` in the ``test`` environment, run: 
    
    
    [gcloud beta apigee archives update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/update) uvxwzy56789 --environment=demo --update-labels=foo=1,bar=2

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/delete)`
     `(BETA)` Delete an Apigee archive deployment. 
`[deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/deploy)`
     `(BETA)` Deploy an Apigee archive deployment to an environment. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/describe)`
     `(BETA)` Describe an Apigee archive deployment. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/list)`
     `(BETA)` List Apigee archive deployments. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/update)`
     `(BETA)` Update an existing Apigee archive deployment. 
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha apigee archives](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
